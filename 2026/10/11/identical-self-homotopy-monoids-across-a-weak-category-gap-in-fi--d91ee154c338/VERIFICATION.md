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
# Verification of the finite-space self-homotopy monoid comparison

The main assertion is proved for **all** integers \(m\ge2\) by the symbolic cap lemma in `RESULT.md`. The following fully finite computations verify its critical nine-point hypothesis and the first capped case; they are not extrapolated to arbitrary cardinalities.

Run `python3 verify.py` using a Python interpreter with the standard library. The algorithm constructs the full partial order on the nine vertices from the thirteen exact Hasse covers and enumerates every monotone selfmap, using a linear extension and checking all preceding comparable coordinates. It then unions pairs that differ by one coordinate and whose old and new values are comparable. Every pointwise comparison of maps decomposes into such one-coordinate comparisons by modifying domain coordinates from maximal to minimal, so those unions determine all finite-space homotopy components, not merely a sampled subset.

The complete outputs are:

```text
P9: maps=12575, components=3, component_sizes=[12573, 1, 1], isolated=2
P9+D2: maps=232727, components=5, component_sizes=[232723, 1, 1, 1, 1], isolated=4
abstract_monoid(m=2): size=5, units=4, associative=YES
abstract_monoid(m=3): size=49, units=12, associative=YES
VERIFY_OK
```

The isolated nine-point maps are explicitly checked to be exactly its two automorphisms, represented by images of the ordered vertices:

```text
(0,1,2,3,4,5,6,7,8)
(2,1,0,4,3,5,6,8,7)
```

The four isolated eleven-point capped maps are the two possible base automorphisms times the two nonconstant permutations of the new maxima. This validates a nontrivial test case of the cap lemma.

The source's category computations and the statement that the nine-point base is weakly contractible but not contractible were checked against Corollary 4.2 and Proposition 5.2 of arXiv:2609.39615v1. The first homology of \(B_m\) is independently computed by the connected graph formula for \(K_{2,m}\): \(2m-(m+2)+1=m-1\). The source's exact Hasse covers agree with those in `verify.py`.

These computations do not compare the full homotopy types of the selfmapping spaces and do not prove a classification for arbitrary base posets without the cap-lemma hypotheses. Independent external audit is unperformed.
