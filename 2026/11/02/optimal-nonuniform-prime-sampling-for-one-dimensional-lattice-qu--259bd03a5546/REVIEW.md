# Scientific review

## Correctness — PASS

The claim concerns the exact worst-case expected absolute error, not its square or an RMS surrogate. Fourier aliasing and nonnegative identical-phase extremizers prove that the apparent Cauchy--Schwarz bound is actually attained for all candidate sampling vectors. Distinct-prime least-common-multiple reduction produces the positive definite quadratic matrix \(D+uu^{\mathsf T}\). Its Sherman--Morrison inverse gives a unique minimizer, while \(c\le K\le p_{\min}\) proves strict positivity of every optimal probability. The derivative of the weight formula proves monotonicity for \(s>1\), and the prime number theorem establishes the sharp positive limiting gap. The analytic proof includes the single-prime boundary. An independently runnable standard-library script passed 402 exact and numerical groups, but finite tests are not used to assert the infinite result.

## Originality — PASS, qualified

Full-text comparisons were made with Kuo--Nuyens--Wilkes (arXiv:2304.10413), Kritzer--Kuo--Nuyens--Ullrich (arXiv:1706.04502), Dick--Goda--Suzuki (arXiv:2109.11694), Nuyens--Wilkes (arXiv:2308.03138) and Goda--Krieg (arXiv:2411.19164). The closest source makes the prime choice uniform and presents a worst-case error formula but does not give the nonuniform minimax solution or the limiting relative penalty. Other compared methods change the generator, the shift, the error criterion or the asymptotic question. Searches for nonuniform random-prime probability optimization and related terms yielded no directly equivalent statement. This is a best-knowledge assessment, not a proof of priority: general quadratic optimal-design results and hard-to-find specialized lattice studies remain meaningful risks.

## Value — PASS

The prime distribution is an actual design choice in a published integration algorithm; the result replaces an ad hoc uniform choice by an explicitly computable unique optimal law. It proves a strict and quantitatively nonvanishing smoothness-dependent improvement (about \(8.0\%\) at \(\alpha=1\), and \(34.5\%\) at \(\alpha=2\)) in the precise worst-case error criterion, not just a finite numerical gain. It also identifies the limitation that evaluating a larger random prime costs more nodes, which is outside this risk-only optimization.

## Literature and limitations

The result is limited to the one-dimensional, unshifted, single-prime periodic Korobov setting with \(\alpha>1/2\). No novelty or performance claim is made for higher dimensions, general weights, random shifts, independent randomized generators, RMS error or work-normalized cost. Publication priority and independent validation remain open.

Self-review: passed. Independent audit: not yet performed.
