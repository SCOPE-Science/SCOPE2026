# Sharp quadratic high-mode amplification of the SSEP correlation–dissipation ratio

## Finding

In the weak-harmonic-drive, continuum hydrodynamic mode-response model for the boundary-driven symmetric simple exclusion process, the largest normalized correlation-lag-to-excess-dissipation ratio grows **quadratically** in the mode index. The sharp leading and first subleading coefficients and the asymptotically optimal forcing frequency are explicit.

Let \(n\ge 1\) and \(\lambda_n=(n\pi)^2\). For each forcing frequency \(\omega>0\), set \(s=\sqrt{\omega/2}\), and define the source's positive excess-dissipation form factor

\[
F(s)=\frac{s^2(\cosh s+\cos s)-s(\sinh s+\sin s)}{2(\cosh s-\cos s)}.
\]

The mode-specific dimensionless ratio is

\[
Q_n(\omega)=\frac{2\lambda_n^2\omega^2(\omega^2+36\lambda_n^2)}{135F(\sqrt{\omega/2})(\omega^2+4\lambda_n^2)(\omega^2+16\lambda_n^2)}.
\]

Define

\[
h(r)=\frac{r(r^2+36)}{(r^2+4)(r^2+16)},\quad
z_*^3+88z_*^2+528z_*-2304=0,\quad z_*>0,\quad r_*=\sqrt{z_*}.
\]

The cubic has exactly one positive root. Write

\[
C_* = \frac{8\pi^2}{135}h(r_*),\qquad
D_* = \frac{\sqrt2}{\pi\sqrt{r_*}}C_*.
\]

**Theorem.** If \(M_n=\sup_{\omega>0}Q_n(\omega)\), then as integer \(n\to\infty\),

\[
\boxed{M_n=C_*n^2+D_*n+O(1)},\qquad
C_*=0.297094183914500\ldots,\quad D_*=0.102415840220860\ldots.
\]

For every sufficiently large integer \(n\), the supremum is attained at a **unique** positive forcing frequency \(\omega_n\). Its exact asymptotic tuning is

\[
\boxed{\frac{\omega_n}{\lambda_n}=r_*+\frac{\delta_*}{n}+O(n^{-2})},\quad
\delta_*=\frac{\sqrt2\,h(r_*)}{2\pi r_*^{3/2}h''(r_*)}
=-0.241124011432592\ldots,
\]

in particular \(\omega_n/n^2\to \pi^2 r_*=16.8299967002559\ldots\). The conclusion is a sharp, unbounded failure of a **mode-independent bound for the source-defined normalized ratio**, not a claim that the unnormalized physical lag itself grows with \(n\).

## Assumptions and scope

We adopt the source's linearized continuum hydrodynamic formulas for open SSEP on the unit interval with diffusion coefficient \(1\), Dirichlet boundaries, mean density \(0<\rho_0<1\), a nonzero small stationary boundary gradient \(g_0\), and a harmonic perturbation of amplitude \(0<|\epsilon|\ll|g_0|\ll1\). The displayed ratio is independent of these nonzero amplitudes after cancellation. For each \(n\), the frequency varies over \((0,\infty)\). Limits in this statement are taken **within this defined continuum response family** as \(n\to\infty\); no finite-lattice joint limit, nonlinear-drive universality, or fixed-resolution experimental extrapolation is asserted.

The source gives the mode lag \(\ell_n(\omega)\) and average excess entropy production \(\overline{\dot\Sigma}_{\mathrm{ex}}\) as

\[
|\ell_n|^2=\frac{4g_0^2\epsilon^2\omega^2(\omega^2+36\lambda_n^2)}{\lambda_n^2(\omega^2+4\lambda_n^2)(\omega^2+16\lambda_n^2)},\qquad
\overline{\dot\Sigma}_{\mathrm{ex}}=\frac{\epsilon^2}{2\chi_0}F(s),\quad\chi_0=\rho_0(1-\rho_0),
\]

and defines \(Q_n=\lambda_n^4|\ell_n|^2/(540g_0^2\chi_0\overline{\dot\Sigma}_{\mathrm{ex}})\). These equations yield the stated rational expression exactly; no separate abbreviated formula is needed.

## Proof

**1. Positivity and two regimes of the dissipation factor.** Set \(A(s)=s(\cosh s+\cos s)-(\sinh s+\sin s)\) and \(B(s)=\cosh s-\cos s\), so \(F(s)=sA(s)/(2B(s))\). For \(s>0\), \(B(s)>0\), \(A(0)=0\), and \(A'(s)=s(\sinh s-\sin s)>0\); therefore \(F(s)>0\). Taylor expansion and elementary exponential asymptotics give

\[
F(s)=\frac{s^4}{30}+O(s^8)\quad(s\downarrow0),\qquad
F(s)=\frac{s^2-s}{2}+O(s^2e^{-s})\quad(s\to\infty).
\]

In particular, with \(E(s)=s^2/(2F(s))\), we have \(E(s)=1+s^{-1}+O(s^{-2})\) at infinity, with the corresponding differentiated estimates. Positivity, continuity, and the two endpoint expansions imply the global bound \(0<E(s)\le K(1+s^{-2})\) for some finite constant \(K\), a fact needed to control frequencies depending on the mode index.

**2. Exact scaling factorization.** Write \(\lambda=\lambda_n\), \(r=\omega/\lambda\), and \(s=\sqrt{r\lambda/2}\). Direct cancellation in the source-defined ratio gives

\[
\frac{Q_n(r\lambda)}{\lambda}=\frac{8}{135}\,h(r)E\!\left(\sqrt{r\lambda/2}\right).
\]

For each compact interval bounded away from \(0\) and infinity, the right side converges in \(C^2\), as \(n\to\infty\), to \(8h(r)/135\). This alone would not establish an asymptotic for the global supremum, because maximizing frequencies could escape to zero or infinity.

**3. Uniform exclusion of escaping maximizers.** Since \(h(r)=O(r)\) as \(r\downarrow0\), the global bound for \(E\) gives

\[
\sup_{0<r\le\eta}\frac{Q_n(r\lambda_n)}{\lambda_n}
\le K_1\left(\eta+\lambda_n^{-1}\right).
\]

Since \(h(r)=O(r^{-1})\) as \(r\to\infty\), the analogous estimate is \(\sup_{r\ge R}Q_n(r\lambda_n)/\lambda_n\le K_2/R\) for \(R\ge1\) and \(n\ge1\). Thus neither endpoint can asymptotically compete with the positive interior maximum. Continuity and the low- and high-frequency endpoint limits show that \(Q_n\) has a finite supremum, attained in the positive interior whenever it exceeds the endpoint value \(1\); for all large \(n\) the interior maximum is of order \(\lambda_n\).

**4. Unique limiting optimum.** Direct differentiation yields

\[
h'(r)=\frac{-r^6-88r^4-528r^2+2304}{(r^2+4)^2(r^2+16)^2}.
\]

The numerator is strictly decreasing as a polynomial in \(z=r^2\ge0\), positive at \(0\), and negative at infinity. It therefore vanishes at exactly \(r=r_*\). Hence \(h\) has a unique global maximum there and \(h''(r_*)<0\). Uniform interior convergence and the endpoint bounds now give \(M_n/\lambda_n\to8h(r_*)/135\), with every maximizer's ratio \(\omega_n/\lambda_n\to r_*\). Local \(C^2\) convergence, strict curvature, and exclusion of the complement of a small neighborhood establish uniqueness of the optimizer for all sufficiently large \(n\).

**5. Sharp two-term envelope and frequency.** Uniformly near \(r_*\), put \(a=\sqrt2/\pi\). Since \(s=n\pi\sqrt{r/2}\), the refined expansion is

\[
\frac{Q_n(r\lambda_n)}{\lambda_n}=
\frac8{135}\left[h(r)+\frac{a}{n}\frac{h(r)}{\sqrt r}+O(n^{-2})\right]
\]

with two derivatives. Differentiating at the unique maximizer and using \(h'(r_*)=0\) gives

\[
\frac{\omega_n}{\lambda_n}=r_*+\frac{a\,h(r_*)}{2r_*^{3/2}h''(r_*)}\,n^{-1}+O(n^{-2}).
\]

Substitution into the envelope and \(\lambda_n=\pi^2n^2\) proves exactly \(M_n=C_*n^2+D_*n+O(1)\), with the coefficients stated above. This completes the proof.

## Verification

The standalone `verify.py` reconstructs the complex lag from the published response and its quasistatic limit, simplifies the squared modulus and dimensionless ratio, verifies the derivative polynomial symbolically, checks the two asymptotic limits for \(F\), and independently evaluates the ratio from its original physical definitions at multiple modes and frequencies. Numerical maximization for \(n=2,3,4,5,10,20,40,80,160\) confirms the limiting optimizer and the uniformly bounded residual after subtracting \(C_*n^2+D_*n\). The finite numerical tests do not establish any universal quantifier; the proof above supplies the global maximization and endpoint control. Run `python verify.py` with SymPy, mpmath and SciPy installed; `verification_output.json` records the actual numerical replay.

## Relationship to prior work

Vijayan, Thilakaraj, V and V A (arXiv:2610.07964v1) derived the mode-resolved lag, excess-dissipation form factor, and ratio \(Q_n\), established the slowest-mode bound, and reported higher-mode violations numerically including an approximately \(1.42\) peak for mode \(2\). Those formulas are **prior work and the inputs here**. The new analytical object is the **global over-frequency envelope as the mode index diverges**, its sharp two-term growth, unique limiting optimizing frequency, and the uniform endpoint argument allowing mode and frequency to vary together. The prior paper does not state this envelope theorem or its coefficients.

Bodineau and Dagallier (arXiv:2212.11561) study large deviations of time-averaged two-point correlations in open SSEP; this is a different optimization from the source-defined harmonic-frequency ratio. Dechant, Garnier-Brun, and Sasa (Phys. Rev. Lett. 131, 167101, 2023) study general bounds on stationary-observable correlation times. Kolchinsky, Dechant, Yoshimura, and Ito (Phys. Rev. Research 8, 023025, 2026) derive generalized excess/housekeeping speed limits. Neither latter framework directly specifies the \(n\)-indexed SSEP ratio or its sharp high-mode envelope. Originality remains qualified by the possibility of an unlocated prior optimization of the same published response formula.

## Limitations

- The result concerns the **specific normalized** \(Q_n\); it does not establish divergence of the bare lag or of dissipation.
- The large-index limit is taken **after adopting the continuum linear-response mode equations**. Uniform approximation by a finite lattice at mode indices comparable to lattice resolution is not proved.
- No nonlinear-driving, variable-mobility, or interacting-field extension is claimed.
- The optimizer is proved unique **for all sufficiently large modes**, not for every finite mode.
- Priority is assessed on accessible published material and search records; independent audit and full literature completeness are not asserted.

## References

1. V. Vijayan, R. Thilakaraj, Gokila V, Y. V. A, *Long-Range Nonequilibrium Correlations as a Thermodynamic Speedometer*, arXiv:2610.07964v1 (first public 2026-10-06), https://arxiv.org/abs/2610.07964 . See especially formulas (30), (33), (34), (44), Sec. III.3, and appendices E–G.
2. T. Bodineau and B. Dagallier, *Large deviations for out of equilibrium correlations in the symmetric simple exclusion process*, arXiv:2212.11561, https://arxiv.org/abs/2212.11561 .
3. A. Dechant, J. Garnier-Brun, S. Sasa, *Thermodynamic Bounds on Correlation Times*, Phys. Rev. Lett. 131, 167101 (2023), https://doi.org/10.1103/PhysRevLett.131.167101 .
4. A. Kolchinsky, A. Dechant, K. Yoshimura, S. Ito, *Generalized free energy and excess/housekeeping decomposition in nonequilibrium systems: From large deviations to thermodynamic speed limits*, Phys. Rev. Research 8, 023025 (2026), https://doi.org/10.1103/r48t-dghl .
