---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For synchronous binary ring length n>=3, Boolean distributivity gives S(F^t x)=S(x)+{-t,-t+2,...,t}. Translation by -t leaves each length-(t+1) interval in the +2 cyclic order; on each nonempty orbit first saturation occurs iff all positive cyclic gaps are at most t+1. Since S(F^2x) contains S(x), a periodic state must have each +2 orbit either empty or full, and those states are truly periodic (odd n: two fixed; even n: two fixed plus an alternating 2-cycle). Thus the preperiod is max gap minus 1, with empty support assigned zero. For an orbit of size q, rooted cyclic compositions count gap-bounded k-subsets by (q/k)[u^q](u+...+u^h)^k, and inclusion-exclusion yields the asserted binomial coefficient. Two independent parity orbits give B_{q,h}^2 in even rings. A maximal q-gap occurs iff that orbit contains a singleton; this proves the odd n extremizer count n and even n count n*2^(n/2)-(n/2)^2 by inclusion-exclusion, with maxima n-1 and n/2-1. The proof reconstructs all n,t,k including n=3,4, t=0, empty support and q=2. Independently written brute force reproduces every preperiod and occupancy-weight coefficient for all 131064 states over n=3..16, verifies both closed polynomial derivations and sharp extrema; finite computations only corroborate the all-n analytical argument.

## originality

PASS

Qualified PASS for explicit evaluated all-size all-time fixed-density Rule-250 gap-enumeration polynomial and sharp labelled-extremizer count, NOT for Rule-250 OR definition, periodic orbit classification, generic transfer matrix count or Wuensche n=15 maximum-delay example. Public primary materials were read in relevant full-text form, and two semantic Resultary searches did not expose the particular explicit bounded-gap polynomial; known broader/corollary coverage is explicitly credited. The Macfarlane PostScript and early Wolfram source remain material priority risks, so no absolute novelty certification is claimed.

## value

PASS

Finite cyclic Rule-250 dynamics is a natural, classical Boolean dynamical system. Its entire incoming transient forest is not resolved by knowing its eventual periods: explicit E_{n,t}(z) gives simultaneously every time-to-attractor distribution and Hamming-weight slice for arbitrary ring length. The odd/even step-two orbit structure yields a sharp parity transition in maximal delay and counts of slowest initial conditions, natural invariants needed for finite-size convergence and exact benchmark statistics. The gap composition coefficient is classical and is not asserted to be new; the useful contribution is an explicit complete dynamical classification rather than a tiny arbitrary parameter slice or raw simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
