# Exact max-norm Hodge stability on symmetric block-design incidence graphs

## Finding
For the point–block incidence graph of **any nontrivial symmetric** \(2\)-design with parameters \(2\!-(v,k,\lambda)\), equip every edge with unit conductance and orient every edge from its point to its block. Let \(P\) denote the Euclidean orthogonal projection from edge flows onto potential-gradient flows, and \(Q=I-P\) the orthogonal circulation projection. Their induced coordinatewise maximum norms are
\[
\boxed{\|P\|_{\infty\to\infty}=1+\frac{2(k-1)\{2(k-\lambda)^2+(\lambda-1)(2k-\lambda)\}}{vk\lambda},}
\]
\[
\boxed{\|Q\|_{\infty\to\infty}=\|P\|_{\infty\to\infty}+1-\frac{2(2v-1)}{vk}.}
\]
Both values are attained by signed unit-bounded edge data. In particular, for every such design, \(\|P\|_{\infty\to\infty}>\|Q\|_{\infty\to\infty}\) if \(k\le3\), whereas \(\|Q\|_{\infty\to\infty}>\|P\|_{\infty\to\infty}\) if \(k\ge4\). The strict reversal depends **only on the block size**, not the intersection parameter or isomorphism type.

For a finite projective plane of order \(q\ge2\), this specializes to
\[
\|P\|_{\infty\to\infty}=1+\frac{4q^3}{(q+1)(q^2+q+1)},\qquad
\|Q\|_{\infty\to\infty}=\|P\|_{\infty\to\infty}+1-\frac{2(2q^2+2q+1)}{(q^2+q+1)(q+1)}.
\]
Thus the projective-plane gradient and circulation norms approach \(5\) and \(6\), respectively, along prime-power orders \(q\to\infty\). More generally, for any family of existing symmetric designs with \(k\to\infty\) and \(\lambda/k\to\alpha\in[0,1]\), these norms converge respectively to \(5-4\alpha+2\alpha^2\) and \(6-4\alpha+2\alpha^2\).

## Assumptions and scope
A symmetric \(2\!-(v,k,\lambda)\) design has \(v\) points and \(v\) blocks, every block contains \(k\) points, every point occurs in \(k\) blocks, and every two distinct points occur together in exactly \(\lambda\) blocks. Throughout, assume the design is nontrivial: \(2\le k<v\), \(1\le\lambda<k\). Necessarily
\[
\lambda(v-1)=k(k-1).
\]
Distinct blocks also meet in exactly \(\lambda\) points. Its simple connected bipartite incidence graph has \(2v\) vertices, \(vk\) edges, and degree \(k\). The edge space is real Euclidean \(\mathbb R^{vk}\), with its standard inner product and coordinate maximum norm. For an incidence edge \(e=(p,\ell)\), the corresponding incidence column is \(b_e=\mathbf e_p-\mathbf e_\ell\), and \(B\) is the matrix of all these columns. The vertex Laplacian is \(L=BB^{\mathsf T}\) and
\[
P=B^{\mathsf T}L^\dagger B,\qquad Q=I-P.
\]
Here \(L^\dagger\) is the Moore–Penrose inverse; no geometric realization or transitive automorphism action is assumed. All finite symmetric designs are covered, including non-Desarguesian examples.

## Proof
Let \(A\) be the \(v\times v\) point–block incidence matrix. Its Gram matrices obey
\[
AA^{\mathsf T}=A^{\mathsf T}A=(k-\lambda)I+\lambda J,
\qquad A\mathbf1=A^{\mathsf T}\mathbf1=k\mathbf1.
\]
Consequently \(L=\begin{psmallmatrix}kI&-A\\-A^{\mathsf T}&kI\end{psmallmatrix}\). On the direct sum of the mean-zero point and block coordinate subspaces, block inversion gives
\[
\left.L^{-1}\right|_{\mathbf1^\perp\oplus\mathbf1^\perp}
=\frac1{k^2-k+\lambda}
\begin{pmatrix}kI&A\\A^{\mathsf T}&kI\end{pmatrix},
\qquad k^2-k+\lambda=v\lambda.
\]
There is one further nonconstant eigenvector, with coordinates \((\mathbf1,-\mathbf1)\), eigenvalue \(2k\). The constant vector \((\mathbf1,\mathbf1)\) is in the kernel. Combining these orthogonal components and applying \(B^{\mathsf T}\) on both sides yields, for edges \(e=(p,\ell)\) and \(f=(p',\ell')\), the **complete transfer-current kernel**
\[
\boxed{
P_{ef}=\frac{k(\mathbf1_{p=p'}+\mathbf1_{\ell=\ell'})-A_{p\ell'}-A_{p'\ell}}{v\lambda}+\frac1{vk}.}
\]
This formula is valid for every symmetric design and every pair of its incidence edges, with no transitivity hypothesis.

Fix any edge \(e=(p,\ell)\), and scale its row of \(P\) by \(vk\lambda\). Exactly five classes occur, completely determined by the design axioms:

| Edge \(f\) relative to \(e\) | Count | Scaled entry \(vk\lambda P_{ef}\) |
|:---|---:|---:|
| identical | \(1\) | \(2k(k-1)+\lambda\) |
| shares point or block, but not identical | \(2(k-1)\) | \(k(k-2)+\lambda\) |
| disjoint, exactly one crossed incidence | \(2(k-1)(k-\lambda)\) | \(\lambda-k\) |
| disjoint, both crossed incidences | \((k-1)(\lambda-1)\) | \(\lambda-2k\) |
| disjoint, neither crossed incidence | \((k-1)(k-\lambda)^2/\lambda\) | \(\lambda\) |

To verify the counts, the \(k-1\) other blocks through \(p\) each contain \(k-\lambda\) points outside \(\ell\), giving one of the two one-cross families. The other one-cross family is its dual. Each of the \(k-1\) other points of \(\ell\) lies on exactly \(\lambda-1\) other blocks through \(p\), giving the two-cross family. Finally, each of the \(v-k=(k-1)(k-\lambda)/\lambda\) blocks not through \(p\) contains exactly \(k-\lambda\) points outside \(\ell\), giving the zero-cross class. These five classes partition all \(vk\) edges.

For \(2\le k<v\), the only negative entries are the two disjoint crossed-incidence classes; all other entries are strictly positive. Because the constant edge vector equals a point-versus-block potential gradient, \(P\mathbf1=\mathbf1\). Hence the absolute row sum is one plus twice the total magnitude of negative entries:
\[
\sum_f|P_{ef}|=1+\frac{2\{2(k-1)(k-\lambda)^2+(k-1)(\lambda-1)(2k-\lambda)\}}{vk\lambda}.
\]
This is the claimed gradient norm, since the row formula does not depend on \(e\).

The diagonal entry is \(P_{ee}=(2v-1)/(vk)\) (substitute \(v\lambda=k^2-k+\lambda\) into the identical-edge row). It satisfies \(0<P_{ee}<1\), since \(vk-(2v-1)=v(k-2)+1>0\). For \(Q=I-P\), all off-diagonal entries have the same absolute values as those of \(P\), and the diagonal becomes \(1-P_{ee}\). Thus
\[
\sum_f|Q_{ef}|=\sum_f|P_{ef}|+1-2P_{ee},
\]
proving its exact norm. The difference is
\[
\|Q\|_{\infty\to\infty}-\|P\|_{\infty\to\infty}
=1-\frac{2(2v-1)}{vk}=\frac{k-4}{k}+\frac{2}{vk}.
\]
It is negative for \(k=2,3\), and positive for \(k\ge4\). For either operator, choose an arbitrary output edge and take the input edge vector to be the signs of that output row, with arbitrary values of magnitude at most one on zero entries; the corresponding output coordinate attains the absolute row sum, proving sharpness.

For a projective plane, substitute \((v,k,\lambda)=(q^2+q+1,q+1,1)\). For general design families, use \(v\lambda=k^2-k+\lambda\) and \(\lambda/k\to\alpha\) in the rational expressions; the projective-plane convergence uses prime-power planes, whose existence is known. The examples \(\alpha=1/2\) and \(\alpha=1\) also occur along binary Hadamard designs and complements of prime-power projective planes, respectively.

## Verification
The accompanying `checker.py` independently constructs incidence graphs from prime-field projective planes, their complementary designs, and binary Hadamard designs. With Python standard-library exact rational arithmetic, it reconstructs a row of \(P\) by solving the reduced vertex Laplacian rather than using the claimed formula as an input. It then checks individual current entries, all five support counts, the diagonal, and both induced norms. The checker's executed test suite passed **5,979 exact assertions** over nine design configurations. The analytic proof above, rather than a finite test, establishes the universal statements.

## Relationship to prior work
Graph combinatorial Hodge theory supplies the gradient–cycle orthogonal decomposition and its least-squares interpretation; transfer-current theory identifies the electrical interpretation of the matrix \(B^{\mathsf T}L^\dagger B\). General electrical-flow localization results control norms without computing this exact design-specific row formula. The present calculation exploits the strong point–block incidence identities to derive every transfer-current entry and its signs, and obtains exact worst-case amplification and the degree-four reversal for arbitrary symmetric designs. No priority or independence certification is asserted, and equivalent expressions under electrical-network terminology may predate this calculation.

## Limitations
The statements concern **unweighted**, undirected simple incidence graphs of **symmetric** nontrivial designs with standard Euclidean edge projection and coordinate \(\ell_\infty\) norms. They do not cover arbitrary nonsymmetric block designs, arbitrary conductance patterns, or other induced norms. Asymptotic limits apply only along existing parameter families. Numerical examples and the standalone checker are consistency checks, not substitutes for the universal proof. Historical originality remains subject to a fuller expert literature audit.

## References
1. X. Jiang, L.-H. Lim, Y. Yao, Y. Ye, *Statistical ranking and combinatorial Hodge theory*, arXiv:0811.1067, publicly available November 7, 2008. https://arxiv.org/abs/0811.1067
2. A. Kassel, W. Wu, *Transfer current and pattern fields in spanning trees*, arXiv:1312.2946, first posted December 10, 2013. https://arxiv.org/abs/1312.2946
3. J. Kelner, P. Maymounkov, *Electric routing and concurrent flow cutting*, arXiv:0909.2859, 2009. https://arxiv.org/abs/0909.2859
4. A. Schild, S. Rao, N. Srivastava, *Localization of electrical flows*, arXiv:1708.01632, 2017. https://arxiv.org/abs/1708.01632
