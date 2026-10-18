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

# Verification and reproducibility

The theorem is proved analytically in `RESULT.md`. Independently, run `python3 verify_fan.py` under Python 3 using no third-party packages. The checker enumerates acyclic orientations, constructs integer-coordinate zonotope vertices, finds reversible orientation flips (polytope edges), and compares the exact parallel-edge census with contraction predictions. For small fans it independently integrates actual edge crossings over every distinct interval of vertex-projection heights. It also checks both exact equality-normal classifications on all 19,496 nonzero integer normal patterns with entries in \(\{-2,-1,0,1,2\}\) (hub coordinate fixed to zero) for path sizes three through six.

Observed output includes exact vertex/edge pairs \((18,28)\), \((54,114)\), \((162,432)\), \((486,1566)\), and \((1458,5508)\) for path sizes three to seven respectively, followed by 1,025 scalar assertions, 19,496 equality grid comparisons, and eight non-path tree-cone multiplicity profiles passed. The checker uses deterministic integer and rational arithmetic and a fixed pseudorandom seed for supplementary directional samples; its finite runs do not certify the universal theorem. For the all-dimensional mathematical argument, see the path inequality and equality analysis in `RESULT.md`.

No independent audit or validation has been performed.
