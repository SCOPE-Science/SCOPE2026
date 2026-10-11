---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The half-central-angle equation is continuous and strictly increasing on the relevant radius interval, so the polygon exists uniquely. Fresh integer recurrence reconstruction gives \(\deg P=384\) and \(\deg Q=768\); the constant coefficient has exact \(769\)-adic valuation two, degrees one through 383 have valuation at least two, degrees 384 through 767 at least one, and the leading coefficient valuation zero. These points lie on or above the segment from \((0,2)\) to \((768,0)\), with endpoints attained, so the Newton polygon has reduced slope \(-1/384\). Each local irreducible factor degree is divisible by 384, hence the geometric root has global degree 384 or 768, neither a power of two. The standard constructibility-degree criterion then proves nonconstructibility.

## originality

PASS

Czédli--Kunos Theorem 1.1(iv) already proves the broader existential fact that every odd order at least eight admits some nonconstructible cyclic polygon with at most two integer side lengths. It therefore covers existence at order 771, but does not imply nonconstructibility of this concrete multiset. Full-text inspection found no occurrence of 768, 769, or 771, and Resultary returned the assigned explicit witness as the exact hit. The originality claim is properly limited to the explicit consecutive-length witness and its local certificate.

## value

PASS

Although existential order-771 nonconstructibility is known, a concrete two-consecutive-integer witness with a short exact local-field certificate is a motivated exact object: it supplies reproducible data for a historically difficult order and can serve as a benchmark without invoking Hilbert irreducibility. This is more than recomputing a known table entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
