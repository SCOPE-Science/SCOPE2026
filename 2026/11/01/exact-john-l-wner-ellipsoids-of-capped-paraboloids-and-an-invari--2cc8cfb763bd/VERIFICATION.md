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
# Verification record

The included `verify.py` uses Python 3 with NumPy and SciPy. Run `python verify.py` in the extracted artifact directory. It checks numerical instances of the exact John containment identity, the endpoints of the Löwner convex quadratic envelope, and the algebraic contact moments of the normalized contact points. It tests 10 dimensions, 10,001 axial locations per dimension for each ellipsoid, and solves eight independently initialized constrained three-parameter optimizations in dimensions \(2,3,5,8\). A successful execution reported a largest discrepancy of \(2.43\times10^{-14}\) for the polynomial identity and a largest numerical optimization-relative parameter discrepancy below \(3.85\times10^{-8}\).

The proof uses two identities valid for all integer dimensions \(d\ge2\), independently of sampling: (i) the John squared-radius gap is a nonnegative perfect square; and (ii) the Löwner bound is a convex function with both endpoint values one. The two positive finite isotropic contact designs certify global optimality and uniqueness, including nonsymmetric competitors. Numerical tests do not imply universal mathematical truth, and no external or independent audit has been performed.
