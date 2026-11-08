---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Uniform labeled Cayley tree with three fixed DISTINCT vertices: conditioned marked u-v path length ℓ, rooted-forest determinant m n^(r−1) counts completions. Marking a root gives generating function a(z)^(n−ℓ−2)*(ℓ+z)/(ℓ+1); marking nonroot gives z a(z)^(n−ℓ−2). Mixture by probability p=(ℓ−1)/(n−2) yields 1+B+J(1+C), with B,J,C independent, for ℓ≤n−2; ℓ=n−1 forces H=2. Exact leaf P(H=1|ℓ) decreases, hence all-n positive nonleaf covariance; at penultimate versus last ℓ the ≥2 and ≥3 tail events cross. Centered generating function cancels n^−1/2 contribution and order-n^−1 contains (2−x²)/2 z e^(z−1)(z−1)²; Rayleigh L/√n and uniform exponential tails yield √n covariance constant −sqrt(π/2)b_q/2 for fixed q. Independently computed n=8,ℓ=4 degree probabilities {1:49/128,2:133/320,3:11/64,4:9/320,5:1/640} summing to 1. Fixed q≥4 eventually negative, q=3 leading zero only. The actual package script enumerates all Prüfer codes n≤8; its logs are not accepted as an infinite proof.

## originality

PASS

Qualified PASS for third-vertex (neither endpoint) exact degree mixture and fixed-threshold tail covariance sign reversal. Earlier published Resultary endpoint-degree conditional law directly determines some mean identities through degree conservation but NOT this third-degree distribution or high-threshold cancellation. Classical rooted-forest formulas are tools, not claimed new.

## value

PASS

A natural three-marked-vertex probabilistic statistic exhibits a nontrivial reversal of dependence under thresholding: nonleaf and mean regression increase while high-degree tail covariances eventually decrease. It is a reusable structural distinction between mean order and distribution order, not a tiny unmotivated enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
