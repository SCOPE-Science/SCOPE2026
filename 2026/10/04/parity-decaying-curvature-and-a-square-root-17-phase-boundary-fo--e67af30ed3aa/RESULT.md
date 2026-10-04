# Parity-decaying curvature and a square-root-17 phase boundary for symmetric determinantal degrees
## Finding
For integers \(n\ge 3\) and \(1\le r\le n\), let
\[
S_{n,r}=\deg\{[A]\in\mathbb P(\operatorname{Sym}^2\mathbb C^n):\operatorname{rank}A\le r\}.
\]
Put \(c=n-r\). For every interior rank \(2\le r\le n-1\), equivalently \(1\le c\le n-2\), define the adjacent-rank curvature
\[
Q_{n,c}=\frac{S_{n,r-1}S_{n,r+1}}{S_{n,r}^2}.
\]
Then
\[
Q_{n,c}=\frac{1}{2(2c+1)}
\frac{\prod_{j=0}^{c}(n-c+2j)}{\prod_{j=0}^{c-1}(n-c+1+2j)}.
\]
Moreover, whenever \(1\le c\le n-4\),
\[
\frac{Q_{n,c+2}}{Q_{n,c}}=
\frac{(2c+1)(n-c-2)(n+c+2)}{(2c+5)(n-c-1)(n+c+1)}<1.
\]
Thus the odd-corank and even-corank curvature subsequences are each strictly decreasing. If \(c=c_n\) and \(c_n/n\to\theta\in(0,1)\), then
\[
Q_{n,c_n}\longrightarrow \frac{\sqrt{1-\theta^2}}{4\theta}.
\]
Consequently, for every fixed \(\theta<1/\sqrt{17}\), ranks with corank ratio tending to \(\theta\) are eventually locally log-convex, while for every fixed \(\theta>1/\sqrt{17}\) they are eventually locally log-concave. The critical rank fraction is therefore
\[
\frac rn\longrightarrow 1-\frac1{\sqrt{17}}.
\]
No eventual-sign assertion is made at the critical ratio itself.

## Assumptions and scope
The ground field is \(\mathbb C\), and degree is projective degree in \(\mathbb P(\operatorname{Sym}^2\mathbb C^n)\). The adjacent-rank curvature is defined only when both neighboring ranks exist, so \(2\le r\le n-1\). The asymptotic statement concerns arbitrary integer sequences \(c_n\) satisfying \(c_n/n\to\theta\in(0,1)\). Log-concavity at a rank means \(S_{n,r}^2\ge S_{n,r-1}S_{n,r+1}\); log-convexity means the reverse inequality.

## Proof
Nie, Ranestad and Sturmfels record the classical degree formula
\[
S_{n,n-c}=\prod_{j=0}^{c-1}
\frac{\binom{n+j}{c-j}}{\binom{2j+1}{j}}.
\]
Write \(F_c=S_{n,n-c}\). Taking the quotient of consecutive values gives
\[
\frac{F_{c+1}}{F_c}
=\frac{c!}{(2c+1)!}\prod_{j=0}^{c}(n-c+2j).
\]
Therefore
\[
Q_{n,c}=\frac{F_{c+1}F_{c-1}}{F_c^2}
=\frac{F_{c+1}/F_c}{F_c/F_{c-1}},
\]
which simplifies to the displayed product formula.

Applying the same product formula at \(c+2\) and cancelling gives
\[
\frac{Q_{n,c+2}}{Q_{n,c}}=
\frac{(2c+1)(n-c-2)(n+c+2)}{(2c+5)(n-c-1)(n+c+1)}.
\]
All factors are positive in the stated range, and the denominator minus the numerator after cross multiplication is
\[
(2c+5)(n-c-1)(n+c+1)-(2c+1)(n-c-2)(n+c+2)=4n^2-1>0.
\]
This proves strict decrease along each parity class of \(c\).

For the asymptotic statement, rewrite the curvature as
\[
Q_{n,c}=\frac1{2c+1}
\frac{\Gamma((n+c+2)/2)}{\Gamma((n+c+1)/2)}
\frac{\Gamma((n-c+1)/2)}{\Gamma((n-c)/2)}.
\]
The standard ratio asymptotic \(\Gamma(x+1/2)/\Gamma(x)\sim\sqrt{x}\) yields, when \(c/n\to\theta\in(0,1)\),
\[
Q_{n,c}\sim
\frac{\sqrt{(n+c)(n-c)}}{4c}
\longrightarrow \frac{\sqrt{1-\theta^2}}{4\theta}.
\]
This limit is greater than \(1\) precisely when \(17\theta^2<1\), and smaller than \(1\) precisely when \(17\theta^2>1\). Since \(Q_{n,c}>1\) is equivalent to local log-convexity and \(Q_{n,c}<1\) to local log-concavity, the phase boundary follows.

## Verification
The standalone checker `artifacts/verify_symmetric_curvature.py` reconstructs the classical projective degrees from the binomial-product formula and compares the adjacent-rank ratio with the new product expression in 561 exact-integer cases. It also verifies 6,786 exact two-step parity contractions, including the identity that the cross-multiplied gap is \(4n^2-1\). A separate floating-point regression checks convergence to the proved gamma-ratio limit for several noncritical corank fractions. The regression is not used as an infinite proof.

## Relationship to prior work
Nie, Ranestad and Sturmfels give the symmetric determinantal degree formula and use these rank loci in the algebraic geometry of semidefinite programming. Their Proposition 14 supplies the exact input above but does not state adjacent-rank log-curvature, parity decay, or the \(1/\sqrt{17}\) corank phase boundary. The older Harris--Tu work is the source they cite for the degree formula. Manivel, Michałek, Monin, Seynnaeve and Vodička study asymptotics of other complete-quadric and semidefinite-programming enumerative invariants; their invariants are dual/intersection degrees rather than the ordinary projective degrees \(S_{n,r}\) considered here. A separate unrestricted-matrix determinantal family has a related rank-curvature threshold, but its degree product and exact curvature law are different and do not imply the symmetric-matrix identities proved here.

## Limitations
The theorem does not determine the sign at sequences lying exactly on the critical scale beyond the limit \(Q_{n,c_n}\to1\). The strict two-step inequality controls each parity subsequence, but this result alone does not prove that \(Q_{n,c+1}<Q_{n,c}\) for every adjacent pair. The literature search did not locate a prior statement of the rankwise curvature law, but absence from the inspected sources is not a proof of bibliographic uniqueness. Harris--Tu was not materially inspected in full text here; its role is limited to the degree formula attribution made explicitly by Nie, Ranestad and Sturmfels.

## References
1. J. Nie, K. Ranestad, B. Sturmfels, *The Algebraic Degree of Semidefinite Programming*, arXiv:math/0611562, Proposition 14; published in *Mathematical Programming* 122 (2010), 379--405, DOI 10.1007/s10107-008-0253-6.
2. J. Harris, L. W. Tu, *On symmetric and skew-symmetric determinantal varieties*, *Topology* 23 (1984), 71--84, DOI 10.1016/0040-9383(84)90026-0.
3. T. Józefiak, A. Lascoux, P. Pragacz, *Classes of determinantal varieties associated with symmetric and skew-symmetric matrices*, *Math. USSR-Izvestiya* 18 (1982), 575--586, DOI 10.1070/IM1982v018n03ABEH001400.
4. L. Manivel, M. Michałek, L. Monin, T. Seynnaeve, M. Vodička, *Complete quadrics: Schubert calculus for Gaussian models and semidefinite programming*, *J. Eur. Math. Soc.* 26 (2024), 3091--3135, DOI 10.4171/JEMS/1330.
