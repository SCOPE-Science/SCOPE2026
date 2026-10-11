---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Lifting a monotone crown map to the infinite alternating fence gives increments in {-1,0,1} whose total is 2n times the degree and bounds absolute degree by floor(m/n). Between nonzero increments every zero run has even length. Comparable-map moves cancel adjacent opposite signs and slide zero pairs, reducing every nonextremal fixed-degree map to a common sign-pure normal form and using a spare zero pair to connect target phases. At maximal degree when n divides m, every increment has the same sign, leaving n target phases for each sign and no comparable perturbation, hence isolated maps. Fresh exhaustive mapping-poset replay gives map/component totals 48/1, 200/3, 234/7, 1156/7, and 1248/3 for the five representative pairs, with degree-resolved component sizes exactly as predicted.

## originality

PASS

Best-of-knowledge originality passes with a substantial close-analogy risk. Cavallo-Sattler define the same crown winding number and prove only the shorter-to-longer zero-degree bound. Cukic-Kozlov classify connected components of graph-Hom complexes between ordinary cycles by wrap data and isolate maximal wraps, but graph homomorphisms forbid collapsing a source edge, whereas monotone crown-poset maps may collapse comparable pairs; their complex is therefore not the finite-space mapping poset. The assigned cancellation/zero-pair argument is the missing bridge that classifies all monotone maps. The older Farley and Currie-Visentin papers explicitly enumerate raw order-preserving maps but their full text was inaccessible in this run; authorized institutional attempts after OA failure were unavailable, so no whole-document noncoverage claim is made.

## value

PASS

This is a complete two-parameter classification for the standard finite T0 models of the circle. It identifies every realizable degree, a sharp divisibility boundary, and the exact rigid maximal-winding multiplicity, providing concrete finite-space information that ordinary topological homotopy and graph-Hom analogues do not by themselves supply.

The dated certificate retains the supplied scientific assessment, sources and limitations.
