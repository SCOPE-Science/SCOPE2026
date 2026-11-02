---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

PASS: A commuting idempotent is a projection onto an ordered pair of invariant module summands for F_q[t]/(t^a)^m plus F_q[t]/(t^b)^m. Their automorphism group cardinality is q^(a x²+2a xy+b y²) times Phi_x(q) Phi_y(q), from Hom dimensions and reduction modulo t. The transitive automorphism action has stabilizer Aut(image) x Aut(kernel), yielding every exact profile count. Completing the exponent gives -2a(r+s-m)²-2(b-a)(s-m/2)²; the Phi factors tend uniformly to their nonzero Euler-product limits on growing central boxes while Gaussian tails are exponentially small. Thus the parity-dependent product-theta limit and total-variation estimate follow; finite counts do not establish it. Independently recalculated the nine (r,s) exact counts for q=2,a=1,b=2,m=2: [1,384,256,96,2304,96,256,384,1], sum 3778; approximate TV distances at m=6,7,10,11 were respectively .03311,.02260,.00803,.00555.

## originality

PASS

PASS qualified: the finite orbit-stabilizer/profile distribution is an acknowledged consequence of earlier module-decomposition enumeration and is not counted as novel. The assessed contribution is the explicit two-coordinate parity-sensitive independent theta limit with total-variation rate for the natural many-block family; examined centralizer and decomposition sources do not assert or immediately imply that asymptotic law without additional limit analysis. Broader Hall-polynomial asymptotic treatments could contain an equivalent and remain a material priority risk.

## value

PASS

PASS: Image Jordan multiplicities of a random commuting idempotent are natural complete invariants of its invariant direct summand, unlike a manufactured numeric slice. Their asymptotic factorization after W,V transformation, persistent parity shift, and negative covariance in original coordinates are structurally informative over an infinite matrix family. The fact that the finite orbit formula is classical does not collapse the new quantitative probability law into textbook arithmetic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
