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

Run `python3 verify.py`. The verifier contains the forty tetrahedra from the cited primary source and uses only exact bit-vector linear algebra over \(\mathbf F_2\).

It checks:

- face vector \( (11,51,80,40) \);
- \(\dim H_1(K;\mathbf F_2)=1\);
- the explicit 17-edge cocycle vanishes on every triangular boundary and is not a coboundary;
- exactly 55 empty triangles occur and every one pairs nontrivially with that cocycle;
- all 2048 vertex subsets by both cocycle evaluation and a quotient-rank computation of their image in global \(H_1\);
- equivalence between nonzero global image and containment of a generator triangle;
- the complete support and independence counts;
- closure of the three published automorphism generators to 48 facet-preserving permutations, and the stated orbit sizes.

The finite exhaustive verifier proves only the stated complex and coefficient field. It does not extrapolate to other triangulations or coefficient systems.

Expected terminal output:

`VERIFY_OK f=11,51,80,40 H1=1 generator_triangles=55 support=3:55,4:242,5:442,6:462,7:330,8:165,9:55,10:11,11:1 independent=0:1,1:11,2:55,3:110,4:88,5:20 aut=48 gen_orbits=3,4,12,12,24 exceptional5_orbits=8,12`
