---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and limits

Compile the standalone C++17 checker and run the independent Python checker in the directory that also contains `orbit_certificates.csv`:

```sh
c++ -O2 -std=c++17 verify_census.cpp -o verify_census
./verify_census
python3 verify_orbits.py orbit_certificates.csv
```

Observed successful checks:

```text
CENSUS_OK vertices=20 edges=30 tested=1048576 forests=755608
CENSUS_OK forest_coefficients=1,20,190,1140,4845,15492,38580,76260,120540,151920,150480,113400,60620,19600,2520
CENSUS_OK maximum_order=14 minimum_FVS_size=6 optimum=2520
CENSUS_OK maximum_induced_trees=1860 disconnected_maximum_forests=660
CENSUS_OK inclusion_maximal_forests_13=1120 _14=2520
FORESTS_OK masks=1048576 induced_forests=755608 optimum=2520 maximal_13=1120
AUT_OK adjacency_preserving_bijections=120
ORBITS_OK full_automorphism_group=120 optimum_orbits=25 orbit_sizes=120x18+60x5+40+20
ORBITS_OK tree_orbits=17 two_component_orbits=8 certificate_coverage=2520
```

The C++ checker uses cycle-detecting union/find on each induced edge set. The Python checker uses independently constructed breadth-first components and the edge-minus-vertex forest identity, and then searches all automorphisms by exhaustive partial adjacency-preserving assignments. The CSV encodes all orbit representatives in the documented vertex bit labelling and is checked for disjoint complete orbit coverage.

The computation is exhaustive for this one finite graph; it is not an independent mathematical audit, and it says nothing about arbitrary graph orders. The minimum feedback vertex cardinality and existence of a 14-vertex induced forest predate this classification. The two most closely related generalized Petersen decycling papers were not fully available for priority comparison.
