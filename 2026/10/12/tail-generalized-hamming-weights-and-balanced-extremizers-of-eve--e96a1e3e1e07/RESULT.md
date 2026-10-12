# Tail generalized Hamming weights and balanced extremizers of even-cycle edge codes

## Finding
Let \(k\geq 3\) be an integer, let \(q>2\) be a prime power, and put \(Q=q-1\). The edge code \(C_{2k,q}\) of the cycle of length \(2k\) is the \(\mathbb F_q\)-linear code obtained by evaluating the \(2k\) monomials \(x_i x_{i+1}\), with cyclic subscripts, on \((\mathbb F_q^\times)^{2k}\). Its length is \(N=Q^{2k}\) and its dimension is \(2k\).

For every \(k\leq r\leq 2k-1\), set \(d=2k-r\). Then its \(r\)-th generalized Hamming weight is
\[
d_r(C_{2k,q})=Q^{2k}-Q^{d+1}.
\]
Also \(d_{2k}(C_{2k,q})=Q^{2k}\).

Define \(\mathcal B_{k,d}(Q)\) to be the set of partitions of the \(2k\) **edge positions** into exactly \(d\) nonempty *unlabeled* blocks \(B\), each satisfying
\[
\#\{i\in B:i\text{ odd}\}-\#\{i\in B:i\text{ even}\}\equiv0\pmod Q.
\]
The exact number of distinct dimension-\(r\) subcodes attaining \(d_r\) is
\[
\boxed{\quad E_r(C_{2k,q})=Q^{2k-d-1}\,|\mathcal B_{k,d}(Q)|.\quad}
\]
Moreover, all attaining subcodes are classified by these partitions and compatible nonzero edge scalars as specified in the proof. These statements hold without a large-field assumption.

For the stable range \(q\geq k+2\), every block has as many odd as even edge positions, and the count is explicitly
\[
E_r(C_{2k,q})=Q^{2k-d-1}\frac{(k!)^2}{d!}
\sum_{\substack{a_1+\cdots+a_d=k\\a_j\geq1}}
\prod_{j=1}^d\frac{1}{(a_j!)^2}.
\]
More generally, for every \(Q\geq2\), the exact residue-partition count is the finite multinomial sum
\[
|\mathcal B_{k,d}(Q)|=
\frac{(k!)^2}{d!}
\sum_{\substack{\sum_j a_j=\sum_j b_j=k\\
 a_j,b_j\geq0,\ a_j+b_j>0\\a_j-b_j\equiv0\pmod Q}}
\prod_{j=1}^d\frac{1}{a_j!\,b_j!}.
\]

For illustration, over \(\mathbb F_5\) and the six-cycle, the last four generalized weights are \((3840,4032,4080,4096)\), and the numbers of their minimizing subcodes are \((96,576,256,1)\). Over \(\mathbb F_3\), the six-cycle weights are \((48,56,60,64)\), with minimizing-subcode counts \((60,120,16,1)\); the additional minimizers at this smaller field are precisely accounted for by the congruence condition.

## Assumptions and scope
A generalized Hamming weight \(d_r(C)\) is the minimum of \(|\operatorname{supp}(D)|\) over all distinct \(r\)-dimensional linear subcodes \(D\subseteq C\), where a coordinate lies in \(\operatorname{supp}(D)\) if some codeword of \(D\) is nonzero there. Subcodes are counted as linear subspaces, not by their ordered bases. Only affine-torus evaluation is used: the \(N\) coordinate positions are all vertex-tuples with nonzero entries, including those mapping to the same edge-product tuple. The formulas give the upper half of the generalized-weight hierarchy; no exact assertion is made for \(1\leq r<k\).

## Proof
**1. The edge-product image.** Put \(n=2k\) and write indices modulo \(n\). Define
\[
\Phi:(\mathbb F_q^\times)^n\longrightarrow(\mathbb F_q^\times)^n,
\qquad \Phi(x)_i=x_i x_{i+1}.
\]
Every image point \(u\) obeys \(\prod_{i\ \mathrm{odd}}u_i=\prod_{i\ \mathrm{even}}u_i\), because both products equal \(\prod_i x_i\). Conversely, given nonzero \(u_i\) satisfying that equation, choose an arbitrary nonzero \(x_1\) and recursively set \(x_{i+1}=u_i/x_i\). The closing equation is exactly the displayed product identity. Therefore \(\Phi\) is onto
\[
H=\{u\in(\mathbb F_q^\times)^n:\prod_{i\ \mathrm{odd}}u_i=\prod_{i\ \mathrm{even}}u_i\},
\]
and every fiber has precisely \(Q\) points. The monomials \(x_i x_{i+1}\) are linearly independent as functions on the vertex torus: their distinct square-free exponent vectors lie in \(\{0,1\}^n\), with every exponent below \(q-1\). This follows from successive one-variable interpolation on \(\mathbb F_q^\times\). Consequently \(\dim C_{2k,q}=n\).

**2. All subcodes become linear sections.** For an arbitrary \(r\)-dimensional subcode, let \(W\leq\mathbb F_q^n\) be its \(r\)-dimensional coefficient space, and let \(U=W^\perp\leq\mathbb F_q^n\) be its ordinary dot-product annihilator. Then \(\dim U=d=n-r\). A vertex-torus coordinate is zero simultaneously for every codeword of the subcode exactly when \(\Phi(x)\in U\). Thus its number of simultaneous zero coordinates is
\[
Z(W)=Q\,|U\cap H|=Q\,|U\cap(\mathbb F_q^\times)^n\cap H|.
\]
Choose any \(d\) coordinate positions whose restrictions to \(U\) form an independent coordinate projection. Such a set exists because \(\dim U=d\). This projection is injective on \(U\), so there are at most \(Q^d\) points of \(U\) with every coordinate nonzero, and hence \(Z(W)\leq Q^{d+1}\).

**3. The bound is sharp precisely at and above the half-dimension threshold.** For each \(1\leq d\leq k\), partition the \(k\) odd edge positions and \(k\) even edge positions into \(d\) corresponding nonempty groups, each with equal cardinalities. Set \(u_i=t_j\) for every edge position \(i\) in group \(j\), with \(t_1,\ldots,t_d\in\mathbb F_q\). The resulting \(d\)-plane \(U\) is contained in the multiplicative hypersurface whenever all \(t_j\) are nonzero, because odd and even exponents cancel groupwise. It therefore contains exactly \(Q^d\) points of \(H\) in the torus, showing \(Z(W)=Q^{d+1}\) and proving the weight formula for \(k\leq r\leq n-1\). Since every generator monomial is nonzero at every vertex-torus point, the full code has support \(N\), establishing \(d_n=N\).

**4. Rigidity of every extremizer.** Suppose equality \(|U\cap H|=Q^d\) holds. Relative to any invertible \(d\)-coordinate projection, every torus assignment \(t\in(\mathbb F_q^\times)^d\) must yield a point of \(U\cap H\). Thus every remaining original coordinate functional on \(U\) is nowhere zero on this entire torus. A nonzero linear form in at least two of the \(t_j\) always has a torus zero when \(q>2\). Indeed, after fixing all but two participating variables nonzero, choose those two nonzero terms with prescribed sum: \(\mathbb F_q^\times+\mathbb F_q^\times=\mathbb F_q\) for every \(q>2\). Hence every coordinate functional of \(U\) is a nonzero scalar multiple of exactly one parameter coordinate. We may write
\[
u_i=c_i t_{g(i)},\qquad c_i\in\mathbb F_q^\times,
\]
for a surjection \(g:\{1,\ldots,n\}\to\{1,\ldots,d\}\). Its nonempty fibers \(B_j=g^{-1}(j)\) partition the edge positions. Their membership can be recovered intrinsically from which nonzero coordinate functionals are proportional, so the unlabeled partition does not depend on the chosen parametrization. Substituting into the defining equation of \(H\) gives, for all nonzero \(t_j\),
\[
\left(\prod_{i\ \mathrm{odd}}c_i\right)
\prod_{j=1}^{d}t_j^{a_j}
=
\left(\prod_{i\ \mathrm{even}}c_i\right)
\prod_{j=1}^{d}t_j^{b_j},
\]
where \(a_j\) and \(b_j\) count odd and even positions in block \(j\). Since \(\mathbb F_q^\times\) is cyclic of order \(Q\), this identity holds for *all* \(t\) if and only if \(a_j-b_j\equiv0\pmod Q\) for every \(j\) and \(\prod_{i\ \mathrm{odd}}c_i=\prod_{i\ \mathrm{even}}c_i\). Conversely, these two conditions produce precisely the extremal planes. In particular every admissible block has size at least two (a singleton has imbalance \(\pm1\)), so equality is impossible for \(d>k\). This explains why the proved exact hierarchy begins at \(r=k\).

**5. Counting the extremal planes and subcodes.** Fix one admissible unlabeled partition into \(d\) blocks and order the blocks once. The nonzero scalar choices \((c_1,\ldots,c_n)\) satisfying the single multiplicative product equation number exactly \(Q^{n-1}\): any \(n-1\) scalars determine the last. Replacing all \(c_i\) in block \(j\) by \(\lambda_j c_i\), with \(\lambda_j\in\mathbb F_q^\times\), does not change the plane \(U\), and preserves the product equation since \(a_j-b_j\) is divisible by \(Q\). This action is free, of order \(Q^d\). Conversely, two such parametrizations of the same plane and same intrinsic partition differ only by these scalings. Hence the number of distinct extremal planes for each partition is \(Q^{n-d-1}\). Orthogonal annihilation is a bijection between these planes and dimension-\(r\) coefficient subspaces, proving the stated extremizer count.

To obtain the explicit multinomial sum, label the \(d\) blocks temporarily. For prescribed odd and even occupancies \((a_j,b_j)\), the numbers of ways to distribute the labeled odd and even positions are \(k!/\prod_j a_j!\) and \(k!/\prod_j b_j!\). Divide by \(d!\) to remove block labels. If \(Q>k\), the congruences \(a_j\equiv b_j\pmod Q\) and \(|a_j-b_j|\leq k\) force \(a_j=b_j\geq1\), giving the stable-range simplification. All claimed formulas follow.

## Verification
A standalone Python 3 verifier, `verify.py`, checks independent finite instances using two representations. It enumerates *all* coefficient-annihilator subspaces in reduced row-echelon form for \((q,k)=(3,2),(5,2),(3,3)\), reconstructs edge columns directly from vertex-torus tuples, and checks both the maximum simultaneous zero count and the number of extremizers. Its separate image-hypersurface enumeration covers \((q,k)=(5,3)\) for \(d=1,2\), checking respectively \(3906\) and \(508431\) subspaces. It separately constructs \(96\) distinct extremizers for \((q,k,d)=(5,3,3)\); **this last construction is not an exhaustive search over all planes**. These finite computations returned `VERIFY_OK`. The all-parameter theorem rests on the proof, not on finite enumeration.

## Relationship to prior work
Asensio, Gaggero, Ragunathan, Saha, and Van Tuyl established ordinary weight distributions and minimum distances for edge codes of unicyclic graphs, including even cycles (arXiv:2608.30407v1, especially §4.2, Theorem 4.7). Jaramillo-Velez introduced edge codes and studied basic parameters and tree-code distributions (arXiv:2404.02301v1). Patanker and Singh studied generalized Hamming weights for codes containing *all* square-free monomials of a fixed degree, rather than the sparse even-cycle edge-monomial subspace (arXiv:2002.10920v4). González Sarabia, Camps, Sarmiento, and Villarreal obtained general projective-torus results and second generalized weights for complete bipartite graph parameterizations (arXiv:1611.06405v2). Those statements do not provide this cycle-family higher-dimensional subcode-support hierarchy together with its exact extremizer classification. The first generalized weights and ordinary code construction are not claimed as new.

## Limitations
The exact generalized weights for \(1\leq r<k\) are not determined here; only strict nonattainment of the elementary projection bound follows from Step 4. The complete subcode-support distribution away from minima is also not determined. No probabilistic performance or independent external validation is asserted. Although the specific published statements inspected do not imply the theorem, an equivalent general toric-configuration or finite-geometry formulation elsewhere cannot be ruled out solely by the searches performed.

## References
1. S. Asensio, G. Gaggero, N. Ragunathan, A. Saha, A. Van Tuyl, *Edge codes constructed from unicyclic graphs*, arXiv:2608.30407v1, 2026-08-31. https://arxiv.org/html/2608.30407v1
2. D. Jaramillo-Velez, *The edge code of hypergraphs*, arXiv:2404.02301v1, 2024-04-02. https://arxiv.org/pdf/2404.02301
3. N. Patanker, S. K. Singh, *Generalized Hamming weights of toric codes over hypersimplices and square-free affine evaluation codes*, arXiv:2002.10920v4. https://arxiv.org/html/2002.10920v4
4. M. González Sarabia, E. Camps, E. Sarmiento, R. H. Villarreal, *The second generalized Hamming weight of some evaluation codes arising from a projective torus*, arXiv:1611.06405v2. https://arxiv.org/pdf/1611.06405
