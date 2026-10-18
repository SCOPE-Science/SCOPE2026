---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

From W_{j+1}=W_j^a 1 W_j, the gap recurrence G_2=A^(a-1)CB and G_{j+1}=(G_jA)^(a-1)G_jCBG_j (A=a+1,B=a,C=1) gives only AA,AC,BA,BC,CB digrams. A reversible complete-gap sequence must be a run of A or an alternating B,C run. Boundary contexts cap its total length by a²+3a−1 for a>=4; the explicit palindromic W_3 factor of that length proves sharpness. The a=3 localization lemma says every length-19 factor occurs in W_3 of length 85, because length<=|W_2|=21 and all two-copy boundaries occur in W_3. Independently reconstructed its complete 37-factor certificate with no reversed pair and its length-18 palindrome. Any reversible longer factor contains a reversible length-19 subfactor. Finite samples at a=4..8 merely corroborate the proved infinite family.

## originality

PASS

PASS best-of-knowledge: the exact quadratic a-dependent reversal isolation threshold and exceptional a=3 localization are not implied by the inspected reflection-complexity treatment of classical sigma_2, or general reversal-free word existence theorems. The known threshold 13 at a=2 is correctly excluded. Unindexed rank-one/Chacon generalizations remain plausible.

## value

PASS

This supplies a sharp all-parameter transition between reversible and reversal-isolated factors for a canonical morphic-word family, including an exceptional a=3 value that requires a localized finite classification. Exact cutoffs are natural invariants needed to quantify reflection complexity and palindrome disappearance, not arbitrary sample computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
