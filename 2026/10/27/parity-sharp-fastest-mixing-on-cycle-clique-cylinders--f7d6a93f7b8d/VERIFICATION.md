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

# Reproduction and checks

Run `python3 verify.py` in a Python environment with NumPy and SciPy installed, for example after `python3 -m pip install -r requirements.txt`.

An execution of the standalone script returned:

```
VERIFY_OK LP_cases 220 dense_eigensystems 60 asymptotic_checks 40 odd_m2_ratio_to_6 5.999881803635598
```

The script checks the two analytic candidate bounds and their feasible weights over 220 pairs \((n,m)\) with \(3\le n\le22\) and \(2\le m\le12\), then solves a corresponding independent linear program. It independently forms full transition matrices and diagonalizes them in 60 pairs, including the extreme signed mode. It also stress-tests the parity cutoff, the fixed-fiber asymptotic heuristic ratio for 40 larger-order instances, and the odd two-layer prism ratio approaching \(6\).

The mathematical proof covers every allowed \(n,m\) and does not rely on finite enumeration, floating-point precision, or an external certification process. As a particular exact consistency example, for \((n,m)=(3,7)\) the theorem gives \(\Gamma=21/32\), cycle edge probability \(7/32\), clique edge probability \(3/32\), zero holding, and optimal SLEM \(11/32\).
