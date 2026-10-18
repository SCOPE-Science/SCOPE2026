# Scientific assessment: geometric-payoff stability on a periodically renewing resource

## Correctness — PASS

The source's normalized discrete resource rule reduces exactly to a logistic map on the invariant all-defector face. Its primitive period-two points have the stated closed forms, the resource return derivative is \(-A^2+2A+4\), and the transverse derivative of the positive-fitness replicator update is exactly \(S(n)\). The triangular two-step Jacobian proves local attraction whenever both eigenvalues have modulus less than one; equality is explicitly withheld. The general variance formula follows from the affine payoff and the two resource values. In the witness the exact eigenvalues are \(37321/40000\) and \(4/25\), while the payoff at mean resource is \(403/400>1\). Symbolic reconstruction and independent forward-map trajectory checks using the included script agree. The source's physical square is invariant under the strict parameter inequalities verified in the proof.

## Originality — PASS

The primary Mondal–Ray–Chakraborty 2024 manuscript supplies the dynamics, qualitative periodic/chaotic examples, pointwise boundary stability table, and a mean-game ansatz. Its relevant Sections II–IV do not state a period-return transverse product, a variance-corrected two-cycle stability boundary, or an admissible open set where the mean criterion and actual stability disagree. Related continuous-time classifications cannot imply this discrete Floquet threshold; general periodic replicator results do not give this particular coupled resource/payoff regime. Bounded searches of mathematical research records, aliases, and relevant literature did not identify stronger covering implications. Residual risk includes unindexed specialist work and standard techniques potentially applied elsewhere; novelty is claimed for the model-specific sharp threshold and physical mismatch interval, not for Floquet or arithmetic–geometric mean theory themselves.

## Value — PASS

Predicting whether cooperators can invade a population supported by an oscillating resource is central to interpreting this particular discrete ecological game. The sharp interval \(1<m<\sqrt{277}/16\) proves that an average-payoff prediction can reverse the genuine local ecological selection outcome on an open, physically invariant set. It supplies a simple exact reproducible diagnostic where the motivating model currently presents a mean-game heuristic, rather than a small numerical improvement or an arbitrary computational sample.

## Closest literature and boundaries

The closest full text is S. S. Mondal, A. Ray, and S. Chakraborty (2024), DOI:10.1063/5.0190800, Section III B and Table I; its mean-game heuristic is discussed rather than accepted as a general theorem. Ito and Yamamichi (2024), DOI:10.1093/pnasnexus/pgae455, analyze continuous-time feedback games. Mukhopadhyay and Chakraborty (2020), DOI:10.1016/j.jtbi.2020.110288, provide context for periodic discrete evolutionary play.

Only local period-two stability and the precise noncritical stability boundaries are proved; global basins, noisy systems, chaotic invariant resource distributions, and nonlinear dynamics at the unit multiplier are not determined. Numerical orbits are supplementary. Originality comparison is bounded rather than exhaustive.

Self-review: passed. Independent audit: not yet performed.
