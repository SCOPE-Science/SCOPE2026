# Independent mathematical audit

## correctness

PASS

PASS. At k=alpha+gamma+mu=beta K, the exact noise-zero, constant-h BIM is z_{n+1}=z_n+tau_n F(z_n), tau_n=h/[1+h(k+beta I_n)]. Positive initial S,I,R and S+I+R<=K stay in the invariant simplex; x_n=K-S_n>=I_n, I_n is positive strictly decreasing, and a uniform lower bound on tau_n proves extinction I_n->0. Stable forced recurrences give x_n,R_n->0. The ratio r_n=x_n/I_n satisfies a contractive affine recursion with limiting fixed point k/mu; reciprocal increments 1/I_{n+1}-1/I_n->beta k h/[mu(1+kh)]. Cesaro proves lim nhI_n=mu(1+kh)/(beta k). The ODE similarly has r(t)->k/mu and lim t I(t)=mu/(beta k). Independently checked exact rational step identities and an 800000-step trajectory, not as an infinite proof.

## originality

PASS

PASS, best of knowledge. The full accessible Schurz–Tosun paper sets out this actual balanced implicit update and proves invariant-domain properties and fixed finite-time convergence, but the examined model/method/results do not provide a fixed-positive-h critical infected 1/n amplitude or the exact ratio to the ODE. Earlier related SIS BIM noise-threshold work concerns a stochastic transverse stability boundary, not the nonlinear noise-free SIR critical tail. Classical SIR critical 1/t asymptotics alone cannot determine the scheme-specific factor 1+kh without analyzing this exact nonlinear update.

## value

PASS

PASS. Near epidemic invasion criticality, the leading extinction amplitude is a natural quantitative asymptotic invariant. The exact fixed-step factor exposes a limitation of an unconditionally positive scheme despite finite-horizon convergence and invariant-domain preservation. This is an interpretable, state-independent asymptotic bias, not a trivial sign or tiny finite instance; its derivation needs dynamics on a nonhyperbolic boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
