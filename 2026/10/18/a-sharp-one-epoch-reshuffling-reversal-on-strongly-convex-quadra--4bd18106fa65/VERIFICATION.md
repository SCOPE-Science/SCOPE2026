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

The rank-one matrices P,Q are the unit-step maps, not the Hessians: I−P and I−Q have eigenvalues {1,1−b} and {1,1−p}, are positive definite, and each has L=1. The centered components have common minimizer zero. For u=(1,0), P²u=QPu=0 while v=PQu=(0,bp/2) and w=Q²u=(p²/2,p²/2). Thus RR and IID expectations are F(v)/2 and [F(v)+F(w)]/4, where F uses H=I−(P+Q)/2. Substitution gives F(v)=b²p²(4−2b−p)/32 and F(w)=p⁴(4−b−2p)/16; subtraction recovers p²T_p(b)/128. The derivative T′_p(b) is concave in b and strictly positive at both endpoints (2p² and 2(1−p+p²)). T_p(0)<0, while T_p(1)=4p³−6p²−p+2 decreases from 2 to −1, so p_* is unique, and the endpoint p=p_* gives a strict negative gap throughout 0<b<1. Factoring at p=1/2 gives the stated threshold and exact tie. The expectation ratio is 2F(v)/(F(v)+F(w))<2 since F(w)>0; F(v)∼p²/16 and F(w)∼3p⁴/16 in the stated double limit, proving sharpness. Independent rational history checks at p=1/2 gave gap 29/128000 at b=4/5, a tie at b=3/4 with both expectations 9/2048, and gap −5/4096 at b=1/2. These corroborate the deductions; the frozen checker grid is not needed to prove them.

## originality

PASS

Qualitative RR reversals, the underlying rank-one angular family, and the Euclidean sharp factor-two comparison have precedents. The distinct result is the exact terminal expected-objective boundary for centered, common-minimizer strongly convex quadratics at η=1/L, including objective reversal and sharpness of the ratio in that metric. This metric changes even the sign for some identical maps and starting vectors, so the close indexed Euclidean theorem is not equivalent. The factor-two upper bound alone is the elementary conditioning bound and is not independently novel.

## value

PASS

Expected objective error is the optimization metric here; substituting the indexed Euclidean risk can give the opposite sign for the very same algorithm and input. The centered 2D witness removes component-minimizer mismatch and uses the standard step 1/L instead of overshoot. The exact region does more than furnish an isolated numerical example: it identifies where the objective reversal survives in the model and how large it can be even with identical gradient-evaluation budgets. Value is for this tightly controlled counterexample and comparison, not for the generic conditioning bound or for asymptotic claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
