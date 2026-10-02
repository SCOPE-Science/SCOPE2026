# Review status

Scientific audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: PASS. The coordinate/determinant argument was reconstructed. After placing the distinguished edge symmetrically, the volume equals \(s|\det Y|/n!\). Diameter constraints give \(\|y_i\|^2\le D^2-s^2/4\) and \(\|y_i-y_j\|\le D\). The weighted complete-graph frame operator \(S=YQY^	op\) has a computable determinant and a sharp trace bound; AM--GM on its eigenvalues yields exactly the displayed volume profile. Equality forces every transverse norm and pairwise-distance constraint to be tight, hence every edge except the distinguished one has length \(D\). The converse Gram matrix is positive definite and makes the frame operator scalar. The normalized shortest-edge profile and inverse formula follow algebraically.

Originality: PASS. Searches covered the classical largest-small-simplex problem, recent aggregate frame inequalities, prescribed-edge and shortest-edge formulations, and distance-geometry terminology. The full 2025 frame-inequality preprint was inspected: it gives volume bounds from total edge energy and the regular-simplex equality case, but contains no diameter condition and no one-edge-conditioned profile. No located primary source states or mechanically implies the exact formula, equality family, or inverse shortest-edge law.

Scientific value: PASS. The theorem refines the classical regular-simplex diameter extremum into a sharp one-parameter stability profile valid at every shortest-edge ratio. The equality family and best-possible inverse edge bound are natural geometric information, not an arbitrary finite slice.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
