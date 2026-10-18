# A tridiagonal Green kernel for uniform facet normals of fan-graph Lipschitz-free balls

## Finding

Let \(m\ge3\) be an integer, and let \(G_m=K_1\vee P_m\) be the unweighted fan graph with hub \(o\) and ordered path vertices \(1,\ldots,m\). Equip its vertices with shortest-path distance. The unit ball \(P_m\) of the real Lipschitz-free space over this metric is the symmetric edge polytope
\[
P_m=\operatorname{conv}\{\pm(\delta_v-\delta_w):vw\in E(G_m)\}.
\]
Here \(\delta_o=0\) and the other \(\delta_i\) are the canonical molecule coordinates; the corresponding dual unit ball consists of real \(1\)-Lipschitz functions vanishing at \(o\).

Choose a facet of \(P_m\) uniformly, and write \(X_i\) for the value at path vertex \(i\) of its uniquely hub-normalized supporting potential \(f\), so the supporting equation has value \(1\) on that facet. Define integers
\[
b_0=1,\qquad b_1=2,\qquad b_2=4,\qquad
b_k=b_{k-1}+2b_{k-2}+2b_{k-3}\quad(k\ge3),
\]
and \(d_m=b_{m-1}+b_{m-2}\). Then exactly \(2d_m\) facets occur, \(\mathbb E X_i=0\), and the **complete covariance matrix** \(K_m=\operatorname{Cov}(X_1,\ldots,X_m)\) satisfies
\[
\boxed{(K_m)_{ij}=\frac{b_{\min(i,j)-1}\,b_{m-\max(i,j)}}{d_m}\quad(1\le i,j\le m).}
\]

In particular \(K_m\) is positive definite and \(K_m^{-1}\) is an irreducible symmetric tridiagonal matrix with strictly negative immediate off-diagonal entries. Explicitly, putting
\[
\Delta_i=b_i b_{m-i}-b_{i-1}b_{m-i-1}>0\quad(1\le i<m),
\]
one has
\[
\boxed{(K_m^{-1})_{i,i+1}=-(d_m/\Delta_i),\qquad (K_m^{-1})_{ij}=0\quad(|i-j|>1).}
\]
The remaining diagonal entries are uniquely determined by this inverse and are given explicitly in the proof.

Let \(\rho=2.26953084208114\ldots\) be the unique positive real root of \(\rho^3-\rho^2-2\rho-2=0\). For any fixed nonnegative integer \(r\), as \(m\to\infty\) with \(i\to\infty\), \(m-i-r\to\infty\), and \(j=i+r\),
\[
\boxed{\lim (K_m)_{i,j}=\frac{\rho^3}{\rho^2+4\rho+6}\,\rho^{-r}.}
\]
Thus the limiting bulk correlation at separation \(r\) is exactly \(\rho^{-r}\), despite the presence of many overlapping triangular cycles in the original graph.

## Assumptions and scope

All graphs are finite, simple, unweighted and connected. The displayed covariance concerns values of *hub-anchored* supporting potentials; these are dual coordinates in \(\operatorname{Lip}_0(G_m)\), not Euclidean-centered vertex-coordinate representatives. The uniform law is on **facets** of the primal transportation unit ball, equivalently on the distinct vertices of its dual Lipschitz unit ball, rather than on all integer-valued Lipschitz functions. The theorem concerns \(m\ge3\), where the fan is not a cactus; the formulas also hold for \(m=2\). A tridiagonal inverse covariance does not mean that the discrete random vector itself has Gaussian or conditional-independence properties.

## Proof

**1. Enumerating the dual vertices.** The integer-potential facet criterion of Higashitani, Jochemko and Michałek says that a supporting potential is a facet normal precisely when all graph-edge differences have absolute value at most one and edges with absolute difference exactly one span a connected subgraph. Since every path vertex is adjacent to the hub and \(f(o)=0\), all values \(x_i=f(i)\) belong to \(\{-1,0,1\}\). An edge between consecutive path vertices is admissible exactly when its values are not \(-1\) and \(1\) in either order. Every nonzero value is connected tightly to the hub. Thus tight-edge connectedness is equivalent to every zero value having a neighboring nonzero path value. Put differently, valid words have monochromatic nonzero runs, internal zero runs of length at most two, and zero runs at either path endpoint of length at most one. These conditions are sufficient as well as necessary, and every such word labels one distinct facet.

**2. A one-sided extension sequence.** Fix the value \(+1\) at the right boundary of a finite path segment, and let \(b_k\) count valid length-\(k\) words on its left, including the requirement that every zero in the combined word has a neighboring nonzero. Direct inspection gives \(b_0=1\), \(b_1=2\), \(b_2=4\). For \(k\ge3\), classify by the suffix of the left segment immediately preceding the fixed \(+1\): either a \(+1\), one zero preceded by one of the two signs, or two zeros preceded by one of the two signs. These disjoint possibilities yield respectively \(b_{k-1}\), \(2b_{k-2}\), and \(2b_{k-3}\) extensions. This proves the recurrence. By symmetry the same count holds when the fixed boundary value is \(-1\).

To count all facets, split according to the final path value. If it is nonzero, choose its sign and complete the first \(m-1\) positions in \(b_{m-1}\) ways. If it is zero, the preceding value is nonzero; choose its sign and complete the first \(m-2\) positions in \(b_{m-2}\) ways. Therefore the facet count is \(2(b_{m-1}+b_{m-2})=2d_m\).

**3. Exact two-point function.** A valid word is determined by its zero set and an independent choice of \(+1\) or \(-1\) on every maximal consecutive run of nonzero positions. Conditioning on the zero set, the uniform sign choices are independent and symmetric. Hence \(\mathbb E X_i=0\). For \(i<j\), all contributions to \(\sum_x x_i x_j\) cancel if \(i,j\) lie in different nonzero runs; if they belong to the same run, their product is one. Exactly the same argument applies to \(i=j\). The surviving words are precisely those with every position in \([i,j]\) nonzero. Choose their common sign in two ways, independently extend the left end in \(b_{i-1}\) ways, and the right end in \(b_{m-j}\) ways. This gives
\[
\sum_{\text{facets }x}x_i x_j=2b_{i-1}b_{m-j}\quad(i\le j).
\]
Dividing by the facet count \(2d_m\), and using symmetry in the indices, proves the covariance identity.

**4. Invertibility and sparse precision.** The all-\(+1\) word and the \(m\) words obtained by replacing one of its values by zero are all valid facet potentials. Their affine span is the whole \(\mathbb R^m\); hence the covariance is positive definite. Write \(u_i=b_{i-1}\), \(v_i=b_{m-i}\). Then the covariance is a *Green matrix* \((K_m)_{ij}=u_i v_j/d_m\) for \(i\le j\). Its adjacent minors are governed by \(\Delta_i=u_{i+1}v_i-u_iv_{i+1}>0\), since \(b_k\) is strictly increasing. Elementary elimination of this Green matrix gives precisely
\[
(K_m^{-1})_{i,i+1}=-\frac{d_m}{\Delta_i},\qquad
(K_m^{-1})_{11}=\frac{2d_m}{\Delta_1},\qquad
(K_m^{-1})_{mm}=\frac{2d_m}{\Delta_{m-1}},
\]
and, for \(1<i<m\),
\[
(K_m^{-1})_{ii}=\frac{d_m}{b_{i-1}}
\left(\frac{b_{i-2}}{\Delta_{i-1}}+\frac{b_i}{\Delta_i}\right).
\]
For completeness, multiplying this proposed tridiagonal matrix by the Green matrix proves it equals the identity: off-diagonal entries cancel using the two-factor form, while diagonal entries reduce to the adjacent determinant identities \(u_{i+1}v_i-u_iv_{i+1}=\Delta_i\). Strict negativity follows from \(\Delta_i>0\).

**5. Bulk asymptotics.** The recurrence has generating function
\[
\sum_{k\ge0}b_k z^k=\frac{1+z}{1-z-2z^2-2z^3}.
\]
Its dominant pole is the simple positive pole \(z=\rho^{-1}\); the other characteristic roots have strictly smaller modulus than \(\rho\) (they are a nonreal conjugate pair of modulus less than one). Residue extraction gives
\[
b_k\sim A\rho^k,\qquad
A=\frac{\rho+1}{1+4/\rho+6/\rho^2}.
\]
Substitution into the exact covariance formula, with both boundaries diverging and separation held fixed, yields the claimed limit. Dividing by the corresponding diagonal limits yields the bulk correlation \(\rho^{-r}\).

## Verification

The standalone file `verify_fan_facets.py` uses standard-library exact rational arithmetic. For each \(m=2,\ldots,9\), it enumerates all \(3^m\) candidate integral potentials and **independently** tests connectedness of the tight-edge graph by traversal. It then checks the facet count, the mean-zero property, every covariance entry, and every zero or explicit nonzero entry of the inverse covariance. All eight finite instances passed. This checks the computations but does not replace the infinite-family combinatorial proof.

## Relationship to prior work

Higashitani, Jochemko and Michałek (2018, Theorem 3.1) established the integer-potential facet criterion. Braun and Bruegge (2022/2023) analyzed facet counts of sparse symmetric edge polytopes. Mori, Mori and Ohsugi (2023, Section 3) characterized facets of graph suspensions using dominating sets and counted sign choices, encompassing the *underlying enumeration setup* for the fan. Alexander, Fradelizi, García-Lirola and Zvavitch (2019) placed such transportation polytopes in the setting of finite-dimensional Lipschitz-free spaces. None of the inspected relevant mathematical statements evaluates the fan's uniform-facet covariance or proves the exact tridiagonal inverse and sharp correlation rate; the present result relies on, but does not claim, the earlier facet classification.

## Limitations

The path order and hub anchoring are essential to the formula. The full joint law is discrete, not Gaussian; only its covariance has a nearest-neighbor precision matrix. This does not assert a Gaussian Markov field or probabilistic conditional independence. The bulk limit concerns fixed separation away from both endpoints, not a uniform approximation for growing separation. Published and mathematical-record searching cannot rule out every unindexed or differently formulated predecessor; this calculation has not received an independent scientific audit.

## References

1. A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678 (first posted 2018-07-20), Theorem 3.1.
2. B. Braun, K. Bruegge, *Facets of Symmetric Edge Polytopes for Graphs with Few Edges*, arXiv:2201.13303 (first posted 2022-01-31), Journal of Integer Sequences 26 (2023), Article 23.7.2.
3. A. Mori, K. Mori, H. Ohsugi, *Number of facets of symmetric edge polytopes arising from join graphs*, arXiv:2312.11287 (first posted 2023-12-18), Section 3.
4. M. Alexander, M. Fradelizi, L. C. García-Lirola, A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (first posted 2019-11-24).
