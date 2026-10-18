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

Both first Krylov spaces equal span(g) with g=A^Tb and B=A^TA positive definite. Minimizing the primal residual b−tAg gives t_Q=s0/s1, while minimizing normal residual g−tBg gives t_M=s1/s2, where sj=g^TB^j g. Their squared normal residuals share determinant Δ=s0*s2−s1²: ||q_Q||²=s0Δ/s1², ||q_M||²=Δ/s2; hence if Δ>0 their ratio is sqrt(s0*s2)/s1. For eigenvalues of B in [m,M], the scalar bound λ²≤(m+M)λ−mM and endpoint optimizing mean give ratio ≤(M+m)/(2sqrt(mM))=(κ²+1)/(2κ). Cauchy–Schwarz gives lower 1. The A=diag(1,κ), g=(κ,1) example realizes upper equality. Independently rationally checked κ=3: the first-step LSQR and LSMR normal residual factors are 4/3 and 4/5, with ratio 5/3. In eigenvector case Δ=0, both methods solve the mode and the ratio is not defined; bounds are stated only for nonzero residuals.

## originality

PASS

Classical Paige–Saunders LSQR is CG on normal equations and minimizes the first-step primal residual, while Fong–Saunders LSMR is MINRES on normal equations and minimizes the normal residual. The sharp Kantorovich RMS/mean spectral inequality itself is classical. The mathematical difference asserted here is their exact algorithm-specific first-step normal-residual ratio, a sharp attainable condition-number envelope, and precise onset κ>1+sqrt2 of LSQR normal-residual increase while LSMR decreases. The primary LSMR article and Hallman–Gu LSMB comparison address early stopping and related iterates but no exact same factor was seen in accessible portions. A hidden classical CG/MINRES first-step lemma is the main residual risk, not falsely excluded by an abstract search.

## value

PASS

The natural early-termination question is the quantitatively sharp disadvantage of LSQR versus LSMR on the stationarity/normal residual after a single iteration. The exact condition-number envelope and sharp κ=1+sqrt2 onset of LSQR residual growth give a reproducible algorithm-selection diagnostic; this precise tight solver comparison can be useful despite its short proof from classical Krylov and Kantorovich facts. No general later-step advance is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
