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

The analytic proof reconstructs the exact one-excitation action of the four-site periodic Heisenberg Hamiltonian and derives the complete formula
\[
Q=\frac34-\bigl[\operatorname{Re}(a\overline b)\bigr]^2
\]
on the zero-energy subspace spanned by the two opposite-momentum states. The derivation uses only orthogonality, fixed-excitation reduced states, and the average-purity identity for the Meyer–Wallach measure.

`verify_counterexample.py` independently checks the endpoint witnesses with exact standard-library arithmetic. It confirms that the two momentum vectors and their real standing-wave sum are zero-energy eigenvectors, that the source plane-wave value is \(3/4\), and that the standing wave has \(Q=1/2\). The captured output is stored in `verification_output.txt`.

The checker verifies endpoint witnesses only; the continuous range is established by the proof, not by finite sampling. No claim is made for other excitation sectors, other energy eigenspaces, or other chain lengths.
