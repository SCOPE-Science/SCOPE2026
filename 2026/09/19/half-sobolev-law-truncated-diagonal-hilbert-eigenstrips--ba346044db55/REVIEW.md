# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The exact identity follows from three elementary ingredients that can be checked independently:
the product Fourier factorization
\[
\widehat{F_{\varepsilon,g}}(\xi_1,\xi_2)
=
\widehat{\mathbf1_{(-\varepsilon,\varepsilon)}}(\xi_1)
\widehat g(\xi_1+\xi_2),
\]
the fact that the multiplier of \(H_1H_2-I\) is \(-2\) on the first and third quadrants and zero on the
other two, and a Fubini change of variables. Constants agree with the unitary Fourier normalization used
in the source paper.

The \(\dot H^{1/2}\) limit is not merely an upper estimate. The kernel
\(J(s)=\int_0^s(\sin u/u)^2du\) satisfies \(J(s)\le s\) and \(J(s)/s\to1\). Dominated convergence handles
finite half-Sobolev energy, while Fatou's lemma forces the rescaled defect to diverge when that energy is
infinite.

For piecewise \(W^{1,1}\) cutoffs, the distributional derivative consists of an \(L^1\) part plus finitely
many point masses. This gives the stated \(1/\xi\) Fourier tail. Diagonal jump terms yield the logarithmic
coefficient, cross terms are bounded oscillatory logarithmic integrals, and the remainder is
\(o(\log R)\). The exact defect kernel is bounded at low frequency and decays like \(1/s\) after division
by \(s\), so frequencies above \(1/\varepsilon\) contribute only lower-order terms. For
\(g=\mathbf1_{(-1,1)}\), the two unit jumps give the coefficient
\(16/\pi^2\) for the squared defect and \(2/\pi\) for the normalized leading constant.

No empirical computation is used in place of proof.

## Originality

**PASS, to the best of our knowledge.** The closest source, arXiv:2609.15155, was inspected at the theorem
statement and at the Fourier proof of its truncated diagonal-strip example. It proves only the upper-order
bound
\[
\|\mathcal H\chi_{V_\varepsilon}-\chi_{V_\varepsilon}\|_2/
\|\chi_{V_\varepsilon}\|_2
\lesssim\sqrt{\varepsilon|\log\varepsilon|},
\]
and does not state an exact leading constant, an arbitrary-cutoff identity, a half-Sobolev
characterization, or a jump-count asymptotic. Searches using combinations of "double Hilbert transform",
"product Hilbert transform", "diagonal strip", "approximate eigenvector", "quadrant projection",
"fractional Sobolev", and "Hardy projection" did not locate an equivalent result.

Older papers on double Hilbert transforms located in search primarily study boundedness of singular
integrals along polynomial or analytic surfaces, not this indicator/quasi-eigenvector truncation problem.
The 1972 Fefferman paper was identified as foundational background but was not relied on for a claim that
its full text excludes the present formula.

Residual originality risk remains nontrivial because the result is a natural spectral refinement of a
very recent computation, and the exact kernel identity may be expressible in standard product Hardy-space
language. Unindexed contemporaneous work or an older formulation under different terminology could
therefore overlap.

No prior SCOPE record was located under the source identifier `2609.15155` or under
"Hilbert transform", "quasi eigenvector", and "Sobolev strip" terminology.

## Value

**PASS.** The result does more than optimize a constant in the source example. It identifies the exact
regularity threshold controlling the truncation defect, proves a converse characterization by
\(\dot H^{1/2}\), explains the source logarithm as a jump-discontinuity endpoint effect, and gives the
sharp leading constant for the motivating bounded strip. This is a reusable mechanism for constructing
and comparing approximate eigenstrips with different longitudinal regularity.

## Limitations

The theorem concerns diagonal-strip profiles and the \(L^2\) double Hilbert transform. Smooth cutoffs are
not indicators, so the half-Sobolev improvement is a functional statement rather than a new family of
bounded open sets. The result does not classify all near-invariant indicators, does not answer the
quantitative stability question in arXiv:2609.15155, and does not cover the bent-strip or positive-density
constructions from that paper.

No independent validation, independent audit, formal proof-assistant verification, or external expert
review is asserted.
