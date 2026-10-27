# Scientific review: sharp two-point Green–Ampt inverse classification

## Correctness

**PASS.** The normalized forward integral \(Kt=Bg(F/B)\), where \(g(u)=u-\log(1+u)\), gives the exact two-point ratio \(R_\rho(u)=g(\rho u)/g(u)\). The proof's key nonstandard step is global elasticity monotonicity: \(h(u)=u^2/[(1+u)g(u)]\) satisfies \(h'(u)<0\), because \(H(u)=u^2/(u+2)-g(u)>0\) and \(H'(u)=u^2/[(1+u)(u+2)^2]>0\). Therefore the ratio descends strictly from \(\rho^2\) to \(\rho\), giving exact existence, strict boundary exclusions, and uniqueness. Taylor expansion at small \(u\) and the logarithmic large-\(u\) identity establish both parameter boundary laws. The packaged Python checker passed 4,000 reproducible parameter recoveries, exact rational checks of the derivative identity, the exact example, and extreme-regime comparisons. Finite tests corroborate, but do not establish, the theorem.

## Originality

**PASS, with stated historical-priority qualifications.** Exact two-point feasibility \(\rho<q<\rho^2\), uniqueness of both parameters throughout that region, and the contrast between reciprocal and logarithmic inverse degenerations were compared against the relevant Green–Ampt forward literature and prior inverse-parameter studies. Zeleke and Si (2005) fully discuss inversion and numerical uniqueness for falling-head data; Rucker (2009) concerns joint electrical/wetting-front observations; Lai et al. (2015) concern an enhanced forward infiltration/redistribution scheme. The relevant inspected passages do not give this constant-head two-observation parameter-domain theorem. The source law alone is not treated as a novel contribution. The nearest incomplete comparisons are Warrick (1993), addressing general inverse hydraulic scaling, and Mohammadzadeh-Habili and Heidarpour (2011), addressing upward-front parameter estimation. These sources remain named risks, as does possible implication from a general nonlinear inverse-function monotonicity theorem. No absolute priority or independent validation is claimed.

## Mathematical and scientific value

**PASS.** Two observations are the minimal number naturally needed to recover the two effective positive parameters of this idealized forward model. The exact feasible region supplies a pre-fitting falsification test, as well as an inverse that is unique when feasible. The sharp and asymmetric endpoint degenerations identify where conductivity and capillary length separate poorly, and at what rate; the logarithmic edge is not conveyed by a generic uniqueness statement or the first-order forward-rate equation. These are structural statements about physical data compatibility and calibration conditioning, not isolated numerical examples or arbitrary parameter slices.

## Scientific limitations

Only exact, cumulative, uninterrupted-ponding observations with known zero-time and a constant two-parameter Green–Ampt law are covered. No measurement-noise stability theorem, statistical confidence interval, empirical validation, layered-soil or changing-rainfall extension, or independent audit is provided. The accessible historical coverage does not establish absolute originality.

Self-review: passed. Independent audit: not yet performed.
