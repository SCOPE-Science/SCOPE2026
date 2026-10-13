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

The proof has two independent components.

First, for every \(r\)-dimensional coefficient subspace \(U\), the simplex block has exactly \(2^m-2^{m-r}\) supported coordinates because the unsupported columns are precisely the nonzero vectors of \(U^\perp\). The two appended blocks are repetitions of the two column vectors \(e_1+e_2\) and \(e_1\); therefore their support contributions are determined exactly by whether \(U\) lies in the kernels of the corresponding linear functionals. Counting \(r\)-subspaces in two distinct hyperplanes and their intersection gives the four multiplicities in RESULT.md. This is an exact finite-dimensional proof for every admissible parameter, not an extrapolation from experiments.

Second, `verify.py` independently reconstructs the generator columns, enumerates every subspace of \(\mathbb F_2^m\), computes support unions directly, and checks both the spectrum formula and generalized Hamming weights for \((m,n',n'')=(3,6,2)\) and \((4,10,4)\). Its exact output is stored in `verification_output.txt` and ends with `VERIFY_OK`. The one-dimensional spectra are \(\{4:1,6:2,8:2,10:2\}\) and \(\{8:3,12:4,14:4,18:4\}\), matching the published Examples 6.7 and 6.8.

The computation is a finite verification of representative instances. The general theorem rests on the hyperplane-counting proof; the finite replay is not used as a proof for unbounded \(m\).
