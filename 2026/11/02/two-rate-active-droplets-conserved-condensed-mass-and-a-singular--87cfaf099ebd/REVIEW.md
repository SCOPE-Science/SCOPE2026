# Independent mathematical audit

## correctness

PASS

For the explicitly specified one-dimensional stationary kinetic equations, r>0, alpha_g,alpha_l>0, rho_m>4, and the symmetric one-interface low-density gas branch, write S=v sigma and R=v rho. Away from the origin S'=-r rho and R'=-(r+alpha) sigma; phasewise S^2-rR^2/(r+alpha) is constant. Gas decay forces its zero first integral and sigma_g=eta_g rho_g, selecting the small interface root y_b and giving exactly one/chi_g half-gas mass via S(b)/r. Interface R,S continuity gives rho_l(b)=rho_m, sigma_l(b)=rho_m eta_g and the two-mode liquid solution rho_l(x)=rho_m(cosh(k(b-x))+beta sinh(k(b-x))), sigma_l(x)=rho_m eta_l(sinh(k(b-x))+beta cosh(k(b-x))), k=rho_m chi_l, beta=chi_l/chi_g. Positivity follows because the polarization ratio lies between eta_l and eta_g. Total mass reduces exactly to beta*mu=sinh(u)+beta cosh(u), u=kb, mu=M chi_g/2. Strict increase in u gives unique b>0 iff mu>1; source jump S(0+)=rM/2 checks the delta reset source. Varying chi_l increases liquid mass at fixed b, implying strictly decreasing b; beta->infinity forces u->acosh(mu), with L1-rescaled sinh inner law and weak liquid delta atom of mass M-2/chi_g. Independently recomputed normalization, monotonicity for multiple rate sets, and u/b limits; inspected verify.py ODE/flux/orientation/quadrature checks. No claim outside the branch, no dynamics or microscopic convergence. Finite samples alone do not establish universal theorem.

## originality

PASS

Grange's arXiv:2610.26149v2 solves the same local-reset MIPS model with ONE homogeneous alpha, including the gas profile, threshold and condensed mass. It does not provide a distinct liquid/gas tumbling-rate matching law or singular alpha_l->infinity conditional shape. Evans–Majumdar 2018 is one RTP, Cates–Tailleur addresses density-dependent motility, and other generic transfer methods are related but not located with this full conclusion. Originality is best-knowledge, not worldwide priority proof.

## value

PASS

Different dense-phase reorientation is physically motivated and mathematically changes the inner transfer modes. The result separates observables fixed by dilute flux (nucleation threshold and condensed mass) from tunable width and center height, then establishes a nontrivial concentration-without-mass-loss limit and explicit conditional inner profile. This is a meaningful exact parameter-perturbation/limit theorem, not a mere renaming of the homogeneous formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
