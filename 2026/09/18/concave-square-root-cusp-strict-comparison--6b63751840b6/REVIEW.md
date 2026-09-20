# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked directly against Theorem 2.6 of Larsen (2026). That theorem requires a continuous positive coefficient with strong existence and pathwise uniqueness, local Lipschitz regularity away from the cusp, and a function \(Q\) satisfying logarithmic one-sided integral bounds together with
\[
\Delta(M,D)^2\le DQ(M/D)\Gamma(M,D)^2.
\]

For a nondecreasing concave \(\phi\) with \(\phi(0)=0\) and \(\phi(r)\le K\sqrt r\), concavity implies both that \(\phi(r)/r\) decreases and that \(\phi\) is globally \(1/2\)-Hölder with constant at most \(\sqrt2K\). This verifies pathwise uniqueness for both \(1+\phi(x^+)\) and \(1+\phi(|x|)\), while positivity and continuity give the remaining existence assumptions. Local Lipschitz regularity off zero follows from concavity.

The key two-variable estimate was checked separately in the central and tail regimes. For \(|M/D|\le1\), the \(1/2\)-Hölder bound gives \(\Delta^2\le2K^2D\). For \(z=M/D\ge1\), concavity gives
\[
|\Delta|
\le K\sqrt{\frac{2D}{z}},
\]
and the negative tail follows by vanishing of the one-sided cusp or evenness of the symmetric cusp. Thus
\[
Q(z)=\frac{4K^2}{1+|z|}
\]
dominates \(\Delta^2/D\) in all regimes and has exactly logarithmic one-sided integrals.

The factor \(\Gamma\) was also checked explicitly. On the one-sided central region it is \(1+(1/2-z)\phi(D(z+1/2))\); on the symmetric central region it is \(1+b\phi(Da)+a\phi(Db)\). Outside the central region,
\[
\Gamma-1=a\phi(Db)-b\phi(Da)\ge0
\]
because \(\phi(r)/r\) is decreasing. Hence \(\Gamma\ge1\), completing Larsen's hypothesis.

For the logarithmically damped example,
\[
\phi_\gamma(r)=r^{1/2}[\log(e/r)]^{-\gamma}
\]
before the cutoff, direct differentiation gives
\[
\phi_\gamma''(r)
=
r^{-3/2}L(r)^{-\gamma}
\left[-\frac14+\frac{\gamma(\gamma+1)}{L(r)^2}\right].
\]
The chosen cutoff has \(L=2(\gamma+1)\), so the second derivative is negative up to the cutoff and the constant continuation preserves concavity. The Sobolev classification follows from
\[
|\phi_\gamma'|^p\asymp r^{-p/2}L(r)^{-\gamma p}.
\]
In particular, the \(p=2\) integral is finite exactly when \(\gamma>1/2\). The failure of the Yamada-Ogura modulus criterion follows because every admissible modulus dominates \(\phi_\gamma\), while
\[
\int_0^\varepsilon [\log(e/h)]^{2\gamma}\,dh<\infty.
\]

No numerical experiment is needed for the proof.

## Originality

Larsen (2026) proves the general two-variable Lyapunov criterion and verifies it for the pure square-root one-sided and symmetric cusps. The same paper proves the sharp power-family threshold and emphasizes that neither \(W^{1,p}_{\mathrm{loc}}\), \(p<2\), nor Hölder regularity alone suffices.

Yamada-Ogura (1981) provide the classical modulus condition. Yamada (1986) provides a broader factorization theorem and includes positive \(W^{1,2}_{\mathrm{loc}}\) coefficients after localization. Fang-Zhang (2005) and Lan-Wu (2014) give general nonconfluence criteria; Larsen's literature comparison states that their conditions do not relax the relevant classical modulus condition after specialization to the present one-dimensional driftless equation.

Targeted searches used combinations of strict comparison, nonconfluence, noncoalescence, concave diffusion coefficient, square-root cusp, logarithmic cusp, logarithmically damped square root, regularly varying cusp, Yamada-Ogura modulus, and the exact source title. The current SCOPE archive was also searched by the source paper, mathematical object, and synonymous claim families. No inspected source or prior SCOPE record stated the concave square-root reduction or the displayed logarithmically damped family.

The principal residual originality risk is the full 1986 Yamada factorization theorem and related older one-dimensional nonconfluence literature. Only the bibliographic statement and its role as summarized in Larsen were available here; the full theorem was not inspected. It could contain an equivalent criterion under different factorization language. Accordingly, the originality judgment is only to the best of our knowledge, and the record does not claim that the logarithmically damped family lies outside every Yamada-type factorization.

## Value

The result turns a two-variable condition involving the midpoint-gap geometry of two synchronous solutions into a simple one-variable shape test: concavity plus a square-root envelope. It therefore supplies an easily checkable structural class rather than another isolated cusp example.

The logarithmically damped family shows that the positive side of the square-root threshold contains a nontrivial Sobolev boundary. For \(0<\gamma\le1/2\), strict comparison holds while the classical Yamada-Ogura modulus condition fails and the coefficient remains outside \(W^{1,2}_{\mathrm{loc}}\). The transition at \(\gamma=1/2\) is exact for local square-integrability of the derivative. This separates shape information from regularity-class membership in the grey zone highlighted by Larsen.

## Limitations

The criterion is sufficient rather than necessary and covers a single concave cusp at zero. The logarithmic family does not come with a converse when the logarithmic factor is reversed or enlarged. The broader Yamada (1986) factorization theorem was not fully inspected, so older equivalent coverage remains a concrete originality risk. No multidimensional, drifted, discontinuous-coefficient, or multiple-cusp extension is claimed.
