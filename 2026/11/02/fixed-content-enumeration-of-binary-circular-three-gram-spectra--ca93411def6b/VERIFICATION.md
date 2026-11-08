---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

A circular three-gram histogram is a nonnegative balanced integer flow on the four-vertex order-two binary de Bruijn graph. Balance forces (h000,h001,h010,h011,h100,h101,h110,h111)=(a,t,t+f-s,s,t,f,s,h), c=t+f-s>=0, p=a+2t+f, q=h+t+s+f. The positive support admits an Eulerian closed walk exactly when connected. Five disjoint cases (t=s=0 with three connected types; t>0,s=0; t=0,s>0; t,s>0 with t>=s; t,s>0 with s>t) enumerate feasible flows via geometric series, yielding the displayed bivariate and length series. The pole order five gives n^4/288. Direct count of necklaces vs histograms n<=6 proves first collision, and zero-run padding gives distinct colliding necklaces for every n>=6. Independently enumerated binary words/fixed-content histograms through n14 and padded collisions through n25, matching first 14 coefficients; general theorem follows the connected-flow case proof, not finite tests.

## originality

PASS

Classical de Bruijn Euler-flow sufficiency (Arnoux 2016), linear k-abelian classes (Karhumäki et al.) and first-order cyclic Markov types (Jacquet et al.) are prior work. The full 2016 Cassaigne–Karhumäki–Puzynina–Whiteland proceedings discusses linear k-abelian equivalence and rationality; its asymptotic class-count for a different boundary convention has degree six, not this degree-four circular full three-gram count. No inspected published work directly states the fixed-content rational function or the sharp necklace collision threshold, though stronger general all-gram flow enumeration might imply the result and remains a priority risk.

## value

PASS

Complete circular three-gram multiplicity is a natural exact information model for reconstruction from read histograms. A fixed-composition rational generating function, sharp class-count asymptotic and exact zero-error necklace-code size/first collision boundary answer more than the generic Eulerian realizability criterion. The fact is self-contained and useful for combinatorics on words and sequence reconstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
