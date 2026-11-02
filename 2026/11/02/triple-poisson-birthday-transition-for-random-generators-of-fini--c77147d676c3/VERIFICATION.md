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

# Verification and reproducibility

The standalone Python 3 standard-library script `verify.py` independently constructs multiplication in several finite local rings, enumerates all ordered generating tuples in stated cases, computes linear-span closure under products, and compares the resulting counts with the exact product identity used in the proof. Execute with `python3 verify.py`. The tested examples include the residue fields \(\mathbb F_2\) and \(\mathbb F_4\), cotangent dimensions one and two, direct powers of up to four local factors, \(\mathbb F_2[x]/(x^3)\), and two nonisomorphic local factors of cotangent dimensions one and two. The output ends in `VERIFY_OK` when all checks pass.

The verifier checks algebra generation by direct multiplication rather than by assuming the residue/Frobenius orbit or cotangent criterion. Its expected-count routine is used only to compare enumeration results. The finite tests do not establish the general exact formula or the Poisson limits. The proof in `RESULT.md` gives the uniform finite-algebra reduction, the subfield and rank-defect asymptotics, collision factorial moments, asymptotic independence, and the boundary cases.

For the first triple-critical case \(f=k=d=2\), \(r=\lfloor c q^2\rfloor\), evaluate the finite formula logarithmically using \(T_{q,2,2}=q^4-q^2\) and the local full-rank factor \((1-q^{-2})(1-q^{-4})\). At \(c=1\), the sequence for \(q=5,11,41,101\) approaches \(e^{-3}\); these numerical checks illustrate but do not prove the limit.

No independent mathematical audit has been performed, and full publication-priority certification is not claimed.
