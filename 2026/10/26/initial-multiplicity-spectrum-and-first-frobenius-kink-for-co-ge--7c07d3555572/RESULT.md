# Initial multiplicity spectrum and first Frobenius kink for co-generated triples

## Finding

Let \(2\le a<b\) be coprime integers and put
\[
R_{a,b}(n)=\#\{(x,y,z)\in\mathbb Z_{\ge0}^{3}: ax+by+(a+b)z=n\},\qquad n\in\mathbb Z_{\ge0}.
\]
For every integer \(k\ge0\), let \(G_k=\#\{n\ge0:R_{a,b}(n)\le k\}\) and \(g_k=\max\{n\ge0:R_{a,b}(n)\le k\}\). For \(k\ge1\), let \(N_k=\#\{n\ge0:R_{a,b}(n)=k\}\).

**Theorem (complete first multiplicity phase and its first transition).** For every \(1\le k\le a\),
\[
N_k=a+b-k,\qquad
G_k=\frac{(a-1)(b-1)}2+k(a+b)-\frac{k(k+1)}2,\qquad
g_k=ab-a-b+bk.
\]
The zero-representation case is \(G_0=(a-1)(b-1)/2\) and \(g_0=ab-a-b\). At the next threshold,
\[
N_{a+1}=a,\qquad G_{a+1}=G_a+a,\qquad g_{a+1}=b(2a-1).
\]
Consequently the increments of the generalized Frobenius threshold satisfy
\[
g_k-g_{k-1}=b\quad(1\le k\le a),\qquad g_{a+1}-g_a=a,
\]
so the first change of increment is at \(k=a+1\) for every such pair \((a,b)\).

## Assumptions and scope

All summands and all counted arguments are nonnegative integers; ordered triples \((x,y,z)\) with the three *labeled* denominations \(a,b,a+b\) are counted. The denomination \(a+b\) is deliberately redundant for ordinary semigroup membership but not for multiplicity. The hypotheses \(2\le a<b\) and \(\gcd(a,b)=1\) are essential for the stated fundamental rectangle and the comparison \(b>a\). No assertion is made for \(k>a+1\), noncoprime pairs, or other third denominations. The maximum in \(g_k\) exists because the coefficients are positive, coprime, and the number of representations grows without bound.

## Proof

**Step 1: unique fundamental rectangle and representation formula.** The Chinese remainder theorem gives a unique pair \((u,v)\) with \(0\le u<b\), \(0\le v<a\), and
\[
n\equiv au+bv\pmod{ab}.
\]
Indeed \(u\equiv a^{-1}n\pmod b\), and \(v\equiv b^{-1}n\pmod a\). Write \(t=(n-au-bv)/(ab)\in\mathbb Z\). Since \(0\le au+bv<2ab\) and \(n\ge0\), necessarily \(t\ge-1\). The equation \(aU+bV=n\) has no nonnegative solution if \(t=-1\), while if \(t\ge0\), all its nonnegative solutions, without repetitions, are
\[
(U,V)=\bigl(u+bj,\ v+a(t-j)\bigr),\qquad 0\le j\le t.
\]
Each such \((U,V)\) corresponds bijectively to \(1+\min(U,V)\) triples \((x,y,z)\) by \(U=x+z\), \(V=y+z\). Thus
\[
R_{a,b}(n)=\sum_{j=0}^{t}\bigl(1+\min(u+bj,v+a(t-j))\bigr),\quad t\ge0,
\]
and \(R_{a,b}(n)=0\) for \(t=-1\).

**Step 2: low multiplicities exclude all higher layers.** At \(t=0\), the formula reduces to \(R_{a,b}(n)=1+\min(u,v)\). At \(t=1\), because \(u+b>v\),
\[
R_{a,b}(n)=2+v+\min(u,v+a).
\]
If this value is at most \(a+1\), then \(u<v+a\), since otherwise it is at least \(a+2\); therefore it equals \(u+v+2\), with \(u+v\le a-1\). Conversely every \(u,v\ge0\) with \(u+v\le a-1\) is inside the fundamental rectangle (because \(b>a\)) and yields this expression. For \(t\ge2\), the \(j=1\) summand is at least \(a+1\), because \(u+b\ge b>a\) and \(v+a(t-1)\ge a\); the two endpoint summands are each at least \(1\). Thus \(R_{a,b}(n)\ge a+3\). In particular only \(t=-1,0,1\) can contribute to \(R_{a,b}(n)\le a+1\).

**Step 3: exact multiplicity counts.** For \(1\le k\le a\), the \(t=0\) rectangle contains exactly \((b-k+1)+(a-k)=a+b-2k+1\) pairs with \(\min(u,v)=k-1\). The \(t=1\) triangle contains exactly \(k-1\) pairs with \(u+v=k-2\), where this count is zero for \(k=1\). Hence \(N_k=a+b-k\). At \(k=a+1\), no \(t=0\) pair remains, and the \(t=1\) diagonal \(u+v=a-1\) has \(a\) pairs; hence \(N_{a+1}=a\). Since the third generator is the sum of the other two, the nonrepresentable integers are precisely those not representable by \(a,b\). Sylvester's two-generator genus therefore yields \(G_0=(a-1)(b-1)/2\). Summing \(N_1,\ldots,N_k\) gives the asserted \(G_k\), and adding \(N_{a+1}=a\) gives \(G_{a+1}\).

**Step 4: exact largest low-multiplicity arguments.** The largest \(t=0\) argument with \(R_{a,b}(n)\le k\le a\) is attained at \((u,v)=(b-1,k-1)\), and equals
\[
T_k=a(b-1)+b(k-1)=ab-a-b+bk.
\]
The alternative boundary \((u,v)=(k-1,a-1)\) is smaller by \(k(b-a)>0\). For \(2\le k\le a\), the largest \(t=1\) argument with \(R_{a,b}(n)\le k\) has \(u+v=k-2\) and is maximized at \((u,v)=(0,k-2)\), giving \(ab+b(k-2)=T_k-(b-a)<T_k\). For \(k=1\) there is no eligible \(t=1\) argument. Any nonrepresentable argument is at most \(ab-a-b<T_k\). Therefore \(g_k=T_k\). At \(k=a+1\), every \(t=0\) argument has maximum \(2ab-a-b=g_a\), whereas the maximum eligible \(t=1\) argument is at \((u,v)=(0,a-1)\) and equals \(ab+b(a-1)=b(2a-1)=g_a+a\); no higher layer contributes. The stated \(g_{a+1}\) and increment comparison follow. \(\square\)

## Verification

The accompanying `verify.py` computes independent generating-function coefficients of \(\prod_{d\in\{a,b,a+b\}}(1-X^d)^{-1}\) using integer dynamic programming, compares them against the rectangle-layer formula at every integer in a finite certified test window, and checks all values \(N_k,G_k,g_k\) for \(0\le k\le a+1\). To reproduce: `python3 verify.py`. In the run reported here, the script returned `CERTIFICATE_OK pairs=575 exact_denumerant_values=952360`. This finite corroboration is not substituted for the preceding proof of the infinite theorem.

## Relationship to prior work

Aldrich, Gulbrandsen, and Keddy (arXiv:2610.20899, first submitted 14 October 2026) give general two-sided quasi-polynomial bounds for three-denomination denumerants and existence of generalized Frobenius numbers. Their inspected Theorem C and main sections do not give the present exact low-multiplicity counts or the first change of generalized Frobenius slope. Komatsu and Ying (Symmetry 2023, 15, 1328) provide exact generalized Frobenius and genus formulas for an *arithmetic progression* of three distinct denominations, not the co-generated triple \((a,b,a+b)\): since \(b=2a\) would be required for these three to form a progression in ascending order, and \(\gcd(a,b)=1\) with \(a\ge2\), the families are disjoint. Komatsu, Laishram, and Punyani (Symmetry 2023, 15, 852) give formulas for specific generalized Fibonacci-type triples; their recurrence constraints do not allow arbitrary coprime \((a,b)\). Standard general denumerant quasipolynomial algorithms can in principle compute each instance, but no inspected result supplied this uniform initial phase and first transition across all coprime pairs. The novelty comparison is best-knowledge, not a formal uniqueness certification.

## Limitations

The third denomination is redundant for membership but changes representation multiplicities. The theorem treats the natural first phase up to the first slope change, not all \(k\). General closed-form denumerant techniques, unindexed older calculations, or an undocumented special case could implicitly cover the formulas. Computational checks are finite; independent review has not been performed.

## References

1. M. Aldrich, D. Gulbrandsen, C. Keddy, *Enumerating Integral Points on Triangles in \(\mathbb R^3\)*, arXiv:2610.20899, first public version 14 October 2026, especially Theorem C and §3.2. https://arxiv.org/abs/2610.20899
2. T. Komatsu, H. Ying, *The \(p\)-Numerical Semigroup of the Triple of Arithmetic Progressions*, Symmetry 15 (2023), 1328, doi:10.3390/sym15071328. https://www.mdpi.com/2073-8994/15/7/1328
3. T. Komatsu, S. Laishram, P. Punyani, *\(p\)-Numerical Semigroups of Generalized Fibonacci Triples*, Symmetry 15 (2023), 852, doi:10.3390/sym15040852. https://arxiv.org/abs/2304.00443
4. T. Komatsu, J. Mu, *\(p\)-Numerical Semigroups of Triples from the Three-Term Recurrence Relations*, Axioms 13 (2024), 608; openly posted 24 July 2024. https://www.preprints.org/manuscript/202407.1982
