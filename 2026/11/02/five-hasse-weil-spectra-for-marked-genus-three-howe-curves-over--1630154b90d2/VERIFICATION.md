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

All admissible ordered pairs equal 7*6=42, with 21 unordered enumerated in spectrum_21.csv. Explicit three quotient maps x+1/x, x-1/x, x^2 induce Klein-four H1 splitting into three elliptic factors, giving L_C(T)=product(1-t_i T+9T^2) and #C(F9)=10-sum(t_i). Independently implemented F9 arithmetic (a+3b, i^2=2) enumerated every one of the 42 coefficient pairs, reproduced five exact trace-triplet frequencies and all point counts. The 21-row source CSV agrees, and independent source verify_extensions.py models F9,F81,F729; no extrapolation to unbounded base fields.

## originality

PASS

Ohashi 2021 establishes the genus-three Howe model, elliptic splitting and superspecial maximality conditions; Moriya-Kudo 2022 develops broader Richelot isogeny algorithms and superspecial enumeration. Neither read passage gives the five polynomial multiplicities across all 42 marked models. Preexisting p-rank strata do not determine these Weil polynomial classes. Possible unindexed finite arithmetic table remains.

## value

PASS

A complete exact zeta census for the natural marked F9 Howe normal form yields all extension point counts and the Jacobian isogeny classes, not just a small sample or p-rank. The finite field/family is natural from genus-three elliptic splitting; value restricted to that marked family, not all genus-three moduli.

The dated certificate retains the supplied scientific assessment, sources and limitations.
