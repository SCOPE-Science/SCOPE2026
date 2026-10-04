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
At \(\mathcal R_0=1\), the critical relation is
\[
\beta\gamma_E\gamma_L\gamma_N=\alpha_1\alpha_2\alpha_3\mu_A.
\]
The proof uses two exact identities. First, the Lyapunov derivative is
\[
\dot V=-\frac{\mu_AA(A+N+L)}{K+A+N+L}.
\]
Second, with the normalized zero-eigenvector coordinate \(z=p^Tx\),
\[
\dot z=-\frac{A(A+N+L)}{H(K+A+N+L)}.
\]
Together with the stable spectral complement, the second identity gives the quadratic coefficient
\[
\kappa=\frac{C}{KH},
\]
and hence \(z(t)\sim 1/(\kappa t)\).

The standalone script `verification/verifier.py` uses exact rational arithmetic. It verifies the threshold relation, the right and left null-vector identities for the critical Jacobian, \(\ell^Tr=\beta H\), the formulas for \(C\), \(\kappa\), and \(Q\), and the witness
\[
\alpha_1=\alpha_2=\alpha_3=2,\quad
\gamma_E=\gamma_L=\gamma_N=\mu_A=1,\quad
K=10,\quad\beta=8.
\]
For this witness it confirms \(r=(4,2,1,1)^T\), \(H=5/2\), \(C=4\), \(\kappa=4/25\), and \(Q=25/4\). The replay command is `python3 verification/verifier.py`; the expected output is `VERIFY_OK`.

The script checks algebraic consistency only. It does not certify the infinite-time theorem by sampling. The proof of global convergence is the Lyapunov-LaSalle argument in `RESULT.md`, and the proof of the sharp rate is the stable-subspace asymptotic argument there. Controlled dynamics, model perturbations, and finite-time eradication are outside the verified claim.
