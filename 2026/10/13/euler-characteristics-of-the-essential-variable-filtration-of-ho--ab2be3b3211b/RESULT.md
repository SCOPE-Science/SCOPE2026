# Euler characteristics of the essential-variable filtration of homogeneous forms
## Finding
Let \(V\) be a complex vector space of dimension
\[
m\ge2,
\]
and let
\[
d\ge3.
\]
For
\[
1\le r\le m,
\]
define
\[
\mathcal S^{\le r}_{m,d}
\subset
\mathbb P(\operatorname{Sym}^dV^*)
\]
to be the projective locus of degree-\(d\) homogeneous forms that, after a linear change of coordinates, depend on at most \(r\) variables.

Equivalently, if
\[
C_F:V\longrightarrow \operatorname{Sym}^{d-1}V^*,
\qquad
v\longmapsto \partial_vF,
\]
is the first catalecticant, then
\[
\mathcal S^{\le r}_{m,d}
=
\{[F]:\operatorname{rank}C_F\le r\}.
\]

Then
\[
\boxed{
\chi_{\mathrm{top}}(\mathcal S^{\le r}_{m,d})
=
\sum_{s=1}^{\min(r,d)}
\binom ms\binom{d-1}{s-1}
}.
\]

Put
\[
\mathcal S^{\le0}_{m,d}=\varnothing
\]
and let
\[
E_r
=
\mathcal S^{\le r}_{m,d}
\setminus
\mathcal S^{\le r-1}_{m,d}
\]
be the exact essential-dimension stratum. Then
\[
\boxed{
\chi_c(E_r)
=
\binom mr\binom{d-1}{r-1}
\qquad
(1\le r\le\min(m,d))
}
\]
and
\[
\boxed{
\chi_c(E_r)=0
\qquad
(d<r\le m).
}
\]

The last vanishing is not an emptiness statement. For every
\[
1\le r\le m,
\]
the Fermat-type form
\[
x_1^d+\cdots+x_r^d
\]
has essential dimension exactly \(r\). Hence when \(m>d\), the nonempty strata of essential dimensions
\[
d+1,\ldots,m
\]
all have compactly supported Euler characteristic zero.

In particular, once
\[
r\ge d,
\]
the cumulative Euler characteristic has already reached the ambient value
\[
\chi_{\mathrm{top}}\!\left(\mathbb P(\operatorname{Sym}^dV^*)\right)
=
\binom{m+d-1}{d},
\]
even if
\[
r<m
\]
and the subspace variety is still proper.

## Assumptions and scope
The base field is \(\mathbb C\). The invariant on the projective cumulative loci is ordinary topological Euler characteristic. The exact essential-dimension strata are quasi-projective, so compactly supported Euler characteristic is used.

The restriction
\[
d\ge3
\]
is intentional. The quadratic case is the symmetric determinantal rank filtration and is outside the present claim.

The essential dimension of \(F\) is the least dimension of a linear subspace \(U\subset V^*\) such that
\[
F\in\operatorname{Sym}^dU.
\]
It equals the rank of the first catalecticant. Indeed, if \(F\in\operatorname{Sym}^dU\), then \(U^\perp\subset V\) lies in the kernel of \(C_F\), so the catalecticant rank is at most \(\dim U\). Conversely, if \(K=\ker C_F\), choose coordinates adapted to \(K\); the identities \(\partial_vF=0\) for all \(v\in K\) show that \(F\) contains no variables dual to \(K\), hence \(F\in\operatorname{Sym}^d(K^\perp)\).

The cumulative locus is closed. It is the image of the natural proper map
\[
\mathbb P(\operatorname{Sym}^d\mathcal U)
\longrightarrow
\mathbb P(\operatorname{Sym}^dV^*),
\]
where \(\mathcal U\) is the tautological rank-\(r\) bundle over \(\operatorname{Gr}(r,V^*)\).

## Proof
Choose a basis
\[
x_0,\ldots,x_{m-1}
\]
of \(V^*\), and choose an integer
\[
B>d.
\]
Let \(\mathbb C^*\) act diagonally by
\[
z\cdot x_j=z^{B^j}x_j.
\]
A degree-\(d\) monomial
\[
x^\alpha=x_0^{\alpha_0}\cdots x_{m-1}^{\alpha_{m-1}},
\qquad
\sum_j\alpha_j=d,
\]
has weight
\[
w(\alpha)=\sum_{j=0}^{m-1}\alpha_jB^j.
\]
Because
\[
0\le\alpha_j\le d<B,
\]
uniqueness of base-\(B\) expansion shows that distinct degree-\(d\) monomials have distinct weights. Therefore the fixed locus of the action on
\[
\mathbb P(\operatorname{Sym}^dV^*)
\]
consists exactly of the monomial coordinate points.

The variety
\[
\mathcal S^{\le r}_{m,d}
\]
is invariant under \(\operatorname{GL}(V)\), hence under this one-parameter subgroup. A monomial
\[
x^\alpha
\]
has essential dimension equal to the number of variables occurring with positive exponent. To see this, if its support has size \(s\), it visibly lies in the symmetric power of the \(s\)-dimensional span of those variables. On the other hand, its nonzero first derivatives with respect to the support variables are pairwise distinct monomials, so the first catalecticant has rank \(s\).

Thus the fixed points of
\[
\mathcal S^{\le r}_{m,d}
\]
are precisely the degree-\(d\) monomials whose support size is at most \(r\).

For a fixed support size \(s\), choose the variables in
\[
\binom ms
\]
ways. The positive exponent vectors on those variables are the compositions of \(d\) into \(s\) positive parts, of which there are
\[
\binom{d-1}{s-1}.
\]
Hence
\[
\#(\mathcal S^{\le r}_{m,d})^{\mathbb C^*}
=
\sum_{s=1}^{\min(r,d)}
\binom ms\binom{d-1}{s-1}.
\]

For any complex algebraic variety \(Y\) with an algebraic \(\mathbb C^*\)-action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
A proof uses Rosenlicht stratification of the nonfixed locus and additivity: after refining by stabilizer type, each nonfixed piece is a locally trivial bundle with fiber a finite quotient of \(\mathbb C^*\), hence with compactly supported Euler characteristic zero.

Since the cumulative loci are projective,
\[
\chi_c=\chi_{\mathrm{top}},
\]
which proves the first formula.

For the exact strata, additivity gives
\[
\chi_c(E_r)
=
\chi_{\mathrm{top}}(\mathcal S^{\le r}_{m,d})
-
\chi_{\mathrm{top}}(\mathcal S^{\le r-1}_{m,d}).
\]
If
\[
r\le d,
\]
the difference is exactly
\[
\binom mr\binom{d-1}{r-1}.
\]
If
\[
r>d,
\]
the cumulative fixed-point count no longer changes, so
\[
\chi_c(E_r)=0.
\]

Finally, for every \(r\le m\), the form
\[
x_1^d+\cdots+x_r^d
\]
has linearly independent first derivatives
\[
dx_1^{d-1},\ldots,dx_r^{d-1},
\]
so its essential dimension is exactly \(r\). This proves that the zero-Euler strata above the degree are genuinely nonempty.

## Verification
The bundled checker exhausts
\[
2\le m\le9,
\qquad
3\le d\le9.
\]
For every pair \((m,d)\), it enumerates all degree-\(d\) exponent vectors, computes support size, and verifies every cumulative and exact formula for
\[
1\le r\le m.
\]

It also verifies the hockey-stick identity at the ambient boundary:
\[
\sum_{s=1}^{\min(m,d)}
\binom ms\binom{d-1}{s-1}
=
\binom{m+d-1}{d}.
\]

These finite computations are regression evidence only. The all-parameter theorem follows from base-\(B\) weight separation, the support-size characterization of monomial essential dimension, and Euler localization.

## Relationship to prior work
Landsberg and Weyman introduced tensor subspace varieties as loci of tensors contained in prescribed-dimensional factor subspaces and described their Grassmannian-bundle desingularizations. The present family is the symmetric one-factor analogue inside
\[
\mathbb P(\operatorname{Sym}^dV^*).
\]

Landsberg and Ottaviani developed catalecticant and vector-bundle methods for symmetric tensors and Veronese secants. Their full text contains no Euler-characteristic discussion.

The quadratic specialization
\[
d=2
\]
is the symmetric determinantal rank filtration and is intentionally excluded from the present claim. Ordinary tensor subspace varieties have different fixed-point behavior because their monomial coordinates have one index in each tensor factor rather than a support statistic inside one symmetric power.

Targeted searches for symmetric subspace varieties, bounded essential variables, first-catalecticant rank loci, Euler characteristic, Poincaré polynomial, and exact essential-dimension strata did not locate the formulas above.

## Limitations
Euler characteristic is coarse. The vanishing
\[
\chi_c(E_r)=0
\]
for \(r>d\) does not imply that those nonempty strata are topologically simple.

The result treats ordinary symmetric powers. Partially symmetric tensors with several symmetric factors have a multigraded support statistic and are not claimed here.

The proof is short once the subspace-variety viewpoint is combined with a separating one-parameter subgroup. An older or unindexed observation may therefore contain the same fixed-point count.

## References
J. M. Landsberg and Jerzy Weyman, *On the ideals and singularities of secant varieties of Segre varieties*, arXiv:math/0601452, first submitted 18 January 2006; *Bulletin of the London Mathematical Society* 39 (2007), 685--697.

J. M. Landsberg and Giorgio Ottaviani, *Equations for secant varieties of Veronese and other varieties*, arXiv:1111.4567, first submitted 19 November 2011; *Annali di Matematica Pura ed Applicata* 192 (2013), 569--606, DOI 10.1007/s10231-011-0238-6.
