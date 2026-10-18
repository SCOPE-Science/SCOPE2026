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

# Verification and limitations
The analytic proof in `RESULT.md` enumerates all overlap types for a triangle and an induced chordless cycle: zero/one shared vertices are independent, two shared vertices are compatible in precisely the cyclic-adjacency fraction \(2/(\ell-1)\), and three shared vertices force a contradiction. These mutually exclusive types exhaust all vertex intersections for a triangle. Their known counts yield the exact covariance, and a positive prefactor times an affine factor yields the unique sign threshold.

Execute `python3 verify.py` from the extracted package directory. It performs exhaustive finite independent-edge graph enumeration (selected orders through six vertices, several rational probabilities), compatibility checks for all representative intersecting motif pairs, and rational sign and monotonicity checks for a grid of \(n,\ell\). Expected line: `PASS: 6063 exact checks`. These finite checks are **not** proof for arbitrary order; the written overlap argument is.

Scientific boundaries: simple labeled \(G(n,p)\), \(n\ge\ell\ge4\), \(0<p<1\); counts distinguish unlabeled induced cycle edge sets, not orientations or embeddings. The fixed-edge-count random graph, higher moments, nonlinear association, and growing-\(\ell\) asymptotics are not established. General historical covariance formulas might cover or imply portions of the result; independent literature audit has not been performed.
