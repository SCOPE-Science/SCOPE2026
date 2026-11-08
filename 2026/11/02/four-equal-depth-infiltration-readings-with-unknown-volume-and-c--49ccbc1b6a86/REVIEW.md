# Independent mathematical audit

## correctness

PASS

For positive K,a,F0 and step h, three time differences obey tau_i=lambda*h-S*log((x+i+1)/(x+i)) with S=lambda*a>0 and x=(F0+a)/h. The two discrete second differences satisfy delta0=S*D(x), delta1=S*D(x+1). D(x)=integral_0^infinity exp(-xt)(1-exp(-t))^2/t dt: normalized-Laplace variance makes log D strictly convex, so D(x)/D(x+1) strictly decreases from infinity to 1 and has a unique inverse. Reconstructed lambda=(tau0+S log(1+1/x))/h, a=S/lambda, c=z0+a-hx and t* fixed by t0. The extra strict tau0>S(1/x-log(1+1/x)) is exactly F0>0; this also ensures tau0>0 and positive lambda. Varying x continuously with only two differences proves an open continuum for every admissible three-time data set. Independent 100 seeded synthetic four-level reconstructions and monotonic ratio checks corroborate formulas; not a noise-stability result.

## originality

PASS

Best-of-knowledge originality after primary-text and implication comparison: dual unknown-origin four-level global inverse not directly established by the accessed Green–Ampt sources. Inaccessible relevant sources are recorded as residual priority risks rather than converted to false assertions.

## value

PASS

The forward Green–Ampt law is established, but simultaneously unknown clock and volume origins make inverse calibration genuinely ambiguous. This gives the sharp four-reading minimum, an explicit globally invertible physical inverse, and a necessary/sufficient feasibility inequality, rather than only local Jacobian rank or a numerical fit. Exact noisy conditioning is outside its scope, but this structural identifiability limit is natural for field-level sensor calibration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
