---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Rescaling by extinction gives (n-k)(u+kv) and k as the count-chain rates; balanced adjacent fluxes give binomial multiplicity times the rising product of u+jv. For v>0 the tilted Gamma representation is normalized since its (1+vT)^n moment is the partition function. Conditional on its latent success probability the sites are independent, so their covariance is the variance of a strictly increasing function of a nondegenerate random variable. At v=0 sites are independent. For two sites the rational Pearson formula has positive derivative (1+u+v)^(-2) and a nonzero limit. The exact three-site quotient gives the stated quartic derivative numerator: in ascending powers the signs are +,+,arbitrary,-,-, so exactly one positive root exists and is simple, with positive derivative before it and negative after. The derivative of the three-site marginal is strictly positive. For n>=3 the one-vacancy weight relative to full occupancy is asymptotic to n/((n-1)v); at least two vacancies have total relative weight O(v^(-2)). Thus one-site vacancy has probability asymptotic to 1/((n-1)v), two-site vacancy is O(v^(-2)), and the normalized pair correlation tends to zero. Positivity, continuity and the two zero endpoints force an interior maximum; the argument does not count maxima for n>=4.

## originality

PASS

The count law, associated moments and raw covariance values are available from earlier exact work, and a bell-shaped raw covariance was already reported in the same complete-graph family. The frozen claim credits the count law and does not claim generic association as novel. Its distinct contribution is the global normalized Pearson shape theorem: the sharp minimum of three patches, unique global peak at three for every u>0, and the zero-limit/nonmonotonicity result for every fixed finite n>=3. The inspected covariance shape does not imply that conclusion; at n=2 raw covariance actually peaks while Pearson rises strictly.

## value

PASS

Whether stronger neighbor colonization synchronizes occupied patches is a natural question about a standard finite occupancy model. The exact opposite two-versus-three-patch behavior and the three-patch unique peak give a sharp benchmark for normalized synchrony; rising marginal occupancy and a peak in raw covariance cannot answer that question. Positivity with a vanishing high-colonization limit extends the phenomenon to every fixed larger patch count, so it is not just an isolated parameter example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
