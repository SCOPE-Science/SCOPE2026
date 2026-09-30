# Independent audit — 2026-09-29

**Record:** `2026/09/18/scale-thinning-rigidity-centered-maximal-norm--8233a2f0cb72`  
**Disposition:** **PASSED**

## Correctness

**PASS** — The martingale and spatial-realization proof checks out. For q=1-1/B and F=q^{-T/p}, direct conditioning yields the displayed C_m(q), E F^p=n(1-q)+1, and a lower bound whose successive limits are C_infty(q)=(1-q)/(1-q^(1/p')) and then p'. Any radius set with inf R=0 or sup R=infinity contains arbitrarily long chains with the required multiplicative separation. The interval for each digit position P_j has length at least one under rho_j/rho_{j-1}<=delta^2/B^2; past digits are frozen off a set of relative measure O(n delta), future digits average over a period of size at most delta rho_j, and localization plus maximal-operator continuity permits compactly supported smooth approximation.

## Originality

**PASS** — Madrid's September 2026 paper establishes the unrestricted exact norm p' and, according to a detailed current public review, also treats a geometric sequence of powers of two using the same martingale/digit-realization machinery. Wei--Nie--Wu--Yan (2016) prove that continuous upper truncation 0<r<gamma preserves the norm. Searches for arbitrary prescribed, irregular, lacunary, and superlacunary radius sets did not locate the stronger theorem that every set with unbounded logarithmic diameter has norm p', nor its finite-subfamily smooth-near-extremizer form. The contribution therefore passes as an extension beyond the known continuous-truncation and dyadic cases, while crediting the underlying realization method to Madrid.

## Scientific value

**PASS** — The theorem shows that the newly determined sharp constant is rigid under arbitrarily severe and irregular scale thinning, not merely continuous truncation or a fixed geometric grid. The finite-subfamily strengthening isolates the phenomenon in a reusable finite construction and clarifies that scale density is not responsible for the sharp norm.

## Independent checks

- Recomputed the finite product martingale distribution, conditional expectations, monotonicity of C_m(q), and the three limiting steps leading to p'.
- Verified algebraically that the separation assumption makes each allowable P_j interval at least unit length and forces strictly increasing digit positions.
- Checked the good-set measure, periodic suffix averaging error, boundary localization, and Lp-stable smoothing against the unrestricted p' upper bound.

## Findings

- The arbitrary-radius theorem is mathematically supported by the displayed construction.
- The dyadic/geometric special case and much of the martingale realization method are prior in Madrid's work and are correctly excluded from the novelty claim.
- No broader arbitrary-unbounded-log-diameter theorem was located in the current search.

## Literature evidence

- https://arxiv.org/abs/2609.12440 — Madrid (2026), exact unrestricted centered Hardy--Littlewood maximal norm p/(p-1).
- https://www.themoonlight.io/en/review/the-norm-of-the-centered-hardy-littlewood-maximal-operator — Current detailed review of Madrid reporting the geometric powers-of-two restriction and digit/martingale realization method.
- https://doi.org/10.1186/s13660-016-0963-x — Wei, Nie, Wu and Yan (2016), equality of the full and continuously upper-truncated centered maximal norms.

## Limitations

- The audit did not obtain Madrid's full manuscript directly; the dyadic special case was conservatively treated as prior based on a detailed public review.
- The theorem is one-dimensional and does not settle compact-annulus radius sets, weak (1,1), or higher-dimensional exact constants.
- The condition is a sufficient structural criterion and is not asserted necessary for attaining p'.

## Publication consequence

The audited claim may remain at its source path. This audit does not modify the research statement; it adds only the independent-audit evidence and updates the independent-audit verification channel.
