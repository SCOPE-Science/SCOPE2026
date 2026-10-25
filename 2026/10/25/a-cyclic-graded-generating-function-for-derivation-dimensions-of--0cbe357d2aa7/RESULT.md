# A cyclic-graded generating function for derivation dimensions of finite-field evolution algebras

## Finding
Let \(q=p^e\) be a prime power and let \(\mathcal E_A\) be the marked \(n\)-dimensional evolution algebra over \(\mathbb F_q\), with fixed ordered natural basis \(e_1,\ldots,e_n\), given by
\[
e_i e_j=0\quad(i\ne j),\qquad e_i^2=\sum_{j=1}^n A_{ij}e_j,
\]
where \(A\in\operatorname{GL}_n(\mathbb F_q)\). Put \(\delta(A)=\dim_{\mathbb F_q}\operatorname{Der}(\mathcal E_A)\). The matrices are counted individually, not modulo algebra isomorphism or a change of natural basis.

Write \(g_n(q)=|\operatorname{GL}_n(\mathbb F_q)|=\prod_{j=0}^{n-1}(q^n-q^j)\), with \(g_0(q)=1\), and introduce the formal exponential series
\[
G_q(x)=\sum_{n\ge0}\frac{g_n(q)}{n!}x^n.
\]
If \(p\) is odd, let \(r=\operatorname{ord}_{\mathbb F_p^\times}(2)\), and define the formal power series
\[
F_{q,r}(y)=\sum_{m\ge0}\frac{g_m(q)^r}{(m!)^r}y^m.
\]
**The complete derivation-dimension distribution** is
\[
\boxed{\sum_{n\ge0}\frac{x^n}{n!}\sum_{A\in\operatorname{GL}_n(\mathbb F_q)}u^{\delta(A)}
=G_q(x)F_{q,r}(x^r)^{(u-1)/r}.}
\]
The power on the right is defined formally by the exponential and logarithm of a series with constant term one. In characteristic two, \(\delta(A)=0\) for every invertible \(A\), and the corresponding distribution series is just \(G_q(x)\).

Moreover, in odd characteristic the sharp attainable range is
\[
\boxed{0\le\delta(A)\le\lfloor n/r\rfloor.}
\]
Every integer in this range occurs. In particular, no nonzero derivations exist below dimension \(r\), while the first nonzero stratum has size
\[
\boxed{\#\{A\in\operatorname{GL}_r(\mathbb F_q):\delta(A)=1\}
=(r-1)!(q-1)^r.}
\]
More generally, for \(r\le n<2r\), the number of \(A\) with \(\delta(A)=1\) is exactly
\[
\boxed{\binom nr (r-1)!(q-1)^r g_{n-r}(q),}
\]
and all remaining invertible matrices have derivation dimension zero. At \(p=q=3\), the complete counts by derivation dimension for \(n=4\) are \(24{,}253{,}200\), \(7{,}872\), and \(48\) for dimensions \(0,1,2\), respectively.

## Assumptions and scope
All dimensions are over the same finite field \(\mathbb F_q\), and the algebra is **perfect**, meaning \(\mathcal E_A^2=\mathcal E_A\), equivalently \(A\) is invertible. The graph of \(A\) has an arrow \(i\to j\) precisely when \(A_{ij}\ne0\); connectedness refers to its underlying undirected support graph. All generating functions are formal over \(\mathbb Q[u]\), not analytically convergent generating functions. The coefficient of \(x^n u^d/n!\) counts marked structure matrices with derivation dimension \(d\). No assertion is made about counting isomorphism classes.

## Proof
**Step 1 (derivations are diagonal).** Write \(D(e_i)=\sum_k d_{ki}e_k\). Since \(e_ie_j=0\) for distinct \(i,j\), the Leibniz identity gives
\[
0=D(e_ie_j)=d_{ji}e_j^2+d_{ij}e_i^2.
\]
The vectors \(e_i^2\) form a basis because \(A\) is invertible. Therefore \(d_{ij}=d_{ji}=0\), and every derivation is diagonal, say \(D(e_i)=\lambda_i e_i\). The remaining Leibniz equations are exactly
\[
\lambda_j=2\lambda_i\qquad\text{for every arrow }i\to j.
\]
Conversely, every solution of these equations determines a derivation. When \(p=2\), these relations and the absence of zero columns force every \(\lambda_j=0\), proving the characteristic-two assertion.

**Step 2 (balanced components and cyclic colorings).** Let \(p\) be odd, and let \(r\) be the multiplicative order of \(2\) in \(\mathbb F_p^\times\). In a weakly connected support component, either every solution \(\lambda_i\) is zero or a nonzero solution is determined by the value at one vertex and therefore has dimension one. Nonzero solutions exist precisely when one can assign a residue \(c(i)\in\mathbb Z/r\mathbb Z\) to every vertex such that
\[
c(j)\equiv c(i)+1\pmod r\qquad(i\to j).
\]
Indeed, choosing a nonzero root value makes each \(\lambda_i\) a power of \(2\) times that root value, and conversely such a coloring gives a solution. A connected component admitting a coloring has **exactly \(r\)** such colorings: fixing the color of one vertex determines all others. Call these components *good*. Hence \(\delta(A)\) equals the number of good weakly connected support components. This is also the balance criterion of Elduque--Labra (2019); the new work below concerns its finite-field weighted enumeration.

**Step 3 (count all cyclic colorings).** For a fixed coloring \(c\) of all \(n\) labels obeying the edge rule, arrange the labels by their residue classes. The matrix has potentially nonzero blocks only from color class \(i\) to color class \(i+1\). Invertibility forces every color class to have the same size \(m\), so \(n=rm\). Conversely, if all class sizes equal \(m\), the matrix is invertible exactly when each of the \(r\) cyclic blocks is invertible. There are \(g_m(q)^r\) choices after an ordered partition of labels into \(r\) equal classes. Thus the exponential generating series for **pairs consisting of an invertible matrix and a compatible coloring** is
\[
\sum_{m\ge0}\frac{g_m(q)^r}{(m!)^r}x^{rm}=F_{q,r}(x^r).
\]
Every matrix in this colored class has only good connected components. A connected good component admits exactly \(r\) colorings; disconnected good components can be colored independently.

**Step 4 (connected-component exponential formula).** A matrix is uniquely decomposed, up to unordered arrangement, into blocks on the weakly connected components of its support graph. Such a block is invertible whenever the entire matrix is invertible, since no entries join different components. Let \(C_q(x)\) be the exponential series for connected-support invertible matrices, and \(B_{q,r}(x)\) that for connected good-support invertible matrices. The labelled exponential formula yields
\[
G_q(x)=\exp C_q(x),\qquad
F_{q,r}(x^r)=\exp(rB_{q,r}(x)).
\]
Marking every good component by \(u\), and every other component by \(1\), gives
\[
\begin{aligned}
\sum_{n\ge0}\frac{x^n}{n!}\sum_{A\in\operatorname{GL}_n(\mathbb F_q)}u^{\delta(A)}
&=\exp\bigl(C_q(x)+(u-1)B_{q,r}(x)\bigr)\\
&=G_q(x)\,F_{q,r}(x^r)^{(u-1)/r}.
\end{aligned}
\]
This is an identity of formal power series and is valid for every prime power of odd characteristic.

**Step 5 (sharp dimension cutoff and first stratum).** Every good connected component has \(rm\) vertices for a positive integer \(m\), by Step 3 applied to that component. Thus \(\delta(A)\le\lfloor n/r\rfloor\). Equality, and indeed every intermediate value, is achieved by disjoint weighted directed \(r\)-cycles (one per good component) and a diagonal invertible block on any remaining vertices; the latter contributes no good component. For \(r\le n<2r\), a matrix with \(\delta(A)=1\) must consist of a single weighted directed \(r\)-cycle on some \(r\) labels, plus an arbitrary invertible matrix on the remaining \(n-r<r\) labels. There are \((r-1)!\) cyclic arrangements and \((q-1)^r\) edge-weight choices, proving the exact first-stratum formula.

## Verification
The standalone Python 3 checker `verify.py` enumerates finite-field structure matrices and solves the **full Leibniz linear system in all \(n^2\) unknown matrix entries of a derivation**, rather than using the connected-component rule. It independently generates coefficients from the formal formula using exact rational arithmetic. Exhaustive checks passed for \((p,n)=(3,1),(3,2),(3,3),(5,1),(5,2),(7,1),(7,2),(2,1),(2,2),(2,3)\), totaling \(13{,}963\) invertible matrices. Additional coefficient identities at dimensions \(4\) and primes \(3,5\) passed. Use `python3 verify.py`. The output is recorded in `test_results.txt`. These finite computations are checks, not an infinite proof; the proof is in Steps 1--5.

## Relationship to prior work
Elduque and Labra, *Evolution algebras, automorphisms, and graphs* (arXiv:1902.02191v1, 2019), Theorem 4.1 and Corollary 4.3, already prove that the derivation dimension of a perfect evolution algebra is given by the qualifying connected components of its directed graph; that structural criterion and the two-dimensional example are **not** claimed as new. The present statement counts the whole \(\operatorname{GL}_n(\mathbb F_q)\) model, simultaneously at every dimension, using cyclic block invertibility and a connected-component weighted exponential formula. Cabrera Casado, Cadavid, and Reis (2023) study derivations of nondegenerate evolution algebras and related graph conditions, but their examined results do not state this labelled finite-field distribution. Prior work on general derivation spaces and graph characterizations also remains relevant.

## Limitations
This theorem counts marked ordered structure matrices, not unmarked algebras, algebra isomorphism classes, or generic arbitrary (possibly singular) evolution algebras. The formal generating series usually have zero analytic radius of convergence because \(g_n(q)\) grows quadratically exponentially in \(n\); no asymptotic coefficient claim follows from analytic singularity arguments. The graph-to-derivation criterion is previously known, and a broader finite-field matrix-enumeration identity not found in the examined sources remains a possible originality risk.

## References
1. A. Elduque and A. Labra, *Evolution algebras, automorphisms, and graphs*, arXiv:1902.02191v1 (first posted 2019-02-06), Theorem 4.1 and Corollary 4.3. https://arxiv.org/abs/1902.02191
2. Y. Cabrera Casado, P. Cadavid, and T. Reis, *Derivations and loops of some evolution algebras*, Rev. R. Acad. Cienc. Exactas Fís. Nat. Ser. A Mat. 117 (2023), article 119, DOI:10.1007/s13398-023-01446-2. https://doi.org/10.1007/s13398-023-01446-2
3. Y. Cabrera Casado, P. Cadavid, M. L. Rodiño Montoya, and P. M. Rodriguez, *On the characterization of the space of derivations in evolution algebras*, arXiv:1912.06925 (2019). https://arxiv.org/abs/1912.06925
