---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The endpoint identities βr=1, β−1=r, and 1−r=p show that A maps onto A∪B and C onto B∪C; the relative lengths of the stay and return target atoms are r and p. Each B choice sends the whole switch interval onto exactly A or C. On each allowed transition the conditional coordinate is uniform on the target atom by the constant affine slope, even given any preceding finite atom history. Thus the stated P_q applies, and solving the balance equations gives masses (q,p,1−q)/(1+p), which yield the frozen density. The same Markov and branch argument at successive visits to B gives i.i.d. L=1+J, with J geometric on {1,2,…} of parameter p and independent of the fresh Bernoulli-q mark. The length-independent mark selects reward 1 or J, so E[R]/E[L]=(1−qr)/(1+p). With ρ equal to this ratio, total variance gives Var(R−ρL)=(r/p²)[qρ²+(1−q)(1−ρ)²]+q(1−q)r²/p². Use qρ²+(1−q)(1−ρ)²=(ρ−1+q)²+q(1−q) and ρ−1+q=p(2q−1)/(1+p). Dividing by E[L] gives an equivalent profile (pr/(1+p)³)(2q−1)²+(r+r²)q(1−q)/(p(1+p)); expansion yields exactly the displayed positive concave quadratic. Ergodicity of the finite chain gives the almost-sure law. The cycle CLT applies and geometric boundary tails are negligible on the square-root scale. Independently, the tilted matrix for the labeled transitions has the frozen cubic. Its Perron root at tilt zero is isolated and simple for 0<q<1, so a complex tilt neighborhood admits an analytic leading eigenprojection and an exponentially smaller remainder in the stationary generating function. Cauchy estimates then give convergence of its first two normalized log derivatives and in particular of Var(S_n)/n; the same analytic expansion yields the Gaussian limit. Endpoint biases are only limits in the claim. Independent evaluation gave V_min≈0.0894427191000, V(1/2)≈0.4736067977500 and the factor ≈5.295084971875.

## originality

PASS

Credit only the evaluated second-order digit-count profile across all biases for the stationary absolutely continuous model and its sharp optimization. The Markov/invariant-law framework, golden full-branch return maps, their words and geometric timing, and the independent digit process under a different measure are prior. No overlapping all-bias variance theorem or stronger matching fluctuation result was identified in the inspected passages.

## value

PASS

For the natural stationary digit-count observable, the same mean at balanced bias could suggest fair Bernoulli-like fluctuations and the unchanged switch clock could suggest little bias dependence. The exact all-bias dispersion distinguishes both: the timing is unchanged while the second-order statistic is strictly optimized at fair switching, and the independent-fair benchmark with equal digit mean gives a substantially different variance. Researchers using stationary digit counts can use the precise rate and distinguish the AC and maximal-entropy preparations. The contribution is this evaluated, optimized profile for the random interleaving, not application of a generic CLT or recomputation of known branch lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
