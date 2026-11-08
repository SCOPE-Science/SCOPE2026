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

For k≥1, write rho^k(0)=AB with A=rho^(k−1)(0), B=rho^(k−1)(1). A cyclic window of length at most 2|A| is contained in ABA or BAB according to its starting block; these equal rho^(k−1)(010) or rho^(k−1)(101). Both base trigrams occur in the substitution fixed point, so every cyclic factor occurs linearly in the infinite word. The 8 admissible preimage digrams form a substitution-closed set, and all occur by rho^4(0). Four exact length-16 coded supertiles span all windows up to length 16, giving 36 palindromes and none at lengths 15/16. Centered factors preclude any palindrome ≥15. Exhaustive circular enumeration of k=0..8 and explicit occurrence of all 36 linear palindromes inside R_8 prove sharp stabilization at k=8; nested dyadic prefixes preserve inclusion. Independent checker corroborates the finite exact ingredients; the general containment comes from the three-block embedding.

## originality

PASS

Very important implication: Schaeffer–Shallit 2015 already lists the eight maximal *ordinary* Rudin–Shapiro palindromes. Their centered subpalindromes determine the 36-word infinite palindrome language, so that language enumeration *alone is covered* and must not be presented as original. The remaining substantive claim is the all-length cyclic-to-linear factor containment for each full dyadic prefix, plus exact rank-eight circular stabilization, not implied by maximal ordinary palindromes or earlier prefix attractor results. Allouche 1997 full text inaccessible (Oxford VPN disconnected), creating residual priority risk; based on inspected material the surviving cyclic claim is original.

## value

PASS

Cyclic closing can create new factors absent from the infinite sequence; proving it never happens at any scale for this distinguished automatic word is a structural boundary-fidelity theorem, with a sharp exact stabilization of all cyclic palindromes. The ordinary 36-word count is prior-derived support only; the independently useful cyclic theorem and rank are mathematically substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
