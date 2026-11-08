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

For m>=3, a>0, -1/(m-1)<b<1 and m a²<c=1+(m−1)b, write e=1−b. All unrestricted positive diagonal congruences DAD are addressed via equivalence κ(DAD)<=k iff some positive diagonal W satisfies W<=A<=kW; averaging feasible W over permutations of m leaves gives a symmetric optimum without assuming symmetry upfront. Symmetric scaling diag(sqrt x,1,…,1) gives leaf-difference eigenvalue e (mult m−1) and a 2x2 plane block T(x)=[[x,sqrt(mx)a],[sqrt(mx)a,c]], with strictly increasing eigenvalues λ± and λ+ /λ− uniquely minimized at x=c. Whether e lies inside the λ± interval at x=c gives phase condition a²c>=mb²; otherwise unique crossing at x=b(1−b)/(b−a²). The sharp κ values follow from the extreme eigenvalues. A tight generalized plane eigenvector and PSD null-quadratic-form implication force every unrestricted optimal W to coincide with its leaf average; hence optimizer unique up to common scaling. Setting x=1 gives Jacobi iff b=0 or a²=b², and for fixed 0<a²<b<1 the branch changes at m_c=a²(1−b)/[b(b−a²)] with x saturation after the threshold. Independent direct Jacobi eigendecomposition and positive-diagonal numerical optimization for five parameter cases matched the closed forms; finite experiments do not establish global uniqueness.

## originality

PASS

Best-of-knowledge PASS: exact result and mathematical object are not established by accessible identified prior statements; reviewed aliases, reductions, stronger coverage and checked data. Distinct original ingredient: two-phase symmetry reduction and rigidity against all independent leaf scales. Residual priority and access risks retained.

## value

PASS

Provides an exact unrestricted optimal congruence preconditioner, a nontrivial strict uniqueness theorem and dimension-dependent saturation transition for a natural positive correlation/hub-leaf covariance family. These precise constants guide conditioning in structured SPD systems; unlike generic SDP formulation this is explicit and fully classified for every m≥3 and all permitted positive/negative correlations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
