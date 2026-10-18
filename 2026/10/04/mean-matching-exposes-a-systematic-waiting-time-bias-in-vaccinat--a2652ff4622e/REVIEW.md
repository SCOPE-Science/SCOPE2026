# Independent mathematical audit

## correctness

PASS

For waiting T independent of Exp(h), probability immune before infection is Laplace transform E(exp(-hT)). Strict Jensen gives bound e^(-hT*) with equality iff deterministic T. Mean matching theta_V=1/T* yields P_exp=1/(1+x)>P_fix=e^(-x) for x=hT*>0. Constant inflow gives fluxes p0P and p0(1-P) and stock p0(1-P)/h, with reverse ordering of breakthrough/waiting stock. Derivative d[e^x/(1+x)]/dx=x e^x/(1+x)^2>0. Independently checked six x values, but strict Jensen/competing risk proves arbitrary distributions.

## originality

PASS

The 2022 ODE/transport vaccination-model comparison explicitly says its fixed delay and exponential exit parameters lack a direct correspondence. Its full accessible source does not state the mean-matched constant-hazard Laplace-transform inequality or steady-flow discrepancy; specialized contribution is model calibration, not Jensen convexity as new mathematics.

## value

PASS

Resolves a specific calibration ambiguity explicitly identified by the source epidemic models: matching the mean waiting times leaves a systematic one-sided immunization and backlog error, with exact dependence on dimensionless x=hT*. Valuable benchmark for interpreting exponential ODE versus fixed-delay transport assumptions, without claiming fully coupled outcomes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
