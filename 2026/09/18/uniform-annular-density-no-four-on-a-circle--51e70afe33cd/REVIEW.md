# Review: Uniform thick-annulus density for extensible no-four-on-a-circle sets

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The argument uses the published Ghosal--Goenka random sampling law and their simultaneous dyadic bounds on the three bad-quadruple classes. The new step is a uniform concentration estimate for all square annuli of relative thickness at least a fixed \(\eta\), followed by a deletion charge.

For \(A_{n,m}=[n+m]^2\setminus[n]^2\), the exact shell count \(2r-1\) gives \(\mathbb E|Q\cap A_{n,m}|\ge\alpha m\). Chernoff yields a failure probability at most \(e^{-\alpha m/8}\). Summing over all integer pairs with \(\eta n\le m\le n\) is finite, so Borel--Cantelli gives the required occupancy simultaneously for all sufficiently large admissible annuli.

Every point deleted from such an annulus has a witnessing bad quadruple lying in \([n+m]^2\). Mapping a deleted point to one witnessing quadruple is injective because each quadruple chooses a single maximal-norm point under the fixed tie-breaking rule. With \(T=\lceil\log_2(n+m)\rceil\), the source bounds therefore give
\[
D_{n,m}\le6C\alpha^4 2^T<24C\alpha^4n\le(24C/\eta)\alpha^4m.
\]
The choice \(\alpha^3\le\eta/(192C)\) leaves at least \(3\alpha m/8\) points. All inequalities are one-sided in the safe direction, and the same choice of realization satisfies both the source dyadic event and the probability-one annular concentration event.

No empirical computation is needed for the proof.

## Originality

The source preprint arXiv:2609.20447 was read at theorem/proof level. It proves the prefix statement \(|S\cap[n]^2|=\Omega(n)\), and its dyadic shells serve as bookkeeping for bad-quadruple estimates; no simultaneous thick-annulus density theorem was found there. The 2026 finite-box paper by Ghosal--Goenka--Keevash was also checked for the surrounding no-four-on-a-circle results.

Searches covered the source title and identifier and combinations of "no-four-on-a-circle", "extensible", "annular density", "square annulus", "dyadic shell", "shell density", and "local density". No prior equivalent formulation was located. Prefix linear density alone does not imply the displayed annular lower bound, so the theorem is not a formal restatement of the source conclusion.

No inaccessible paper emerged as a concrete high-risk source with a matching annular claim. The main residual risk is contemporaneous or not-yet-indexed work because the motivating preprint was submitted on 17 September 2026.

## Value

The result upgrades a global prefix-density construction to uniform mesoscopic radial regularity: every constant-relative-thickness square shell eventually contains linearly many retained points. It also identifies a simple general mechanism combining weighted shell concentration with cumulative deletion estimates. This is a meaningful strengthening of the extensible construction rather than a new finite-box parameter value.

## Limitations

The result is origin-centred and \(\ell_\infty\)-shaped, depends on a fixed \(\eta\), does not handle thinner relative shells or translated windows, and does not optimize constants. It remains an existential probabilistic construction.
