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

# Verification and reproducibility

The three included scripts should be run from the directory containing them:

```sh
python3 verify_orbits.py
python3 verify_group.py
python3 verify_geometry.py
```

Python 3.9 or later is sufficient for the two finite-group scripts. The geometric script requires SymPy; all field and Gröbner computations explicitly use modulus \(2\), without floating point.

`verify_orbits.py` constructs the degree-four binary point-vanishing kernel directly from all fifteen nonzero vectors, quotients by the four multiples of \(G\), and enumerates all \(2^{16}=65536\) classes. It generates the action of the fifteen symplectic transvections and reports \(128\) orbits in total and exactly two rationally smooth orbits of size \(144\), with representatives `13387` and `13394` in the program’s deterministic basis. The direct gradient filter checks all classes, not just representatives.

`verify_group.py` enumerates exactly \(720\) binary symplectic matrices, checks that the orbit of the smooth representative has size \(144\), and checks the stabilizer has exactly five matrices. It verifies the exhibited generator has order five and that \(F(Ax)+F(x)=YG(x)\).

`verify_geometry.py` checks that the projective singularity ideal of the good representative is the unit ideal in every one of four affine charts, by exact Gröbner basis calculations. For the other representative, it verifies a singular point over the degree-five extension defined by \(T^5+T^3+T^2+T+1\); its coordinates are explicitly given in the proof. These checks distinguish geometric from merely rational smoothness.

Expected success markers: `ORBIT_VERIFY_OK`, `GROUP_VERIFY_OK`, and `GEOMETRY_VERIFY_OK`.

The proof of connectedness and the genus and ramification formulas use standard complete-intersection and tame-quotient results, not finite experiments. The scripts certify the stated finite classifications and polynomial identities; no abstract automorphism classification or independent external validation is claimed.
