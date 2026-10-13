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

The standard-library verifier `artifacts/verify.py` checks the exact decomposition
\[
\tau(\tau(ab))=(\omega(a)+\nu_2(\tau(b))+1)
\tau\left(\tau(b)/2^{\nu_2(\tau(b))}\right)
\]
for every \(1\le n=ab\le200000\), where \(a\) is the exponent-one squarefree component and \(b\) the powerful component. It independently confirms the divisor counts for the first 2000 integers, reconstructs powerful numbers in two ways through 100000, and evaluates a finite truncation of the constant series.

The full proof of the asymptotic is analytical. It requires the displayed fourth-moment concentration lemma and the uniform powerful-tail bound; neither is claimed to follow from the finite data. The numerical partial constant is not represented as a certified value for the infinite series. `artifacts/replay.txt` contains the actual verification output.
