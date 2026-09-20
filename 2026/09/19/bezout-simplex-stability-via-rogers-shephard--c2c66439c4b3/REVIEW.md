# Review: quantitative Bézout stability for simplices

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The argument was checked at the four points where a hidden normalization error would change the conclusion.

First, retaining a factor \(c\) in the restricted Bézout inequality produces \(c^{n-1}\), not \(c\), after the projected Minkowski inequality. With \(P=V_{n-1}(P_{v^\perp}K)\) and \(P_s=V_{n-1}(P_{v^\perp}K_v^s)\), this gives
\[
P_s\le c^{n-1}P\left(1-\frac{Ps}{nV(K)}\right)^{n-1}.
\]
Integrating recovers the exact case at \(c=1\) and yields the stated directional chord modulus.

Second, the covariogram normalization is consistent at both endpoints. The radial function of \(K-K\) in direction \(-v\) is \(\ell_K(v)\), and
\[
\int_{\mathbb R^n}g_K(x)\,dx=V(K)^2.
\]
The required scalar integral is
\[
\int_0^1\bigl((1-qr)^n-(1-q)^n\bigr)r^{n-1}dr
=q^{-n}\int_0^q y^n(1-y)^{n-1}dy,
\]
so the beta-function constant satisfies \(nB(n+1,n)=\binom{2n}{n}^{-1}\). At \(c=1\) the resulting lower bound becomes equality in Rogers–Shephard, as it must for a simplex.

Third, Böröczky's theorem is applied to the actual Rogers–Shephard deficit \(\delta\). Since the new estimate gives \(\delta\le1-\Psi_n(c)\), substituting this upper bound into the monotone stability estimate is valid.

Fourth, the asymptotic expansion
\[
1-\Psi_n(1+\varepsilon)
=n(n-1)^{1/n}\varepsilon^{1/n}+O_n(\varepsilon^{2/n})
\]
is consistent with \(\Psi_n(1)=1\). No optimality claim is made for the exponent or constants.

The relative-inradius extension was checked separately by retaining the same factor \(c\) in the inner-parallel-body argument. It requires the full two-body Bézout constant, not merely the restricted chord-intersection constant, and the public statement preserves that distinction.

## Originality

The recent Langharst–Wang paper proves the constant-one characterization for all dimensions and identifies the restricted chord-intersection tests, longest-chord equality, and relative-inradius equality as equivalent simplex criteria. Its stated results are qualitative; the relevant proof is an equality-forcing argument and does not state a quantitative stability theorem or a Banach–Mazur estimate.

Soprunov–Zvavitch introduced the mixed-volume Bézout inequality and an isomorphic version, while Saroglou–Soprunov–Zvavitch and related work established earlier qualitative characterizations or partial cases. These are treated as prior art. Searches using combinations of “Bézout inequality”, “mixed volume”, “stability”, “Banach–Mazur”, “simplex”, “Bézout constant”, “longest chord”, “relative inradius”, and “Rogers–Shephard” did not locate the explicit implication
\[
b_{\rm ch}(K)\le c
\Longrightarrow
\frac{V(K-K)}{\binom{2n}{n}V(K)}\ge\Psi_n(c),
\]
or the resulting Banach–Mazur stability bound.

Böröczky's 2005 quantitative Rogers–Shephard theorem is an essential prior ingredient and is not claimed as new. The contribution claimed here is the explicit quantitative bridge from the much smaller family of chord-intersection Bézout tests to Rogers–Shephard near-equality, plus the quantitative chord and inradius moduli.

Residual originality risk remains because the mixed-volume Bézout literature uses several constants and equivalent formulations, and the motivating characterization is very recent. No inaccessible source was identified whose title or abstract gives concrete evidence of the same stability theorem; older literature with different terminology could nevertheless contain a related estimate.

## Value

The result upgrades a newly completed qualitative simplex characterization into an explicit stability statement and does so using only the special test family needed by the new proof, rather than all auxiliary convex bodies. It links three natural affine-geometric quantities: the Bézout defect, the Rogers–Shephard difference-body deficit, and Banach–Mazur distance to the simplex class. The directional inequality also supplies a concrete witness: a deficient longest-chord efficiency forces a quantitatively large violation among the special Bézout tests.

## Limitations

The \(1/n\) stability exponent is not proved optimal. The numerical Banach–Mazur constant inherited from Böröczky is extremely large. The result does not classify near-extremizers more finely than Banach–Mazur proximity, and no independent audit has yet been performed.
