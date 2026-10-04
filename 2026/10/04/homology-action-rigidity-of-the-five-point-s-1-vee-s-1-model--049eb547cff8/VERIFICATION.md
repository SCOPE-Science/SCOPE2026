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

The embedded `verify.py` reconstructs the five-point poset with two minima and three maxima and uses the oriented edges
\[
[a,x],[a,y],[a,z],[b,x],[b,y],[b,z].
\]
It checks the cycle basis
\[
c_1=[a,x]-[b,x]+[b,y]-[a,y],
\qquad
c_2=[a,x]-[b,x]+[b,z]-[a,z].
\]

The program then enumerates all \(5^5=3125\) set maps, filters order-preserving maps exactly, computes the induced simplicial chain maps and integral \(H_1\)-matrices, and verifies equality with the explicit union of one zero matrix, \(18\) rank-one outer products, and the \(12\) integral isometries of
\[
q(s,t)=s^2+st+t^2.
\]
It also independently detects order-isomorphisms and compares them with the maps whose homology matrices have determinant \(\pm1\).

Run `python3 verify.py`. The expected output is:

`VERIFY_OK`
`continuous_self_maps=197`
`distinct_H1_matrices=31`
`matrix_types=1_zero+18_rank_one+12_q_isometries`
`map_rank_distribution=149_zero_action+36_rank_one_action+12_isomorphism_action`
`homeomorphisms=12`
`H1_isomorphism_iff_homeomorphism=yes`
`q=x^2+x*y+y^2`

The finite computation is exhaustive for the stated five-point object. Literature comparison and novelty assessment are not machine-certified.
