# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**  The core identity is exact.  If \(f\in\mathcal N_m\), then after the
disk automorphism sending \(f(0)\) to zero, generalized Schwarz gives
\(h=z^{m+1}\phi\).  For offsets \(k\le m\), the term \(h^2\) starts strictly beyond
degree \(m+1+k\), so the relevant section is exactly
\[
a+(1-|a|^2)z^{m+1}S_k\phi.
\]
Optimizing the remaining scalar \(a\) gives the necessary and sufficient threshold
\(2r^{m+1}M_k(r)\le1\); the converse is obtained by an extremal Schur function and
letting \(|a|\) approach one.

For the Schur functional, Szász's coefficient theorem is applied with
\(\mu_\ell=r^{k-\ell}\).  The required square-root polynomial is a rescaling of
\[
B_k(w)=\sum_{j=0}^k\binom{2j}{j}4^{-j}w^j.
\]
Eneström--Kakeya gives the stated zero-free range because consecutive coefficient
ratios are \((2j+2)/(2j+1)\).  Szász's equality statement then makes the bound exact.
The displayed equations for offsets \(0,1,2\) follow by substitution.  For offset
\(3\), the stronger \(|w|>4/3\) zero bound is checked by a reciprocal scaling and
the cubic Hurwitz criterion; the transformed cubic satisfies the strict Hurwitz
inequality \(105\cdot21>7\cdot83\).  Monotonicity of the resulting positive-power
polynomials gives uniqueness of every listed root.

Adversarial checks included the sign in the disk automorphism, the strict degree
inequality \(2(m+1)>m+1+k\), the reversal of the \(\mu_j\) coefficients in Szász's
functional, the scaling of the zero-free disk, and the boundary case where a zero
may lie on \(\mathbb T\) but not in \(\mathbb D\).  The asymptotic constants follow
by taking logarithms of the exact root equations and expanding at \(r=1\).

## Originality

**PASS, to the best of our knowledge.**  The direct 2026 source
(arXiv:2609.17114) treats only the Neil algebra \(f'(0)=0\).  It computes the first
two relevant section radii there and derives the universal Neil-algebra radius, but
does not formulate higher-order constraint algebras, the reduction to \(M_k(r)\),
the general fixed-offset root law, or the offset-two and offset-three formulas
above.  The paper also says that, to the authors' knowledge, it is the first attempt
to improve the Fejér--Rogosinski radius for a proper subalgebra of
\(H^\infty(\mathbb D)\).

Searches by the source identifier, “Neil algebra”, higher-order/vanishing-derivative
constraints, missing initial coefficients, Fejér--Rogosinski sections, and the
displayed root equations did not locate an equivalent theorem.  The current SCOPE
archive was searched by the same object and claim families and no overlap was
located.

Kovalev's 2025 paper (arXiv:2507.04544) gives a modern statement of the classical
Szász theorem and sharp bounds for short coefficient segments in the unrestricted
Schur class.  It supplies an ingredient, not the constrained-section reduction.
The classical literature cited by Das--Sarkar (Rogosinski, Schur--Szegő, Szász,
Nabetani) concerns unrestricted section theory or related mapping generalizations.

Two older sources remain the main residual literature risk.  Rhoda Manning,
*On the Derivatives of the Sections of Bounded Power Series*, Ann. of Math. 43
(1942), 617--622, was identified but its full text was not independently inspected;
its title concerns derivatives of sections rather than prescribed vanishing
derivatives of the original function, but it is close enough to merit caution.
Likewise the full texts of Nabetani's 1935 papers on sections were not independently
checked.  Because the Neil-algebra source is very recent, unindexed concurrent
extensions are also possible.

## Value

**PASS.**  The result turns the isolated Neil-algebra calculation into a structural
higher-order theorem.  It identifies exactly why the first \(m+1\) nonconstant
sections are special (the quadratic Schwarz term has not yet entered), connects
their sharp radii to classical coefficient extremals, and produces explicit new
families of exact radii.  The fixed-offset asymptotic
\[
1-R_{m+1+k}^{(m)}
\sim \frac{\log(2C_k(1))}{m}
\]
gives a hierarchy of endpoint constants rather than a single numerical extension.

## Limitations

The optimal radius valid simultaneously for all section orders of
\(\mathcal N_m\), \(m>1\), is not determined.  The exact Szász formula is used only
where the corresponding extremal polynomial is proved zero-free at the candidate
radius.  Sections beyond offset \(m\) contain nonlinear powers of the Schwarz
factor and are outside the reduction.  The uninspected Manning and Nabetani full
texts remain explicit originality risks.
