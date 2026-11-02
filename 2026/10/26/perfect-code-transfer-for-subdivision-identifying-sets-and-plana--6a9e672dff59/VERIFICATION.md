---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Open domination of every inserted edge vertex forces selected original vertices A to cover base edges, so T=V\A is independent. Open independence means selected inserted vertices cross A/T; distinct edge signatures and exactly one selected subdivision neighbor at each a force exactly one T-neighbor per a. Thus every closed neighborhood contains exactly one T vertex (perfect code); if t in T is pendant, the sole adjacent a and t share an identical singleton open signature, and isolated t is undominated, so deg(t)>=2. Conversely any nonpendant perfect code yields selected originals A and every cut subdivider: A originals have distinct singleton edge signatures, T originals have disjoint multi-edge signatures, and subdivision vertices distinguish their A endpoints, proving the bijection. Exactly |A| cut subdividers implies |C_T|=2(n−|T|). Cubic planar G has only nonpendant T, perfect code cardinality n/4, and the polynomial reduction preserves YES instances; known planar cubic perfect-code NP-hardness plus NP membership gives the restricted result. Independently direct brute-force tested 75 small bases, plus the K4/Q3 controls.

## originality

PASS

Seo–Slater 2017 full primary paper already characterizes OLD_oind sets for all girth>=5 graphs via selected and unselected neighborhood counts and proves general NP-completeness; those are not new here. Cappelle et al 2022 full paper proves hardness separately for planar bipartite max-degree-five girth-six and planar subcubic girth-nine; neither theorem implies the simultaneous planar+bipartite+subcubic+subdivision restriction. The new exact code correspondence can be derived using established high-girth criteria but is not explicitly stated/entailed without a subdivision-specific combinatorial reduction, and provides a parsimonious all-base count. The planar cubic perfect-code NP-hardness premise was previously published in 1988. Equivalent subdivision-identifying code transfer may be indexed elsewhere: a material priority risk.

## value

PASS

Efficient closed-neighborhood perfect codes in ordinary graphs and open-independent locating sets in their subdivisions are two natural identification notions. The exact bijection and size generating function transport existence and enumeration, and combining it with planar cubic hardness strengthens previously incomparable planar-bipartite and planar-subcubic restrictions to an actual intersection subclass. This is a motivated parsimonious structural reduction, not an arbitrary isolated small instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
