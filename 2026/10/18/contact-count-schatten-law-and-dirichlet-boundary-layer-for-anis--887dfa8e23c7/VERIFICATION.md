---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

The degree-n monomial row of R_r:H2(D^d)->A_d sends z^nu to r^nu z^n, while ||z^n||^2=1/binom(n+d-1,d-1); orthogonal homogeneous blocks are rank-one, giving sigma_n^2=h_n(u)/N_n exactly. Dirichlet(1,...,1)-mixture of iid category draws makes composition counts uniform, so sigma_n^2=E prod u_j^A_{n,j} decreases with n. Factoring prod(1-u_j z)^-1 at the maximal poles gives k unit-radius polynomial asymptotic and k=0 exponential decay, hence contact-count Schatten cutoff and k=d coisometry. For scaling radii exp(-t_j/2N), conditional multinomial expectation of exp(-sample-average(t)) compared with exp(-Dirichlet mean) yields nonnegative Jensen gap <= E Var(t|P)/(2N)=sum(t_j-tbar)^2/(2N(d+1)). Uniform log-sum-exp expansion gives +(2N)^-1 E[e^-mu Var(t|P)] plus O(N^-2) on compact t sets. Checked exact rational h_n(u)/N_n for u=(1,1/4,0), degrees 1,2,3,15 independently. Finite checks do not establish asymptotics.

## originality

PASS

Best-of-knowledge the full quantified final claim is not shown covered by the inspected primary statements, including aliases/stronger-theorem comparisons. The known unweighted diagonal map is the all-radius-one limiting case; determining all radii and the boundary layer requires new parametric spectral analysis. Neither gives this fully explicit anisotropic singular sequence or Dirichlet 1/N signed crossover. Similarity of spaces/parameters does not imply the degree-n row norm or sharp Schatten boundary; negative search cannot certify priority. The proposed theorem quantifies all singular values and their contact-count phase and critical scaling, not a corollary of range existence. Inaccessible relevant full text is explicitly a residual risk; absence from a database alone is not novelty proof.

## value

PASS

This is a complete and natural approximation-number/compactness/Schatten phase diagram for a canonical trace from a polydisc Hardy space to its diagonal Bergman line. The sharp count of boundary-contact coordinates and the signed 1/N Dirichlet crossover quantify a nontrivial regime not supplied by mere boundedness or range results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
