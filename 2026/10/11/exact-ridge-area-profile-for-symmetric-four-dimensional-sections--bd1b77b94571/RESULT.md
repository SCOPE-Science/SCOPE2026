# Exact ridge-area profile for symmetric four-dimensional sections of the five-cube

## Finding

Let \(C=[-1,1]^5\). For each real \(s\geq 0\), set
\[
L_s=\{x\in\mathbb R^5:x_1+x_2+x_3+x_4+s x_5=0\},
\qquad P_s=C\cap L_s.
\]
The Euclidean metric on \(P_s\) is inherited from the four-dimensional linear subspace \(L_s\). Define the total ridge measure
\[
\Phi_2(P_s)=\sum_{F\in\mathcal F_2(P_s)}\mathcal H^2(F),
\]
where the sum is over **distinct** two-dimensional faces. Put \(R_s=\sqrt{s^2+2}\). Then for every finite \(s\geq0\), including all transition parameters,
\[
\boxed{
\Phi_2(P_s)=
\begin{cases}
6(8-s)R_s+4\sqrt3(8-s^2),&0\leq s\leq2,\\[2pt]
\dfrac{12R_s}{s}\left(8-\dfrac{(4-s)^2}{2}\right)+4\sqrt3(4-s)^2,&2\leq s\leq4,\\[5pt]
\dfrac{96R_s}{s},&s\geq4.
\end{cases}}
\]
In particular,
\[
96<\Phi_2(P_s)\leq48\sqrt2+32\sqrt3.
\]
The upper equality holds **only** at \(s=0\). The sharp lower infimum is \(96\), approached as \(s\to\infty\), and not attained for any finite parameter. The full attained range is \((96,48\sqrt2+32\sqrt3]\).

The profile need not decrease monotonically: in \((0,2)\) it has a strict local minimum at the unique root \(\rho\in(3/5,2/3)\) of \(s^3+25s^2-21s+3=0\), and a strict local maximum at \(s=1\). It decreases strictly for \(s>1\).

## Assumptions and scope

The parameter \(s\) is nonnegative; signs of coefficients and permutations of the first four coordinates give congruent sections. All areas use Euclidean two-dimensional Hausdorff measure, without a normalization by the ambient measure of the full boundary. The domain is the fixed one-parameter family of **central hyperplane sections of the five-cube**; this result does not address all four-dimensional cube sections, all admissible polytopes, or any unrestricted sharp ridge inequality.

Every \(P_s\) is a four-dimensional polytope containing the origin in its relative interior. A positive-area two-face lies in the intersection with a three-dimensional face of the five-cube obtained by fixing exactly two coordinates. These intersections have pairwise disjoint relative interiors unless they are identical; in this family a full two-dimensional intersection cannot have three fixed cube coordinates, so every positive-area two-face is counted once. The statement remains valid when some candidate intersections have zero area, at \(s=0,2,4\) as well as elsewhere.

## Proof

**1. Face-to-slice reduction.** For a nonzero triple of nonnegative weights \(w=(a,b,c)\), define
\[
A_w(t)=\mathcal H^2\!\left(\left\{y\in[-1,1]^3:a y_1+b y_2+c y_3=t\right\}\right).
\]
Of the ten coordinate pairs in \(C\), six pairs lie among the first four coordinates. Fixing each such pair to the four possible sign combinations leaves three free coordinates with weights \((1,1,s)\) and section levels \(0,0,2,-2\). Four pairs contain coordinate five; each leaves weights \((1,1,1)\) and levels of absolute values \(1+s\) and \(|1-s|\), each twice. Consequently the exact ridge sum is
\[
\Phi_2(P_s)=12\bigl(A_{(1,1,s)}(0)+A_{(1,1,s)}(2)\bigr)
+8\bigl(A_{(1,1,1)}(1+s)+A_{(1,1,1)}(|1-s|)\bigr).
\tag{1}
\]
This counts all two-faces directly in the intrinsic Euclidean metric; the fixed-coordinate embedding is an isometry on each three-face.

**2. Exact slice areas.** The convolution of three independent uniform random variables on \([-1,1]\), combined with the coarea identity, gives
\[
A_w(t)=8\lVert w\rVert_2 f_w(t),
\]
where \(f_w\) is the density of their weighted sum. Integrating the triangular density of the sum of two uniforms yields, for \(u\geq0\),
\[
A_{(1,1,1)}(u)=\sqrt3\begin{cases}
3-u^2,&0\leq u\leq1,\\
(3-u)^2/2,&1\leq u\leq3,\\
0,&u\geq3.
\end{cases}
\tag{2}
\]
For \(s>0\), write \(R_s=\sqrt{s^2+2}\). A second application of convolution gives the explicit integral
\[
A_{(1,1,s)}(t)=\frac{R_s}{s}\int_{t-s}^{t+s}(2-|u|)_+\,\mathrm du,
\qquad (z)_+=\max(z,0).
\tag{3}
\]
The formula extends continuously to \(s=0\). At the two required section levels it specializes to
\[
A_{(1,1,s)}(0)=R_s\begin{cases}4-s,&0\leq s\leq2,\\4/s,&s\geq2,\end{cases}
\quad
A_{(1,1,s)}(2)=R_s\begin{cases}
s/2,&0\leq s\leq2,\\
\bigl(8-(4-s)^2/2\bigr)/s,&2\leq s\leq4,\\
4/s,&s\geq4.
\end{cases}
\tag{4}
\]
Substitution of (2) and (4) into (1) gives all three branches of the displayed theorem, with matching endpoint values at \(s=2\) and \(s=4\).

**3. Strict lower bound.** For \(s\geq4\), the third branch equals \(96\sqrt{1+2/s^2}>96\) and tends to \(96\). For \(2\leq s\leq4\), put \(z=4-s\) and \(r=\sqrt{1+2/s^2}>1\). Then
\[
\Phi_2(P_s)=12r(8-z^2/2)+4\sqrt3z^2
>96+(4\sqrt3-6)z^2\geq96.
\]
For \(0\leq s\leq1\), the first branch is at least \(42\sqrt2+28\sqrt3>96\). For \(1\leq s\leq2\), the factor \((8-s)\sqrt{s^2+2}\) is increasing, since its derivative is \((8s-2s^2-2)/\sqrt{s^2+2}>0\); hence the first branch is at least \(58\sqrt3>96\). These intervals exhaust the parameter range.

**4. Sharp upper bound and interior extrema.** On \(0<s<2\), differentiation yields
\[
\Phi_2'(P_s)=\frac{6(8s-2s^2-2)}{\sqrt{s^2+2}}-8\sqrt3s.
\tag{5}
\]
Any critical point therefore satisfies \(3(4s-s^2-1)=2\sqrt3s\sqrt{s^2+2}\). Squaring and factoring gives
\[
9(4s-s^2-1)^2-12s^2(s^2+2)
=-3(s-1)(s^3+25s^2-21s+3).
\tag{6}
\]
The cubic has exactly two roots in \((0,2)\), one in \((0,1/5)\) and one in \((3/5,2/3)\); this follows by its one positive derivative-zero point, together with the displayed sign brackets. The smaller root fails the unsquared positive-sign requirement. The surviving root \(\rho\) and \(s=1\) are both actual critical points. The derivative in (5) has signs negative at zero, positive at \(s=4/5\), and negative at \(s=3/2\). Thus \(\rho\) is the unique strict interior minimum and \(1\) the unique strict interior maximum of the first branch.

For \(2\leq s\leq4\), put \(B=8-(4-s)^2/2\), \(r=\sqrt{1+2/s^2}\), \(z=4-s\). The derivative of the middle branch is
\[
-\frac{24B}{s^3r}+z(12r-8\sqrt3).
\tag{7}
\]
When \(s\geq\sqrt6\), one has \(r\leq2/\sqrt3\), so both terms are nonpositive and the first is strictly negative. When \(2\leq s\leq\sqrt6\), the absolute value of the first term is at least \(8\), whereas the second term is at most \(2(6\sqrt6-8\sqrt3)<8\). The derivative is therefore strictly negative. On \(s\geq4\), the third branch is also strictly decreasing. The only possible global maxima are at \(s=0\) and \(s=1\), where
\[
\Phi_2(P_0)=48\sqrt2+32\sqrt3,
\qquad \Phi_2(P_1)=70\sqrt3.
\]
The first exceeds the second because \(48\sqrt2>38\sqrt3\). Continuity and the limit in Step 3 then give the exact range and all asserted equality conditions.

## Verification

The self-contained program `verify.py` reconstructs the plane intersections with all forty three-dimensional cube faces using rational edge interpolation, computes convex hull areas via an independent exact shoelace calculation, and compares the separate rational coefficients of \(\sqrt{s^2+2}\) and \(\sqrt3\) against the formula. Eighteen rational parameter values, including all three transition points, give `EXACT_RIDGE_FACE_SLICES_OK 18` and `EXACT_ENDPOINTS_OK`. Run it with `python3 verify.py` from the directory containing this document.

These finite computations are reproducibility checks, **not** exhaustive verification of the continuum of parameters. The analytic identities and sign arguments in the proof establish the infinite-domain statements.

## Relationship to prior work

Michał Zwierzyński's 2026 paper *A Sharp Surface-Area Extension of Vaaler's Theorem* (arXiv:2609.27798v1), especially its Section 5, formulated the sharp ridge-skeleton conjecture \(\Phi_{n-2}\geq n(n-1)2^{n-1}\) for admissible polytopes. Its Proposition 5.3 proves two other special families; Proposition 5.4 proves a weaker general estimate. The same paper already supplies the skeletal polynomial of the three-dimensional central diagonal four-cube section; its Cartesian-product identity therefore implies **the endpoint at \(s=0\)**. The new point here is the full continuously varying profile, its sharp interval bound and its interior stationary-point classification, none of which follows from that endpoint computation. Roman Karasev's *Rogers's proof of Vaaler's theorem* (arXiv:2505.16247) concerns volume and surface area, not this codimension-two profile.

Earlier work by G. R. Burton (1980) addresses integral-geometric formulas involving skeletal measures and affine sections. The accessible abstract concerns averages over sections rather than this fixed pointwise family; the complete article could not be compared, leaving a genuine bibliographic risk.

## Limitations

This is not a proof of the general ridge-skeleton conjecture in dimension four: it covers only hyperplanes with normal vector proportional to \((1,1,1,1,s)\). The value at \(s=0\) is already computable from the cited 2026 paper, and the conjectured limiting bound is supplied by the four-cube. No claim of independent peer review or universal novelty certification is made. An equivalent older exact slice formula may remain unidentified.

## References

1. Michał Zwierzyński, *A Sharp Surface-Area Extension of Vaaler's Theorem*, arXiv:2609.27798v1 (first public 2026-08-19), Section 5. https://arxiv.org/html/2609.27798v1
2. Roman Karasev, *Rogers's proof of Vaaler's theorem*, arXiv:2505.16247 (first public 2025-05-22). https://arxiv.org/abs/2505.16247
3. G. R. Burton, *Skeleta and sections of convex bodies*, Mathematika 27 (1980), 97–103, DOI:10.1112/S0025579300009980. Accessible abstract only for this comparison.
