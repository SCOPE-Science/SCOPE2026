---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Under independent uniform sign sampling and independent Bernoulli pre-step refresh, put r=1-h and d=p+(1-p)h. Averaging the update gives C'11=(r²+h²v²)C11-2h²v²C12+h²v²C22, C'12=r[pC11+(1-p)C12], C'22=pC11+(1-p)C22. For P with unit diagonal and off-diagonal pr/d this gives M(P)=P-(hQ/d)E11, with E11+M(E11) positive definite by its positive leading minor and determinant p[1+h²v²+(1-p)r²]. Thus the two-step map supplies an order contraction when Q>0 and growth when Q<0, with a fixed positive definite P at Q=0. From common nonzero initialization, C2 is positive definite by independent nonzero sign variance except at p=h=1, when C3 is positive definite. This gives the required lower comparison for the iterate, not just a statement about an abstract spectral radius. At h=2 the same growth argument works even for the semidefinite P at p=1; at h>2 Jensen and the unbiased mean give exponential growth. Q is strictly concave with Q(0)>0, Q(2)<0, and a single positive root. Q(1)=1-2v² and Q_p=(h-1)(h-2), proving the direction of the strict reversal and its constant threshold at v²=1/2. Independent rational substitution gives 7/64 and -1/32 at the two witness probabilities; when Q<0, M(P)≥P also transfers the geometric lower bound to the intervening iterates. The finite check corroborates only that witness, not the theorem.

## originality

PASS

The exact p=1/2 frontier is existing coverage, as already acknowledged by the finding. Credit only the all-positive-p classification and the contrast-dependent reversal with the fixed-step witness. The closest inspected narrow theorem excludes other p; the broad algorithm papers do not give exact scalar necessity or the reversal.

## value

PASS

The exact boundary separates stable and unstable behavior in a canonical variance-reduced method; the fixed-step witness isolates a counterintuitive failure caused by increasing refresh alone, even though the estimator remains unbiased. The contrast cutoff supplies a structural explanation and is useful separately from the already known single-p boundary. It is not a claim about optimal refresh cost or general objectives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
