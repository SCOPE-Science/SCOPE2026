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

Port H=(113322,797), squarefree B=157*q*r*s with prime 157<q<r<s, identity 797B-113322*partial(B)=1. Algebra yields inherited R1=113322*157=17791554 and c1=797*157-113322=11807; for fixed q, c2=c1*q-R1, R2=R1*q, equation c2*r*s-R2*(r+s)=1 forces c2>0. From s>r>q derive 1507<=q<=4520, with 375 prime q candidates. From s>r derive r in max(q+1,R2//c2+1)..floor(2R2/c2), finitely exhaustive and safe global r bound ~1.1 million. For every q and prime r in this interval compute uniquely forced integer s=(R2*r+1)/(c2*r-R2), test exact divisibility. Independent sieve-based enumeration checked 242779 admissible prime r pairs and exactly one integral candidate (q,r,s)=(1979,10093,16879); each prime and s>r confirmed, direct integer identity verified B=52931284472141 and cB-Rpartial(B)=1. All bounds derived algebraically; no heuristic primality or failure/timeout inference. Only least-prime-157 branch, not all possible fillings.

## originality

PASS

Wang 2026 primary paper Prop 8.4 supplies exactly the same four-prime product as a known primitive filling, but explicitly notes smaller fillings may be incomplete and does not classify all four-prime fillings beginning with 157. The uniqueness statement adds an exhaustive inherited-equation branch theorem (375 second primes and 242779 third-prime possibilities). Resultary related primary pseudoperfect facts concern a different number-theoretic notion. Source existence does not imply uniqueness.

## value

PASS

A motivated exact partial classification of a currently incomplete finite-port filling search: isolates the same least prime as a displayed key primitive filling and rules out every other four-prime filling in that natural branch, which can constrain inherited channels in a six-prime problem. This exact branch fact is not a random constant substitution or merely rechecking a known witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
