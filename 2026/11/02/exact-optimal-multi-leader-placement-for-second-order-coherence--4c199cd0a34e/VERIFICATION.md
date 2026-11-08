---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Block diagonal grounded path inverse has tail Green kernel min(i,j) and interior Green kernel min(i,j)(m+1-max(i,j))/(m+1). Squared Frobenius traces give P(m),Q(m) and strictly increasing p_r,q_r, so optimal gap allocations are exactly the cheapest available increments, with ties handled by exchange. Since q1=1/4,q2=31/36,p1=1,q3=77/36, both endpoints appear in every optimum exactly when n<=3k-2; strict convex uniform n^-4 scaling yields ratio 15^(1/3) of interior to tails and cost 1/(6D_k^3). Independent exact rational inverse and exhaustive minimizer checks covered 968 path-leader subsets for n<=9, including n=k. General result follows from Green and exchange proofs, not tests.

## originality

PASS

Best-of-knowledge PASS for the precise complete statement, after distinguishing prior objects, scope and implications. Relevant primary mathematical results were inspected, and none of the materially read theorems supplies the same whole claim. Earlier components are explicitly credited; unsuccessful indexing alone is not proof of priority. See four structured checks, primary reading and residual risks.

## value

PASS

The second-order position variance tr(L_FF^-2) for noise-driven grounded path networks is an established natural performance functional. An exact all-minimizer discrete allocation rule, endpoint threshold, and universal cube-root-15 spacing are useful optimization results, not a generic restatement of first-order leader placement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
