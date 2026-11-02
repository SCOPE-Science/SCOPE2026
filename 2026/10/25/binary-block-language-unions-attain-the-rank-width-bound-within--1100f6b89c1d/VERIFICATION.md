---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For A^d every valid fixed-depth prefix has one right residual; B^d has one at even and two at odd depths. The union has nonempty quotient widths 1,2,3 at internal even depths, 5 at nonterminal middle odd depths, 3 at the final odd depth, 1 at the end. Different depths have disjoint residual word lengths. Sum=8d−6 plus one shared dead state gives 8d−5. At depth 1 at most two prefixes, against product-rank allowance 5, loses 3; penultimate rank has at most three nonempty one-letter residuals, losing 2; all other ranks saturate. Check d=2 endpoint non-overlap and infinite d≥2 with Myhill–Nerode. Independent exact enumerator d2..6 confirms but does not prove all d.

## originality

PASS

The published block-language union bound and a ternary tightness witness are acknowledged. The additional exact binary rank-by-rank quotient profile, family sc=8d−5 and sharp loss of precisely five within this specific width profile are derived directly. This is a modest special-profile result, not a global binary optimum. An encoding of the ternary witness makes indirect prior implication the principal priority risk.

## value

PASS

The exact binary rank-width endpoint obstruction and a sharp unbounded witness family give a meaningful finite-alphabet boundary case for known block-language union complexity bounds. The exact five-state loss for the specified width profile, not merely an encoding of a known witness, is the narrow independently useful invariant and benchmark; this is not a general binary upper-bound classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
