---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The source Theorem 3.9 generator is [I_n | G_D], D={x∈F_3^n:x1∈{0,1}}\{0}, n>=3, length n+2*3^(n-1)-1. For r-message subspace U, annihilator W=U^perp of dimension h=n-r, the zero coordinates equal |D∩W|+s(W), with s the number of standard axes in W. If W lies in A={x1=0}, |D∩W|=3^h-1; otherwise a nonzero first-coordinate map has fibers each 3^(h-1), so |D∩W|=2*3^(h-1)-1. Inclusion-exclusion over coordinate axes gives E_{m,h}(s)=C(m,s)Σ_j(-1)^j C(m-s,j)[m-s-j choose h-s-j]_3; contained W count E_{n-1,h}(s), noncontained difference E_{n,h}(s)-E_{n-1,h}(s). The former regime dominates minimum-support minimization, giving d_r=r+2*3^(n-1)-3^(n-r), exactly C(n-1,r-1) minimizers, even h=0 boundary. Independently enumerated ALL subspaces via a separate reduced-row-echelon generator for n=3,4 and matched every support histogram, including n=3 (10:1,13:2,14:6,15:4) at r=1. The all-n proof uses geometry and exact Gaussian-binomial inclusion-exclusion, not a finite inference.

## originality

PASS

Mondal–Lee Theorem 3.9 and Example 3.10 give code parameters and ordinary codeword weight distribution but not all r-subcode-support spectra. A separately published Resultary theorem on systematic full-simplex ternary code instead covers Mondal–Lee Theorem 3.7, whose generator includes every nonzero column, not two x1-slices. Its d_r=3^n-3^(n-r)+r differs from audited half-space d_r=r+2*3^(n-1)-3^(n-r). Pan–Chen–Liu–Liu and Li–Chen–Qu discuss GHW or subcode supports for other defining sets, and their general intersection technology does not evaluate this exact two-regime construction plus identity columns. Residual risk is a disguised equivalent affine family.

## value

PASS

Subcode support-size distributions refine ordinary weight enumerators and generalized distances, naturally answering a structural question about a recently introduced LCD code family at ALL dimensions, not a tiny arbitrary instance. The precise two-slice geometry creates two annihilator regimes and exact multiplicities; the generalized Hamming hierarchy and minimizer counts are consequences. Such spectra are independently useful for higher-weight and reliability studies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
