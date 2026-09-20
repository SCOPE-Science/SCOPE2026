# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness — PASS

The proof has three independent quantitative components.

First, Karagulyan's Theorem 1.1 gives a permutation of \(m\) trigonometric
frequencies whose maximal partial-sum operator has \(L^2\) norm
\(\gtrsim\log m\). The relevant input can be represented by a unit Fourier
coefficient vector. Splitting that vector into real and imaginary parts loses
only an absolute factor and produces a real unit vector with the same
logarithmic order.

Second, Lewko's coloring deletion argument is retained at finite \(N\) rather
than replaced by its \(o(N)\) consequence. If \(K=m^2\) and
\(B_m=\binom{m^2}{m}\), the number of deletion positions is at most
\(B_m r_m(N)\). Choosing progression-free density
\[
\delta_m=\bigl(100m^2\log(2m)B_m\bigr)^{-1}
\]
and applying Gowers's explicit quantitative Szemerédi theorem makes this at
most \(\eta_mN\), where
\(\eta_m=(100m^2\log(2m))^{-1}\). The entropy estimate for exceptional
colorings, together with the elementary lower bound for the number of
balanced colorings, leaves a strictly negative exponential margin:
\[
2\log(1-1/m)
+2H(\eta_m)
+2\eta_m\log\!\frac{B_m}{m-1}
+\frac{m^2}{N}\log(N+1)<0.
\]
The numerical constant \(100\) is more than sufficient; the proof supplies
elementary analytic bounds rather than relying on numerical evidence.

Third, Lewko's two-copy trigonometric construction converts the prescribed
progression pattern into a lower bound for every ordering. Zero coefficients
on intervening terms make a subsequence sufficient. Frequency translation and
integer dilation preserve the maximal-sum distribution, and the probability
mass \(1/2\) of the selected copy contributes only an absolute \(L^2\) factor.

Finally, for
\[
X_m=2^{2^{Q_m^{\,2^{2^{m+9}}}}},
\qquad
Q_m=100m^2\log(2m)\binom{m^2}{m},
\]
one has \(\log_2^{(5)}X_m=m+O(1)\). Inverting the scale converts the
\(\log m\) obstruction into \(\log_2^{(6)}N\). The monotone enlargement
argument is valid because added functions may be assigned zero coefficients.

The real-valued \(\sqrt2\)-bounded corollary follows by the standard
realification
\(\sqrt2\operatorname{Re}(e(t)\phi_n)\); averaging in \(t\) preserves a
lower bound for the maximal \(L^2\) norm.

## Originality — PASS, to the best of our knowledge

Lewko's 2026 paper was inspected in full. It proves qualitative divergence of
the optimal finite Garsia constant and explicitly says that the proof as
written gives no useful dependence of \(N\) on the target constant \(H\),
because it uses qualitative Fourier divergence and Szemerédi, and that the
true growth rate is unknown. It cites Karagulyan's 2020 paper but does not
insert Karagulyan's sharp finite \(L^2\) logarithmic obstruction into a
quantitative version of the finite construction.

Karagulyan's theorem and Gowers's explicit Szemerédi theorem were inspected
at their theorem statements. Searches combining Garsia/Kolmogorov
rearrangement constants, Lewko's arXiv identifier, Karagulyan, quantitative
Szemerédi, and iterated logarithms did not locate an explicit unbounded
lower-rate statement equivalent to
\(\mathfrak G_N\gtrsim\log^{(6)}N\).

The main residual originality risk is that the estimate is a synthesis of
known quantitative ingredients with a very recent combinatorial construction.
A contemporaneous note may not yet be indexed, and an expert could derive a
different explicit rate by quantifying the same construction. Bourgain's 1989
article was not independently checked line by line; however, an unbounded
finite lower rate there would conflict with the historical status summarized
in Lewko's 2026 resolution. No inaccessible source was found that gives
concrete evidence of prior coverage.

## Value — PASS

The direct source identifies the growth rate of the optimal finite Garsia
constant as unknown and supplies only qualitative divergence. The result here
provides a fully explicit unbounded lower rate while preserving the strongest
unimodular finite setting. It also isolates quantitatively where the enormous
loss occurs: the dependence on progression length in the available explicit
Szemerédi bound. This turns a qualitative obstruction into a benchmark that
can be improved independently by better additive-combinatorial or
permutation-pattern estimates.

The result does not approach Bourgain's \(O(\log\log N)\) upper bound, so its
value is as a first explicit quantitative floor and a decomposition of the
losses rather than a solution of the rate problem.

## Limitations

- The lower rate is six-fold iterated logarithmic and is not claimed sharp.
- The explicit finite-size threshold is crude and chosen for transparency.
- No quantitative almost-everywhere divergence rate is obtained for the
  infinite construction.
- The unimodular examples are complex-valued; the real-valued version is
  bounded by \(\sqrt2\).
- No leading constant is claimed.
- A contemporaneous unindexed quantitative refinement of the 2026 source may
  exist.
- Bourgain's 1989 article was not independently checked line by line.
- Cross-model review has not been performed.
