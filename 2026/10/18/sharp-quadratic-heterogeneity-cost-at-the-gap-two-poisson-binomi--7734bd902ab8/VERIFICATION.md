---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

At each integer k>=1, m=k+d_k and homogeneous q satisfy the exact threshold tie by Kleiner Theorem 1, with unique boundary tie by Proposition 7. For two factors (q+z,q-z) the generating polynomial changes by -z²(u-1)²: P(S=k)-P(S=k+2)=alpha_k z² for every feasible z. Rigidity gives alpha_k>0. Factorial ratios express alpha_k/c=(1+t)²B_k/[m(m-1)]. All symmetric mixed second derivatives are alpha_k, pure second derivatives zero, and sum_i v_i=0 gives isotropic alpha_k/2 eps² sum v_i². Derivative of binomial atom difference under common added h/m equals 2c/[mq(1-q)]>0, so IFT gives unique local compensating h and exact C=tB/[4(m-1)]. d_k~sqrt(k/8), binomial factorial expansion B_k=4+O(k^-1/2), yielding sqrt(k)C->2sqrt2. Independent binomial convolutions at k=1,2,5,24,80 match full-range pair identity and alpha formula; k=10^4,10^6 approach the large-k limit. Boundary k=0 is excluded precisely because Kleiner rigidity fails there.

## originality

PASS

Kleiner establishes the boundary tie and rigidity, not a signed second variation or mean compensation coefficient. A published pair-balancing transport law gives general second-difference operations but not this critical-binomial cross-level coefficient, strict curvature and asymptotic cancellation. The new quantitative stability is a non-immediate targeted extension; exact prior premise credited.

## value

PASS

Once the unique boundary crossover is known, the invariant physical question is how unequal trial probabilities destroy a tie and how many additional expected successes restore it. The global opposite-pair law, isotropic local Hessian and nontrivial 2sqrt2 asymptotic restoration constant quantify sharp stability and are not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
