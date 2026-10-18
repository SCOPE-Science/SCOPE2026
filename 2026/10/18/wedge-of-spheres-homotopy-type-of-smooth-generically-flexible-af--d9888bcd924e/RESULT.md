# Wedge-of-spheres homotopy type of smooth generically flexible affine quotients

## Finding
For each integer \(n\geq 1\), let \(X_n\) be the smooth affine hypersurface over \(\mathbb C\)
\[
 x^2y+z^3w^2\prod_{i=1}^{n}u_i^2=1
 \quad\subset\quad \mathbb A^{n+4},
\]
and give it the \(\mathbb G_m\)-action with weights \((1,-2,2,-2,-1,0,\ldots,0)\) on \((x,y,z,w,u_1,u_2,\ldots,u_n)\). Let \(Y_n=X_n/\!/\mathbb G_m\), and let \(D_n\subset Y_n\) be the image of \(\{x=0\}\).

Then \(D_n\cong\mathbb A^1\times(\mathbb G_m)^n\), its normal line bundle in \(Y_n\) is trivial, and \(Y_n\setminus D_n\cong\mathbb A^{n+2}\). Consequently, in the classical complex topology,
\[
 \boxed{\quad Y_n(\mathbb C)\simeq \bigvee_{r=0}^{n}\bigvee^{\binom nr} S^{r+2}.\quad}
\]
In particular, \(Y_n(\mathbb C)\) is simply connected, its integral cohomology is torsion-free with \(H^0\cong\mathbb Z\), \(H^1=0\), and
\[
 H^{r+2}(Y_n(\mathbb C);\mathbb Z)\cong\mathbb Z^{\binom nr}\quad (0\leq r\leq n),
\]
with all other cohomology groups zero. Every cup product of two positive-degree classes is zero. Its Poincaré polynomial is \(1+t^2(1+t)^n\). These are homotopy statements, not merely equalities of Betti numbers.

## Assumptions and scope
All varieties and quotients are taken over \(\mathbb C\). The index \(n\) is any integer at least one; the complex dimension of \(Y_n\) is \(n+2\). The quotient is the affine categorical quotient; the two explicit quotient charts below also show that it is a geometric quotient by the displayed torus. Classical homotopy equivalence is denoted by \(\simeq\). In the wedge expression, the multiplicity of \(S^{r+2}\) is exactly \(\binom nr\).

The smoothness, generic flexibility, non-flexibility, and existence of the invariant divisor in this family are prior results of Nikitina; none of those properties is asserted as new here. The finding is the complete integral homotopy classification and its explicitly identified two-stratum source.

## Proof
**1. Complement chart.** Every point of \(X_n\) with \(x\neq0\) has a unique torus representative with \(x=1\). Its remaining invariant coordinates are
\[
 Z=z/x^2,\quad W=x^2w,\quad V=xu_1,\quad U_i=u_i\ (i\ge2).
\]
The hypersurface equation uniquely determines the normalized \(y\)-coordinate as
\[
 x^2y=1-Z^3W^2V^2\prod_{i=2}^n U_i^2.
\]
Thus \(X_{n,x}\cong\mathbb G_m\times\mathbb A^{n+2}\) equivariantly, where the torus acts on the first factor; taking the quotient gives \(Y_n\setminus D_n\cong\mathbb A^{n+2}\). The equation forces \(u_1\neq0\) whenever \(x=0\), so the complement of this chart really is exactly \(D_n\).

**2. Boundary chart and intrinsic structure.** On \(\{u_1\neq0\}\), normalize \(u_1=1\) using the unique torus element \(t=u_1\). Write the invariant coordinates
\[
 q=xu_1,\quad b=y/u_1^2,\quad c=zu_1^2,\quad d=w/u_1^2,\quad U_i=u_i\ (i\ge2).
\]
The quotient chart has equation
\[
 q^2b+c^3d^2\prod_{i=2}^nU_i^2=1.
\]
All points of \(D_n\) lie in this chart, where \(D_n\) is exactly \(q=0\); hence it is a smooth Cartier divisor with a *globally trivial normal line bundle*, trivialized by its local defining function \(q\) on an entire open neighborhood containing \(D_n\). Within \(D_n\), the variables \(c,d,U_2,\ldots,U_n\) are nonzero and satisfy
\[
 c^3d^2\prod_{i=2}^nU_i^2=1,
\]
while \(b\) is unrestricted. Put \(s=(cd\prod_{i=2}^nU_i)^{-1}\). Then, uniquely,
\[
 c=s^2,\qquad d=s^{-3}\prod_{i=2}^nU_i^{-1}.
\]
Indeed these identities follow on the locus by \(c^3(d\prod U_i)^2=1\), and conversely solve that relation for all \(s,U_i\neq0\). Consequently \((b,s,U_2,\ldots,U_n)\) are algebraic coordinates on \(D_n\cong\mathbb A^1\times(\mathbb G_m)^n\). This simultaneously establishes connectedness, smoothness, and normal triviality without invoking a Picard-group calculation.

**3. Homotopy identification.** Work with underlying complex manifolds. Take a smooth tubular neighborhood \(N\) of the closed smooth hypersurface \(D_n\subset Y_n\); its disk and circle bundles model the complex normal line bundle. Set \(U=Y_n\setminus D_n\). The open cover \(Y_n=U\cup N\) is a homotopy pushout of \(U\longleftarrow U\cap N\longrightarrow N\). By Step 1, \(U\) is contractible. The inclusion \(U\cap N\to N\) is homotopic, via the tubular deformation retraction, to the circle-bundle projection \(S(\nu)\to D_n\). Replacing \(U\) with a point in the homotopy pushout therefore identifies \(Y_n\) up to homotopy with the homotopy cofiber of \(S(\nu)\to D_n\). This cofiber is the Thom space \(\operatorname{Th}(\nu)\) of the normal line bundle: replace its disk bundle by its zero-section deformation retract. The normal bundle \(\nu\) is trivial by Step 2, so
\[
 Y_n(\mathbb C)\simeq\operatorname{Th}(\nu)\simeq \Sigma^2(D_n(\mathbb C)_+)\simeq\Sigma^2(((S^1)^n)_+).
\]
Here a subscript \(+\) means adjoining a disjoint base point, and \(\Sigma\) is reduced suspension. The standard suspension splitting \(\Sigma(A\times B)\simeq\Sigma A\vee\Sigma B\vee\Sigma(A\wedge B)\) for connected based CW complexes, iterated over the \(n\) circle factors, gives
\[
 \Sigma^2(((S^1)^n)_+)\simeq\bigvee_{r=0}^n\bigvee^{\binom nr}S^{r+2}.
\]
This is an *unstable* homotopy equivalence. The asserted integral groups, trivial positive-degree cup products, and simply connectedness follow from the wedge decomposition.

## Verification
The two quotient charts are explicit algebraic isomorphisms, not point-count experiments. Their displayed coordinate transformations can be verified by checking torus weights and substituting them into the defining equation. The boundary parametrization is inverse in both directions; its key integer identity is \(3\cdot2+2\cdot(-3)=0\). The normal trivialization uses the invariant coordinate \(q=xu_1\) on the full chart where \(u_1\neq0\). The topological step uses the standard open-cover homotopy-pushout and Thom-space constructions, with no finite enumeration needed.

The included checker `CHECK.py` evaluates weight identities, both affine-chart monomial substitutions, torus parametrization exponents and the first twelve binomial Betti profiles. Those checks corroborate the exact algebraic identities; they are **not** offered as a proof of the all-\(n\) homotopy equivalence, which is provided in Step 3.

## Relationship to prior work
Nikitina, *Generically Flexible Varieties with an Invariant Divisor*, arXiv:2610.05344v1, Section 3, introduces the same hypersurface, torus weights and quotient, proves smoothness and generic but not full flexibility, constructs the invariant divisor, and gives polynomial generators and relations for the invariant ring. Her paper does **not state** the affine-space complement, torus-cylinder boundary, trivial normal bundle, integral homotopy type, Betti polynomial, or cohomology-ring conclusion. Those deductions from the explicit geometry are the contribution assessed here. Gaifullin, arXiv:2507.14745v1, treats an earlier, different, generally singular family of generically flexible affine quotients with four invariant divisors; its orbit-stratification results do not imply this homotopy classification. The cofiber/Thom-space and suspended-product splitting used in Step 3 are standard algebraic topology, not claimed as new.

## Limitations
The theorem concerns only these explicitly weighted complex affine quotients. It does not describe their algebraic \(\mathbb A^1\)-homotopy types, their entire automorphism groups, or the full orbit decomposition of their special automorphism groups. The existence of the smooth non-flexible family and of its invariant divisor are prior literature. Novelty of the *homotopy classification* is asserted only against the examined sources and targeted searches, not as a proof of global uniqueness; an equivalent unindexed computation remains possible.

## References
1. A. Nikitina, *Generically Flexible Varieties with an Invariant Divisor*, arXiv:2610.05344v1 (submitted 2026-10-04), https://arxiv.org/html/2610.05344v1 .
2. S. Gaifullin, *Generically flexible affine varieties with invariant divisors*, arXiv:2507.14745v1 (submitted 2025-07-19), https://arxiv.org/html/2507.14745v1 .
3. Standard tubular-neighborhood, homotopy-pushout, Thom-space, and suspension-splitting results for finite CW complexes; the specific application and coordinate identifications are given above.
