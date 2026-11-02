# Antipodal-cap boundary layer and exponential reversal law for a magnetically aligned active Brownian swimmer

## Finding

Consider rotational Brownian motion on the unit sphere at rotational diffusivity \(D>0\), in a uniform aligning field of dimensionless strength \(\xi>0\). Start with the orientation exactly parallel to the field, and stop when its field projection first falls below \(b\in(-1,1)\). The stopping time is \(\tau_{\xi,b}\). Its exact mean is
\[
 M_\xi(b):=\mathbb E_1\tau_{\xi,b}=\frac1{D\xi}\int_b^1\frac{e^{\xi(1-u)}-1}{1-u^2}\,du. \tag{1}
\]
For fixed \(b\in(-1,1)\), the strong-alignment asymptotic is
\[
 M_\xi(b)\sim\frac{e^{\xi(1-b)}}{D\xi^2(1-b^2)}. \tag{2}
\]
For the physically distinct joint limit in which the target is a shrinking antiparallel cap, set \(b_\xi=-1+\eta/\xi\) with any fixed \(\eta>0\), and define \(E_1(\eta)=\int_\eta^\infty e^{-s}\,ds/s\). Then the two-term boundary-layer law is
\[
 2D\xi e^{-2\xi}M_\xi(b_\xi)=E_1(\eta)+\frac{e^{-\eta}}{2\xi}+O_\eta(\xi^{-2}). \tag{3}
\]
In the **same joint limit** the entire exit-time law is asymptotically memoryless:
\[
 \frac{\tau_{\xi,b_\xi}}{M_\xi(b_\xi)}\ \Longrightarrow\ \operatorname{Exp}(1),\qquad
 \mathbb E\left[\left(\frac{\tau_{\xi,b_\xi}}{M_\xi(b_\xi)}\right)^k\right]\to k!\quad(k\in\mathbb N). \tag{4}
\]
The angular half-width of the antiparallel target cap is \(\theta_\xi=\arccos(1-\eta/\xi)\sim\sqrt{2\eta/\xi}\); hence (3) identifies the natural inverse-square-root angular crossover between activation and target geometry. The result concerns **orientation reversal**, not first passage of the particle's spatial coordinates.

## Assumptions and scope

The unit orientation vector \(n_t\in S^2\) is a reversible diffusion with generator \(D(\Delta_{S^2}+\xi\nabla_{S^2}(n\cdot e_z)\cdot\nabla_{S^2})\). Thus its invariant density is proportional to \(e^{\xi n\cdot e_z}\). Put \(U_t=n_t\cdot e_z\), started from \(U_0=1\), and \(\tau_{\xi,b}=\inf\{t\ge0:U_t\le b\}\). We use the standard conservative entrance behavior at the poles and absorption only at \(b\). For (3)–(4), \(D\) and \(\eta\) are positive constants and \(\xi\to\infty\), so \(b_\xi\in(-1,1)\) eventually. No translational noise or particle speed enters the orientation hitting time.

## Proof

The projected generator acts on smooth functions by
\[
 L_\xi f(u)=D\big[(1-u^2)f''(u)+(\xi(1-u^2)-2u)f'(u)\big]
   =De^{-\xi u}\big[(1-u^2)e^{\xi u}f'(u)\big]'. \tag{5}
\]
For a bounded nonnegative forcing \(g\), solve \(-L_\xi h=g\), with \(h(b)=0\) and the regularity condition at \(u=1\). The unique solution is \(h=K_\xi g\), where
\[
 (K_\xi g)(u)=\frac1D\int_b^u\frac{e^{-\xi z}}{1-z^2}\left(\int_z^1e^{\xi v}g(v)\,dv\right)dz. \tag{6}
\]
The inner integral vanishes linearly at \(z=1\), so (6) is finite. Taking \(g\equiv1\) gives the mean profile \(m_1(u)\), and evaluation at \(u=1\) gives (1). A Laplace boundary estimate at fixed \(b\) gives (2).

For the shrinking target, substitute \(s=\xi(1+u)\) into (1). Exactly,
\[
 2D\xi e^{-2\xi}M_\xi(-1+\eta/\xi)
 =\int_\eta^{2\xi}\frac{e^{-s}-e^{-2\xi}}{s(1-s/(2\xi))}\,ds. \tag{7}
\]
Split this integral at \(s=\xi\). On \([\eta,\xi]\), expand \((1-s/(2\xi))^{-1}=1+s/(2\xi)+O(s^2/\xi^2)\), with the remainder bounded by a constant multiple of \(s^2/\xi^2\). Integrability of \(se^{-s}\) yields an \(O_\eta(\xi^{-2})\) error. On \([\xi,2\xi]\), the cancellation between the two exponentials makes the integrand at most \(2e^{-s}\); the contribution is exponentially small. Extending the two leading integrals to infinity yields (3), since \(\int_\eta^\infty e^{-s}ds/s=E_1(\eta)\) and \(\int_\eta^\infty e^{-s}ds=e^{-\eta}\).

It remains to establish (4), which is not a consequence merely of knowing the mean. Write \(m_k(u)=\mathbb E_u[\tau_{\xi,b}^k]\). Standard killed-diffusion potential theory and induction from the backward equations give \(m_0\equiv1\) and \(m_k=kK_\xi m_{k-1}\). Since \(K_\xi\) is positive and \(K_\xi 1=m_1\) increases in \(u\),
\[
 0\le m_k(u)\le m_k(1)\le k!M_\xi(b)^k. \tag{8}
\]
Moreover, for every \(u\ge0\),
\[
 0\le M_\xi(b)-m_1(u)\le M_\xi(b)-m_1(0)\le \frac{e^\xi}{D\xi}. \tag{9}
\]
By (3), (9) divided by \(M_\xi(b_\xi)\) tends to zero exponentially. The normalized positive kernel of \(K_\xi\) at \(u=1\) is a probability measure
\[
 \mathcal P_\xi(dv)=\frac{e^{\xi v}\left[\int_b^v e^{-\xi z}(1-z^2)^{-1}dz\right]dv}{D M_\xi(b)}. \tag{10}
\]
For fixed \(\eta>0\), (7) shows \(M_\xi(b_\xi)\asymp_\eta e^{2\xi}/\xi\). On \(v\le0\) the numerator of (10) integrates to at most \((D\xi)^{-1}\int_b^0e^{-\xi z}(1-z^2)^{-1}dz=O_\eta(e^\xi/\xi)\), so \(\mathcal P_\xi(v<0)\to0\).

For each \(k\), let \(f_{k,\xi}(u)=m_k(u)/(k!M_\xi(b_\xi)^k)\). From (8) these functions belong to \([0,1]\), and the recursion implies
\[
 0\le f_{k,\xi}(1)-f_{k,\xi}(u)\le1-\frac{m_1(u)}{M_\xi(b_\xi)}\qquad(u\in[b_\xi,1]). \tag{11}
\]
Hence the right-hand side of (11) is uniformly small on \([0,1]\). Since \(f_{0,\xi}\equiv1\), induction using \(f_{k,\xi}(1)=\int f_{k-1,\xi}(v)\mathcal P_\xi(dv)\) and concentration of \(\mathcal P_\xi\) on \([0,1]\) gives \(f_{k,\xi}(1)\to1\) for every fixed integer \(k\ge1\). These are precisely the moments of \(\operatorname{Exp}(1)\); tightness follows from the first moment and the exponential distribution is moment-determinate, proving (4).

## Verification

An accompanying deterministic checker evaluates the exact positive integral in (7), independently checks (1) by quadrature of the backward representation, and compares the leading and two-term strong-field formulas for multiple \(\eta\) and \(\xi\). Its finite numerical tests verify constants but do not prove (4), which follows from the preceding kernel and moment argument. The result includes no simulated spatial first passages.

## Relationship to prior work

Kuznetsov, Sposini, Kantorovich and Chechkin (2026) develop the same magnetic active-Brownian orientation generator and analyze spatial drift, diffusivity and first arrival at a spatial target; they do not give the orientation-to-antiparallel-cap joint limit (3)–(4). The classical general backward-equation method for one-dimensional diffusion gives (6), and its use here is not presented as novel. Established rotational-diffusion relaxation methods (Waldron, Kalmykov and Coffey, 1994) and field-driven magnetic moment first-passage studies (Denisov et al., 2007) are relevant precursors, as are general spherical narrow-escape and small-noise metastability theories. The assessed contribution is the **specific joint strong-alignment/shrinking-antiparallel-cap crossover**, its sharp second term, and the simultaneous fully normalized exponential reversal law, not a new derivation of general one-dimensional first-passage or metastability theory.

## Limitations

The asymptotic (3) fixes \(\eta>0\); it is not claimed uniformly as \(\eta\to0\) or \(\eta\to\infty\) with \(\xi\). The exact response requires axial symmetry, isotropic rotational diffusion and a purely aligning field. The theorem does not cover interacting swimmers, anisotropic rotational noise, rotating fields, or translational arrival at a spatial target. Exact priority for related asymptotics in older magnetic-rotation literature has not been independently established; the classical literature identified in the references was only partly accessible in full text.

## References

1. A. A. Kuznetsov, V. Sposini, S. S. Kantorovich and A. V. Chechkin, *Drift-diffusion interplay in active Brownian particles under orienting field*, arXiv:2606.31914 (first public June 30, 2026), https://arxiv.org/abs/2606.31914 .
2. J. T. Waldron, Y. P. Kalmykov and W. T. Coffey, *Rotational Brownian motion and dielectric relaxation of polar molecules subjected to a constant bias field: Exact solution*, Phys. Rev. E 49, 3976 (1994), https://doi.org/10.1103/PhysRevE.49.3976 .
3. S. I. Denisov, K. Sakmann, P. Talkner and P. Hänggi, *Rapidly driven nanoparticles: Mean first-passage times and relaxation of the magnetic moment*, Phys. Rev. B 75, 184432 (2007), https://doi.org/10.1103/PhysRevB.75.184432 .
4. D. Coombs, R. Straube and M. J. Ward, *Diffusion on a sphere with localized traps: Mean first passage time, eigenvalue asymptotics, and Fekete points*, SIAM J. Appl. Math. (2009), https://doi.org/10.1137/080733280 .
5. *Some exact results for one-dimensional diffusion with absorption*, Phys. Rev. B 20, 2558 (1979), https://doi.org/10.1103/PhysRevB.20.2558 .
