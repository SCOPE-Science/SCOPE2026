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

PASS, qualified on cited prior formula: Taking the given published Dirichlet expansion F_m(s)=sum_L m! S(L-1,m-1)(zeta(s)-1)^L, exact Stirling generating algebra reduces it to m!z^m/prod_{1<=j<m}(1-jz), z=zeta(s)-1. Distinct simple real poles at rho_j>1 with zeta(rho_j)=1+1/j have computed residues; zeta(s) is vertically almost periodic on Re(s)>1 by simultaneous prime-phase recurrence and absolute convergence. Rouché discs at finitely many rho_j yield a common unbounded sequence of heights with simple poles and converging residues. Strict triangle inequality excludes nonreal poles on Re(s)=rho_{m-1}. Lowry-Duda Theorem 2 (full primary theorem read) converts supremum of nonreal pole real parts to two-sided Omega±(X^{r_m-eps}) for the unsmoothed summatory count; endpoint step values are handled by choosing one-sided limits. Independent finite Stirling checks confirmed algebra, not the infinite analytic argument. Same-source Huxley preprint full PDF inaccessible, so the exact imported Theorem 5.3 remains citation-dependent, not independently reread.

## originality

PASS

Huxley–Lettington–Schmidt supply the sum-system Dirichlet series and leading pole/asymptotic; Lowry-Duda supplies the general nonreal-pole oscillation theorem. The contribution assessed is the simultaneous common-height zeta-level pole/residue replication and its application yielding all-m two-sided sharp error obstruction, not the imported general results or elementary generating-function algebra. Huxley full preprint could not be read due transport and institution VPN limitation; best-of-knowledge priority is qualified, and any decisive overlap would require re-assessment.

## value

PASS

PASS: The singularity structure of a natural arithmetic counting Dirichlet series has a meaningful global asymptotic consequence: *no fixed power saving* past the known leading term, with both signs of error arbitrarily close to the main exponent. The common-height replica ladder gives additional explicit residues for every relevant level and is more than routine evaluation of the leading real pole. The result is dependent on cited general oscillation theory; that use is credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
