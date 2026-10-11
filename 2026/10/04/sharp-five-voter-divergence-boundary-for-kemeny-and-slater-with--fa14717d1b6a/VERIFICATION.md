---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For a transitive three-candidate majority tournament both objectives choose the topological order. For a directed 3-cycle, Slater's three optimal orders each reverse one majority edge, whereas Kemeny minimizes the reversed majority-margin weight, so its top set is obtained from the weakest cycle edge or tied weakest edges. Every three-voter majority cycle has margins \((1,1,1)\), while the five-voter witness \(2ABC,2BCA,1CAB\) has margins \((1,3,1)\). A fresh independent exact replay of all labeled profiles for electorate sizes \(1,3,5\) reproduced the histograms \(6\); \(204+12\); and \(7236+360+180\), and an independent anonymous replay found exactly six divergent profiles with multinomial weight \(180\). The frozen verifier source was also read; its finite exhaustions corroborate the structural proof.

## originality

PASS

Lamboray's primary thesis explicitly gives the three-alternative structural comparison: in a majority cycle the Slater orders reverse one edge and the Kemeny orders reverse a smallest-margin edge. Klamler gives broader qualitative antagonistic examples. Neither inspected source states the smallest odd electorate realizing unequal cycle margins, the exact \(180\)-profile census, or its single relabeling orbit. Resultary searches for the exact boundary and constants returned no matching prior record.

## value

PASS

This is a natural first-divergence boundary between two classical aggregation rules, not an arbitrary parameter slice. It gives the complete smallest odd-electorate classification, prevalence, margin geometry and symmetry orbit after the local three-candidate rule behavior is known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
