---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

In the minimal expansion of the Fraisse generic ultrametric over chain Lambda_d with d>=1 proper covers, each adjacent equivalence pair carries one subquotient order on child classes. A finite induced n-point type (n>=1) is a recursively ordered hierarchy. Reading all child orders top-down gives a unique permutation of n labeled leaves, and recording the first common equivalence level of each adjacent leaf pair gives a d-letter gap word of length n-1. For every i, E_i-classes are precisely maximal contiguous blocks cut at gaps of color>i, and the local subquotient orders are the induced orders on child blocks; this is an inverse bijection. Thus a_d(n)=n! d^{n-1}. Equality partitions of repeated tuple coordinates yield b_d(n)=sum_{k=1}^n S(n,k)k!d^{k-1}=F_n(d)/d and EGF (e^x-1)/(1-d(e^x-1)), with d=a_d(2)/2. This does not claim n=0 in a_d. Verified against Braunfeld Definition 7.7 and Braunfeld-Simon Definition 5. The actual verifier recursively enumerates ordered nested set partitions for d<=3 n<=5, while independent arithmetic checks Stirling/Fubini identities for d<=4 n<=9; infinite bijection is the proof.

## originality

PASS

Braunfeld's 2017 minimal successor-order expansion and Braunfeld--Simon classification fully cover the model, but their inspected primary definitions/theorems do not give the finite tuple orbit count or the permutation-with-colored-gaps parameterization. Classical ordered Bell/Fubini polynomials and the d=1 ordered partition case are prior. Closest Resultary Fubini orbit profiles for echeloned spaces and Catalan/Schroeder ordered ultrametrics concern different automorphism groups; no implication of n!d^{n-1} for this exact minimal chain expansion. The claimed new content is the explicit orbit invariant on the canonical chain-lattice Ramsey expansion, not the elementary Fubini transform alone.

## value

PASS

Tuple-orbit profiles are natural exact invariants of oligomorphic automorphism groups and chain minimal expansions are canonical Fraisse/Ramsey objects. The gap-color bijection describes every finite induced type, yields whole profiles, and recovers chain depth already at n=2. The exact closed form is a useful characterization even without a downstream classification theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
