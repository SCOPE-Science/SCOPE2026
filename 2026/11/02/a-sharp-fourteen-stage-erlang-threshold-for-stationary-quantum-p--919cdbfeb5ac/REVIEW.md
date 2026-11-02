# Scientific review: a sharp Erlang renewal quantum threshold

## Correctness — PASS

The exact domain is a finite-dimensional self-adjoint Hamiltonian, a normalized pure reset vector, independent Erlang interarrival clocks with integer shape and positive rate, and equilibrium-renewal sampling. The age density is the normalized survival law, yielding the characteristic function as a finite Erlang mixture. The spectral expansion reduces the stationary purity-minus-fidelity order to the sign of one real even scalar function. Polynomial multiplication is explicit, with a factor \(y^2\) cancelled only after its zero terms have been established. Exact rational Sturm sequences exclude positive roots for every shape from \(2\) through \(13\) and count exactly two for shape \(14\), where rational sign brackets isolate each one. An all-integer analytic angle witness establishes the reversed ordering for each \(k\geq14\). Exact age moments and the characteristic-function tail give the opposite signs near zero and infinity; no numerical interpolation is used to infer infinitely many instances. The embedded verifier executed all 92 exact assertions successfully, including independent rational transform identities. The main risks are interpreting the fidelity as that to the *pure reset* state and distinguishing clock rate from mean reset frequency; both are explicitly normalized.

## Originality — PASS, qualified

The closest work is Sevilla and Valdés-Hernández (arXiv:2209.05643, Sections 2.1, 3.1–3.3 and 4): its general stationary renewal state and purity/fidelity expressions and its explicit gamma reset family can be specialized to the present characteristic transform, so neither of those ingredients is new. No directly stated strict ordering for every system at shapes \(2\) through \(13\), first failure at \(14\), uniform analytic witnesses for all higher integer shapes, or exactly-two-crossing result for shape \(14\) was identified in the inspected primary text. Kulkarni and Majumdar (arXiv:2307.07485, Section III.2) note Poisson purity/fidelity equality for their interacting spins, a special case of the general \(k=1\) identity. Wald and collaborators (arXiv:2410.11497) treat discrete-time stochastic resetting rather than the present Erlang renewal classification. Research-record searches targeted the exact reset-state equality, Erlang waiting times, the threshold fourteen, and equivalent spectral/characteristic formulations. No found record subsumes the sharp theorem. Residual risk: an unlocated broader comparison or established classification could imply the threshold; absence from checked records is not a uniqueness or publication-priority proof. This is an assessment of the *evaluated global threshold*, not a claim to have invented the underlying renewal method.

## Value — PASS

Purity and fidelity are two natural, experimentally meaningful and directly comparable stationary observables. A universal ordering across all spectra and pure reset states for low clock shapes, followed by sharp first failure at shape fourteen, reveals an unexpected way that multi-stage renewal timing changes the relationship between mixedness and return to the reset state. The exact boundary and all-higher-shape witness convert implicit general renewal formulas into a checkable protocol-design restriction. A full sign classification for a natural family, not an arbitrary isolated numerical example or a routine normalization check, is the principal mathematical value. Finite and analytic portions are separated carefully.

## Closest literature and limits

- F. J. Sevilla and A. Valdés-Hernández, arXiv:2209.05643: generic renewal model, stationary moments, gamma family, qubit formulas; broad foundational coverage but no located sharp integer-stage sign classification.
- M. Kulkarni and S. N. Majumdar, arXiv:2307.07485: explicitly observes Poisson equality for a coupled-spin example; does not address renewal-stage threshold.
- S. Wald et al., arXiv:2410.11497: distinct discrete-time resetting framework; relevant context, not direct implication.

At shapes \(k\geq15\), the theorem guarantees a witness and at least two crossings, not the number of all crossings. It is silent on non-Erlang clocks, mixed resets and finite observation times. No external independent audit or exhaustive priority certification has been carried out.

Self-review: passed. Independent audit: not yet performed.
