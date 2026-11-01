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

For the specified genus-two Weierstrass curve z^2=f_5(x) with monic squarefree quintic, Weierstrass pole semigroup <2,5>, A=O(p) and the nonzero class represented by t^-3, the displayed nonlinear gluing gives b_q=sum_{j=2}^q binom(q-1,j-1) f_j t^(3j-2q). The finite leading jets of P,Q,R,S,H are regular in the W chart: t^3 z=x^6/f5(x)=x+O(1); all subsequent principal parts lift because H^1(C,O(qp))=0 for q>=3. Direct multiplication has PS-QR vanishing at order 5 and leading -z at order 6. Alongside T^2,X,T^3,TX,Z this yields TZ, the sixth homogeneous generator of gr_F(Rhat)=C+sum_{j>=2}H^0(O(jp)); a weighted semigroup proof covers every degree and the complete-filtered lifting lemma gives a surjection from five formal variables. Park-Shin Lemma 8.2/Prop 8.6 provide the lower bound 5, hence exact edim 5. Serre-duality pairing Res_p(t^-3 dx/z)=-2 is nonzero. These arguments concern completion and specified analytic contraction, not convergence of ad hoc series on a fixed punctured chart. Independent finite calculations checked the cancellation and all basis monomials through degree 60; not an infinite proof.

## originality

PASS

Best-of-knowledge: Park-Shin arXiv:2610.21093 proves the nonlinear contraction and an edim lower bound 5, not equality; its graded algebra and lifting lemma do not automatically provide five analytic lifts. The independently inspected Fujiki Section 5 treats affine bundles, orbit closures, and obstruction kernels, not an exact five-generator embedding dimension theorem. The surviving precise claim is the explicit cancellation PS-QR reducing six initial homogeneous classes to five formal generators. Grauert 1962 full text remains inaccessible (authorized access reported a disconnected VPN), so older implicit coverage is retained as a genuine priority risk.

## value

PASS

Embedding dimension is the canonical minimal local embedding-space dimension of a normal surface singularity. The existing sharp lower bound for a natural genus-two, Wahl-defect-zero nonlinear family did not determine whether the singularities are embeddable in five versus six dimensions. The explicit cancellation settles this exact invariant across all monic squarefree quintics and situates the family just beyond the codimension-two dimension-four context. It is not a routine restatement of the lower bound nor a claimed general higher-genus classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
