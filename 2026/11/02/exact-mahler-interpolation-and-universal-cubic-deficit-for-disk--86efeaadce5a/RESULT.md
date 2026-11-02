# Exact Mahler interpolation and universal cubic deficit for disk-clipped regular polygons

## Finding

Let \(n\ge3\), \(\alpha=\pi/n\), and let \(P_n\subset\mathbb R^2\) be a regular \(n\)-gon centered at the origin with inradius one. For \(1\le r\le\sec\alpha\), set \(K_{n,r}=P_n\cap rB_2\), where \(B_2\) is the closed unit disk, and set \(\beta=\arccos(1/r)\in[0,\alpha]\). The Santaló point of \(K_{n,r}\) is the origin. Its Mahler product has the **exact formula**

\[
\mathcal M_n(r)=|K_{n,r}|\,|K_{n,r}^{\circ}|
=n^2\bigl(\alpha-\beta+\sin\beta\cos\beta\bigr)
       \bigl(\alpha-\beta+\tan\beta\bigr).
\]

The function \(r\mapsto\mathcal M_n(r)\) is strictly decreasing on \([1,\sec\alpha]\), with endpoints \(\mathcal M_n(1)=\pi^2\) and \(\mathcal M_n(\sec\alpha)=n^2\sin^2\alpha\). Its sharp one-sided endpoint laws are

\[
\pi^2-\mathcal M_n(r)
=\frac{2\sqrt2\,\pi n}{3}(r-1)^{3/2}
+O_n\bigl((r-1)^{5/2}\bigr),\qquad r\downarrow1,
\]

\[
\mathcal M_n(r)-n^2\sin^2\alpha
=n^2\sin^2\alpha\cos\alpha\,(\sec\alpha-r)
+O_n\bigl((\sec\alpha-r)^2\bigr),\qquad r\uparrow\sec\alpha.
\]

Finally, writing \(r_n(t)=\sec(t\pi/n)\) for \(0\le t\le1\), the *normalized deficit profile* satisfies the uniform limit

\[
\frac{\pi^2-\mathcal M_n(r_n(t))}
     {\pi^2-n^2\sin^2(\pi/n)}
=t^3+\frac{\pi^2}{n^2}
\left(\frac{2t^3}{15}-\frac{4t^5}{5}+\frac{2t^6}{3}\right)
+O(n^{-4}),
\]

uniformly in \(0\le t\le1\). In particular, the complete disk-to-polygon Mahler deficit converges to a universal cubic profile, not merely a comparison of the two endpoint bodies.

## Assumptions and scope

The polar \(K^\circ=\{y:\langle x,y\rangle\le1\ \text{for every }x\in K\}\) is taken about the origin; \(|\cdot|\) denotes planar Lebesgue area. Regular polygons have \(n\ge3\) and inradius one. The body is the **intersection** of a polygon and a concentric disk, not a parallel body \(P_n+rB_2\). All formulas and strict inequalities cover every integer \(n\ge3\) and each indicated real radius. The \(O_n\) constants may depend on a fixed \(n\); the final \(O(n^{-4})\) is uniform in \(t\in[0,1]\). The Santaló-center assertion follows from uniqueness and nontrivial rotational symmetry.

## Proof

**1. Polygon–circle area.** Choose outward facet normal at angle zero. In one fundamental angular half-sector \(0\le\theta\le\alpha\), the radial function is

\[
\rho_{K_{n,r}}(\theta)=\min\{r,\sec\theta\}.
\]

The transition occurs at \(\theta=\beta\), because \(\sec\beta=r\). Polar-coordinate integration over the \(2n\) half-sectors gives

\[
A:=|K_{n,r}|=n\int_0^\alpha\rho_{K_{n,r}}(\theta)^2\,d\theta
=n\left[\tan\beta+(\alpha-\beta)\sec^2\beta\right]. \tag{1}
\]

**2. Polar area.** Polarity interchanges intersections and convex hulls of polars for bodies with the origin in their interiors. Thus

\[
K_{n,r}^\circ=\operatorname{conv}\bigl(P_n^\circ,\,r^{-1}B_2\bigr).
\]

The vertices of \(P_n^\circ\) lie on the unit circle at successive angular separation \(2\alpha\), and \(r^{-1}=\cos\beta\). For each polar vertex, the two tangent segments to the disk \(\cos\beta B_2\) meet that circle at angular offsets \(\pm\beta\). Its sector of the convex hull consists of two triangles of combined area \(\sin\beta\cos\beta\) and circular sectors of combined area \((\alpha-\beta)\cos^2\beta\). Accordingly,

\[
B:=|K_{n,r}^\circ|=n\left[\sin\beta\cos\beta+(\alpha-\beta)\cos^2\beta\right]. \tag{2}
\]

This decomposition is valid also at both endpoints, when one or another piece has zero area.

**3. Exact product.** Equation (1) can be rewritten as \(A=n\sec^2\beta\,[\alpha-\beta+\sin\beta\cos\beta]\). Equation (2) is \(B=n\cos^2\beta\,[\alpha-\beta+\tan\beta]\). Multiplying proves the boxed product, including endpoint values.

**4. Strict decrease.** Differentiate the dimensionless product \(F(\beta)=(\alpha-\beta+\sin\beta\cos\beta)(\alpha-\beta+\tan\beta)\):

\[
F'(\beta)=\sin^2\beta\left[(\alpha-\beta)(\tan^2\beta-1)-\tan\beta\right]. \tag{3}
\]

For \(0<\beta\le\pi/4\), the bracket is strictly negative. For \(\pi/4<\beta<\alpha\le\pi/3\), use \(\alpha-\beta\le\pi/12\), \(\tan^2\beta-1\le2\) and \(\tan\beta>1\), whence the bracket is less than \(\pi/6-1<0\). Since \(r=\sec\beta\) increases strictly for positive \(\beta\), the Mahler product decreases strictly across the entire nondegenerate interval.

**5. Endpoint rates.** At \(\beta=0\), Taylor expansion gives \(F(\beta)=\alpha^2-\alpha\beta^3/3+O_\alpha(\beta^5)\) and \(r-1=\beta^2/2+O(\beta^4)\). Since \(n^2\alpha=n\pi\), the first endpoint expansion follows. At \(\beta=\alpha\), equation (3) gives \(F'(\alpha)=-\sin^2\alpha\tan\alpha\). The chain rule with \(dr/d\beta=\sec\beta\tan\beta\) gives \((d\mathcal M_n/dr)(\sec\alpha)=-n^2\sin^2\alpha\cos\alpha\). Analyticity in a neighborhood of positive \(\beta=\alpha\) proves the second expansion.

**6. Uniform polygon-to-disk scaling.** Substitute \(\beta=t\alpha\), \(0\le t\le1\). Standard Taylor expansions with remainders uniform for \(|t\alpha|\le\alpha\le\pi/3\) give, as \(\alpha\downarrow0\),

\[
\mathcal M_n(r_n(t))
=\pi^2\left[1-\frac{t^3}{3}\alpha^2+
\left(\frac{4t^5}{15}-\frac{2t^6}{9}\right)\alpha^4
+O(\alpha^6)\right].
\]

At \(t=1\) this recovers \(n^2\sin^2\alpha=\pi^2[1-\alpha^2/3+2\alpha^4/45+O(\alpha^6)]\). Divide the two deficits; the denominator is positive for all finite \(n\ge3\), and has asymptotic \(\pi^2\alpha^2/3\), giving the stated uniform expression.

## Verification

A standalone Python 3 script (`check.py`) independently integrates the primal radial area by midpoint quadrature and computes the polar area from the convex hull of sampled circular points and the exact polar polygon vertices. It also checks endpoint values, strict order, two asymptotic coefficients, and the normalized high-sided profile. In the recorded execution, all 417 assertions passed. These are finite numerical cross-checks; equations (1)–(3), the endpoint expansions, and uniform Taylor estimates constitute the proof.

## Relationship to prior work

The planar rotational-symmetry Mahler inequality \(\mathcal M(K)\ge n^2\sin^2(\pi/n)\) and its equality case are due to Böröczky, Makai, Meyer and Reisner (2013; openly available as arXiv:1507.01481). Their Theorem 3 and Corollary 4 supply the polygonal lower endpoint bound, not a radius-by-radius formula, monotonicity, or scaling profile for disk intersections. The Blaschke–Santaló inequality supplies the upper endpoint bound \(\pi^2\). Meyer and Reisner (2011) treat extremal volume products of polygons of bounded vertex count; their polygon-only extremizers do not determine the clipped smooth/polygonal interpolation. Harrell, Henrot and Lamboley (2011 preprint, 2015 journal) establish local concavity and minimizer constraints for Mahler products, not the present exact disk-clipping path. Existing computations for outer parallel-body roundings \(P_n+tB_2\) concern a different family and cannot be dualized or reparameterized into \(P_n\cap rB_2\) using the elementary polar identities.

## Limitations

The theorem concerns a concentric Euclidean disk intersected with a regular planar polygon, not arbitrary polygons, off-center disks, higher-dimensional polytopes, or Minkowski sums. The parameterwise novelty assessment is based on the identified primary literature and targeted record searches; it is not an independent exhaustive historical-priority certificate. The proof does not establish monotonicity for general nested convex bodies.

## References

1. M. Meyer and S. Reisner, *On the volume product of polygons*, Abh. Math. Semin. Univ. Hambg. 81 (2011), 93–100, https://doi.org/10.1007/s12188-011-0054-3 (online 2011-04-05). Text consulted via https://www.researchgate.net/publication/225173584_On_the_volume_product_of_polygons.
2. K. J. Böröczky, E. Makai Jr., M. Meyer and S. Reisner, *On the volume product of planar polar convex bodies—lower estimates with stability*, Stud. Sci. Math. Hungar. 50 (2013), 159–198, https://arxiv.org/abs/1507.01481 (open preprint first uploaded 2015-07-06; 2013 journal article).
3. E. M. Harrell, A. Henrot and J. Lamboley, *On the local minimizers of the Mahler volume*, J. Convex Anal. 22 (2015), 809–825, https://arxiv.org/abs/1104.3663 (initial public preprint 2011-04-19).
