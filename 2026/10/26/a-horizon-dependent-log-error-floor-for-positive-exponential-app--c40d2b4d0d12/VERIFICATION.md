---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Positive normalized mixtures satisfy log g(0)=0 and (log g)''=Var_t(lambda)>=0. For c=π/(4b²), F(T/2)>=−cT²/4−E and convexity gives F(T/2)<=F(T)/2<=−cT²/2+E/2, hence E>=cT²/6=πT²/(24b²). Any log-distortion with |ln ratio|>=delta forces some relative error >=1−exp(−delta), proving the corollary. Holds for all m, positive weights, nonnegative rates and T,b>0; no finite sampling is involved.

## originality

PASS

For the specific atmospheric memory kernel exp(-πt²/(4b²)), the supplied explicit term-independent uniform log-error obstruction for normalized positive mixtures is not stated in the inspected source model or in retrieved Gaussian cosine-sum work, which permits oscillatory/signed terms and a different norm. The derivation is short from classical log-convexity, so novelty is qualified: priority of this particular specialization of a general convex approximation inequality is not established. Full-text inspection of Loy–Anderssen (2020) now confirms that the qualitative nonapproximation of non-CM Gaussian targets already follows from closedness of CM; the assessed new component is only this explicit finite-horizon quantitative log/relative bound.

## value

PASS

Although the inequality follows from a short elementary log-convexity argument, it is motivated by a specific Gaussian survival kernel used in an actual atmospheric memory integral and gives a parameter-explicit, horizon-dependent, term-count-independent obstruction to a natural positive parallel-exponential Markovian reduction. Such a no-go bound can decisively reject uniform relative-fidelity targets before fitting and is more than a normalization/type check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
