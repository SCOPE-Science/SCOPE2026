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

# Exact finite cross-checks

Execute `python3 verify.py` with Python 3 and no external packages. The included `VERIFY_OUTPUT.txt` is its observed output.

For all coprime \(1\le p<q\le28\), all \(1\le k\le6\), and every \(1\le n\le q+\lfloor(kq-1)/p\rfloor+2\), the checker independently enumerates circular factors of the primitive mechanical period, computes images after relocating the first \(k\) ones, and compares the distinct-image count with the modular formula. An independently ordered rational-phase pass checks the complete factor set, interval-contiguity of image fibers and each eligible-edge count. It also tests eventual injectivity at all lengths from the stated threshold and noninjectivity at its immediately preceding length. The recorded run passed 49,750 parameter-iteration-length cases, with 769,053 phase-factor comparisons, 23,908 post-period injectivity checks, and 93,235 direct replays of the iterated operator.

The infinite result relies on the written prefix-dominance and edge-index proofs. Finite enumeration is corroborative, not logically sufficient for arbitrary parameters. Independent mathematical audit and publication-priority certification have not been performed.
