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

For rank-two PSD A=diag(a,b,0,...), Gaussian sketch q=Ag/||Ag|| leaves a rank-one residual eigenvalue r=ab/(a+b)[1+ab/(a²cos²theta+b²sin²theta)]. An independent Gaussian probe gives centered error r(Z²−1) with Z independent of r, making overestimate probability P(Z²>1) universal. The exact angular integrals E[1/D]=1/(ab), E[1/D²]=(a²+b²)/(2a³b³) give Var(T++)=ab(a²+6ab+b²)/(a+b)², versus 2(a²+b²)/3 for three Hutchinson probes. The difference has palindromic quartic 2t⁴+t³−14t²+t+2 and unique t≥1 threshold 2.331488011135..., with both variance signs. Dominated convergence under A→A0 in fixed dimension gives nearby positive-definite persistence. Independent Sympy rational verification and threshold calculation support, not replace, infinite proof.

## originality

PASS

Best-of-knowledge: the established general Hutch++ conditional variance formula, Gaussian probe baseline, and broad query bounds are credited. Neither inspected primary paper evaluates the two-dimensional Gaussian-sketch angular residual second moment to obtain the closed equal-three-product variance difference or its unique eigenvalue-ratio crossover. Priority uncertainty remains explicitly recorded.

## value

PASS

This natural minimum-cost three-matvec allocation compares two widely used Gaussian trace estimators. The exact spectral transition shows when one random deflation is worse than allocating every query to independent probes, and when it becomes better, with stable full-rank sign regimes. It is an informative method-selection benchmark, explicitly not a universal query-optimality statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
