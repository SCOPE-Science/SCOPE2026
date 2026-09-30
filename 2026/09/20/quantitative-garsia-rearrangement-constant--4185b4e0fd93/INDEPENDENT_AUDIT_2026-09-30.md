# Independent Audit — 2026/09/20/quantitative-garsia-rearrangement-constant--4185b4e0fd93

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `40afa7a6133c00741505a42a40ea79151af16493`
- Disposition: **PASSED**

## Correctness

**PASS** — The quantitative extraction from Lewko's construction is internally consistent. Karagulyan's theorem supplies a permutation of m Fourier modes whose L2 maximal operator is bounded below by c log m; splitting a complex coefficient vector into real and imaginary parts loses only an absolute factor. In the coloring step, Gowers's explicit Szemeredi bound with exponent 2^{2^{m+9}} makes r_m(N)<=N/Q_m at N>=X_m. Lewko's deletion count then gives at most the stated entropy-sized exceptional family. The balanced-coloring denominator is at least K^N/(N+1)^K, and the exponent is negative with the submitted eta_m; an independent numeric check of the displayed entropy upper bound for m>=2 found no exception. The two-copy Fourier system is orthonormal and unimodular, while zero coefficients make enlargement to any N>=N_m harmless. Finally, L_3(X_m)=D_m log_2 Q_m, L_4(X_m)=2^{m+9}+O(log m), and L_5(X_m)=m+O(1), so the c log m obstruction becomes c L_6(N). The realification argument is also valid.

## Originality

**PASS** — Lewko's September 2026 paper gives qualitative divergence using a two-copy trigonometric construction, a permutation-pattern counting lemma and qualitative Szemeredi input. Karagulyan 2020 provides the sharp logarithmic finite Fourier obstruction, and Gowers 2001 provides an explicit quantitative progression bound. Targeted searches did not locate a prior explicit finite-size Garsia lower rate, let alone the six-fold iterated logarithm obtained by composing these inputs. The components are prior art; the claimed novelty is their explicit quantitative synthesis in Lewko's finite Garsia problem.

## Scientific value

**PASS** — Although extremely slow and deliberately nonoptimal, the L_6(N) rate turns a newly qualitative divergence theorem into a fully effective finite statement and isolates exactly where quantitative losses enter. That is useful baseline information for a problem whose true finite growth remains far from the known log-log upper bound.

## Sources

- **On Kolmogorov's rearrangement problem and Garsia's conjecture** — Mark Lewko. https://arxiv.org/abs/2609.18491 — Primary 2026 qualitative construction using two trigonometric copies, a permutation-pattern lemma, Szemeredi's theorem and counting.
- **On Weyl multipliers of the rearranged trigonometric system** — Grigori A. Karagulyan. https://arxiv.org/abs/2004.01003 — Theorem 1.1 gives the sharp logarithmic L2 lower bound for a rearranged finite trigonometric maximal operator.
- **A new proof of Szemeredi's theorem** — W. T. Gowers. https://doi.org/10.1007/s00039-001-0332-9 — Source of the explicit general progression bound used to make Lewko's qualitative pattern argument effective.
- **On Kolmogorov's rearrangement problem for orthogonal systems and Garsia's conjecture** — Jean Bourgain. https://doi.org/10.1007/BFb0090057 — Classical log-log upper-bound context; the audited novelty is the lower rate.

## Limitations

- The six-fold iterated-log lower bound is extremely weak and not claimed close to the true finite growth.
- The explicit size X_m is intentionally crude and will improve with sharper progression or pattern-counting bounds.
- The theorem is finite L2 information; it does not quantify almost-everywhere divergence of the infinite construction.
- A contemporaneous refinement of the very recent Lewko preprint remains a residual priority risk.

## Independent checks

```json
{
  "karagulyan_log_lower_statement_checked": true,
  "gowers_quantitative_scale_checked": true,
  "entropy_exponent_inequality_numerically_checked": true,
  "two_copy_orthonormality_checked": true,
  "realification_argument_checked": true,
  "iterated_log_inversion_reconstructed": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned record tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. Open-access and preprint sources were checked first. No decisive comparison remained inaccessible; where a nondecisive full-document retrieval timed out, that limitation is stated explicitly rather than treating the paper as read.
