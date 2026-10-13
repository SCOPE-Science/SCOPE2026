# Full-rank quantum Cesàro mixing on generalized-quadrangle incidence graphs

## Finding
Let \(\mathcal Q\) be any finite generalized quadrangle of order \((q,q)\), where \(q\ge2\) is an integer and such a quadrangle exists. Write \(X\) for its bipartite point–line incidence graph, \(A\) for its real adjacency matrix, and \(N=2(q+1)(q^2+1)\) for its number of vertices. The infinite-time continuous-time adjacency quantum-walk average mixing matrix is
\[
\widehat M=\lim_{T\to\infty}\frac1T\int_0^T\big(e^{itA}\circ e^{-itA}\big)\,dt.
\]
Here \(\circ\) denotes entrywise multiplication, and the integrand means the entrywise product of the unitary evolution with its complex conjugate. The complete spectrum, listing each mixing eigenvalue followed by its multiplicity, is
\[
\begin{array}{c|c}
\text{mixing eigenvalue}&\text{multiplicity}\\ \hline
1&1\\
\dfrac{q}{2(q+1)}&1\\
\dfrac{(q-1)\big(3q^2+4q+3+2(q+1)\sqrt{2q}\big)}{8q(q^2+1)}&\dfrac{q(q+1)^2}{2}\\
\dfrac{(q-1)\big(3q^2+4q+3-2(q+1)\sqrt{2q}\big)}{8q(q^2+1)}&\dfrac{q(q+1)^2}{2}\\
\dfrac{3q^2-2q+3}{8q(q+1)}&q(q^2+1).
\end{array}
\]
Every listed eigenvalue is strictly positive for \(q\ge2\). Consequently \(\widehat M\) is positive definite, with \(\operatorname{rank}\widehat M=N\), for *every* generalized quadrangle of order \((q,q)\), without an assumption of point, line, or flag transitivity. The boundary at \(q=1\) is sharp: the corresponding thin incidence graph is \(C_8\), whose average-mixing rank is \(4\), rather than \(8\).

More precisely, \(\widehat M\) is constant on each of the five graph-distance classes. For distance matrices \(D_0,\ldots,D_4\),
\[
\widehat M=\sum_{i=0}^4 c_iD_i,
\]
with the following exact coefficients:
\[
\begin{aligned}
c_0&=\frac{3q^6+4q^5+10q^4+4q^3+3q^2+4}{8(q+1)^2(q^2+1)^2},\\
c_1&=\frac{q^5+2q^4+q^3+2}{4(q+1)^2(q^2+1)^2},\\
c_2&=\frac{3q^4+2q^2+7}{8(q+1)^2(q^2+1)^2},\\
c_3&=\frac{q^2+4q+1}{4q(q+1)^2(q^2+1)^2},\\
c_4&=\frac{3q^4+4q^3+14q^2+4q+3}{8q^2(q+1)^2(q^2+1)^2}.
\end{aligned}
\]
In particular, the answer depends only on the order, not on the isomorphism type of the generalized quadrangle.

## Assumptions and scope
A generalized quadrangle of order \((q,q)\) has \(q+1\) points on each line and \(q+1\) lines through each point; for each nonincident point–line pair there is a unique intervening incident point on that line collinear with the given point. Its incidence graph is finite, simple, connected, bipartite, \((q+1)\)-regular and distance-regular of diameter four. Its intersection array is \(\{q+1,q,q,q;1,1,1,q+1\}\). The theorem is conditional on the existence of such a geometry; symplectic generalized quadrangles provide examples for prime-power orders. It addresses infinite-time Cesàro averaging, not instantaneous uniform mixing, perfect state transfer, or the corresponding discrete-time quantum walk.

## Proof
**Adjacency spectrum and multiplicities.** Let \(B\) denote the adjacency matrix of the collinearity graph on the point set and \(C\) the square point–line incidence matrix. There are \(v=(q+1)(q^2+1)\) points and equally many lines, and
\[
CC^{\mathsf T}=(q+1)I_v+B.
\]
The generalized-quadrangle axiom gives the strongly regular parameters
\[
(v,k,\lambda,\mu)=\big((q+1)(q^2+1),q(q+1),q-1,q+1\big).
\]
Indeed, two collinear points have exactly the other \(q-1\) points of their unique joining line as common neighbors, and two noncollinear points have one common neighbor along each of the \(q+1\) lines through either point. Hence \(B\) has eigenvalues \(q(q+1)\), \(q-1\), and \(-q-1\), respectively with multiplicities \(1\), \(q(q+1)^2/2\), and \(q(q^2+1)/2\). The bipartite incidence adjacency matrix \(A=\begin{pmatrix}0&C\\C^{\mathsf T}&0\end{pmatrix}\) therefore has eigenvalues
\[
\theta\in\{q+1,-(q+1),\sqrt{2q},-\sqrt{2q},0\}
\]
with multiplicities \(m_\theta=1,1,q(q+1)^2/2,q(q+1)^2/2,q(q^2+1)\), respectively. These five eigenvalues are distinct for \(q\ge2\).

**Distance polynomials and spectral projector entries.** Write \(D_i\) for the distance-\(i\) adjacency matrices and \(k_i\) for their common row sums. The intersection array yields
\[
(k_0,k_1,k_2,k_3,k_4)=(1,q+1,q(q+1),q^2(q+1),q^3),
\]
\[
\begin{aligned}
p_0(t)&=1,\quad p_1(t)=t,\quad p_2(t)=t^2-(q+1),\\
p_3(t)&=t^3-(2q+1)t,\\
p_4(t)&=\frac{t^4-(3q+1)t^2+q(q+1)}{q+1},
\end{aligned}
\]
where \(D_i=p_i(A)\). In particular, for the orthogonal projector \(E_\theta\) onto the \(\theta\)-eigenspace, \(E_\theta\) belongs to the distance algebra and is constant on graph-distance classes. If its entry at distance \(i\) is \(e_{\theta,i}\), taking the trace against \(D_i\) proves
\[
Nk_i e_{\theta,i}=\operatorname{tr}(E_\theta D_i)
=m_\theta p_i(\theta),\qquad
 e_{\theta,i}=\frac{m_\theta p_i(\theta)}{Nk_i}.
\]
This calculation establishes the normalization; there is no hidden division by an eigenspace dimension.

**Cesàro limit.** Since \(A\) is real symmetric, time averaging kills cross terms between unequal eigenvalues, and
\[
\widehat M=\sum_\theta E_\theta\circ E_\theta.
\]
Thus the distance-\(i\) entry is exactly
\[
c_i=\sum_\theta\left(\frac{m_\theta p_i(\theta)}{Nk_i}\right)^2.
\]
Substituting the five eigenvalues and the five distance polynomials and expanding gives the five displayed rational functions \(c_i\). Because \(D_i=p_i(A)\), the quantum mixing eigenvalue on the adjacency \(\theta\)-eigenspace is precisely
\[
\mu_\theta=\sum_{i=0}^4 c_ip_i(\theta).
\]
Substitution and simplification give the five displayed eigenvalues; their multiplicities are the adjacency multiplicities already proved. In particular \(\sum_i k_ic_i=1\), as also follows from stochasticity.

**Positivity and boundary.** For \(q\ge2\), every factor of the expressions is positive except potentially the minus branch. But its numerator includes
\[
3q^2+4q+3-2(q+1)\sqrt{2q}
=\big(q+1-\sqrt{2q}\big)^2+2(q^2+1)>0.
\]
All eigenvalues are therefore strictly positive and the rank equals \(N\). For the thin order-one quadrangle the incidence graph is the eight-cycle, and direct evaluation of the same five spectral branches at \(q=1\) gives two zero branches of multiplicity two each, hence rank four.

## Verification
The accompanying \(\texttt{verify.py}\) checks the five distance-entry formulas, the five spectral eigenvalue formulas and normalization symbolically in \(q\) with exact arithmetic. Separately, it constructs symplectic generalized quadrangles over the prime fields of orders two and three, forms their actual bipartite incidence matrices, independently diagonalizes these matrices, and compares the resulting Cesàro average with the predicted distance-class matrix. The replay result is:

```text
VERIFY_OK symbolic_distance_coefficients=5 symbolic_eigenvalues=5 finite_graphs=2 matrix_entries=7300 max_entry_error=6.66e-16 max_eigen_error=9.44e-16
```

The matrix comparisons cover graph orders \(30\) and \(80\), or \(7300\) entries. Symbolic simplification confirms the identities independent of \(q\); the unrestricted geometric reduction and strict inequalities are supplied above as mathematical proof, not inferred from the finite examples.

## Relationship to prior work
The spectral-projector formula for continuous-time quantum average mixing is standard; see Godsil (2011), Coutinho–Godsil–Guo–Zhan (2018), and Coutinho–Baptista–Godsil–Spier–Werner (2022). General association-scheme eigenmatrix methods can compute average mixing on any specified distance-regular graph; the 2024 survey by Coutinho and Guo also discusses mixing rank problems, especially for *primitive* distance-regular graphs. The present bipartite incidence graphs are imprimitive, so their full-rank classification does **not** resolve the primitive-graph question. Huang's 2014 treatment of bipartite diameter-four distance-regular graphs supplies related geometrical parameters but does not give the displayed quantum average-mixing spectrum. The contribution isolated here is the explicit, order-uniform spectrum, distance-profile, and strict positivity classification for all generalized quadrangles of order \((q,q)\), including nontransitive examples, with the sharp thin boundary. Existing general algorithms and association-scheme identities may substantially shorten derivations and are not represented as new.

## Limitations
The result is conditional on the existence of the indicated geometries; it does not establish existence for arbitrary integers \(q\). It covers balanced order \((q,q)\), not general order \((s,t)\). The finite numerical tests are illustrative only. No general claim of novelty relative to every unpublished or inaccessible work is possible, and a closed special case embedded in a more general published eigenmatrix theorem remains an originality risk.

## References
1. C. Godsil, *Average mixing of continuous quantum walks*, arXiv:1103.2578 (2011).
2. G. Coutinho, C. Godsil, K. Guo, H. Zhan, *A New Perspective on the Average Mixing Matrix*, Electronic Journal of Combinatorics 25(4), P4.14 (2018), doi:10.37236/7867, arXiv:1709.03591.
3. G. Coutinho, P. Baptista, C. Godsil, T. Spier, S. Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (first public version 2022-08-18).
4. G. Coutinho, K. Guo, *Selected open problems in continuous-time quantum walks*, arXiv:2404.02236v1 (2024).
5. J. Huang, *Bipartite Distance-Regular Graphs of Diameter Four*, University of Waterloo thesis (2014).
