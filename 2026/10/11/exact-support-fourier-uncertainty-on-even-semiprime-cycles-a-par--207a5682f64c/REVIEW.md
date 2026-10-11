# Scientific review: exact-support parity law

## Correctness — PASS
The CRT decomposition gives exactly two \(p\)-point Fourier channels. If both are nonzero, each time support has at most \(k\) elements and Tao's prime-order bound forces at least \(2(p-k+1)\) total nonzero frequencies; if one vanishes, paired time support forces even \(k\) and at least \(p-k/2+1\) frequencies. Both sharp constructions have their exact declared time supports. For the explicit polynomial, all \(p\)-th roots are distinct and exactly the prescribed \(s-1\) are zeros; prime uncertainty rules out any missing coefficient. The crossover calculation and the \(p-7\) gap follow algebraically. The supplied code rechecks root and coefficient assertions for seven sample primes but is not an infinite proof.

## Originality — PASS (residual literature risk)
Loukaki's theorem treats parity-balanced Fourier minors and a stratified bound; it does not explicitly state the exact-cardinality profile or its jumps. Bonami–Ghobber's 2013 Theorem 4 handles equality cases for the at-most-support minimum, which does not imply the exact-support values for odd \(k\), where smaller supports may yield strictly smaller Fourier spectra. Previous published results treat three-point exact support, four-point indicators, and isolated small-group profiles. None of those statements implies this unified parameter-dependent exact profile. Remaining risk is an unindexed or implicitly equivalent general exact-support computation.

## Mathematical value — PASS
The complete first-half profile for infinitely many even semiprime cyclic groups is a natural harmonic invariant. It identifies a sharp parity obstruction, the phase boundary \(3r=p+1\) between two different extremizing constructions, and arbitrarily large upward jumps between adjacent exact support sizes. These jumps disappear entirely if “exactly” is replaced by “at most,” explaining why the finer invariant is necessary.

## Limits
All coefficients are complex; exact counts, rather than coefficient-vector classification, are proved. The prime-order uncertainty theorem is used as established literature, not proved from scratch. The finite verification code is supplementary.

Same-model review: passed. Independent audit: not yet performed.
