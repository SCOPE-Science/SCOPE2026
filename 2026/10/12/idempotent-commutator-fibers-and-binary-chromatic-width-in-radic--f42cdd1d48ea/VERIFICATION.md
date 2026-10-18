---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For A=kQ/J^2 the idempotent vertex coefficients are 0/1 and an arrow coefficient is free precisely when endpoint bits differ. The commutator arrow coordinate (p_u-p_v)r_a-(r_u-r_v)p_a then has q choices at each paired vertex-label change and supports a nonzero prescribed z_a only if BOTH bits change. Multiplying over arrows gives the four-state exact fiber polynomial for all loopless multiquivers and finite fields, including repeated/opposite arrows. The nonzero target support requires a vertex 2-coloring, and conversely one such coloring constructs a single idempotent commutator. For sums of h, a nonzero target arrow must be separated by at least one of h vertex bits, giving chi<=2^h; binary encodings of proper chi-colorings attain h=ceil(log2 chi). Zero target has width 0 and edges outside J do not occur. Independently enumerated complete GF(2) and GF(3) triangle fibers (35 exact target checks), confirmed GF(2) 26 idempotents, zero fiber 340, full support zero single-fiber; this is corroboration, not proof of arbitrary quivers.

## originality

PASS

The exact target fibers restricted to pairs of idempotents and sharp binary chromatic width are not implied by the older unrestricted q^2 chromatic bound, nor by results about invertible idempotent commutators in matrix rings. The triangle over F2 strictly separates restricted and unrestricted conditions. The 2002 general ring characterization of single commutators may specialize to the bipartiteness subclaim, but the full source was inaccessible, so priority of that portion remains a specifically named risk; exact all-fiber counts and sharp additive widths remain plausible distinct contributions.

## value

PASS

Prescribed commutator fibers of *restricted* factors form a natural algebraic invariant; the four-state formula provides every fiber, not merely existence. The sharp field-independent chromatic obstruction and unbounded gap from unrestricted commutator width on complete graphs are structural and useful for comparing algebraic constraints to graph colorings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
