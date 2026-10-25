# Sharp discrete second-difference endpoint and a common pointwise extremizer

## Finding

For each integer \(d\geq1\), extend \(a=(a_1,\ldots,a_d)\in\mathbb C^d\) by zero outside \(\{1,\ldots,d\}\), and write \(\Delta a_r=a_r-a_{r-1}\). The sharp constant in
\[
\sum_{j=1}^{d}|a_j|\leq \mathcal C_d\max_{1\leq r\leq d+2}|\Delta^2a_r|
\]
is, on writing \(d=4m+s\) with \(0\leq s\leq3\),
\[
\boxed{\mathcal C_d=\begin{cases}
m(m+1)(2m+1),&s=0,\\
\frac{(m+1)^2(4m+1)}2,&s=1,\\
2(m+1)^3,&s=2,\\
\frac{(m+1)^2(4m+7)}2,&s=3.
\end{cases}}
\]
The \(s=0\) branch is used only for \(m\geq1\). In particular \(\mathcal C_d/d^3\to1/32\).

There is a **single nonnegative symmetric extremizing sequence** \(a^*\) which simultaneously saturates every coordinatewise estimate
\[
|a_j|\leq a_j^*\max_{1\leq r\leq d+2}|\Delta^2a_r|,\qquad 1\leq j\leq d.
\]
More precisely, put \(N=d+2\), \(k=\lfloor N/4\rfloor\), \(u=k+1\), \(v=N-k\), \(L=v-u\), and \(\tau=(N-4k-2)/2\). Define the real curvature sequence \(b^*\) on \(\{1,\ldots,N\}\) by
\[
b_r^*=\begin{cases}
1,&r<u\text{ or }r>v,\\
\tau,&r=u\text{ or }r=v,\\
-1,&u<r<v.
\end{cases}
\]
The two knot indices are distinct for every \(d\geq1\). Then
\[
 a_j^*=\sum_{r=1}^{j}(j-r+1)b_r^*,\qquad 1\leq j\leq d,
\]
is strictly positive and satisfies \(\Delta^2a^*=b^*\) with zero extension and \(\|b^*\|_\infty=1\). Consequently, \(\sum_j a_j^*=\mathcal C_d\), and scalar complex multiples of \(a^*\) are extremizers.

A dual statement is the exact discrete least-absolute-deviation formula
\[
\min_{q\in\mathbb R_1[z]}\sum_{r=1}^{N}|(r-u)(r-v)+q(r)|
=\sum_{r=1}^{N}|(r-u)(r-v)|=2\mathcal C_d,
\]
where \(\mathbb R_1[z]\) denotes real polynomials of degree at most one. Thus the quadratic with knots at the indicated two integer locations solves a monic discrete \(\ell^1\) approximation problem on every consecutive grid.

## Assumptions and scope

The theorem concerns **all complex sequences** of an arbitrary fixed positive length, **zero extension on both sides**, the **backward** second difference, the coefficient \(\ell^1\) norm, and the difference-coefficient \(\ell^\infty\) norm. No periodic boundary identification, sign restriction on the input, or infinite-support limiting argument is assumed. The sharp constant concerns this finite-dimensional operator inequality only; it is not a claim about Fourier-function \(L^\infty\) norms or arbitrary higher difference orders.

## Proof

**1. Moment constraints and the candidate.** Set \(b_r=\Delta^2 a_r\), \(1\leq r\leq N\). Summation by parts with zero extension gives
\[
\sum_{r=1}^{N}b_r=0,\qquad \sum_{r=1}^{N}r b_r=0,\qquad
a_j=\sum_{r=1}^{j}(j-r+1)b_r.
\]
Conversely, every \(b\in\mathbb C^N\) satisfying the two moment equations yields a unique zero-extended \(a\) by the last formula: the reconstructed values at the final two indices vanish. Since \(N=4k+s\), \(s\in\{0,1,2,3\}\), the displayed \(\tau=(s-2)/2\) lies in \([-1,1]\). The vector \(b^*\) is symmetric about \((N+1)/2\) and has sum \(2k-(N-2k-2)+2\tau=0\), hence both moments vanish. Its sup norm equals one.

**2. One chord certifies every coordinate.** Fix \(j\in\{1,\ldots,d\}\). On the grid define the convex ramp \(h_j(r)=\max\{j-r+1,0\}\), and let \(\ell_j\) be the affine function agreeing with \(h_j\) at \(r=u,v\). Convexity gives \(h_j(r)-\ell_j(r)\geq0\) outside \([u,v]\), and \(h_j(r)-\ell_j(r)\leq0\) strictly between its endpoints. At both knots the difference vanishes. Thus, with \(|b_r|\leq1\) and the zero moments,
\[
|a_j|=\left|\sum_{r=1}^{N}(h_j(r)-\ell_j(r))b_r\right|
\leq\sum_{r=1}^{N}|h_j(r)-\ell_j(r)|.
\]
The sign pattern of \(b^*\) matches \(h_j-\ell_j\) at every grid location where it is nonzero; its fractional values occur only at the two knots, where the difference is zero. Hence the final sum equals
\(\sum_r(h_j(r)-\ell_j(r))b_r^*=\sum_r h_j(r)b_r^*=a_j^*\).
This proves, for every complex \(a\), the simultaneous coordinatewise inequalities after scaling \(b\) by its sup norm. The right side is positive because the convex ramp has a kink between the two endpoints or outside their chord, and in all dimensions at least one grid value differs. Repeating for all \(j\) proves the required sharp \(\ell^1\) inequality, attained by \(a^*\).

**3. Exact summation, dual quadratic, and four residue classes.** Sum the ramps over all coordinates:
\[
W(r):=\sum_{j=1}^{d}h_j(r)=\frac{(N-r)(N-r-1)}2\quad(1\leq r\leq N).
\]
This is a quadratic of leading coefficient \(1/2\). Its affine chord \(\ell_W=\sum_j\ell_j\) through \(u,v\) therefore satisfies
\[
W(r)-\ell_W(r)=\tfrac12(r-u)(r-v).
\]
Summing the already sharp pointwise identities gives
\[
\mathcal C_d=\sum_j a_j^*
=\frac12\sum_{r=1}^{N}b_r^*(r-u)(r-v)
=\frac12\sum_{r=1}^{N}|(r-u)(r-v)|.
\]
Here \(b^*\) equals the sign of the quadratic outside its two roots. For every affine polynomial \(q\), its dot product with \(b^*\) vanishes by the moment constraints, while \(\|b^*\|_\infty\leq1\). Therefore
\(\sum_r|(r-u)(r-v)+q(r)|\geq\sum_r b_r^*((r-u)(r-v)+q(r))=2\mathcal C_d\), proving the dual minimum.

Write \(L=v-u=N-2k-1\). Pairing the two outer grid tails and summing the interior gives the finite arithmetic identity
\[
\mathcal C_d=\sum_{h=1}^{k}h(h+L)+\frac12\sum_{h=1}^{L-1}h(L-h)
=\frac{k(k+1)(2k+1)}6+\frac{Lk(k+1)}2+\frac{L(L^2-1)}{12}.
\]
Substituting \(N=d+2\) and the four possibilities \(d\bmod4\) gives the four displayed cubic branches. Each has leading term \(d^3/32\), completing the proof.

## Verification

The attached standalone standard-library Python script `checks/verify.py` uses `fractions.Fraction` and checks, for every \(1\leq d\leq160\): the two moments; exact support boundary values; the equality \(\Delta^2a^*=b^*\); positivity and symmetry; every one of the \(d\) separate affine-chord certificates; and the agreement of the extremal sum, discrete quadratic norm, arithmetic sum, and four residue-class formulas. It completed 26,880 exact assertions without errors. These finite tests are supplementary; the preceding convexity and summation argument proves the statement for all dimensions and all complex inputs.

## Relationship to prior work

Hindov, Nitzan, Olsen, and Rydhe (arXiv:2610.19010v1, initially public 13 October 2026) introduced the general coefficient-norm setting and determined the sharp constants for \(\ell^1\) input against **\(\ell^2\)** differences, for every derivative order. Their sign-preserving left-inverse theorem and the associated least-squares discrete Chebyshev principle are acknowledged; this theorem addresses the distinct **\(\ell^\infty\)** curvature endpoint for order two, with a four-class exact formula, an explicit discrete least-absolute-deviation quadratic, and a simultaneous pointwise extremizer. The argument above is independently self-contained for this endpoint and does not claim the source's \(\ell^2\) formulas as new.

Related continuous Sobolev endpoint inequalities and sharp Fourier-function supremum problems use different domains or norms; neither is identified here with the coefficient-supremum problem. Priority over every possible older discrete spline or optimal-recovery formulation is not established.

## Limitations

The sharp constant is proved only for the second backward difference with zero extension and a coefficient \(\ell^\infty\) norm. The theorem does not determine unrestricted higher-order endpoint constants, other combinations of exponents, a complete uniqueness classification of equality inputs, or optimal constants on periodic grids. Independent expert validation and exhaustive bibliographic priority assessment remain outstanding.

## References

1. R. Hindov, S. Nitzan, J.-F. Olsen, and E. Rydhe, *A sharp discrete Sobolev inequality and left inverses of higher order differences*, arXiv:2610.19010v1 (13 October 2026), https://arxiv.org/html/2610.19010v1. See introduction, Theorem 1, Theorem 17, and Sections 3.4–4.
2. J. Richardson, *A Sharp Fourier Inequality and the Epanechnikov Kernel*, arXiv:2310.09713 (2023), https://arxiv.org/abs/2310.09713. Distinct Fourier-function supremum norm formulation cited for context.
