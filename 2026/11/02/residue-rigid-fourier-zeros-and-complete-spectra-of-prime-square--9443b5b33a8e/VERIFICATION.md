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

# Reproducible arithmetic checks

Run `python3 verify.py` from this package (standard Python 3, no third-party dependencies). The checker constructs each graph directly from the proposed digit function. It detects exact zeros by divisibility of a nonnegative-coefficient mask polynomial by \(\Phi_{p^2}\): within every fixed residue modulo \(p\), the \(p\) coefficient counts must be equal. No approximate complex arithmetic or numerical tolerances are involved.

The checker exhaustively compares the proposed zero criterion for all \(81\) Fourier labels for each of the \(27\) functions \(h\) at \(p=3\), and for all \(625\), respectively \(2401\), labels for three functions at \(p=5\), respectively \(7\). For each tested graph it constructs three complete spectra with different residue and high-digit assignments and checks every frequency-pair orthogonality exactly. It also independently enumerates all \(64\) possible four-element spectra at \(p=2\) as a **boundary check only**, and all affine spectra at \(p=3\) and \(5\), obtaining \(54\) and \(500\). Successful output ends with `AFFINE_SPECTRA_ENUMERATION_OK 5 500`.

The infinite theorem and counts for arbitrary \(p,h\) are established by the four algebraic proof steps in RESULT.md, not by finite enumeration. The boundary check at \(p=2\) is not presented as a new discovery. Neither historical priority nor independent mathematical verification is certified by the checker.
