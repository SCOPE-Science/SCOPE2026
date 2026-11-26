---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Stationary flow is π_i r_i=J, so the reversed chain jumps counterclockwise out of i at the same rate r_i. Reflections i↦−i for b=d and i↦2−i for a=c conjugate the generators, preserve π and parity, and prove full reversibility on the two surfaces. In each alternating word three intervals change parity; only the one-jump paths contribute at order h³, giving JU and JV. Their difference is −J(a−c)(b−d), proving necessity. Stationary marginals of 00 and 11 force the only nonpalindromic length-three pairs to be equal. For length four I checked the prefix/suffix balance at 000, 111, 010, 101, 001 and 100: the five other signed differences are 0, 0, Δ, −Δ, Δ as ordered in RESULT.md. A word with m changes has probability Θ(h^m) because exactly the required jumps with all other intervals jump-free give a positive leading term. For nonalternating reversal pairs m≤2, so (p−q) log(p/q)=O(h^{6−m})=O(h⁴); the alternating pair gives the stated cubic coefficient with O(h⁴) remainder. Every word has positive probability at fixed h>0. The asymptotics are for fixed positive rates, and the minimality is only for equally spaced observations. The supplied script was inspected, not executed.

## originality

PASS

The explicit finite-block KL law is the distinct supported contribution. The general impossibility for fewer than four equally spaced binary frames is prior literature. The exact rate boundary and cubic four-frame probability asymmetry have demonstrably equivalent coverage in a distinct later-dated catalogue record, so I do not credit those as unmatched or resolve priority from catalogue dates. That overlap does not give the explicit all-word KL coefficient or its remainder.

## value

PASS

The motivating question is how much directional information remains in the shortest usable uniformly spaced record after parity hides the microscopic cycle. The exact leading KL quantifies that question, identifying the uncommon alternating records that carry the leading information and the dependence on both opposite-rate contrasts. This is not a microscopic dissipation estimate (the microscopic reversed paths lack support), nor an entropy rate. It is a concrete finite-window observable near a sharp reversibility boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
