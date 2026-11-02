---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

PASS: Resistance to two pinned vertices in a tree is h+z(ell-z)/ell, where h is pendant resistance and z is distance on the grounded path of total ell. Directly recomputed the eight symmetry-type grounded trace formulas from original RESULT.md (blob 20519d3fbfd07a0550ad1d942d0b8739904df3af): hubs 0 excess, own-hub+leaf t(q+1)-1 or t(p+1)-1, cross-hub+leaf [t(q-1)-1]/(t+1) or [t(p-1)-1]/(t+1), two leaves same side [N-4+2t(other side+1)]/2, opposite leaves [N-4+t(N-2)]/(t+2). Leaf-pair excesses strictly positive; own-hub options are worse than cross-hub options by t[1+(q+1)t]/(t+1) or its twin; compare remaining cross terms and zero to get stated threshold and tie/equal-side cases. Independently inverted rational grounded Laplacians and tested 690 pair/parameter combinations spanning 25 positive rational (p,q,t) instances (independent_extra.py: DOUBLE_STAR_OK), not extrapolated from finite checks.

## originality

PASS

PASS best knowledge: Grounded Laplacian resistance method and leader centrality are established; Patterson–Yi–Zhang 2017 studies resistance and perfect rooted trees with unit weights, Fitch–Leonard 2014 paths/cycles, Patterson–Bamieh 2010 leader selection. No inspected primary theorem supplies all p,q>=2 and continuous bridge t with the exact minority-side phase transition, though specialized weighted-bistar literature could.

## value

PASS

PASS: With a natural two-leader pinned-consensus variance objective, an exact change in optimal leader geometry occurs as an intercommunity resistance changes, with a surprising threshold set solely by the smaller leaf multiplicity. The full minimizer set and equality cases are useful structural design information, not a generic matrix inversion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
