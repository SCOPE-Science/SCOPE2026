# Self-review: sharp finite-time three-card quantum-stochastic mixing

## Correctness — PASS
The Lindblad factorization is legal because the random-transposition class sum commutes with every jump. The six-dimensional regular representation decomposes as trivial, sign and standard irreducibles. Character inversion yields all six exact probabilities, and explicit differentiation on the three intervals of the total-variation absolute-value formula yields the unique cosine optimizer. Its long-time expansion is analytic. `verify.py` reconstructs the independent matrix propagation and reports `VERIFY_OK 18205 six_state_checks, sharp_envelope and asymptotic_ratio`. Sampled computations support, but do not prove, the continuous-parameter statements.

## Originality — PASS, subject to priority risk
He, Hutsalyuk, Mussardo and Stampiggi (arXiv:2609.13387; first public 2026-09-11) established the underlying central quantum stochastic walk, complete convolution/Fourier solution, and generic quantum speedup. The complete arXiv primary manuscript Sections 5.1--5.3 and appendices and corresponding author's thesis chapter 3.6 were materially inspected; its detailed results include the exact general group kernel, S2 example, slow-mode estimates, and larger-size numerical evidence. The current distinct statement is the all-parameter sharp optimization on S3, its unique phase and exact exponential prefactor. Ahmadi et al. (2003) treat a pure-unitary instantaneous mixing problem, not the dissipative optimum. Targeted published-record searches found no equivalent explicit optimum. The general source kernel may support an earlier implicit unindexed derivation; the direct PDF fetch failed but complete official arXiv HTML was materially read; originality is not independently certified.

## Value — PASS
The smallest nonabelian shuffling example has two distinct decay modes; optimally cancelling the three-cycle deviations gives a natural complete design theorem for how those modes compete. It produces an exact sharp mixing envelope that decays quadratically in the leading classical exponential, rather than merely demonstrating qualitative improvement. The result assumes time-retuned, unbounded coherent amplitude and does not assert robustness, finite-control optimality, or trace-distance gain.

Self-review: passed. Independent audit: not yet performed.
