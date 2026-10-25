# Transverse long spikes defeat Steiner-point overlap alignment

## Finding
Let \(d\ge2\), let \(B_d\subset\mathbb R^d\) be the closed unit Euclidean ball, and let \(e_1,\ldots,e_d\) be an orthonormal basis. For each \(t>1\), form the \(d\) full-dimensional convex bodies
\[
C_{i,t}=\operatorname{conv}(B_d\cup\{t e_i\}),\qquad 1\le i\le d.
\]
Let \(s(K)\) be the Steiner point of a convex body \(K\), and write
\[
N_d(t)=\operatorname{vol}_d\!\left(\bigcap_{i=1}^d(C_{i,t}-s(C_{i,t}))\right),\qquad
M_d(t)=\sup_{v_1,\ldots,v_d\in\mathbb R^d}\operatorname{vol}_d\!\left(\bigcap_{i=1}^d(C_{i,t}+v_i)\right).
\]
Then the sharp **asymptotic efficiency of Steiner alignment on this family** is
\[
\boxed{\lim_{t\to\infty}\frac{N_d(t)}{M_d(t)}=2^{-d}.}
\]
More precisely, with
\[
D_d=\bigcap_{i=1}^d\{x:\|x-(x\cdot e_i)e_i\|_2\le1\},
\]
one has \(N_d(t)\to 2^{-d}\operatorname{vol}_d(D_d)\) and \(M_d(t)\to\operatorname{vol}_d(D_d)\). In the plane, \(D_2=[-1,1]^2\), so the respective overlap areas tend to \(1\) and \(4\). In particular, Steiner-point alignment has planar two-body worst-case efficiency **at most \(1/4\)**, strictly below the exact \(4/9\) worst-case guarantee for centroid alignment.

## Assumptions and scope
All intersections and volumes are ordinary Euclidean ones, and each translation vector is independently chosen when defining \(M_d(t)\). A convex body here is compact, convex, and has nonempty interior. The Steiner point is normalized by
\[
s(K)=\frac{d}{\sigma(S^{d-1})}\int_{S^{d-1}} h_K(u)u\,d\sigma(u),\qquad h_K(u)=\max_{x\in K}\langle x,u\rangle.
\]
This definition also extends continuously to lower-dimensional compact convex sets. The result is for \(d\) orthogonal spikes in dimension \(d\) (in particular two bodies in the plane). It is not an exact determination of the worst-case constant over all families.

## Proof
**1. Cylindrical constraint and its optimal translated intersection.** Put
\[
T_i(r)=\{x:\|x-(x\cdot e_i)e_i\|_2\le r\},\qquad D_d(r)=\bigcap_i T_i(r)=rD_d.
\]
Every \(C_{i,t}\) is contained in \(T_i(1)\), which is invariant under translations along \(e_i\). Moreover \(D_d\) is bounded: summing the inequalities defining \(D_d\) gives
\[
(d-1)\|x\|_2^2\le d,
\]
so \(\|x\|_2\le R_d:=\sqrt{d/(d-1)}\). It has positive volume because it contains \(B_d\).

For arbitrary vectors \(v_i\), set \(E=\bigcap_i(T_i(1)+v_i)\). This is bounded (every coordinate is bounded by at least one cylinder transverse to that coordinate). Since every cylinder is centrally symmetric, \(-E=\bigcap_i(T_i(1)-v_i)\), and convexity gives
\[
\frac{E+(-E)}2\subseteq D_d.
\]
For nonempty \(E\), Brunn--Minkowski implies \(\operatorname{vol}_d(E)\le\operatorname{vol}_d((E-E)/2)\le\operatorname{vol}_d(D_d)\). The empty case is immediate. Hence \(M_d(t)\le\operatorname{vol}_d(D_d)\) for every \(t\).

**2. Long-spike sections.** A supporting line from \(t e_i\) tangent to the unit ball touches it at axial coordinate \(1/t\). Therefore, for \(1/t\le z\le t\), the section of \(C_{i,t}\) at \(x\cdot e_i=z\) is a centered \((d-1)\)-ball of radius
\[
\rho_t(z)=\frac{t-z}{\sqrt{t^2-1}}.
\]
(The formula follows from the right triangle having axial distance \(t-1/t\) and tangential radius \(\sqrt{1-t^{-2}}\).) It applies in all dimensions.

**3. Steiner-center location.** By rotational symmetry about \(e_i\), write \(s(C_{i,t})=a_t e_i\), with the same \(a_t\) for all \(i\). The segment \(S_{i,t}=[0,t e_i]\) is contained in \(C_{i,t}\), and every point of \(C_{i,t}\) is within distance one of some point of \(S_{i,t}\). Thus their Hausdorff distance is at most one, whence their support functions differ by at most one. The displayed Steiner integral and \(s(S_{i,t})=(t/2)e_i\) yield
\[
\left|a_t-\frac t2\right|\le d.
\]
In particular \(a_t/t\to1/2\). In dimension two one can also integrate \(h_{C_{1,t}}(\cos\theta,\sin\theta)=\max(1,t\cos\theta)\) explicitly to obtain
\[
a_t=\frac{t\arccos(1/t)-\sqrt{1-t^{-2}}}{\pi}.
\]

**4. Explicit volume brackets for Steiner alignment.** For all sufficiently large \(t\), set
\[
\ell_t=\frac{t/2-d-R_d}{\sqrt{t^2-1}},\qquad
u_t=\frac{t/2+d+R_d}{\sqrt{t^2-1}}.
\]
Both are positive and smaller than one. Whenever \(x\in D_d\), each axial coordinate \(x\cdot e_i+a_t\) lies in \([1/t,t]\), and the section formula gives a transverse radius between \(\ell_t\) and \(u_t\). Since the centered intersection is contained in \(D_d\) and points of \(D_d(\ell_t)\) have transverse norm at most \(\ell_t\), it follows that
\[
D_d(\ell_t)\subseteq\bigcap_i(C_{i,t}-a_t e_i)\subseteq D_d(u_t).
\]
Taking volumes,
\[
\ell_t^d\operatorname{vol}_d(D_d)\le N_d(t)\le u_t^d\operatorname{vol}_d(D_d).
\]
As \(t\to\infty\), both parameters tend to \(1/2\), proving \(N_d(t)\to2^{-d}\operatorname{vol}_d(D_d)\).

**5. Translations attaining the cylindrical limit.** Translate each spike **backward by \(\sqrt t\)** and put
\[
q_t=\frac{t-\sqrt t-R_d}{\sqrt{t^2-1}}.
\]
For sufficiently large \(t\), one has \(0<q_t<1\) and the section identity gives
\[
D_d(q_t)\subseteq\bigcap_i(C_{i,t}-\sqrt t\,e_i)\subseteq D_d.
\]
Indeed, on \(D_d\) every axial coordinate has absolute value at most \(R_d\), while \(\rho_t(x\cdot e_i+\sqrt t)\ge q_t\). Thus
\[
q_t^d\operatorname{vol}_d(D_d)\le M_d(t)\le\operatorname{vol}_d(D_d).
\]
Since \(q_t\to1\), the claimed limit follows. Equivalently, for all sufficiently large \(t\) the efficiency lies in the explicit interval
\[
\ell_t^d\le\frac{N_d(t)}{M_d(t)}\le \left(\frac{u_t}{q_t}\right)^d,
\]
whose endpoints both tend to \(2^{-d}\).

## Verification
Run `python3 verify_spike_selector.py` in a standard Python environment. It independently evaluates the planar Steiner support-function integral by midpoint quadrature and checks the closed formula, the elementary \(d\)-dimensional certified ratio bounds, and the strict planar comparison with \(4/9\). The verification output is numerical corroboration only; the proof of the limit uses the exact inclusions and Brunn--Minkowski, not discretization.

## Relationship to prior work
Feldman, *Arranging convex bodies for maximum intersection volume: the sharp efficiency of centroid alignment* (arXiv:2608.04516v1, August 5, 2026), proves the centroid-selector worst-case \(4/9\) for two planar bodies and explicitly identifies the Steiner point as a natural selector to test in Question 20. That theorem treats centroids, not Steiner points, and its cone construction does not state the transverse-spike selector comparison proved here. The support-integral definition and Minkowski additivity of the Steiner point are classical; their use here is not claimed as new. Brunn--Minkowski supplies the standard comparison for translations of centrally symmetric cylinders.

## Limitations
The construction gives an **upper bound** \(2^{-d}\) on the unrestricted worst-case efficiency for \(d\) bodies under Steiner alignment, not equality for that unrestricted infimum. It proves a strict selector separation from centroids in the plane, but does not determine the best selector or establish an analogous ordering in higher dimensions. The shapes used are smooth except where the long conical sheets meet the original balls. Exact finite-\(t\) optimizing translations are not classified; only their asymptotic optimal value is established. Possible unindexed earlier results on Steiner-aligned overlap remain an originality risk.

## References
1. D. V. Feldman, *Arranging convex bodies for maximum intersection volume: the sharp efficiency of centroid alignment*, arXiv:2608.04516v1, first public August 5, 2026, https://arxiv.org/html/2608.04516v1 .
2. R. Schneider, *On Steiner points of convex bodies*, Israel Journal of Mathematics 9 (1971), 241–249. Classical Steiner selector background.
3. *A note on a problem posed by Linderholm*, Journal of Geometry (2025), https://doi.org/10.1007/s00022-025-00783-4 . Contains the support-function integral defining the planar Steiner point.
4. Standard Brunn--Minkowski inequality for compact convex bodies; see the references within Feldman (2026), particularly Schneider's convex-body monograph.
