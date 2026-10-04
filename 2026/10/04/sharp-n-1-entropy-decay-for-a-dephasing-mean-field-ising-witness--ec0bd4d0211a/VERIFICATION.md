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

The analytic verification has four steps. First, \(A^{m_t}=0\) because \(\operatorname{tr}(m_tZ)=0\). Second, the local \(Z\)-dephasing generators commute with the all-to-all \(ZZ\) Hamiltonian, giving the exact state \(U_N(t)m_t^{\otimes N}U_N(t)^\dagger\). Third, direct pair conjugation gives \(\langle X_i\rangle=r_t\cos(2Jt/N)^{N-1}\). Fourth, \(\log m_t=\alpha_tI+\operatorname{artanh}(r_t)X\) reduces the many-body relative entropy to that one-site expectation.

The bundled `verify.py` enumerates computational-basis phase differences for small \(N\), without matrix-exponential libraries, and checks them against the cosine-power formula. It also checks the exact relative-entropy expression and the two fixed-time asymptotic constants. Running `python3 verify.py` prints `VERIFY_OK`.

Finite enumeration does not prove the all-\(N\) statement. The proof is the commutation, conjugation, logarithm identity, and asymptotic expansion given in `RESULT.md`. The result is restricted to the stated qubit Ising interaction and local dephasing witness.
