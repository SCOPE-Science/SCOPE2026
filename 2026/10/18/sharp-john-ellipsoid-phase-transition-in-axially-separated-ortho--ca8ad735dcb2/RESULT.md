# Sharp John-ellipsoid phase transition in axially separated orthogonal disk hulls

## Finding

Let \(D_t^-\) be the unit closed disk in the \(xy\)-plane centered at \((-t/2,0,0)\), and \(D_t^+\) the unit closed disk in the \(xz\)-plane centered at \((t/2,0,0)\), with \(t\ge0\). Put \(K_t=\operatorname{conv}(D_t^-\cup D_t^+)\). Its unique largest-volume contained ellipsoid is
\[
J_t=\left\{(x,y,z):\frac{x^2}{a_t^2}+\frac{y^2+z^2}{b_t^2}\le1\right\},
\]
where the squared semiaxes are **exactly**
\[
(a_t^2,b_t^2)=
\begin{cases}
(1-t^2/4,\;1/2),&0\le t\le1,\\[2pt]
((t+2)^2/12,\;(t+2)/(6t)),&t\ge1.
\end{cases}
\]
The two formulas coincide at \(t=1\). The John volume is
\[
\operatorname{Vol}_3(J_t)=
\begin{cases}
\frac{2\pi}{3}\sqrt{1-t^2/4},&0\le t\le1,\\[3pt]
\frac{\pi(t+2)^2}{9\sqrt3\,t},&t\ge1.
\end{cases}
\]
It decreases strictly as \(t\) increases from \(0\) to \(2\), then increases strictly for \(t>2\). Its unique global minimum is \(8\pi/(9\sqrt3)\) at \(t=2\), exactly when the two source disks touch at one point. The transverse semiaxis stays at \(1/\sqrt2\) until the sharp change at \(t=1\), after which it decreases strictly. The volume function is continuously differentiable, but not twice differentiable, at \(t=1\).

## Assumptions and scope

All disks are filled closed Euclidean unit disks, with their centers on their shared \(x\)-axis; the containing hull is three-dimensional for each \(t\ge0\). All Euclidean ellipsoids, with **unrestricted** center, orientation and semiaxes, are allowed. The statement concerns the maximal-volume *inscribed* (John) ellipsoid, not the minimal-volume enclosing (Löwner) ellipsoid. Scaling both disks by a common radius \(R>0\) multiplies all semiaxes by \(R\), all volumes by \(R^3\), and replaces \(t\) with the separation divided by \(R\).

## Proof

**1. Symmetry forces the optimizer to have only two semiaxes.** Every full-dimensional compact convex set has a unique maximum-volume inscribed ellipsoid. The hull \(K_t\) is invariant under independent sign changes of \(y\) and \(z\), and under \((x,y,z)\mapsto(-x,z,y)\). The unique optimizer inherits those symmetries. Its center must be the origin, its quadratic form must be diagonal, and the \(y\)- and \(z\)-coefficients must coincide. Thus every possible John ellipsoid has the displayed form, with \(a,b>0\). This does **not** assume centering or alignment of arbitrary competing ellipsoids.

**2. Exact support containment.** The support function of the hull, at \(u=(p,q,r)\), is
\[
h_{K_t}(p,q,r)=\max\left\{-\frac{tp}{2}+\sqrt{p^2+q^2},\;\frac{tp}{2}+\sqrt{p^2+r^2}\right\}.
\]
The ellipsoid support is \(h_E(p,q,r)=\sqrt{a^2p^2+b^2(q^2+r^2)}\). By the symmetries it suffices to take \(p\ge0\). When \(p=0\), minimizing the body support over \(q^2+r^2=1\) gives \(1/\sqrt2\), so the exact necessary and sufficient condition in that plane is \(b^2\le1/2\).

For \(p>0\) put \(s=(q^2+r^2)/p^2\) and \(v=q^2/p^2\in[0,s]\). The reduced support is the maximum of the increasing function \(\sqrt{1+v}-t/2\) and the decreasing function \(\sqrt{1+s-v}+t/2\). If \(s\le t^2+2t\), their minimum possible maximum is \(1+t/2\), attained at \(v=s\). If \(s\ge t^2+2t\), the curves meet, and writing their square roots as \(A,B\) gives \(A-B=t\), \(A^2+B^2=2+s\), hence \(A+B=\sqrt{4+2s-t^2}\). Therefore
\[
\min_{q^2+r^2=sp^2}\frac{h_{K_t}(p,q,r)^2}{p^2}
=\begin{cases}
(1+t/2)^2,&0\le s\le t^2+2t,\\[2pt]
1+s/2-t^2/4,&s\ge t^2+2t.
\end{cases}
\]
Because \(a^2+b^2s\) is increasing in \(s\) and has slope at most \(1/2\) when \(b^2\le1/2\), the infinitely many support inequalities reduce **equivalently** to
\[
\boxed{\quad b^2\le\frac12,\qquad a^2+t(t+2)b^2\le(1+t/2)^2.\quad}
\]
This equivalence includes \(t=0\). It proves both necessity and sufficiency of the proposed feasible semiaxes.

**3. Strict volume maximization.** In three dimensions the ellipsoid volume is \(\frac{4\pi}{3}ab^2\). At a maximum, the second constraint is active. Write \(X=b^2\), \(C=(t+2)^2/4\), and \(D=t(t+2)\). Then \(a^2=C-DX\) and, apart from a positive constant, volume is \(X\sqrt{C-DX}\), with \(0<X\le1/2\) and \(C-DX>0\). For \(t>0\), its derivative has the sign of \(2C-3DX\), so the unique unconstrained optimum is \(X_0=2C/(3D)=(t+2)/(6t)\). This lies at or below \(1/2\) exactly for \(t\ge1\). Hence \(X=1/2\) is uniquely optimal for \(0<t\le1\), and \(X=X_0\) uniquely optimal for \(t\ge1\). Substitution yields the two formulas. For \(t=0\), the independent constraints \(a^2\le1\) and \(b^2\le1/2\) give the stated unique maximum.

**4. Monotonicity and the second threshold.** The first volume branch has negative derivative on \((0,1]\). The second is \(\frac{\pi}{9\sqrt3}(t+4+4/t)\), with derivative \(\frac{\pi}{9\sqrt3}(1-4/t^2)\), which changes sign exactly at \(t=2\). Both first derivatives agree at \(t=1\); the left and right second derivatives there are respectively \(-4\pi/(9\sqrt3)\) and \(8\pi/(9\sqrt3)\). Consequently the optimizer undergoes a genuine active-constraint transition at \(t=1\), and the unique global minimum of its volume occurs at the geometrically distinguished contact separation \(t=2\).

## Verification

The included self-contained file `verify_exact.py` uses exact rational arithmetic to test eight selected parameters and the support-boundary identity, and checks the claimed ellipsoid support inequality at 110,000 independently sampled directions, with eleven contact-direction tests. It completed with `VERIFY_OK exact_cases=8 sampled_directions=110000 contact_cases=11`. The proof of containment and optimization for **all** real parameters and directions is the preceding algebra, not the finite test. No computer-dependent lemma, floating-point certificate of uniqueness, or unproved extrapolation is needed.

## Relationship to prior work

Finch's *Convex Hull of Two Orthogonal Disks* (first made public 19 November 2012, arXiv:1211.4514) treats centered and touching configurations and computes volume, surface area and mean width. Those intrinsic-volume results neither supply nor imply the above maximal inscribed ellipsoid as the disk separation varies. Güler and Gürtuna (arXiv:0709.0707) establish general uniqueness, symmetry reduction, and results for slabs and truncated cones, but do not evaluate this disk-hull family; uniqueness/symmetry is used here as known machinery. Horváth (arXiv:1509.08859) studies volumes of hulls of two bodies, not their inscribed ellipsoids. Nash, Pir, Sottile and Ying (arXiv:1612.09382) classify algebraic boundaries and face lattices of hulls of two circles, not their John ellipsoids. An enclosing ellipsoid of the same hull is a logically different extremal problem and provides no deduction of the present support-containment constraints.

## Limitations

The result is only for equal-radius disks in exactly perpendicular planes, translated symmetrically along their common axis. No formula for arbitrary plane angles, unequal radii, shifted axes, or all possible disk pairs is claimed. The geometric analytic proof is complete, but the novelty comparison is not a guarantee against obscure historical computations or unindexed tables. No independent audit has been performed.

## References

1. S. R. Finch, *Convex Hull of Two Orthogonal Disks*, arXiv:1211.4514 (first public 2012-11-19), https://arxiv.org/pdf/1211.4514.
2. O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707 (2007), https://arxiv.org/pdf/0709.0707.
3. Á. G. Horváth, *Volume of convex hull of two bodies and related problems*, arXiv:1509.08859 (2015), https://arxiv.org/html/1509.08859v2.
4. E. D. Nash, A. F. Pir, F. Sottile and L. Ying, *Convex Hull of Two Circles in \(\mathbb R^3\)*, arXiv:1612.09382 (2016), https://arxiv.org/pdf/1612.09382.
