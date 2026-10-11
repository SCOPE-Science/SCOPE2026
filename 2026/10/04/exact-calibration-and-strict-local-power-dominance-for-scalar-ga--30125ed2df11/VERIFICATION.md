---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For scalars, direct substitution into the published two-way cross-fitted statistic gives \(\sqrt{m/(m-1)}\{\operatorname{sgn}(t_2)t_1+\operatorname{sgn}(t_1)t_2\}\), hence the signed sum of independent absolute Student variables under the null; sign/magnitude independence gives the exact one-sided cutoff. Under \(\mu_m=h/\sqrt m\), the two half-sample Student statistics converge to independent \(N(h,1)\) variables. The orthogonal transform to \(U,V\) yields the exact limiting rejection event and cutoff. The single-crossing comparison of conditional rejection functions was checked algebraically, and the folded-normal likelihood ratio \(e^{-h^2}\cosh(\sqrt2hr)\) is strictly increasing for every \(h\ne0\), making the integrated power gap strictly positive. Independent numerical quadrature reproduced the stated 5% cutoff and the example powers but is not used for the universal proof.

## originality

PASS

Kim--Ramdas define the exact two-way cross-fitted statistic and prove its fixed-dimensional non-Gaussian limiting behavior; their appendix explicitly describes calibration of multiple splits as difficult and says it is unknown in general whether such tests can be calibrated with provably higher power than a single split. Their scalar Gaussian material supplies the single-split benchmark, not the audited exact finite Student representation or strict dominance theorem for this two-way statistic. Guo--Shah later provide a general rank-transformed subsampling calibration for aggregated randomized tests, but analyze a different procedure and do not imply the exact finite law or the closed all-\(h\) dominance result here.

## value

PASS

The theorem resolves a concrete calibration and power question for the simplest nontrivial instance of a published cross-fitting construction. Exact finite-sample calibration removes a practical ambiguity in the scalar Gaussian case, and the strict local-power comparison for every nonzero local signal is a structural statement, not merely one numerical example. Its scope is deliberately narrow but mathematically motivated by the source's calibration discussion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
