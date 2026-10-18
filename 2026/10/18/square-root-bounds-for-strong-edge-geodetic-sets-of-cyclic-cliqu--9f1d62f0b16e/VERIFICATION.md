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

The theorem is mathematically justified by the lower-bound capacity argument and the balanced cyclic-anchor construction in `RESULT.md`. The file `verify.py` is a standalone Python 3 standard-library checker. Run `python3 verify.py`; the complete expected stdout is in `verify_output.txt`.

The checker constructs \(260\) general-bound witnesses for graphs \(C_n\square K_m\), for \(n\) from 3 through 80 with additional larger orders up to 300 and \(m\in\{2,3,4\}\) for tested small orders. It checks that selected vertices are actual anchors, exactly one geodesic is selected per unordered endpoint pair, each step is an existing graph edge, every geodesic has the exact graph distance, and every graph edge is covered. All \(81,327\) tested general-bound graph edges are accounted for. A separate routine validates all \(54\) sharp square-cycle witnesses for \(3\le k\le20\) and \(m\in\{2,3,4\}\), accounting for another \(54,435\) graph edges. It checks exact selected-set size \(mk\), full clique and rim edge coverage, unique endpoint pairs and geodesic lengths, and the checker also tests \(234,952\) cyclic intervals for the anchor-count property. The witness generator deterministically chooses the first unused eligible endpoint pair for each clique rung.

Finite tests do **not** prove the theorem at all orders, nor certify novelty or establish the true sharp constant. The symbolic proof applies to every \(n\ge3\), \(m\ge2\), including the exact square-order specialization for every \(k\ge3\). External independent audit has not been performed.
