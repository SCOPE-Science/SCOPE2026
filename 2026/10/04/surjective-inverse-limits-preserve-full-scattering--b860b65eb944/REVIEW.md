# Independent mathematical audit

## correctness

PASS

Fix a nontrivial finite open cover \(\mathcal U=\{U_j\}\) of the inverse limit and an infinite time set. For each non-dense \(U_j\), choose an open hole \(O_j\subset X\setminus\overline{U_j}\). Finite-coordinate cylinder neighborhoods of finitely many chosen points in these holes can be pushed to one common stage \(r\), giving nonempty open \(V_j\subset X_r\) with \(\pi_r^{-1}(V_j)\subset O_j\). Choose closed \(F_j\subset V_j\) with nonempty interior and put \(W_j=X_r\setminus F_j\). Surjectivity of \(\pi_r\) proves that the \(W_j\) cover \(X_r\): otherwise a stage point in all \(F_j\) lifts to a point omitted by every \(U_j\). Thus \(\mathcal W=\{W_j\}\) is nontrivial and \(U_j\subset\pi_r^{-1}(W_j)\). Equivariance commutes with the joins, and surjectivity gives \(N(\pi_r^{-1}\mathcal C)=N(\mathcal C)\), so the inverse-limit cover complexity dominates the full-scattering stage complexity and diverges. The countable-product corollary then follows by taking the inverse sequence of finite products and using the published finite-product theorem.

## originality

PASS

The closest current source, Hui Xu's 2026 paper, states finite-product closure of full-scattering. The audited theorem instead proves permanence under arbitrary countable surjective inverse limits, from which countable products follow. Current Resultary and targeted searches returned no prior inverse-limit or countably-infinite-product full-scattering theorem. The full Xu paper could not be obtained through the public arXiv/OA routes used in this run, and the authorized institutional retrieval service was unavailable, so the judgment is explicitly best-of-knowledge rather than a whole-document noncoverage assertion.

## value

PASS

Inverse-limit permanence is a natural structural closure property in topological dynamics and converts the newly proved finite-product theorem into a countable-product theorem. The result handles arbitrary surjective inverse systems, not only a single special construction, and isolates precisely where surjectivity is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
