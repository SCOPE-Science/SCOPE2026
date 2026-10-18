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

# Verification of the circular-ladder zero-forcing classification

The result is proved mathematically in `RESULT.md`, with exact input definitions and full boundary scope. The executable checks below are finite and cannot replace an infinite-family proof.

## Actual checks

Run `python3 verify_direct.py` and `python3 verify_templates.py` using Python 3 without external dependencies. `verify_direct.py` independently constructs \(C_n\square K_2\) and simulates ordinary zero forcing for every three- and four-vertex set for \(5\le n\le13\), testing both the five candidate families and exchange edges. It checks adjacency reciprocity, connected components and exact degree histograms. Its record is `direct_results.json`.

`verify_templates.py` separately instantiates the symbolic patterns for all \(6\le n\le50\), constructs the exchange graph from pairwise three-vertex intersections, checks every entry in the five-type adjacency table, and computes counts and connectivity. Its record is `template_results.json`. Canonically sorted-state SHA-256 digests agree between the two constructions where compared.

At \(n=6\), both yield 78 optimal sets and 288 exchange edges, with degree frequencies 5:24, 8:48, 12:6. At \(n=13\), direct enumeration yields 169 sets and 624 edges. At \(n=50\), the symbolic test yields 650 sets and 2400 edges. The \(n=5\) boundary has a distinct degree profile, so the theorem explicitly requires \(n\ge6\).

## Boundaries and limitations

All counts depend on vertex-distinguished sets, ordinary one-white-neighbor forcing, and token jumping rather than sliding. Computational checks cover the stated finite ranges only; the proof's initial-force classification and finite parametric template-count argument establish the general statements. No external or independent audit is claimed.
