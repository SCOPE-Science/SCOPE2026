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

# Verification of the Kac-ring revival law

Run the included `verify.py` with Python 3 using `python3 verify.py` in the directory containing this file. No third-party packages are required. The deterministic exact stage enumerates every one of the \(2^N\) flipper configurations for each \(4\le N\le12\), for all \(1\le k\le\lfloor N/2\rfloor\), weighted by independent Bernoulli probability \(p=0.3\). It verifies both \(\mathbb E[A_{N,k}]=q^k\) and the exact variance identity, including wraparound boundary cases.

The second stage uses a fixed seed and 500 independent samples with \(N=6000\), \(p=0.25\), and \(k=6\), computing the fully signed magnetization \(E_N A_{N,k}\). Its second moment is compared against the mixture limit \(\sigma_q^2+Nq^{2k}\), with a coarse sampling tolerance; a separate signed-mean check verifies parity cancellation. Output from an execution of the packaged script:

```
EXACT finite-state means/variances pass N=4..12, every k<=N/2
MC signed magnetization moments 6000 6 3.019 3.132 passed; signed mean -0.06
```

Finite enumeration and Monte Carlo do not certify convergence for infinite \(N\), asymptotic independence, or originality. Those conclusions depend respectively on the block central limit argument, the parity-weighted characteristic-function estimate, and bibliographic comparisons in the scientific proof and review. Independent external audit has not been performed.
