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

# Mathematical verification

To reproduce the classification, compile and execute the standalone C++ exhaustive witness/classifier, then run the three separate Python checks from the folder containing all embedded files:

```sh
g++ -O3 -std=c++17 quartic_census.cpp -o quartic_census
./quartic_census
python3 quartic_profiles.py
python3 verify_certificates.py
python3 check_orbits_sympy.py
```

The last checker uses SymPy 1.14.0; the others use only the Python standard library and a C++17 compiler. The finite-field library in the witness verifier is separate from the C++ singular-point search; it checks all 21,847 recorded witnesses over fields up to \(\mathbf F_{16}\). The geometric smoothness of every retained quartic is certified by the dehomogenized Jacobian ideal containing \(1\) in each of three affine charts for every one of the 78 projective orbit representatives. This is a proof of geometric smoothness, unlike simply failing to find singularities at small extension degrees. Every one of 32,767 nonzero masks is covered by either the certified singular or certified smooth collection, with no overlap.

The exact line-restriction condition is \(a_1=a_3=0\) for a binary quartic restriction \(\sum_{j=0}^{4}a_js^{4-j}t^j\), and the unique contact quadratic \(Q_L=a_0s^2+a_2st+a_4t^2\) is checked at all three rational points of each line. Each of 10,920 geometrically smooth equation masks is assigned one joint contact profile. Independently, a SymPy substitution rechecks the line restriction and contact classification on all 78 orbit representatives, and group-equivariance transfers it to the full 10,920 equation list. The complete orbit catalogue and 40-cell frequency table are embedded.

The programs above were actually executed from the package's file directory, and their outputs agreed with 10,920 smooth, 21,847 certified singular, 78 ambient projective orbits and 40 joint contact profiles. The 78-orbit count agrees with the independent published Nart--Ritzenthaler isomorphism count; that agreement is corroboration, not a novelty claim. The check does not search arbitrary extensions for new classes beyond the fixed binary field, nor constitute external peer review.
