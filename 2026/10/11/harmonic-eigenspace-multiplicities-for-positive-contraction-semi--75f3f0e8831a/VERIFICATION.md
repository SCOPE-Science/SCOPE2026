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

For beta=0 the spaces coincide. For beta!=0 set tau=2pi/|beta|, F=Fix(T_tau). Gluck 2021 Theorem 3.1 makes F a Dedekind-complete Banach lattice in its inherited order and norm, without requiring it be a sublattice of E. Restrictions U_s=T_s|F and U_{tau-s} are positive inverse operators, hence lattice automorphisms; choose a/tau irrational. Eigenvectors of U_a with eigenvalue exp(i j beta a) must satisfy U_t x=exp(i j beta t)x by density of nonnegative irrational multiples mod tau and strong continuity; their right derivative yields A x=i j beta x. Thus the eigenspaces agree for every integer j. Apply Gluck 2015 Proposition 3.1(b), whose normalized lattice-power/independence proof compares dimensions of an eigenvalue and its powers. For L1(T) plus L1(T) translations at speeds 1 and 2, Fourier modes give dimension 1 at i and 2 at 2i. This proves exact finite geometric multiplicity inequality, not generalized or approximate eigenspace claims.

## originality

PASS

Gluck 2021 explicitly proposes a semigroup dimension estimate after Corollary 3.5 but refrains because no convenient generator/semigroup multiplicity theorem is available. The audited irrational single-time sampling transfers Gluck 2015 DISCRETE multiplicity inequality to exact generator eigenspaces, genuinely resolving the stated obstacle for the given hypotheses. This is a bounded best-of-knowledge priority assessment.

## value

PASS

A finite geometric-multiplicity upgrade of the established cyclicity theorem directly answers the structural question Gluck 2021 left open for semigroups, and the explicit strictness example shows the inequality has quantitative content beyond eigenvalue existence. A precise reusable fixed-space/sampling lemma bridges discrete lattice homomorphism theory and continuous generators, making the result substantive without claiming broader spectra or a new cyclicity theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
