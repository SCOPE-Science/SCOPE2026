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

Run `python3 verify_cup_spiders.py` with Python 3. The verifier computes all pairwise graph distances by BFS from the actual spider edge list. It generates four orbit-representative target sequences on \(S(1,2^b)\) for all \(b=2,\ldots,120\), then checks every source has exactly the distance-many cups, each destination is occupied, no target is emptied, and exactly \(|V|-1\) moves produce one final stack.

The finite checker also uses an independent memoized exhaustive reachability search with no target-origin moves to reject the inner long-arm targets in the nine cases \((a,b)=(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2),(4,3),(5,2)\). Exhaustive search includes all legal moves involving other vertices (excluding moving cups away from the target, which cannot occur in any successful stacking sequence). The observed result was `VERIFY_OK 476 constructive cases, 9 exhaustive obstruction cases`.

These computations are finite. The theorem for unbounded \(a,b\) requires the obstruction argument and the explicit parity-dependent construction proved in RESULT.md. They have not been independently validated.
