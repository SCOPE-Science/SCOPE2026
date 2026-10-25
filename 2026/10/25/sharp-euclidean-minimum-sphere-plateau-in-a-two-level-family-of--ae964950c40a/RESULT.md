# Sharp Euclidean minimum-sphere plateau in a two-level family of marked poset polytopes

## Finding
Fix integers \(p,q\ge2\) and a real parameter \(0\le t\le1\). Consider the complete two-level marked poset with \(p\) mutually incomparable lower elements, \(q\) mutually incomparable upper elements, all lower elements below all upper elements, and additional marked bottom and top elements of values zero and one. Set the lower transfer parameters to zero and every upper transfer parameter to \(t\) in the continuous marked-poset family of Fang--Fourier--Litza--Pegel [1]. Its standard-coordinate polytope is
\[
K_{p,q}(t)=\bigl\{(x,y)\in\mathbb R^p\times\mathbb R^q:
 x_i\ge0,\quad (1-t)x_i\le y_j,\quad y_j+t x_i\le1
\text{ for all }i,j\bigr\}.
\tag{1}
\]
Put \(u=t(1-t)\), \(d=p-qu\), \(z_+=\max\{z,0\}\), and
\[
a=\frac{d_+}{2p}.
\tag{2}
\]
The **unique smallest enclosing ball** of \(K_{p,q}(t)\), for the ordinary Euclidean metric in all \(p+q\) coordinates, has center
\[
\boxed{c_{p,q}(t)=(a\mathbf1_p,\tfrac12\mathbf1_q)}
\]
and **exact squared radius**
\[
\boxed{R_{p,q}(t)^2=\frac q4+\frac{\bigl(p-qt(1-t)\bigr)_+^2}{4p}.}
\tag{3}
\]
This includes the order-polytope endpoint \(t=0\) and the mixed chain-order endpoint \(t=1\).

The vertices have the following complete description (with duplicate occurrences of the zero lower vector omitted):
\[
\begin{aligned}
\mathcal A&=\{(\mathbf0_p,\varepsilon):\varepsilon\in\{0,1\}^q\},\\
\mathcal B&=\{(\delta,(1-t)\mathbf1_q):\delta\in\{0,1\}^p\setminus\{\mathbf0_p\}\}.
\end{aligned}
\tag{4}
\]
There are exactly \(2^q+2^p-1\) distinct vertices at every parameter. A *contact vertex* means a vertex on the boundary of the minimum enclosing ball. Their exact classification is:

* If \(t=0\) or \(t=1\), every vertex in (4) is a contact.
* If \(0<t<1\) and \(qt(1-t)\le p\), the contacts are **every** vertex of \(\mathcal A\) and the **unique** point \((\mathbf1_p,(1-t)\mathbf1_q)\) of \(\mathcal B\) with all lower coordinates one: exactly \(2^q+1\) contacts.
* If \(0<t<1\) and \(qt(1-t)>p\), the contacts are **only** the \(2^q\) vertices of \(\mathcal A\).

The radius locks at \(R_{p,q}(t)=\sqrt q/2\) and the lower center coordinate becomes zero precisely when \(qt(1-t)\ge p\). A plateau interval of positive length occurs exactly when \(q>4p\), with boundaries
\[
\boxed{t_\pm=\frac{1\pm\sqrt{1-4p/q}}2.}
\tag{5}
\]
At \(q=4p\) the threshold is attained only at \(t=1/2\). For \(0<t<1\), the combinatorial face lattice is constant as \(t\) varies, by the face-lattice constancy theorem of [1], despite this sharp change in Euclidean center location and contact-orbit count.

## Assumptions and scope
The two marked elements are an artificial bottom and top, with values zero and one; only the \(p+q\) unmarked coordinates carry the Euclidean metric. Every lower element is covered by every upper element; bottom covers every lower element and every upper element is covered by top. In the notation of [1, Definition 1.2], the lower unmarked transfer parameters equal zero and the upper parameters all equal \(t\). Substitution into the saturated-chain inequalities gives (1). In particular, this is a specific family of marked poset polytopes, **not** an arbitrary affine interpolation of two fixed polytopes. For \(p,q\ge2\), all coordinates are essential, and (1) has interior, for example lower entries sufficiently close to zero and upper entries close to one half.

The smallest enclosing Euclidean ball is also called the minimum covering ball or Chebyshev outer ball. The radius in (3) concerns the full-dimensional realization (1), not the maximum inscribed ball or the John ellipsoid. No arbitrary coordinate rescaling is allowed.

## Proof
**1. Exact vertex set.** Write \(M=\max_{1\le i\le p}x_i\). The first group of constraints gives \(x_i\ge0\). Combining the other constraints for an index attaining \(M\) gives
\[
(1-t)M\le y_j\le1-tM
\quad(j=1,\ldots,q),
\]
which forces \(0\le M\le1\); consequently \(0\le x_i\le1\). When \(M=0\), the feasible points are \((0,y)\) with \(y\in[0,1]^q\), the convex hull of \(\mathcal A\). When \(M=1\), every \(y_j=1-t\), while the vector \(x\) belongs to \([0,1]^p\) with at least one coordinate one; it lies in the convex hull of the nonzero zero-one vectors, giving the \(\mathcal B\)-hull.

For \(0<M<1\), put
\[
v_j=\frac{y_j-(1-t)M}{1-M},\qquad u_i=\frac{x_i}{M}.
\]
Then \(v\in[0,1]^q\) and \(u\in[0,1]^p\) with at least one coordinate one, and the exact decomposition
\[
(x,y)=(1-M)(\mathbf0_p,v)+M(u,(1-t)\mathbf1_q)
\tag{6}
\]
places the point in \(\operatorname{conv}(\mathcal A\cup\mathcal B)\). Every listed corner directly satisfies (1), proving equality of that hull with the polytope. Each vertex of \(\mathcal A\) is extreme because it is a cube corner on the face \(x=0\). Every vertex of \(\mathcal B\) is extreme because its lower projection is a nonzero corner of \([0,1]^p\), and at a point with at least one lower coordinate one the upper fiber is the singleton \((1-t)\mathbf1_q\). This proves (4) with no missing vertices.

**2. Squared distances from the proposed center.** Put \(a=d_+/(2p)\) as in (2), and \(c=(a\mathbf1_p,\tfrac12\mathbf1_q)\). Every vertex of \(\mathcal A\) has squared distance
\[
\|v-c\|^2=pa^2+\frac q4=R_{p,q}(t)^2.
\tag{7}
\]
If a vertex of \(\mathcal B\) has exactly \(k\) lower coordinates equal to one (\(1\le k\le p\)), its squared distance is
\[
\|v-c\|^2=pa^2+k(1-2a)+q(t-\tfrac12)^2.
\tag{8}
\]
Since \((t-\tfrac12)^2=\tfrac14-t(1-t)\), subtraction of (8) from (7) gives the **exact gap**
\[
R_{p,q}(t)^2-\|v-c\|^2
=qt(1-t)-k(1-2a).
\tag{9}
\]
If \(p>qt(1-t)\), then \(1-2a=qt(1-t)/p\), so (9) is \(qt(1-t)(1-k/p)\ge0\). If \(p\le qt(1-t)\), then \(a=0\), so (9) is \(qt(1-t)-k\ge p-k\ge0\). Thus the radius (3) encloses every listed vertex, hence all of (1).

For \(t=0,1\), the right-hand side of (9) is zero for every \(k\); all listed vertices are contacts. For \(0<t<1\), the gap in (9) vanishes precisely when \(k=p\) in the regime \(qt(1-t)\le p\); it is strictly positive for every \(k\) if \(qt(1-t)>p\). The vertex classification in the Finding follows, including the threshold equality case.

**3. A global optimality and uniqueness certificate.** It remains to prove that no shifted ball has smaller radius; symmetry alone would not suffice. If \(a=0\), the proposed center \(c\) is the mean of the \(2^q\) contact vertices \(\mathcal A\): independently select each upper coordinate as a fair Bernoulli bit. This gives a probability distribution of contacts with mean \(c\).

If \(a>0\), set
\[
\theta=\frac{\tfrac12-a(1-t)}{1-a}.
\tag{10}
\]
Because \(0<a\le1/2\) and \(0\le t\le1\), one has \(0\le\theta\le1\). Place total probability \(a\) on the all-ones lower vertex \(b_*=(\mathbf1_p,(1-t)\mathbf1_q)\), and total probability \(1-a\) on \(\mathcal A\), using independent Bernoulli-\(\theta\) upper bits within \(\mathcal A\). By (9), every positively weighted vertex is a contact. The resulting mean is exactly
\[
a b_*+(1-a)(\mathbf0_p,\theta\mathbf1_q)
=(a\mathbf1_p,\tfrac12\mathbf1_q)=c.
\tag{11}
\]
For any probability distribution of contact vertices \(V\) with \(\mathbb EV=c\), and every alternative center \(z\in\mathbb R^{p+q}\), the variance identity states
\[
\mathbb E\|V-z\|^2
=\mathbb E\|V-c\|^2+\|z-c\|^2
=R_{p,q}(t)^2+\|z-c\|^2.
\tag{12}
\]
At least one vertex therefore has squared distance at least the right side of (12) from \(z\). Thus every enclosing ball has squared radius at least (3), with a **strictly larger** required squared radius whenever \(z\ne c\). The displayed center is globally optimal and unique, establishing the theorem without a conjectured spherical symmetry assumption.

**4. Plateau and combinatorial distinction.** The positive-part expression in (3) is constant at \(q/4\) exactly when \(qt(1-t)\ge p\). The function \(t(1-t)\) has maximum \(1/4\) at \(t=1/2\), so a nonempty strict interval where \(qt(1-t)>p\) exists precisely for \(q>4p\), and solving the quadratic inequality gives (5). The lower center coordinate changes from positive to zero there, and the entire \(\mathcal B\) vertex class becomes strictly internal to the sphere. On the other hand, all transfer parameters \((0_p,t\mathbf1_q)\) with \(0<t<1\) lie in the relative interior of the same face of the parameter hypercube. Theorem [1] therefore asserts a constant combinatorial type throughout, not a constant Euclidean metric.

## Verification
A standalone `verify.py` enumerates the candidate vertex set, checks the exact rational squared-radius, contact counts, and contact-barycenter certificate for 126 parameter profiles, covering 81,618 candidate vertex occurrences, including endpoints and the strict plateau. It also independently enumerates all vertices of the halfspace system by intersections of active hyperplanes in 24 small-dimensional profiles, and solves the convex minimum-ball epigraph program in five additional profiles (including a strict plateau) using SLSQP. It reports `CHECK_OK` when successful. Run from the same directory using `python3 verify.py`; NumPy and SciPy are the only nonstandard Python dependencies. Numerical optimization tolerances are defined in the script. These finite calculations corroborate, but do not establish, the general all-integer, all-real-parameter claim; that claim follows from (6)--(12).

## Relationship to prior work
Fang, Fourier, Litza, and Pegel [1] define the universal continuous marked-poset family and prove that combinatorial type is fixed on the relative interior of each parameter-hypercube face. The present polytope is obtained by specialization of their Definition 1.2. Their treatment of transfer maps, Ehrhart equivalence, tropical subdivisions, and face lattices does not state (3), the enclosing-ball optimality certificate, or the contact screening threshold (5).

Ahmad, Fourier, and Joswig [2] treat maximal ranked posets, including two-level complete posets, and prove comparisons of face vectors of order and chain-order polytopes. Those face-count results do not determine the Euclidean outer sphere of the continuous interpolation.

Previously published calculations of the John ellipsoid of a balanced two-level order polytope concern a different optimization problem (maximum *inscribed ellipsoid*) and the endpoint realization. Previously published minimum-sphere formulas for complete multipartite *stable-set* polytopes with at least three parts explicitly exclude the two-part graph case and do not treat the continuous middle-parameter family. Neither implies the current covering-ball formula or its active-contact transition. General smallest-enclosing-ball characterizations provide the variance identity (12) but not the family-specific vertex list, exact center, phase boundary, or contact classification.

## Limitations
The theorem is for the complete height-two marked poset, all lower transfer parameters zero, all upper transfer parameters equal, and the standard unweighted Euclidean metric on the unmarked coordinate space. It does not establish analogous formulas for arbitrary marked posets, unequal transfer weights between upper elements, or transformed Euclidean norms. The plateau and contact counts are properties of the minimum enclosing sphere, not claims about inscribed ellipsoids or inballs. The proof is self-contained once the universal marked-poset definition and its face-type constancy theorem are supplied. An equivalent metric reformulation under terms such as convex hull of two families of cube corners or complete-bipartite stable-set interpolation could have been missed in bibliographic searches; this remains a bibliographic originality risk.

## References
1. Xin Fang, Ghislain Fourier, Jan-Philipp Litza, Christoph Pegel, *A Continuous Family of Marked Poset Polytopes*, arXiv:1712.01037v1 (first publicly posted 2017-12-04), https://arxiv.org/pdf/1712.01037; *SIAM Journal on Discrete Mathematics* 34 (2020), 611--639, DOI 10.1137/18M1228529. Definition 1.2 (p. 4) and face-lattice constancy theorem (p. 3).
2. Ibrahim Ahmad, Ghislain Fourier, Michael Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626v1 (first publicly posted 2023-09-04), https://arxiv.org/pdf/2309.01626; later journal publication *Discrete Applied Mathematics* 390 (2026), 28--39.
3. Richard P. Stanley, *Two poset polytopes*, *Discrete & Computational Geometry* 1 (1986), 9--23. Background definitions of order and chain polytopes.
4. Jack Elzinga and Donald Hearn, *The minimum sphere covering a convex polyhedron*, *Naval Research Logistics Quarterly* 21 (1974), 715--718, DOI 10.1002/nav.3800210414. General enclosing-sphere background.
