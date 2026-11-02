---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

PASS: The idempotent equation in the specified evolution basis is x=A^T x^[2]. For invertible M=A^T, classical Lang/semilinear normal form M=B(B^[2])^-1 over the algebraic closure turns fixed points into B(F2^n), exactly 2^n geometric idempotents. Frobenius_q descent C=B^-1 B^[q] lies in GL_n(F2) and counts rational idempotents as 2^dim ker(C-I). A rational twisted-conjugacy orbit of M corresponds to a binary conjugacy class [C] and has stabilizer |Z_GL_n(F2)(C)|; hence uniform M produces the uniform binary matrix C conjugacy-class law. Möbius inversion on binary subspace lattice gives N_{n,k}= [n choose k]_2 Σ_{j=0}^{n-k}(-1)^j 2^{j choose 2}[n-k choose j]_2 2^{(k+j)(n-k-j)}|GL_{n-k-j}(F2)|. Independently enumerated all invertible binary matrices n=1,2,3: fixed-point count histograms respectively {2:1}, {1:2,2:3,4:1}, {1:48,2:98,4:21,8:1}. These agree with the formula; all extension degrees and n follow from the proof, not finite tests.

## originality

PASS

PASS (qualified): earlier works cover classical Lang/semilinear normalization, evolution algebra isomorphism classes and the average nonzero idempotent count. The uniform-matrix full distribution independent of extension degree and binary fixed-space law is a sharper separate statement. Any equivalent random semilinear matrix orbit theorem remains a risk.

## value

PASS

PASS: Rational idempotent elements form a central invariant of a perfect evolution algebra. This all-n complete probability law over all 2-power fields, including nontrivial extension-degree invariance and exact k-frequencies, goes beyond the already published mean or existence statement; the binary descent makes a structural arithmetic prediction useful in finite-algebra experiments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
