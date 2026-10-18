# Scientific review

## Correctness

**PASS.** The stopped-Poisson matrix kernel is differentiated explicitly. Poisson unimodality gives complete, exact sign patterns of every row and column; terminal absorption creates the Poisson-tail column. The global \(\ell^\infty\) optimizer follows by exact piecewise monotonicity. The \(\ell^1\) terminal-column optimization has a unique critical root because a polynomial in inverse time is strictly decreasing. A uniform \(O(\sqrt n)\) bound rules out every nonterminal column for large \(n\). Uniform Stirling estimates and a Poisson Chernoff bound locate the optimizer in the \(\sqrt{n\log n}\) window; a geometric bound on the upper tail yields the second asymptotic. An independently evaluated finite matrix exponential agrees with each formula on sampled dimensions and times, which is corroboration, not a universal proof.

## Originality

**PASS within inspected sources, with priority risk.** The classical Poisson distribution and its mode are acknowledged as ingredients. Inspected work on resolvent-controlled semigroup orbit decay, fractional linear birth–death distributions and irreducible birth–death mixing does not logically include the exact two endpoint derivative norms or the absorbed-chain optimizer shift. Relevant mathematical-record comparisons include pure-birth *numerical-step positivity* and unrelated *diagonal spectral-spacing maximal regularity*, neither of which covers the statement. Accessible earlier same-topic results concern cyclic, hypercube or symmetric lattice heat processes with different generators. An older absorption paper was available only by abstract, so historical coverage cannot be ruled out exhaustively.

## Value

**PASS.** Sharp \(t\|QT(t)\|\) controls dimension-dependent time-derivative sensitivity. The same fixed spectral set \(\{-1,0\}\) supports \(\sqrt n\) growth at one endpoint and almost \(n\) at the other, with an exact \(\sqrt{n\log n}\) optimizer displacement at \(\ell^1\). The boundary-driven distinction is a motivated semigroup feature and not merely an isolated Poisson probability computation.

## Boundaries

The theorem covers only \(\ell^1\) and \(\ell^\infty\) on counting-measure coordinates. The eventual \(\ell^1\) optimizer theorem does not give the smallest admissible \(n\). Historical priority remains subject to later independent full-text checking, especially older absorbed birth–death literature.

Self-review: passed. Independent audit: not yet performed.
