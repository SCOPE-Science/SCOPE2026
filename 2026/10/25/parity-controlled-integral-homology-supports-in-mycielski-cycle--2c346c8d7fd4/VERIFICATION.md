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

The full proof works over \(\mathbb Z\) for every integer \(n\ge5\). Its certificate is a constructive decomposition of the original complex and each one-vertex deletion, together with integral Mayer–Vietoris naturality. The crucial nonstandard step is a unit-degree map from the parity component of the apex link to the spoke circle after deleting a shadow vertex. This is checked by following its two spokes once while every other edge maps into the surviving shadow simplex.

Run `python3 verify_myc_support.py` with the Python standard library. This independently regenerates simplices from the graph, checks reduced mod-two Betti numbers of complete complexes and all single-vertex deletions for \(5\le n\le11\), and exhaustively checks inclusion-induced degree-two image ranks over \(\mathbb F_2\) for every induced subset at \(n=5\) and \(n=6\). The expected last line is `VERIFY_OK_MYC_CYCLE_SUPPORT_PARITY`. As always, finitely many characteristic-two checks do not prove an all-\(n\) integer statement; that proof is in `RESULT.md`.

Independent audit has not been performed.
