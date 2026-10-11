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

# Reproduction and verification

Extract both `evidence/verify_four_cut.py` and `evidence/four_cut_certificate.json` into a common `evidence` directory. With Python 3.9 or later, run `python3 evidence/verify_four_cut.py` from the containing directory. No external libraries, network calls or third-party files are required.

The verifier enumerates every four-vertex subset of the triangular graph, checks disconnectedness using breadth-first graph search, and matches it to the ten triangle-plus-complement-edge patterns. It regenerates the full complex, its complete integer-labeled pairing certificate and both critical-face sets. It explicitly builds the entire directed Hasse graph and topologically sorts all 370 nodes; 1320 arrows are considered. It also independently computes the simplicial boundary ranks over \(\mathbb F_2\), with ranks by face size zero through six of `(0,1,9,36,74,50,10)` and reduced Betti vector `(0,0,0,11,0,0)`.

For each of all 120 permutations of the five underlying labels, the code sums the signed traces of fixed oriented faces and uses the Lefschetz formula, which is valid because the exact discrete-Morse argument proves integral homology concentration. It independently computes all seven rational Specht characters by the Frobenius alternant coefficient formula, then checks their character inner products and confirms the three irreducible summands with multiplicity one.

The finite DAG and complete matching prove the homotopy classification; the mod-two calculation is a consistency check and not by itself an integral proof. All exhaustive arguments concern this fixed ten-vertex complex. Neither the full integral group-action lattice nor a generalization to larger triangular graphs was verified. Independent external audit remains unperformed.
