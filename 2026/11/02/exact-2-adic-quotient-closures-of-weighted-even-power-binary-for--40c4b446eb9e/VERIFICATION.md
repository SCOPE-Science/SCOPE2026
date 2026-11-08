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

For even n, the exact odd-unit nth powers are 1+2^(v2(n)+2)Z2 by 2-adic logarithm. Comparing v2(x),v2(y) gives exactly the three value families 2^(nv)(1+qZ2), 2^(nv)(c+qZ2), 2^(nv)(1+c+qZ2), including zero. In nonsplit case d=v2(1+c)<h these are cosets with fixed valuations; dividing the nested unit subgroups yields precisely the nine balls and valuation classes, and local finiteness on nonzero annuli plus zero establishes closedness. In split case odd root of X^n+c gives simple-zero quotient-density. Nonnegative integers are dense in Z2. Independent modular direct enumeration matched 126 normalized image profiles; no inference of all-adic truth from finite residue tests.

## originality

PASS

Antony–Barman–Miska 2022 theorem 1.1 establishes the same dense-versus-nondense branch, but not the precise nonsplit value and quotient cosets. Miska–Murru–Sanna give the unweighted power-sum value closure for some exponents; coefficients c=1 modulo q reduce to those previously known unweighted cases. Novelty is limited to the remaining weighted nonsplit congruence classes and exact nine-ball classification; split density and identified unweighted special cases are not newly claimed. An implicit broader local polynomial image theorem remains a bounded priority risk.

## value

PASS

The exact topology of an established p-adic quotient-density family is a natural next question beyond yes/no density. Unit groups and valuation shells specify which local obstructions survive, with explicit weighted cases not reduced to the known unweighted theorem; no downstream theorem is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
