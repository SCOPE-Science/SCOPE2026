# Independent mathematical audit

## correctness

PASS

The model and positivity domain were reconstructed from actual RESULT.md at the assigned source tree and matched Enatsu (2024) equations (15a)-(15b): n>0 and p>0 for all finite time by multiplicative prey equation and positive scalar DDE variation of constants (including tau=0). Logistic comparison gives finite K for prey. For h>=q=e^{-beta tau}, qH(n,p)=q z/(1+h z)<q/h<=1 for every finite z=(1+alpha p)n, so constant history supremum P bounds predator p(t)<=P by scalar method of steps. The finite K,P yield A=qH(K,P)<1 *even at h=q*. The root rho_A in (0,1) of rho_A+A exp(rho_A tau)=1 makes P exp(-rho_A t) a valid supersolution with dominating negative-time history, giving global p(t)->0 exponentially and excluding blowup. With d=(1+alpha p)p/[1+h(1+alpha p)n]->0, reciprocal prey u=1/n solves u'=(-sigma+d)u+sigma/kappa, whose eventual coefficient squeeze gives n->kappa. Thus a(t)=qH(n(t-tau),p(t-tau))->a_*=q kappa/(1+h kappa) in (0,1). For every eta with 0<a_*-eta<a_*+eta<1, two-sided scalar positive DDE exponential comparison after time T yields -rho_-(eta)<=liminf log p/t<=limsup log p/t<=-rho_+(eta), with rho_-(eta)>rho_+(eta) the unique roots for gains a_*-eta,a_*+eta; letting eta->0 proves the exact logarithmic rate -rho_*. Tau=0 is included by the same scalar root/ODE argument. If h<q and kappa>1/(q-h), N(v)=1/((q-h)(1+alpha v)) lies inside (0,kappa) and F(v)=q sigma N(v)(1-N(v)/kappa)-v switches from positive at v=0 to negative at infinity, so a strictly positive equilibrium exists for any positive sigma,alpha; this proves only parameter-uniform threshold sharpness. The independently written checker corroborated 11 exact rational saturation/equilibrium or bounded characteristic/root envelopes; it cannot prove universal DDE statements.

## originality

PASS

Best-of-knowledge originality for the *combined all-history/global sharp barrier and exact log-rate* on the exact delayed Enatsu–Roy–Banerjee system, not for the model, saturation inequality, equilibrium census, or generic scalar-DDE comparison theory. The 2024 primary Theorem 3.1 gives no-positive-equilibrium cases and local stability; those cannot logically imply attraction of every continuous strictly positive delay history or any tail exponent. A public same mathematical model periodic average theorem excludes periodic coexistence but explicitly leaves nonperiodic omega limits uncontrolled. The 2025 open-access Peng–Jiang delay acts on prey logistic feedback, a different dynamical equation. The closely titled Vishwakarma 2025 paper remains full-text inaccessible (only preview/abstract inspected); no positive evidence of coverage was found, but it is a genuine unresolved priority risk and failed searches are not treated as novelty proof. The exact all-history comparison argument including equality and the root limiting rate survives the inspected primary comparisons.

## value

PASS

This is a motivated global-dynamics problem left open by equilibrium/local-bifurcation analysis of an established cooperative-hunting maturation-delay model. The exact uniform handling-time criterion h>=e^{-beta tau}, including equality, yields a strong all-positive-history extinction conclusion regardless of cooperation strength alpha; the formula rho_* gives a natural quantitative observable (predator log-decline speed) and identifies its independence of initial history and alpha. The positive coexistence equilibrium for some tuples below the boundary supplies a sharp uniform obstruction. These conclusions are broader and more consequential than only checking the absence of equilibria or cycles. Standard comparison steps are used, but the parameter-uniform global theorem with sharpness and exact rate is independently useful for the specific nonlinear delayed model. It is not offered as a general theory for h<q or arbitrary delays.

The dated certificate retains the supplied scientific assessment, sources and limitations.
