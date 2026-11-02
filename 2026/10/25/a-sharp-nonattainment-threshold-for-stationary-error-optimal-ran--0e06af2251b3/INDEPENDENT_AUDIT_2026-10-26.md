# Independent mathematical audit

## correctness

PASS

For the scalar affine u'=1−3u and reciprocal-probability sampled implicit step, reconstructed the two affine maps r1=p/(p+2h), c1=h/[3(p+2h)], r2=(1−p)/(1−p+h), c2=−h/[3(1−p+h)]. The strict contractions have unique stationary law. First/second-moment fixed-point calculations yield the exact risk and sign of Vh(p)−1/36 governed by K(p,h). Independently verified the rational risk/K identity and resultant −2592 h^4(3h+1)^2 P(h) symbolically in SymPy, with P(h)=200h^5+5829h^4−1620h^3+528h^2−1008h−528. Descartes positive-root argument, Jensen-style derivative uniqueness and resultant give one threshold h*=0.7166725626…, unique equality probability ~0.8029974, and for h>h* strict nonattainment as p tends to 1. Endpoint p=1 excluded by unbiased random sampling; no claim for finite horizon/general operators.

## originality

PASS

Best-of-knowledge original precise final theorem after comparison with source-specific hypotheses; all named comparisons and inaccessible-source risks recorded.

## value

PASS

A natural stationary optimal-design question for a published randomized resolvent integrator: a fully worked minimal heterogeneous splitting exhibits exact algebraic attainment/nonattainment bifurcation, with a boundary optimizer excluded by positive-sampling constraints. The exact threshold is not a mere reparameterization of usual finite-horizon stability or operator-variance tuning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
