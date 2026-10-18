# Shape-selected transverse stability of balanced Stuart–Landau polygons under reactive coupling

## Finding

A zero-mean rotating polygon in the identical, complex-coupled Stuart–Landau flow has a complete Floquet spectrum determined by a single shape statistic: the modulus of its second circular phase moment. The spectrum gives a necessary and sufficient strict transverse stability criterion, a sharp reactive-coupling threshold, and a four-oscillator family where transverse attraction and instability occur at the **same physical parameters** but at different polygon shapes.

Specifically, let \(d=\left|M^{-1}\sum_j e^{2i\theta_j}\right|<1\), \(x=MC_r/a\), \(y=MC_i/a\), and \(a=\beta-MC_r\). Define
\[
\mathcal H(x,u,s)=\bigl[u+(2-x)^2\bigr]\bigl[(1-x)u-x(2-x)^2\bigr]+s(2-x)^2(x^2+u).
\]
The rotating polygon is **strictly normally attracting** (all Floquet exponents other than the \(M-2\) tangential zero exponents are strictly negative in real part) exactly when
\[
0<x<1,\qquad \mathcal H(x,y^2,d^2)>0.
\]

## Assumptions and scope

Fix any integer \(M\ge3\), saturation \(\kappa>0\), growth \(\beta>0\), real natural frequency \(\omega\), dissipative coupling \(C_r>0\), and arbitrary reactive coupling \(C_i\in\mathbb R\). The ordinary differential equations on \(\mathbb C^M\) are
\[
\dot z_j=(\beta+i\omega-\kappa|z_j|^2)z_j+(C_r+iC_i)\sum_{\ell\ne j}(z_\ell-z_j),\quad 1\le j\le M.
\]
Assume \(a=\beta-MC_r>0\). Set \(r=\sqrt{a/\kappa}\) and \(\Omega=\omega-MC_i\). Choose phases \(\theta_j\in\mathbb R\) satisfying \(\sum_j e^{i\theta_j}=0\). Then \(z_j(t)=r e^{i(\Omega t+\theta_j)}\) is an exact solution. Restrict to noncollinear phase configurations, which are characterized by
\[
\Delta=M^{-1}\sum_{j=1}^M e^{2i\theta_j},\qquad d=|\Delta|<1.
\]
Here “transversely stable” refers to the spectrum normal to the smooth \((M-2)\)-dimensional balanced-polygon manifold in the co-rotating frame, **not** asymptotic attraction to one individual periodic orbit. Tangential polygon-shape and common-phase directions are neutral. The result does not assert global attraction or nonlinear Hopf bifurcation at equality.

## Proof

**1. Rotating-frame linearization and neutral modes.** In \(w_j=e^{-i\Omega t}z_j\), the polygon is the constant solution \(w_j^*=r e^{i\theta_j}\). The exact complex-real linearization is
\[
\dot\xi_j=-a\xi_j-a e^{2i\theta_j}\overline{\xi_j}+C\sum_{\ell=1}^M\xi_\ell,\qquad C=C_r+iC_i.
\]
The real radial perturbations \(\xi_j=e^{i\theta_j}\rho_j\) with \(\sum_j\rho_j e^{i\theta_j}=0\) have eigenvalue \(-2a\); the real angular perturbations \(\xi_j=i e^{i\theta_j}\psi_j\) with \(\sum_j\psi_j e^{i\theta_j}=0\) have eigenvalue \(0\). Because the phase vectors span \(\mathbb R^2\) when \(d<1\), each real nullspace has dimension exactly \(M-2\). Thus these contribute \(-2a\) and zero each \(M-2\) times, and there are four remaining collective directions.

**2. Four-dimensional collective factor.** With \(S=\sum_j\xi_j\), eliminate each \(\xi_j\) from the linear eigenvalue equations for \(\lambda\ne0,-2a\) to obtain
\[
[\lambda(\lambda+2a)-M(\lambda+a)C]S+aM\Delta\overline C\,\overline S=0.
\]
The conjugate equation yields the real characteristic factor
\[
\begin{aligned}
F(\lambda)={}&[\lambda^2+(2a-q)\lambda-aq]\,[\lambda^2+(2a-\overline q)\lambda-a\overline q]\\
&-a^2d^2|q|^2,\qquad q=MC.
\end{aligned}
\]
By polynomial continuation, this holds at the excluded eigenvalues too. The full characteristic polynomial is \(\lambda^{M-2}(\lambda+2a)^{M-2}F(\lambda)\). Writing \(x=MC_r/a>0\) and \(y=MC_i/a\), the dimensionless factor \(Q(t)=a^{-4}F(at)\) is
\[
Q(t)=t^4+(4-2x)t^3+(4-6x+x^2+y^2)t^2+2(x^2+y^2-2x)t+(1-d^2)(x^2+y^2).
\]
In particular, the entire spectrum depends on phase shape only through \(d^2\).

**3. Complete strict Hurwitz criterion.** Write \(Q(t)=t^4+b_1t^3+b_2t^2+b_3t+b_4\), where
\[
\begin{split}
b_1&=4-2x,\quad b_2=4-6x+x^2+y^2,\\
b_3&=2(x^2+y^2-2x),\quad b_4=(1-d^2)(x^2+y^2)>0.
\end{split}
\]
The quartic Routh–Hurwitz inequalities are positivity of all four coefficients, \(b_1b_2>b_3\), and \(b_1b_2b_3>b_3^2+b_1^2b_4\). Two exact algebraic identities are
\[
b_1b_2-b_3=2(1-x)[y^2+(2-x)(4-x)],
\]
\[
b_1b_2b_3-b_3^2-b_1^2b_4=4\mathcal H(x,y^2,d^2).
\]
If \(x\ge2\), then \(b_1\le0\). If \(1\le x<2\), then \(b_1b_2-b_3\le0\). Thus no strict Hurwitz stability is possible for \(x\ge1\).

For \(0<x<1\), put \(u=y^2\). The polynomial \(\mathcal H(x,u,d^2)\) is quadratic in \(u\) with positive leading coefficient \(1-x\), negative constant term, and hence has exactly one positive root \(u_{\mathrm{crit}}\). At the value \(u=x(2-x)\), where \(b_3=0\), its Hurwitz identity gives \(\mathcal H=-b_1^2b_4/4<0\). Consequently \(\mathcal H>0\) forces \(u>x(2-x)\), implying \(b_3>0\) and \(b_2>0\). The remaining Hurwitz conditions are automatic from the first identity. This proves the announced if-and-only-if test. Increasing \(d^2\) increases \(\mathcal H\) strictly, since \(\partial\mathcal H/\partial(d^2)=(2-x)^2(x^2+u)>0\); its unique root in \(u\) therefore decreases strictly. At the root, \(b_3>0\) and the equality factors as \((t^2+\nu^2)(t^2+b_1t+b_4/\nu^2)\), where \(\nu^2=b_3/b_1>0\). The second quadratic is strictly Hurwitz, so the first is a simple imaginary pair and the other modes are transversely damped.

**4. Four-agent shape selection.** For \(M=4\), choose \(x=1/2\), \(y=1\), and phases \((0,\pi,\phi,\phi+\pi)\) with \(\phi\not\equiv0\pmod\pi\). Then \(d^2=\cos^2\phi\) and
\[
\mathcal H(1/2,1,\cos^2\phi)=\frac{5}{32}(18\cos^2\phi-13).
\]
Therefore strict normal attraction occurs precisely for \(\cos^2\phi>13/18\). At \(\phi=\pi/2\) the square is transversely unstable; at \(\phi=\pi/6\) the unequal-angle antipodal-pair polygon is strictly normally attracting. These occur with the same physical coefficients: \(C_r=a/8\), \(C_i=a/4\), and \(\beta=3a/2\), with arbitrary \(a,\kappa>0\).

## Verification

The standalone `CHECKER.py` uses only Python and NumPy. Run `python CHECKER.py` after installing NumPy. It tests exact rational Hurwitz identities and directly constructs the \(2M\)-dimensional real co-rotating Jacobian for regular balanced polygons with \(3\le M\le10\) and nonregular four-agent shapes. It compares the full numerical characteristic polynomial against the predicted factored polynomial and checks the stability classification. The recorded run passed 2,283 individual checks. These finite tests provide diagnostic reproducibility and are not substitutes for the general algebraic proof above.

## Relationship to prior work

Zhao and Uchida (2026), arXiv:2610.08239v1, equations (38)–(55), establish balanced polygon solutions and characterize their transverse stability by numerically sampling Jacobians; their Section 5 does not provide a closed shape-invariant characteristic polynomial or sharp reactive-coupling stability inequality. The present result deliberately considers the homogeneous-growth special case of their general heterogeneous model and solves the missing exact stability question for that case.

Zou and Zhan (2009), *Splay States in a Ring of Coupled Oscillators: From Local to Global Coupling*, analyze **real** global coupling. Their Appendix B already identifies the second phase moment and a four-dimensional collective reduction; its equation (58) and condition (59) establish stability only for negative real coupling. Those results supply important precedents, but do not imply the present positive-dissipative-coupling stabilization by reactive coupling, the quartic Hurwitz surface, or sharp four-agent shape selection.

Liu et al. (2017) consider global synchronization and real-coupling range effects, not the stated nonreal-coupling threshold. A formally equivalent theorem in other complex-coupled oscillator literature remains a bibliographic possibility.

## Limitations

The theorem assumes identical growth rates, equal nonlinear saturation, common natural frequency, and no Kerr-type nonlinear frequency shift. The phase tuple must be noncollinear (\(d<1\)). No conclusion is claimed for collinear polygons, global basins, stochastic forcing, or nonlinear dynamics at the transverse imaginary-eigenvalue threshold. The result is an analytic stability classification, not an independent proof of novelty against all possible literature.

## References

1. L. Zhao and N. Uchida, *Heterogeneity-induced chaos in globally coupled Stuart–Landau oscillators*, arXiv:2610.08239v1, first posted 2026-10-06; https://arxiv.org/html/2610.08239v1 .
2. W. Zou and M. Zhan, *Splay States in a Ring of Coupled Oscillators: From Local to Global Coupling*, SIAM Journal on Applied Dynamical Systems 8 (2009), 1324–1340; https://doi.org/10.1137/09075398X .
3. S. Liu, W. Zou, M. He, J. Kurths, and M. Zhan, *Global Stability of the Sync with Amplitude Effects*, SIAM Journal on Applied Dynamical Systems 16 (2017); https://doi.org/10.1137/16M1086005 .
