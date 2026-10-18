# A greatest-common-divisor law for Euclidean inballs and center cubes of rectangular Monge polytopes

## Finding
For integers \(p,q\ge2\), put \(g=\gcd(p,q)\), \(m=pq\), and \(\alpha=\sqrt{1-1/m}\). Let the normalized, nonsymmetric **rectangular Monge polytope** be
\[
\mathcal M_{p,q}=\left\{X\in\mathbb R_{\ge0}^{p\times q}:\sum_{i,j}X_{ij}=1,\quad X_{i,j+1}+X_{i+1,j}-X_{ij}-X_{i+1,j+1}\ge0\ (0\le i<p-1,\ 0\le j<q-1)\right\}.
\]
In the intrinsic Frobenius metric on its affine hyperplane, its exact Euclidean inradius is
\[
\boxed{r_{p,q}=\left[pq\alpha+\frac{p^2q^2-p^2-q^2+g^2}{6}\right]^{-1}.}
\]
**All** centers of maximum-radius contained balls form an affine cube of dimension \(g-1\). Hence the incenter is unique if and only if \(p\) and \(q\) are coprime. The \((p-1)(q-1)\) adjacent Monge facets are tangent at every such center. At a cube point with exactly \(e\) parameters equal to either endpoint, the ball is also tangent to exactly \(p+q-g+e\) coordinate nonnegativity facets. Thus the total number of tangent facets is \(pq+1-g+e\), ranging from \(pq+1-g\) in the relative interior to \(pq\) at each cube vertex.

An explicit parametrization of every center is as follows. Choose arbitrary \(\delta_k\in[-1,1]\), \(1\le k<g\). Use zero-based row and column indices. Put \(U_0=V_0=0\). For \(1\le i<p\), write \(iq=p h+r\) with \(0\le r<p\), and define
\[
U_i-U_{i-1}=\begin{cases}2h,&r>0,\\2h-1+\delta_{i/(p/g)},&r=0.\end{cases}
\]
For \(1\le j<q\), write \(jp=q h+r\) with \(0\le r<q\), and define
\[
V_j-V_{j-1}=\begin{cases}2h,&r>0,\\2h-1-\delta_{j/(q/g)},&r=0.\end{cases}
\]
The quotients indexing \(\delta\) in the divisible cases are integers in \(\{1,\ldots,g-1\}\). Then
\[
\boxed{X_{ij}=r_{p,q}\bigl[\alpha+U_i+V_j-2ij\bigr],\qquad0\le i<p,\ 0\le j<q.}
\]
Every choice of the parameters gives a center, and every center occurs in this way, uniquely.

## Assumptions and scope
The matrices have nonnegative entries and sum one; all adjacent inequalities use the displayed Monge sign. The metric is the Frobenius norm **restricted to the sum-one affine hyperplane**, not a coordinatewise norm or an affine-transformed metric. Rows and columns may have different cardinalities; both are at least two. All inequalities above are facets of this polytope by Erickson and Kretschmann (Theorem 5.3), which is a cited prior result. The previously published square-matrix inball theorem is also prior work, not a new special case.

## Proof
**1. Reduction to a nonnegative mixed-difference problem.** Write \(H=\{Y:\sum Y_{ij}=0\}\), the tangent space of the normalization hyperplane, and \(\Delta_{ij}Y=Y_{i,j+1}+Y_{i+1,j}-Y_{ij}-Y_{i+1,j+1}\). A coordinate normal projected onto \(H\) has norm \(\alpha\); a mixed-difference normal belongs to \(H\) and has norm \(2\). Therefore an intrinsic closed radius-\(r\) ball centered at \(X\) lies in the polytope precisely when \(X_{ij}\ge\alpha r\) and \(\Delta_{ij}X\ge2r\). For positive \(r\), define \(Z_{ij}=X_{ij}/r-\alpha\). Its conditions become \(Z_{ij}\ge0\), \(\Delta_{ij}Z\ge2\), and
\[
\sum_{i,j}Z_{ij}=r^{-1}-pq\alpha.
\]
Thus it suffices to find the minimum \(T\) of \(\sum Z_{ij}\) for nonnegative arrays with all mixed differences at least two, and classify its minimizers.

**2. A positive dual certificate from coupled grid intervals.** For \(1\le a<p\), \(1\le b<q\), set
\[
\lambda_{ab}=\min(qa,pb)-ab>0,
\]
and set \(\lambda_{ab}=0\) if either index is on an outer boundary (zero or its full dimension). Define nonnegative cell masses
\[
\pi_{ij}=pq\left|\left[\frac{i}{p},\frac{i+1}{p}\right]\cap\left[\frac{j}{q},\frac{j+1}{q}\right]\right|,
\]
where the vertical bars denote ordinary one-dimensional interval length. One checks by taking the two mixed differences of \(pq\min(a/p,b/q)-ab\) that
\[
1-\bigl(\lambda_{i+1,j}+\lambda_{i,j+1}-\lambda_{i+1,j+1}-\lambda_{i,j}\bigr)=\pi_{ij}.
\]
Summation by parts therefore gives the **exact gap identity**
\[
\boxed{\sum_{i,j}Z_{ij}-2\sum_{a,b}\lambda_{ab}=\sum_{i,j}\pi_{ij}Z_{ij}+\sum_{a,b}\lambda_{ab}(\Delta_{a-1,b-1}Z-2)\ge0.}
\]
Since every \(\lambda_{ab}>0\), equality holds exactly when **all mixed differences equal two** and \(Z_{ij}=0\) for every pair of grid intervals with positive overlap. This identifies equality without relying on a numerical optimizer.

**3. Evaluation of the dual mass.** Let \(T\) be uniform on \([0,1]\) and let \(I=\lfloor pT\rfloor\), \(J=\lfloor qT\rfloor\). Expressing each integer floor as a sum of its threshold indicators yields
\[
\sum_{a=1}^{p-1}\sum_{b=1}^{q-1}\lambda_{ab}=pq\operatorname{Cov}(I,J).
\]
Indeed the covariance of the two threshold indicators at \(a/p\), \(b/q\) is \(\min(a/p,b/q)-ab/(pq)\). To evaluate the covariance exactly, write \(s(t)=\{t\}-1/2\), the centered sawtooth, and note
\[
I=pT-\{pT\},\quad J=qT-\{qT\},\quad \operatorname{Cov}(T,s(kT))=\frac1{12k}.
\]
The last equality follows by integrating separately over the \(k\) equal subintervals. The periodic sawtooth has the classical \(L^2\) Fourier expansion \(s(t)=-\sum_{n\ne0}e^{2\pi\mathrm i nt}/(2\pi\mathrm i n)\). Orthogonality shows that the only terms surviving in \(\int_0^1s(pt)s(qt)\,dt\) correspond to \(n=q h/g\), \(m=-p h/g\), and hence
\[
\int_0^1s(pt)s(qt)\,dt=\frac{g^2}{12pq}.
\]
Using \(\operatorname{Var}(T)=1/12\) gives
\[
\operatorname{Cov}(I,J)=\frac{p^2q^2-p^2-q^2+g^2}{12pq},\quad
2\sum\lambda_{ab}=\frac{p^2q^2-p^2-q^2+g^2}{6}=:T_{p,q}.
\]
Therefore \(\sum Z\ge T_{p,q}\), and step 1 implies \(r\le[pq\alpha+T_{p,q}]^{-1}\).

**4. Constructing every equality array.** Put \(Z_{ij}=U_i+V_j-2ij\) with the increments in the Finding. Every adjacent mixed difference is exactly two. Let the \(p\) row intervals and \(q\) column intervals be ordered along \([0,1]\). Starting with \(Z_{00}=0\), traverse their grid endpoints. When a row boundary lies strictly inside column interval \(j\), the prescribed increment of \(U\) is \(2j\), so zero propagates between the two overlapping rows. A column-only boundary similarly has increment \(2i\), and at a common boundary \(i/p=j/q\), the two increments sum to \(2(i+j-1)\), so zero propagates from cell \((i-1,j-1)\) to cell \((i,j)\). Consequently **every cell with positive interval overlap has \(Z_{ij}=0\)**.

Nonnegativity follows from the discrete monotonicity \(Z_{i,j}-Z_{i-1,j}=(U_i-U_{i-1})-2j\): for a fixed column interval \([j/q,(j+1)/q]\), this difference is nonpositive before the row boundary enters the interval, zero while it lies strictly inside, and nonnegative after it leaves. The cells with overlapping intervals are therefore global minima of their columns and have value zero. At the shared interval boundaries, the two neighboring off-overlap entries are exactly \(1-\delta_k\) and \(1+\delta_k\), so nonnegativity holds for \(\delta_k\in[-1,1]\). The gap identity then forces \(\sum Z=T_{p,q}\). Hence every displayed matrix \(X\) is sum-one and is a maximum-ball center.

Conversely, any maximizing center must attain equality in the dual gap. The condition \(\Delta Z=2\) implies the general representation \(Z_{ij}=U_i+V_j-2ij\), normalized by \(U_0=V_0=0\); the overlap cells include \((0,0)\) and enforce its zero. Propagating the forced overlap zeros through the endpoint sweep determines each non-common row or column increment uniquely. A common boundary leaves exactly one free scalar \(\delta_k\), appearing with opposite signs in its row and column increments. The adjacent off-overlap entries are \(1-\delta_k\) and \(1+\delta_k\), forcing \(-1\le\delta_k\le1\). There are precisely \(g-1\) interior common boundaries, at \(k/g\). This reconstructs *all* the displayed arrays, and individual \(\delta_k\) are recovered from the corresponding adjacent entry, so the parameter map is injective. The center locus is therefore an affine \((g-1)\)-cube.

**5. Exact contact counts.** The union of both interval subdivisions has \((p-1)+(q-1)-(g-1)\) distinct interior division points, hence exactly \(p+q-g\) overlapping cells. These and only these cells have zero slack whenever every \(|\delta_k|<1\). Strictness away from overlap follows from the preceding row-difference monotonicity; outside an overlap the cumulative step has a strictly positive difference except when immediately neighboring a common boundary with an endpoint parameter. At that boundary, \(\delta_k=1\) adds precisely the zero cell \((i-1,j)\), while \(\delta_k=-1\) adds precisely \((i,j-1)\), with \(i=kp/g\), \(j=kq/g\). They are distinct from overlap cells and from one another. Thus the coordinate-facet contact count is \(p+q-g+e\). Since every one of the \((p-1)(q-1)\) Monge inequalities is an equality at its distance-\(r\) support plane, the total is \((p-1)(q-1)+p+q-g+e=pq+1-g+e\).

## Verification
The standalone standard-library script `verify_rectangular_monge.py` reconstructs the dual coefficients, exact projected overlap masses, all mixed-difference equations, normalization, nonnegative center arrays, and every predicted zero cell using rational arithmetic. Its reproducible command is `python3 verify_rectangular_monge.py`. It passed 1,806 exact parameter profiles for every pair \(2\le p,q\le12\), including all ternary grid parameters when \(g\le6\). In separate development checks, all 169 pairs \(2\le p,q\le14\) passed exact normalization tests and 5,839 exact parameter-grid contact tests passed; independent finite linear-programming checks matched selected cases. Such finite checks do not establish the universal theorem: the dual identity, covariance computation and equality analysis do.

## Relationship to prior work
Erickson and Kretschmann, *The structure and normalized volume of Monge polytopes* (arXiv:2311.07522, first publicly posted 2023-11-13), define precisely this nonnegative sum-one Monge family for arbitrary rectangular dimensions and prove the complete facet system (Theorem 5.3). Their theorem is the cited input for all-facets assertions, **not** a prior inradius classification.

The published note *An affine \((n-1)\)-cube of Euclidean incenters for square Monge polytopes* (identifier `b3dc6b94166a`) already determines the inradius, complete cube of centers, and facet contacts when \(p=q=n\). That entire square specialization is **known** and is not asserted to be novel here. The contribution is the rectangular formula with its nontrivial \(\gcd(p,q)\) term, the coprimality uniqueness theorem, the full unequal-grid cube parameterization, and the sharp contact counts. The square theorem by itself cannot determine nonsquare behavior: its minimum-assignment argument exploits a square identity permutation, whereas the proof above constructs a new unequal-grid coupling and exact dual certificate.

Erickson and Jones, *A lattice path model for the volume of the Monge polytope* (arXiv:2609.09508, 2026), investigate the same family through Stanley decompositions, normalized volumes and Ehrhart series, not its intrinsic Euclidean inballs. No broader covering inradius theorem was located in the inspected sources; that is an evidence-based comparison, not proof of global priority.

## Limitations
The result concerns Euclidean inballs and their centers for the **normalized** nonnegative nonsymmetric Monge polytope, with \(p,q\ge2\) and the inherited Frobenius metric. It does not determine John ellipsoids, enclosing balls, other metrics, weighted coordinate inequalities, or generalized Monge cones. Complete bibliographic novelty cannot be proved from an incomplete literature index; especially results under optimal-transport or grid-convexity terminology may contain equivalent claims. Independent mathematical validation has not been performed.

## References
- W. Q. Erickson and J. Kretschmann, *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522, v1 posted 2023-11-13, especially Theorem 5.3. https://arxiv.org/abs/2311.07522
- *An affine \((n-1)\)-cube of Euclidean incenters for square Monge polytopes*, published scientific result (2026), identifier `b3dc6b94166a`.
- W. Q. Erickson and N. B. Jones, *A lattice path model for the volume of the Monge polytope*, arXiv:2609.09508, posted 2026-09-08. https://arxiv.org/abs/2609.09508
- R. Rudolf and G. J. Woeginger, *The cone of Monge matrices: Extremal rays and applications*, Math. Methods Oper. Res. 42 (1995), 161–168, DOI:10.1007/BF01415751. (Background on the Monge cone, not a radius theorem.)
