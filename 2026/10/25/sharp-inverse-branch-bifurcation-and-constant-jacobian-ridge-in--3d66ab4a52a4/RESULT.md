# Sharp inverse-branch bifurcation and constant-Jacobian ridge in risk-sensitive learning dynamics

## Finding
For the two-dimensional adaptive-belief multiplicative-weights map described below, put
\[
 A=a\left(1-\frac{ckp_1}{1-k}\right).
\]
On the open population-state strip with an unrestricted belief coordinate, the map is one-to-one exactly when \(A\le4\); it is a smooth global diffeomorphism exactly when \(A<4\). When \(A>4\), its complete inverse-image census is one or three simple preimages, separated by two explicit caustic curves (two distinct preimages at the caustics). Both folds genuinely occur inside the physically allowed square, and an output with three distinct physical preimages exists. The caustic band has exact width and onset law
\[
 W(A)=A r-4\operatorname{artanh}r
 =\frac{(A-4)^{3/2}}3+O((A-4)^{5/2}),
 \qquad r=\sqrt{1-4/A}.
\]
At \(A=4\), the inverse becomes cubic-root singular, although forward injectivity persists. A separate exact geometric consequence of the same reduction is that, for \(k=1/(1+cp_1)\), the log-odds-coordinate Jacobian determinant is the constant \(1-k\), regardless of the learning intensity. Accordingly, every compactly supported invariant probability has Lyapunov-exponent sum \(\log(1-k)\), and every compact *fully invariant* set in the interior has planar Lebesgue area zero.

## Assumptions and scope
Let \(a>0\), \(c>1\), \(p_1>0\), \(0\le p_0\), \(p_0+p_1\le1\), \(b\in(0,1)\), and \(0<k<1\). The physical phase space is \((0,1)\times[0,1]\), and its smooth analytic extension is \((0,1)\times\mathbb R\). Set
\[
 X=\frac{x}{x+(1-x)\exp(a(x-b+cq))},\qquad
 Q=(1-k)q+k(p_0+p_1x),\qquad F(x,q)=(X,Q).
\]
Every physical point maps into the physical space. The symbol \(X\) always denotes the new population state, while \(x\) is the old one. The results about the exact one-versus-three inverse count refer to the analytic extension; the existence of three preimages in the physical square is asserted separately. No claim that *every* output in the caustic band has three physical preimages is made. The area and Lyapunov conclusions require compact invariant sets/measures contained in the interior \(0<x<1\); they do not concern measures concentrated on the boundary.

## Proof
**1. An exact scalar inverse equation.** Introduce log odds \(y=\log(x/(1-x))\) and \(Y=\log(X/(1-X))\). Direct substitution gives
\[
 Y=y-a(x-b+cq),\qquad Q=(1-k)q+k(p_0+p_1x).
\]
At a specified target \((Y,Q)\), the second equation determines
\[
 q=\frac{Q-k(p_0+p_1x)}{1-k}.
\]
Substitution in the first equation leaves one scalar equation:
\[
 \Phi_A(x)=H(Y,Q),\quad
 \Phi_A(x)=\log\frac{x}{1-x}-Ax,\quad
 H(Y,Q)=Y-ab-\frac{ackp_0}{1-k}+\frac{acQ}{1-k}.
\]
Thus the entire inverse-fiber problem is one-dimensional. Since \(\Phi_A(x)\to-\infty\) as \(x\downarrow0\) and \(\Phi_A(x)\to+\infty\) as \(x\uparrow1\), at least one inverse always exists in the extended strip.

**2. The complete inverse multiplicity.** We have
\[
 \Phi_A'(x)=\frac1{x(1-x)}-A.
\]
The first term has global minimum \(4\), achieved uniquely at \(x=1/2\). If \(A<4\), the derivative is strictly positive, and the inverse-function theorem yields a smooth global inverse. At \(A=4\), the derivative vanishes only at \(x=1/2\), so the map remains strictly increasing and is a homeomorphism, but has no differentiable inverse along that critical output curve. Indeed, with \(x=1/2+u\),
\[
 \Phi_4(1/2+u)=-2+\frac{16}{3}u^3+O(u^5),
\]
so the inverse has the asymptotic cube-root law \(u\sim (3(H+2)/16)^{1/3}\), with the real cube root.

For \(A>4\), define \(r=\sqrt{1-4/A}\) and \(x_-=(1-r)/2\), \(x_+=(1+r)/2\). The derivative changes sign \(+,-,+\) at these points. Put \(h_{\max}=\Phi_A(x_-)\) and \(h_{\min}=\Phi_A(x_+)\). Then targets with \(h_{\min}<H<h_{\max}\) have exactly three distinct inverse points; targets at either equality have exactly two distinct inverse points, one of which is a quadratic critical point; all other targets have exactly one. The critical input curves are \(x=x_-\) and \(x=x_+\), and their images are the parallel straight lines \(H(Y,Q)=h_{\max}\) and \(H(Y,Q)=h_{\min}\) in the output log-odds plane. The Jacobian has negative sign strictly between the folds and positive sign outside them.

**3. The exact opening of the triple-image band.** Using the formulas for \(x_\pm\),
\[
 h_{\max}-h_{\min}=Ar-4\operatorname{artanh}r.
\]
This is positive because \(A=4/(1-r^2)\) and the derivative of \(r/(1-r^2)-\operatorname{artanh}r\) is \(2r^2/(1-r^2)^2>0\) for \(0<r<1\). Its Taylor expansion at \(r=0\), together with \(r^2=(A-4)/A\), gives the stated \((A-4)^{3/2}/3\) leading law. Equivalently, when \(a>4\), a fold region exists precisely for
\[
 0<k<k_{\mathrm{fold}}=\frac{a-4}{a-4+acp_1};
\]
for \(a\le4\) no fold occurs at any allowed memory rate.

**4. Realization of three inverses inside the physical square.** Since \(A>4\) implies \(ckp_1/(1-k)<1\), we have \(s=kp_1/(1-k)<1/c<1\). Choose
\[
 Q_* =\frac{1-k}{2}+k\left(p_0+\frac{p_1}{2}\right)
\]
and any \(H_*\) strictly between the two caustic levels. Define \(Y_*\) by \(H(Y_*,Q_*)=H_*\). For each of the three roots \(x\) of \(\Phi_A(x)=H_*\), the inverse belief equals
\[
 q=\frac12+s\left(\frac12-x\right)\in(0,1).
\]
The three sources therefore belong to the physical square, and \((X_*,Q_*)=(1/(1+e^{-Y_*}),Q_*)\) is a physical output. Conversely, when \(A\le4\), strict monotonicity proves global injectivity even on the physical square.

**5. Weighted area contraction and recurrence.** The derivative in \((y,q)\)-coordinates is
\[
 D\widetilde F(y,q)=
 \begin{pmatrix}
 1-a x(1-x)&-ac\\ kp_1 x(1-x)&1-k
 \end{pmatrix},
\quad \det D\widetilde F=(1-k)\bigl[1-Ax(1-x)\bigr].
\]
Since \(x(1-x)\) is nonconstant and \(a>0\), this determinant is independent of position **if and only if** \(A=0\), equivalently \(k=1/(1+cp_1)\). At that value, \(0<1-k<1\) and the map is a smooth global diffeomorphism of \(\mathbb R^2\) in log-odds coordinates. In the original coordinates the weighted area form \(\omega=dx\,dq/[x(1-x)]\) satisfies \(F^*\omega=(1-k)\omega\).

If \(K\) is compact, contained in \((0,1)\times\mathbb R\), and **fully invariant**, \(F(K)=K\), its log-odds image has finite planar area. The change-of-variables formula and injectivity give \(|K|_\omega=(1-k)|K|_\omega\), hence \(|K|_\omega=0\), and ordinary area also vanishes. For every compactly supported invariant probability in the interior, the logarithmic determinant is the constant \(\log(1-k)\) in the smooth log-odds coordinates. The multiplicative ergodic theorem therefore yields the exact Lyapunov sum \(\lambda_1+\lambda_2=\log(1-k)\) almost surely. Equivalently, every period-\(m\) orbit has determinant \(\det D F^m=(1-k)^m\) at the periodic point, because the coordinate-change factors telescope.

## Verification
The accompanying standalone `check_geometry.py` symbolically checks the transformed determinant, verifies the cubic critical expansion, computes exact caustic widths at four parameters, constructs three distinct physical preimages at one admissible parameter point, and checks the \(3/2\)-power onset numerically at three small offsets. `verification_output.txt` records its output. These finite checks do not prove the global image census, invariant-set area theorem, or Lyapunov identity; those follow from the preceding analytic arguments.

## Relationship to prior work
Metaxas and Sapsis (arXiv:2606.29967, 2026) introduced the risk-sensitive learning map (their Eq. (9)), proved equilibrium and time-average properties, and exhibited numerically multiple bifurcation families and chaotic regimes. Those are prior results, not asserted here as new. The present result supplies an exact global one-to-three inverse geometry, sharp memory-dependent fold threshold, and a constant-Jacobian parameter ridge not asserted in the inspected source. General planar-endomorphism singularity theory (Krauskopf–Osinga–Peckham; Hobbs–Osinga) already describes fold/cusp mechanisms abstractly; the local square-root and cubic-root singularities are standard. The new object-specific content is the exact parameter boundary, global inverse count and caustic width, physical three-preimage realization, and special weighted-area/Lyapunov law. These formulas do not follow merely from the source's equilibrium bifurcation diagrams.

## Limitations
This theorem concerns the stated analytic risk-sensitive map and its open interior. The unrestricted-belief strip is used only for an exact global inverse census; an output with three *physical* inverse images is proved, not a full physical preimage table for every output. The parameter threshold is about invertibility, not a necessary or sufficient criterion for chaos, attractor coexistence, or convergence. The zero-area conclusion requires **full invariance** (not just a trapping region), and the Lyapunov sum requires a compactly supported invariant measure away from the boundaries. No independent literature-priority audit has been performed.

## References
1. K. Metaxas and T. P. Sapsis, *Risk-Sensitive Learning in Population Games under Extreme Events: Bifurcations and Chaotic Dynamics*, arXiv:2606.29967 (initial public submission June 29, 2026), Sections 2–3 and Appendix A, https://arxiv.org/abs/2606.29967 ; accessible article full text: https://www.researchgate.net/publication/408235857_Risk-Sensitive_Learning_in_Population_Games_under_Extreme_Events_Bifurcations_and_Chaotic_Dynamics.
2. B. Krauskopf, H. M. Osinga, and B. B. Peckham, *Unfolding the Cusp-Cusp Bifurcation of Planar Endomorphisms*, SIAM J. Applied Dynamical Systems **6** (2007), 403–440, doi:10.1137/060672753.
3. C. A. Hobbs and H. M. Osinga, *Bifurcations of the Global Stable Set of a Planar Endomorphism Near a Cusp Singularity*, Int. J. Bifurcation Chaos **18** (2008), article metadata: https://pureportal.coventry.ac.uk/en/publications/bifurcations-of-the-global-stable-set-of-a-planar-endomorphism-ne/.
