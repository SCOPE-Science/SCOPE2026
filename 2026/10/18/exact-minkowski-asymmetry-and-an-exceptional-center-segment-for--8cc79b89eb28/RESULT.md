# Exact Minkowski asymmetry and an exceptional center segment for interval-incidence polytopes

## Finding
For every integer \(n\ge2\), consider the zero-inclusive consecutive-ones polytope
\[
P_n=\operatorname{conv}\!\left(\{\mathbf0\}\cup\{\mathbf1_{[i,j]}:1\le i\le j\le n\}\right)\subset\mathbb R^n.
\]
Here \(\mathbf1_{[i,j]}\) is one on the indicated interval and zero elsewhere. Define Minkowski asymmetry by
\[
s(P_n)=\min_{c\in\mathbb R^n}\min\{s\ge1:P_n-c\subseteq s(c-P_n)\}.
\]
Its exact value in every dimension is
\[
\boxed{s(P_n)=\begin{cases}1,&n=2,\\ \frac32,&n=3,\\2,&n\ge4.\end{cases}}
\]
The entire set \(\mathcal M_n\) of optimal Minkowski centers is
\[
\boxed{\begin{aligned}
\mathcal M_2&=\{(\frac12,\frac12)\},\\
\mathcal M_3&=\{(\frac25,\frac35,\frac25)\},\\
\mathcal M_4&=\left\{\frac13(1,1+t,1+t,1):0\le t\le1\right\},\\
\mathcal M_n&=\{\frac13\mathbf1\}\quad(n\ge5).
\end{aligned}}
\]
Thus the asymmetry stabilizes at two in dimension four, whereas the minimizing-center locus has positive affine dimension **only** in dimension four: a line segment, as opposed to a singleton in every other dimension.

## Assumptions and scope
This is the standard zero-inclusive interval-incidence realization, equivalently the connected-block polytope of a block path on \(n\) blocks. By the unimodular transformation of Bruckamp, Chimani and Juhnke, it is also affinely equivalent to an origin-adjoined positive type-\(A_n\) root polytope; Minkowski asymmetry is invariant under invertible affine maps. The nonzero-only interval-vector polytope is a different object. No Euclidean structure is needed for the stated invariant or its centers.

A point \(c\) is an \(s\)-center precisely when
\[
\frac{(s+1)c-v}{s}\in P_n\quad\text{for every vertex }v\text{ of }P_n.
\tag{1}
\]
This follows by rewriting the containment \(P_n-c\subseteq s(c-P_n)\) and using convexity.

## Proof
**1. Membership by positive variation.** Set \(w_0=0\) and, for \(w\in\mathbb R^n\), define
\[
V^+(w)=\sum_{i=1}^n\max\{0,w_i-w_{i-1}\}.
\]
Then
\[
\boxed{P_n=\{w\in\mathbb R_{\ge0}^n:V^+(w)\le1\}.}\tag{2}
\]
For an interval indicator, the positive variation is exactly one, and for zero it is zero; convexity of \(V^+\) establishes one inclusion. Conversely, for nonnegative \(w\) write its layer-cake decomposition \(w_i=\int_{0}^{\infty}\mathbf1_{\{w_i>t\}}\,dt\). Every superlevel subset of the index path decomposes into maximal, disjoint consecutive intervals. Decomposing the superlevel indicators into the corresponding interval indicators expresses \(w\) as a nonnegative combination of interval vertices. The total coefficient mass is
\[
\int_0^{\infty}\#\{\text{runs of }\{i:w_i>t\}\}\,dt=V^+(w)\le1.
\]
The remaining coefficient goes on the zero vertex. This proves (2) in every dimension, including on the boundary.

**2. General lower bounds.** If a valid linear inequality \(a\cdot w\le b\) has minimum \(\ell=\min_{w\in P_n}a\cdot w\), condition (1) forces
\[
(s+1)a\cdot c\le s b+\ell.\tag{3}
\]
Apply (3) to \(w_i\ge0\) and \(w_i\le1\), both valid and attained at interval vertices. Every \(s\)-center obeys
\[
\frac1{s+1}\le c_i\le\frac{s}{s+1}.\tag{4}
\]
For any three indices \(i<j<k\), the valid alternating inequality \(w_i-w_j+w_k\le1\) has maximum one and minimum minus one (at the singleton vertex \(\mathbf1_{\{j\}}\)). Hence
\[
c_i-c_j+c_k\le\frac{s-1}{s+1}.\tag{5}
\]
For \(n\ge4\), choose \(i<j<k<\ell\). Adding (5) for the triples \((i,j,k)\) and \((j,k,\ell)\) yields
\[
c_i+c_\ell\le\frac{2(s-1)}{s+1}.
\]
By (4) the left side is at least \(2/(s+1)\), so necessarily \(s\ge2\). For \(n=3\), (4) and (5) instead give
\[
\frac{2-s}{s+1}\le c_1-c_2+c_3\le\frac{s-1}{s+1},
\]
thus \(s\ge3/2\). For \(n=2\) the basic definition gives \(s\ge1\).

**3. Achieving the bounds.** If \(n\ge4\), let \(s=2\) and \(c_0=\mathbf1/3\). For any interval-indicator vertex \(v\), including \(v=0\),
\[
\frac{3c_0-v}{2}=\frac{\mathbf1-v}{2}\in P_n.
\]
Indeed, the complement of a contiguous interval is the union of at most two disjoint contiguous intervals, so half its incidence vector is a convex combination of at most two interval indicators and zero. This proves (1), even at the zero vertex. For \(n=2\), \(P_2=[0,1]^2\), centrally symmetric around \((1/2,1/2)\), giving \(s=1\).

For \(n=3\), take \(s=3/2\) and \(c=(2/5,3/5,2/5)\). By (2), the three-dimensional polytope has the equivalent inequalities
\[
0\le w_i\le1\quad(i=1,2,3),\qquad w_1-w_2+w_3\le1.\tag{6}
\]
Indeed, the positive-variation expression is the maximum of \(w_1,w_2,w_3,w_1-w_2+w_3\). For every vertex \(v\), the reflection in (1) is
\[
y=\frac{5c-2v}{3}=\frac13(2-2v_1,3-2v_2,2-2v_3).
\]
Its coordinates all lie in \([0,1]\). Moreover
\[
y_1-y_2+y_3=\frac{1-2(v_1-v_2+v_3)}3\le1
\]
since every interval vertex satisfies \(v_1-v_2+v_3\ge-1\). Thus \(y\in P_3\), and \(s(P_3)=3/2\).

**4. Exhausting all centers.** At \(s=2\) in dimensions \(n\ge4\), write \(c_i=1/3+d_i\). Equations (4) and (5) become
\[
0\le d_i\le\frac13,\qquad d_i-d_j+d_k\le0\quad(i<j<k).\tag{7}
\]
For each quadruple \(i<j<k<\ell\), adding the two triple inequalities on \((i,j,k)\) and \((j,k,\ell)\) yields \(d_i+d_\ell\le0\). Thus \(d_i=d_\ell=0\), and the individual inequalities force \(d_j=d_k\). At \(n=4\), all necessary coordinates therefore have the form
\[
c=\frac13(1,1+t,1+t,1),\quad0\le t\le1.\tag{8}
\]
Both endpoints are feasible. The first was verified above. For the second, put \(c_1=(1,2,2,1)/3\); for every interval vertex \(v\), the vector \((3c_1-v)/2\) is nonnegative and has positive variation at most one. This is checked directly, and exhaustively, on the eleven vertices \(0000\), \(1000\), \(1100\), \(1110\), \(1111\), \(0100\), \(0110\), \(0111\), \(0010\), \(0011\), \(0001\): their values of \(V^+(3c_1-v)\) are respectively \(2,2,2,1,1,2,1,1,2,2,2\). By (2) and (1), \(c_1\) is optimal. The set of \(s\)-centers is convex (it is defined by linear inequalities (3)), so (8) is the entire feasible optimal segment.

For \(n\ge5\), apply the quadruple conclusion to \((1,2,3,4)\) and \((2,3,4,5)\). It forces \(d_1=\cdots=d_5=0\). Every remaining \(d_j\), with \(j>5\), vanishes by the quadruple \((1,2,3,j)\). Therefore \(c_0\) is the unique center for \(n\ge5\).

For \(n=3\), equality in the already sharp lower-bound chain forces \(c_1=c_3=2/5\) and \(c_2=3/5\). For \(n=2\), the unit square has a unique symmetry center. This proves the complete classification.

## Verification
A standalone exact-rational checker `verify_interval_asymmetry.py` constructs all original interval vertices through dimension eighteen and verifies the reflection membership condition (1) using (2) for each proposed extremal center, giving 1,167 exact checks. It separately evaluates the eleven four-dimensional endpoint variations and exercises the sharp lower-bound certificates. The checker was executed from the embedded source and printed `VERIFY_OK`.

The infinite-dimensional assertion is proved algebraically in the preceding sections; the finite checker does not establish the universal statements by enumeration. The endpoint enumeration in dimension four is exhaustive because that polytope has exactly eleven vertices.

## Relationship to prior work
Bruckamp, Chimani and Juhnke (original public version 2023) introduce the connected-block formulation and give its complete facet description, its edges, its Gorenstein property, and its Narayana \(h^*\)-polynomial in the block-path case. Their Theorem 7.6 identifies the affine-unimodular correspondence with positive type-\(A\) root polytopes. Their inspected article does not classify Minkowski asymmetry or optimal reflection centers.

A published study titled *Block-path connected-block polytopes have parity-split inradii and large incenter loci* considers exactly the same zero-inclusive family, but its invariant is the Euclidean largest inscribed ball, which is not the affine-invariant Minkowski reflection problem treated here; neither its sharp metric radii nor its center dimensions imply (or agree with) the present optimal reflection centers. Another result titled *Exact 1-skeleton and simple-vertex exhaustion of transitive-tournament root polytopes* treats the related positive-root family and its graph, not affine asymmetry. The known general Minkowski asymmetry classification for **order polytopes** also has different hypotheses; the present zero-inclusive interval-incidence body is not being identified as an order polytope.

The proof here only requires the displayed vertex definition; its nontrivial ingredient is the sharp two-triple lower bound and complete equality-case classification. Prior facet descriptions are supporting context, not used as a hidden mathematical premise.

## Limitations
The result concerns the zero-inclusive, unweighted path case. It does not classify arbitrary connected-block graphs, weighted interval vectors, or the nonzero-only interval polytope. Affine equivalence preserves the asymmetry but does not preserve a particular coordinate description of its center set. An equivalent older result under alternative interval or root terminology cannot be excluded solely from the inspected corpus. No independent external mathematical validation is claimed.

## References
1. Justus Bruckamp, Markus Chimani, Martina Juhnke, *On the Connected Blocks Polytope*, arXiv:2304.06318, initial version 2023-04-13; *Discrete & Computational Geometry* **73** (2025), 946–972, DOI 10.1007/s00454-024-00675-5, especially Theorems 5.11 and 7.6. https://arxiv.org/abs/2304.06318
2. Mohamed Didi Biha, Hervé L. M. Kerivin, Peh H. Ng, *Polyhedral study of the connected subgraph problem*, *Discrete Mathematics* **338** (2015), 80–92, DOI 10.1016/j.disc.2014.08.026. https://doi.org/10.1016/j.disc.2014.08.026
3. Matthias Beck, Jessica De Silva, Gabriel Dorfsman-Hopkins, Joseph Pruitt, Amanda Ruiz, *The combinatorics of interval-vector polytopes*, *Electronic Journal of Combinatorics* **20** (2013), P22, arXiv:1211.2039. https://arxiv.org/abs/1211.2039
