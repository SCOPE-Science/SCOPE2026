# Two repelling symmetry-forced 2-cycles for even Chebyshev maps
## Finding
For every even integer \(n\ge 18\), the odd real map
\[
Q_n(x)=\frac{x^{n+1}\left(n(n+1)(2n+1)x^{2n}+2n(n+1)x^n-n(n-1)\right)}{2\left((n+1)x^n+1\right)^3}
\]
has exactly two positive solutions \(x_-<x_+\) of \(Q_n(x)=-x\). If \(\widetilde c\) denotes its positive free critical point, so that
\[
\widetilde c^n=\frac{n-1}{(n+1)(2n+1)},
\]
then \(0<x_-<\widetilde c<x_+\). Both symmetric period-two orbits \(\{-x_-,x_-}\}\) and \(\{-x_+,x_+}\}\) are repelling.

For the Chebyshev map \(C_n\) associated with \(p_n(z)=z(z^n-1)\), each of the \(n/2\) odd-numbered invariant critical lines is conjugate to \(Q_n\). Hence \(C_n\) has exactly \(n\) centrally symmetric period-two cycles on those lines, two per line, and all are repelling.

## Assumptions and scope
The statement concerns even integers \(n\ge18\) and only centrally symmetric period-two cycles lying on the odd-numbered invariant critical lines. It does not classify arbitrary real, nonreal, or nonsymmetric period-two cycles, and it does not settle the source's open convergence question for even \(n\ge18\).

The source defines \(Q_n\), proves it is odd for even \(n\), identifies the positive critical point \(\widetilde c\), and proves \(|Q_n(\widetilde c)|>\widetilde c\) in this range. It constructs the inner cycle \(\{-x_-,x_-}\}\), referring in its numerical table to the closest period-two point to the origin. The result here gives an exact global count of the centrally symmetric cycles on each critical line and determines the stability of both of them.

## Proof
Set \(y=x^n\) for \(x>0\). Dividing the equation \(Q_n(x)=-x\) by \(x\) and clearing the positive denominator gives
\[
E_n(y)=(n+1)(4n^2+5n+2)y^3+2(n+1)(4n+3)y^2+(-n^2+7n+6)y+2=0.
\]
A direct cubic-discriminant calculation gives
\[
\operatorname{disc}_y(E_n)=4n^6(n+1)(4n^2-63n-59).
\]
This is positive for every real \(n\ge18\), so \(E_n\) has three distinct real roots. For \(n\ge18\), the coefficient of \(y\) is negative. Therefore \(E_n(-y)\), viewed for positive \(y\), has coefficient signs \(-,+,+,+\); Descartes' rule gives exactly one negative root of \(E_n\). The two remaining roots are positive. Since the source's critical-value identity yields \(Q_n(\widetilde c)<-\widetilde c\), while \(Q_n(x)+x>0\) for small positive \(x\) and again for sufficiently large \(x\), exactly one positive solution lies on each side of \(\widetilde c\).

To classify stability, note that
\[
\frac{Q_n(x)}x+1=\frac{E_n(y)}{2((n+1)y+1)^3}.
\]
At a positive root of \(E_n\), differentiation gives
\[
Q_n'(x)=-1+\frac{nyE_n'(y)}{2((n+1)y+1)^3}.
\]
If the roots are ordered \(y_0<0<y_-<y_+\), then \(E_n'(y_-)<0\), hence \(Q_n'(x_-)<-1\).

For the outer root define
\[
H_n(y)=nyE_n'(y)-4((n+1)y+1)^3.
\]
Then \(Q_n'(x_+)>1\) is equivalent to \(H_n(y_+)>0\). Elimination gives
\[
\operatorname{Res}_y(E_n,H_n)=8n^9(n+1)^2R(n),
\qquad
R(n)=16n^4-216n^3-815n^2-931n-356.
\]
At \(n=18\), the outer root is bracketed by
\[
\frac1{28}<y_+<\frac1{27},
\]
because \(E_{18}(1/28)=-113/5488<0\) and \(E_{18}(1/27)=2720/19683>0\). Also
\[
H_{18}(1/28)=293023/5488>0,
\]
and \(H_{18}\) is increasing on \([1/28,\infty)\), so \(H_{18}(y_+)>0\). Finally,
\[
R(18)=138730,
\]
and \(R^{(1)}(18)=133025\), \(R^{(2)}(18)=37250\), \(R^{(3)}(18)=5616\), while \(R^{(4)}(n)=384>0\). Thus \(R(n)>0\) for all real \(n\ge18\). The discriminant stays positive there, so the ordered outer root \(y_+(n)\) varies continuously; the nonzero resultant prevents \(H_n(y_+(n))\) from vanishing. Its sign is therefore positive throughout \([18,\infty)\). Hence \(Q_n'(x_+)>1\).

For even \(n\), \(Q_n\) is odd and \(Q_n'\) is even. The multiplier of either symmetric two-cycle is therefore \((Q_n'(x_\pm))^2>1\), proving repulsion. Distinct critical lines intersect only at the origin, so two nonzero cycles on each of \(n/2\) lines give exactly \(n\) such cycles for \(C_n\).

## Verification
The symbolic identities, discriminant, resultant, exact \(n=18\) brackets, and positivity anchors were independently replayed from the packaged `verify.py` and returned `VERIFY_OK`. The verification uses exact integer and rational arithmetic through SymPy; no floating-point computation is part of the proof.

## Relationship to prior work
Nayak and Phogat's recent paper defines this exact family, proves the invariant-line conjugacy, derives \(Q_n'\), and for even \(n\ge18\) constructs the inner symmetric two-cycle used to delimit the origin basin on a critical line. Its Table 1 calls that point the period-two point closest to the origin, but the text does not give an exact count of the centrally symmetric period-two cycles or determine their multipliers. The theorem here identifies the outer companion, proves there are exactly two such cycles per critical line, and proves both are repelling.

Earlier work of Gutiérrez and Varona studies attracting and superattracting cycles for Chebyshev maps of cubic polynomial families. Those parameter families and conclusions do not determine the symmetric cycles of \(p_n(z)=z(z^n-1)\) for even \(n\ge18\). Nayak and Pal's general symmetry work supplies structural background but does not contain this count or stability classification.

## Limitations
The result rules out only the two centrally symmetric real period-two cycles on each critical line as attracting or parabolic obstructions. It does not rule out attracting cycles of higher period, nonsymmetric period-two cycles, or nonreal periodic attractors. In particular, it does not answer whether the Chebyshev map is convergent for every even \(n\ge18\).

A residual literature risk remains because the focal preprint is recent and its wording “closest to the origin” suggests awareness of additional period-two points even though no exact global count or stability theorem is stated in the inspected version. A later revision or an unindexed note could contain an equivalent classification.

## References
1. T. Nayak and P. Phogat, “Chebyshev’s method applied to polynomials with rotational symmetry,” arXiv:2609.02884v1, first public 2026-09-02. Primary MSC 37F10.
2. T. Nayak and S. Pal, “Symmetry and dynamics of Chebyshev’s method,” arXiv:2208.11322; Mediterranean Journal of Mathematics 22 (2025), Paper 12.
3. J. M. Gutiérrez and J. L. Varona, “Superattracting Extraneous Fixed Points and n-cycles for Chebyshev’s Method on Cubic Polynomials,” Qualitative Theory of Dynamical Systems 19 (2020), Paper 54, DOI 10.1007/s12346-020-00390-5.
