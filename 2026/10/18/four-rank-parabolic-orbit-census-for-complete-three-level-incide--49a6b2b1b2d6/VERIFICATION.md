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

For arbitrary base field, fixing rank u fixes the dimension of ker A. Relative position of ker A and im B is exhausted by intersection dimension v−t, and independent source and target basis changes exhaust the choices of surjection B and injection on Y/ker A. Conjugating by the unipotent off-diagonal S,T changes only C, by SB−AT. The entire kernel of C ↦ (ker B → X/im A) consists of such changes: first extend the im A-valued part on ker B, then factor the remainder through B. The restriction/quotient map is onto. By complementary extensions, the Levi stabilizer acts independently and fully on the two residual spaces, so w gives exactly one orbit per admissible tuple. Counting choices of the intersection, its projection and its lifts produces q^{t(b−u−v+t)}; multiplying the injection counts and constant C-fibre count verifies every cardinality factor. Projection of im N to Y has dimension v with kernel im A+C(ker B), so the rank and Jordan formulas follow, and the uniform quotient-map distribution proves conditional independence. The balanced summand is h[(2 times sum over ell from 0 to m of min(ell+1,h))−min(m+1,h)] for m=max(u,v) and h=n−m+1. Independent symbolic summation of its two polynomial pieces gave the claimed parity formulas. Independent image-cardinality enumeration, via python /workspace/branches/independent-reproductions/algebra_reproduction.py, verifies all 4096 triples for (q,a,b,c)=(2,2,2,2) and 6561 for (3,2,2,1). The finite checks are corroboration only; the classification proof uses the full parabolic, not just the unipotent radical or the incidence-algebra unit group. The bundled checker was inspected, not executed.

## originality

PASS

Pass for the explicit all-t finite-field conjugacy census with cardinalities and balanced-level count. Exclude from novelty the established orbit finiteness and quiver/module classification, the Jordan marginals, and the exact previously published numerical t=0 element-count summand. The earlier t=0 source does not assert its rank fibre is a single full-parabolic orbit, and the general finite-field per-orbit factor for t>0 is not supplied there.

## value

PASS

The first complete block-poset case with a nontrivial composite and a residual long block is natural. Counting each full-parabolic orbit, not merely its ambient Jordan label, gives usable exact sizes for all dimensions and field orders and an explicit field-independent balanced count. The positive-composite dimension factor and conditional distribution make this more than another marginal calculation or the already known square-zero slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
