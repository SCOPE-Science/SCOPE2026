---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

PASS. Read the actual RESULT.md and verification code by their frozen Git blob SHA. The directed BEST and Matrix–Tree theorems give q^(q-2)((q-1)!)^q cyclic Euler tours; simultaneous contraction of two vertex-b turns with four distinct edges changes the factorial by 1/((q-1)(q-2)). The rooted Laplacian rank-two update leads to J=[q^2-q(2+x+y)+x+y+xy-u-v-uv]/[q^2(q-1)(q-2)]; a single shortcut gives p_abc=(q-1-x)/[q(q-1)]. Injective partial-match constraints on (a,d) and (c,e) leave only 0,1,direct-2,crossed-2 matches. Subtraction gives precisely the four listed covariance fractions, with their feasible q cutoffs; crossed becomes 0 at q=5 and >0 from q=6. An independently authored enumeration of Euler successor permutations checked all 24 and 20736 cyclic tours at q=3,4 and all corresponding ordered motifs against the joint formula. Those finite enumerations support, but do not establish, the all-q algebraic theorem.

## originality

PASS

Best-of-knowledge PASS for the complete sharp four-pattern sign classification and its global alphabet cutoffs, not for the raw counting method or determinant probability formula. Rødland 2006 supplies broader general pattern-count formulas and indeed implies the joint-probability ingredients, while Sawada–Gabrić supplies the uniform de Bruijn ensemble. Checked primary results do not explicitly derive the uniform sign transition, its zero class and exceptional negative motifs as one theorem. Any implication via routine substitution is a real residual coverage risk; the classification requires equality-pattern exhaustion and sign analysis, not a new general counting technique.

## value

PASS

PASS. A complete covariance sign law for two local motifs in uniformly sampled order-two de Bruijn cycles identifies exact positive, zero, and negative dependence, including a sharp q=5 all-nonnegative transition and q=6 strict-positivity transition. These are natural questions for assessing joint motif coverage in a random universal cycle, and the all-q classification avoids repeated casework from a general pattern-count formula. The value does not depend on treating the classical probability identities as novel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
