---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

A regular-differential Cartier calculation gives stable Cartier rank two when A!=0 and zero when A=0, with rank 2 (a-number 1) on every smooth fiber. The exact characteristic-five discriminant identity Delta=(a^2+c)A-2b^2(ac+b^2) implies Delta|A=0 has zeros iff b=0, hence two curves L0=(b,c) and L1=(b,c+a^2). The affine substitution z=c+3a^2 transforms A exactly to z^2+ab^2+a^4, a characteristic-five D5 isolated normal rational-double-point model; irreducibility via odd a-adic valuation and Serre R1+S2 yields normality. On a!=0, Delta=2b^2c^2/a. Along L0 the local relation c~unit*b^2 gives order 6, whereas c is a unit along L1 giving order 2. Independently verified the discriminant, D5 coordinate and restriction identities mod5 with SymPy; package direct GF5 verifier source checked, finite enumeration cannot prove a global Weil divisor.

## originality

PASS

Best-of-knowledge originality of the precise final result is retained after direct scope/implication comparisons and meaningful reading, with identified prior machinery and explicit inaccessible-source risks. No failed search is treated as a novelty proof.

## value

PASS

An explicit rank-drop locus in Picard Jacobian arithmetic acquires a canonical normal surface with a D5 boundary singularity and sharply unequal discriminant orders. The Weil multiplicities are relevant to degenerations and intersection theory in this natural coefficient-marked moduli chart, beyond generic Cartier matrix formulas or known a-number values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
