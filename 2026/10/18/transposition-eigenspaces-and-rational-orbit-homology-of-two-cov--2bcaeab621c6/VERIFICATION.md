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

# Reproducibility checks

Run `python3 verify.py` from the extracted package directory, using the Python standard library. The reported output in `verify_output.txt` is the actual result of this invocation. The checker constructs the two-cover condition for every nonempty outside graph for \(2\le n\le6\), verifies each individual local alternating weight against the five-type structural classification, and independently enumerates every union of transposition edge-orbits for \(4\le m\le7\). It then compares direct signed Lefschetz totals with \(\binom{m-1}{3}\), computes the implied homology traces and involution-invariant Betti ranks, and verifies the polynomial-binomial equality for \(4\le m\le100\).

## Mathematical boundaries

Finite enumeration certifies only the enumerated parameters. The proof in `RESULT.md`, particularly the exhaustive two-hub cover classification, gives the all-parameter conclusion. The independent premises for homology concentration and the degree-four representation are identified under References. No independent audit has been performed and no claim is made for the full degree-three symmetric-group character or for integral quotient torsion.
