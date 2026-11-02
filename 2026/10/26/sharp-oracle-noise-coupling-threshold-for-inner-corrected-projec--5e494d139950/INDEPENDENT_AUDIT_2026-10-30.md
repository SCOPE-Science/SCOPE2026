# Independent mathematical audit

## correctness

PASS

PASS: Checked published IPFE tableau Eq114 against all four source-defined k0..k3 stages. Substitution on ah=1 gives v=lambda(1-lambda)x+h[lambda²eta0+(1-lambda)eta1]; k3-k2=lambda a v-(1+lambda)eta2+eta3, so x_next=Gx+sum c_i eta_i with c=(hLlambda²,hL(1-lambda),-hxi(1+lambda)/(2lambda),hxi/(2lambda)). Squaring under stipulated moment/covariance and independence across outer steps proves Q and the geometric-variance recurrence for every n. The nonnegative deficit term scales (1-rho)/lambda² with coefficient approaching h²sigma²/2; remaining Q0→5h²sigma²/2, so the biconditional and both limits follow without cancellation. G<3/8. Independent exact rational stage arithmetic and all five correlations verified in >1000 combinations, but the threshold follows analytically for arbitrary lambda.

## originality

PASS

Qualified best-of-knowledge statement-based originality after checking primary comparison and relevant published Resultary records; no uninspected full text asserted not covering. Old deterministic tableau plus classical variance identities permit a new calculation, but no inspected primary statement proves the infinite-horizon iff coupling threshold or independent-batch Ω(lambda^-2) law for this IPFE model. The inaccessible primary remains a named historical risk.

## value

PASS

PASS: Deterministic RK stability of a new derivative-corrected projective method does not guarantee bounded stochastic-oracle errors. The theorem identifies an exact coupling rate, leading constants, and independent-sampling batch complexity for the simplest meaningful stiff scalar fast mode, enabling implementers to distinguish a stable integrator from a noise-unstable corrected integrator. The covariance calculation is elementary but the derived sharp performance boundary is model-motivated, not an arbitrary normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
