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

# Reproducibility and verification

Run `python3 verify_pattern.py` with the Python 3 standard library. The expected result is `VERIFY_OK: 17861 independent finite exact assertions`. The program computes samples by independent direct enumeration and compares them with the cyclic-phase decomposition, including non-maximizing windows. It exhausts binary marker templates of period up to six and one-defect residue supports of periods three through eleven; it constructs explicit attaining finite windows for the latter family.

The base mechanical test word has rational slope \(98/257\) and period \(257\). This ensures that direct enumeration terminates and that every inspected pattern is an exact finite object. It is not an irrational Sturmian word and does not justify the full infinite theorem by extrapolation. The universal result is established by the phase-disjointness and recurrence argument in the accompanying proof and the exact cyclic-run combinatorics.

Scientific scope is limited to one uniformly recurrent binary pattern Sturmian residue interleaved with letters from a disjoint, constant periodic marker template. The independent audit has not been performed.
