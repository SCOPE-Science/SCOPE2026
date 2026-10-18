---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Reconstructed the source-initialized inexact WRaSK update with normalized integer rows v1=(0,1,1), v2=(2,1,0), v3=(1,-1,0), lengths squared 2,5,2 and det=-3, xhat=(2,0,2), lambda=1/2, y0=x0=0. Independently exact-fraction enumeration of all 9 row-pairs yields matrix [[6,49/10,61/16],[971/200,89/20,409/100],[61/16,401/100,6]] of squared solution errors and uniform average 4193/900. First-choice row2 produces smallest first-step error 49/10 versus 13/2 others; residual power p>0 raises its probability above 1/3. For every real p>=24, P(first=2)>100/101 and P(second=1 | first=2)>2048/2049; path error 971/200 gives the strict two-step lower bound 994304/206949>4193/900 without assuming anything on other paths except nonnegative loss. At lambda=0 the same geometry has greedy 102/25 versus uniform 101/25; algebraic identity 4(Rgreedy-Runiform)=(1+c^2)(u^2-v^2)+2(cu-v)^2>=0 for u^2>=v^2 proves two rows cannot reverse in ordinary orthogonal projection, even for parallel/tied rows. The two-row theorem does NOT extend to positive lambda.

## originality

PASS

The source Algorithm 1 and weighted p-sampling are previously known, with upper bounds on expected Bregman error or squared-error rates. The submitted claim is not a rate guarantee: it compares exact path-averaged solution errors at k=1 and k=2. Primary 2022 Zhang paper (lawful full arXiv version) and 2021 Tondji conference text were materially inspected; neither provides this explicit reversal and two-row impossibility. A relevant published one-step coherence residual spike measures total residual, not two-step solution distance.

## value

PASS

A concrete full-rank consistent linear system shows that greedy residual-power selection can improve first-step expected squared solution error and yet worsen second-step risk despite a valid convergence-rate bound. The universal two-row orthogonal-projection barrier and attained three-row boundary make this a motivated mechanism/minimality fact, not an arbitrary table of iterates. The positive-regularizer witness and unregularized minimality are stated separately.

The dated certificate retains the supplied scientific assessment, sources and limitations.
