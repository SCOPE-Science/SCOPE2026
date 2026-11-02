# Water-filling classification of extremal ellipsoids for ball–box intersections

## Finding

**Theorem.** Fix an integer \(d\ge 3\) and \(a=(a_1,\ldots,a_d)\in(0,1]^d\), and define the full-dimensional centrally symmetric convex body
\[
K(a)=\{x\in\mathbb R^d:\|x\|_2\le1,\ |x_i|\le a_i\text{ for every }i\}.
\]
Put \(S=\sum_{i=1}^d a_i^2\). If \(S\le1\), set \(m_i=a_i\). If \(S>1\), let \(t\in(0,1)\) be the unique solution of
\[
\sum_{i=1}^d\min\{a_i^2,t\}=1,
\qquad m_i=\min\{a_i,\sqrt t\}.
\]
The unique John ellipsoid \(J(a)\) and Löwner ellipsoid \(L(a)\) are, respectively,
\[
\boxed{J(a)=\left\{x:\sum_i\frac{x_i^2}{a_i^2}\le1\right\},\qquad
L(a)=\left\{x:\sum_i\frac{x_i^2}{d m_i^2}\le1\right\}.}
\]
In particular, letting \(H(a)=\prod_i[-m_i,m_i]\), one has the **exact contact-skeleton identity**
\[
\boxed{L(K(a))=L(H(a)),\quad H(a)\subseteq K(a)\subseteq L(H(a)).}
\]
Every one of the \(2^d\) signed corners \((\pm m_1,\ldots,\pm m_d)\) is a Löwner contact point. If \(S\ge1\), all those contact points also lie on the unit sphere. In the \(S>1\) regime the active coordinate caps are exactly those with \(a_i^2<t\); the other cap parameters can be varied within their inactive regime without affecting the ellipsoid.

The exact volume ratio is
\[
\boxed{\frac{\operatorname{vol}_d L(a)}{\operatorname{vol}_d J(a)}
=d^{d/2}\prod_{i=1}^d\frac{m_i}{a_i}.}
\]
It lies between \(1\) and \(d^{d/2}\); the lower equality holds only for the uncut ball \(a_i=1\) for all \(i\), and the upper equality holds exactly when \(S\le1\) (then the intersection is the entire box). The original ball remains the Löwner ellipsoid **if and only if** every cap half-width obeys \(a_i\ge1/\sqrt d\). These assertions include parameter-boundary coincidences \(a_i^2=t\), with either tie convention.

## Assumptions and scope

All distances and volumes are Euclidean. The ball has radius one, its center and every coordinate-slab midpoint are the origin, and the slabs are orthogonal. Every \(a_i\) is strictly positive and no larger than one; the body is therefore full-dimensional. The genuinely multi-cut case has at least two indices with \(a_i<1\). A one-cut special case was addressed by earlier slab-ellipsoid literature and is included only to state a closed family formula. The result does not extend by assertion to nonorthogonal or off-center slabs.

## Proof

1. **Water level and its uniqueness.** The continuous nondecreasing function \(f(t)=\sum_i\min(a_i^2,t)\) starts at zero and equals \(S>1\) when \(t\ge\max_i a_i^2\). Until that last threshold it is strictly increasing. Thus \(f(t)=1\) has exactly one solution \(t\in(0,\max_i a_i^2)\). Sorting the squared caps determines which terms are fixed and gives \(t=(1-\sum_{i\in I}a_i^2)/(d-|I|)\), with \(I=\{i:a_i^2<t\}\). If \(S\le1\), every point of the box \(\prod_i[-a_i,a_i]\) has squared norm at most \(S\), so \(K(a)\) is that box.

2. **Inscribed ellipsoid.** Reflection in each coordinate hyperplane leaves \(K(a)\) invariant. By uniqueness, its maximum-volume inscribed ellipsoid is centered and diagonal. Its semiaxis along coordinate \(i\) is at most \(a_i\), since the entire ellipsoid lies inside \(|x_i|\le a_i\). Conversely, the ellipsoid with semiaxes \(a_i\) lies inside every slab and inside the unit ball: for \(x_i=a_i y_i\) and \(\sum_i y_i^2\le1\), one has \(\sum_i x_i^2\le(\max_i a_i^2)\sum_i y_i^2\le1\). This proves the John formula, with uniqueness from the standard extremal-ellipsoid theorem.

3. **The optimal contact box.** Define \(H=\prod_i[-m_i,m_i]\). Since \(m_i\le a_i\) and \(\sum_i m_i^2=\min(S,1)\le1\), every point of \(H\) lies in \(K(a)\). This is the unique maximum-volume centered axis-parallel box contained in \(K(a)\): writing its half-width squares as \(z_i>0\), maximize \(\tfrac12\sum_i\log z_i\) subject to \(z_i\le a_i^2\) and \(\sum_i z_i\le1\). For \(S\le1\) all caps saturate; for \(S>1\), the strictly concave objective and the Karush–Kuhn–Tucker equations imply \(z_i=\min(a_i^2,(2\lambda)^{-1})\) for a single positive multiplier \(\lambda\), with \(\sum_i z_i=1\). Thus \(z_i=m_i^2\) uniquely. The unique Löwner ellipsoid of \(H\) is \(E=\{\sum_i x_i^2/(d m_i^2)\le1\}\). Indeed, transform its signed corners by \(y_i=x_i/(\sqrt d\,m_i)\); the corners become the \(2^d\) vectors \((\pm1,\ldots,\pm1)/\sqrt d\). They lie on the unit sphere and, with weights \(d/2^d\) each, satisfy the centered contact identities \(\sum w_v v=0\) and \(\sum w_v vv^T=I_d\). The necessary-and-sufficient Löwner contact criterion proves global optimality and uniqueness of \(E\) for \(H\).

4. **The other containment.** If \(S\le1\), \(K(a)=H\), so the assertion follows. Suppose \(S>1\) and put \(I=\{i:a_i^2<t\}\). For every \(x\in K(a)\), the positivity of \(1/a_i^2-1/t\) on \(I\) gives
\[
\begin{aligned}
\sum_{i=1}^d\frac{x_i^2}{m_i^2}
&=\frac{\|x\|_2^2}{t}+\sum_{i\in I}x_i^2\left(\frac1{a_i^2}-\frac1t\right)\\
&\le\frac1t+\sum_{i\in I}\left(1-\frac{a_i^2}{t}\right)\\
&=|I|+\frac{1-\sum_{i\in I}a_i^2}{t}=d.
\end{aligned}
\]
The last equality is the water-level identity \(\sum_i\min(a_i^2,t)=1\). Thus \(K(a)\subseteq E\). Together with \(H\subseteq K(a)\), this shows that \(E\) is the unique Löwner ellipsoid of \(K(a)\): any ellipsoid enclosing \(K(a)\) must enclose \(H\) and hence cannot have smaller volume than \(E\).

5. **Consequences and endpoint cases.** The ratio follows by multiplying the semiaxes. Since \(m_i\le a_i\), it is at most \(d^{d/2}\), with equality iff \(S\le1\): if \(S>1\), at least one inequality \(m_i<a_i\) is strict. The ratio is at least one by \(J(a)\subseteq K(a)\subseteq L(a)\). Equality forces the two ellipsoids to coincide and the body itself to equal their common ellipsoid. An intersection of the ball with a proper coordinate cap is not an ellipsoid (a nonempty flat facet appears), so equality occurs only when every \(a_i=1\). Finally \(L(a)=B_2^d\) precisely when \(m_i=1/\sqrt d\) for all \(i\), which is equivalent to all \(a_i\ge1/\sqrt d\). Parameter ties leave the defining formulas unchanged.

## Verification

A standalone Python checker evaluates the water-level equation, confirms three sets of exact rational squared-contact radii, enumerates every signed corner to check containment and Löwner contact, and tests random admissible points. On the present package's \(`ball_box_waterfill_verify.py`\), 216 configurations across dimensions two through eight passed, including 216,000 random admissible points. Numerical tests corroborate but are not used to prove the infinite parameter family; the global proof is the contact-certificate-and-sandwich argument above. Reproduce with \(`python3 ball_box_waterfill_verify.py`\) using only the standard Python library.

## Relationship to prior work

Todd (1982) derives outer ellipsoids for one-sided and two-sided cuts made with one linear form; Güler and Gürtuna (2007), especially their Theorem 6.1, give the complete slab case and the general centered contact characterization. The formulas above agree with their centered one-slab specialization, including its sharp threshold. They do not state the arbitrary collection of independently capped coordinates or the equality with the extremal ellipsoid of the maximum-volume inscribed coordinate box. The latter equality is the main geometric claim, supported here by a new explicit all-dimensional containment and a complete contact set. Standard optimal-design and general convex-programming formulations imply how to *test* a proposed Löwner ellipsoid but do not themselves provide the stated water-level solution.

## Limitations

The novelty comparison is best-knowledge and not an independent priority determination. Existing literature on ellipsoidal cuts and minimum-volume enclosing ellipsoids is extensive, and an unidentified special-case design theorem might subsume the water-level formula. Orthogonality, central symmetry and a common Euclidean ball are essential hypotheses. No claim is made for translated slabs, nonorthogonal cuts, or a general intersection of ellipsoids. The contact-corner set is sufficient but not asserted to exhaust every contact point.

## References

- M. J. Todd, *On Minimum Volume Ellipsoids Containing Part of a Given Ellipsoid*, Mathematics of Operations Research **7** (1982), 253–261. DOI: 10.1287/moor.7.2.253.
- O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707v1, first publicly submitted 2007-09-05, particularly Sections 2, 5–7.
- S. Boyd and L. Vandenberghe, *Convex Optimization*, Chapter 8 (geometric problems), Cambridge University Press, 2004 (general enclosing/inscribed-ellipsoid optimization).
