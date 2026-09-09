# Validated principal-eigenvalue enclosure for the individual MOTS in the equal-mass Brill–Lindquist cell (bare masses 1, 1; separation 2)

## Context
Marginally outer trapped surfaces (MOTS) model quasi-local black-hole horizons in
initial data. Strict stability ($\lambda_1(L_\Sigma)>0$) implies stably-outermost
status and spherical topology (Andersson–Mars–Simon; Galloway) and anchors the
Jang-equation blow-up rate $-1/\sqrt{\lambda}\log\tau$ (Yu). No prior work logs a
principal-eigenvalue enclosure for any Brill–Lindquist two-puncture cell: stability
theory is qualitative, Kerr eigenvalue work is a different family, and horizon-finder
papers on Brill–Lindquist data test location only.

## Definitions
- Time-symmetric vacuum Brill–Lindquist data on $\mathbb{R}^3$ minus two punctures:
  $\psi = 1 + 1/(2d_1) + 1/(2d_2)$, $g = \psi^4\delta$, punctures at
  $(\rho,z)=(0,+1),(0,-1)$, bare masses $\alpha_1=\alpha_2=1$, separation $b=2$, $K\equiv 0$.
- ADM mass $m_{\mathrm{ADM}} = \alpha_1+\alpha_2 = 2$.
- MOTS candidate $\Sigma$: axisymmetric star-shaped surface about the upper puncture,
  $X(\lambda)=H(\lambda)\sin\lambda$, $Z(\lambda)=1+H(\lambda)\cos\lambda$,
  $\lambda\in[0,\pi]$, $H$ tabulated (801 nodes, N=800; 401-node companion).
  MOTS equation $\theta_+ = H_\delta + 4N_\delta\cdot\nabla\psi/\psi = 0$.
- Time-symmetric MOTS stability operator ($X=0$): $L_\Sigma = -\Delta_\Sigma + Q$,
  $Q = -(\mathrm{Ric}_g(n,n)+|A_g|^2)$.
- Units: eigenvalues computed in code units are rescaled to $m_{\mathrm{ADM}}=1$ units
  via $\lambda_1(m_{\mathrm{ADM}}{=}1)=\lambda_1(\mathrm{code})\times m_{\mathrm{ADM}}^2
  = 4\,\lambda_1(\mathrm{code})$.

## Result
For the fixed data above, the per-end outermost MOTS candidate $\Sigma$ satisfies
$$\lambda_1(L_\Sigma) \in [0.157883,\,0.159998]\ \text{(code units)}
= [0.631530,\,0.639991]\ \text{(}m_{\mathrm{ADM}}=1\text{ units)},$$
hence in particular $\lambda_1 \ge 0.02$ (preset success criterion, passed by ~30x).
$\lambda_1>0$ certifies strict stability.

## Proof / evidence
- Newton axisymmetric MOTS solve: replayed interior $\max|\theta_+| = 3.9\times10^{-11} < 10^{-6}$;
  $H\in[0.382774,0.414862]$, $H>0$, $H'(0)=H'(\pi)=0$: embedded topological 2-sphere.
- Reduction: time symmetry gives $X=0$ so $L_\Sigma=-\Delta+Q$ is self-adjoint;
  axisymmetric Fourier modes shift $L$ by $m^2/(\psi^4X^2)\ge 0$, so the ground state is
  in the $m=0$ sector. Ambient Ricci via the 3D conformal formula; $|A_g|^2_g =
  \psi^{-4}|\mathring{A}_\delta|^2$.
- Lower bound: $-\Delta_\Sigma\ge 0$ on a closed surface, so $\lambda_1\ge\min_\Sigma Q$
  by the positive principal eigenfunction. Grid minimum $q_{\min}=0.157901$ (identical
  at N=400/800 to 6dp); Lipschitz continuum gap $\le 1.78\times10^{-5}$ plus $10^{-6}$
  fp margin gives $L=0.157883$ code units.
- Upper bound: Rayleigh quotient with $u\equiv 1$ gives $\lambda_1\le\fint_\Sigma Q\,dA
  = 0.159996$; trapezoidal remainder $\le 6.26\times10^{-7}$ plus $10^{-6}$ margin gives
  $U=0.159998$ code units.
- Cross-checks: pointwise Gauss identity $Q=K_\Sigma-|A|^2/2$ to $3.7\times10^{-6}$
  (bulk); $\fint Q = 0.159996$ vs $4\pi/A = 0.160002$ (nearly round);
  area $A=78.538913 \le 16\pi m_{\mathrm{ADM}}^2 = 201.061930$ (Penrose holds).
- Replay: `python3 artifacts/verify_certificate.py`.

## Limitations
- Full TARGET branch (A) not claimed: Jang blow-up profile inequality and rigorous
  common-MOTS nonexistence proof were not completed. Outermost status is
  candidate-level (per-end outermost, standard for separated data; origin spheres
  $R\ge 2.4$ untrapped; no second/exotic MOTS found).
- Continuum corrections are explicit analytic bounds on computed grids, not
  machine-checked interval arithmetic; pole nodes excluded from the FD stencil with
  extrapolated pole values (cap error $O(10^{-5})$, negligible at the 30x margin).

## Reproducibility
Artifacts: `prof800.npy` (surface $H$ + $Q$, N=800), `prof400.npy` (N=400 companion),
`stageF.py` (Newton solver + $Q$ assembly), `verify_certificate.py` (replay:
residual, enclosure, area, sphericity). Run `python3 artifacts/verify_certificate.py`.

## References
- Andersson–Mars–Simon, Stability of MOTS and existence of MOTT, arXiv:0704.2889.
- Bussey–Cox–Kunduri, Eigenvalues of the MOTS stability operator for slowly rotating Kerr, arXiv:2010.01682.
- Yu, Blowup rate control for Jang's equation, arXiv:1906.08841.
- Hui–Lin, Revisiting the apparent horizon finding problem with multigrid methods, arXiv:2404.16511.
