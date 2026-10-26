# A sharp angular-aperture commutator transition in the two-mode Gaussian Fock space

## Finding
Let \(0<a,b<1\), \(t>0\), and let \(E,F\) be arbitrary Lebesgue-measurable subsets of the angular circle of lengths \(2\pi a\) and \(2\pi b\), respectively. On the normalized Gaussian Fock space, compress the indicators of the disk-clipped angular apertures \(\{re^{i\theta}:0<r<\sqrt t,\ \theta\in E\}\) and \(\{re^{i\theta}:0<r<\sqrt t,\ \theta\in F\}\) to the span of \(1,z\); denote the resulting positive operators by \(A_E(t)\) and \(A_F(t)\).

Set
\[
G(t)=\int_0^t u^{1/2}e^{-u}\,du,\qquad
s_a(t)=\frac{G(t)}{\pi}\sin(\pi a),\qquad
h_a(t)=\frac{at e^{-t}}2,
\]
with analogous definitions for \(b\), and set \(\rho_a(t)=h_a(t)/s_a(t)\). Then the **sharp** commutator norm over all admissible angular masks is
\[
\boxed{
\sup_{|E|=2\pi a,\ |F|=2\pi b}\|[A_E(t),A_F(t)]\|=
\begin{cases}
2\sqrt{(s_a(t)^2+h_a(t)^2)(s_b(t)^2+h_b(t)^2)},&\rho_a(t)\rho_b(t)\le1,\\[2mm]
2\big(h_a(t)s_b(t)+h_b(t)s_a(t)\big),&\rho_a(t)\rho_b(t)\ge1.
\end{cases}}
\]
The two expressions agree at equality. **All maximizing masks** are, up to null sets, single circular arcs of the prescribed angular lengths. If their centers have separation \(\delta\), equality holds exactly when
\[
\cos\delta=-\rho_a(t)\rho_b(t)\quad\text{if }\rho_a(t)\rho_b(t)<1,
\qquad
\delta=\pi\pmod{2\pi}\quad\text{if }\rho_a(t)\rho_b(t)\ge1.
\]
For each fixed \(a,b\), there is a **unique** critical squared radius \(t_{a,b}>0\) where \(\rho_a(t_{a,b})\rho_b(t_{a,b})=1\): below it antipodal arc centers are necessary, while above it the optimal centers separate by a strictly smaller angle in \((\pi/2,\pi)\), tending to \(\pi/2\) as \(t\to\infty\).

## Assumptions and scope
Use \(d\gamma(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\) on \(\mathbb C\). The analytic Gaussian Fock space is \(\mathcal F=\{f\text{ entire}:\int|f|^2d\gamma<\infty\}\). Its orthonormal vectors \(1,z\) span \(H\), and \(P_H\) denotes orthogonal projection from \(L^2(d\gamma)\) onto \(H\). The operator \(A_E(t)\) means \(P_H M_{\mathbf 1_{\Omega_{E,t}}}|_H\), not the full infinite-dimensional Fock Toeplitz operator. The masks are any measurable angular sets; no connectedness, smoothness, or disjointness assumption is imposed. Angular sizes \(a,b\) are fixed, with \(0<a,b<1\); the radius parameter is finite and positive. All operator norms are complex Hilbert-space operator norms.

## Proof
**1. Exact compressed matrices.** Put \(Z_E=\int_E e^{i\theta}\,d\theta\). Direct Gaussian polar integration in the ordered orthonormal basis \((1,z)\) gives
\[
A_E(t)=\begin{pmatrix}
a(1-e^{-t})&\overline{c_E}\\
c_E&a\big(1-(1+t)e^{-t}\big)
\end{pmatrix},\qquad
c_E=\frac{G(t)}{2\pi}Z_E.
\]
Indeed, the two diagonal radial integrals are respectively \(1-e^{-t}\) and \(1-(1+t)e^{-t}\), after accounting for angular fraction; the mixed radial integral is \(G(t)/2\), with the remaining \(1/\pi\) angular normalization. Subtracting a scalar multiple of the identity, the Hermitian traceless part of \(A_E(t)\) is \(\big(\begin{smallmatrix}h_a&\overline{c_E}\\c_E&-h_a\end{smallmatrix}\big)\).

**2. Sharp angular rearrangement.** For every measurable \(E\) of length \(2\pi a\),
\[
|Z_E|\le 2\sin(\pi a).
\]
If \(Z_E\ne0\), rotate the phase so that its real part is \(\int_E\cos\theta\,d\theta\). Among sets of fixed length, the integral of \(\cos\theta\) is maximized uniquely, up to null sets, by the centered arc \((-\pi a,\pi a)\), because it is the superlevel set of \(\cos\theta\) at the unique level providing the desired measure. Its integral is \(2\sin(\pi a)\). The same inequality is trivial if \(Z_E=0\), with strictness because \(0<a<1\). Conversely, rotating a maximizing arc realizes every complex phase of \(c_E\) with modulus exactly \(s_a\).

**3. Sharp matrix optimization and equality.** The traceless Hermitian parts correspond to Bloch vectors \(v_E=(\Re c_E,\Im c_E,h_a)\) and \(v_F=(\Re c_F,\Im c_F,h_b)\), where harmless complex-conjugation conventions reflect both horizontal axes together. The Pauli commutator identity gives
\[
\|[A_E,A_F]\|=2|v_E\times v_F|.
\]
Write \(r=|c_E|\le s_a\), \(u=|c_F|\le s_b\), and \(\delta=\arg(c_F)-\arg(c_E)\). Then
\[
|v_E\times v_F|^2
=h_a^2u^2+h_b^2r^2-2h_a h_b r u\cos\delta+r^2u^2\sin^2\delta.
\]
For any \(r,u>0\), replacing a positive \(\cos\delta\) by its negative never decreases the expression and strictly increases it if \(\cos\delta>0\). With \(\cos\delta\le0\), the right-hand side is strictly increasing in each nonzero radius \(r,u\), since \(h_a,h_b>0\). Cases with a vanishing horizontal radius are likewise strictly dominated by admissible boundary choices. Thus any global maximizer has \(r=s_a\), \(u=s_b\), forcing both masks to be arcs.

Set \(c=\cos\delta\). At the boundary radii the squared cross product is the strictly concave quadratic
\[
H(c)=h_a^2s_b^2+h_b^2s_a^2-2h_a h_b s_a s_b c+s_a^2s_b^2(1-c^2),\qquad -1\le c\le1.
\]
Its unconstrained vertex is \(c_*=-h_a h_b/(s_a s_b)\). If \(h_a h_b\le s_a s_b\), the vertex belongs to \([-1,1]\), and the exact identity \(H(c_*)=(s_a^2+h_a^2)(s_b^2+h_b^2)\) gives the first branch. If \(h_a h_b\ge s_a s_b\), the maximum occurs uniquely at \(c=-1\), where \(H(-1)=(h_a s_b+h_b s_a)^2\). Strict concavity proves the entire equality classification, including the transition point.

**4. Unique critical radius.** Substituting \(u=tv\) in \(G(t)\) yields
\[
\rho_a(t)=\frac{\pi a}{2\sin(\pi a)}\;
\frac{t^{-1/2}}{\int_0^1 v^{1/2}e^{t(1-v)}\,dv}.
\]
The positive numerator factor is constant in \(t\); the power \(t^{-1/2}\) decreases strictly and the positive integral increases strictly. Hence \(\rho_a\rho_b\) is continuous and strictly decreasing from infinity to zero. It crosses one exactly once. The angular statements follow from \(\cos\delta=-\min\{1,\rho_a\rho_b\}\).

## Verification
The accompanying executable \(verify.py\) checks the exact Pauli commutator identity and the two quadratic optimization identities symbolically. It separately compares all three matrix entries against direct Gaussian radial quadratures, checks the sharp bound on sampled arbitrary disconnected angular masks, reproduces equality for optimal sectors across both branches, and numerically verifies several unique critical roots. It passed 1,353 checks. These finite checks corroborate normalization; the arbitrary-mask and all-radius assertions are established by the analytic argument above.

For example, when \(a=b=1/2\), the unique critical squared radius is approximately \(t_{a,b}=0.739402495523\), equivalently \(\sqrt{t_{a,b}}\approx0.859885164149\). For larger radii, two semicircular angular windows maximize their commutator at an angle strictly between a right angle and a straight angle; for smaller radii the optimal centers are antipodal.

## Relationship to prior work
Keller and Luef develop Fock and polyanalytic Toeplitz quantization and a semiclassical commutator calculus. Their operator-symbol asymptotics do not supply an exact sharp optimization over discontinuous disk-clipped angular masks in the fixed two-dimensional polynomial sector. Dewage and Ólafsson analyze the commutative family of quasi-radial Fock Toeplitz operators; angular masks here are nonradial and create a radius-dependent noncommutativity phenomenon. Galbis proves norm estimates for radial Fock Toeplitz symbols; these do not determine the two-aperture commutator or the arc rigidity. Existing general matrix-commutator algebra and one-dimensional rearrangement facts are used explicitly rather than claimed as new; the contribution is the sharp Fock-aperture geometry, its complete measurable-shape equality classification, and its unique radial orientation transition.

## Limitations
The result applies only to the two-dimensional Fock subspace \(\operatorname{span}\{1,z\}\), to apertures with a common finite radial cutoff, and to angularly measurable binary masks of prescribed measures. It makes no statement about the operator norm of commutators on the full Gaussian Fock space, arbitrary radial profiles, or bands of dimension three and higher. An equivalent special-case calculation in unindexed Toeplitz or angular rearrangement literature cannot be excluded solely by bibliographic searching. No independent external mathematical audit has been performed.

## References
1. J. Keller and F. Luef, *Polyanalytic Toeplitz operators: isomorphisms, symbolic calculus and approximation of Weyl operators*, arXiv:1905.07741 (first posted 2019-05-19), later *J. Fourier Anal. Appl.* 27 (2021), 47. https://arxiv.org/abs/1905.07741
2. V. Dewage and G. Ólafsson, *Toeplitz operators on the Fock space with quasi-radial symbols*, arXiv:2107.01465 (first posted 2021-07-03), later *Complex Anal. Oper. Theory* 16 (2022), 61. https://arxiv.org/abs/2107.01465
3. A. Galbis, *Norm estimates for selfadjoint Toeplitz operators on the Fock space*, arXiv:2102.02031 (first posted 2021-02-03). https://arxiv.org/abs/2102.02031
