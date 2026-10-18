---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS. Counting-measure Schur orthogonality identifies the standard coefficient block with End(V), norm factor (n−1)/n!. Conjugacy-class averaging commutes with conjugation and the multiplicity-free End(V) decomposition [n]⊕[n−1,1]⊕[n−2,2]⊕[n−2,1,1]. Scalar, centered fixed-point diagonal, and skew-symmetric projection squared norms are R0=(f−1)²/(n−1), R1=f(n−f)/(n−2), R3=(n−f−2t)/2; the orthogonal residual is R2≥0. Each orbit-frame sector eigenvalue is (n−1)M/n!·Rj/Dj, with coincident/zero levels retained. Rank requires R0,R1,R2,R3>0; the algebraic factorization of R2 and n=4 cycle types gives exact stated injectivity criterion. Independent orthonormal-matrix numerical enumeration of all conjugacy classes for n=4,5,6 reproduced eigenvalues/multiplicities. General C relies on the representation proof, not finitely many classes.

## originality

PASS

Known ordered-pair representation decompositions and group Fourier frame identities provide the toolkit, while published exact spectra for isolated three-cycle or transposition sampling cover special classes only. Neither inspected general theorem implies the universal cycle-type (f,t) law, all-sector multiplicities and full-rank classification for every conjugacy class of S_n.

## value

PASS

PASS. Exact singular values and rank of restricting a full irreducible Fourier coefficient block to a conjugacy class determine stable group sampling and reconstructability. Reduction to only two cycle statistics despite class size depending on full cycle type is a natural structural classification, not a trivial substitution; it extends beyond isolated class results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
