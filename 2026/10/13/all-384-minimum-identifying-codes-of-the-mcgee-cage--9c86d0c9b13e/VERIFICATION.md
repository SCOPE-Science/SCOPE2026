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

# Exact verification

The finite proof invokes an analytical bound and exact exhaustive computations, all reproducible from the included standalone files. Run `python3 verify.py` with the dependencies in `requirements.txt` and a C++17 compiler. The verifier constructs the McGee graph from the LCF pattern \([12,7,-7]^8\), separately tests \(1{,}961{,}256\) masks of size \(10\) and \(2{,}496{,}144\) masks of size \(11\), and compares direct closed-neighborhood signatures with the logically equivalent \(300\)-set separator formulation for **every** mask tested. The results are zero and \(384\) respectively.

For all \(384\) optimal sets, Python reconstructs the graph independently, checks the closed-neighborhood signatures, enumerates all \(32\) graph automorphisms, and verifies the \(13\) disjoint code orbits with exact expected representatives, sizes, selected-vertex-orbit intersections, and induced edge counts. The check uses integer arithmetic only for the mathematical conditions. The mathematical lower bound \(5|C|\ge48\) excludes every cardinality below \(10\). The verifier does not claim results for other cubic cages or provide an external audit.

Observed successful output:

```text
VERIFY_OK graph=McGee(24,36,girth7) exhaustive_masks=C(24,10)+C(24,11)=4457400
VERIFY_OK gamma_ID=11 optimum_codes=384 independent_conditions=2 automorphisms=32 orbits=13 orbit_sizes=16x2+32x11
VERIFY_OK eight_vertex_orbit=0,3,...,21 orbit_representatives= 600041,697203,1134197,1140085,1219301,1225331,1395303,1395507,1402169,1403187,1462891,1664369,1919283
```
