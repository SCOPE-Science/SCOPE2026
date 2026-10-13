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
The standalone program `artifacts/verify.py` reconstructs the full ternary multiplication \([e_2,e_3,e_4]=e_1\), the cyclic relative Rota–Baxter identity of nonzero weight, and its four independent basis-triple defects. It symbolically establishes that every block matrix preserving \(Ke_1\) satisfies the identity exactly when
\[
\det A=a(\sigma_2(A)+\lambda).
\]
It also computes the transverse defect for unrestricted matrices, independently checks the quadratic-form Gram determinant \(-1/256\), and replays a zero-weight non-derived-preserving example.

For \(\mathbf F_2\) the program exhaustively evaluates all \(2^{16}=65536\) endomorphisms, finding **4736** weight-one operators, all preserving the derived line. For \(\mathbf F_3\) and \(\mathbf F_5\), it enumerates all \(q^9\) quotient matrices and independently verifies their quadratic and singular fibers for every nonzero weight. The exact operator totals are **579555** and **583929** for the two weights over \(\mathbf F_3\), and **253359375** (square weight) versus **253515625** (nonsquare weight) over \(\mathbf F_5\). It also enumerates all \(4^9\) quotient matrices over \(\mathbf F_4\), obtaining **17743872** operators for each nonzero weight.

The program's output is embedded in `artifacts/verify_output.txt` and terminates with `VERIFY_OK`. The arbitrary-field result, finite-field point counts for all prime powers, geometric integrality, and zeta-function formulas are established by the written proof; the enumerations are finite replay checks and not substitutes for those proofs.
