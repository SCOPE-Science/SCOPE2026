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

# Verification of the Heisenberg Rota–Baxter census

Run \(\texttt{python3 verify.py}\). No third-party dependencies are required. The script uses exact arithmetic over prime fields and explicitly implemented binary extension field \(\mathbb F_4\).

It computes the explicitly defined sign convention for weight-\(\lambda\) Lie Rota–Baxter equations directly, independently of the reduced symplectic criterion. It exhausts all \(q^9\) general linear operators on the three-dimensional algebra for \(q=2,3\) and every weight, and for weights zero and one at \(q=4\). These are preexisting low-dimensional cases used only as verification baselines, not the new priority claim.

In the five-dimensional binary case, all \(2^{16}\) possible matrices \(A\) are checked for each scalar fiber using the symplectic criterion and stratified by the rank of \(A-cI\), yielding \((1,225,3150)\) in both singular scalar fibers when weight one, and \(720\) symplectic matrices for the weight-zero nonsingular fiber. The full operator totals (incorporating \(2^4\) free central functionals) are \(65{,}536\) at zero weight and \(108{,}032\) at weight one. Randomized direct-versus-reduced identities cover dimensions five and seven and different finite fields. Further integer counts cross-check parameter products. The checker ends with `ALL_HEISENBERG_RB_CHECKS_PASSED` when all assertions hold.

**Boundaries:** finite exact tests do not prove any universal claim for arbitrarily high dimension or field size. The written proof supplies this. Random tests are not exhaustive. None of these checks constitutes independent audit or historical originality certification.
