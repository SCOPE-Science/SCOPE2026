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

# Verification of the full binary Perazzo Jacobian calculation

The proof is symbolic for **every** integer \(m\ge3\) over characteristic-zero fields. First, direct differentiation yields \((U,V)^m\) and the two remaining degree-\(m\) relations. Grading by \((U,V)\)-degree isolates an exact two-column graded presentation of the top layer; a nonzero minor proves injectivity. Binomial-coordinate rescaling identifies the rank-drop ideal with the rational normal curve Hankel minors of height \(m-1\ge2\). Local depth over the regular polynomial subring \(S\) proves torsion-freeness and primaryness; the same presentation computes Hilbert, depth and the non-Cohen--Macaulay locus. For \(m=3\), Hilbert--Burch identifies the top layer with the twisted-cubic ideal sheaf.

To corroborate the algebra, execute `python3 VERIFY_COMPUTATION.py` in the same directory. This source uses only the Python 3 standard library, constructs the entire homogeneous Jacobian space in each tested degree, computes its rank by sparse modular elimination for primes \(1000003\) and \(1000033\), and checks the predicted Hilbert dimensions in degrees \(m,m+1,m+2,m+3\) for \(m=3,4,5\). It also tests rank-one Veronese specializations of the derivative matrix. The recorded output ended with `VERIFY_OK 27`; the twelve Hilbert numbers, ordered by \(m=3\), \(4\), \(5\), were respectively \((50,97,166,261)\), \((203,421,782,1338)\), and \((784,1661,3214,5783)\).

Finite modular experiments cannot prove an infinite characteristic-zero family. The proof of the prime ideal, exact module decomposition and non-Cohen--Macaulay locus relies on the explicit algebraic reasoning in `RESULT.md`. This package contains no external independent audit or formal machine proof. The singularity assertions refer to the ordinary Jacobian scheme and not the Artinian apolar quotient.
