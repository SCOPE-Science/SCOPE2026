# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The statement reduces to three independent assertions.

First, the unweighted outer-exponent inclusion
\[
(\oplus E_n)_p\longrightarrow(\oplus E_n)_q,\qquad p<q,
\]
is strictly singular for arbitrary finite-dimensional blocks. The gliding-hump proof uses only finite rank of initial block projections. An assumed lower bound on an infinite-dimensional subspace produces almost disjoint normalized vectors. Their partial sums have \(p\)-norm of order \(m^{1/p}\), while their images have \(q\)-norm of order at most \(m^{1/q}\) (bounded when \(q=\infty\)), contradicting the lower bound. Bounded block multiplication preserves strict singularity.

Second, failure of the proposed finite-strict-singularity criterion immediately produces arbitrarily large finite-dimensional subspaces inside a single high-weight block on which the operator is bounded below. This gives the lower bound
\[
b_m(D_\lambda)\ge
\sup_{\dim E_n\ge m}|\lambda_n|.
\]

For sufficiency, fixing a positive threshold leaves only blocks of uniformly bounded dimension. Auerbach coordinates factor the associated unweighted block inclusion through the scalar formal inclusion \(\ell_p\to\ell_q\). The factor norms are controlled solely by the uniform dimension bound. Since scalar Bernstein numbers equal \(m^{1/q-1/p}\), the high-weight part is finitely strictly singular with the stated quantitative estimate. The low-weight remainder has arbitrarily small operator norm. This yields the displayed Bernstein upper envelope and proves finite strict singularity.

Third, compactness follows from finite-rank truncations when the weights vanish. If they do not vanish, unit vectors chosen in distinct high-weight blocks have images with pairwise separated supports, preventing relative compactness.

Checks were made for \(p=1\), for \(q=\infty\) using the \(c_0\)-sum, for repeated block dimensions, for unbounded dimensions, and for zero or complex weights. No complementability of arbitrary subspaces is used.

## Originality

The scalar inclusion \(\ell_p\hookrightarrow\ell_q\) and its finite strict singularity are classical and are not claimed as new. Milman's classical separation of strictly singular from finitely strictly singular operators also uses finite-dimensional Hilbertian structure and is explicitly treated as prior art.

Targeted searches covered exact and synonymous terminology: finitely strictly singular, superstrictly singular, Bernstein numbers, formal identities, block-diagonal maps, weighted block maps, \(\ell_p\)-sums of finite-dimensional spaces, and dimension profiles. Modern sources found detailed scalar, variable-exponent, Besov, Sobolev, Lorentz, and other structured sequence-space criteria, but no statement of the arbitrary-Banach-block threshold
\[
\sup\{\dim E_n:|\lambda_n|\ge t\}<\infty\quad\forall t>0
\]
as an if-and-only-if criterion, nor the resulting three-way compact/FSS/SS classification with the stated Bernstein envelope.

Residual risk is concentrated in older operator-ideal literature. Milman's 1970 Russian paper was not inspected in full. Pietsch's 1978 monograph *Operator Ideals* was not exhaustively inspected. An equivalent result may therefore exist under older terminology or as an unstated consequence. This is why originality is asserted only to the best of our knowledge.

## Value

The result supplies one mechanism that interpolates between the two classical extremes: scalar formal inclusions, which are finitely strictly singular but non-compact, and growing finite-dimensional block constructions, which can be strictly singular without being finitely strictly singular. The exact obstruction is not the Banach geometry inside a block but the dimensions of blocks surviving each positive weight threshold.

The quantitative Bernstein estimate also converts a qualitative threshold criterion into an explicit decay envelope determined by the dimension profile \(d_\lambda(t)\). This makes the statement reusable for concrete block decompositions without requiring Euclidean blocks or a special basis inside the \(E_n\).

## Sources checked

- V. D. Milman, 1970, bibliographic data and later descriptions of his formal-inclusion and non-FSS constructions.
- Th. Schlumprecht, *Operators and Matrices* 6 (2012), DOI 10.7153/oam-06-22.
- D. E. Edmunds and J. Lang, *Notes on Non-Compact Maps and the Importance of Bernstein Numbers*, arXiv:2503.19600 / *Advances in Operator Theory* (2025).
- J. Lang and A. Nekvinda, *Mathematische Nachrichten* 298 (2025), DOI 10.1002/mana.12031.
- Recent work using Milman's flat-vector lemma and modern Bernstein-number formulations, including 2026 work on Baernstein and Schreier spaces.

The cited current literature was used to test stronger or equivalent coverage, not as the source of the research target.
