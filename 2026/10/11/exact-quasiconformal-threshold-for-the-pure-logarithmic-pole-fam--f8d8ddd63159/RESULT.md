# Exact quasiconformal threshold for the pure logarithmic pole family

## Finding

Fix
\[
0\le p<1,
\qquad
A\in\mathbb C,
\]
and consider the pure logarithmic pole map
\[
f_{A,p}(z)
=
\frac{1}{z-p}
+
A\log\left|\frac{1-pz}{z-p}\right|.
\]

Let
\[
s=(1-p^2)|A|.
\]
For every
\[
0\le k<1,
\]
the map belongs to
\[
\Sigma_H^k(p)
\]
if and only if
\[
s\le\frac{2k}{1+k}.
\]
Equivalently,
\[
|A|
\le
\frac{2k}{(1+k)(1-p^2)}.
\]

More precisely, for
\[
s<1,
\]
the optimal quasiconformal-extension coefficient is
\[
k_{\min}(A,p)
=
\frac{s}{2-s}.
\]
It is attained by the explicit extension
\[
\widehat f_{A,p}(z)
=
\begin{cases}
\displaystyle
\frac{1}{z-p}
+
A\log\left|\frac{1-pz}{z-p}\right|,
& |z|<1,\\[1.2ex]
\displaystyle
\frac{1}{z-p},
& |z|\ge1.
\end{cases}
\]

Thus the logarithmic coefficient can be classified exactly in this natural one-parameter subfamily.

## Assumptions and scope

The class
\[
\Sigma_H^k(p)
\]
is the class used in arXiv:2606.03306v2: sense-preserving univalent harmonic mappings on the unit disk with a simple pole at
\[
p\in[0,1)
\]
that admit a
\[
k
\]
-quasiconformal extension to the Riemann sphere.

The finding concerns the subfamily obtained by setting the analytic and coanalytic regular parts equal to zero. It does not determine the true supremum of
\[
|A|
\]
over the full class with arbitrary regular parts.

The parameter
\[
k
\]
is the Beltrami coefficient bound used by the source, not the maximal-dilatation parameter
\[
K=(1+k)/(1-k).
\]

## Proof

Set
\[
w=\frac{z-p}{1-pz},
\qquad
c=(1-p^2)A.
\]
The inverse automorphism is
\[
z=\frac{p+w}{1+pw}.
\]
A direct computation gives
\[
z-p
=
\frac{(1-p^2)w}{1+pw},
\qquad
1-pz
=
\frac{1-p^2}{1+pw}.
\]
Therefore
\[
\log\left|\frac{1-pz}{z-p}\right|
=
-\log|w|
\]
and
\[
\frac{1}{z-p}
=
\frac{p+1/w}{1-p^2}.
\]
After the conformal affine postcomposition
\[
G_c(w)
=
(1-p^2)f_{A,p}(z)-p,
\]
the family becomes
\[
G_c(w)
=
\frac1w-c\log|w|.
\]

The Wirtinger derivatives are
\[
(G_c)_w
=
-\frac1{w^2}
-
\frac{c}{2w},
\qquad
(G_c)_{\bar w}
=
-\frac{c}{2\bar w}.
\]
Hence
\[
\begin{aligned}
J_{G_c}(w)
&=
|(G_c)_w|^2-|(G_c)_{\bar w}|^2\\
&=
|w|^{-4}
\left(
\left|1+\frac c2w\right|^2
-
\frac{|c|^2|w|^2}{4}
\right)\\
&=
|w|^{-4}
\left(
1+\operatorname{Re}(cw)
\right).
\end{aligned}
\]
Thus
\[
J_{G_c}(w)>0
\]
throughout
\[
0<|w|<1
\]
whenever
\[
|c|<1.
\]

There is also an elementary global univalence proof. On the circle
\[
|w|=r,
\]
\[
G_c(re^{i\theta})
=
r^{-1}e^{-i\theta}
-
c\log r.
\]
Thus its image is the circle with center
\[
-c\log r
\]
and radius
\[
1/r.
\]
If
\[
0<r_1<r_2\le1,
\]
the distance between the two centers is
\[
|c|\log(r_2/r_1).
\]
Because
\[
|c|<1
\]
and
\[
\log t<t-1
\qquad(t>1),
\]
\[
|c|\log(r_2/r_1)
<
r_2/r_1-1
\le
\frac1{r_1}-\frac1{r_2}.
\]
The image circles are therefore strictly nested. At
\[
r=1
\]
the image is the unit circle, while as
\[
r\downarrow0
\]
the radii tend to infinity faster than the centers move. Consequently
\[
G_c
\]
is a sense-preserving homeomorphism from the punctured disk onto
\[
\{|\zeta|>1\}.
\]

Its complex dilatation has modulus
\[
|\mu_{G_c}(w)|
=
\frac{|c|\,|w|}
{2\left|1+\frac c2w\right|}.
\]
For fixed
\[
|w|=r,
\]
the denominator is minimized when
\[
cw
\]
is negative real. Hence
\[
\max_{|w|=r}
|\mu_{G_c}(w)|
=
\frac{|c|r}{2-|c|r}.
\]
The right side is increasing in
\[
r,
\]
so
\[
\|\mu_{G_c}\|_\infty
=
\frac{|c|}{2-|c|}.
\]

Any quasiconformal extension must agree with
\[
G_c
\]
inside the disk, so no extension can have a smaller Beltrami bound.

Conversely, define
\[
\widehat G_c(w)
=
\begin{cases}
G_c(w),&|w|<1,\\
1/w,&|w|\ge1.
\end{cases}
\]
The two formulas agree on
\[
|w|=1.
\]
The inside maps onto the exterior of the unit circle and the outside reciprocal maps onto the closed unit disk. Thus
\[
\widehat G_c
\]
is a sphere homeomorphism. It is conformal outside the unit disk and has Beltrami norm
\[
|c|/(2-|c|)
\]
inside. Therefore this value is the optimal extension coefficient.

Undoing the conformal changes of variables gives
\[
\widehat f_{A,p}(z)
=
\frac1{z-p}
\]
outside the unit disk.

Finally,
\[
\frac{s}{2-s}\le k
\]
is equivalent to
\[
s\le\frac{2k}{1+k},
\]
which proves the classification.

## Verification

The primary 2026 paper was inspected in full at its definition of
\[
\Sigma_H^k(p),
\]
Theorems 1.1 and 1.2, and the proof of the logarithmic-coefficient estimate.

The source proves the strict general bound
\[
|A|<\frac{2k}{1-p^2}
\]
by a Schwarz-lemma argument on the complex dilatation. It also gives a sufficient derivative-smallness criterion, but no necessity statement for that criterion.

For the pure logarithmic family, the source criterion with
\[
h=g=0
\]
reduces to
\[
|A|
\le
\frac{k(1-p)}{(1+p)(1+p^2)}.
\]
The exact threshold proved here is larger and is obtained by computing the full Beltrami norm and a global homeomorphic extension.

The proof above uses exact identities only. No finite numerical experiment, sampling argument, or unproved completeness assumption enters the classification.

## Relationship to prior work

Chen and Wang's recent paper is the first inspected source in this line to retain the logarithmic singularity while studying quasiconformal extension of the pole class. Its predecessor results by Bhowmik and Satpati treat the corresponding pole problem without the logarithmic term and therefore do not contain this subfamily.

Hengartner and Schober's classical theory supplies the general exterior-disk representation with a logarithmic term. The full 1987 article was not available in the full-text sources inspected for this run, so no whole-document noncoverage claim is made about it. Exact-formula searches for the pure family and its quasiconformal threshold did not surface an earlier classification.

The new statement is not a special case of the source's sufficient theorem: that theorem yields only the smaller bound displayed above. Nor is it implied by the source's general necessary estimate, which is strictly less precise for this subfamily.

The classification therefore gives an exact benchmark between the recent paper's broad necessary estimate and its conservative sufficient condition.

## Limitations

The result concerns the pure logarithmic subfamily
\[
h=g=0.
\]
Regular analytic or coanalytic terms can alter the internal dilatation and may allow larger logarithmic coefficients in the full class.

The theorem determines the optimal Beltrami bound for this family, but it does not determine the global supremum of
\[
|A|
\]
over all of
\[
\Sigma_H^k(p).
\]

The classical 1987 full text was not available in the full-text sources inspected, so a differently formulated old observation about this exact one-parameter family remains a residual originality risk.

## References

1. Z. Chen and L.-M. Wang, *Area Theorems and Quasiconformal Extensions of Harmonic Mappings with a Pole*, arXiv:2606.03306v1--v2, 2026.
2. B. Bhowmik and G. Satpati, *An area theorem for harmonic mappings with nonzero pole having quasiconformal extensions*, Proceedings of the American Mathematical Society 152 (2024), 3881--3891, DOI: 10.1090/PROC/16850.
3. B. Bhowmik and G. Satpati, *On quasiconformal extension of harmonic mappings with nonzero pole*, Comptes Rendus Mathématique 363 (2025), 445--454, DOI: 10.5802/crmath.686.
4. W. Hengartner and G. Schober, *Univalent harmonic functions*, Transactions of the American Mathematical Society 299 (1987), 1--31, DOI: 10.1090/S0002-9947-1987-0869396-9.
