# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

PASS.

The statement reduces the new regime to two exact endpoint norms and one standard interpolation step.

- At $p=2$, Cauchy--Binet plus Hadamard's Gram inequality gives norm $1$.
- At $p=\infty$, Hadamard's determinant bound gives at most $n^{n/2}$ for every coordinate minor, while the unnormalised Fourier matrix attains $n^{n/2}$.
- Multilinear complex interpolation between these endpoints gives the upper bound $n^{n(1/2-1/p)}$ for $2<p<\infty$.
- The same Fourier matrix, supported on $n$ coordinates, has row $\ell^p$ norm $n^{1/p}$ and one nonzero maximal minor of modulus $n^{n/2}$, attaining the upper bound.

The argument can be run on finite truncations and then passed to $\ell^p$, avoiding any endpoint-density subtlety.  Numerical spot checks on random finite complex matrices for $n=2,3,4$ and several $p\ge2$ were consistent with the sharp formula, while Fourier frames attained it to numerical precision.  These checks are supplementary; the proof is exact.

The real-scalar corollaries use only $C^{\mathbb R}_{n,p}\le C^{\mathbb C}_{n,p}$, the source paper's $\{\pm1\}$ determinant witness, and the coordinate-frame lower bound $1$.  Equality for real orders admitting a Hadamard matrix follows because the real lower bound then equals the complex upper bound.

## Originality

PASS, to the best of our knowledge.

The recent source arXiv:2608.00983 was inspected through its theorem, proof, supercritical remark, open-problem section, and scalar-sensitive surrounding discussion.  It states only the $p\le2$ exact constant, gives a real $\{\pm1\}$ lower bound for $p>2$, and leaves the supercritical sharp constants, continuity at $2^+$, and fixed-$n$ behavior open.  No later arXiv version was present at the time of review.

The complex-Hadamard literature was checked for the needed endpoint fact.  Tadej--Życzkowski explicitly give the Fourier matrix construction in every order and distinguish complex from real Hadamard matrices.  Searches using Plücker, exterior-power, compound-matrix, minors, $\ell^p$, determinant-norm, Fourier, and complex-Hadamard formulations did not locate the exact Plücker multilinear norm formula above.

Residual risk: the formula is built from classical ingredients, so an older equivalent result could exist under tensor-norm or compound-matrix terminology.  The most plausible uninspected sources are Defant--Floret (1993) and Ryan (2002), whose full texts were not exhaustively checked.  Feldman's paper itself cites these books for nearby tensor-product facts while saying it had not located its sharp constant in print.  Accordingly, originality is claimed only to the best of our knowledge.

## Value

PASS.

The result does more than add a parameter case.  It completely determines the supercritical sharp constant over complex scalars, resolves the source paper's continuity and asymptotic questions there, proves $2^+$ continuity for the real interpretation as well, and isolates the classical maximal-determinant obstruction as a genuinely real-scalar phenomenon.  It also identifies an explicit extremizing mechanism (Fourier complex Hadamard frames) and a reusable endpoint-interpolation template for exterior-coordinate norm problems.

## Scientific limitations

The source preprint does not place a single explicit scalar-field convention next to Theorem 2.1.  Its use of $\mathbb C^\times$ projectivization and multilinear complex interpolation makes the complex case natural, but if an author intended that particular sharp-constant discussion to be exclusively real, the complex formula should be read as a complementary theorem rather than a correction.  The real sharp constant for orders without a real Hadamard matrix is not determined here.
