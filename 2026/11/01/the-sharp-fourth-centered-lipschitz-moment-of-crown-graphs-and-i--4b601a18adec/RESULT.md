# The sharp fourth centered Lipschitz moment of crown graphs and its twelve-pair transition

## Finding
For every integer \(n\ge3\), let \(C_n\) be the crown graph with vertices \(A_1,\ldots,A_n,B_1,\ldots,B_n\), edges \(A_iB_j\) precisely when \(i\ne j\), and unit-edge shortest-path metric. Write \(N=2n\), \(\bar f=N^{-1}\sum_{v\in C_n}f(v)\), and define the fourth centered Lipschitz moment
\[
\mathcal M_4(C_n)=\max_{\operatorname{Lip}(f)\le1}\frac1N\sum_{v\in C_n}|f(v)-\bar f|^4.
\]
Then
\[
\boxed{\mathcal M_4(C_n)=\max\left\{\frac1{16}+\frac5n,\ \frac12-\mathbf1_{n\,\mathrm{odd}}\left(\frac1{4n^2}+\frac3{16n^4}\right)\right\}.}
\]
The first entry is strictly larger for \(3\le n\le11\); the second is strictly larger for every \(n\ge12\). There is no integer tie between branches.

For \(3\le n\le11\), every maximizer, modulo an additive constant, changing the overall sign, swapping the bipartition classes, and simultaneously permuting the pair indices, has the four-level pattern \(f(A_1)=0\), \(f(B_1)=3\), \(f(A_j)=2\), \(f(B_j)=1\) for \(j\ne1\). For \(n\ge12\), every maximizer under the same equivalences takes constant value \(1\) on one bipartition class and values \(0\) and \(2\) on the other, with multiplicities \(\lfloor n/2\rfloor\) and \(\lceil n/2\rceil\). In particular the sharp fourth moment changes optimizer type at twelve matched pairs.

## Assumptions and scope
The vertex measure is uniform counting measure normalized by \(1/(2n)\); the output is the *fourth power* of the norm of the centered map from edge-Lipschitz functions modulo constants to the uniform \(L^4\) space. The Lipschitz constraint is \(|f(A_i)-f(B_j)|\le1\) for every \(i\ne j\). The missing pairs \(A_iB_i\) have graph distance \(3\), while same-class distinct vertices have distance \(2\). Functions are real. This is a sharp finite-dimensional inequality, not a statement about random walks or fourth moments of a random graph model.

## Proof
**1. Vertices are integral and suffice.** Fix an arbitrary vertex value to zero. The admissible functions form a compact convex polytope, because \(C_n\) is connected. The centered fourth-moment functional is strictly convex on this affine section: the map \(f\mapsto(f(v)-\bar f)_v\) is injective after quotienting constants, and the fourth power is strictly convex on the real line. Therefore every maximizer is a vertex. At a vertex, the subgraph of edges on which \(|f(u)-f(v)|=1\) must be connected: otherwise a proper connected component can be shifted slightly without violating any constraint, writing the candidate as the midpoint of two other admissible functions. Connectivity implies that after one value is set to zero, every vertex value is an integer (sum of signed unit increments along the tight-edge spanning tree). We may translate so that \(\min_i f(A_i)=0\). Since every two \(A\)-vertices have graph distance two, \(f(A_i)\in\{0,1,2\}\). Because \(n\ge3\), for a fixed \(A\)-assignment, the permitted interval for \(b_i=f(B_i)\) is exactly
\[
I_i=\left[\max_{j\ne i} f(A_j)-1,\ \min_{j\ne i} f(A_j)+1\right].
\]
The independent coordinate intervals are compatible with the full edge constraints; at every maximizer, strict convexity in each coordinate forces \(b_i\) to one of the two endpoints. Thus the following finite classification exhausts *every* maximizer, not merely one optimizer.

**2. The basic three-level inequality.** Suppose, up to translation, a candidate has \(k\) nonzero vertex values, all \(+1\) or \(-1\), with signed count difference \(d\). On \(N=2n\) vertices, direct expansion gives
\[
F_N(k,d)=\frac{k}{N}+\frac{d^2}{N^2}\left(-4+\frac{6k}{N}\right)-\frac{3d^4}{N^4}.
\]
Whenever \(k\le n\), the quadratic coefficient is at most \(-1\), so \(F_N(k,d)\le k/N\). If \(k=n\), \(d\) has the parity of \(n\), and the maximum occurs precisely at \(|d|=0\) for even \(n\), or \(|d|=1\) for odd \(n\). Its value is
\[
U_n=\frac12-\mathbf1_{n\,\mathrm{odd}}\left(\frac1{4n^2}+\frac3{16n^4}\right).
\]
For \(k\le n-1\), one has \(F_N(k,d)\le(n-1)/(2n)<U_n\), since the latter is the fourth moment of the balanced \(n\)-nonzero pattern. Thus all such three-level assignments are bounded by \(U_n\), with equality only in the balanced case and \(k=n\).

**3. Endpoint classification by the \(A\)-levels.** Set \(c_a=\#\{i:f(A_i)=a\}\), for \(a\in\{0,1,2\}\), so \(c_0\ge1\). Each case follows directly from the intervals \(I_i\).

* If \(c_0=n\), then every \(b_i\) equals \(-1\) or \(+1\). This is exactly the \(k=n\) instance of Step 2, hence bounded by \(U_n\) with the stated balanced equality case.

* If \(c_2=0\) and both \(c_0,c_1\ge2\), all \(b_i\) lie in \(\{0,1\}\). For any binary random variable of bias \(p\), the centered fourth moment is \(q-3q^2\), with \(q=p(1-p)\in[0,1/4]\), so it is at most \(1/12<U_n\).

* If \(c_2=0\) and exactly one of \(c_0,c_1\) is one, all but one \(b_i\) belong to \(\{0,1\}\). The special \(b_i\) is either an ordinary binary value or an outlier at distance one beyond that binary range. By changing sign and translating, an outlier assignment has values in \(\{0,1,2\}\), exactly one value \(2\), and mean \(\mu\in[\tfrac12+\tfrac1N,1]\). Put \(\varepsilon=1/N\). Its centered fourth moment is exactly
\[
(1-\mu)\mu^4+\mu(1-\mu)^4+\varepsilon\bigl[\mu^4-2(1-\mu)^4+(2-\mu)^4\bigr].
\]
The first term is at most \(1/12\), while the bracket equals \(2+12(1-\mu)^2\le5\). Therefore this case is bounded by \(1/12+5/(2n)\). For \(3\le n\le11\), this is strictly below \(T_n=1/16+5/n\). For \(n\ge12\), it is at most \(7/24<U_n\). Binary assignments are already covered by the preceding inequality.

* If \(c_1=0\) and \(c_0,c_2\ge2\), every \(b_i\) equals \(1\), giving a three-level assignment with \(k=n\) after subtracting \(1\), hence at most \(U_n\). If one of \(c_0,c_2\) is one, there is precisely one exceptional \(B\)-coordinate with two available endpoints. Choosing the endpoint nearer \(1\) again yields the \(k=n\) pattern bounded by \(U_n\). Choosing the farther endpoint yields (up to reflection) exactly the four-level multiset \(\{0^1,1^{n-1},2^{n-1},3^1\}\). Its mean is \(3/2\) and its centered fourth moment is
\[
T_n=\frac{2(3/2)^4+(2n-2)(1/2)^4}{2n}=\frac1{16}+\frac5n.
\]
The four-level pattern is feasible: its only distance-three pair is the deleted matched edge with values \(0\) and \(3\).

* Finally, suppose \(c_0,c_1,c_2>0\). When \(c_0,c_2\ge2\), every \(b_i=1\), yielding \(k\le n\) nonzero signs after subtracting \(1\). If exactly one extreme level occurs once and the other occurs at least twice, only its corresponding \(b_i\) can differ from \(1\): subtracting \(1\) gives \(k\le n\) unit signs. When \(k=n\), the signed excess satisfies \(|d|=n-2\), so Step 2 still gives \(F_N(k,d)\le U_n\). If both extreme levels occur once, at most four entries differ from \(1\) and Step 2 gives a fourth moment at most \(4/(2n)=2/n\). For \(n=3\) this is strictly below \(T_3\); for \(4\le n\le11\) it is at most \(1/2<T_n\); for \(n\ge12\) it is below \(U_n\). All possibilities are exhausted.

The two explicit constructions from the statement attain \(T_n\) and \(U_n\), respectively, proving the maximum formula. All inequalities away from the relevant cases are strict, so the endpoint classification also proves the claimed rigidity of the maximizing patterns.

**4. The integer transition.** If \(n\) is even, \(U_n=1/2\), and \(T_n>U_n\) exactly for \(n<80/7\); among even integers this means \(n\le10\). If \(n\) is odd and \(n\le11\), then \(T_n\ge T_{11}=91/176>1/2\ge U_n\). If \(n\) is odd and \(n\ge13\), then \(T_n\le T_{13}<1/2-1/(4\cdot13^2)-3/(16\cdot13^4)\le U_n\). Consequently the switch is exactly at \(n=12\), without an integer tie.

## Verification
Run `python3 verify_crown_fourth.py` using Python's standard library. It independently enumerates all orbit-reduced integral endpoint assignments for \(3\le n\le36\), directly enumerates labelled endpoint assignments for \(3\le n\le6\), checks both exact attaining witnesses and phase inequalities through \(n=69\), and replays the algebraic three-level fourth-moment identity using rational arithmetic. All finite tests agree with the displayed formula. These tests do not replace the general proof above.

## Relationship to prior work
Alon, Boppana, and Spencer introduced graph spread (the *second* centered Lipschitz moment), as described in Addario-Berry, Janson, and McDiarmid's 2009 preprint. Yancey's analysis addresses structural properties of maximal-variance Lipschitz functions. A separately published sharp Euclidean-inradius and contact-facet result for crown-graph symmetric edge polytopes already determines the *second* centered moment of these exact graphs via polar duality. The second-moment calculation and its contact sets are prior work and are not claimed here. They do not imply the fourth-centered-moment maximum: the fourth objective differs on non-contacting vertices of the Lipschitz polytope, and the threshold here is twelve rather than eight matched pairs. Literature and mathematical-record searches did not identify an exact fourth-moment classification for crown graphs; that absence is not a proof of uniqueness in the literature.

## Limitations
Only real one-Lipschitz functions, the uniform vertex measure, unit-length crown-graph edges, and the fourth centered absolute moment are treated. The result does not provide an all-exponent formula, a general weighted crown classification, or a new statement about the second centered moment. Independent review and exhaustive coverage of unindexed literature remain outstanding.

## References
1. N. Alon, R. Boppana, J. Spencer, *An asymptotic isoperimetric inequality*, Geometric and Functional Analysis 8 (1998). Original graph-spread framework.
2. L. Addario-Berry, S. Janson, C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156, first posted 2009-02-06. Full open-access HTML: https://arxiv.org/html/0902.1156v2 .
3. M. Yancey, *Probabilistic and Geometrical Applications to Graph Theory*, arXiv:1705.09725. https://arxiv.org/abs/1705.09725 .
4. *A sharp Euclidean inradius and tangent-facet transition for crown-graph symmetric edge polytopes*, published mathematical research record (2026), identifier `2026/10/11/SCOPE-a-sharp-euclidean-inradius-and-tangent-facet-transition-for-crow--2cd222e2d952`. Comparison concerns the second-moment polar-dual invariant, not the fourth-moment theorem.
