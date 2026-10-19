# Two-by-two sine-transform minor rigidity at odd prime powers

## Finding

For any odd prime \(p\ge5\), any integer \(k\ge1\), and \(N=p^k\), put \(m=(N-1)/2\) and
\[
(S_N)_{r,c}=\frac{2}{\sqrt N}\sin\left(\frac{2\pi rc}{N}\right),\qquad 1\le r,c\le m.
\]
For distinct rows \(r,s\in\{1,\ldots,m\}\) and distinct columns \(x,y\) in that set, the corresponding determinant vanishes **if and only if** at least one of the following conditions holds:

**(C), crossed-zero products:** both \((N\mid rx\ \text{or}\ N\mid sy)\) and \((N\mid ry\ \text{or}\ N\mid sx)\).

**(A), column congruence:** there is a *single* \(\varepsilon\in\{1,-1\}\) such that \(N\mid r(x-\varepsilon y)\) and \(N\mid s(x-\varepsilon y)\).

**(B), row congruence:** there is a *single* \(\varepsilon\in\{1,-1\}\) such that \(N\mid(r-\varepsilon s)x\) and \(N\mid(r-\varepsilon s)y\).

The conditions may overlap. Their union is exact, including indices divisible by \(p\); there are no further cyclotomic cancellations for \(p\ge5\).

Moreover, **for every odd prime \(p\ge3\)**, the total number of singular two-by-two submatrices of \(S_{p^2}\), counted by unordered row pairs and unordered column pairs, is
\[
Z_p=\frac{(p-1)^2(p-3)(8p^2-7p-3)}{64}.
\]
In particular \(Z_3=0\), \(Z_5=81\), \(Z_7=765\), and \(Z_{11}=11100\). As \(p\to\infty\), \(Z_p\sim p^5/8\), and the fraction of singular two-by-two minors is \(8p^{-3}(1+o(1))\). The \(p=3\) prime-square assertion concerns \(N=9\) only; no general claim is made about \(3^k\) for higher exponents.

## Assumptions and scope

These are the compressed Fourier sine matrices associated with inversion-odd functions on the cyclic group \(\mathbb Z/N\mathbb Z\), not the unrelated Dirichlet-boundary DST variants. The indexing set consists of the positive representatives of nonzero signed pairs. There is no restriction to primitive row or column indices. A minor is the determinant for two *distinct* rows and two *distinct* columns, with no positivity or principal-minor restriction. Divisibility is always in the ordinary integers. Overall row, column, and matrix normalizations are nonzero and do not affect singularity.

## Proof

**1. A short cyclotomic relation is formal at prime powers.** Let \(N=p^k\), \(p\ge5\), and let \(\zeta\) be a primitive \(N\)-th root of unity. For \(a\in\mathbb Z/N\mathbb Z\) write \(V_a(X)=X^a-X^{-a}\) in the group ring \(\mathbb Z[X]/(X^N-1)\). Vanishing of the two-by-two determinant is equivalent to
\[
P(\zeta)=0,\quad P(X)=V_{rx}(X)V_{sy}(X)-V_{ry}(X)V_{sx}(X).
\]
The reduced representative of \(P\) of degree less than \(N\) has integral coefficients, augmentation \(P(1)=0\), and coefficient \(\ell^1\)-norm at most eight. Since \(\Phi_{p^k}(X)=1+X^{p^{k-1}}+\cdots+X^{(p-1)p^{k-1}}\), the equality \(P(\zeta)=0\) forces \(P=\Phi_{p^k}Q\) with \(\deg Q<p^{k-1}\). Therefore each residue-class fiber of coefficients of \(P\) modulo \(p^{k-1}\) is constant, equal to the corresponding coefficient of \(Q\). If \(Q\) has at least two nonzero coefficients, then \(\|P\|_{\ell^1}\ge 2p>8\). If it has exactly one nonzero coefficient, \(P(1)=pQ(1)\ne0\), again impossible. More generally, if \(Q\ne0\), augmentation gives \(\sum Q_j=0\), hence at least two nonzero coefficients, and contradicts the length bound. Thus \(Q=0\) and \(P\) is identically zero in the group ring. This is the only step requiring \(p\ge5\).

**2. Formal products yield the three alternatives.** Let \(C_a=X^a+X^{-a}\). In the cyclic group ring,
\[
V_aV_b=C_{a+b}-C_{a-b}.
\]
Because \(N\) is odd, distinct classes \(\{a,-a\}\) have disjoint supports in these \(C\)-expressions; for \(a=0\), \(C_0=2\). The product \(V_aV_b\) is zero exactly when \(a=0\) or \(b=0\) modulo \(N\). If two such products are nonzero and equal, their positive \(C\) terms and negative \(C\) terms agree separately. Consequently for one pair of signs \(\varepsilon,\delta\in\{1,-1\}\),
\[
a+b\equiv\varepsilon(c+d),\qquad a-b\equiv\delta(c-d)\pmod N.
\]
Since two is invertible modulo odd \(N\), this says either \((a,b)\equiv\pm(c,d)\) or \((a,b)\equiv\pm(d,c)\), with a common sign in each pair. Apply this to \((a,b,c,d)=(rx,sy,ry,sx)\). The zero-products alternative becomes (C). The first nonzero-product matching becomes (A), and the second becomes (B). Each of (A), (B), and (C) conversely makes the formal determinant zero, proving the classification.

**3. Census at the prime square.** Now let \(N=p^2\), \(p\ge5\). Among \(1,\ldots,(p^2-1)/2\), precisely \(d=(p-1)/2\) indices are multiples of \(p\) (call them *divisible indices*), and \(u=pd\) are units. Put \(h=\binom d2\). Directly from (A)--(C), singular minors occur exactly in the following disjoint classes: both row and column pairs divisible (\(h^2\) choices); exactly one pair divisible, and the other pair mixed between divisible and unit (\(2hdu\) choices); exactly one pair divisible, and the other pair consists of units congruent up to sign modulo \(p\) (\(2h\,d\binom p2\) choices). Indeed, units in the half-interval form \(d\) signed residue classes modulo \(p\), each of size \(p\). The other pair patterns have neither a zero-product obstruction nor a shared signed congruence. Thus
\[
Z_p=h^2+2hd\left(u+\binom p2\right)
=h^2+4pd^2h
=\frac{(p-1)^2(p-3)(8p^2-7p-3)}{64}.
\]
For \(p=3\) the group-ring length argument does not apply, but \(S_9\) has no singular two-by-two minor by an exact finite-field certificate: reducing its unnormalized cyclotomic entries through a primitive ninth root modulo \(19\) produces a nonzero determinant for each of the \(\binom42^2=36\) minors. A complex algebraic zero would reduce to zero in that field because the cyclotomic relation is preserved; hence none is zero over \(\mathbb C\). This is reproducible by the included standard-library verifier. The displayed formula gives zero at \(p=3\), completing the census. Finally, the leading coefficient and total-pair count give the stated asymptotics.

## Verification

The file `verify_dst.py` is a standalone Python 3 standard-library verifier. Run `python verify_dst.py`. The recorded output is `verification_output.txt`. It uses exact modular cyclotomic computations, not floating-point sine evaluations. It enumerates every two-by-two minor in orders \(9,5,25,49,121,125\), compares the classification to vanishing/nonvanishing certificates, and verifies the prime-square census for \(9,25,49,121\). For a negative certificate, at least one reduction to an explicitly displayed finite field is nonzero. A putative complex zero would reduce to zero in every such field. The infinite prime-power classification is proved above; finite enumeration alone does not establish it.

## Relationship to prior work

Garcia--Karaali--Katz, *An improved uncertainty principle for functions with symmetry* (arXiv:1807.07648, first publicly posted 19 July 2018), establishes the odd cyclic discrete sine-transform framework and, in Theorem 1.3, the nonvanishing of **all** minors at prime order; it observes zero entries at odd composite orders. Neither assertion supplies the exact composite-prime-power two-by-two minor classification or its prime-square census. Christie--Dykema--Klep study low-weight vanishing sums of roots of unity, a general algebraic context for cyclotomic cancellations, rather than sine-matrix minor incidence. Results on ordinary uncompressed Fourier minors are not interchangeable with minors of this inversion-odd compression: the latter are alternating four-character combinations. The present claim is the exact arithmetic criterion and enumeration, not the general cyclotomic fact that roots of unity may cancel.

## Limitations

The full congruence classification is asserted for \(p\ge5\), not arbitrary composite \(N\) or prime powers of \(3\). At \(p=3\), only the separate \(N=9\) census is established. It does not classify three-by-three or larger minors or their determinant magnitudes. The finite checker is a reproducibility aid, not a substitute for the group-ring proof. Prior results under an equivalent alternative formulation in older harmonic-analysis or algebraic coding literature cannot be completely excluded by the present bibliographic search. Independent review has not been performed.

## References

1. S. R. Garcia, G. Karaali, D. J. Katz, *An improved uncertainty principle for functions with symmetry*, arXiv:1807.07648 (initially 19 July 2018), https://arxiv.org/html/1807.07648v4 ; especially Section 1.2 and Theorem 1.3.
2. L. Christie, K. J. Dykema, I. Klep, *Classifying minimal vanishing sums of roots of unity*, arXiv:2008.11268 (initially 25 August 2020), https://arxiv.org/html/2008.11268v2 .
3. T. Y. Lam, K. H. Leung, *On vanishing sums of roots of unity*, arXiv:math/9511209, https://arxiv.org/abs/math/9511209 .
