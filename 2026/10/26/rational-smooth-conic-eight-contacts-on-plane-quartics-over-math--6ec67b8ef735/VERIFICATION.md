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

# Computational verification

Both Python programs run with Python 3 and SymPy. Keep `census_octactic.py` and `verify_octactic.py` together; the first writes `conic_census.json`, then the second loads this certificate and writes `octactic_verified.json`.

The first enumerates all \(279\) binary quartic projective orbits, reconstructs \(78\) geometrically smooth ones by exact chartwise Groebner bases, and searches each rational point on smooth representatives for smooth conic contacts of order eight using formal local series in \(\mathbf F_2[t]/(t^8)\). Its weighted frequency output is \(\{0:9849,1:840,2:210,4:21\}\).

The second independently constructs all \(84\) smooth-conic/rational-point flags, solves the conic local parameter for each, tests the resulting conditions directly on all \(32,767\) nonzero quartic masks, rechecks Groebner smoothness of every supplied representative, and recreates every orbit from \(168\) explicitly generated coordinate transformations. Its output is the same frequency table; there are \(28\) geometrically smooth conics, \(78\) smooth quartic orbits, and \(10,920\) smooth forms. The \(21\) maximizing quartics are explicitly listed in `octactic_verified.json`, including the representative numbered `4689`.

Each program's arithmetic is finite, exact, and deterministic. Its assertions check conic count, orbit count, partition, smooth count, distribution, and extremal size. The second checker shares the first program's orbit representatives as an input but independently validates the labels, orbit sizes, and full partition. Thus the two methods are independent with respect to the geometric contact computation but not completely independent in how the orbit representatives are initially selected. Formal power-series checks establish the local multiplicity; they are not numerical approximations. No claims beyond these finite exhaustive calculations have been tested, and no external independent audit has been performed.
