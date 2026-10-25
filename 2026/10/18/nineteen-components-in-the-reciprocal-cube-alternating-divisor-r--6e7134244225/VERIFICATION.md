---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For all positive n, multiplicativity reduces s_{-3}(n) to local factors f_p(e)=sum_{j=0}^e(-p^{-3})^j. For p>=11, an exact five-prime exceptional certificate and Nagura’s prime interval theorem for p>=29 prove u_p=-log(1-p^-3)<=sum_{q>p}u_q; the subsum interval lemma therefore fills the closure [T,1]. Exact inequalities T f_p(2)<=f_p(1) for p=3,5,7 and T f_2(4)<=f_2(3) reduce arbitrary prime powers to 135 rational scales. Independently computed all 135, merged them using rigorous rational two-sided bounds from floor(10^18/k^3) through k=100000 and an analytic tail, and verified ALL 19 submitted rational endpoint pairs, all 18 strict gaps and every overlap. Closest certified separation >0.0000326 and overlap >0.0002716. This proves 19 components given the stated standard prime-gap and subsum lemmas; the finite rational certificate alone is not the infinite tail proof.

## originality

PASS

PASS on the exact r=3 component classification, not on multiplicativity, Defant’s interval/density framework, or the general subsum lemma. Defant’s 2015 paper states a connectedness/density criterion and separately raises exact component counts as a problem. The published 2026 exact two-component result treats r=2, which neither implies nor gives the nineteen disjoint intervals for r=3. Complete independent r=3 endpoint enumeration adds a concrete solution to a naturally posed parameter case. Unindexed exact tables remain a priority risk.

## value

PASS

A natural arithmetic function has a documented open component-count question at specific exponents; the precise r=3 closure topology, with rational coefficients and 18 certified gaps, supplies an otherwise unknown exact answer to that question. The prime-tail reduction plus a rigorous 135-factor certificate creates reusable arithmetic structure; this is not an arbitrary digit slice or just a simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
