# A five-vertex positivity boundary and one-band sign recovery for TR-BDF2 heat flow on complete multipartite graphs

## Finding
Let \(G=K_{p_1,\ldots,p_r}\) be any unweighted complete multipartite graph with \(r\ge2\) nonempty parts and \(N=\sum_{j=1}^{r}p_j\ge2\). Let \(L\) be its combinatorial Laplacian. Apply the unmodified, L-stable TR-BDF2 method with \(\gamma=2-\sqrt2\) to \(u'=-Lu\), and denote its completed one-step matrix by \(T(h)\), for real \(h\ge0\). With
\[
 a=1-1/\sqrt2,\qquad b=\sqrt2-1,\qquad
 F(z)=\frac{1-bz}{(1+az)^2},\qquad T(h)=F(hL),
\]
the following hold.

1. Every off-diagonal entry of \(T(h)\) is **strictly positive** for every \(h>0\), regardless of the number and sizes of the parts.
2. \(T(h)\) is entrywise nonnegative for every \(h\ge0\) **if and only if \(N\le5\)**. When \(N\le5\), all entries are strictly positive for every \(h>0\).
3. If \(N\ge6\), then **each vertex** has precisely one bounded open interval of positive timesteps on which its self-transition is strictly negative. The endpoints are two distinct positive roots of an explicit quartic below. That entry is strictly positive at every other positive timestep except at the two zero endpoints. All vertices belonging to the same part have identical intervals. The intervals of different parts need not be asserted to coincide.

The cutoff is independent of the multipartite profile, even though the two zeros in each part depend on its size.

## Assumptions and scope
The graph is simple, undirected, unweighted, and complete multipartite, with at least two parts. \(L=D-A\) is the unnormalized positive-semidefinite combinatorial Laplacian. The result concerns the *completed endpoint map*, not internal TR-BDF2 stages, and one timestep, not a claim about intermediate approximations. The timestep is real and nonnegative. All roots below refer to exact real roots, not a floating-point root count.

For a part of size \(p\) put \(q=N-p\ge1\). Define
\[
 P_{N,p}(h)=p(1+aNh)^2(1+aqh)^2
 +q(1-bNh)(1+aqh)^2
 +N(p-1)(1-bqh)(1+aNh)^2.
\]
For \(N\ge6\), the endpoints \(h_-^{(N,p)}<h_+^{(N,p)}\) are exactly the two positive roots of \(P_{N,p}\). Its coefficients belong to \(\mathbb Q(\sqrt2)\). No generic radical expression for the quartic roots is needed.

## Proof
**1. Stability function and spectral projectors.** The L-stable TR-BDF2 parameter is \(\gamma=2-\sqrt2\). The two substeps give the scalar decay stability function \(F\) above, with \(2a+b=1\). For a complete multipartite graph, let \(J\) denote the all-ones matrix and \(J_p\) the within-part all-ones matrix extended by zero. There are three types of Laplacian eigenspaces: constants (eigenvalue \(0\)); block-constant vectors orthogonal to constants (eigenvalue \(N\)); and the sum-zero space inside a part of size \(p\) (eigenvalue \(q=N-p\)). Thus
\[
 T(h)=\frac JN+F(Nh)\left(\sum_j\frac{J_{p_j}}{p_j}-\frac JN\right)
 +\sum_jF((N-p_j)h)\left(I_{p_j}-\frac{J_{p_j}}{p_j}\right).
\]
Here \(I_{p_j}\) denotes the identity on the indicated part, extended by zero. In particular, for distinct vertices in different parts,
\[
 T_{uv}(h)=\frac{1-F(Nh)}N;
\]
for two distinct vertices in the same part of size \(p\),
\[
 T_{uv}(h)=\frac{1-F(Nh)}N+\frac{F(Nh)-F(qh)}p;
\]
and for a vertex in that part,
\[
 d_{N,p}(h):=T_{uu}(h)=\frac1N+\left(\frac1p-\frac1N\right)F(Nh)
 +\left(1-\frac1p\right)F(qh).
\]

**2. Off-diagonal positivity.** A direct calculation yields
\[
 \frac{1-F(z)}z=\frac{1+a^2z}{(1+az)^2},\qquad z>0.
\]
Its derivative is \(a(a-2-a^2z)/(1+az)^3<0\). Consequently, for \(z>0\) and \(0<\beta<1\),
\[
 F(\beta z)<(1-\beta)+\beta F(z).
\]
Take \(\beta=q/N\) and \(z=Nh\). Multiplying the same-part expression by \(p\) gives \(pT_{uv}=1-\beta+\beta F(z)-F(\beta z)>0\). Across parts, \(1-F(Nh)>0\), proving strict positivity of every off-diagonal entry.

**3. Small dimensions.** Differentiation gives
\[
 F'(z)=\frac{abz-1}{(1+az)^3}.
\]
Its minimum on \([0,\infty)\) is
\[
 z_*=\frac1{ab}=4+3\sqrt2,\qquad m_*=F(z_*)=\frac{1-\sqrt2}{2}.
\]
Since every spectral projection has nonnegative diagonal, every \(N\)-vertex connected undirected graph obeys
\[
 [F(hL)]_{uu}\ge\frac{1+(N-1)m_*}{N}.
\]
For \(2\le N\le5\), this is strictly positive, because \(1+4m_*=3-2\sqrt2>0\). Together with Step 2, this proves unconditional entrywise positivity for all multipartite graphs of those orders.

**4. A negative self-transition in each part from six vertices onward.** Fix \(p\in\{1,\ldots,N-1\}\), put \(q=N-p\), and choose the natural comparison timestep \(h_0=z_*/q\). Algebraic simplification gives the exact identity
\[
 d_{N,p}(h_0)=-\frac{H(p,q)}{2(1+\sqrt2)(p+\sqrt2q)^2},\qquad
 H(p,q)=(p+\sqrt2q)^2-(3+2\sqrt2)(p+2q).
\]
If \(N\ge7\), writing \(x=p/N\) yields
\[
 \frac{(p+\sqrt2q)^2}{p+2q}
 =N\frac{(\sqrt2-(\sqrt2-1)x)^2}{2-x}
 \ge N(12\sqrt2-16)>3+2\sqrt2.
\]
The minimum over \(0\le x\le1\) occurs at \(x=2-\sqrt2\). The final strict inequality holds for \(N\ge7\) since \(82\sqrt2-115>0\). Therefore \(H(p,q)>0\), giving \(d_{N,p}(h_0)<0\).

For \(N=6\), direct factorization with \(q=6-p\) gives
\[
 H(p,6-p)=(3-2\sqrt2)(p-3)(p-4).
\]
For integer \(p\in\{1,2,5\}\), the value at \(h_0\) is strictly negative. For \(p=3\) or \(4\), it is zero, but
\[
 d'_{6,p}(h_0)=\frac qp F'(6h_0)>0,
\]
because \(F'(z_*)=0\), \(6h_0>z_*\), and \(F'(z)>0\) above its minimum. Hence sufficiently small positive \(\varepsilon\) satisfies \(d_{6,p}(h_0-\varepsilon)<0\). This completes the existence proof for every part and every \(N\ge6\).

**5. Exactly one bounded negative interval.** Multiplication of \(pN d_{N,p}(h)\) by the strictly positive denominator \((1+aNh)^2(1+aqh)^2\) gives \(P_{N,p}(h)\). The quartic has positive constant and leading coefficients,
\[
 [h^0]P_{N,p}=pN>0,\quad [h^4]P_{N,p}=pa^4N^2q^2>0,
\]
positive linear coefficient
\[
 [h^1]P_{N,p}=pN\big(2a(N+q)-q\big)>0
\]
(the last inequality follows from \(4a-1=3-2\sqrt2>0\)), and negative cubic coefficient
\[
 [h^3]P_{N,p}=a^2Nq\{2pa(N+q)-b[q^2+N^2(p-1)]\}<0
\]
whenever \(N\ge6\). To verify the last inequality, use \(a=b/\sqrt2\): for \(p\ge2\), its bracket divided by \(b\) is less than \(N(2\sqrt2p-N(p-1))<0\) because \(N\ge6\) and \(6(p-1)>2\sqrt2p\); for \(p=1\), it is \(\sqrt2(1+2q)-q^2<0\) as \(q\ge5\). The quadratic coefficient may have either sign, but these four established signs force exactly two sign changes in the ordered quartic coefficient sequence. Descartes' rule of signs therefore allows at most two positive roots counting multiplicity. Step 4 supplies a negative value, while \(d_{N,p}(0)=1\) and \(\lim_{h\to\infty}d_{N,p}(h)=1/N>0\). Hence there are at least two distinct positive roots; exactly two exist, both simple. Their open interval is precisely the set of negative diagonal values.

## Verification
The accompanying standalone `VERIFY.py` runs using the Python standard library. It performs exact arithmetic in \(\mathbb Q(\sqrt2)\) with rational coefficients, checks the minimizing argument, the negative-witness identity and quartic coefficients across multiple orders and part sizes, and independently constructs the graph Laplacian and rational method by exact matrix inversion for explicit multipartite graphs and rational timesteps. The replay output is given in `VERIFICATION.md`. None of the finite checks substitutes for the inequalities and Descartes argument proving the all-order theorem.

## Relationship to prior work
Bonaventura and Della Rocca (first posted October 14, 2015) derive the TR-BDF2 method, its L-stable parameter, stability function, finite radius of absolute monotonicity, and positivity-preserving hybrid variants. The present result instead examines the unmodified completed method on the discrete graph heat equation and obtains a sharp graph-order classification, with strict off-diagonal positivity and exactly one recoverable negative diagonal band per part. The source's general SSP-radius condition does not imply these all-timestep, graph-specific results; conversely, this theorem does not extend to arbitrary nonlinear positive systems or arbitrary graph families. General finite-dimensional positivity and absolute-monotonicity results do not alone resolve the threshold or root count here.

## Limitations
This is a result about unweighted complete multipartite graphs, not arbitrary positively weighted graphs, directed generators, nonlinear equations, time-varying graphs, positivity of internal stages, or a universal nonnegative step for all \(N\ge6\). For each part size, the negative interval may differ; the theorem does not claim simultaneous negativity of all diagonals at a common timestep. Exact zero endpoints are specified implicitly as positive roots of the stated quartic. The originality comparison is based on inspected accessible literature and known result summaries; older or unindexed equivalences may exist. Independent external validation has not been performed.

## References
- L. Bonaventura and A. Della Rocca, *Monotonicity, positivity and strong stability of the TR-BDF2 method and of its SSP extensions*, arXiv:1510.04303, first submitted October 14, 2015. https://arxiv.org/abs/1510.04303
