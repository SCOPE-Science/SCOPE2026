---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Rank-one purity of every successful output forces each contributing product Kraus A⊗B to map the three-dimensional antisymmetric support into the target line. A nonzero contributing branch has rank A=rank B=2 with a common one-dimensional kernel; otherwise an antisymmetric input involving a kernel vector would map to a nonzero product vector in an entangled target line. On the common two-plane, writing X=A†A and Y=B†B gives |alpha|^2=(TrX TrY-Tr(XY))/2. The matrix equation for the antisymmetric vector and Schatten Hölder gives TrX TrY>=2|alpha|^2(c+s)^2, hence Tr(XY)>=2 sin(2theta)|alpha|^2. Summing success effects E and using that the separable failure effect R=I-E has nonnegative trace pairing with the swap F yields 3=TrF>=Tr(FE)>=2 sin(2theta) sum|alpha|^2. Since each branch succeeds on P_-/3 with probability |alpha|^2/3, p<=1/[2 sin(2theta)]. The six explicit ordered-pair product Kraus operators in RESULT.md attain p=min{1,1/[2 sin(2theta)]}; their summed effect is diagonal with coefficients at most one and the diagonal complement is a separable failure effect. Boundary theta=pi/4 gives 1/2 and sin(2theta)=1/2 joins the deterministic branch continuously.

## originality

PASS

Akibue--Miyazaki--Osaka study exactly this distillation family. Their full 2026 article constructs the same lower-bound protocol with success min{1,[2 sin(2theta)]^{-1}} for all phases/weights, formulates the exact SEP conic problem, and for the uniform antisymmetric benchmark reports that the strengthened numerical hierarchy indicates the protocol is optimal. It does not provide an analytic upper bound proving equality. Chitambar--Duan establish separable-operation advantages for different mixed-to-pure transformations. No checked source supplies the swap-witness analytic optimum for the uniform rank-three antisymmetric qutrit state.

## value

PASS

The exact SEP frontier resolves a concrete benchmark for which the motivating 2026 paper supplied an achievable curve and strengthened numerical evidence but no analytic optimality proof. A closed one-copy conversion frontier for a canonical antisymmetric state is a natural resource-theory invariant and the swap-witness upper bound is reusable structural mathematics rather than a mere numerical certification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
