# Sharp surface-chord fourth moments of orthotopes in every dimension at least four

## Finding

Let \(d\ge4\) be an integer. For a nondegenerate orthotope with independent surface-area-uniform endpoints, let \(D\) be their ambient Euclidean distance. Its normalized even-moment ratio satisfies the exact and sharp bound
\[
\boxed{1+\frac1d+\frac{2(d-1)}{5(d+2)^2}\le\frac{\mathbb E[D^4]}{(\mathbb E[D^2])^2}<\frac{12}{5}.}
\]
Equality on the left characterizes cubes up to scaling; the right supremum is approached by a slender orthotope and is never attained. Every intermediate value occurs. For \(p_i=a_i^2/\sum_j a_j^2\), the stronger global stability inequality holds:
\[
\boxed{\frac{\mathbb E[D^4]}{(\mathbb E[D^2])^2}-\kappa_d\ge\frac{2d^2}{5(d+2)^2}\sum_i(p_i-1/d)^2,\quad\kappa_d=1+\frac1d+\frac{2(d-1)}{5(d+2)^2}.}
\]
The square-root inverse-isotropy exponent is optimal. The minimum strictly decreases with dimension, so two even moments do not determine the unknown dimension within this family.

## Assumptions and scope

Let \(K=\prod_{i=1}^d[-a_i,a_i]\subset\mathbb R^d\) for \(d\ge4\) and all \(a_i>0\). Select independent \(X,Y\) according to normalized \((d-1)\)-dimensional Hausdorff measure on the **entire boundary** \(\partial K\), including all \(2d\) facets (the lower-dimensional edges have probability zero). Define \(D=\|X-Y\|_2\). The measure is not the distribution induced by a random secant line, and it is not uniform volume sampling.

Write
\[
T=\sum_i a_i^{-1},\quad B=\sum_i a_i^2,\quad E=\sum_i a_i^4,\quad R=\frac{\sum_i a_i}{T},\quad C=\frac{\sum_i a_i^3}{T},\quad Q=B+2R.
\]
The letter \(R\) here is a weighted squared-length statistic, not a sphere radius.

## Proof

**1. Exact surface mixture.** The pair of facets orthogonal to coordinate \(i\) has combined area proportional to \(1/a_i\), so the index \(I\) of the facet containing \(X\) obeys \(\Pr(I=i)=1/(a_iT)\). Conditional on \(I=i\), the coordinate \(X_i\) equals either \(a_i\) or \(-a_i\) with equal probability, and all other coordinates are independent uniforms on their respective intervals. Consequently
\[
\mathbb E[X_i]=0,\qquad
\mathbb E[X_i^2]=\frac{a_i^2+2a_i/T}{3},\qquad
\mathbb E[X_i^4]=\frac{a_i^4+4a_i^3/T}{5}.
\]
For \(i\ne j\), the same mixture gives
\[
\mathbb E[X_i^2X_j^2]=\frac{a_i^2a_j^2}{9}\left(1+\frac2{a_iT}+\frac2{a_jT}\right).
\]
Summing the coordinate moments yields
\[
\mathbb E\|X\|^2=\frac Q3,\qquad
\operatorname{Var}(\|X\|^2)=\frac4{45}(E+4C-5R^2).
\]
Since \(X,Y\) are independent and centered,
\[
\mathbb E[D^2]=\frac{2Q}{3},\qquad
\mathbb E[D^4]=2\operatorname{Var}(\|X\|^2)+4\bigl(\mathbb E\|X\|^2\bigr)^2+4\operatorname{tr}\bigl((\mathbb E[XX^{\mathsf T}])^2\bigr).
\]
The covariance matrix is diagonal by the coordinate sign symmetries, giving the **exact** rational identity
\[
\boxed{\kappa=1+\frac25\frac{E+4C-5R^2}{Q^2}+\frac{\sum_i(a_i^2+2a_i/T)^2}{Q^2}
=1+\frac{\frac75E+\frac{28}{5}C-2R^2+4B/T^2}{(B+2R)^2}.}
\]

**2. Sharp lower bound.** Cauchy--Schwarz gives \(E\ge B^2/d\) and \(C\ge R^2\); the latter applies to the probability weights \(1/(a_iT)\) and squared values \(a_i^2\). Moreover,
\[
BT-d\sum_i a_i=\sum_{i<j}\frac{(a_i+a_j)(a_i-a_j)^2}{a_ia_j}\ge0,
\]
so \(0<R/B\le1/d\), with equality precisely for cubes. Because \(\sum_i(a_i^2+2a_i/T)=Q\), Cauchy--Schwarz gives the final term in the exact identity at least \(1/d\). The first nonconstant term obeys
\[
\frac{E+4C-5R^2}{Q^2}\ge\frac{B^2/d-R^2}{(B+2R)^2}=f(R/B),\qquad f(x)=\frac{1/d-x^2}{(1+2x)^2}.
\]
Now \(f'(x)=-(2x+4/d)/(1+2x)^3<0\), and \(f(1/d)=(d-1)/(d+2)^2\), establishing \(\kappa\ge\kappa_d\). All positive orthotopes are covered, and equality requires all their half-edge lengths equal.

For the quantitative remainder, retain the nonnegative term \(E-B^2/d\) in this argument. As \(Q\le B(d+2)/d\),
\[
\kappa-\kappa_d\ge \frac25\frac{E-B^2/d}{Q^2}
\ge \frac{2d^2}{5(d+2)^2}\left(\frac EB^2-\frac1d\right)
=\frac{2d^2}{5(d+2)^2}\sum_i\left(\frac{a_i^2}{B}-\frac1d\right)^2.
\]
This implies a square-root bound for the squared-side proportion vector. The exponent cannot be improved: at fixed \(d\), the shape perturbation \((a_1,a_2,a_3,\ldots,a_d)=(1+\varepsilon,1-\varepsilon,1,\ldots,1)\) has anisotropy norm of exact first order in \(|\varepsilon|\), while smoothness and symmetry at the cube make \(\kappa-\kappa_d=O(\varepsilon^2)\). The positive remainder above also makes it of quadratic order.

**3. Sharp strict upper bound.** Algebraically, from the exact identity,
\[
\frac{12}{5}-\kappa=\frac{\frac75(B^2-E)+\frac{28}{5}(BR-C)+\frac{38}{5}R^2-4B/T^2}{(B+2R)^2}.
\]
Here \(B^2>E\) for all positive half-edges in dimension at least two; \(BR>C\) because
\(BT R-T C=B\sum_i a_i-\sum_i a_i^3=\sum_i a_i\sum_{j\ne i}a_j^2>0\).
Also \(R^2=(\sum_i a_i)^2/T^2\ge B/T^2\). Thus every term group in the numerator is strictly/nonnegatively signed, proving \(\kappa<12/5\). In the family \(a_1=L\), \(a_2=\cdots=a_d=1\), the exact rational identity gives \(\kappa\to12/5\) as \(L\to\infty\). The shape domain is connected, and its image under continuous \(\kappa\) contains the cube minimum and values arbitrarily near the upper endpoint. Hence **every** value in the stated half-open interval is attained.

**4. Dimensional feasibility and its boundary.** The sharp cube value is
\(\kappa_d=1+1/d+2(d-1)/(5(d+2)^2)\). A direct rational subtraction yields
\[
\kappa_d-\kappa_{d+1}
=\frac{7d^4+50d^3+165d^2+282d+180}{5d(d+1)(d+2)^2(d+3)^2}>0.
\]
Its expansion is \(1+7/(5d)+O(d^{-2})\). For any prescribed positive second moment \(m_2\) and any shape with required \(\kappa\), multiplication of all half-edges by
\(\sqrt{m_2/(\mathbb E[D^2])}\) gives the prescribed \(m_2\) without changing \(\kappa\). Thus the feasible integer dimensions \(d\ge4\) are exactly those with \(\kappa_d\le\kappa<12/5\), an upward-closed set, and the union of all feasible scale-free ranges is \((1,12/5)\).

## Verification

The standalone `orthotope_surface_moments_verify.py` uses exact `fractions.Fraction` arithmetic and independently conditions on all ordered facet-normal pairs to calculate both moments. It compares those separately integrated values with the displayed closed form, checks strict bounds, rigidity, stability and dimension monotonicity for rational test shapes in dimensions four through eight. Execute with `python3 orthotope_surface_moments_verify.py`. The observed result was `VERIFY_OK exact_fractional_checks=320 dimensions=4..8`. This is diagnostic finite verification; global conclusions rest on the algebraic proof above.

## Relationship to prior work

Mathai, Moschopoulos and Pederzoli (1999) explicitly evaluate distances in the ordinary three-dimensional cube, including particular pairs of faces, but do not state the sharp all-dimensional aspect-ratio inequality for two boundary-area-uniform points. Their accessible abstract was compared, not their unavailable complete paper. Burgstaller and Pillichshammer (first published online 2009-10-02) bound the **first** ordinary distance moment for **interior-uniform** points in compact convex bodies; their full article was examined and does not imply this boundary fourth-moment theorem. García-Pelayo (2011) gives a general method to express even distance moments in terms of density moments; this forward machinery does not itself imply global shape extrema or sharp all-dimensional bounds, although its full manuscript was unavailable. Earlier results for three-dimensional rectangular boxes concern only \(d=3\) and do not establish either the \(d\ge4\) theorem or the dimension-dependent stability and feasibility statements here.

## Limitations

This result is for positive-axis orthotopes with their **entire surface-area distribution** in integer dimension at least four and exact population moments. It is not an assertion about nonrectangular parallelepipeds, intrinsic boundary distances, random-line chord models, interior-uniform point sampling, or statistical estimation from finitely many observations. The positive constant in the global stability inequality is explicit but is not claimed to be the best possible constant. The exact square-root exponent, not that constant, is optimal. Historical priority requires further review of earlier work, particularly inaccessible full texts in three-dimensional face-distance statistics and general distance-moment theory; an unsuccessful source search cannot certify novelty.

## References

1. B. Burgstaller and F. Pillichshammer, *The Average Distance Between Two Points*, Bulletin of the Australian Mathematical Society 80 (2009), 353–359, DOI: 10.1017/S0004972709000707. Published online 2009-10-02.
2. A. M. Mathai, P. Moschopoulos and G. Pederzoli, *Distance between random points in a cube*, Statistica 59 (1999), 61–81, DOI: 10.6092/issn.1973-2201/1104. Exact first-public calendar day not established.
3. R. García-Pelayo, *Moments of the distribution of distance*, Journal of Mathematical Physics 52 (2011), 033505, DOI: 10.1063/1.3559719.
