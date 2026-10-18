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

# Finite and formal verification

The standalone `verify.py` uses integer coefficients throughout. It constructs powers of \(A(q)=\prod_{j\ge1}(1-q^j)\) via exact logarithmic derivatives and the reciprocal Euler product via unrestricted integer partitions. For smaller cases it also multiplies the factors directly, independently of the logarithmic derivative algorithm.

Prime-power checks cover \(t=2,4,8,3,9,5,25,7\), and check all displayed finite coefficients modulo the asserted optimal prime power. At the index \(p^{a-1}\), the checked residue is \(-p^{a+1}\) modulo \(p^{a+2}\), and every earlier coefficient is zero modulo \(p^{a+2}\). Non-prime-power checks cover \(t=6,10,12,15,18,20,21,30\), comparing the first nonzero residue modulo every divisor prime at index \(p^{2a}\).

Execute `python3 verify.py`; the successful result ends in `VERIFY_OK`. A finite run cannot prove infinitely many parameter choices. The formal Frobenius lifting and characteristic-prime coefficient arguments in `RESULT.md` provide the universal proof. The literature comparison is not an independent audit.
