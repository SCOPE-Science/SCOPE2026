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

# Proof and reproducibility checks

The critical algebraic cancellation is exact: for \(p=\sigma/d_2\), \(k=d_1-p\tau>0\) and \(G'=a_1+p a_2\), logarithmic differentiation of \(xy^pe^{-G}\) eliminates both forcing functions and the resident-dependent cross term. The remaining drift is \(-kx\), so \((1/W)'=k e^G y^{-p}>0\). Positivity/finite bounds, the logistic comparison, and the scalar convolution estimates are proved directly in `RESULT.md`. They are not certified by the numerical tests.

Run `python3 check.py` using Python 3.8+ with the standard library. The checker verifies the cancellation coefficients as exact rational numbers; constructs the logistic resident orbit and the predicted positive periodic correction; checks the exact averaged coefficient \(1/k\) by quadrature; and integrates two very different positive initial states through 320 forcing periods. The numerical outputs are finite-horizon convergence diagnostics, not proofs for infinite time or priority. A representative execution returned \(k=1.7066666666666668\), \(\langle f\rangle=0.5859375\), predicted phase values \(f=0.2799365956972193\) and \(Z=0.13018741038964696\); computed \(tx=0.2799471319941986\), \(t(y-Y)=0.1302166007123871\) for one initial state, with the other trajectory approaching the same profiles.

The mathematical conclusion is confined to the stated positive initial data, periodic continuous growth rates, constant cooperative couplings with \(d_1d_2>\sigma\tau\), and the exact zero-mean invasion boundary. No independent audit, formal proof certification, exhaustive search, or backward-attractor classification has been performed.
