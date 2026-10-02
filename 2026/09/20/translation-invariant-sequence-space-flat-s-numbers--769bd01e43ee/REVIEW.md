# Independent audit review — 2026-10-01

## Final claim

If \(G\) is an infinite discrete group and \(T\) is a bounded operator on \(\ell_p(G)\) for \(1\le p<\infty\), or on \(c_0(G)\), commuting with all left translations, then every approximation, Bernstein, Gelfand, and Kolmogorov number of \(T\) equals \(\|T\|\); the distances to compact, finitely strictly singular, and strictly singular operators also equal \(\|T\|\), witnessed on a \(1\)-complemented classical sequence subspace where \(T\) is bounded below arbitrarily close to its norm.

## Correctness — PASS

A finitely supported almost-norming vector can be translated to disjoint input blocks while finite truncations of its image are translated to disjoint output blocks; choosing summable/Hölder-compatible tail errors gives an infinite-dimensional copy of \(\ell_p\) or \(c_0\) on which \(T\) is bounded below by \(\|T\|-\varepsilon\). Block norm-one functionals yield a norm-one projection onto that subspace. This immediately gives the strict-singular/FSS/compact distance and approximation/Bernstein identities. Finite-codimensional intersection gives the Gelfand identity, and uniform tails on a finite-dimensional quotient subspace plus a translate avoiding a finite coordinate set gives the Kolmogorov identity. The endpoint estimates for \(p=1\) and \(c_0\) are separately valid.

## Originality — PASS

Karlovych–Shargorodsky (2024) is genuine broader prior art for maximal noncompactness: its accessible abstract states norm equals Hausdorff measure of noncompactness for broad translation-invariant sequence-space maps on \(\mathbb Z^d\). It does not state the exact all-\(n\) Bernstein/Gelfand/Kolmogorov/approximation profiles or the exact FSS/strict-singular distances. Published SCOPE searches found related flat-profile theorems for specialized operator classes, none of which implies this arbitrary group-translation commutant theorem. The 2024 full theorem section could not be exhaustively fetched, so equivalent stronger wording inside it remains a residual risk.

## Value — PASS

Determining four classical s-number scales and three operator-ideal distances exactly is a substantial quantitative strengthening of ordinary maximal noncompactness, and the complemented almost-norming witness is a reusable structural mechanism for translation-invariant operators on natural sequence spaces.

## Source inspections

- **Discrete Riesz transforms on rearrangement-invariant Banach sequence spaces and maximally noncompact operators** (Karlovych–Shargorodsky, Pure Appl. Funct. Anal. 9 (2024), 195–210): PARTIAL_COVERAGE. The accessible statement proves norm equals Hausdorff measure of noncompactness for translation-invariant maps on \(\mathbb Z^d\), but does not mention the audited flat \(a_n,b_n,c_n,d_n\) profile or strict-singular distances.
- **Notes on Non-Compact Maps and the Importance of Bernstein Numbers** (arXiv:2503.19600): CONTEXT. It supports treating Bernstein numbers as finer data than ordinary maximal noncompactness; it is not a coverage theorem for the translation-invariant class.

## Residual risks

- The complete 2024 Karlovych–Shargorodsky theorem section was not exhaustively inspected; an equivalent stronger formulation inside that paper or older multiplier literature remains a material risk.
