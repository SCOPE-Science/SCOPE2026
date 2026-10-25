# Sharp RK4 positivity equals spectral stability on complete multipartite diffusion networks

## Finding

Let \(G=K_{n_1,\ldots,n_r}\) be the unweighted complete multipartite graph, with \(r\ge2\) and arbitrary positive integer part sizes \(n_1,\ldots,n_r\). Write \(N=\sum_{i=1}^r n_i\), and let \(L\) be the symmetric combinatorial graph Laplacian. A classical fourth-order explicit Runge–Kutta step for \(u'=-Lu\) has endpoint transition matrix
\[
K(h)=I-hL+\frac{h^2L^2}{2}-\frac{h^3L^3}{6}+\frac{h^4L^4}{24},\qquad h\ge0.
\]
Let \(\rho=2.78529356340528\ldots\) be the unique positive zero of
\[
\phi(z)=24-12z+4z^2-z^3.
\]
For **every** such partition and **every** real step \(h\ge0\), the following are equivalent:
\[
\boxed{K(h)\text{ is entrywise nonnegative}}
\quad\Longleftrightarrow\quad
\boxed{\|K(h)\|_{2\to2}\le1}
\quad\Longleftrightarrow\quad
\boxed{h\le\rho/N}.
\]
Here the operator norm is the real Euclidean matrix norm. Moreover, every same-part off-diagonal entry and every diagonal entry is strictly positive for \(h>0\). All cross-part entries are equal; they are strictly positive when \(0<h<\rho/N\), zero at \(h=\rho/N\), and strictly negative when \(h>\rho/N\). Thus the endpoint matrix is a genuine stochastic diffusion transition up to the sharp threshold and becomes block diagonal at equality, despite the underlying connected diffusion network.

If \(\Delta=N-\min_i n_i\) is the maximum degree, the forward-Euler endpoint positivity threshold is \(1/\Delta\). In this family the exact RK4-to-Euler threshold ratio is
\[
\frac{\rho\Delta}{N}=\rho\left(1-\frac{\min_i n_i}{N}\right)\ge\frac\rho2>1.
\]
The threshold is uniform over all part-size distributions with the same total number of vertices, including unequal bipartite graphs, complete graphs, stars, and arbitrary numbers of nontrivial parts.

## Assumptions and scope

The graph is finite, simple, undirected, complete multipartite, unweighted, and has at least two nonempty vertex parts. The Laplacian is \(L=D-A\), with one unit conductance for each edge between different parts and no within-part edges. The numerical method is the classical four-stage/fourth-order **completed endpoint step** on the autonomous linear ODE, not a claim of positivity for all internal Runge–Kutta stages or for nonlinear systems. No assertion is made for other graphs, unequal edge conductances, or other time integrators. Initial-state nonnegativity is preserved for every initial state exactly when the matrix is entrywise nonnegative.

## Proof

**Spectral decomposition.** Let \(E_i\) be the orthogonal projector onto vectors constant on part \(i\) and zero elsewhere, let \(E=\sum_iE_i\), let \(P_0={\bf1}{\bf1}^{\mathsf T}/N\), and let \(Q_i=I_i-E_i\), with \(I_i\) the coordinate projector onto part \(i\). These projectors are mutually orthogonal except that \(P_0\le E\); the orthogonal decomposition of the identity is
\[
I=P_0+(E-P_0)+\sum_i Q_i.
\]
Direct evaluation of \(L\) shows eigenvalue zero on \(P_0\), eigenvalue \(N\) on \(E-P_0\), and eigenvalue \(N-n_i\) on \(Q_i\). The eigenvalue \(N\) is present because \(r\ge2\). Writing
\[
R(z)=1+z+z^2/2+z^3/6+z^4/24,\qquad R_i=R(-(N-n_i)h),\quad R_N=R(-Nh),
\]
we obtain the exact projector formula
\[
K(h)=P_0+R_N(E-P_0)+\sum_iR_iQ_i
     =R_NE+(1-R_N)P_0+\sum_iR_iQ_i.
\]
In particular, for any two vertices belonging to **different** parts,
\[
K_{ab}(h)=\frac{1-R_N}{N}=
\frac h{24}\bigl(24-12Nh+4N^2h^2-N^3h^3\bigr)=\frac h{24}\phi(Nh).
\]

**Noncritical entries.** Take distinct vertices \(a,b\) in the same part of size \(p\), and write \(q=N-p>0\). The formula gives
\[
\begin{aligned}
K_{ab}(h)
&=\frac{p+qR(-Nh)-NR(-qh)}{pN}\\
&=\frac{h^2q}{24}
\left[12-4(p+2q)h+(p^2+3pq+3q^2)h^2\right].
\end{aligned}
\]
The quadratic bracket has positive leading coefficient and discriminant
\[
16(p+2q)^2-48(p^2+3pq+3q^2)=-16(2p^2+5pq+5q^2)<0,
\]
so \(K_{ab}(h)>0\) for all \(h>0\). A singleton part contains no such pair. Every diagonal entry equals the corresponding same-part off-diagonal expression plus \(R(-qh)\). Strict positivity of this last factor follows from the identity
\[
R(-x)=\left(1-\frac x2\right)^2+
\frac{x^2}{24}\left[(x-2)^2+2\right]>0
\qquad(x\ge0).
\]
At \(h=0\), \(K(0)=I\). Thus the **only possible negative entries**, for any \(h\ge0\), are cross-part entries.

**Exact sign and no reentry.** The derivative is
\[
\phi'(z)=-\left[3\left(z-\frac43\right)^2+\frac{20}{3}\right]<0.
\]
As \(\phi(0)=24\) and \(\phi(z)\to-\infty\), there is exactly one positive root \(\rho\), between \(2\) and \(3\). Consequently the cross-part entries have precisely the claimed three sign regimes, with no positivity reentry. The equalities at the boundary follow by substitution, and the row sums of \(K\) always equal one because \(L{\bf1}=0\).

**Spectral stability.** On the nonnegative real axis \(R(-x)>0\). Moreover,
\[
R(-x)-1=-\frac{x}{24}\phi(x),
\]
so \(0<R(-x)\le1\) exactly for \(0\le x\le\rho\). All Laplacian eigenvalues belong to \([0,N]\), and \(N\) itself is an eigenvalue. Therefore \(\|K(h)\|_{2\to2}\le1\) holds precisely for \(0\le h\le\rho/N\). This coincides exactly with entrywise nonnegativity, completing the proof.

**Forward-Euler comparison.** Euler's matrix is \(I-hL\); its off-diagonals are nonnegative and the largest degree is \(\Delta=N-\min_i n_i\), so its sharp threshold is \(1/\Delta\). As \(\min_i n_i\le N/2\) and \(\rho>2\), the claimed strict improvement follows.

## Verification

The attached standalone `verify.py` directly reconstructs Laplacian matrices for all unordered integer partitions of \(2\le N\le10\) having at least two parts, computes each RK4 matrix using exact rational arithmetic at steps \(h=(1/2)/N,1/N,2/N,3/N\), and compares every entry with the symbolic projector expressions. It additionally verifies the crucial symbolic polynomial identities, the discriminant, the sum-of-squares identity, the strict derivative identity, row sums, and a rational enclosure of \(\rho\). Its successful output is:

`VERIFY_OK symbolic spectral identities, exact positivity certificates, 512 complete multipartite direct rational RK4 matrices, 16048 vertex-pair checks`

These finite checks are reproducibility aids, **not** proofs of the unlimited quantifiers; those follow from the formulas above. No interval-arithmetic package or numerical eigenvalue solver is needed.

## Relationship to prior work

Gottlieb, Shu and Tadmor (2001), especially Sections 2–3, establish the general strong-stability-preserving (SSP) framework and a forward-Euler-based CFL criterion for linear systems. Higueras (2005) develops general absolute-monotonicity and Runge–Kutta monotonicity theory. Hadjimichael, Macdonald, Ketcheson and Verner (2013) examine SSP Runge–Kutta method design and effective order. Those results provide the numerical-method background but do not state the **complete-multipartite graph-specific equivalence** between endpoint nonnegativity and spectral stability or the universal exact \(\rho/N\) threshold independent of the part sizes. The general Euler-based SSP restriction by itself cannot give the larger exact threshold proved here.

The spectral RK4 stability endpoint \(\rho\) is classical; it is **not** claimed as a new number. The contribution is the positivity equivalence, exact entrywise mechanism, and universal graph-family classification. Indeed, the equivalence is not automatic for arbitrary graphs: on the four-vertex path, the end-to-end RK4 entry is \(h^3(1/6-h/4)<0\) at \(h=3/4\), whereas the spectral condition remains satisfied because \((3/4)(2+\sqrt2)<\rho\).

Blanes, Iserles and Macnamara (2022) discuss graph-Laplacian positivity and general order barriers, motivating why bounded, graph-specific positivity regions must not be confused with unconditional positivity of a general-purpose method. The accessible abstract supports that distinction; its complete 2022 text was not relied on as a negative-coverage certificate. The complete text of Higueras (2005) was not available in this review; this is an originality risk, not evidence of noncoverage.

## Limitations

The theorem is restricted to the autonomous symmetric *unweighted* complete-multipartite Laplacian and the completed classical RK4 endpoint. It does not assert internal-stage positivity, universal SSP, positivity for heterogeneous spoke/edge weights, or an extension to all symmetric graph Laplacians. The number \(\rho\) is the already known negative-real-axis RK4 absolute-stability endpoint. A complete historical novelty determination would require checking any specialized graph-family positivity results not located in the literature search; an inaccessible full text of Higueras (2005) was not assessed beyond its bibliographic abstract. No independent external validation has been performed.

## References

1. S. Gottlieb, C.-W. Shu and E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review 43 (2001), 89–112, doi:10.1137/S003614450036757X. First electronically public 2001-02-02. Authorized open repository: https://drum.lib.umd.edu/bitstreams/faa96f40-0fbb-4af0-84a3-5e3b80c908df/download .
2. I. Higueras, *Representations of Runge–Kutta Methods and Strong Stability Preserving Methods*, SIAM Journal on Numerical Analysis 43 (2005), 924–948, doi:10.1137/S0036142903427068. Publisher page: https://epubs.siam.org/doi/10.1137/S0036142903427068 .
3. Y. Hadjimichael, C. B. Macdonald, D. I. Ketcheson and J. H. Verner, *Strong Stability Preserving Explicit Runge–Kutta Methods of Maximal Effective Order*, SIAM Journal on Numerical Analysis 51 (2013), 2149–2165, arXiv:1207.2902v1 (first public 2012-07-12), doi:10.1137/120884201. Author-hosted text: https://www.davidketcheson.info/assets/papers/2013_effective_order_ssp.pdf .
4. S. Blanes, A. Iserles and S. Macnamara, *Positivity-Preserving Methods for Ordinary Differential Equations*, ESAIM M2AN 56 (2022), 1843–1870, doi:10.1051/m2an/2022042. Abstract and bibliography: https://www.numdam.org/articles/10.1051/m2an/2022042/ .
