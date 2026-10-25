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

# Verification instructions and limits

Run `python3 verify.py` with Python 3.8 or newer and no extra packages. The computation constructs 216 ordered triple vertices, checks 16,416 edges from integer congruences, and exhaustively enumerates all maximal cliques using an invariant-preserving Bron--Kerbosch search. The exact five-size histogram is the theorem's finite certificate, and the terminal search condition ensures maximality. Recorded output is embedded as `verification_output.txt`.

An optional independent replay, `python3 crosscheck.py`, requires `networkx==3.6.1` and produces `crosscheck_output.txt`. It constructs the edge relation afresh and uses a separately maintained maximal-clique iterator. The two resulting histograms agreed exactly, including 248,264 reported maximal cliques.

Neither enumeration is intended as an infinite-dimensional proof. Only within the 216-vertex problem does exhaustive search establish all cases. No external independent scientific audit is asserted.
