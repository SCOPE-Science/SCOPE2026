# Exact Minkowski asymmetry and center strata of panhandle matroid base polytopes

## Finding
For every triple of integers \(3\le r\le p\) and \(t\ge2\), put \(n=p+t\). The panhandle matroid \(\operatorname{Pan}_{r,p,n}\) has bases
\[
\mathcal B=\{B\subseteq[n]: |B|=r,\ |B\cap[p]|\ge r-1\}.
\]
Its base polytope \(P=\operatorname{conv}\{\mathbf 1_B:B\in\mathcal B\}\) has the exact intrinsic Minkowski asymmetry
\[
\boxed{\ s(P)=\rho=\max\left\{t,\frac{p+t-r}{r},\frac{r}{p-r+1}\right\}.\ }
\]
The **complete set of optimal centers** is
\[
\boxed{\ \mathcal M(P)=\left\{\frac{z}{\rho+1}: 1\le z_i\le\rho\ (1\le i\le n),\quad
\sum_{i=1}^{n}z_i=r(\rho+1),\quad\sum_{i=p+1}^{n}z_i\le\rho\right\}.\ }
\]
An explicit optimal center is specified by
\[
v=\max\{t,r(\rho+1)-p\rho\},\qquad
z_i=\begin{cases}(r(\rho+1)-v)/p,&1\le i\le p,\\v/t,&p<i\le n,\end{cases}
\qquad c=z/(\rho+1).
\]
The affine dimension of the entire minimizing-center set is
\[
\boxed{\ \dim\operatorname{aff}\mathcal M(P)=
\begin{cases}
p-1,&\rho=t>\max\{(p+t-r)/r,\ r/(p-r+1)\},\\
t-1,&\rho=r/(p-r+1)>t,\\
0,&\text{otherwise}.
\end{cases}\ }
\]
The otherwise case includes the strict \((p+t-r)/r\)-dominated regime and either boundary tie with \(t\). All three strict regimes occur for infinitely many parameter choices.

## Assumptions and scope
The integer restrictions are \(3\le r\le p\) and \(t\ge2\), with \(n=p+t\). The ambient metric is irrelevant because Minkowski asymmetry is affine invariant. We use the convention
\[
s(P)=\inf\{\lambda\ge1:\exists c\in\operatorname{aff}(P),\ -(P-c)\subseteq\lambda(P-c)\}.
\]
The polytope has affine hull \(\sum_i x_i=r\) of dimension \(n-1\). For example, the vector with head coordinates \((r-1/2)/p\) and tail coordinates \(1/(2t)\) lies in its relative interior, because its coordinates are strictly between zero and one and its tail sum is \(1/2<1\).

The essential structural input is the exact halfspace model of Hanely et al., Proposition 4.4:
\[
P=\left\{x\in[0,1]^n:\sum_{i=1}^{n}x_i=r,\quad\sum_{i=p+1}^{n}x_i\le1\right\}.
\]
Every individual coordinate takes both values zero and one on some base vertex, and the tail sum takes both zero and one. These claims follow directly from the two types of bases, namely \(r\) head elements or \(r-1\) head elements plus one tail element.

## Proof
Fix \(\lambda\ge1\) and \(c\in\operatorname{aff}(P)\), and put \(z=(\lambda+1)c\). The reflected containment condition is equivalent to requiring \(((\lambda+1)c-x)/\lambda\in P\) for **every** \(x\in P\). It suffices to test the displayed halfspace inequalities of \(P\) against all vertices. Their exact attainable lower and upper support values give, respectively, the following necessary and sufficient linear inequalities:
\[
1\le z_i\le\lambda\quad(1\le i\le n),\qquad
\sum_{i=1}^{n}z_i=r(\lambda+1),\qquad
\sum_{i=p+1}^{n}z_i\le\lambda.\tag{1}
\]
Indeed, applying the reflected map to an edge coordinate \(x_i\in[0,1]\) and allowing \(x_i=0,1\) produces \(z_i\le\lambda\) and \(z_i\ge1\). Applying it to the tail-sum constraint, whose minimum is zero, produces the last inequality. The affine sum is preserved precisely when the displayed equality holds. Thus no other constraints remain.

Summing the tail lower bounds in (1) gives \(\lambda\ge t\). Summing all coordinate lower bounds gives \(r(\lambda+1)\ge p+t\), or \(\lambda\ge(p+t-r)/r\). Summing the head upper bounds and the tail upper bound gives \(r(\lambda+1)\le(p+1)\lambda\), or \(\lambda\ge r/(p-r+1)\). Hence every feasible dilation has \(\lambda\ge\rho\).

Conversely, set \(\lambda=\rho\), and let \(S=r(\rho+1)\). Choose
\[
v=\max\{t,S-p\rho\}.
\]
The three already established inequalities imply \(v\le\rho\), \(v\le S-p\), and \(v\ge t\). Explicitly, \(S-p\rho\le\rho\) is exactly the third bound, while \(t\le S-p\) is exactly the second bound. As \(\rho\ge1\), the remaining comparisons are immediate. Consequently \(t\le v\le\rho\) and \(p\le S-v\le p\rho\). Assign the first \(p\) coordinates of \(z\) the common value \((S-v)/p\) and the last \(t\) coordinates the common value \(v/t\). They satisfy (1), proving \(s(P)=\rho\) and the explicit-center formula. Substituting \(\lambda=\rho\) into (1) proves that the displayed center locus is complete.

To determine its affine dimension, write \(L=(p+t-r)/r\) and \(U=r/(p-r+1)\). If \(\rho=L>t\), summing \(z_i\ge1\) forces \(z_i=1\) for every coordinate, so the center is unique. If \(\rho=U>t\), the upper-bound sum is tight; therefore every head coordinate equals \(\rho\) and the tail sum equals \(\rho\). The latter coordinates form a hyperplane slice of \([1,\rho]^t\), and \(\rho>t\) ensures that their common point \(\rho/t\) lies strictly inside the cube, yielding affine dimension \(t-1\).

If \(\rho=t>L,U\), the tail sum is at most \(t\) while its \(t\) summands are all at least one, so every tail coordinate equals one. The head sum is \(r(t+1)-t\), which lies strictly between \(p\) and \(pt\) by the assumed strict inequalities. Hence the remaining head coordinates form a relatively full hyperplane slice of \([1,t]^p\) with dimension \(p-1\). At either tie \(\rho=t=L\) or \(\rho=t=U\), the head entries are all forced to one or to \(t\), respectively, so the center is unique. For \(3\le r\le p\), the two bounds \(L\) and \(U\) cannot simultaneously exceed \(t\): the first would require \(p>r(t+1)-t\), while the second would require \(p<r+r/t-1\), which are incompatible for \(r\ge3\), \(t\ge2\). These cases exhaust all possibilities.

## Verification
The standalone `panhandle_verify.py` reproduces exact rational checks without nonstandard dependencies. It loops over \(3\le p\le9\), \(3\le r\le p\), and \(2\le t\le6\), enumerates every base vertex for each choice, constructs the proposed center using rational arithmetic, and verifies the reflected image of **each** vertex satisfies every defining halfspace. It checks all asserted support extrema and includes witnesses for each of the three strict regimes. The run returned `EXACT_VERIFY_OK`: 140 parameter triples, 23,440 base vertices, and 616,260 exact facet/containment comparisons.

To reproduce: `python3 panhandle_verify.py`. These are finite cross-checks of the displayed formulas; the unbounded theorem is proved by the analytic argument above.

Examples of the distinct center strata are \((r,p,t)=(3,15,2)\) with \(\rho=14/3\) and a unique center; \((6,6,2)\) with \(\rho=6\) and a one-dimensional center family; and \((3,5,3)\) with \(\rho=3\) and a four-dimensional center family. The parameter choices \((3,7,2)\) and \((6,7,3)\) attain the two tie configurations, each yielding a unique center.

## Relationship to prior work
Hanely, Martin, McGinnis, Miyata, Nasr, Vindas-Meléndez and Yin introduced panhandle matroids and identified their base polytopes as pieces cut from hypersimplices; Proposition 4.4 supplies the halfspace system used here. Their main invariants are Ehrhart polynomials and volumes, whereas this finding determines an intrinsic affine-symmetry measure and all optimal centers. Work by McGinnis and by Deligeorgaki, McGinnis and Vindas-Meléndez develops panhandle Ehrhart positivity and bounds, not this reflection problem. General Schubert-matroid Ehrhart treatments provide a broader combinatorial setting but no identified implication giving this exact asymmetry or the center-stratum dimensions.

## Limitations
This theorem covers the stated nondegenerate parameter range only. It does not assert a Minkowski-asymmetry formula for arbitrary lattice-path matroids, arbitrary paving matroids, or other Schubert matroid base polytopes. It does not calculate Euclidean John/Löwner ellipsoids, which are different invariants. No claim of independent verification, exhaustive bibliographic priority, or authorship attribution is made. Although the examined primary literature and published-result searches did not identify a dominating formulation, an earlier theorem under different terminology remains possible.

## References
1. D. Hanely, J. L. Martin, D. McGinnis, D. Miyata, G. D. Nasr, A. R. Vindas-Meléndez and M. Yin, *Ehrhart Theory of Paving and Panhandle Matroids*, arXiv:2201.12442 (v1 posted 2022-01-28), especially Section 4 and Proposition 4.4. https://arxiv.org/abs/2201.12442 ; https://arxiv.org/html/2201.12442v3
2. D. McGinnis, *Ehrhart positivity for a certain class of panhandle matroids*, arXiv:2303.04113 (2023). https://arxiv.org/abs/2303.04113
3. D. Deligeorgaki, D. McGinnis and A. R. Vindas-Meléndez, *Ehrhart Bounds for Panhandle and Paving Matroids Through Enumeration of Chain Forests*, arXiv:2311.01640 (2023). https://arxiv.org/abs/2311.01640
4. W. Fan and J. Li, *On the Ehrhart Polynomial of Schubert Matroids*, arXiv:2110.11549 (2021). https://arxiv.org/abs/2110.11549
