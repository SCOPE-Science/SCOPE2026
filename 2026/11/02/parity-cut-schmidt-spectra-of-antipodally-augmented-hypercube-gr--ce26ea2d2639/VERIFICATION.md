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

# Reproduction and scope

Run `python3 verify.py` with Python 3 and NumPy installed. The checker reconstructs the complete antipodally augmented hypercube adjacency and the coordinate-parity cut for each tested \(n\) and \(S\); it does not read any cached adjacency or spectrum data. Integer bitset pivot reduction is performed over \(\mathbb F_2\). Every nonempty subset for dimensions three through nine and every subset size for dimensions ten and eleven are checked; `verification_output.txt` is the recorded output of an actual invocation.

The last six tests construct the full pure graph-state amplitudes via the controlled-\(Z\) phase rule and trace out the opposite set of qubits numerically. They compare the count and values of the nonzero spectrum, not only the entropy; their greatest reported floating-point deviations are below \(1.1	imes10^{-16}\). This independent construction is finite corroboration and does not replace the all-dimensional ring-algebra proof in `RESULT.md`.

The proof identifies two key facts not certified by enumeration: (1) any characteristic-two group-algebra element with nonzero linear part is conjugate under a ring automorphism to a coordinate nilpotent, hence has rank half the group algebra dimension; (2) the exceptional odd full parity operator is conjugate to a tensor-sum differential with exactly \(2^m\) homology dimensions. The mathematical review is self-review; independent audit has not been performed.
