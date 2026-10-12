---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The universal argument is mathematical rather than experimental. Its critical inputs are: the sextic is absolutely irreducible; its normalization is a genus-five Howe curve; the source proves that the central singularity is a node; Proposition 4.2.6 gives exactly one further sign-symmetric pair in Cases II and III; and the local equation is even in the transverse sign coordinate. These imply total \(\delta\)-defect \(5\), hence \(\delta=2\) at each noncentral point.

For Case III, formal splitting in the direction with nonzero quadratic coefficient produces \(U^2-h(V)\). Uniqueness of the formal critical section and sign symmetry make \(h\) even. Since \(\delta(U^2-h(V))=\lfloor\operatorname{ord}(h)/2\rfloor\), the source's lower bound \(\operatorname{ord}(h)\ge4\) together with \(\delta=2\) gives exact order \(4\), hence \(A_3\).

For Case II, `verify.py` symbolically checks that the second system in Lemma 4.2.2 makes the cubic \(P(s)\) have a triple root. At an infinity point this would produce an \(A_2\) cusp because the point is multiplicity two and the other local coordinate occurs only in even powers, contradicting \(\delta=2\). In the surviving double-root case, the same parity and defect argument gives \(A_3\).

The script also checks the paper's explicit Case-II example over \(\mathbb F_{31}\). Its completed-square transverse quartic coefficient is nonzero, providing a concrete exact replay of the tacnode behavior. This example is not used to infer the universal statement.

The replay used SymPy 1.14.0 after inspecting its installed package source. No assertion is made for characteristics \(2,3,5\) or for five-singularity models.
