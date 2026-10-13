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

# Reproducibility and limits

Run `python3 verify.py` with a Python 3 installation; the script uses only the standard library. It checks the seven finite strict inequalities establishing tail overlap for primes \(5,7,11,13,17,19,23\), all nine two-prime multipliers, the Archimedean rational comparisons needed for the two gaps and every overlap, and the conditional density weights. Expected output begins `EXACT_CERTIFICATE_OK` and reports `components=3` with `conditional_weights=36/91,16/91,39/91`.

The code also enumerates the cube-free integers up to \(100000\) solely as an illustration. Such enumeration neither proves that infinitely many prime-tail options fill an interval nor establishes an asymptotic density. The unrestricted parts of the mathematical argument require Nagura's prime-interval bound, Euler products, a three-option greedy interval-covering lemma, and the standard cube-free density via Möbius inversion, each explained in `RESULT.md`. No external proof assistant, independent mathematical review, or separate certification is claimed.
