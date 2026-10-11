# Sharp minimum-sphere bounds for matroid independence polytopes distinguish uniform density from arboricity two

## Finding
Let \(M\) be a finite loopless matroid on a ground set \(E\) of size \(m\ge2\), with rank \(1\le r\le m\). Its standard independence polytope is
\[
P_I(M)=\operatorname{conv}\{\mathbf1_I:I\subseteq E\text{ independent}\}\subset\mathbb R^E.
\tag{1}
\]
Let the Euclidean metric be inherited from \(\mathbb R^E\), set
\[
u=\tfrac12\mathbf1_E,\qquad
 t=\min\{r/m,1/2\},\qquad q=t\mathbf1_E,
\]
and put
\[
\Phi(m,r)=\frac m4-m\left(\frac12-t\right)^2
=\begin{cases}
\frac{r(m-r)}m,&2r<m,\\[3pt]
\frac m4,&2r\ge m.
\end{cases}
\tag{2}
\]

**Theorem.** The unique minimum-enclosing-ball center is
\[
\boxed{c(M)=\operatorname{proj}_{P_I(M)}(u)},
\tag{3}
\]
and its squared radius is
\[
\boxed{R(M)^2=\frac m4-\|u-c(M)\|^2\le\Phi(m,r).}
\tag{4}
\]
The equality classes exhibit two different combinatorial mechanisms.

If \(2r<m\), equality in (4) holds exactly when
\[
\boxed{r_M(S)\ge\frac rm|S|\quad\text{for all }S\subseteq E.}
\tag{5}
\]
This is the uniformly dense matroid condition. In that case \(c(M)=(r/m)\mathbf1_E\), and the contact vertices are exactly the indicator vectors of all bases.

If \(2r\ge m\), equality in (4) holds exactly when
\[
\boxed{|S|\le2r_M(S)\quad\text{for all }S\subseteq E.}
\tag{6}
\]
By the matroid partition theorem, this means that the entire ground set can be partitioned into **two independent sets**. In that case \(c(M)=u\), and **every** independent-set indicator vertex is a contact.

The comparison has a quantitative form. For every nonempty \(S\subseteq E\), define the rank deficit
\[
\delta_M(S)=\bigl(t|S|-r_M(S)\bigr)_+,
\qquad(a)_+=\max\{a,0\}.
\]
Then
\[
\boxed{\Phi(m,r)-R(M)^2\ge
\max_{\varnothing\ne S\subseteq E}\frac{\delta_M(S)^2}{|S|}.}
\tag{7}
\]
This deficit bound is sharp as a universal inequality.

More generally, let \(w_e=1-2c_e(M)\). The complete set of contact vertices is
\[
\boxed{\{\mathbf1_I:I\text{ maximizes }\sum_{e\in I}w_e
\text{ over all independent sets}\}.}
\tag{8}
\]
The weights are nonnegative because \(c_e(M)\le1/2\) for every \(e\).

The radius also has the **random-independent-set variance** representation
\[
\boxed{R(M)^2=\max_{\mu}\sum_{e\in E}p_e(1-p_e),\qquad
p_e=\Pr_{I\sim\mu}(e\in I),}
\tag{9}
\]
where \(\mu\) ranges over all probability measures on the independent sets of \(M\). A maximizing measure has marginal vector \(c(M)\) and is supported on the contact sets (8).

## Assumptions and scope
The rank function is \(r_M(S)\), and all independent sets include the empty set. No loops are allowed, so (1) is full dimensional; parallel elements and disconnected matroids are allowed. The geometric embedding in (1) matters: arbitrary affine transformations do not preserve the stated Euclidean radii.

A fundamental matroid-polytope description is
\[
P_I(M)=\bigl\{p\in\mathbb R^E:p_e\ge0\ (e\in E),\quad p(S)\le r_M(S)\ (S\subseteq E)\bigr\},
\tag{10}
\]
where \(p(S)=\sum_{e\in S}p_e\). For comparison, the uniform matroid of rank \(r\) on \(E\) has
\[
P_I(U_{r,m})=[0,1]^m\cap\{p(E)\le r\}.
\tag{11}
\]
Its indicator vertices are all subsets of size at most \(r\). Its minimum-sphere formula serves as the rank-size envelope, rather than an assumption on arbitrary matroids.

The projection operator in (3) is ordinary Euclidean nearest-point projection onto a compact convex polytope. No algorithmic uniqueness or independence certification beyond the displayed proof is asserted.

## Proof
**1. An exact \(0/1\)-sphere identity.** Let \(V\) be any nonempty subset of \(\{0,1\}^m\), and let \(P=\operatorname{conv}V\). Put \(u=\frac12\mathbf1\), and let \(c\) be the unique closest point of \(P\) to \(u\). For each \(v\in V\), the Boolean identity \(\|v\|^2=\langle\mathbf1,v\rangle\) gives
\[
\|v-z\|^2=\|z\|^2+\langle\mathbf1-2z,v\rangle.
\tag{12}
\]
The projection variational inequality says
\[
\langle u-c,p-c\rangle\le0\quad(p\in P).
\tag{13}
\]
Consequently the linear functional \(\mathbf1-2c\) is maximized on \(P\) at \(c\). Equation (12) yields
\[
\max_{v\in V}\|v-c\|^2
=\|c\|^2+\langle\mathbf1-2c,c\rangle
=\langle\mathbf1,c\rangle-\|c\|^2
=\frac m4-\|u-c\|^2.
\tag{14}
\]
For any competing center \(z\in\mathbb R^m\), since \(c\in P=\operatorname{conv}V\), equation (12) gives
\[
\begin{aligned}
\max_{v\in V}\|v-z\|^2
&\ge\|z\|^2+\langle\mathbf1-2z,c\rangle\\
&=\|z-c\|^2+\langle\mathbf1,c\rangle-\|c\|^2.
\end{aligned}
\tag{15}
\]
Thus the ball (14) is globally optimal and **uniquely centered** at \(c\). Equality for a Boolean vertex in (14) holds exactly when it maximizes \(\langle\mathbf1-2c,v\rangle\), proving the general contact rule.

For any probability distribution \(\mu\) on \(V\), put \(p=\mathbb E_\mu v\in P\). The sum of coordinate Bernoulli variances equals
\[
\mathbb E_\mu\|v-p\|^2
=\sum_{e=1}^m(p_e-p_e^2)
=\frac m4-\|u-p\|^2.
\tag{16}
\]
Every \(p\in P\) arises as the mean of some \(\mu\); maximizing (16) over \(\mu\) proves (9) from (14). Since the maximizing mean is \(c\) and \(c\) lies in the supporting face (13), any convex representation of \(c\) is supported on contact vertices.

**2. Uniform comparison.** Apply part 1 first to the uniform independence polytope \(Q=P_I(U_{r,m})\). It is invariant under all coordinate permutations, and the projection of \(u\) onto \(Q\) is uniquely permutation invariant, of the form \(q=s\mathbf1\). Minimizing \(m(s-1/2)^2\) over \(0\le s\le r/m\) gives \(s=t\), so
\[
\operatorname{proj}_Q(u)=q,
\qquad R(Q)^2=\Phi(m,r).
\tag{17}
\]
Every independent set of \(M\) has cardinality at most \(r\), so \(P_I(M)\subseteq Q\). Thus
\[
\operatorname{dist}(u,P_I(M))\ge\operatorname{dist}(u,Q),
\]
and (4) follows. Because the projection onto \(Q\) is unique, equality occurs **if and only if** \(q\in P_I(M)\).

**3. Both equality classes and contacts.** If \(2r<m\), then \(q=(r/m)\mathbf1\). By (10), its feasibility in \(P_I(M)\) is exactly (5). The total coordinate sum of \(q\) equals \(r\), so it also lies in the matroid base polytope. Devriendt--Mulas call condition (5) uniform density and characterize it through constant base marginals. Since \(w_e=1-2r/m>0\) for all \(e\), the maximum-weight independent sets in (8) are exactly the bases.

If \(2r\ge m\), then \(q=u\). Its feasibility in (10) is exactly (6). Edmonds' matroid partition theorem says that (6) is equivalent to a partition \(E=A\sqcup B\), with both \(A\) and \(B\) independent. Conversely, such a partition provides the explicit midpoint representation
\[
u=\frac12\mathbf1_A+\frac12\mathbf1_B\in P_I(M).
\tag{18}
\]
Now \(w_e=0\) for every coordinate, so every independent-set vertex is a contact. This includes the boundary case \(2r=m\), where the two rank-feasibility conditions coincide.

The polytope \(P_I(M)\) is coordinatewise down-closed. If its projection \(c\) had some coordinate \(c_e>1/2\), decreasing only that coordinate to \(1/2\) would retain feasibility and strictly shorten its distance to \(u\); hence \(0\le c_e\le1/2\), completing (8).

**4. Quantitative loss from a rank obstruction.** Since \(q\) is the Euclidean projection of \(u\) onto \(Q\), for every \(p\in Q\) the projection inequality yields
\[
\|u-p\|^2
\ge\|u-q\|^2+\|p-q\|^2.
\tag{19}
\]
Every \(p\in P_I(M)\) satisfies \(p(S)\le r_M(S)\). For a nonempty subset with \(\delta_M(S)>0\), Cauchy--Schwarz implies
\[
\|p-q\|^2\ge\frac{\bigl(q(S)-p(S)\bigr)^2}{|S|}
\ge\frac{\delta_M(S)^2}{|S|}.
\tag{20}
\]
Minimizing (19) over \(p\in P_I(M)\) and taking the maximum over nonempty \(S\) proves (7).

To check sharpness, let
\[
M=U_{1,3}\oplus U_{2,2}.
\]
Its five-coordinate independence polytope is the Cartesian product of a standard three-coordinate simplex and a two-coordinate square. Euclidean projection of \(u\) acts separately on factors, giving
\[
c=(1/3,1/3,1/3,1/2,1/2).
\]
Therefore
\[
R(M)^2=\frac54-3\left(\frac16\right)^2=\frac76,
\qquad \Phi(5,3)-R(M)^2=\frac1{12}.
\]
For the first three-element parallel class \(S\), \(t=1/2\), \(r_M(S)=1\), and \(\delta_M(S)=1/2\); consequently \(\delta_M(S)^2/|S|=1/12\). Thus the coefficient in (7) cannot be improved uniformly. The contact vertices are the three singleton choices from the first factor times the four Boolean vertices in the second factor, exactly \(12\) contacts.

**5. A graphic illustration.** For the graphic matroid of \(K_n\), \(n\ge3\), the ground set has \(m=n(n-1)/2\) edges and rank \(r=n-1\). The uniform distribution on its spanning trees has equal edge marginals \(r/m=2/n\), because the complete graph is edge-transitive. Hence its matroid is uniformly dense. For \(n\ge5\), the low-rank equality formula gives
\[
\boxed{R(P_I(M(K_n)))^2=\frac{(n-1)(n-2)}n,
\qquad c=\frac2n\mathbf1_{E(K_n)},}
\tag{21}
\]
with exactly the spanning-tree indicators as contacts. For \(n=3,4\), the rank inequalities imply two-forest partition and the high-rank equality case applies; the center is \(u\) and every spanning-forest indicator is a contact.

## Verification
The proof establishes (3)--(9) for **every finite loopless matroid** with \(m\ge2\), not only enumerated examples.

The accompanying `verify.py` reconstructs uniform, partition, and small graphic matroids by exact rank functions. For each, it enumerates every subset of the ground set, checks the rank inequalities, numerically computes the Euclidean projection using the complete rank-inequality description, compares the farthest independent-set vertex distance with (4), checks the sharp uniform envelope and equivalence conditions, verifies (7), and independently solves the minimum-enclosing-ball epigraph problem for a selected range. It also replays the sharp direct-sum example with exact rational arithmetic. Requires Python 3, NumPy, and SciPy.

The computations test finite families and serve only as corroboration. They cannot certify the all-matroid theorem or global bibliographic originality.

## Relationship to prior work
Ferroni's early work establishes the standard matroid independence-polytope object and develops Ehrhart-positive tilings of its uniform members. Ferroni--McGinnis treat uniform-matroid independence polytopes explicitly in a geometry-classified study of prism slices and Ehrhart theory. Neither same-object full text contains Euclidean minimum-sphere or contact classifications.

Devriendt--Mulas **already establish** the equivalence between uniform density, constant marginals on bases, and feasibility of a constant point in the matroid base polytope. The equivalence in (5) is credited to that literature: the present statement is its **new Euclidean radius equality interpretation**, not a rediscovery of uniform density. Edmonds' classical matroid partition theorem **already establishes** the equivalence between (6) and a partition into two independent sets; the present contribution is the exact **sphere saturation** and all-vertex contact geometry for this combinatorial class.

For the uniform matroid \(U_{r,m}\), the displayed result specializes to the established uniform-independence-polytope outer-radius phase law. The general theorem is strictly broader: it determines the exact center of **every** matroid independence polytope by a convex projection and classifies **all** matroids saturating either rank-size envelope. Neither the uniform specialization nor prior fixed-rank matroid-base-polytope radius statements imply the present full-dimensional assertion. The nonuniform sharp graphic family and rank-defect example show that the result is not simply a relabeling of the uniform case.

More generally, the projection calculation (12)--(16) follows standard minimum-sphere duality for Boolean vertex configurations; no novelty is asserted for that geometric identity in isolation. The claimed structural contribution is the complete pair of matroid equality classes, the contact geometry, and the quantitative rank-defect certificate.

## Limitations
All Euclidean statements concern the standard \(0/1\) indicator-vector realization. The sphere does not have to be centered at the coordinatewise midpoint, and non-uniform-density matroids can have several different center coordinates. For a general matroid, (3) is an exact strongly convex optimization characterization, **not** a closed radical formula for all coordinates.

The rank-defect inequality (7) is a rigorous one-sided quantitative bound; it is not asserted to be equality for every matroid. The equality classes rely on classical base-polytope uniform-density and matroid-partition theorems, which are explicitly credited. The generic Boolean-sphere projection identity may occur in standard optimization treatments under different terminology. In particular, the absence of a matching statement in targeted searches cannot establish worldwide novelty, and independent mathematical review is not claimed.

## References
1. Luis Ferroni and Daniel McGinnis, *Lattice points in slices of prisms*, arXiv:2202.11808, initial public version 2022-02-23; *Canadian Journal of Mathematics* 77 (2025), 1013--1040, DOI 10.4153/S0008414X24000233. Primary MSC2020 52B20.
2. Luis Ferroni, *Integer point enumeration on independence polytopes and half-open hypersimplices*, arXiv:2012.04711, initial public version 2020-12-08; *Discrete Mathematics* 344 (2021), 112446, DOI 10.1016/j.disc.2021.112446.
3. Karel Devriendt and Raffaella Mulas, *Uniform density in matroids, matrices and graphs*, arXiv:2306.15267, initial public version 2023-06-27; *Australasian Journal of Combinatorics* 94 (2026), 145--176.
4. Jack Edmonds, *Minimum partition of a matroid into independent subsets*, *Journal of Research of the National Bureau of Standards* 69B (1965), 67--72, DOI 10.6028/jres.069B.004.
