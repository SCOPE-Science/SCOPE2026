# Exact rank and volume laws for square two-block sparse-sign sketches

## Finding

Let \(p,q\geq1\) be arbitrary integers and \(n=p+q\). Independently for each of the \(n\) columns, choose a left hash \(L\) uniformly in \(\{1,\ldots,p\}\), a right hash \(R\) uniformly in \(\{1,\ldots,q\}\), and independent uniform signs \(\varepsilon,\delta\in\{-1,1\}\). Form the real \(n\times n\) sketch \(S\) with that column equal to
\[
  2^{-1/2}(\varepsilon e_L+\delta e_{p+R}).
\]
For equal block sizes this is the square, two-block normalized SparseStack model. Unequal block sizes allow different allocations of the same total output dimension.

Let \(E\) be the event \(\operatorname{rank}(S)=n\). On \(E\), let \(C\) be the number of connected components of the bipartite multigraph whose vertices are the \(p+q\) hash buckets and whose labeled edges are the columns. Define
\[
 \Phi_{p,q}(u)=\mathbb E[\mathbf 1_E u^C].
\]
**Exact finite-size theorem.** For every \(p,q\geq1\) and every indeterminate \(u\),
\[
 \boxed{\displaystyle
 \Phi_{p,q}(u)=\frac{(p+q)!\,p!\,q!}{(pq)^{p+q}}
 \sum_{k=0}^{\min(p,q)}(-1)^k
 {1-u/4\choose k}\,
 \frac{q^{p-k}p^{q-k}}{(p-k)!\,(q-k)!}.}
\]
The generalized binomial coefficient is the polynomial \({\alpha\choose k}=\alpha(\alpha-1)\cdots(\alpha-k+1)/k!\), with \({\alpha\choose0}=1\). In particular \(\Phi_{p,q}(1)\) is the **exact nonsingularity probability**, and the coefficients of the polynomial give the joint probabilities of nonsingularity and each possible component count.

On every nonsingular outcome, the Gram-volume determinant has the *exact* discrete value
\[
 \boxed{\det(S^{\mathsf T}S)=4^{C-n/2}.}
\]
Thus the polynomial also determines the entire nonzero determinant distribution (with equal determinant values possibly arising from distinct graph shapes). Its fourth-argument identity is
\[
 \mathbb E\det(S^{\mathsf T}S)=2^{-n}\Phi_{p,q}(4)
 =\frac{n!}{2^n p^p q^q},
\]
where the determinant is zero off \(E\).

For the maximally unequal allocation \(p=1,q\geq1\), the formula simplifies to
\[
 \boxed{\mathbb P(E)=\frac{(q+1)!}{4q^q}.}
\]
For equal blocks \(p=q=b\), the first four exact probabilities are \(1/2\), \(87/256\), \(2675/13122\), and \(126557865/1073741824\) for \(b=1,2,3,4\), respectively. This is an exact-arithmetic, no-oversampling, coordinate-subspace injectivity benchmark; it is not a theorem about all subspaces or floating-point performance.

## Assumptions and scope

Every hash and every sign is independent across columns and blocks. Parallel graph edges are allowed, but every column chooses one bucket in each of two **disjoint** blocks. The matrix is square because the number of columns equals \(p+q\). No numerical rounding, row sparsification, sketch truncation, dependence between signs, or rank tolerance is present. The graph retains isolated vertices. Its cycle count is well defined on \(E\), when every connected component is unicyclic. The labels of the \(n\) input columns matter in the sampling probability.

## Proof

**1. Exact signed-incidence rank classification.** Multiply each column by its left sign, which does not change rank or absolute determinant. The column becomes an incidence vector supported at its two hash endpoints with coefficients \(1\) and an independent fair sign \(\sigma\). For a connected multigraph component with \(v\) vertices and \(e\) edges, its rows admit a nontrivial left-kernel vector precisely when all cycle-sign products satisfy the consistent parity condition; otherwise the row rank is \(v\). This follows by fixing one vertex value and propagating the row-kernel equation along a spanning tree: each extra edge either imposes the already satisfied relation or forces the initial value to zero. Therefore a tree has independent columns (\(e=v-1\)), a unicyclic component has \(e=v\) independent columns exactly when its unique cycle is sign-inconsistent, and any component with \(e>v\) has dependent columns regardless of signs.

Summing \(e-v\) across components gives zero because the full graph has exactly \(n\) edges and \(n\) vertices. Full column rank consequently forces **every** component to have \(e=v\), rather than merely ruling out multicyclic components: any tree or isolated vertex would require some other component to have \(e>v\). Conversely, all-unicyclic components with inconsistent signs give full rank. Conditional on a graph with \(c\) unicyclic components, its distinct cycle parities are independent and fair, so its conditional success probability is exactly \(2^{-c}\).

**2. Exact determinant on success.** In an unicyclic component, repeatedly expand the unnormalized determinant along a leaf row. Each removed tree edge gives a factor of magnitude one; what remains is a cyclic signed-incidence block, including the allowed length-two cycle of parallel edges. Its determinant is zero for consistent signs and has magnitude two for inconsistent signs. Multiplying across \(c\) components, the unnormalized determinant therefore has magnitude \(2^c\) on success. Each of the \(n\) normalized columns supplies a factor \(2^{-1/2}\), yielding \(|\det S|=2^{c-n/2}\) and the asserted Gram determinant.

**3. Enumeration with labeled vertices and edges.** Introduce formal exponential generating functions \(T_L(x,y)\) and \(T_R(x,y)\) for bipartite labeled trees rooted on the left and right, respectively. Decomposing the neighbor branches of the root gives the formal identities
\[
 T_L=x\exp(T_R),\qquad T_R=y\exp(T_L).
\]
Every connected unicyclic bipartite multigraph is an alternating even-cycle core decorated with rooted trees. For a core using \(k\) left and \(k\) right vertices, its contribution after dividing by the left/right vertex-label factorials, by the edge-multiplicity factorial, and by the fair probability \(1/2\) that the cycle parity is inconsistent, is
\[
 \frac{(T_LT_R)^k}{4k},\qquad k\geq1.
\]
For \(k\geq2\), this uses the \(k!(k-1)!/2\) undirected alternating cycles on prescribed sets of \(k\) left and \(k\) right vertices. The \(k=1\) term is the two-parallel-edge cycle: its \(1/2!\) edge-multiplicity factor and its \(1/2\) sign-success factor give exactly \(1/4\). Attachments introduce no additional independent cycles.

Marking each component by \(u\) and using the labeled exponential formula gives
\[
 F(x,y;u)=\exp\!\left(\sum_{k\geq1}\frac{u}{4k}(T_LT_R)^k\right)
 =(1-T_LT_R)^{-u/4}.
\]
For \(p\) labeled left vertices, \(q\) labeled right vertices and \(n=p+q\) labeled edges, the favorable hash-and-sign weight is \(p!q!n![x^p y^q]F\). The edge labels produce \(n!\) arrangements, and the parallel-edge factorial has already been included in the generating function. Each independently labeled edge chooses one of \(pq\) ordered pairs uniformly; dividing by \((pq)^n\) yields
\[
 \Phi_{p,q}(u)=\frac{n!p!q!}{(pq)^n}[x^p y^q](1-T_LT_R)^{-u/4}.
\]

**4. Exact coefficient evaluation.** Make the formal change of variables \(s=T_L\), \(t=T_R\); then \(x=s e^{-t}\) and \(y=t e^{-s}\). Its logarithmic Jacobian is \(1-st\). Formal bivariate coefficient extraction (equivalently, the residue change of variables) gives
\[
 [x^p y^q](1-T_LT_R)^{-u/4}
 =[s^p t^q]e^{q s+p t}(1-st)^{1-u/4}.
\]
Expanding \((1-st)^{1-u/4}\) by the generalized binomial theorem and the two exponentials by Taylor's theorem gives the finite sum in the Finding, with \(k\leq\min(p,q)\). This proves every polynomial coefficient exactly, without enumeration cutoff or limiting approximation.

**5. Two checks and a simple specialization.** At \(u=4\), the factor \((1-st)^{1-u/4}\) becomes one. The exact coefficient is \(q^p p^q/(p!q!)\), so \(\Phi_{p,q}(4)=n!/(p^p q^q)\), proving the determinant-moment formula after multiplication by \(2^{-n}\). Independently, the columns are iid with covariance \(\operatorname{diag}((2p)^{-1}I_p,(2q)^{-1}I_q)\). Expanding the determinant and averaging columnwise gives \(\mathbb E\det(S)^2=n!\det(\operatorname{Cov}(S_{:,1}))\), reproducing the same identity. If \(p=1\), the binomial sum has only two terms, immediately giving \(\Phi_{1,q}(1)=(q+1)!/(4q^q)\).

## Verification

Run `python verify.py` with a Python 3 standard-library interpreter. The included standalone checker independently enumerates every hash assignment for eleven block allocations through \((p,q)=(3,3)\), averaging the independent sign parities from graph structure. It additionally enumerates every hash and sign assignment and computes actual integer determinants for five small allocations. It verifies exact rational nonsingularity probabilities, the extreme-allocation closed form, polynomial coefficient nonnegativity, and the independent covariance/determinant second-moment identity for one hundred block allocations. These are supplementary finite checks; Steps 1–5 prove the result for every positive integer pair.

## Relationship to prior work

Jeendgar, Flint and Anzt (arXiv:2606.20195, initially public 18 June 2026; revised 13 October 2026) define the normalized independent-block SparseStack distribution and investigate the practical geometry, mixed-precision errors and GPU performance. Their exact coordinate-subspace CountSketch collision formula concerns the one-block case, not this two-block all-size joint rank/volume law. Camaño, Epperly, Meyer and Tropp (arXiv:2508.21189, Sections 1.5.1, 3.1 and Appendix B) study general SparseStack injectivity, matrix-function guarantees and numerical performance but do not give the displayed exact two-block finite coefficient law in the material inspected. General sparse-random-matrix rank theory, including Coja-Oghlan and collaborators (2023), addresses broad rank asymptotics rather than this all-size coefficient and determinant distribution. Classical signed-incidence graph rank facts are used and not claimed as new. Previous analyses of this same two-block coordinate model with aspect-ratio asymptotics do not imply the exact finite-size polynomial or determinant spectrum at the square boundary. No exhaustive historical uniqueness claim is made.

## Limitations

The result holds for one particular two-sparse signed sketch distribution and the square coordinate-subspace endpoint. It does not characterize the smallest positive singular value, condition-number tails, general subspace embeddings, any positive oversampling, nonuniform or dependent hashes, finite-precision accumulation, or practical end-to-end runtime. The exact Gram determinant measures volume, not worst-direction distortion; a nonzero but small determinant does not itself quantify the inverse norm. The unicyclic rank criterion is classical graph linear algebra; the asserted contribution is the exact finite random-sketch rank-and-volume generating law and its block-allocation specializations. Equivalent formulations in older graph-enumeration literature remain possible.

## References

1. A. Jeendgar, C. Flint, and H. Anzt, *Randomized Sketching is Robust to Low-Precision Rounding on GPUs*, arXiv:2606.20195, originally submitted 18 June 2026; revised as *On the Robustness of Sparse Randomized Sketching to FP16 Rounding on GPUs* on 13 October 2026. https://arxiv.org/abs/2606.20195 ; https://arxiv.org/html/2606.20195
2. C. Camaño, E. N. Epperly, R. A. Meyer, and J. A. Tropp, *Faster Linear Algebra Algorithms with Structured Random Matrices*, arXiv:2508.21189v1, 28 August 2025. https://arxiv.org/html/2508.21189
3. A. Coja-Oghlan and collaborators, *The rank of sparse random matrices*, Random Structures & Algorithms (2023). https://doi.org/10.1002/rsa.21085
4. G. Cornuéjols, *Combinatorial Optimization: Packing and Covering*, Chapter 6 on signed incidence and balanced matrices, SIAM (2001). https://doi.org/10.1137/1.9780898717105.ch6
