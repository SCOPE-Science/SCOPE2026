---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For the ordinary unitary two-dimensional irrep pi(r)=diag(zeta^k,zeta^-k), pi(s)=swap, normalized vector and 2n group-element-labelled projectors, Pauli coordinates give identity eigenvalue n. Rotations/reflections cancel cross terms. For order ell=ord(zeta^{2k})>2 the traceless eigenvalues are nd^2,2n|c|^2 twice; at ell=2 they are nd^2,4n(Re c)^2,4n(Im c)^2. Their trace is n, hence min <=n/3; equality is attained precisely at d^2=1/3, and additionally phase arg c ≡pi/4 mod pi/2 if ell=2. Exceptional iff n divisible 4,k=n/4. Tight operator identity implies rank-one complex projective 2-design with multiplicity and condition number sqrt3. Independent direct orbit projector four-dimensional Gram matrices at (n,k)=(5,1),(8,2),(12,2),(6,1) reproduced eigenvalues n/3,n/3,n/3,n (within floating precision), including exceptional locked phase.

## originality

PASS

The earlier published two-dimensional dihedral maximal-spanning vectors result classifies whether the orbit spans operators, not the complete singular spectrum or sharp optimum/equality locus. Scott 2006 establishes universal equivalence of tight IC POVMs to complex projective 2-designs, but it does not determine which dihedral fiducials realize it. A broader Cheng 2025 phase-retrievability article remains unread and a residual risk.

## value

PASS

Stable Hermitian matrix recovery under strongly structured group-orbit measurements is a natural optimal experimental-design problem. The exact spectral family identifies all optimal dihedral fiducials, including the exceptional inability of real relative phases to recover a full matrix, not merely existing qualitative phase retrievability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
