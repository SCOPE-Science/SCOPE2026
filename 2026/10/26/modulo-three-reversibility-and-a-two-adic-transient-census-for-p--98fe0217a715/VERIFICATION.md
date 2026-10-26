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

# Verification of circular-prism parity dynamics

The embedded `prism_xor_check.py` is standalone Python 3, using only the standard library. Run `python3 prism_xor_check.py` in the directory containing this file. Its saved output is in `verification_output.txt`.

The program builds the \(2n\times2n\) open-neighbour adjacency matrix with three distinct neighbours for every \(n\ge3\), computes matrix ranks of iterates and periodic-point equations by binary elimination, and independently computes the proposed polynomial-gcd exponents. It checks 726 rank identities for circumferences 3 through 24 and iterates up to 20 (plus nullity ranks for transient times). It also enumerates all labelled configurations for circumferences 3 through 8 and computes each actual first periodic entry time by detecting orbit repetition, checking all 87,360 states and their predicted exact distributions.

The program is independent evidence for bounded sizes; the all-size proof is the triangular Laurent-polynomial reduction and primary-factor argument in `RESULT.md`. No code experiment proves the infinite assertion by itself. Exact primitive-cycle formulas require polynomial gcd computations in \(\mathbb F_2[z]\) for the chosen period. No external independent audit has been carried out.
