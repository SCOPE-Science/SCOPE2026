# Independent Audit — 2026/09/21/generalized-muirhead-identric-e4-phase-boundary--3d52bbf9bbcb

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `8719b065f61212b9d25ca2162affc5d075710c20`
- Disposition: **PASSED**

## Correctness

**PASS** — The hyperbolic normalization is exact: for x=g e^-z,y=g e^z, log(M/I)=log cosh(dz)/s-(z coth z-1), so comparison is controlled by R_d(z)-s. The E4 inequalities become d0<d<1 and L(d)<s<U(d). The endpoint expansions give R_d(0)=3d^2/2 and R_d(infinity)=d. At s=L(d), the already-classified E1 boundary yields strict positivity for every finite z and both endpoint gaps are positive, proving C(d)>L(d); the d=d0 limit gives C=3/5. For d<log2, either the local quadratic term or the large-z expansion gives C<U, with finite attainment. For d>=log2, Pittenger's sharp power-mean comparison and monotonicity in power order imply R_d(z)>d for finite z while R_d tends to d, so C=d. Continuity follows after compactifying z, and strict increase follows because R_{d2}-R_{d1} is positive and continuous even at both compactified endpoints. Independent numerical minimization gave C(0.64)≈0.613915, C(2/3)≈0.657471, C(0.68)≈0.676406, and C(0.69)≈0.689380, all strictly between L and U; the exact mixed example at y/x=64 has log(M/I)≈-0.00337707, matching its rational certificate.

## Originality

**PASS** — Wang-Chu-Qiu explicitly state that they cannot discuss the complementary E4 case and leave it as an open problem. The audited theorem gives a necessary-and-sufficient one-dimensional phase curve throughout that exact region, including a complete globally positive subregion and a mixed-sign subregion. Later generalized-Muirhead literature located in targeted searches addresses other comparison means or structural properties, not this E4 identric classification. Originality is therefore supported for the phase boundary, with residual risk from unindexed or differently notated work.

## Scientific value

**PASS** — The result resolves a clearly stated 2010 open region sharply rather than merely adding sufficient conditions. It identifies the full phase geometry, proves the boundary is continuous and strictly increasing, and supplies exact global and mixed-sign examples. Lack of an elementary closed form for C(d) does not diminish the necessary-and-sufficient classification.

## Sources

- **Some Comparison Inequalities for Generalized Muirhead and Identric Means** — M.-K. Wang; Y.-M. Chu; Y.-F. Qiu. https://doi.org/10.1155/2010/295620 — Primary source: classifies the other parameter regions and explicitly leaves the remaining E4 case as an open problem.
- **Inequalities between arithmetic and logarithmic means** — A. O. Pittenger. https://zbmath.org/?q=an%3A0472.26010 — Classical sharp identric/power-mean bound used for the d>=log 2 collapse; also quoted in the 2010 primary source.
- **Exact inequalities involving power mean, arithmetic mean and identric mean** — Y.-M. Chu; M.-Y. Shi; Y.-P. Jiang. https://doi.org/10.33993/jnaat402-1042 — Later identric/power-mean comparison background, distinct from the audited two-parameter E4 phase classification.

## Limitations

- No elementary closed form is proved for C(d) on (sqrt(2/5),log 2).
- Uniqueness of the finite minimizer is not claimed.
- The theorem is specific to the E4 region left unresolved by the 2010 source.
- Equivalent prior coverage in unindexed or differently notated literature remains a residual originality risk.

## Independent checks

```json
{
  "hyperbolic_normalization_rederived": true,
  "E4_reparameterization_checked": true,
  "endpoint_expansions_checked": true,
  "compactification_monotonicity_argument_checked": true,
  "sample_phase_values": {
    "d_0.64": 0.6139148287878556,
    "d_2over3": 0.6574705562951556,
    "d_0.68": 0.6764055373894176,
    "d_0.69": 0.6893804611308562
  },
  "mixed_example_log_ratio": -0.0033770704269603597,
  "source_open_problem_checked": true,
  "source_tree_unchanged": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned record tree was unchanged from the inventory snapshot through the checked commit. GitHub was used only as read-only evidence. Open-access and preprint sources were checked first, and no decisive comparison required institutional retrieval. No GitHub write or separate dispatcher report was performed.
