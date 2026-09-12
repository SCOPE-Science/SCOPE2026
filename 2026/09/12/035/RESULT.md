# Non-realizability of an explicit six-atom cone-volume measure with centroid at the origin

## Context

The discrete logarithmic Minkowski problem asks which discrete measures on the
sphere $S^{n-1}$ arise as cone-volume measures $V_P$ of convex polytopes
$P \subset \mathbb{R}^n$ with the origin in their interior. For a polytope with
facets $F_i$, outer unit normals $u_i$, support values $h_i>0$ and facet
volumes $|F_i|$, the cone-volume measure is $V_P = \sum_i c_i \delta_{u_i}$
with $c_i = \frac{1}{n}h_i|F_i| > 0$. A theorem of Henk–Linke proves that every
polytope with centroid at the origin satisfies the subspace concentration
condition, but that condition is not sufficient in general. The question
audited here is whether one explicit six-atom measure satisfying all standard
necessary conditions is realizable under the strictly stronger
centroid-at-origin normalization.

## Definitions

Let $e_1,e_2,e_3,e_4$ be the standard basis of $\mathbb{R}^4$,
$v_1 = (-1,-1,0,0)/\sqrt{2}$, $v_2 = (0,0,-1,-1)/\sqrt{2}$,
$\beta = 1/(2+2\sqrt{2}) = (\sqrt{2}-1)/2$,
$\alpha = \beta/\sqrt{2} = (2-\sqrt{2})/4$, and

$$\mu = \alpha(\delta_{e_1}+\delta_{e_2}+\delta_{e_3}+\delta_{e_4})
  + \beta(\delta_{v_1}+\delta_{v_2}).$$

Then $4\alpha+2\beta = 1$, so $\mu$ is a probability measure on $S^3$, and
$\alpha - \beta/\sqrt{2} = 0$ gives vanishing barycenter
$\sum \mu_i u_i = 0$. Moreover $2\alpha+\beta = 1/2 = 2/4$, i.e. $\mu$
satisfies the subspace concentration inequality with complementary equality
on the coordinate 2-planes $\mathrm{span}\{e_1,e_2\}$ and
$\mathrm{span}\{e_3,e_4\}$.

## Result

**Theorem.** With $\alpha,\beta,v_1,v_2,\mu$ as above, there is no convex
polytope $P \subset \mathbb{R}^4$ with centroid at the origin whose normalized
cone-volume measure $V_P/|P|$ equals $\mu$. In fact, every origin-interior
polytope with $V_P/|P| = \mu$ is exactly a product $T(p)\times T(q)$,
$p,q>0$, of two right-isosceles triangles, whose centroid
$(p(1-\sqrt{2})/3,p(1-\sqrt{2})/3,q(1-\sqrt{2})/3,q(1-\sqrt{2})/3)$ is never
zero. The witness $P(1,1) = T(1)\times T(1)$, with $T(1)$ having vertices
$(1,1),(1,-1-\sqrt{2}),(-1-\sqrt{2},1)$, has $6$ facets, $9$ vertices,
$V_P/|P| = \mu$, and centroid
$((1-\sqrt{2})/3,\ldots) \approx (-0.138,\ldots)$, showing the centroid
hypothesis is the exact and only obstruction.

## Proof / evidence

Suppose $P$ has $0$ in its interior and $V_P/|P| = \mu$. Since every atom of
$\mu$ carries positive mass, $P$ has exactly the six facets with the stated
normals and support values $h_1,\dots,h_4,k_1,k_2 > 0$:
$P = \{x_1\le h_1,x_2\le h_2,x_3\le h_3,x_4\le h_4,
x_1+x_2\ge -k_1\sqrt{2},x_3+x_4\ge -k_2\sqrt{2}\}$.
Constraints decouple, so $P = T'\times T''$ with
$T' = \{y_1\le h_1,y_2\le h_2,y_1+y_2\ge -k_1\sqrt{2}\}$ and $T''$ analogous;
each is a non-degenerate right-isosceles triangle of leg
$L' = h_1+h_2+k_1\sqrt{2}$. For such a triangle with origin interior, edge
lengths $L',L',\sqrt{2}L'$, distances $h_1,h_2,k_1$, and area $L'^2/2$, the
normalized 2D cone-volume weights are $h_1/L',h_2/L',k_1\sqrt{2}/L'$.
A 4D facet $E'\times T''$ has cone-volume $c = |T''|\cdot c'/2$ where
$c'$ is the 2D cone-volume of $E'$, and since $|P| = |T'||T''|$,
$c/|P| = \frac12 c'/|T'|$. Hence 4D weights $(\alpha,\alpha,\beta)$ force 2D
weights $(2\alpha,2\alpha,2\beta)$ on each triangle. From
$\alpha = \beta/\sqrt{2}$ this forces $h_1 = h_2 = k_1 =: p$ (and likewise
$q$ for $T''$), verified exactly by $p/L = 2\alpha$ and
$p\sqrt{2}/L = 2\beta$ for $L = p(2+\sqrt{2})$. The triangle centroid, the mean
of its vertices, is $p(1-\sqrt{2})/3 \ne 0$ per coordinate, so the product
centroid is never the origin. The converse computation shows every
$P(p,q)$ realizes $\mu$. All identities hold exactly over
$\mathbb{Q}(\sqrt{2})$ and are machine-checked in
`artifacts/verify.py` (all assertions pass).

## Limitations

The disproof uses the standard fact that a full-dimensional polytope with
centroid at the origin contains the origin in its interior. It does not
address non-polytopal convex bodies, smooth bodies, other center
normalizations (e.g. Santaló point), or the general discrete logarithmic
Minkowski problem beyond this six-atom measure.

## Reproducibility

Run `python3 artifacts/verify.py` (requires sympy); exit 0 with
`ALL CHECKS PASSED` confirms closed forms $\beta=(\sqrt2-1)/2$,
$\alpha=(2-\sqrt2)/4$, probability and barycenter identities, subspace mass
$2\alpha+\beta=1/2$, general-triangle area/weight/centroid formulas, the
isosceles forcing identities, the product cone-volume identities, and a float
cross-check of the $P(1,1)$ realization.

## References

- K. Böröczky, E. Lutwak, D. Yang, G. Zhang, The logarithmic Minkowski
  problem, J. Amer. Math. Soc. 26 (2013), 831–852.
- M. Henk, E. Linke, Cone-volume measures of polytopes, Adv. Math. 2014
  (arXiv:1305.5335): centroid-at-origin implies subspace concentration.
- K. Böröczky, P. Hegedűs, G. Zhu, On the discrete logarithmic Minkowski
  problem; G. Zhu, The logarithmic Minkowski problem for polytopes,
  Adv. Math. 2014.
