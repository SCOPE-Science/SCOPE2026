# A sharp global brightness-direction switch for right circular cones

## Finding
For a solid right circular cone of radius \(r>0\), height \(h>0\), and aspect \(k=h/r\), let \(A_k(u)\) be the Euclidean area of the cone's orthogonal shadow perpendicular to the unit direction \(u\). There is a **single sharp critical aspect**
\[
\boxed{k_c=2.64140255206409\ldots}
\]
such that the following complete global maximizing-direction classification holds:

- When \(0<k<k_c\), precisely the two axial viewing directions maximize projected area; the maximum is \(\pi r^2\).
- At \(k=k_c\), the axial directions and an additional unique oblique latitude circle of unoriented viewing directions are **simultaneously** global maximizers.
- When \(k>k_c\), the only global maximizers are the oblique viewing directions at one latitude, and their shadow area is strictly larger than \(\pi r^2\).

The transition latitude is \(|u_z|=0.58898107634912\ldots\). The critical aspect and the oblique maximizing directions have the following **exact one-dimensional characterizations**. Put
\[
D(\alpha)=\frac\pi2+\alpha,\quad F(\alpha)=\cos\alpha+D(\alpha)\sin\alpha,\quad
H(\alpha)=\sqrt{\frac{D(\alpha)}{\sin\alpha\cos\alpha}}.
\]
Let \(\alpha_s\) be the unique root in \((0,\pi/4)\) of \(\tan(2\alpha_s)=\pi+2\alpha_s\). Let \(\alpha_c\in(0,\alpha_s)\) be the unique solution of
\[
\boxed{D(\alpha_c)\bigl(D(\alpha_c)+\cot\alpha_c\bigr)=\pi^2},
\qquad \boxed{k_c=H(\alpha_c)}.
\]
For every \(k>k_c\), there is a unique \(\alpha(k)\in(0,\alpha_c)\) satisfying \(H(\alpha(k))=k\). The maximizing latitude and normalized maximum brightness are respectively
\[
\boxed{|u_z|=\frac{k\sin\alpha(k)}{\sqrt{1+k^2\sin^2\alpha(k)}}},
\qquad
\boxed{\frac{\max_u A_k(u)}{r^2}=
\frac{kF(\alpha(k))}{\sqrt{1+k^2\sin^2\alpha(k)}}}.
\]
At equality \(k=k_c\), use \(\alpha_c\) in the latitude formula. The assertion classifies **global** maximizers and their competing values, rather than merely classifying the stationary points of the directional shadow-area function.

## Assumptions and scope
The cone is the convex hull of the disk \(\{(x,y,0):x^2+y^2\le r^2\}\) and its axis apex \((0,0,h)\), with \(r,h>0\). Shadows are orthographic, with ordinary two-dimensional area. An azimuthal circle of directions means all unit vectors whose absolute vertical component is fixed; opposite normals give the same unoriented plane. The main result is deterministic (all directions), not an average over a random sample. The scale-free parameter is \(k=h/r\).

## Proof
**1. Exact area profile and change of variables.** Scaling gives \(r=1\). Write \(z=|u_z|\in[0,1]\). The base disk has surface-area measure concentrated at normal \(-e_z\); lateral surface at azimuth \(\phi\) has outward normal times area element \(\frac12(h\cos\phi,h\sin\phi,1)d\phi\). Cauchy's absolute-normal projection formula yields
\[
B_k(z)=\frac{\pi z}{2}+\frac14\int_0^{2\pi}
\bigl|k\sqrt{1-z^2}\cos\phi+z\bigr|\,d\phi.
\]
Consequently \(B_k(z)=\pi z\) if \(z\ge k/\sqrt{1+k^2}\). Otherwise, with \(x=z/(k\sqrt{1-z^2})\in[0,1)\), elementary integration of the absolute cosine gives
\[
B_k(z)=\frac{\pi z}{2}+\sqrt{k^2-(1+k^2)z^2}
+z\arcsin\left(\frac{z}{k\sqrt{1-z^2}}\right).
\]
Writing \(x=\sin\alpha\), the entire nontrivial branch, \(0\le\alpha\le\pi/2\), becomes
\[
\boxed{G_k(\alpha)=\frac{kF(\alpha)}{\sqrt{1+k^2\sin^2\alpha}}}.
\]
The other branch is \(\pi z\), whose unique maximum is \(\pi\) at \(z=1\). Thus the overall maximum is exactly \(\max\{\pi,\max_{0\le\alpha\le\pi/2}G_k(\alpha)\}\).

**2. Uniqueness of the nonaxial candidate.** The cancellation \(F'(\alpha)=D(\alpha)\cos\alpha\) gives
\[
G_k'(\alpha)=\frac{k\cos\alpha}{(1+k^2\sin^2\alpha)^{3/2}}
\left[D(\alpha)-k^2\sin\alpha\cos\alpha\right].
\]
Hence interior stationary angles satisfy \(k=H(\alpha)\). The function \(H\) diverges at both endpoints and has precisely one minimum \(k_s=H(\alpha_s)\). Indeed, the sign of \((H^2)'\) is the sign of
\[
\sin(2\alpha)-(\pi+2\alpha)\cos(2\alpha),
\]
which changes exactly once in \((0,\pi/4)\), because \(\tan(2\alpha)-\pi-2\alpha\) increases strictly from \(-\pi\) to infinity. On \([\pi/4,\pi/2)\) the sign is positive. For \(k\le k_s\), \(G_k\) is increasing (apart from one possible tangency). For \(k>k_s\), \(G_k\) has exactly one interior local maximum, at the smaller root \(\alpha_-(k)\in(0,\alpha_s)\), and one interior local minimum at the larger root. Since \(G_k(\pi/2)=\pi k/\sqrt{1+k^2}<\pi\), only the smaller-root local maximum can ever beat the axial value \(\pi\).

**3. Exactly one crossing with the axial maximum.** Define \(M(k)=\max_{0\le\alpha\le\pi/2}G_k(\alpha)\). For every fixed \(\alpha\),
\[
\frac{\partial G_k(\alpha)}{\partial k}=
\frac{F(\alpha)}{(1+k^2\sin^2\alpha)^{3/2}}>0.
\]
Thus \(M(k)\) is continuous and strictly increasing: evaluating at a maximizing angle for a smaller parameter gives the strict comparison. Furthermore \(M(k)\to0\) as \(k\downarrow0\), whereas \(M(k)\ge G_k(0)=k\to\infty\). There is therefore exactly one \(k_c>0\) with \(M(k_c)=\pi\). At \(k_s\), the nonaxial branch is increasing, so \(M(k_s)=\pi k_s/\sqrt{1+k_s^2}<\pi\). Therefore \(k_c>k_s\), and the only nonaxial maximizer at this crossing is \(\alpha_-(k_c)\).

**4. Exact crossing equation and direction classification.** At a stationary point \(k^2=D(\alpha)/(\sin\alpha\cos\alpha)\), direct simplification yields
\[
G_k(\alpha)^2=\frac{F(\alpha)D(\alpha)}{\sin\alpha}
=D(\alpha)\bigl(D(\alpha)+\cot\alpha\bigr).
\]
Equating this to \(\pi^2\) gives the stated equation for \(\alpha_c\), whose uniqueness on \((0,\alpha_s)\) follows from the unique crossing and the one-to-one smaller-root branch of \(H\). This also proves every equality direction. The numerical constants in the Finding are evaluations of these isolated roots; they are not substitutes for the exact characterizations.

## Verification
The accompanying `verify.py` reconstructs the critical roots, tests the analytic maximum against dense independent directional evaluations through both phases, and reconstructs projected convex hulls of 128-sided approximations to the base disk in 1,200 randomly sampled directions. The maximum observed approximation error is below \(0.002\) in unit-radius area. Reproduce with `python3 verify.py` after installing NumPy and SciPy. These numerical experiments are corroboration; the proof of the sharp crossing and all equality directions is entirely analytic.

## Relationship to prior work
Pennell and Deignan [1] compute the projected area of an arbitrarily oriented right circular cone. Their calculation precedes the present work and the underlying orientation-dependent area formula is **not** claimed new. The exact global maximum-direction competition and sharp transition aspect are separate extremal conclusions. Finch [2] analyzes the surface area and mean width of oblique circular cones and cylinders and asks different geometric optimization questions; Slepian [3] explains Cauchy's general average-shadow formula but does not determine the largest individual cone shadow. Existing work on cone random brightness describes a lower transition at \(k_s=2.14553929088975\ldots\), where two interior stationary points first appear, but does not identify when the oblique local maximum actually overtakes the axial global maximum. The present theorem distinguishes these two thresholds and classifies the global maximizers completely.

## Limitations
No claim is made to a new all-direction cone-shadow formula, the earlier local-stationary-point threshold, or optimality among arbitrary cones or other convex bodies. The historic Pennell–Deignan paper was identifiable from its published abstract, but the full text could not be obtained, so an explicit global optimization in that work cannot be excluded. The computed decimal approximations have no independent formal interval certificate; their rigorously defined mathematical values are the isolated solutions proved above. The analytical proof applies to all real positive aspects, while the finite computations only corroborate its formulas.

## References
[1] S. Pennell and J. Deignan, "Computing the Projected Area of a Cone," SIAM Review 31 (1989), 299–302, DOI: 10.1137/1031052, https://doi.org/10.1137/1031052 (published month June 1989; exact original first-public day not verified).

[2] S. R. Finch, "Oblique Circular Cones and Cylinders," arXiv:1212.5946v1, first public 24 December 2012, https://arxiv.org/abs/1212.5946.

[3] Z. Slepian, "The Average Projected Area Theorem—Generalization to Higher Dimensions," arXiv:1109.0595v1, first public 3 September 2011, https://arxiv.org/abs/1109.0595.
