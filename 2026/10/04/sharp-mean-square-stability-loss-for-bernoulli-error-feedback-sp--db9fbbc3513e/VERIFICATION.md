---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Conditioning on transmit/drop branches gives the stated exact three-moment operator. Independent symbolic reconstruction gives \(\det(I-N)=p s[p s+2p-2s]\), so eigenvalue \(1\) appears precisely at \(s=2p/(2-p)\). The package supplies the remaining cubic Jury inequalities and a separate renewal proof for standard zero-residual initialization: geometric waiting time \(J\) yields cycle multiplier \(1-2s/p+(2-p)s^2/p^2\), which crosses one at the same threshold and is minimized at \(p/(2-p)\). The no-memory multiplier \(1-2ps+ps^2\) gives the comparison interval.

## originality

PASS

Fresh Resultary search found no Bernoulli error-feedback threshold. Classic sparsified-SGD/error-feedback sources cover random sparsification and memory but give convergence under scheduled or generic assumptions, not this constant-step scalar necessity-and-sufficiency law. The 2025 tight EF paper is the strongest overlap risk: its official repository contains a random-compressor certificate, which this run inspected directly. That certificate verifies a generic contractive-random-compressor Lyapunov rate with a prescribed stepsize; it does not state or derive the Bernoulli-specific full stability interval, geometric-cycle optimum, or memoryless \(0<s<2\) comparison.

## value

PASS

Random sparsification with residual memory is canonical, and the scalar model isolates a nontrivial geometric-delay overshoot mechanism. The exact stability loss relative to memoryless dropout and the exact cycle-optimal step give a sharp, interpretable communication/stability benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
