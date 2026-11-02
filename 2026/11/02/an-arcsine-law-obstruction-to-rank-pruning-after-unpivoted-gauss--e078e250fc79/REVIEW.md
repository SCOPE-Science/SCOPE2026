# Self-review

## Correctness — PASS

The announced event is conditioned on surviving the first sketch and thus avoids treating its exceptional branch as a normal final factorization. In exact arithmetic the first unpivoted QR block spans the rank-two image, so the second residual is identically zero. The exact row-norm formulas and Cauchy ratio determine a *finite-parameter* ideal pruning probability; the chi-square bound covers the first-stop discrepancy. The resulting \((2/\pi)\arcsin c\) limit is proved by ordinary limits of arctangent endpoints. Eckart–Young establishes the optimal rank-one tolerance, while the already-computed block's singular values establish the zero-new-matvec remedy. Symbolic, rational, QR/SVD, and random tests checked the key identities and normalizations. None of the Monte Carlo outcomes were used to infer the infinite theorem.

## Originality — PASS within stated access limits

The motivating algorithm [1] derives a Pythagorean relation and row-energy pruning but does not quantify this particular rank-optimality obstruction. Relevant earlier randomized numerical-rank, QR and UTV sources [4–7] use different truncation diagnostics and do not state the source algorithm's Cauchy/arcsine probability. Searches of mathematical research records and accessible earlier claims yielded no dominating statement. The classical Cauchy ratio, SVD remedy, and known limits of unpivoted rank diagnostics are not claimed as discoveries. Foster's 1990 specialized QR-diagonal study [8] could not be read fully; it is explicitly retained as a priority risk.

## Mathematical value — PASS

The source's rank-pruning rule is intended to decouple block width and returned numerical rank. A *nonvanishing* excess-rank probability, tunable through every value in \((0,1)\), is an exact reliability benchmark for that explicit design choice, and distinguishes noise in residual detection from geometrical delocalization of singular energy across a QR basis. Postprocessing the same small coefficient block by SVD gives a directly checkable remedy with no further operator actions. This is a motivated numerical linear algebra stability-of-rank-selection problem, not merely a probability exercise.

## Closest sources and scope limits

Smith–Do–Chen (2026), §§3.1–3.2 and Algorithms 2–3, code [2–3]; Meier–Nakatsukasa (2021), Martinsson–Voronin (2015), randUTV (2017), Grigori–Xue (2025); abstract-only Foster (1990). See references and full definitions in `RESULT.md`. No claims about adjoint-free row-estimate sampling, arbitrary rank or block width, finite-precision MATLAB behavior near underflow, or exhaustive historical priority are made.

Self-review: passed. Independent audit: not yet performed.
