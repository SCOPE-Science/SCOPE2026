---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For the real cubic Day--James norm, the sphere consists exactly of same-sign cubic arcs, opposite-sign taxicab facets and nonsmooth axes. On a cubic arc, the unique norming functional fixes the Birkhoff--James partner; for t<=1/2 one norm exceeds 4/3, while for t>=1/2 the cubic expression 1+F(t) has F strictly decreasing to F(1)=3/2^(4/3), established by the explicitly positive H(t) bound. Taxicab partners are forced to the cubic diagonal and give the same sharp value only at their midpoint. At axes the complete supporting-functional interval yields strict lower bounds >4/3. The balanced unit pair attains both norms equal to (1+3/2^(4/3))^(1/3). The analytic stratum split and inequalities prove the continuum claim; independent SymPy identities and 1250 numerical configurations only corroborate it.

## originality

PASS

The primary 2022 paper treats exactly the same cubic norm and g_perp but reports only about 1.2987, with no radical or complete extremizer proof. The 2016 work treats classical J; the 2024 follow-up develops h_- and h_+ and only invokes g_perp for general comparisons, not this exact benchmark. Published records for the quadratic Day--James case and a different mixed-plane James constant are not implication sources.

## value

PASS

The established g_perp invariant is evaluated exactly on a mathematically canonical mixed cubic/taxicab Banach plane previously left at only a decimal benchmark. The complete Birkhoff support-functional stratum analysis supplies an attaining closed radical and explains its location. This is a motivated small exact fact, not a general ell_p classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
