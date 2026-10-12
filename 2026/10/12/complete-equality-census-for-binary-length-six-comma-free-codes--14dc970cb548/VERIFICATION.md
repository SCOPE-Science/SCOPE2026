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
# Verification

The standalone `verify.py` uses only the Python standard library. It reconstructs all \(64\) binary words of length \(6\), identifies exactly \(54\) primitive words and the resulting nine cyclic necklaces, and uses the one-representative-per-necklace lemma to certify the upper bound \(9\).

It then performs a complete depth-first enumeration of transversals of those nine necklaces. A branch is pruned only after the current partial code already contains a forbidden shifted overlap; this predicate is monotone under extension. Every terminal candidate is rechecked directly from the comma-free definition. The replay finds exactly \(1{{,}}972\) maxima.

Finally, the program applies identity, global bit complement, reversal, and complemented reversal to every enumerated maximum. It verifies closure, obtains exactly \(493\) orbits, checks that each orbit has size \(4\), and confirms zero fixed maxima for each nonidentity transformation.

Expected replay summary:

`VERIFY_OK`

`primitive_words=54 necklaces=9 upper_bound=9 dfs_nodes=7699`

`maximum=9 labeled_maxima=1972 symmetry_group=4 orbits=493 orbit_sizes=4x493`

`fixed_nonidentity=0,0,0`

`weight_multiset=1,2,2,3,3,3,4,4,5`

`canonical=000001,000101,000111,100001,100101,100111,101001,101011,101111`

`census_sha256=1bb055dda90b39482eff5bc235fcb28d39ddbb2485e9e2d7e17633d56a1dd61e`

Limits: this is a finite proof for the stated length and alphabet. It does not establish claims at other lengths or alphabet sizes, and it does not treat transformations beyond the explicitly verified order-four group.
