---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The exact package defines s^r independent uniform edge colors and missing colors as acyclic monochromatic subgraphs. One-hot vectors are negatively associated; disjoint color-coordinate blocks and common monotone-decreasing maps preserve negative association. Product MGF bounds give the stated Chernoff estimate. Conditioning on s independent self-loop colors gives E[M|L]=(q/a_s)Z_s, where Z_s is classical empty-box occupancy; total variance then yields the exact lower inequality and its asymptotic (e-2)c_*^2 with a_s->e^-1 and V_s/s->e^-1-2e^-2. The r=2 mean s q~c_*s^(2/3) is cited to Gravner–Kulhanek, not re-proved. Summable Chernoff tails via Borel-Cantelli establish the strong law for any coupling, and upper variance gives L2. Independently enumerated all 16 colorings for s=2 and 19683 for s=3, obtaining exact variance/lower bounds 15/64 vs 9/64, and 14396210/43046721 vs 6396416/43046721. The finite tests cannot establish all s,r.

## originality

PASS

Original contribution assessed as the exact self-loop-occupancy lower variance bound and its positive s^(1/3) coefficient in the specific random de Bruijn model, not the classical negative-association closure, binomial Chernoff, nor the one-color asymptotic. The closely matching 2026 cellular-automata paper is the main historical risk because full primary text was not re-read this run; no decisive prior implication identified.

## value

PASS

Natural missing-constant-count fluctuations in random cellular automata. Quantifies a rigorous positive fluctuation obstruction due only to self-loop labels, complements an optimal binomial-type concentration upper tail, and gives almost sure scaling at the correct deficit scale. Neither the lower nor upper variance exponent is asserted sharp; this is useful two-sided information for an intrinsic observable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
