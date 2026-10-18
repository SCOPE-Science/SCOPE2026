---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Decompose weight w with sum d-1: interior w>=0 exact coefficient ker(lambda_w) if lambda_w≠0 else 0; a boundary w_s=-1 has exact line k e_s if lambda_w≠0 else zero. For anchor r quadratic divergence-free coefficient space ker(1+e_r), predecessor exact space at w-e_r; bracket column lambda_w(a)b-lambda_w(b)a. Every matrix depends only on whether each coordinate is zero/positive and its residue mod p, so a complete all-degree reduction has 50 canonical signatures for p=2 and 108 for p=3 (impossible low-degree signatures excluded). Independently recomputed all finite rank matrices with exhaustive prime-field vector bases: p2 counts 25 interior rank2,21 boundary rank1,four zero; p3 counts 62 interior rank2,42 boundary rank1,four zero; zero rank mismatches. Rank preservation under any same-characteristic field extension proves all fields and all degrees; not merely checking d up to a cutoff.

## originality

PASS

Chao Ma 2026 establishes unrestricted [L2,Ld-1]=E_d in all characteristics, and the stronger restricted-source [L2,E_(d-1)]=E_d for p>=5; the paper explicitly excludes p2,p3 from this stronger theorem. The exact-source predecessor can be a proper subspace, so unrestricted identity does not imply the new low-characteristic recursion. The inspected primary work and semantic search did not establish the claimed dimension-3 small-characteristic result. Priority risk remains for differently titled Cartan-type Lie results.

## value

PASS

The two excluded prime characteristics are precisely the natural gap in a homogeneous exact-source generation theorem; closing both in dimension three gives a characteristic-free statement for that dimension and a complete finite residue-class certificate, a motivated structural lemma rather than a small instance or textbook restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
