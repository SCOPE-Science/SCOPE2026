# Sharp canonical stadium stability at fixed perimeter and minimum width

## Finding
For every planar convex body \(K\) with nonempty interior, perimeter \(P\), minimum width \(w\), and a chosen minimum-width normal direction \(u_0\), let \(S\) be the stadium of radius \(w/2\) and central segment length \((P-\pi w)/2\), whose segment is perpendicular to \(u_0\) and whose Steiner point equals that of \(K\). (A segment of length zero means a disk.) Then the **exact global stability identity** is
\[
\frac{Pw}{2}-\frac{\pi w^2}{4}-A(K)
= A(S)-A(K)
=\frac12\int_0^{2\pi}\bigl[f'(\theta)^2-f(\theta)^2\bigr]d\theta,
\qquad f=h_K-h_S.
\]
The right side is nonnegative and vanishes precisely for \(K=S\). The following global Hausdorff stability estimate has the **best possible universal coefficient**:
\[
\boxed{d_H(K,S)^2\le \frac{3}{2\pi}\,[A(S)-A(K)].}
\]
For **every fixed admissible pair** \(P>\pi w>0\), the coefficient \(3/(2\pi)\) is sharp within bodies with *exactly those* values of perimeter and minimum width. At the boundary \(P=\pi w>0\), all eligible bodies have constant width, and the sharp coefficient improves to \(1/(2\pi)\). Thus the best coefficient has a genuine, discontinuous sharp-constant transition at the constant-width boundary. The constant-width endpoint is recalled for comparison, not asserted to be novel independently.

## Assumptions and scope
We work in the Euclidean plane. A convex body is compact, convex, and has nonempty interior; no smoothness or strict convexity is assumed. Its continuous \(2\pi\)-periodic support function \(h_K\) belongs to \(H^1\); perimeter is \(P=\int_0^{2\pi}h_K\,d\theta\), area is \(A(K)=\tfrac12\int(h_K^2-h_K'^2)\,d\theta\), and width in angle \(\theta\) is \(h_K(\theta)+h_K(\theta+\pi)\). The Steiner point is the vector represented by the first Fourier harmonics of \(h_K\). Hausdorff distance of compact convex bodies is the uniform norm of the difference of their support functions.

The mean width is \(P/\pi\), so \(P\ge\pi w\). Rotate coordinates so \(u_0=(1,0)\), translate both objects to their common Steiner point, and put \(R=w/2\) and \(L=(P-\pi w)/2\). The stadium support function is
\[
h_S(\theta)=R+\frac L2|\sin\theta|.
\]
It has perimeter \(2\pi R+2L=P\), minimum width \(2R=w\), and area \(\pi R^2+2RL=Pw/2-\pi w^2/4\). The orientation and Steiner center matter; the estimate is for the canonical stadium selected by the minimum-width normal, not an arbitrary translate or rotation.

## Proof
**1. Exact deficit decomposition.** The curvature measure of \(S\) is, in periodic distributions,
\[
(h_S+h_S'')\,d\theta = R\,d\theta+L\delta_0+L\delta_\pi.
\]
Let \(f=h_K-h_S\). Equality of perimeter and Steiner point removes Fourier modes \(0,1,-1\). Equality of width at the chosen minimum-width normal gives \(f(0)+f(\pi)=0\). Expanding the quadratic area formula and integrating by parts against the stadium curvature measure yields
\[
A(K)-A(S)
=\int f\,d(h_S+h_S'')+\frac12\int(f^2-f'^2)
=R\int f+L[f(0)+f(\pi)]+\frac12\int(f^2-f'^2)
=\frac12\int(f^2-f'^2).
\]
For nonsmooth convex bodies these identities follow in \(H^1\) and the distributional sense, or by smooth approximation. Write the real Fourier series
\[
f(\theta)=\sum_{n=2}^{\infty}(a_n\cos n\theta+b_n\sin n\theta).
\]
Parseval then gives the **positive exact identity**
\[
A(S)-A(K)=\frac\pi2\sum_{n=2}^{\infty}(n^2-1)(a_n^2+b_n^2).
\]
This establishes equality rigidity and makes the deficit an intrinsic squared Fourier-energy distance to the prescribed stadium.

**2. Universal Hausdorff coefficient.** For every \(\theta\), weighted Cauchy–Schwarz gives
\[
|f(\theta)|^2\le
\left(\sum_{n=2}^{\infty}\frac1{n^2-1}\right)
\left(\sum_{n=2}^{\infty}(n^2-1)(a_n^2+b_n^2)\right).
\]
The first series telescopes to \(3/4\). Taking the supremum and using the exact area identity proves
\[
d_H(K,S)^2=\|f\|_\infty^2\le \frac{3}{2\pi}[A(S)-A(K)].
\]

**3. Sharpness for every nonconstant-width parameter pair.** Fix \(R>0\) and \(L>0\). For integers \(N\ge2\) choose \(\phi_N\in(0,\pi/2)\) satisfying
\[
\sum_{\substack{2\le n\le N\\n\ \mathrm{even}}}
\frac{\cos(n\phi_N)}{n^2-1}=0.
\]
Existence follows by the intermediate value theorem: the sum at zero is positive, while at \(\pi/2\) it is the strictly negative alternating sum \(\sum_{k\ge1}(-1)^k/(4k^2-1)\) truncated after its first term. Define
\[
q_N(\theta)=\sum_{n=2}^N\frac{\cos(n(\theta-\phi_N))}{n^2-1},
\quad h_N=h_S+\varepsilon_Nq_N,
\quad T_N=\sum_{n=2}^N\frac1{n^2-1}.
\]
The mean and first harmonics of \(q_N\) vanish, and \(q_N(0)+q_N(\pi)=0\). Choose a sufficiently small positive \(\varepsilon_N\). Then \(h_N\) is a convex-body support function: its curvature measure is \([R-\varepsilon_N\sum_{n=2}^N\cos(n(\theta-\phi_N))]d\theta+L(\delta_0+\delta_\pi)\), nonnegative for sufficiently small \(\varepsilon_N\). Also \(\theta=0\) remains a global minimum-width direction: its width perturbation vanishes at zero and is Lipschitz, while the base width rises as \(L|\sin\theta|\) away from multiples of \(\pi\). More precisely, on \(0\le\theta\le\pi/2\), \(L\sin\theta\ge2L\theta/\pi\), whereas the width perturbation has a finite Lipschitz constant, so sufficiently small \(\varepsilon_N\) preserves the minimum. Periodicity and reflection yield the other half. Therefore each body \(K_N\) has exactly the original perimeter \(P=2\pi R+2L\) and minimum width \(w=2R\), and the same canonical stadium \(S\).

The Fourier identity and the triangle inequality, with equality at \(\theta=\phi_N\), give **exactly**
\[
A(S)-A(K_N)=\frac\pi2\varepsilon_N^2T_N,
\qquad d_H(K_N,S)=\varepsilon_NT_N.
\]
Consequently
\[
\frac{d_H(K_N,S)^2}{A(S)-A(K_N)}
=\frac2\pi T_N\longrightarrow\frac{3}{2\pi}.
\]
This is sharpness for every fixed \(R,L>0\), not merely for bodies whose width degenerates.

**4. Constant-width boundary.** If \(P=\pi w\), the average width equals its minimum, so continuity forces constant width. All even Fourier modes of \(f=h_K-w/2\) vanish. The corresponding weighted kernel is \(\sum_{n\ge3,\,n\ \mathrm{odd}}(n^2-1)^{-1}=1/4\), yielding \(d_H(K,S)^2\le[A(S)-A(K)]/(2\pi)\). Sharpness follows by smooth, sufficiently small odd Fourier perturbations of the disk with coefficients proportional to \((n^2-1)^{-1}\), taking increasing finite cutoff. This endpoint is consistent with existing sharp constant-width results.

## Verification
A standalone standard-library Python program checks the curvature-density positivity, exact-width constraint, boundary integral area formula, finite Fourier deficit, and approach of the candidate sharpness ratios for six Fourier cutoffs \(N=4,8,16,32,64,128\). It numerically obtains ratios increasing from approximately \(0.3342\) to \(0.4725\), approaching \(3/(2\pi)\approx0.4774648293\). Those finite computations corroborate but cannot prove the universal statement or the infinite-cutoff limit; those are established by the formulas above.

Run `python3 verification/check_stadium_stability.py` with Python 3 and no third-party packages. The checker calculates the area independently by numerically integrating the curvature measure, including the two point masses.

## Relationship to prior work
The classical area–perimeter–minimum-width inequality \(A(K)\le Pw/2-\pi w^2/4\), with stadium equality, is **already known**; it is explicitly quoted by Ftouhi, Masiello and Paoli, Proposition 5.7 (2022/2024). No novelty is claimed for that bound itself. The present result is the globally exact, nonnegative Fourier-energy **remainder** and, more importantly, its **sharp Hausdorff stability coefficient for the moving canonical stadium**, simultaneously for every fixed pair \(P>\pi w>0\), with the constant-width boundary transition.

Gao's 2011 stability inequalities concern Hausdorff distance to the Steiner **disk**, measured against a disk isoperimetric deficit. They do not yield a vanishing deficit relative to the \(P,w\)-matched stadium: as a noncircular stadium is approached, the disk deficit remains positive. Results on bodies of constant width give a stronger boundary-specific constant and do not cover arbitrary varying-width convex bodies. The October 2026 work of An develops planar Minkowski support reconstruction and Steiner-centered Hausdorff estimates via Fourier multipliers, motivating quantitative width-constrained inverse questions, but it does not supply this stadium stability identity and sharp coefficient.

## Limitations
No claim is made that the underlying stadium area inequality is new. The sharp upper constant is a supremum along perturbation sequences; finite computations alone do not prove it. This analysis concerns Euclidean planar compact convex bodies with specified perimeter and minimum width; it does not supply a corresponding higher-dimensional theorem. The canonical stadium depends on the chosen minimum-width direction, which may not be unique. Potential overlap with unindexed older quantitative stability literature remains a scholarly priority risk.

## References
1. Congpei An, *Gauss--Chebyshev Quadrature, S¹-Designs, and the Planar Minkowski Inverse Problem: A One-Dimensional Model for Design-Induced Convex Geometry*, arXiv:2610.11814v1 (first public 2026-10-08), https://arxiv.org/html/2610.11814v1.
2. I. Ftouhi, A. L. Masiello, G. Paoli, *Sharp inequalities involving the Cheeger constant of planar convex sets*, arXiv:2206.13158v3, Proposition 5.7 and quoted classical inequality, https://arxiv.org/html/2206.13158v3.
3. Xiang Gao, *A Note On The Isoperimetric Inequality And Its Stability*, arXiv:1102.5642v1, Section 4, https://arxiv.org/html/1102.5642v1.
