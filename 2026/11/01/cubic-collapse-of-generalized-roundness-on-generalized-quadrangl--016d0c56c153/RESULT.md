# Cubic collapse of generalized roundness on generalized-quadrangle incidence graphs

## Finding
Let \(\mathcal Q\) be any existing finite generalized quadrangle of order \((q,q)\), where \(q\ge2\), and let \(G\) be its point–line incidence graph with unit-edge shortest-path metric \(d\). Put \(v=(q+1)(q^2+1)\), so \(G\) has \(2v\) vertices, and define
\[
F_q(p)=q^3 4^p-q^2(q+1)3^p+q(q+1)2^p-(q+1).
\]
There is a unique zero \(\wp_q\) of \(F_q\) in \(\bigl(0,\log_2(1+1/q)\bigr)\). The supremal generalized roundness, equivalently the supremal exponent of negative type of \((V(G),d)\), is exactly \(\wp_q\): the metric has strict \(p\)-negative type for \(0<p<\wp_q\), has non-strict \(\wp_q\)-negative type, and fails \(p\)-negative type for every \(p>\wp_q\).

At \(p=\wp_q\), the complete nontrivial equality coefficient space in the zero-sum negative-type inequality is one-dimensional, spanned by the vector taking value \(+1\) on every point and \(-1\) on every line. Consequently, the smallest Euclidean dimension for an isometric embedding of the snowflaked metric \(d^{p/2}\) is
\[
\dim_{\min}(d^{p/2})=
\begin{cases}
2v-1,&0<p<\wp_q,\\
2v-2,&p=\wp_q.
\end{cases}
\]
As \(q\to\infty\) through the orders for which such quadrangles exist,
\[
\wp_q=\frac{1}{q^3\log(4/3)}+
\frac{\log(3/2)}{q^4\log^2(4/3)}+O(q^{-5}).
\]
In particular, the critical exponent is of cubic rather than linear order in the inverse order of the geometry. For \(q=2,3,5\), numerical values are approximately \(0.345784723476\), \(0.137565128845\), and \(0.032764105998\), respectively.

## Assumptions and scope
A finite generalized quadrangle of order \((q,q)\) has \(v\) points and \(v\) lines, with exactly \(q+1\) incidences at each point and each line; two points lie on at most one common line, and a nonincident point–line pair has a unique length-three incidence path. This gives a connected bipartite incidence graph of diameter four and girth eight. Its point–point and line–line distances are two when collinear/concurrent and four otherwise; cross-type distances are one for incidence and three otherwise. We assume \(q\) is an integer at least two for which this geometry exists. No existence statement for every integer order is intended.

For \(p>0\), strict \(p\)-negative type means \(\sum_{i,j}c_i c_j d(z_i,z_j)^p<0\) for every nonzero real coefficient vector satisfying \(\sum_i c_i=0\), where \(z_i\) range over all distinct graph vertices. Non-strict negative type allows equality. The Euclidean embedding dimension refers to an isometric embedding of the vertex metric \(d^{p/2}\) into a real Hilbert space of the stated finite dimension.

## Proof
**1. Incidence spectra.** Index points and lines separately, and let \(B\) be the \(v\)-by-\(v\) binary point–line incidence matrix. Let \(J\) be the all-ones matrix and \(I\) the identity. The point-collinearity and line-concurrency adjacency matrices are
\[
A=BB^{\mathsf T}-(q+1)I,\qquad
A'=B^{\mathsf T}B-(q+1)I.
\]
Both are strongly regular, with \(v=(q+1)(q^2+1)\), valency \(k=q(q+1)\), and intersection parameters \(\lambda=q-1\), \(\mu=q+1\). Counting common neighbors of two collinear/noncollinear points proves this directly from the generalized-quadrangle axiom; the dual statement applies to lines. Thus \(A\) and \(A'\) have eigenvalues \(k\), \(q-1\), and \(-(q+1)\), with respective multiplicities
\[
1,\quad f=\frac{q(q+1)^2}{2},\quad g=\frac{q(q^2+1)}2.
\]
This follows, for example, by solving the quadratic strongly regular adjacency identity \(A^2=kI+(q-1)A+(q+1)(J-I-A)\), together with the trace and dimension equations. It implies that the nonzero singular values of \(B\) are \(q+1\) on constants and \(\sqrt{2q}\) with multiplicity \(f\). Its remaining singular value is zero with multiplicity \(g\).

**2. Powered-distance decomposition.** The four possible nonzero graph distances identified above give the following *entire* \(2v\)-by-\(2v\) powered-distance matrix:
\[
D_p=\begin{pmatrix}
2^p A+4^p(J-I-A)&B+3^p(J-B)\\
B^{\mathsf T}+3^p(J-B^{\mathsf T})&2^p A'+4^p(J-I-A')
\end{pmatrix}.
\]
On the hyperplane perpendicular to the all-ones vector, use singular-vector bases for \(B\) and their corresponding eigenspaces for \(A,A'\). This is an orthogonal invariant decomposition. The balanced constant vector \((\mathbf1,-\mathbf1)\) is an eigenvector with eigenvalue
\[
F_q(p)=k2^p+q^3 4^p-(q+1)-q^2(q+1)3^p.
\]
The \(f\)-dimensional left/right singular sectors produce, each with multiplicity \(f\),
\[
R_\pm(p)=(q-1)2^p-q4^p\ \pm\ (3^p-1)\sqrt{2q}.
\]
The two \(g\)-dimensional null singular sectors both have eigenvalue
\[
S(p)=q4^p-(q+1)2^p,
\]
with total multiplicity \(2g\). The dimensions sum to \(1+2f+2g=2v-1\), so these exhaust the zero-sum spectrum. There are no unexamined eigenvalue sectors.

**3. All competing sectors are strictly negative before the stated bound.** Set \(p_0=\log_2(1+1/q)\). Then \(S(p)<0\) for \(0\le p<p_0\) and \(S(p)>0\) for \(p>p_0\). For \(0\le p\le p_0\), put \(u=2^p-1\in[0,1/q]\) and \(\theta=\log_2 3\in(1,8/5)\). Convexity of \((1+u)^\theta\) gives a bound on the chord slopes over \([0,1/2]\):
\[
3^p-1=(1+u)^\theta-1<2u\quad\text{when }u>0.
\]
Indeed \((3/2)^\theta<2\), as follows from \(\theta<8/5\), \(3^8<2^{13}\), and the monotonicity of the power function. Meanwhile
\[
q4^p-(q-1)2^p=(1+u)(1+qu)\ge1+qu\ge2qu\ge2u\sqrt{2q}.
\]
The last two inequalities use \(qu\le1\) and \(\sqrt{2q}\le q\) for \(q\ge2\). Hence \(R_+(p)<0\) when \(p>0\) and \(p\le p_0\), and at \(p=0\) both \(R_\pm(0)=-1\). The \(R_-\) branch is smaller still. Thus the constant point-versus-line eigenvalue \(F_q\) must cross first, if it crosses before \(p_0\).

**4. Unique crossing.** At \(p=0\), \(F_q(0)=-1\). At \(p_0\), \(2^{p_0}=1+1/q\), and direct simplification gives
\[
F_q(p_0)=q(q+1)\bigl(q+2-q3^{p_0}\bigr)>0,
\]
using \(3^{p_0}<1+2/q\). To prove uniqueness globally, define
\[
a(p)=\log4\,4^p-\log3\,3^p>0,\qquad
b(p)=\log3\,3^p-\log2\,2^p>0.
\]
Then \(F_q'(p)=q^3 a(p)-q^2 b(p)+q\log2\,2^p\). Since \(q\ge2\), it suffices to check \(2a(p)-b(p)>0\). Dividing that expression by \(2^p\) gives
\[
H(p)=2\log4\,2^p-3\log3\,(3/2)^p+\log2.
\]
Here \(H(0)=\log(32/27)>0\) and
\[
H'(p)=2\log4\log2\,2^p-3\log3\log(3/2)\,(3/2)^p>0,
\]
for \(p\ge0\), since \(2\log4\log2>3\log3\log(3/2)\) (an elementary numerical-free log bound, e.g. \(\log2>2/3\), \(\log3<11/10\), \(\log(3/2)<5/12\), suffices). Thus \(F_q\) increases strictly on \([0,\infty)\) and has exactly one zero \(\wp_q\in(0,p_0)\).

**5. Negative type, uniqueness and ranks.** For \(0<p<\wp_q\), all eigenvalues of \(D_p\) on the zero-sum hyperplane are strictly negative. At \(p=\wp_q\), exactly the one-dimensional point-minus-line sector vanishes; all others remain strictly negative. For \(\wp_q<p\le p_0\), the eigenvalue \(F_q(p)>0\), while for \(p>p_0\), \(S(p)>0\). This proves the complete strict/endpoint/failure classification, including every larger exponent. The centered Schoenberg Gram matrix \(-\tfrac12 HD_pH\), with \(H=I-\mathbf1\mathbf1^{\mathsf T}/(2v)\), has rank \(2v-1\) strictly below the endpoint and rank \(2v-2\) at the endpoint. By the finite-metric Hilbert embedding criterion, these ranks are precisely the minimal Euclidean dimensions of the corresponding snowflake embeddings. The equality vector and its uniqueness follow from the same spectral nullity.

**6. Cubic asymptotic.** With \(A_0=\log(4/3)\), \(B_0=\log(3/2)\),
\[
F_q'(0)=q^3A_0-q^2B_0+q\log2,
\]
while \(F_q''(p)=O(q^3)\) uniformly on \(0\le p\le p_0\). The mean value theorem and the strict positivity of \(F_q'\) show \(\wp_q=O(q^{-3})\); Taylor's theorem then gives \(1=F_q'(0)\wp_q+O(q^3\wp_q^2)\). Expanding the reciprocal of \(F_q'(0)\) proves
\[
\wp_q=\frac1{A_0q^3}+\frac{B_0}{A_0^2q^4}+O(q^{-5}).
\]
This asymptotic is along existing orders only.

## Verification
The accompanying standalone `verify_gq_negative_type.py` generates the symplectic generalized quadrangles \(W(q)\) for prime orders \(q=2,3,5\) from totally isotropic projective lines, checks the defining incidence and strongly regular identities with integer arithmetic, and independently computes all ordered vertex-pair shortest paths. It reconstructs full powered-distance kernels and checks their spectral branches and centered negative-type signs on both sides of the predicted threshold. The recorded successful checks cover 900, 6400, and 97344 ordered vertex-pair distances, respectively. These are finite corroborations; the proof above applies to every existing finite generalized quadrangle of equal order. Reproduce using Python 3 with NumPy and SciPy: `python verify_gq_negative_type.py`.

## Relationship to prior work
The Schoenberg criterion and the general theory of negative type supply the standard Hilbert-embedding equivalence. Weston [1] gives general finite-metric lower bounds, Sánchez [2] a general finite-metric criterion and formulas for certain other graph metrics, and Vanhove [3] surveys the strongly regular incidence geometry used in Step 1. DeVille [4] supplies general techniques for distance-function matrix spectra of distance-regular graphs. None of the specific results checked in these sources evaluates the point–line incidence metric of every generalized quadrangle of order \((q,q)\) to this critical exponent, identifies its one-dimensional equality kernel, and deduces the sharp critical Hilbert rank. The strong-regularity spectrum is standard prior input, not claimed as new. A broader unexamined theorem or unindexed equivalent calculation remains a priority risk.

## Limitations
The result assumes finite equal-order generalized quadrangles, positive powered distances, the unweighted graph shortest-path metric, and real Hilbert embeddings. No assertion is made for unequal-order quadrangles, nonexistence of particular orders, arbitrary weighted incidence graphs, continuum realizations, or quantitative stability of the negative-type inequality. Only prime-order classical examples are computationally checked; the all-orders statement is proved algebraically.

## References
[1] A. Weston, *Optimal lower bounds on the maximal p-negative type of finite metric spaces*, arXiv:0807.2705v1 (2008-07-17), https://arxiv.org/abs/0807.2705.

[2] S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1 (2011-08-02), https://arxiv.org/abs/1108.0451.

[3] F. Vanhove, *Incidence geometry from an algebraic graph theory point of view*, doctoral thesis (2011), https://biblio.ugent.be/publication/1209078/file/4335521.pdf.

[4] L. DeVille, *The generalized distance spectrum of a graph and applications*, arXiv:1708.02294v1 (2017), https://arxiv.org/abs/1708.02294.
