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

In sweep coordinates, populations below k or above k+1 move monotonically farther from the band and give a constant output when the sweep starts there. Inside the band the unique flips that do not escape are 0 to 1 at k and 1 to 0 at k+1. Escape on either of the first two updates leaves no already processed bit inconsistent with the resulting constant. Thus the only potentially nonconstant outputs come from the two stated first-two-bit signatures, which produce a mixed output prefix. Escape later yields a nonconstant output outside the band, with exactly one more sweep needed. Survival of the whole sweep forces an alternating input and complements it. For even n its complement has the wrong start bit for the same population and escapes on the next sweep; for odd n survival requires n=2k+1 and both alternators already form a cycle. This also excludes transient predecessors of the cycle and all other periodic configurations. The signature sizes are binomial(n-2,k-1) and binomial(n-2,k); subtract the two already periodic states precisely in the odd central case. This handles n=3, and gives a positive second shell for all n>=4. The local binomial estimate at k-(n-1)/2=s sqrt(n)+O(1) yields the stated Gaussian limit with the extra factor 1/2 from 2^n rather than 2^(n-1). An independent functional-graph enumeration discovered cycles without prespecifying them and reproduced the basin and entry claims on 14,344 initial states for all admissible pairs with 3<=n<=10.

## originality

PASS

The known complementation lemma and critical threshold gap are not new. Neither the prior all-function extremal result nor the closest exact entry distributions give the two-bit, two-sweep shell and the isolated odd-central attractor for the specified clique rule.

## value

PASS

Complete graphs are a natural global-interaction benchmark in a threshold-gap regime where general graphs can sustain long cycles. The result explains exactly which initial states delay relaxation and which realize persistent oscillation, separating the size of a slow shell from the tiny basin of the only nonconstant attractor. Neither an upper bound on period nor a numerical small-n census would supply this statewise and parametric information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
