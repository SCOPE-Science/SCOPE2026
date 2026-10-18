# Independent mathematical audit

## correctness

PASS

For n=3r the source interaction law Khat=2r/n I+r²Σ realizes [[1,chi,0],[chi,1,0],[0,0,1]] with Σ=r^-2[[1/3,chi,0],[chi,1/3,0],[0,0,1/3]], positive definite exactly for 0<chi<1/3. The actual simplified-Muon block-polar update is factor minus η times sign(factor times Khat z), z=(a²-1,b²,c²). Let δ=η²/4, t=η sqrt(8-η²)/4, q=t²=2δ-δ², 0<η<1. At X+ all factors and reduced forces are positive, so one full step subtracts η in each block to X-. At X- the forces Khat z- = (-(1-chi)q,(1-chi)q,η²/4), while factor signs are (+,-,-), so all gradient block signs are negative and the next step adds η, yielding X+. All three blocks nonzero at both endpoints, avoiding nonunique polar factors. Reduced loss at X-=(1-chi)q²+η^4/32>0, proving a real non-ground-state period-two orbit for every parameter pair. Independent checker verifies actual sign toggling and positive loss on rational/float witnesses; all-parameter proof is algebraic.

## originality

PASS

The originating Shen–Yang–Shi–Ma–Teng–Ma mixed-spiked paper establishes the factor-manifold sign reduction and reports fixed-step oscillation numerically, but its coupled examples do not provide a parameter-uniform exact coupled two-cycle of the factor iteration. Ma–Huang–Chi–Chen derives decoupled scalar spectral recurrences and analyzes geometric step decay; those cannot directly produce an off-diagonal signal–nuisance cycle. A scalar Signum two-cycle in Resultary confirms that generic sign-step periodicity is prior art; the exact feasible coupled matrix-sensing orbit is the surviving construction. Residual risk of an unpublished equivalent coupled sign-map example remains.

## value

PASS

Demonstrates an exact nonconvergent factor-level orbit in the first genuinely off-diagonal coupling regime of an established optimizer testbed, proving that observed fixed-step late-stage oscillations are not an artifact of diagonal decoupling or numerical coefficient plots. The parameter continuum, admissible positive-definite covariance and nonzero-gradient witness supply the structural boundary sought by the originating analysis. The result is not an unsupported claim about generic training performance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
