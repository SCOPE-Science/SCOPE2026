# Independent mathematical audit

## correctness

PASS

From Exner--Spitzkopf equation (3.6) directly reconstruct R_beta(L)=[nu-e_{rho_beta}+nu eta_{rho_beta}^2 L tan(beta/2)]/[1+eta_{rho_beta}^2 L tan(beta/2)]. With L=x/tan(beta/2), nu<0, Delta=nu-e_rho>0, a=-nu>0, the quotient tends to (Delta-a eta_rho^2 x)/(1+eta_rho^2 x), positive for 0<x<Delta/(a eta^2). Dirichlet eigenmode counting in this positive window and min--max imply liminf beta N_beta(nu)>=2x sqrt(R0(x))/pi. Independent symbolic differentiation confirmed g(y)=y^2(Delta-a y)/(1+y) has derivative y[2Delta+(Delta-3a)y-2ay^2]/(1+y)^2 with exactly one interior positive root ystar=(q-3+sqrt((q+1)(q+9)))/4. Endpoint vanishing makes it the unique global maximum in the trial family. For mu=alpha delta0, checked symmetric double-delta matching equation 2k=alpha(1+exp(-2k rho)) and normalization eta^2=[rho+(2k-alpha)^(-1)]^(-1). Thus the claimed formula is correct as a one-sided spectral lower coefficient; no Weyl law.

## originality

PASS

The source full text (eq. 3.6) already gives the exact variational quotient and an unspecified positive coefficient C_nu in Theorem 3.1; it does not optimize the beta-dependent longitudinal scaling to identify the explicit limiting constant. Prior bound-state existence papers cover other regimes. Originality is the optimized explicit coefficient within that specific trial family, not the variational inequality itself.

## value

PASS

The explicit coefficient converts a nonquantitative inverse-angle eigenvalue accumulation lower bound into a computable asymptotic guarantee using physical transverse parameters; the delta specialization gives a concrete threshold estimate. Such quantitative information is useful for comparison of soft-waveguide geometries, even absent a matching upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
