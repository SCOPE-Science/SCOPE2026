---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Correct for all primes p including 2 and all b>=1. For b>=2, every additive endomorphism has unique coordinates (u,v,p^{b-1}w,z), u,v,w mod p and z mod p^b. Squaring forces u=0 and z=0 mod p, leaving z^2+p^{b-1}vw=0 mod p^b. At b=2s all allowed z are divisible p^s and vw=0, with (2p-1)p^s maps. At b=2s+1, ordinary valuation >=s+1 plus cancellation valuation exactly s with vw=-t^2 gives p^{s+2} total. Generator images (0,p^{b-1}w),(v,z) always span cyclic group: for |z|>=p^2 the first lies in cyclic group of second, and for |z|<=p, vw=0. Sorting orders yields c0=1, c1=(p-1)(2p+1), middle c_j=(p-1)(2p-1)p^{j-1}, odd top (p-1)^2p^s, b=1 homogeneous 1+p^2-1. Independent exhaustive image-subgroup enumeration checks p,b=(2,1),(2,3),(3,2),(3,3),(2,4),(2,5) and their order histograms; not used to extrapolate to all b,p.

## originality

PASS

PASS, best of knowledge: The inspected primary statements and closest published mathematical findings are compared by exact objects, quantifiers and implications, not titles. The noted theorem has specific proof ingredients/coverage beyond what the cited prior claims imply. The listed inaccessible or uninspected material is a residual priority risk, not automatically a failed originality proof.

## value

PASS

PASS: Square-zero endomorphisms naturally define differentials on the elementary mixed-rank primary module C_p⊕C_{p^b}. Their exact image-order stratification (not merely total number), cyclic-image constraint and odd-exponent cancellation are useful structural invariants for differential classifications and contrast homogeneous rank-two vector spaces. This family is the first nonhomogeneous two-generator p-group, not an arbitrary small slice or a pure normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
