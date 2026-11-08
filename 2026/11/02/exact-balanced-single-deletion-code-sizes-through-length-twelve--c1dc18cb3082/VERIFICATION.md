---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Modified Varshamov–Tenengolts residue mod (m+1) provides at least Catalan(m) mutually non-confusable balanced words; checksum differences for deletion-confusable distinct balanced words count a nonzero number <=m of crossed opposite symbols. For all m=1..6, actual dual_certificates.json integer weights of scale 1,000,000 have every source word deletion-shadow cover >=1,000,001 and objective totals 1,000,001;2,000,002;5,000,005;14,195,149;42,317,279;132,512,205, each strictly below (Catalan(m)+1)*scale. Independently fetched and decoded both actual signed Git blobs and reconstructed every word and distinct deletion shadow in a separate JavaScript verifier: all full finite-universe inequalities passed, sizes 2,6,20,70,252,924. Exact primal_gap_m4.json numerators have total 1,419,498 /100,000 and maximum output load 99,999 /100,000, proving strict fractional gap. Unit duals for m=1..3 in the inspected certificate prove LP integrality. These are exhaustive rational finite proofs for m<=6, not an infinite Catalan formula.

## originality

PASS

Cullina–Kulkarni–Kiyavash 2012 establish optimal chromatic number and checksum coloring for constant-weight deletion-confusability graphs; a coloring into m+1 classes only provides A_m>=Catalan and does not imply matching independence upper bounds. Kulkarni–Kiyavash 2012 establish general deletion-channel fractional matching upper bounds but do not state these six exact dual certificates or the first balanced LP fractional gap. Adjacent Resultary single-deletion catalogs concern unrestricted length-six codes or other channels, so do not dominate central constant-weight values. Historical independent-set tables remain a residual priority risk.

## value

PASS

A complete exact initial finite profile for a natural weight-constrained deletion channel plus the first failure of its canonical LP relaxation are meaningful coding-theoretic invariants. Upper bounds require nontrivial all-word integer dual coverage certificates; neither a known coloring nor routine recomputation proves the first relaxation gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
