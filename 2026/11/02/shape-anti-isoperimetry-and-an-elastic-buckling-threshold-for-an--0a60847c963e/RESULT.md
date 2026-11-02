# Shape anti-isoperimetry and an elastic buckling threshold for an active ideal gas

## Finding

An ideal gas made of independent, coordinate-wise telegraph swimmers has a strictly anti-isoperimetric quasistatic shape response. At fixed box volume, the equal-sided box is the unique shape giving the **least work by the gas** during deformation from that box, and increasing anisotropy always gives positive work. This remains an **exact** result in every spatial dimension, rather than an approximation obtained by imposing a one-dimensional run-and-tumble closure in higher dimensions.

Fix \(d\ge2\), \(D>0\), \(v>0\), \(\alpha>0\), a number of noninteracting particles \(n\ge1\), and bath temperature \(T>0\) related to the drag coefficient by \(D=k_{\mathrm B}T/\gamma\). Each particle has independent Cartesian components \(X_i\in[0,L_i]\); each component undergoes reflected diffusion with drift \(v\sigma_i\), where its orientation \(\sigma_i\in\{-1,+1\}\) flips at rate \(\alpha\), independently of the other coordinates. All box lengths are positive, and the thermal and active parameters stay fixed during the quasistatic process. This is the **Cartesian-product telegraph model**, not a constant-speed, uniformly reoriented particle on a sphere.

Write
\[
q=\frac{v^2}{2\alpha D}>0,\quad \kappa=\sqrt{\frac{v^2}{D^2}+\frac{2\alpha}{D}},\quad \theta(z)=\frac{\tanh z}{z},\quad F(L)=\frac{1+q}{1+q\theta(\kappa L/2)}.
\]
Then the exact normal pressure on a pair of faces perpendicular to the \(i\)-th axis is
\[
P_i=\frac{nk_{\mathrm B}T}{V}F(L_i),\qquad V=\prod_{j=1}^d L_j.
\]
Set \(H(s)=\int_0^s F(e^u)\,du\). The work done **by** the gas during any quasistatic protocol from \(\mathbf L^{(0)}\) to \(\mathbf L^{(1)}\) equals
\[
W= nk_{\mathrm B}T\sum_{i=1}^d\bigl[H(\log L_i^{(1)})-H(\log L_i^{(0)})\bigr].
\]
Thus quasistatic work is path-independent at fixed activity, even though the gas is out of equilibrium, and is zero around every closed shape cycle. On the fixed-volume surface, \(\sum_i H(\log L_i)\) is **strictly Schur-convex in the logarithmic lengths**, uniquely minimized by the equal-sided box. For an equal-sided reference with length \(a=V^{1/d}\), stretch two axes to \(ae^t\) and \(ae^{-t}\), keeping the others fixed. With
\[
G(t)=H(\log a+t)+H(\log a-t)-2H(\log a),
\]
we have \(G(t)>0\) for every \(t\ne0\), and the sharp laws
\[
G(t)=aF'(a)t^2+O(t^4)\quad(t\to0),\qquad
G(t)=q|t|+C_a+o(1)\quad(|t|\to\infty)
\]
for some finite constant \(C_a\). In particular, at fixed area the extractable distortion work grows as \(\tfrac12 nk_{\mathrm B}Tq\log(L_1/L_2)+O(1)\) as \(L_1/L_2\to\infty\).

As a concrete mechanical consequence, let an otherwise freely deformable two-dimensional fixed-area box have an additional restoring energy \(Kt^2/2\) for \(t=\tfrac12\log(L_1/L_2)\), with \(K>0\). Its quasistatic force-balance potential is \(U_K(t)=Kt^2/2-nk_{\mathrm B}TG(t)\). The symmetric square loses local stability at the **exact stiffness threshold**
\[
K_c=2nk_{\mathrm B}T\,aF'(a)>0.
\]
For \(0<K<K_c\), the square is a strict local maximum of \(U_K\), and at least one pair of nonzero, opposite-sign **global minimizers** exists. For every choice of positive global minimizer \(t_K\) as \(K\downarrow0\),
\[
Kt_K\longrightarrow nk_{\mathrm B}Tq.
\]
No claim of uniqueness of the off-center minimizers, nor a classification at \(K=K_c\), is made.

## Assumptions and scope

The hard-wall diffusion is reflected in position while leaving each orientation unchanged. The stationary distribution is the product of the unique stationary laws of the one-dimensional reflected telegraph diffusions. Thermal noise is indispensable here: \(D>0\) ensures a regular wall contact density. The pressure is the mechanical contact force of ideal point particles, \(nk_{\mathrm B}T\) times the one-coordinate wall density per transverse area. Quasistatic means that the state equilibrates to its stationary nonequilibrium law at every box shape; the active drive continues to supply energy. The Hookean term is an externally specified shape elasticity and does not arise from particle interactions.

## Proof

For one coordinate, write the stationary orientation-resolved densities \(p_\pm(x)\). Their forward equations and individual reflecting conditions are
\[
0=Dp_\pm''\mp vp_\pm'+\alpha(p_\mp-p_\pm),\qquad
(\pm vp_\pm-Dp_\pm')\big|_{x=0,L}=0.
\]
Let \(\rho=p_++p_-\) and \(m=p_+-p_-\). Summing gives \(D\rho'-vm=0\) throughout the interval, while subtraction gives \(Dm''-v\rho'-2\alpha m=0\). Hence \(\rho'''=\kappa^2\rho'\). Reflection symmetry and the difference of the no-flux equations yield \(D^2\rho''=v^2\rho\) at the endpoints. The normalized solution is
\[
\rho_L(x)=\frac{1+q\cosh(\kappa(x-L/2))/\cosh(\kappa L/2)}{L[1+q\theta(\kappa L/2)]}.
\]
Indeed \(\int_0^L\rho_L(x)dx=1\); the conditional densities are recovered from \(p_\pm=(\rho\pm D\rho'/v)/2\), and are nonnegative as required by the underlying irreducible reflected process. The wall contact density satisfies \(L\rho_L(L)=F(L)\). The reflecting boundary's mean local-time force is \(k_{\mathrm B}T\rho_L(L)\) per particle, so tensorization gives the displayed pressure. This reproduces the exact one-dimensional run-and-tumble contact law while making the multidimensional Cartesian-product construction explicit.

With \(V_i\) the volume displaced by moving face \(i\), \(dV_i=V\,dL_i/L_i\). Inserting the pressure into \(dW=\sum_iP_i\,dV_i\) gives the exact differential \(dW=nk_{\mathrm B}T\sum_i F(L_i)\,d\log L_i\), hence the potential and closed-cycle claim.

For \(z>0\),
\[
-\theta'(z)=\frac{\tanh z-z\operatorname{sech}^2z}{z^2}>0,
\]
because the numerator vanishes at zero and has derivative \(2z\operatorname{sech}^2z\tanh z>0\). Consequently \(F'(L)>0\), so \(H''(s)=e^sF'(e^s)>0\). Strict convexity and pairwise averaging prove strict Schur-convexity and the unique fixed-volume minimizer. Since \(F(L)\to1\) as \(L\downarrow0\) and \(F(L)\to1+q\) as \(L\to\infty\),
\[
G'(t)=F(ae^t)-F(ae^{-t})\in(0,q)\quad(t>0),\qquad G'(t)\to q.
\]
Taylor expansion gives the quadratic law; \(F(ae^t)-(1+q)=O(e^{-t})\) and \(F(ae^{-t})-1=O(e^{-2t})\) yield the constant-remainder asymptotic after integration.

Finally, \(U_K\) is even, smooth, and coercive since \(G(t)=O(|t|)\). Its second derivative at zero is \(U_K''(0)=K-2nk_{\mathrm B}TaF'(a)\). For \(K<K_c\), the origin is a strict local maximum; coercivity ensures nonzero global minima in opposite pairs. For \(K\downarrow0\), evaluate \(U_K\) at \(t=nk_{\mathrm B}Tq/(2K)\): its value tends to \(-\infty\) at order \(1/K\), so every global minimizer escapes to infinity. A positive minimizer obeys \(Kt_K=nk_{\mathrm B}TG'(t_K)\); taking the limit proves the final sharp law.

## Verification

The companion standalone `check.py` independently tests normalization, reflecting boundary identities, wall pressure, strict order, the work potential against a direct force integral, local second variations, large-aspect slopes and a positive-integral representation for \(-\theta'\). It reports 1670 successful deterministic checks. These checks are not used to infer the all-parameter theorem; the analytical argument above does that.

## Relationship to prior work

Li, Eichhorn and Dabelow (2026) derived the exact **one-dimensional** run-and-tumble confinement density and pressure formula, together with a rectangular-box work formula for a **higher-dimensional AOUP approximation**. Both are credited here. Their constant-speed, uniformly reorienting multidimensional RTP is not the product-telegraph model used in this theorem. The added conclusions are the exact high-dimensional product-telegraph realization, full log-majorization ordering, vanishing quasistatic shape-cycle work, unbounded fixed-volume distortion work, and the exact compliant-box stiffness threshold and weak-stiffness aspect law.

Nikola et al. (2015) found a flexible-wall modulational instability arising from pressure nonuniformity along curved boundaries in a thermodynamic-limit active system, rather than this finite-volume rectangular global shape mode. Ezhilan et al. (2015) derived confinement-dependent swim pressure between plates for athermal orientable swimmers, without a globally deformable fixed-volume box. These are related physical mechanisms, not equivalent claims.

## Limitations

The result does **not** describe spherical-orientation RTPs, interacting particles, AOUPs exactly, finite-speed wall actuation, a fluctuating elastic box, or a general dynamical instability without a specified quasistatic mobility law. The unbounded aspect-work limit assumes ideal point particles and a mathematical hard-wall box even as one dimension shrinks to zero; finite-size particles and wall elasticity beyond the stated law will regularize it. Because the underlying one-dimensional pressure was already available, some aspects of the tensorized pressure and convexity consequences may be regarded as implicit in the prior equation; publication-priority assessment remains qualified and independent audit has not occurred.

## References

1. S. Li, R. Eichhorn, L. Dabelow, *Ideal gas of active particles in a box*, arXiv:2610.01287v1 (first submitted 2026-10-01), https://arxiv.org/abs/2610.01287 . Main text, especially equations (1), (11), (14)-(17), and supplementary section S2.
2. N. Nikola, A. P. Solon, Y. Kafri, M. Kardar, J. Tailleur, R. Voituriez, *Active particles with soft and curved walls: Equation of state, ratchets, and instabilities*, arXiv:1512.05697 (2015), https://arxiv.org/abs/1512.05697 .
3. B. Ezhilan, R. Alonso-Matilla, D. Saintillan, *On the distribution and swim pressure of run-and-tumble particles in confinement*, arXiv:1507.06379 (2015), https://arxiv.org/abs/1507.06379 .
