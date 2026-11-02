# Scientific review: exact finite-time transitions for star-network best responses

## Correctness — PASS

The proof covers all star degrees \(s\ge2\), all real parameters \(0<\delta<1\), all initial actions in \([0,1]\), and each specified update schedule separately. Every leaf-first hub update is exactly \(F(c)=\max\{0,1-s\delta+s\delta^2c\}\), so monotonicity makes initial hub activity one the worst case. The untruncated affine recurrence determines the *first* exact zero, including its resonance at \(s\delta^2=1\). The equilibrium classification is separately checked; the random-asynchronous theorem follows from a positive-probability absorbing finite update word, not an unsupported convergence assumption. The first-pass permutation formula counts hub positions exactly, including equality boundaries.

Independent exact-rational checks in `verifier.py` cover 82,953 parameter cases, threshold and resonance examples, 27 small permutation cases with complete order enumeration, and arbitrary-state absorbing update words. The universal proof does not rely on the finite tests.

## Originality — PASS, subject to residual priority risk

Closest primary literature: Misiak and Dziubiński, [*Convergence rates of random-order best-response dynamics in public good games on networks*](https://arxiv.org/abs/2602.15986), February 17, 2026. Its Sections 2.1–2.3 and 3.2.2 establish the random best-response model and numerical convergence patterns, including the star as a complete bipartite graph. The source uses an approximate stopping tolerance, not an exact first-hit classification. It does not give the sharp leaf-first sweep cutoff, two equal-coefficient endpoint logarithms, four-leaf one-sweep threshold, exact random-permutation deactivation probability, or uniform finite-hit geometric tail proved here.

The earlier paper Bramoullé, Kranton and D'Amours, [*Strategic Interaction and Networks*](https://doi.org/10.1257/aer.104.3.898), American Economic Review 104 (2014), Example 2, **already gives the star's unique equilibrium and its activity threshold**. No novelty is claimed for equilibrium identification alone. Its equilibrium and spectral theorems do not supply a finite transient first-zero index under a specified update protocol. Source and conceptual searches did not identify an exact equivalent. Related results on generic coordinate iteration or unindexed studies of star scheduling may exist and remain a genuine priority risk.

## Mathematical value — PASS

Exact convergence times answer a concrete question left open by tolerance-based network game simulations: when can a continuous-action best-response game reach the exact equilibrium in finitely many updates? The all-degree result distinguishes the equilibrium transition \(\delta=1/s\), the sharp spectral resonance \(\delta=1/\sqrt{s}\), and a degree-four onset of one-sweep hub deactivation. Near both the emergence and disappearance of the hub-inactive phase, the worst-case sweep count diverges logarithmically with the same sharp coefficient \(1/\log s\). The random-order results give a rigorously positive exact-hitting probability and tail guarantee, not just a numerical appearance of convergence. The star is a canonical high-degree network example already examined by both primary sources. The quantitative result is self-contained and potentially useful for scheduling and interpreting exact versus tolerance-based convergence.

## Limits and residual risks

Only the specified unweighted stars and homogeneous \(0<\delta<1\) game are covered. Worst-case deterministic sweep counts are not random expected hitting times. The random geometric upper tail is conservative. The random-permutation formula is for *hub* deactivation in one pass; it is not the probability that all actions have reached equilibrium in that pass. Published equilibrium classification is prior work, not a finding here. An unindexed equivalent transient analysis might limit priority. This is not independent validation.

Self-review: passed. Independent audit: not yet performed.
