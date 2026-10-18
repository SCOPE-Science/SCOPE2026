---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Computational verification

The standalone script `verify_borel_chain.py` uses only standard Python. It constructs finite commutative chain rings using modular integer arithmetic and truncated prime-field polynomial arithmetic. For each tested ring, it constructs the upper-triangular unit group, directly solves commutation against every group element, and compares observed class sizes against the valuation formulas. It separately enumerates the action of units on additive-dual parameters and checks the character-degree multiplicities and sum of degree squares.

It tests integer residue rings of orders \(2,3,4,8,16,9,5\), plus truncated polynomial rings with \((q,m)=(2,2),(2,3),(3,2)\). The exhaustive group-level arithmetic therefore compares different rings sharing the same pair \((q,m)\). Expected terminal marker: `VERIFY_OK_BOREL_CHAIN_DUAL_SPECTRA`.

Finite enumeration does not establish the statements for arbitrary length, residue prime powers, or all ring isomorphism types. Those cases rely on the self-contained ideal-count and character-orbit proof in `RESULT.md`. No independent mathematical audit has occurred.
