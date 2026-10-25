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
# Verification record

The theorem concerns the inclusive unordered symmetrized \(\ell^1\)–Rips simplicial complex, not the ordered simplicial set.

## Exact mathematical checks
The minimum Hamiltonian path weight counts unavoidable same-part adjacencies, with equality from a maximally alternating ordering. The weight inequalities imply the two literal filtered-complex identities. Top homology of joins of simplex skeleta is torsion-free. The image of the top integral boundary has precisely the claimed rank in each even stage, and the CW connectivity argument upgrades this to a sphere-wedge homotopy type. Inclusion homomorphisms vanish because the reduced homology of consecutive integer stages lives in distinct dimensions.

## Reproducibility
Run `python3 verification/verify_bipartite.py` (only the Python standard library is needed). The code independently enumerates every Hamiltonian ordering on subsets from nine small complete bipartite graphs to test 187 weights; then independently builds all admissible simplices and computes binary boundary ranks for 92 integer stages with both part sizes at most four. The observed result was `PASS: exhaustive path weights 187 and independent binary homology stages 92`. The finite checks are not a proof of the all-parameter theorem and do not test integral torsion. Integral claims instead rest on the explicit free-chain and CW-homotopy proof in RESULT.md.

## Boundaries and integrity
All binomial expressions use zero outside the natural range. For zero sphere multiplicity, the complex is contractible. Reduced degree-zero homology is used at the initial scale. The computation does not establish novelty, independent validation, or results for arbitrary bipartite graphs, \(p\ne1\), or the ordered simplicial set. No independent audit has been performed.
