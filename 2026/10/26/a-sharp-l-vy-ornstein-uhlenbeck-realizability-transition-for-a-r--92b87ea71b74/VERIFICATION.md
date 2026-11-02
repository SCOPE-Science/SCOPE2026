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

Fourier transforming both conditional Fokker–Planck equations yields F_−=αF_+/(α+q²) and F_+(q)=½e^(−q²/2)(1+q²/α)^(−α/2), giving the cited known marginal. The Frullani transform identity writes its log characteristic function with strictly nonnegative Lévy density ν(x)=[(1+α/2)e^(−√α|x|)−e^(−√(2α)|x|)]/|x|; integrability near zero and infinity establishes infinite divisibility. Splitting off e^(−q²/2)(1+q²/α)^(−α/2) leaves a positive finite Lévy measure with mass log 2 by Frullani. Canonical one-dimensional self-decomposability is equivalent to monotonic k(r)=rν(r) on r>0; differentiating shows −k′(r)=√α[(1+α/2)e^(−√αr)−√2e^(−√(2α)r)]≥0 for all r iff α≥2(√2−1). Below threshold k rises near zero, excluding OU marginals. Above threshold h=−k′≥0 is integrable with symmetric total mass α and defines a CP-driven OU with Brownian sqrt2; integrating exp-damped jumps reconstructs ν. Independent quadrature checked exponent identities at α=.1, α_c,1,2,7. This proves equality of stationary *one-time* marginals only, not the switched path process.

## originality

PASS

Best-of-knowledge: the complete mathematical claim was compared to exact or broader prior theorem statements, unlike-title aliases, current Resultary published findings and known data. Known premises and small cases are acknowledged. No inspected source demonstrates complete coverage; named inaccessible plausible full texts and reduction risks are recorded rather than claimed noncovering.

## value

PASS

An explicitly known stationary law of a physically natural switching diffusion is classified more finely by its infinite divisibility and Lévy-driven OU realizability. A sharp α threshold distinguishes universally possible Lévy decomposition from forbidden OU representation, and gives exact constructive finite jump intensities log2 and α. The precise phase transition cannot be read solely from the known characteristic function without the nontrivial monotone Lévy-profile analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
