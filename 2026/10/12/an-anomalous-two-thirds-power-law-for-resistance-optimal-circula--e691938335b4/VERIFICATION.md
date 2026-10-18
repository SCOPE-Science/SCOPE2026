---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For priced unit-conductance budget on prism C_n square K2, n>=3,t>0, Laplacian on 1-perp injectively parameterizes edge weights; tr(L^{-1}) has strictly positive second variation along any nonzero perturbation, hence globally unique connected optimum. Graph edge-orbit averaging forces rim a and rung b>0. Fourier layer blocks give nonzero eigenvalues a sigma_k and a sigma_k+2b (except symmetric k0), K=2n²(2+t x)(A_n+S_n(x)) with x=b/a, A_n=(n²-1)/12. Poisson-kernel sum yields S_n=n coth[n arcosh(1+x)/2]/(2 sqrt(x(x+2))). Derivative stationary equation t(A+V)=4U where U=sum(sigma+2x)^-2,V=sum sigma(sigma+2x)^-2. T(x)=4/(A/U+V/U) strictly decreases from infinity to zero: U decreases and V/U increases by monotone likelihood ratio, proving unique minimizer. For x=c n^-2/3 uniformly on compact c, coth→1 exponentially and S_n~n^(4/3)/(2sqrt(2c)); rescaled excess objective tends g(c)=tc/12+(2c)^-1/2. Trial upper bound and positive S lower bound compactly trap n^(2/3)x_n; strictly convex g minimizes at c=(18/t²)^(1/3). Thus b~c/(2n^(5/3)), K*=n^4/3+(18t)^(1/3)n^(10/3)/2+o. Checked differentiations and boundary t,n conditions; finite original exact matrix-inversion checker inspected but not extrapolated.

## originality

PASS

Best-of-knowledge surviving original contribution; compare mathematical implication rather than titles/parameters. Ghosh–Boyd–Saberi proves general convex total-effective-resistance design, not the specific priced prism orbit equation/asymptotic law. Azimi–Farrokhi and Cinkir formulas use unweighted circular ladders and thus do not optimize vanishing rung weights. Related 2014 Carmona–Encinas–Mitjana studies weighted linear ladders; only abstract was accessible and cannot be declared whole-document noncoverage.

## value

PASS

Total effective resistance is a standard network-design objective on a canonical circular ladder; allowing a priced rung class uncovers a nontrivial resource-allocation singular limit. The globally optimal ratio shrinks n^-2/3 yet retains connectivity and improves n^4 leading coefficient relative to uniform conductance; exact finite optimizer plus two-term asymptotics are mathematically useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
