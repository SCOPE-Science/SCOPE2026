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

The exact algebraic bottleneck is the \(2+2\) coefficient-sign case. With
\[
\alpha=\frac{1+u}{2},\quad
\beta=\frac{1-u}{2},\quad
\gamma=\frac{1-v}{2},\quad
\delta=\frac{1+v}{2},
\]
where \(0\le u,v<1\), the projected section quadrilateral has vertices
\[
(0,0),\quad
\left(\frac{1+v}{2+u+v},0\right),\quad
\left(\frac{1-v}{2+u-v},\frac{1+u}{2+u-v}\right),\quad
\left(0,\frac{1-u}{2-u-v}\right).
\]
The packaged `verify.py` computes its area centroid exactly and clears the denominators in the equations requiring both displayed coordinates to equal \(1/4\). It reconstructs the two polynomials used in the proof and then evaluates their exact symbolic resultant with respect to \(v\):
\[
16384u^3(u-1)^6(u+1)^9(3u^2-4).
\]
It verifies separately that
\[
P(0,v)=v^2(3v^2-4).
\]
Thus the admissible common zero is exactly \((u,v)=(0,0)\).

The checker also verifies the scalar equation in the \(1+3\) case and the combinatorial count of four singleton-versus-triple partitions plus three pair-versus-pair partitions.

The replay output is:

`VERIFY_OK tetrahedron seven centroidal sections`

The checker uses exact symbolic arithmetic. It is not an exhaustive numerical search, and no finite sampling is used to justify the universal quantifier over planes.
