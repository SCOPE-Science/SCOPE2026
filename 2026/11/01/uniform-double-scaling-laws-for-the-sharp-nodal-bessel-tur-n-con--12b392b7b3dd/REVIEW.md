# Scientific review of the uniform joint-scaling Bessel nodal minimum theorem

## Correctness — PASS

The theorem quantifies over all positive real orders tending to infinity and integer nodal indices whose order ratio belongs to a fixed compact subset of the positive axis. The source supplies strict convexity and unique minimizers, the exact log-derivative quotient, and the exact stationary equation. The differentiated Debye expansion is uniform on the required compact argument interval. Its even/odd parity localizes the minimizer within order \(\nu^{-2}\) of the central WKB phase, and proves a remainder of order \(\nu^{-4}\) in the rescaled location and minimum. At the phase center, the first Debye correction is \(B(t)=1/(8\sqrt{t^2-1})+5/(24(t^2-1)^{3/2})\); solving stationarity yields the stated \(9t^2+22\) numerator. Substitution into the exact Turán expression gives \(9t^2+10\). Direct exact algebra and six numerical samples, including noninteger orders, passed the standalone supplementary checker. The proof does not rely on sampling or an assumption of fixed order.

## Originality — PASS relative to inspected evidence

The closest published fixed-order nodal asymptotic has \(O_{\mu,\alpha}(n^{-3})\) errors and explicitly excludes simultaneous growth. The 2026 arXiv primary paper establishes qualitative order and index monotonicity, not the positive, nonconstant \(n/\nu\)-dependent profile or its two explicit corrections. The 2011 Bessel Turán survey provides earlier minima and inequalities; the 2015 general-cylinder result locates different, unnormalized extrema. DLMF Debye expansions are standard inputs, not optimized nodal Turán conclusions. Actual semantic-search queries and full-text comparisons appear in AUDIT.json. Earlier unindexed equivalent calculations are a residual risk.

## Mathematical value — PASS

The nodal minima are sharp best constants for the oscillatory normalized Turán inequality, and their dependence on two growing parameters is not controlled by either known one-parameter limit. The result establishes a natural complete interior scaling profile and explicit uniform corrections to both the optimal value and the location, thus quantitatively bridging the fixed-index Airy and fixed-order far-tail regimes without claiming either endpoint itself. This is a motivated structural description, not an arbitrary numeric instance or a routine restatement of a Bessel-zero formula.

## Scope and limitations

No uniformity is claimed when the ratio tends to zero or infinity, or for cylinder functions other than \(J_\nu\). The proof uses classical smooth Debye expansions at arguments bounded away from the turning point. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
