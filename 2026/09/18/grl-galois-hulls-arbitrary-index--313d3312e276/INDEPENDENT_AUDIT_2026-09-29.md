# Independent Audit — Full-field generalized Roth--Lempel Galois hulls for arbitrary indices

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `b00cac76ba637abd2b76c72376cdf2c83129f780`  
**Audited current source tree:** `b00cac76ba637abd2b76c72376cdf2c83129f780`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree is unchanged from the dispatcher-audited source tree. GitHub was used read-only as evidence; this audit file is staged by the ledger change-set and is not claimed to be already published.

## Correctness — PASSED

PASS. The full-evaluation normalization is valid: for P(x)=x^q-x, P'(a)=-1 at every a∈F_q, so all Lagrange coefficients are u_a=-1. Choosing z=k-s-h scaled coordinates with multiplier β satisfying β^(Q+1)≠1 makes the hull equation force exactly z roots after the root-count identity g=-f^Q. In the strict range Q(k-1)<q-k, the coefficient tail vanishes and arbitrary nonsingular A_s forces the top s coefficients of f to vanish. At the equality boundary, the submitted scalar A_s=μI_s with μ^(Q+1)≠1 correctly kills the remaining top coefficient. For s=2, the AMDS criterion is also met at the boundary because 0 lies in the required distinct-sum set, so the scalar matrix satisfies the source paper's general distance condition. The supplied GF(8) and GF(27) checks agree with the algebra, including indices excluded by 2ℓ|e.

## Originality — PASSED

PASS, narrowly scoped. Wu--Liu--Chen--Zhou's September 2026 GRL hull construction imposes 2ℓ|e in its main full-evaluation hull theorem, because its general normalization invokes (p^ℓ+1)-st roots of Lagrange data. The submitted full-field observation u_a=-1 bypasses that obstruction and extends the GRL q+s construction, especially the q+2 AMDS/NMDS family, to every Galois index 1≤ℓ≤e-1. Earlier arbitrary-index GRS/EGRS hull results and Hermitian Roth--Lempel results do not by themselves contain this GRL full-evaluation extension.

## Scientific value — PASSED

PASS. The result removes a substantive arithmetic divisibility hypothesis from a very recent GRL hull theorem while preserving prescribed hull dimensions, the length-q+2 AMDS/NMDS specialization, and the associated EAQECC parameters. The improvement is source-specific rather than a new general theory of Galois hulls, but it is a meaningful extension with explicit finite-field checks.

## Independent checks

- Re-derived P'(a)=-1 and the full-field Lagrange coefficient normalization.
- Re-checked the root-count inequality in both the strict and equality boundary cases.
- Checked the scalar-boundary coefficient-tail equation and the source paper's general s=2 AMDS criterion.
- Inspected the included finite-field verifier and its GF(8)/GF(27) outputs as consistency evidence, without relying on them as the proof.
- Compared the claim against arXiv:2609.20453 and nearby arbitrary-index GRS/EGRS and Hermitian Roth--Lempel literature.
- Verified no file under this assigned record changed between the dispatcher source-check commit and current audited main.

## Limitations

- The construction uses the complete evaluation set F_q and does not remove divisibility hypotheses from every evaluation-set construction in the motivating paper.
- At the largest equality-boundary k, the proof uses a scalar extension matrix rather than an arbitrary prescribed A_s.
- The motivating preprint is extremely recent, so contemporaneous unindexed work remains a residual priority risk.

## Evidence and references

- https://arxiv.org/abs/2609.20453
- https://arxiv.org/abs/2412.05011
- https://arxiv.org/abs/2604.11350
- https://arxiv.org/abs/2207.07792
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/grl-galois-hulls-arbitrary-index--313d3312e276

This change set updates only the independent-audit channel. Lean verification and expert attestation are preserved exactly as previously recorded.
