---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The stationary flows have fixed pair sums ell_i opposite state i and a common oriented current j by conservation, exhausting the feasible matrices for |j|<=J. The two directed-triangle determinant terms give det P=(ell_1 ell_2 ell_3+j^2)/(4u); trace zero and the stationary root give residual discriminant (g-j^2)/u. Reversibility at j=0 makes g>=0, and g=0 forces uniform pi by the diagonal of the two-eigenvalue spectral decomposition. For pi=(p,q,r), ell_2 ell_3=-J+4qr, hence J^2-g=(4-9p)qr. The radius is strictly decreasing in j^2 up to g and increasing beyond it, so the exact optimizer has j^2=min(g,J^2). This gives the claimed 4/9 frontier, both branches, all sign choices and the uniform merger. The oriented triangle in the sign direction of j is positive, and some two-cycle is positive at every optimizer (the only possible loss of all reverse edges is a uniform-law endpoint, not optimal); this gives primitivity. A diagonalizable double root -1/2 would force P=-I/2+3(1 pi)/2 and hence uniform pi, proving the nonuniform Jordan claim. Independent exact examples at p=2/5, 4/9 and 9/20 verify existence of the real/complex split, equality at the frontier, and optimal radii 1/2, 1/2 and 2/3 respectively.

## originality

PASS

Credit the exact stationary-concentration threshold and minimizers for the joint constraints of prescribed stationary probabilities and zero diagonal without reversibility. The unrestricted trace bound and reversible stationary-flow representation are not credited as new. No inspected comparison covers the sharp prescribed-law optimization or its equality classification.

## value

PASS

Prescribing the stationary law and prohibiting self-loops are natural joint constraints for a transition design. The result determines exactly when the trace obstruction is attainable, where complex spectra can occur, and when the spectrally best design is necessarily defective. The latter warns against interpreting optimally small eigenvalue modulus as a uniform finite-time mixing guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
