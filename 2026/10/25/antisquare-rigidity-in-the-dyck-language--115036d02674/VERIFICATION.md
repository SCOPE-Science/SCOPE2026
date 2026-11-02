---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For any x complement(x), the number of maximal letter-runs is 2 mod 4 or 3 mod 4 according to parity of the run count in x. The displayed candidates have exactly four runs with both interior runs singleton; they admit neither two-run antisquares of order>=2 nor three-run ones with middle run length>=2. For uniqueness, the canonical Dyck decomposition w=0u1v allows strong induction since avoiding contiguous forbidden factors is hereditary. Exhaustive cases according to semilengths a=|u|/2 and b=|v|/2 exclude every pair but those yielding the displayed candidate: forbidden explicit words 0011, 010101, 0110, 1100 and the family 0^a 10 1^a 01 or 01 G_b appear at relevant seams. Catalan count gives exactly 1/C_n. Independently generated all C_n Dyck words at n=1..10 and enumerated every factor/order>=2, finding precisely the stated sole word at each n. The all-n induction, not this finite check, proves the theorem.

## originality

PASS

Baranwal--Currie--Mol--Ochem--Rampersad--Shallit already classify many minimal forbidden antisquares and supply the longer obstruction family used in the induction. Mol--Rampersad--Shallit study other avoidant Dyck languages and first-return constructions. No inspected older theorem states the complete intersection of good binary words and Dyck words is a singleton at every semilength; this is the surviving exact classification. Simplicity of its proof raises ordinary potential prior-deduction risk but does not itself make it known.

## value

PASS

The precise interaction of two well-motivated languages, balanced Catalan paths and forbidden binary complement squares, collapses an exponentially large Catalan class to exactly one explicitly described word of each semilength. This exact all-length structural classification is more informative than small checks and supplies a reusable strong restriction for Dyck pattern-avoidance constructions. It need not imply a deeper theorem to qualify.

The dated certificate retains the supplied scientific assessment, sources and limitations.
