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

# Reproducible verification

Run `python3 verifier.py` with a standard Python 3 installation, in the directory containing `verifier.py`. The output is recorded verbatim in `verification_output.txt`. No third-party Python modules or external data files are required.

The program constructs \(GP(n,2)\) directly from its defining edges and reconstructs the exact distance-two graph. For every \(13\le n\le40\), it independently checks all possible pairs against the symbolic square adjacency formula and checks every step of all five closed-neighborhood fold sequences. Across this range there are exactly \(742\) inner-vertex links. This is corroboration of, not a substitute for, the universal offset-based proof in `RESULT.md`.

For the exceptional \(n=12\) graph, the program enumerates maximal cliques, takes all their subsets, forms every mod-two boundary matrix (including the reduced augmentation), and computes ranks by exact binary Gaussian elimination. It returns face vector \((24,108,160,84,12)\), boundary ranks \((1,23,85,72,12)\), and reduced Betti vector \((0,0,3,0,0)\). All assertions must succeed before `VERIFY_OK` is printed.

Limitations: finite replay cannot establish the all-parameter claim without the separate symbolic proof; no integral Smith normal form is calculated at \(n=12\). No independent audit has been performed.
