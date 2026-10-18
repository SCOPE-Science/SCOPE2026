# Review of exact word reversal and infinite symbolic memory

## Correctness — PASS

The branch formulas and invariant density agree with the original map and density in Kraaikamp–Langeveld (2016), Section 2.1. Independently, the monotone change of variable \(z=x/(4-x)\) gives a normalized invariant \(dz/(z\log3)\); the two explicitly computed inverse branches satisfy the exact Perron–Frobenius balance. A finite binary cylinder is exactly the interval obtained by its ordered inverse-branch composition. Its endpoints are projective columns of a positive integer matrix \(M_wQ\), so integrating the invariant logarithmic density produces \(|\log(ad/bc)|/\log3\). The matrices satisfy \(M_jQ=QM_j^{\mathsf T}\), yielding an identity for *every* reversed word by induction. The all-zero branch has an exact fixed point and contraction ratio \(1/4\), giving its cylinder formula. A strict derivative inequality makes the successive all-zero conditional probabilities nonconstant at arbitrarily long histories and excludes every finite Markov order. No step uses finite enumeration as a universal proof.

## Originality — PASS (best-knowledge, not priority certification)

The source map and invariant density are explicitly prior art. The 2016 source develops natural extensions, invariant-density approximations, matching and entropy, without asserting an exact finite-word reversal theorem or a non-finite-Markov theorem. The full 2012 paper of Dajani–Hensley–Kraaikamp–Masarotto develops the more general class of flipped continued fractions, but its inspected framework and invariant-measure conclusions likewise do not state either of these assertions. Existence of a two-dimensional natural extension or a stationary density does not by itself force reversal symmetry: the decisive matrix intertwining identity is an additional model-specific check. Targeted mathematical literature and research-record searches found no stronger comparison that entails this precise all-word identity. Possible earlier general symmetrization results for special Möbius maps remain a real historical-priority risk and warrant specialist review.

## Mathematical value — PASS

Reversibility at every block length is a structural property of a non-invertible dynamical digit observable, much stronger than invariance or matching one-digit frequencies. Here it coexists with strictly varying conditional probabilities along arbitrarily long identical symbol runs. The combination identifies a reversible process with genuine infinite memory and supplies every cylinder probability by exact finite matrix arithmetic; it is not a rephrasing of the invariant-density calculation or a narrow arbitrary finite statistic. Its scope is intentionally confined to this historically motivated two-branch map.

## Reproducibility and limitations

The standalone exact-arithmetic checker covers 4,094 nonempty words through length eleven, tiled-cylinder endpoint identities, the density transfer balance at five rational points, and all-zero identities through length 59. Its output was `VERIFY_OK 4094`. The infinite proof is analytic. The statement does not imply that the interval map is time invertible, that other flipped continued-fraction maps have the same reversal property, or that the symbolic process is mixing with a specified rate. A historical equivalent theorem could exist outside the inspected sources.

Self-review: passed. Independent audit: not yet performed.
