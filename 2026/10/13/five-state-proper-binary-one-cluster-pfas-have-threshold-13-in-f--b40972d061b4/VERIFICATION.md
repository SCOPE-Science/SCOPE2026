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
# Verification

Run `python3 verify.py` beside `verify.cpp` and `certificate.json`.

The verifier first regenerates all \(6^5=7776\) partial maps for one letter and checks the functional digraph of every total map, obtaining exactly \(1569\) one-cluster maps. It then exhausts every proper ordered binary PFA having at least one such letter, for \(14{,}594{,}838\) candidates.

For every candidate, a forward breadth-first search starts at the full state set and a separately implemented reverse multi-source breadth-first search starts at the five singleton subsets. Defined subset transitions are generated directly from the partial state maps. The two distances must agree for every candidate.

The verified carefully synchronizing histogram has maximum \(13\), with \(1200\) labeled extremizers. Each extremizer is canonicalized under all \(5!\) state relabelings and both letter orders; exactly five canonical representatives occur, each with orbit size \(240\).

The computation is exhaustive only for five states and two letters. Independent audit has not been performed.
