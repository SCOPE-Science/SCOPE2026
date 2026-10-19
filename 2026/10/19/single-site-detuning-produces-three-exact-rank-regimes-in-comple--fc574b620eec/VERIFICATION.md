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

# Reproduction and limits

The attached `verify.py` runs with Python 3 and SymPy (`python verify.py`). It constructs exact rational Hamiltonians for every \(2\le a,b\le6\) and each \(\tau\in\{0,\frac12,-2,3\}\), totaling 100 parameter profiles.

It does **not** reuse the proof's spectral quotient. Instead, it calculates the dimension of the image of vertex-diagonal matrices under orthogonal projection to the symmetric commutant. It forms the span of symmetric commutators \(HK-KH\) for all elementary skew matrices \(K\), then uses exact matrix ranks to find
\[
\operatorname{rank}\widehat M=\operatorname{rank}[C\;D]-\operatorname{rank}C,
\]
where \(D\) denotes the matrix of diagonal basis columns. This equals the full average-mixing rank because the kernel of the projected diagonal subspace is the spectral-compression kernel for all eigenspaces. For each case the result is compared to the proposed exact formula.

Executed successfully on the supplied standalone script: `VERIFY_OK exact_commutant_cases= 100` (the script also prints elapsed time). All cases passed, including both signs and the zero boundary. These are **finite** exact-arithmetic corroborations; the unrestricted parameter statement is proved separately in RESULT.md. No independent audit or formal certification was performed.
