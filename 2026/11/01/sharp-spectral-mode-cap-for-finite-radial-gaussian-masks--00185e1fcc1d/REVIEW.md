# Scientific review: sharp spectral mode cap

## Correctness — PASS
For every finite union of \(K\) strictly separated bounded squared-radius intervals, rotational invariance gives the exact monomial moments. Adjacent differences reduce to a nonzero exponential polynomial with at most \(2K\) terms; the self-contained Rolle induction gives at most \(2K-1\) real zeros, hence at most that many sign reversals and at most \(K\) strict eigenvalue peaks. For each \(K\), the separated-ring induction keeps earlier strict peaks and adds one at an arbitrarily large degree, with the new contribution asymptotic to \(e^{-M}M^M/(8M)\) on one side and \(-3e^{-M}M^{M+1}/(8M)\) on the other. The proof handles a possible central disk and boundary mode explicitly. The included finite numerical tests are supplementary, not an infinite proof.

## Originality — PASS under the inspected record
The closest finite-union paper, Halvdansson, arXiv:2502.11805v1, Proposition 2.3, calculates rearranged plunge asymptotics rather than this finite-scale natural-degree modal-count bound with sharp attainment. Daubechies provides the diagonalization; Knutsen provides the one-ring mode ordering, and neither presents the global sharp \(K\)-band complexity theorem. Yu and Karlin's general total-positivity machinery is acknowledged as pre-existing and likely yields a related variation-diminishing upper bound. The new claim is **the sharp finite-band spectral statement including realization for every \(K\)**, not the existence of the Poisson integral nor a generic total-positivity principle. Targeted literature and database searches yielded no statement covering both the bound and sharpness. Residual risk: stronger implicit coverage in classical mixture theory or unindexed work, and the uninspected Karlin monograph.

## Value — PASS
A single Gaussian annulus has one natural Hermite spectral peak; multi-annulus masks need not be unimodal. The result gives the optimal global topological cap on the number of spectral peaks for every finite component count, plus simultaneous extremal realization. The cap is independent of radii, widths, and scale. It is a structural spectral invariant for an established family in time-frequency concentration, not a chosen numerical slice or a mere normalization calculation. No claim is made about sorted eigenvalues.

## Limits and available evidence
The infinite theorem is analytic. The checker confirms four examples and discrete moment/difference identities but does not establish generality. Main primary source sections read: Halvdansson 2025 Proposition 2.3 and its proof, Knutsen 2020 Sections 2.3 and 3.1, Daubechies 1988 Sections I and IV, and Yu 2011 Theorem 3 and variation-diminishing lemma. Some historical mixture-theory literature is not exhaustively accessible.

Self-review: passed. Independent audit: not yet performed.
