---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The fixed quartic threefold is smooth as established by primary references. Diagonal weights a=(1,-3,9,-27,81) mod61 preserve every monomial x_i^3 x_(i+1) and have determinant 1. Griffiths residue/Jacobian-ring identification H^{2,1}=R_3 gives 35 degree-three monomials and five independent cubic derivative relations of distinct characters, leaving exactly 30 distinct nonzero characters Phi, disjoint from -Phi, which together exhaust all 60 nonzero residue characters. Thus H^3(Q)(1) has cyclotomic characteristic polynomial Phi_61 and dimension one over K=Q(zeta61). Direct exhaustive exact modular arithmetic checks all 60 multipliers and finds stabilizer of Phi exactly <−3>={1,9,20,34,58}; its six orbits give an induced primitive CM type for the CM field L=K^H of degree12. The Hodge decomposition over L is five copies of the rank-one L CM Hodge structure; classical CM theory gives a simple sixfold A and J~_C A^5, End^0(J)~M_5(L), rational dimension 300. The conclusion is an unpolarized isogeny classification only. Independently re-enumerated monomial characters and all multiplier/coset cases from the fetched source, and reconstructed the Hodge/CM deductions rather than assuming verifier exit codes.

## originality

PASS

Best-of-knowledge distinct exact unpolarized isogeny and rational endomorphism algebra for the natural 30-dimensional intermediate Jacobian. The general Hodge spectrum of González-Aguilera et al. and CM isogeny classification of Milne are explicitly known and credited. Their conjunction makes this result an accessible special-case structural deduction, so its novelty lies only in the verified exact type stabilizer and resulting specific simple factor, not the preexisting general theorems; priority risk is substantial and recorded, not misrepresented as proof of novelty. Searches and inspected principal statements found no earlier explicit exact A^5/M5(L) classification.

## value

PASS

The complete rational isogeny type and endomorphism algebra of the distinguished smooth Klein quartic threefold intermediate Jacobian are canonical and potentially reusable Hodge-geometric invariants. Determining its non-simplicity, exact simple dimension-six CM factor, fifth-power multiplicity, field-of-endomorphisms L of degree12 and rational matrix-algebra dimension300 is a substantive structural classification rather than an arbitrary numerical slice or mere verification of the symmetry group. This value does not require a general new CM theorem; its modest dependence on known spectral theory is disclosed and originality is limited to the exact computed specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
