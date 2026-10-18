---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Binary table (TP,FP,FN,TN) all strictly positive and TP*TN>FP*FN, same N and same actual prevalence P across compared classifiers. Writing Q=N-P,R=TP+FP,S=N-R,Delta=TP*TN-FP*FN gives MCC=Delta/sqrt(PQRS) and kappa=2Delta/(PS+QR). These exact formulas were rederived; positive signs make squared MCC comparisons order-preserving. Complete independent enumeration of positive-Delta tables and all unordered pairs by N,P from N=4 through 12 used integer cross-products for squared MCC and exact rational kappa: no weak disagreement for N<=9, 4 weak-only differences at N10, none at N11, and exactly 2 strict reversals (class-complements) at N12. Through N11, 382 eligible pairs checked. N10 P3: A=(1,1,2,6),B=(2,3,1,4), MCC ties 1/sqrt21, kappas 4/19>1/5. N12 P4: (2,3,2,5) kappa2/17 MCC1/sqrt70 vs (3,5,1,3) kappa1/10 MCC1/8: strictly opposite. Finite exhaustion is valid because claim quantifies only 4<=N<=12 for minimal boundary.

## originality

PASS

Primary published comparison identifies metric properties and large discrepancies (especially negatively associated confusion matrices), but does not derive sharp first positive-association fixed-prevalence ordinal reversal and equality classification at N=12. Targeted Resultary search encountered generic correlation floors and unrelated confusion-matrix Markov fibers, not this threshold. Exact numbers and search failures alone do not guarantee novelty, but statement and restrictions differ substantively from background metrics.

## value

PASS

Sharp minimal data-set size and precise weak-versus-strict onset for two widely used classification measures under scientifically meaningful nondegenerate positive-association/fixed-prevalence constraints. Demonstrates pointwise metric closeness does not guarantee ordinal classifier ranking; exact small-model boundary is useful as a methodological counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
