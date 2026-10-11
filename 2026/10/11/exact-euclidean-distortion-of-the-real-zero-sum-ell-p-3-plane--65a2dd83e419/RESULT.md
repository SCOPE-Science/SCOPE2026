# Exact Euclidean distortion of the real zero-sum \(\ell_p^3\) plane

## Finding

Let \(H=\{x=(x_1,x_2,x_3)\in\mathbb R^3:x_1+x_2+x_3=0\}\), and let \(H_p=(H,\|\cdot\|_p)\) have the norm induced by the real sequence space \(\ell_p^3\). With multiplicative Banach--Mazur distance defined by
\[
d_{\mathrm{BM}}(X,Y)=\inf_{T:X\longrightarrow Y\ \mathrm{invertible}}\|T\|\,\|T^{-1}\|,
\]
we have, for every \(1\le p<\infty\),
\[
\boxed{d_{\mathrm{BM}}(H_p,\ell_2^2)=\max\left\{\frac{(1+2^{p-1})^{1/p}}{\sqrt3},\frac{\sqrt3}{(1+2^{p-1})^{1/p}}\right\}.}
\]
At \(p=\infty\), the distance is \(2/\sqrt3\). The Euclidean metric induced by \(\|x\|_2\) on \(H\) is optimally placed for all exponents. Moreover, this distance equals one exactly at \(p\in\{2,4\}\). For any other exponent, the norm-ratio extrema relative to \(\|x\|_2\) are obtained on scalar multiples and coordinate permutations of \((1,0,-1)\) and \((1,1,-2)\). The former is the maximizer for \(2<p<4\) and the minimizer for \(1\le p<2\) or \(4<p\le\infty\); the latter is the opposite extremum.

## Assumptions and scope

All scalars and linear maps are **real**. The domain is exactly the two-dimensional zero-sum hyperplane of three coordinates, not the full ambient \(\ell_p^3\) and not the analogous complex hyperplane. The exponent range includes both endpoint norms. The distance convention here is multiplicative (and therefore at least one). No higher-dimensional statement is asserted.

## Proof

**1. Optimal Hilbert position by symmetry.** Every invertible linear comparison of the two-dimensional space \(H_p\) with a Hilbert plane determines a positive quadratic form \(Q\) on \(H\). If \(mQ(x)\le\|x\|_p^2\le M Q(x)\) for all \(x\in H\), the associated distortion is \(\sqrt{M/m}\). Each coordinate permutation preserves \(H\) and \(\|\cdot\|_p\). Averaging \(Q\) over all six permutations preserves both pointwise inequalities and hence cannot worsen that distortion. The three-cycle acts on \(H\), with respect to its usual Euclidean metric, as a rotation through \(2\pi/3\). Every real symmetric quadratic form invariant under such a rotation is proportional to \(\|x\|_2^2\). Therefore *no tilted or anisotropic ellipse improves upon the Euclidean pullback*, and
\[
d_{\mathrm{BM}}(H_p,\ell_2^2)=\frac{\displaystyle\max_{x\in H\setminus\{0\}}\|x\|_p/\|x\|_2}{\displaystyle\min_{x\in H\setminus\{0\}}\|x\|_p/\|x\|_2}.
\]
Compactness of the projective circle guarantees attainment.

**2. One-parameter reduction.** Every nonzero \(x\in H\), up to a nonzero scalar and coordinate permutation, has the form \((1,r,-1-r)\) for some \(0\le r\le1\): choose the two same-sign coordinates, change the overall sign if needed, and scale their larger magnitude to one. For finite \(p\), the corresponding norm ratio is
\[
F_p(r)=\frac{\bigl(1+r^p+(1+r)^p\bigr)^{1/p}}{\sqrt{2(1+r+r^2)}}.
\]
For \(p=\infty\), it is \(F_\infty(r)=(1+r)/\sqrt{2(1+r+r^2)}\).

**3. Global monotonicity and the exceptional exponents.** Suppose \(1<p<\infty\), write \(s=p-1\), and differentiate the logarithm of \(F_p\). Multiplication by its strictly positive denominator shows that the sign of \(F_p'(r)\) for \(0<r<1\) is precisely the sign of
\[
G_r(s)=(2+r)r^s+(1-r)(1+r)^s-(1+2r).
\]
For each fixed \(0<r<1\), direct expansion gives \(G_r(1)=G_r(3)=0\). Further,
\[
G_r''(s)=(2+r)r^s(\log r)^2+(1-r)(1+r)^s\bigl(\log(1+r)\bigr)^2>0
\]
for every real \(s\). A strictly convex function with distinct zeros at \(1\) and \(3\) is negative strictly between them and positive strictly outside. Consequently \(F_p\) increases strictly for \(1<p<2\) and \(p>4\), decreases strictly for \(2<p<4\), and is constant for \(p=2,4\). At \(p=1\) and \(p=\infty\), the displayed elementary functions increase strictly on \((0,1)\). This proves that all extrema occur at the two endpoint symmetry orbits. It also verifies the full ranges and endpoint cases without assuming the extremum location from a finite sample.

**4. Exact ratios.** Direct substitution gives
\[
F_p(0)=2^{1/p-1/2},\qquad F_p(1)=\frac{(2+2^p)^{1/p}}{\sqrt6},\qquad
\frac{F_p(1)}{F_p(0)}=\frac{(1+2^{p-1})^{1/p}}{\sqrt3}.
\]
The largest over smallest of these two numbers yields the asserted multiplicative distance. For \(p=\infty\), the analogous ratio is \(F_\infty(1)/F_\infty(0)=2/\sqrt3\). The strict monotonicity for every other exponent proves that distance one occurs *only* at \(p=2\) and \(p=4\). The latter also follows independently from the exact trace-zero identity
\[
2\sum_{i=1}^3x_i^4=\left(\sum_{i=1}^3x_i^2\right)^2\qquad(x\in H),
\]
which shows that \(\|x\|_4=2^{-1/4}\|x\|_2\) on the entire real plane.

## Verification

Run `python3 verification/check.py` from the package root. This standalone standard-library script checks the quartic identity for 289 integer pairs, the vanishing derivative certificates at both special exponents on 999 interior samples each, and the sharp endpoint bounds at 1,001 radial points for each of 20 exponents (including the endpoints). The expected deterministic completion message begins `VERIFY_OK quartic_exact=289 derivative_special=1998 radial_bounds=20020`. These are finite corroborations. The universal theorem is established by symmetry averaging and strict convexity in the real exponent, not by enumeration or floating-point evidence.

## Relationship to prior work

Passer [1] gives a quantitative approximate Jordan--von Neumann theorem, bounding Euclidean Banach--Mazur distance in terms of a small parallelogram-law defect. This is a general local estimate, not the sharp distortion profile for the concrete three-atomic zero-sum plane. Zhang, Meng, and Wu [2] study a different three-dimensional comparison, between the full \(\ell_p^3\) and \(\ell_\infty^3\); their Theorem 2 is an upper bound in that full-dimensional setting, and it does not determine the Euclidean distance of the codimension-one plane. General finite-dimensional distance theory supplies useful context but not the two critical exponents. In the real quartic exponent, the zero-sum hyperplane is already a known Hilbertian special case: the contribution here is the complete exact \(p\)-dependence, optimal Hilbert position, and the two monotonicity transitions, not a new claim about that special case alone.

## Limitations

The analysis is specific to three coordinates and **real** scalars. The computation does not establish analogous formulas for arbitrary codimension-one hyperplanes, complex hyperplanes, or other Schatten-class subspaces. The claim is mathematical and has received same-model review only; it has not undergone independent external verification. An earlier equivalent formulation under type-\(A_2\) root-system or three-atom norm terminology remains a bibliographic possibility, although the inspected sources do not imply the full displayed profile.

## References

[1] Benjamin Passer, *An Approximate Version of the Jordan von Neumann Theorem for Finite Dimensional Real Normed Spaces*, arXiv:1305.3546, first posted 2013-05-13. Sections 1–3, particularly Theorems 2.9 and 3.4.

[2] Longzhen Zhang, Lingxu Meng, and Senlin Wu, *Banach--Mazur Distance from \(\ell_p^3\) to \(\ell_\infty^3\)*, arXiv:2207.05499, first posted 2022-07-12. Introduction, Theorem 2, and Sections 2–3.
