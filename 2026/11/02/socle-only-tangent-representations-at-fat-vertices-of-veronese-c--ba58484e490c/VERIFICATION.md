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

# Reproducibility and scope

Run `python verify.py` with Python 3 and no third-party dependencies. The independent checker enumerates monomial binomial syzygy equalities with all possible homogeneous multipliers and calculates the resulting kernel's dimension by disjoint-set linear algebra. It prints per-parameter dimensions and finishes with `VERIFY_OK: 30 Veronese-cone pairs, monomial syzygy constraints checked`.

Tested range: \(1\le d\le6\) and \(1\le r\le5\), totaling thirty parameter pairs. In every case, all target-degree components below \(r-1\) vanish and the degree-\((r-1)\) component has dimension \((dr+1)(d(r-1)+1)\). The general result follows from the cancellation/divisibility proof in `RESULT.md`; a finite calculation alone would not prove it.

The smooth comparison value \(2N\) for \(d=2\) is justified by the established dimension theorem for the reduced Hilbert scheme of a Kleinian surface. The computation does not verify the full local Hilbert-scheme equations, obstructions, or historical originality. Independent audit has not been performed.
