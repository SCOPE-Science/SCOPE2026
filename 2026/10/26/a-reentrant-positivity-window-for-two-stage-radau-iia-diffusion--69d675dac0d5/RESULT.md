# A reentrant positivity window for two-stage Radau IIA diffusion on square rook graphs

## Finding
For every integer \(q\ge2\), let \(G_q=K_q\square K_q\) be the unweighted square rook graph, let \(L_q\) be its combinatorial Laplacian, and let \(T_q(h)\) be the completed two-stage, third-order Radau IIA update for the heat equation \(u'=-L_q u\):
\[
T_q(h)=(6I-2hL_q)(6I+4hL_q+h^2L_q^2)^{-1},\qquad h\ge0.
\]
Set \(x=qh\) and
\[
D_q(x)=2x^4+(18-4q-2q^2)x^3+(18+18q-5q^2)x^2+36qx+18q^2.
\]
If \(q\in\{2,3\}\), then \(T_q(h)\) is entrywise nonnegative for every \(h\ge0\). For each integer \(q\ge4\), \(D_q\) has exactly two distinct positive zeros \(a_q<b_q\), and the **complete positivity set** is the disconnected set
\[
\boxed{\{h\ge0:T_q(h)\ge0\text{ entrywise}\}=[0,a_q/q]\,\cup\,[b_q/q,\infty).}
\]
Every timestep in the open gap \((a_q/q,b_q/q)\) has a strictly negative diagonal transition at every vertex, even though \(T_q(h)\) is symmetric, has all row and column sums equal to one, and satisfies \(\|T_q(h)\|_{2\to2}=1\) for every \(h\ge0\). In particular, on \(K_4\square K_4\), at \(h=1\), every diagonal entry equals \(-4/323\). Furthermore, as \(q\to\infty\),
\[
a_q\longrightarrow\frac32,\qquad \frac{b_q}{q^2}\longrightarrow1,
\]
so the first positivity-loss time is asymptotic to \(3/(2q)\) and positivity returns only at a timestep asymptotic to \(q\).

## Assumptions and scope
Vertices are ordered pairs from \(\{1,\ldots,q\}^2\); distinct vertices are adjacent exactly when they share one coordinate. Every edge has unit conductance and \(L_q=\deg-A\), with degrees \(2(q-1)\). The assertion concerns entrywise positivity of the **completed one-step matrix**, not positivity of internal Radau stages or preservation of nonlinear constraints. Nonnegativity is entrywise and includes equality at the two boundaries. In the display above, \(\infty\) indicates a semi-infinite interval of finite nonnegative steps, not an actual timestep.

## Proof
Let \(P=J_q/q\) and \(Q=I_q-P\). Because \(L(K_q)=qQ\),
\[
L_q=q(Q\otimes I+I\otimes Q).
\]
Write \(r(z)=(6-2z)/(z^2+4z+6)\), the Radau IIA scalar decay stability function. The four orthogonal tensor projectors yield
\[
T_q(h)=P\otimes P+r(x)(Q\otimes P+P\otimes Q)+r(2x)Q\otimes Q.
\]
Set \(E(x)=(x^2+4x+6)(2x^2+4x+3)\), which is strictly positive for \(x\ge0\), and
\[
F_q(x)=2x^3+(18-2q)x^2+(18+9q)x+18q.
\]
The diagonal entries, adjacent off-diagonal entries, and nonadjacent off-diagonal entries are, respectively,
\[
\frac{D_q(x)}{q^2E(x)},\qquad
\frac{xF_q(x)}{q^2E(x)},\qquad
\frac{2x^2(x^2+9x+9)}{q^2E(x)}.
\]
These identities follow by substituting \(P_{ii}=1/q\), \(Q_{ii}=(q-1)/q\), \(P_{ij}=1/q\), and \(Q_{ij}=-1/q\) for \(i\ne j\). In particular all nonadjacent entries are strictly positive for \(h>0\).

For \(q=2\), every coefficient of \(D_q(x)\) is strictly positive. For \(q=3\), the identity
\[
D_3(x)=2x^2(x-3)^2+9x^2+108x+162
\]
gives strict diagonal positivity. For \(q\ge4\), the coefficient sequence of \(D_q\) in descending degree has at most two sign changes: its leading coefficient is positive and its cubic coefficient is negative; the quadratic coefficient may have either sign, but the linear and constant coefficients are positive. Descartes' rule therefore bounds the number of positive zeros, with multiplicity, by two. Yet
\[
D_q(0)=18q^2>0,\qquad
D_q(q)=-q^2(2q^3+7q^2-36q-72)<0,
\]
where the last inequality holds already at \(q=4\) and the cubic factor is strictly increasing for integers \(q\ge4\). Since \(D_q(x)\to+\infty\) as \(x\to+\infty\), there are exactly two distinct positive roots; \(D_q\) is negative precisely between them.

It remains to show that adjacent entries cannot introduce any additional negative interval. Use
\[
F_q(x)=2x(x^2+9x+9)+q(2x+3)(6-x).
\]
For \(0<x\le6\), this is positive. For \(x\ge q\) and \(x>6\), replacing \(q\) in its negative term by \(x\) gives the positive lower bound
\[
F_q(x)\ge x\bigl[2(x^2+9x+9)-(2x+3)(x-6)\bigr]=x(27x+36)>0.
\]
Thus \(F_q(x)<0\) can occur only for \(6<x<q\). Such an interval is empty if \(q\le6\). If \(q>6\), then \(D_q(6)=-594(q^2-12)<0\) and \(D_q(q)<0\); because \(D_q\) has exactly two positive zeros, every \(x\in(6,q)\) lies inside its negative interval. Consequently \(D_q(x)\ge0\) implies \(F_q(x)>0\) for \(x>0\), and the diagonal sign alone determines entrywise nonnegativity. At \(h=0\), \(T_q(0)=I\). This proves the exact disconnected interval.

For spectral stability, \(|r(z)|<1\) for every \(z>0\): if \(0<z\le3\), the denominator exceeds \(6-2z\) by \(z^2+6z\); if \(z>3\), it exceeds \(2z-6\) by \(z^2+2z+12\). The constant-mode eigenvalue of \(T_q(h)\) is always one, so its Euclidean operator norm is exactly one. The projectors also show symmetry and mass preservation.

For the limiting locations, on bounded \(x\)-intervals,
\[
\lim_{q\to\infty}\frac{D_q(x)}{q^2}=-(2x-3)(x^2+4x+6).
\]
The positive-to-negative sign change at \(3/2\), together with uniqueness of the smaller positive root, implies \(a_q\to3/2\). On the scale \(x=q^2y\) for fixed \(y>0\),
\[
\lim_{q\to\infty}\frac{D_q(q^2y)}{q^8}=2y^3(y-1).
\]
The sign switch across \(y=1\) and uniqueness of the larger root imply \(b_q/q^2\to1\). Finally substituting \(q=4\), \(x=4\) into the diagonal formula gives \(-4/323\).

## Verification
Run `python verify.py` with SymPy installed. The program checks the three orbit-transition rational identities, the diagonal factor and sign certificates, the limiting polynomial, and direct exact matrix rational-function calculations on \(K_q\square K_q\) for \(q=2,3,4,5,6\) at specified positive rational steps, verifying \(5,879\) matrix entries and all row sums. It checks the exact \(q=4\) negative diagonal witness and a finite range of the universal sign inequality. These checks corroborate the algebra; the statements for unbounded \(q\) and all real \(h\) are proved above analytically.

## Relationship to prior work
The classical third-order two-stage Radau IIA tableau and stability function are recorded by Ketcheson's Numipedia entry. Gottlieb, Shu and Tadmor (2001), including their Section 6, study strong stability and implicit Runge–Kutta barriers in general; these are method-wide conditions, not this graph-family endpoint classification. Blanes, Iserles and Macnamara (2021/2022) study graph-Laplacian positivity and alternative positivity-preserving algorithms, not the present explicit sign geometry for the completed Radau IIA rook-graph step. Earlier analyses of Radau IIA on paths, cycles, hypercubes and balanced complete multipartite graphs involve different graph Laplacian spectra; their conclusions do not determine the full sign phase on rook graphs. The present phenomenon is *reentrant entrywise nonnegativity*: the one-step operator is nonnegative for small and very large steps but not intermediate ones.

## Limitations
The theorem is for unweighted square rook graphs and the completed **two-stage Radau IIA** method only. It does not assert that intermediate RK stages are nonnegative, nor any property for general rectangular rook graphs, nonlinear diffusions or other rational RK approximants. Broad numerical stability is not equivalent to positivity. The historical-literature comparison does not establish absolute novelty against every possible specialized source; independent external mathematical validation has not been performed.

## References
1. S. Gottlieb, C.-W. Shu and E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review **43** (2001), 89–112. DOI: 10.1137/S003614450036757X. Author-hosted full text: https://www.math.umd.edu/~tadmor/pub/linear-stability/Gottlieb-Shu-Tadmor.SIREV-01.pdf. Publicly released online 2001-02-02, according to the first-page footnote.
2. D. I. Ketcheson, *Numipedia: Radau IIA2*, https://ketch.github.io/numipedia/methods/RadauIIA2.html (method tableau and scalar stability function; date unspecified).
3. S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for ordinary differential equations*, arXiv:2102.08242, version 1 dated 2021-02-16, https://arxiv.org/html/2102.08242v2 (full-text discussion of graph Laplacians and positivity, including Sections 1–3 and 6).
4. E. W. Weisstein, *Rook Graph*, MathWorld, https://mathworld.wolfram.com/RookGraph.html (standard Cartesian-product graph terminology).
