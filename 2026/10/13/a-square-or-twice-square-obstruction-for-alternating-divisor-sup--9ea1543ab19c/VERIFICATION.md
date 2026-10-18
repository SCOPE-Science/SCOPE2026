---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

β(p^e)=(p^(e+1)+(-1)^e)/(p+1) gives β(u)<=u, and β(m) odd iff every odd prime exponent in odd m is even. The equation forces n even; if n=2^a m with nonsquare odd m, u=β(n) even. The proof exhausts all a: for odd a use R(a)<2/3,R(t)<=3/4 giving β(u)/n<1/2; a=2 gives 3|u and β(u)/n<=(3/4)(3/4)(7/9)=7/16<1/2; even a>=4 and t=v2(u)!=2 gives <=(11/16)^2=121/256<1/2; if t=2, β(u)=3β(v) implies 3|m, so bound <=(11/16)(7/9)(3/4)=77/192<1/2. Contradiction in each branch proves odd m square. Classify parity of a into even square or twice square, disjoint by 2-adic valuation; count candidate shapes exactly. Independent multiplicative finite check through 250000 found solutions 2,4,8,128,32768, supportive only.

## originality

PASS

Tóth 2011 survey has the parity criterion β(n) odd iff n is square or twice square and gives superimperfect examples, but it does not assert that the odd part of every solution 2β(β(n))=n must be square. OEIS A200758 tabulates examples but no proof of the unrestricted shape bound. Though it uses familiar local abundancy inequalities, the case split is a nontrivial necessary structural restriction; possible unpublished elementary derivation is acknowledged.

## value

PASS

The iterated β-superimperfect classification remains open; proving that every candidate has a square odd part reduces possible prime exponent patterns and gives O(sqrt X) global sparsity of the solution set. This is a natural all-integer obstruction rather than a low-range numerological census or complete-classification claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
