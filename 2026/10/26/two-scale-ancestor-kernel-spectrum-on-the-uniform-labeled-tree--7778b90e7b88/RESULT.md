# Two-scale ancestor-kernel spectrum on the uniform labeled tree

## Finding
For each integer \(n\ge4\), take a uniformly random labeled spanning tree \(T\) of the complete graph \(K_n\). Fix two distinct vertices \(r,b\); put \(U=V\setminus\{r,b\}\). Define \(H(x)=\Pr(b\in[r,x]_T)\) for \(x\in U\) and, for distinct \(x,y\in U\), define \(J(x,y)=\Pr(r,x,y\text{ occupy three different components of }T\setminus\{b\})\), with \(J(x,x)=0\). The quadratic ancestor matrix is \(K=HH^{\mathsf T}-J\).

Define the rational number
\[
h_n=\frac1{n-2}\sum_{k=1}^{n-1}(k-1)(k+1)\frac{(n-2)_{k-1}}{n^k},
\qquad j_n=\frac{1-3h_n}{n-3},
\]
where \((m)_a=m(m-1)\cdots(m-a+1)\), including \((m)_0=1\). Then the entire real spectrum of \(K\) is
\[
\boxed{\lambda_\perp=j_n\quad\text{(multiplicity }n-3\text{)},\qquad
\lambda_\parallel=(n-2)h_n^2+3h_n-1\quad\text{(multiplicity }1\text{)}.}
\]
The first eigenspace consists of coordinate vectors summing to zero; the second is the constant-vector line. Moreover,
\[
\boxed{\lim_{n\to\infty}n\lambda_\perp=1,\qquad
\lim_{n\to\infty}\lambda_\parallel=\frac\pi2-1,\qquad
\lim_{n\to\infty}\frac{\lambda_\parallel}{n\lambda_\perp}=\frac\pi2-1.}
\]
Thus the quadratic ancestor inequality has an order-one collective mode and order-\(1/n\) transverse modes in its simplest transitive mean-field model. For all sufficiently large \(n\), both eigenvalues are strictly positive, with condition number asymptotic to \((\pi/2-1)n\).

## Assumptions and scope
All edges of \(K_n\) have equal positive conductance, the spanning tree is uniform, and the marked vertices are distinct and deterministic. The probability space has \(n^{n-2}\) equally likely trees. The deletion \(T\setminus\{b\}\) removes vertex \(b\) and its incident edges. The matrix is indexed only by the \(n-2\) vertices outside \(\{r,b\}\). The same formulas hold independently of the names of these vertices. No statement is made here about unequal conductances or multi-vertex deletion sets.

## Proof
**Path count.** Let \(L=d_T(r,x)\) for fixed distinct \(r,x\). A specified simple path with \(k\) edges between them contains \(k+1\) marked vertices. Contracting its edges turns the marked block into one vertex with \(k+1\) choices for every incident external edge. The weighted Cayley-tree enumeration gives exactly \((k+1)n^{n-k-2}\) spanning trees containing that path. There are \((n-2)_{k-1}\) ordered choices for its internal vertices, and a tree admits exactly one \(r\)-to-\(x\) path. Hence, for every integer \(1\le k\le n-1\),
\[
\Pr(L=k)=\frac{(k+1)(n-2)_{k-1}}{n^k}.
\]
Conditional on \(L=k\), the \(k-1\) internal vertices are exchangeable among the \(n-2\) possible labels. Consequently \(H(x)=\mathbb E(L-1)/(n-2)=h_n\), for every \(x\in U\).

**Three-point median.** Every tree has a unique median \(m_T(r,x,y)\), the common intersection point of the three pairwise paths joining distinct vertices \(r,x,y\). Removing a vertex \(b\) distinct from \(r,x,y\) separates these three vertices into different components exactly when \(m_T(r,x,y)=b\). By label symmetry, the probabilities of the median being each of \(r,x,y\) are equal; each is \(h_n\), since, for example, \(m_T(r,x,y)=r\) exactly when \(r\) is internal to the \(x\)-to-\(y\) path. Each of the remaining \(n-3\) vertices has the same median probability \(j_n\). Summing the disjoint median cases gives \(3h_n+(n-3)j_n=1\). Thus \(J(x,y)=j_n\) off diagonal.

**Spectrum.** With \(m=n-2\), the preceding identities yield \(K=j_n I_m+(h_n^2-j_n)\mathbf1_m\mathbf1_m^{\mathsf T}\). Every vector orthogonal to \(\mathbf1_m\) therefore has eigenvalue \(j_n\), while \(\mathbf1_m\) has eigenvalue \(j_n+m(h_n^2-j_n)=m h_n^2+3h_n-1\), as claimed.

**Mean-field limit.** Write \(p_n(k)=\Pr(L=k)\). For \(k\ge1\),
\[
p_n(k)=\frac{k+1}{n}\prod_{s=2}^{k}\left(1-\frac{s}{n}\right),
\qquad
0\le p_n(k)\le\frac{k+1}{n}\exp\left(-\frac{k(k+1)-2}{2n}\right).
\]
For \(k/\sqrt n\to t\in(0,\infty)\), the product tends to \(e^{-t^2/2}\). The displayed Gaussian domination, together with a Riemann-sum argument and truncation of the tails, gives
\[
\frac{\mathbb E L}{\sqrt n}\longrightarrow\int_0^\infty t^2e^{-t^2/2}\,dt=\sqrt{\frac\pi2}.
\]
Hence \(\sqrt n h_n\to\sqrt{\pi/2}\), and \(n j_n=n(1-3h_n)/(n-3)\to1\). Substituting into the exact eigenvalue identities yields all asserted limits. Positivity of \(j_n\) holds for every \(n\ge4\): the star centered at \(b\) is one witness of the median event. The limit \(\lambda_\parallel\to\pi/2-1>0\) proves strict positivity of the second eigenvalue for all sufficiently large \(n\). This is sufficient for the stated condition-number asymptotic; no all-size strict-positivity theorem is needed.

## Verification
Run `python3 verify.py` with Python 3 standard library. The checker independently enumerates all \(n^{n-2}\) Prüfer sequences for \(n=4,5,6,7\). It recovers tree paths and three-component events from adjacency lists, independently counts path lengths, and compares all exact rational probabilities against the formulas. Exhaustive counts are finite spot checks, not a proof of the all-\(n\) assertion. The path-contraction and symmetry arguments above supply that proof.

For example, at \(n=4\), \(h_4=5/16\), \(j_4=1/16\), and \(\lambda_\parallel=17/128\). At \(n=5\), \(h_5=37/125\), \(j_5=7/125\), and \(\lambda_\parallel=2357/15625\).

## Relationship to prior work
Gefei Cai, *A quadratic ancestor inequality for spanning trees*, arXiv:2610.22180v1 (2026-10-15), introduced the general quadratic ancestor matrix and proved its positive semidefiniteness for arbitrary positive edge weights. The present calculation specializes to uniform complete graphs but answers a different quantitative question: every finite-size eigenvalue and the asymptotic contrast between the collective and transverse directions. Cai's inspected main theorem, proof, and listed applications do not give these exact Cayley-tree matrix eigenvalues. The weighted Cayley enumeration and mean-field distance scale are standard ingredients; neither is asserted new independently.

## Limitations
The formula is restricted to a single deleted vertex in an equal-conductance complete graph. The general ancestor positive-semidefiniteness theorem remains the source for the inequality on arbitrary weighted graphs. The calculation does not prove strict positivity of the collective eigenvalue at every finite order, although exact checks establish it for \(n=4,5,6,7\), and the asymptotic proof establishes it eventually. Searches and full-text inspection reduce but cannot eliminate the possibility of an equivalent spectral formula in older random-tree literature. No independent audit has been performed.

## References
1. Gefei Cai, *A quadratic ancestor inequality for spanning trees*, arXiv:2610.22180v1, first public 2026-10-15, https://arxiv.org/abs/2610.22180 ; full text https://arxiv.org/html/2610.22180v1.
2. Cayley's labeled-tree enumeration and the Prüfer correspondence (classical facts; counting argument included above).
3. *Exact negative regression between endpoint degree and distance in a uniform Cayley tree*, publicly searchable mathematical result (2026-10-04); a related but distinct endpoint-degree/distance question.
