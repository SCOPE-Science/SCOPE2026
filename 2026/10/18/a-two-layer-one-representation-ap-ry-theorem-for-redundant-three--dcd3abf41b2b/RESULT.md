# A two-layer one-representation Apéry theorem for redundant three-coin systems

## Finding

Let integers \(2\le a<b\) be coprime and let \(1\le c<a\). Put \(d=a+cb\) and
\[R(N)=\#\{(x,y,z)\in\mathbb Z_{\ge0}^{3}:ax+by+dz=N\}.\]
For \(0\le j<a\), set
\[
T_j=\begin{cases}ab+bj,&0\le j<c,\\a+bj,&c\le j<a.\end{cases}
\]
Then the least integer in the residue class \(bj\pmod a\) with at least two representations is **exactly** \(T_j\); moreover, every larger integer in the same residue class has at least two representations. Consequently the one-Frobenius number, the one-genus, and the one-Sylvester sum are
\[
\boxed{g_1=ab-a+(c-1)b},\qquad
\boxed{n_1=cb+a-c+\frac{(a-1)(b-1)}2},
\]
\[
\boxed{s_1=\frac{1}{2a}\sum_{j=0}^{a-1}T_j^2-\frac12\sum_{j=0}^{a-1}T_j+\frac{a^2-1}{12}}.
\]
Here \(g_1\) is the largest \(N\ge0\) with \(R(N)\le1\), \(n_1\) counts such integers, including \(0\), and \(s_1\) sums their values. Thus these formulas evaluate three arithmetic invariants of an infinite three-denomination family, despite the third denomination being redundant for ordinary representability.

For a Pell-type recurrence \(P_0(u)=0\), \(P_1(u)=1\), \(P_{i+2}(u)=uP_{i+1}(u)+P_i(u)\), every integer \(u\ge2\), \(i\ge3\) gives a specialization with \(a=P_i(u)\), \(b=P_{i+1}(u)\), \(c=u\). This supplies the complete \(p=1\) Frobenius, genus and Sylvester-sum formulas for **three consecutive Pell-type terms**. At \(u=2,i=3\), the triple \((5,12,29)\) has \(g_1=67\) and \(n_1=49\).

## Assumptions and scope

The variables \(x,y,z\) are separately nonnegative integers. Distinct triples count as different representations, including when two triples give the same expression after replacing \(d\) by \(a+cb\). We require \(a<b\) and \(1\le c<a\); do not silently extend the displayed maximum formula beyond those bounds. All formulas concern exactly \(p=1\), rather than every \(p\). The residue \(bj\pmod a\) is interpreted through its unique representative in \(\{0,\ldots,a-1\}\).

## Proof

Let \(S=\langle a,b\rangle\), and let \(I=\{N\ge0:R(N)\ge2\}\). First establish the **two-certificate lemma**
\[
\boxed{I=(ab+S)\cup(d+S).}\tag{1}
\]
If \(N\in d+S\), writing \(N=d+ax+by\) supplies the two distinct triples \((x,y,1)\) and \((x+1,y+c,0)\). If \(N\in ab+S\), writing \(N=ab+ax+by\) supplies distinct triples \((x+b,y,0)\) and \((x,y+a,0)\). Conversely, suppose \(N\) has at least two representations. If one uses \(z\ge1\), subtracting \(d\) proves \(N\in d+S\). If all representations have \(z=0\), two different solutions of \(ax+by=N\) differ by a nonzero integer multiple of \((b,-a)\). Taking the solution with larger first coordinate shows that it has at least \(b\) units of the first coordinate, hence \(N-ab\in S\). This proves (1), with no assumptions on the number of representations above two.

For each \(j\in\{0,\ldots,a-1\}\), the least element of \(S\) in residue \(bj\pmod a\) is \(bj\). Indeed, a nonnegative representation in that residue has \(y\equiv j\pmod a\), so \(y\ge j\). Consequently the least element of \(ab+S\) in this residue is \(ab+bj\). For \(d+S\), the congruence \(d\equiv cb\pmod a\) gives least element \(a+cb+b((j-c)\bmod a)\): this equals \(a+bj\) when \(j\ge c\), and \(a+ab+bj\) when \(j<c\). Taking the smaller of the two thresholds proves the displayed \(T_j\) formula. As \(a\in S\), all subsequent integers in that residue belong to \(I\), establishing the complete one-Apéry classification.

The largest integer not in \(I\) in residue \(bj\) is \(T_j-a\). In the first block its maximum occurs at \(j=c-1\), with value \(ab-a+(c-1)b\). In the second block its maximum occurs at \(j=a-1\), with value \(b(a-1)\). Their difference is \(bc-a>0\), since \(b>a\) and \(c\ge1\). This proves the one-Frobenius formula.

Let \(r_j\) be the least nonnegative representative of \(bj\pmod a\). The exceptional integers in that residue are exactly \(r_j,r_j+a,\ldots,T_j-a\), comprising \((T_j-r_j)/a\) terms. Since multiplication by \(b\) permutes residues modulo \(a\), we have
\[\sum_jr_j=\frac{a(a-1)}2,\qquad \sum_jr_j^2=\frac{a(a-1)(2a-1)}6.\]
The displayed thresholds give
\[
\sum_jT_j=cab+(a-c)a+\frac{ba(a-1)}2.
\]
Substitution in \(n_1=\sum_j(T_j-r_j)/a\) yields the one-genus formula. Summing the same arithmetic progressions gives
\[
 s_1=\sum_j\left(\frac{T_j^2-r_j^2}{2a}-\frac{T_j-r_j}{2}\right),
\]
which simplifies to the stated Sylvester-sum formula. (The finite sum in that formula is explicit; no unknown Apéry values remain.)

Finally, recurrence subtraction gives \(\gcd(P_i(u),P_{i+1}(u))=1\), and for \(i\ge3\) one has \(P_i(u)>u\) and \(P_{i+1}(u)>P_i(u)\). The recurrence gives \(P_{i+2}(u)=P_i(u)+uP_{i+1}(u)\), so all hypotheses apply with \(c=u\). This completes the specialization.

## Verification

An independently implemented dynamic-programming convolution enumerates \(R(N)\) for every \(N\) in an explicit finite range above the predicted one-Frobenius number. The accompanying `verify.py` checks residue-by-residue membership in \(I\), the exact one-Frobenius number, the complete one-genus, and the one-Sylvester sum. It passes 2,791 coprime triples, 1,707,616 target comparisons, and seven separate Pell-type specializations. Run `python3 verify.py` with Python 3 standard library. The all-parameter result is **proved** above; these experiments are finite corroboration only.

## Relationship to prior work

Komatsu, Laishram and Punyani (2023, arXiv:2304.00443) compute generalized \(p\)-Frobenius quantities for Jacobsthal-polynomial triples of the form \(\{a,va+b,vaJ_{k-1}(v)+bJ_k(v)\}\). Komatsu and Mu (2023, arXiv:2307.08998) analyze \(\{P_i(u),P_{i+2}(u),P_{i+k}(u)\}\), not consecutive Pell-type triples \(\{P_i(u),P_{i+1}(u),P_{i+2}(u)\}\). Their general Apéry inversion formulas are compatible with the derivation here, but their specialized threshold structures do not imply the piecewise values \(T_j\) for \(\{a,b,a+cb\}\). In particular, the third generator is redundant for representability here, but not for the counted three-variable representations. The two-certificate ideal identity (1) is the added structural step.

## Limitations

The classification is restricted to one-representation thresholds and the stated coprimality/inequality assumptions. It does not determine \(p\)-Frobenius invariants for \(p\ge2\), nor does it cover nonconsecutive triples in the cited Pell papers. The representation-counting distinction between a redundant three-variable generator and the two-generator coin problem is essential. A differently phrased earlier theorem might imply this specialization; unindexed literature remains a residual originality risk. The mathematics has received self-review, not independent audit.

## References

1. T. Komatsu, S. Laishram and P. Punyani, *\(p\)-numerical semigroup of generalized Fibonacci triples*, arXiv:2304.00443, first public preprint April 2, 2023. https://arxiv.org/abs/2304.00443 .
2. T. Komatsu and J. Mu, *\(p\)-numerical semigroups of Pell triples*, arXiv:2307.08998, first public preprint July 18, 2023. https://arxiv.org/abs/2307.08998 .
