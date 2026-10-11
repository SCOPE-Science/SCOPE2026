# Sharp fourth-order dual deviation of the disk for inscribed triangles

## Finding

Let \(B_2=\{x\in\mathbb R^2:\lVert x\rVert_2\le1\}\), and let \(\mathcal T\) consist of all nondegenerate triangles \(T\subset B_2\) with \(0\in\operatorname{int}T\). In the dual-volume normalization of Besau--Hoehner--Kur, define
\[
\widetilde\Delta_4(B_2,T)
=\pi\int_{S^1}\bigl(1-\rho_T(u)^4\bigr)\,d\sigma(u)
=\pi-\frac12\int_0^{2\pi}\rho_T(\theta)^4\,d\theta,
\]
where \(d\sigma=d\theta/(2\pi)\). Then
\[
\boxed{\inf_{T\in\mathcal T}\widetilde\Delta_4(B_2,T)=\pi-\frac23.}
\]
The infimum is *not attained*. Any minimizing sequence (modulo rotations, reflections, and passage to subsequences) tends to the right-isosceles triangle with vertices \((1,0),(-1,0),(0,1)\). Equivalently, this boundary triangle has the origin at the midpoint of its hypotenuse. It is outside the admissible class because the origin is not interior.

More precisely, if the three vertices lie on \(S^1\), let the successive positive central gaps be \(2\alpha_1,2\alpha_2,2\alpha_3\), with
\[
0<\alpha_j<\frac\pi2,\qquad \alpha_1+\alpha_2+\alpha_3=\pi.
\]
Put \(s_j=\sin(\pi-2\alpha_j)\). The *exact positive gap identity* is
\[
\boxed{\widetilde\Delta_4(B_2,T)-\left(\pi-\frac23\right)
=\frac13\big[(1-s_1)(1-s_2)+(1-s_3)(1-s_1s_2)\big].}
\]
The same identity, of course, holds after relabeling the three vertices. It proves strict positivity in the open parameter domain and classifies all possible boundary equality shapes.

The regular inscribed triangle is not a local minimizer of \(\widetilde\Delta_4\): its second variation vanishes on angular-gap perturbations, but a nonzero cubic variation changes sign. This is qualitatively different from \(q=2\), when the deviation is the ordinary area deficit and the regular triangle is globally optimal.

## Assumptions and scope

All triangles are nondegenerate, Euclidean, contained in the closed unit disk, and contain the *fixed origin* strictly in their interiors. The origin cannot be moved to the triangle's centroid. All dual-volume assertions use the \(q=4\) extension for \(d=2\), where the normalization constant is \(\kappa_2=\pi\). No assertions concern triangles with the origin outside or the unrestricted placement of a shifted disk.

The radial function is \(\rho_T(u)=\sup\{r\ge0:ru\in T\}\). Since \(T\subset B_2\), \(0<\rho_T\le1\). The expression is therefore an ordinary positive radial deficit.

## Proof

**Step 1: move all vertices to the unit circle.** Let \(v_1,v_2,v_3\) be the vertices of \(T\), and replace \(v_i\) by \(w_i=v_i/\lVert v_i\rVert_2\). Because \(0\in\operatorname{int}T\), the radial rays \(\mathbb R_{>0}v_i\) are distinct, and a positive convex combination of the \(v_i\) is zero. Multiplying those positive coefficients by \(\lVert v_i\rVert_2\) shows that \(0\in\operatorname{int}\operatorname{conv}\{w_i\}\). Also \(v_i\) lies on the segment joining \(0\) and \(w_i\); hence
\[
T\subseteq T'=\operatorname{conv}\{w_1,w_2,w_3\}\subset B_2.
\]
Since the fourth radial moment is monotone under inclusion, it suffices to maximize the moment for three boundary vertices. If some \(\lVert v_i\rVert_2<1\), the inclusion is strict on positive area, so the fourth moment increases strictly.

**Step 2: exact radial integral.** For a boundary triangle containing \(0\) strictly, every consecutive circular gap is smaller than \(\pi\); write it \(2\alpha_i\). In coordinates centered on the outward normal to the corresponding edge, that edge has support line \(r\cos t=\cos\alpha_i\), for \(-\alpha_i\le t\le\alpha_i\). Thus the radial integral contributed by its sector is
\[
I_4(\alpha_i)=\int_{-\alpha_i}^{\alpha_i}
\left(\frac{\cos\alpha_i}{\cos t}\right)^4\!dt
=2\cos^4\alpha_i\left(\tan\alpha_i+\frac13\tan^3\alpha_i\right)
=\frac{\sin2\alpha_i\,(2+\cos2\alpha_i)}3.
\]
The three sectors partition \(S^1\), so \(\int_0^{2\pi}\rho_T^4=\sum_{i=1}^3 I_4(\alpha_i)\).

**Step 3: sharp three-parameter factorization.** Put \(\theta_i=\pi-2\alpha_i\). Then \(\theta_i\in(0,\pi)\), \(\sum\theta_i=\pi\), and \(s_i=\sin\theta_i\in[0,1]\). The trigonometric identity
\[
\sin2\theta_1+\sin2\theta_2+\sin2\theta_3
=4\sin\theta_1\sin\theta_2\sin\theta_3
\qquad(\theta_1+\theta_2+\theta_3=\pi)
\]
gives
\[
\int_0^{2\pi}\rho_T^4\,d\theta
=\frac23\left(s_1+s_2+s_3-s_1s_2s_3\right).
\]
For any \(s_1,s_2,s_3\in[0,1]\) we have the exact factorization
\[
2-s_1-s_2-s_3+s_1s_2s_3
=(1-s_1)(1-s_2)+(1-s_3)(1-s_1s_2)\ge0.
\]
Equality requires at least two of the \(s_i\) to be \(1\). Given \(\theta_i\ge0\) and \(\sum\theta_i=\pi\), this forces \((\theta_1,\theta_2,\theta_3)\) to be a permutation of \((0,\pi/2,\pi/2)\). Consequently \((\alpha_1,\alpha_2,\alpha_3)\) must tend to a permutation of \((\pi/2,\pi/4,\pi/4)\). These and only these limiting central-gap triples yield a right-isosceles triangle with a diameter edge. None has \(0\) in its interior. The displayed deficit formula follows on multiplying by \(1/3\).

**Step 4: attainment and limiting rigidity.** Set
\[
\alpha_1=\frac\pi2-\varepsilon,\qquad
\alpha_2=\alpha_3=\frac\pi4+\frac\varepsilon2,
\qquad 0<\varepsilon<\frac\pi2.
\]
For all sufficiently small \(\varepsilon>0\) this defines a valid boundary-vertex triangle with \(0\) interior. As \(\varepsilon\downarrow0\), the fourth moment tends to \(4/3\), so the deviation approaches \(\pi-2/3\). The factorization proves strict nonattainment. By compactness of triples of vertices of \(B_2\), continuity of the polar moment \(\frac14\int\rho_T^4=\int_T\lVert x\rVert_2^2dx\), strict monotonicity under radial extension, and uniqueness of boundary equality triples, every minimizing sequence modulo plane isometries has only the described limiting shape. In the displayed symmetric family, the exact gap is
\[
\widetilde\Delta_4(B_2,T_\varepsilon)-(\pi-2/3)
=\frac13\Big(2-\sin2\varepsilon-2\cos\varepsilon+\sin2\varepsilon\cos^2\varepsilon\Big)
=\frac{\varepsilon^2}{3}+O(\varepsilon^3).
\]

**Step 5: nonregularity and local cubic mechanism.** The inscribed equilateral triangle has \(\alpha_i=\pi/3\) and fourth moment \(3\sqrt3/4<4/3\). Its deviation is \(\pi-3\sqrt3/8>\pi-2/3\). Set \(F(\alpha)=I_4(\alpha)\). Direct differentiation gives \(F''(\pi/3)=0\) and \(\frac{d^3F}{d\alpha^3}(\pi/3)=8\). Along the admissible perturbation
\[
(\alpha_1,\alpha_2,\alpha_3)=(\pi/3+t,\pi/3+t,\pi/3-2t)
\]
we obtain
\[
\sum_i F(\alpha_i)-3F(\pi/3)=-8t^3+O(t^4).
\]
Thus both signs occur for sufficiently small \(t\), so equilateral symmetry is a degenerate saddle rather than a local minimizer of the fourth dual deviation. In contrast, at \(q=2\) one has \(I_2(\alpha)=\sin2\alpha\), giving the ordinary area-maximizing equilateral triangle by the classical inscribed-triangle theorem.

## Verification

All optimization claims follow from the exact trigonometric and nonnegative-product identities above; no numerical enumeration is used as a proof. A standalone standard-library script `verify.py` checks the factorization on an exact rational grid, compares the angular radial formula against an independent barycentric polar-moment formula for sample inscribed triangles, and checks the right-isosceles limiting moment and the sign-changing cubic perturbation. Run `python3 verify.py`. Finite numerical checks are supplementary to Steps 1–5.

## Relationship to prior work

Hoehner, Schütt and Werner (arXiv:2608.02554v1, first made public August 3, 2026) establish general nonasymptotic lower estimates for \(\widetilde\Delta_q\) with prescribed face count; see their Theorem 3.7, its sphere-covering proof, and the discussion of order-sharp large-\(N\) estimates. The theorem here gives instead the **exact sharp small-\(N\)** value for \((d,M,q)=(2,3,4)\), and a boundary nonattainment classification, neither an immediate implication of general nonasymptotic estimates nor a claim about higher-dimensional optimal polytopes. The normalized fourth dual deviation was defined in earlier work of Besau, Hoehner and Kur (arXiv:1905.08862); that work focuses on general inequalities and asymptotic polytope approximation. The \(q=2\) area-maximizing equilateral triangle is classical and is not claimed new.

## Limitations

This is a single exact finite-vertex case at exponent \(q=4\) in dimension two. It does **not** classify the minimizers at other \(q\), other vertex counts, or bodies whose containing disk may translate. Independent review of the original claim has not been performed. Literature equivalences not indexed or available in full text remain possible.

## References

1. S. Hoehner, C. Schütt, E. M. Werner, *Dual volume approximation of the Euclidean ball by polytopes with a fixed number of k-faces*, arXiv:2608.02554v1 (August 3, 2026), https://arxiv.org/html/2608.02554v1 .
2. F. Besau, S. Hoehner, G. Kur, *Intrinsic and Dual Volume Deviations of Convex Bodies and Polytopes*, arXiv:1905.08862 (2019), https://arxiv.org/abs/1905.08862 .
