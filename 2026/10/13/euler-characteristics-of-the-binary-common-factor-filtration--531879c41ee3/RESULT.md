# Euler characteristics of the binary common-factor filtration
## Finding
Let
\[
1\le m\le n.
\]
For
\[
0\le k\le m,
\]
define the projective common-factor locus
\[
R^{\ge k}_{m,n}
=
\left\{
([f],[g])
\in
\mathbb P(\operatorname{Sym}^m\mathbb C^2)
\times
\mathbb P(\operatorname{Sym}^n\mathbb C^2)
:
\deg\gcd(f,g)\ge k
\right\}.
\]
Here
\[
R^{\ge0}_{m,n}
=
\mathbb P^m\times\mathbb P^n.
\]

For every
\[
1\le k\le m,
\]
the ordinary topological Euler characteristic is
\[
\boxed{
\chi_{\mathrm{top}}(R^{\ge k}_{m,n})
=
(m+1)(n+1)-k(k+1).
}
\]

Thus the entire common-factor filtration has a quadratic Euler profile depending only on the threshold \(k\).

Define the exact gcd-degree strata by
\[
G_k
=
R^{\ge k}_{m,n}\setminus R^{\ge k+1}_{m,n}
\qquad(0\le k<m),
\]
and
\[
G_m=R^{\ge m}_{m,n}.
\]
Then
\[
\boxed{
\chi_c(G_0)=2,
}
\]
\[
\boxed{
\chi_c(G_k)=2(k+1)
\qquad
(1\le k<m),
}
\]
and
\[
\boxed{
\chi_c(G_m)
=
(m+1)(n-m+1).
}
\]

In particular, the projective locus of coprime pairs of nonzero binary forms has compactly supported Euler characteristic \(2\), independently of both degrees.

## Assumptions and scope
The base field is \(\mathbb C\).

A point of
\[
\mathbb P(\operatorname{Sym}^m\mathbb C^2)
\times
\mathbb P(\operatorname{Sym}^n\mathbb C^2)
\]
is a pair of nonzero binary forms, each considered up to its own nonzero scalar.

The degree of the gcd is the degree of a homogeneous greatest common divisor. The condition
\[
\deg\gcd(f,g)\ge k
\]
is closed: equivalently, the Sylvester matrix has the corresponding rank defect, or one may realize the locus as the projective image of the multiplication incidence with a common degree-\(k\) factor.

The cumulative loci are projective, so ordinary and compactly supported Euler characteristic agree there. The exact strata are quasi-projective, so compactly supported Euler characteristic is used.

## Proof
Choose coordinates \(x,y\) on \(\mathbb C^2\) and let \(\mathbb C^*\) act by
\[
z\cdot x=zx,
\qquad
z\cdot y=y.
\]
On
\[
\mathbb P(\operatorname{Sym}^d\mathbb C^2),
\]
the monomials
\[
x^{d-i}y^i,
\qquad
0\le i\le d,
\]
have pairwise distinct weights. Hence the fixed locus consists exactly of the \(d+1\) monomial coordinate points.

The common-factor loci are invariant under this action, because a linear change of variables preserves gcd degree. Therefore the fixed points of \(R^{\ge k}_{m,n}\) are precisely those monomial pairs
\[
\left(
[x^{m-i}y^i],
[x^{n-j}y^j]
\right),
\qquad
0\le i\le m,
\quad
0\le j\le n,
\]
whose gcd has degree at least \(k\).

For such a pair,
\[
\deg\gcd
\left(
x^{m-i}y^i,
x^{n-j}y^j
\right)
=
\min(i,j)+\min(m-i,n-j).
\]
Put
\[
\delta=j-i.
\]
Because \(m\le n\), this becomes
\[
\deg\gcd
=
\begin{cases}
m+\delta,&\delta<0,\\
m,&0\le\delta\le n-m,\\
n-\delta,&\delta>n-m.
\end{cases}
\]
Hence
\[
\deg\gcd\ge k
\]
is equivalent to the strip condition
\[
k-m\le j-i\le n-k.
\]

There are
\[
(m+1)(n+1)
\]
lattice points in the full rectangle
\[
0\le i\le m,
\qquad
0\le j\le n.
\]
The points below the strip satisfy
\[
j-i<k-m.
\]
They form a triangular corner with
\[
1+2+\cdots+k
=
\frac{k(k+1)}2
\]
points. The points above the strip form an equal triangular corner, again with
\[
\frac{k(k+1)}2
\]
points. Therefore
\[
\#(R^{\ge k}_{m,n})^{\mathbb C^*}
=
(m+1)(n+1)-k(k+1).
\]

For any complex algebraic variety \(Y\) with an algebraic \(\mathbb C^*\)-action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
One proof removes the fixed locus and applies Rosenlicht stratification to the complement. After refinement by stabilizer type, each nonfixed stratum is a locally trivial bundle with fiber a finite quotient of \(\mathbb C^*\), hence with fiber Euler characteristic zero. Additivity then leaves only the fixed locus.

Since \(R^{\ge k}_{m,n}\) is projective,
\[
\chi_{\mathrm{top}}(R^{\ge k}_{m,n})
=
\#(R^{\ge k}_{m,n})^{\mathbb C^*}
=
(m+1)(n+1)-k(k+1).
\]

Finally, additivity gives
\[
\chi_c(G_0)
=
(m+1)(n+1)
-
\bigl((m+1)(n+1)-2\bigr)
=
2.
\]
For
\[
1\le k<m,
\]
\[
\chi_c(G_k)
=
\left((m+1)(n+1)-k(k+1)\right)
-
\left((m+1)(n+1)-(k+1)(k+2)\right)
=
2(k+1).
\]
At the top,
\[
\chi_c(G_m)
=
(m+1)(n+1)-m(m+1)
=
(m+1)(n-m+1).
\]
This proves all stated formulas.

## Verification
The bundled checker enumerates every monomial pair for
\[
1\le m\le20,
\qquad
m\le n\le30,
\]
computes its gcd degree directly from exponents, and verifies the cumulative fixed-point formula for every threshold
\[
1\le k\le m.
\]

It also forms the exact gcd-degree histogram and verifies the three stratum formulas, including the degree-independent coprime value \(2\).

These finite computations are regression evidence only. The theorem for all parameters is proved by the strip-count argument and Euler localization.

## Relationship to prior work
The resultant and subresultant framework is classical. D'Andrea and Dickenstein recall that the homogeneous resultant vanishes when the input forms have a common projective root, discuss the Sylvester matrix for binary forms, and place homogeneous subresultants in the same elimination-theoretic framework.

The first cumulative locus
\[
R^{\ge1}_{m,n}
\]
is the projective resultant hypersurface for a pair of binary forms. Higher \(R^{\ge k}_{m,n}\) are the corresponding deeper common-factor, or subresultant, degeneracy loci.

The result here concerns the topology of this entire filtration rather than determinantal formulas for its equations: every cumulative Euler characteristic has the closed quadratic formula above, and the exact gcd-degree strata have the linear staircase
\[
2,\ 4,\ 6,\ldots,2m
\]
until the terminal divisibility stratum.

Targeted searches for Euler characteristics of resultant hypersurfaces, subresultant loci, common-factor varieties, and exact gcd-degree strata did not locate these formulas.

## Limitations
The result concerns pairs of binary forms. Multivariate common-factor loci have more complicated torus-fixed combinatorics and are not covered.

The exact-stratum values use compactly supported Euler characteristic. They do not determine the Betti numbers or homotopy types of the strata.

The proof uses a coarse localization invariant. The same loci have substantially richer singular and intersection-theoretic geometry not detected here.

Because the proof is short once the Sylvester/common-factor filtration is combined with torus localization, an older unindexed observation remains a residual novelty risk.

## References
Carlos D'Andrea and Alicia Dickenstein, *Explicit formulas for the multivariate resultant*, arXiv:math/0007036, first submitted 6 July 2000; *Journal of Pure and Applied Algebra* 164 (2001), 59--86, DOI 10.1016/S0022-4049(00)00145-6.
