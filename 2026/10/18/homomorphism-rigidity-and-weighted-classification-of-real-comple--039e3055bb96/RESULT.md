# Homomorphism rigidity and weighted classification of real complete-multipartite evolution algebras

## Finding

Let \(r,s\ge 2\), let \(\mathbf n=(n_1,\ldots,n_r)\), \(\mathbf m=(m_1,\ldots,m_s)\) have strictly positive integer entries and the same total \(N=\sum_an_a=\sum_bm_b\), and let \(\mathbf c=(c_1,\ldots,c_r)\), \(\mathbf d=(d_1,\ldots,d_s)\) have strictly positive real entries. Define real evolution algebras \(E(\mathbf n;\mathbf c)\) and \(E(\mathbf m;\mathbf d)\) in the manner below. **Every algebra homomorphism between them is either zero or invertible.** All nonzero homomorphisms have the following exhaustive description.

A nonzero homomorphism exists exactly if \(r=s\) and a permutation \(\pi\in S_r\) satisfies \(n_a=m_{\pi(a)}\) for every \(a\), together with the indicated weight condition. If \(r=2\), there is no additional weight restriction. If \(r\ge3\), the ratios \(c_a/d_{\pi(a)}\) must all equal the same \(t>0\). In the latter case every nonzero homomorphism is
\[
f(e_{a,i})=t\sum_{j=1}^{n_a}(O_a)_{ji}e'_{\pi(a),j},\qquad
O_a\in O(n_a),\quad O_a\mathbf 1=\mathbf 1.
\]
If \(r=2\), put \(\beta_a=d_{\pi(a)}/c_a\), and instead use the same formula with part-specific positive factors
\[
t_1=(\beta_1^2\beta_2)^{-1/3},\qquad
 t_2=(\beta_1\beta_2^2)^{-1/3}.
\]
Every choice of admissible \(\pi\) and \(O_a\) gives a homomorphism and therefore an isomorphism. Conversely, every nonzero homomorphism occurs uniquely in this form (with respect to the chosen natural bases).

**Graph corollary.** For any finite complete multipartite graph \(G=K_{n_1,\ldots,n_r}\), its adjacency evolution algebra \(A(G)\) and symmetric-random-walk evolution algebra \(A_{\mathrm{RW}}(G)\) are isomorphic if and only if \(r=2\) or all part sizes are equal; otherwise every homomorphism between them in either direction is zero. This proves the adjacency/random-walk zero-or-isomorphism dichotomy conjectured for singular graphs in [1] throughout the complete-multipartite family. It is not a proof for arbitrary graphs.

## Assumptions and scope

All vector spaces, homomorphisms and dot products are **real**, all weights are strictly **positive**, the two algebras have **equal total finite dimension** \(N\), and each has at least two nonempty parts. These restrictions are essential to the argument: the real inner product forbids cancellation of squared norms, and equality of dimensions forces saturated blockwise orthogonality. We assert no corresponding claim over arbitrary fields, with zero or negative weights, for unequal dimensions, or for disconnected zero-degree graphs.

The source natural basis is \(e_{a,i}\) for \(1\le a\le r\), \(1\le i\le n_a\), with \(e_{a,i}e_{b,j}=0\) when \((a,i)\ne(b,j)\), and
\[
e_{a,i}^2=c_a\sum_{b\ne a}S_b,\qquad S_b=\sum_{j=1}^{n_b}e_{b,j}.
\]
The target natural basis is \(e'_{b,j}\), with analogous blocks \(T_b=\sum_j e'_{b,j}\) and products \((e'_{b,j})^2=d_b\sum_{c\ne b}T_c\). Products are bilinear and commutative but need not be associative. An algebra homomorphism is a real linear map preserving this multiplication. Here \(O(k)\) is the real orthogonal group, and \(\mathbf1\) the all-ones column vector.

## Proof

**1. Independent square classes.** In the target put \(V_b=\sum_{c\ne b}T_c\). These vectors are linearly independent: in the basis \((T_c)\) the coefficient matrix is \(J-I\), with determinant \((-1)^{s-1}(s-1)\ne0\). For vectors \(x,y\) with components \(x^{(b)},y^{(b)}\) in target block \(b\), multiplication is
\[
xy=\sum_{b=1}^s d_b\langle x^{(b)},y^{(b)}\rangle V_b.
\]
Therefore \(xy=0\) if and only if the projections are orthogonal within every target block. Also \(x^2=0\) forces \(x=0\), since \(d_b>0\) and ordinary Euclidean squared norms are nonnegative.

**2. Nonzero homomorphisms are invertible.** Write \(u_{a,i}=f(e_{a,i})\). Distinct \(u_{a,i}\) have orthogonal projections in every target block. If \(u_{a,i}=0\), then the image of its square gives
\[
0=f(e_{a,i}^2)=c_a\sum_{b\ne a}\sum_j u_{b,j}.
\]
The vectors in this sum are pairwise orthogonal with respect to the whole ambient Euclidean inner product, so their sum can vanish only if every term vanishes. Since the complete multipartite graph with at least two parts is connected, this zero propagates along neighbors to every natural-basis image, proving \(f=0\). Thus a nonzero map has \(N\) nonzero columns.

Within target block \(b\) of dimension \(m_b\), there are at most \(m_b\) nonzero projections of distinct columns, by their pairwise orthogonality. Summing these bounds yields at most \(N\) nonzero projections total. Each of the \(N\) nonzero columns contributes at least one, so equality holds. Consequently each column has support in **exactly one** target block, and precisely \(m_b\) columns in target block \(b\) form an orthogonal basis. Hence \(f\) is invertible.

**3. Parts and their sizes are invariants.** The source square algebra has dimension \(r\), spanned by the independent vectors \(\sum_{b\ne a}S_b\), and similarly the target square algebra has dimension \(s\). Invertibility yields \(r=s\). Furthermore, the squares \(e_{a,i}^2\) coincide as \(i\) varies within source part \(a\). Their images are therefore equal, while any nonzero column supported in target block \(b\) has square equal to a strictly positive multiple of \(V_b\). Linear independence of the \(V_b\) forces all columns from a fixed source part into one target part, say \(\pi(a)\), and their norms are equal. The occupancy result from step 2 and \(r=s\) makes \(\pi\) a permutation, with \(n_a=m_{\pi(a)}\). For every \(a\), the block of \(f\) is a positive scalar \(t_a\) times an orthogonal matrix \(O_a\), with \(t_a\) the common column norm.

**4. The common-sum condition and scalings.** Put \(\rho_a=d_{\pi(a)}t_a^2/c_a>0\). Comparing the image and square of \(e_{a,i}\) gives
\[
\sum_{b\ne a} f(S_b)=\rho_a\sum_{b\ne a}T_{\pi(b)}.
\]
Since each \(f(S_b)\) lies in its own target block, this implies \(f(S_b)=\rho_a T_{\pi(b)}\) whenever \(a\ne b\). For \(r\ge3\), any two choices of \(a\) share an available \(b\) distinct from them, hence all \(\rho_a\) are equal to some \(\rho>0\). For \(r=2\), one instead has \(f(S_1)=\rho_2 T_{\pi(1)}\) and \(f(S_2)=\rho_1 T_{\pi(2)}\).

On the other hand, the \(n_b\) columns in target block \(\pi(b)\) are orthogonal, each of norm \(t_b\), and their sum is \(f(S_b)\). Comparing norms with \(\rho_aT_{\pi(b)}\) gives \(t_b=\rho_a\) for each \(a\ne b\), and shows \(O_b\mathbf1=\mathbf1\). In the case \(r\ge3\), all \(t_b=\rho=t\), so \(\rho=d_{\pi(a)}t^2/c_a\) implies \(t=c_a/d_{\pi(a)}\) independently of \(a\). For \(r=2\) one obtains precisely
\[
c_1t_2=d_{\pi(1)}t_1^2,\qquad c_2t_1=d_{\pi(2)}t_2^2,
\]
whose unique positive solution is the displayed cube-root pair.

**5. Converse.** Take any permitted \(\pi\), weights and orthogonal matrices fixing \(\mathbf1\). Distinct natural-basis elements map to vectors with zero product, because their block projections are either disjoint or orthogonal. For a squared basis vector the target product is \(d_{\pi(a)}t_a^2\sum_{b\ne a}T_{\pi(b)}\), whereas the image of its source square is \(c_a\sum_{b\ne a}t_b T_{\pi(b)}\). The weight equations make these equal, proving multiplicativity. Each block is invertible; thus so is the whole map.

**6. Graph corollary.** For the complete multipartite graph on \(N\) vertices, the adjacency weights are \(c_a=1\), while random-walk weights are \(d_a=1/(N-n_a)\). When \(r=2\), the formula gives an isomorphism for arbitrary part sizes, as expected for a biregular graph. When \(r\ge3\), a part permutation preserves the multiset of sizes, and the common-ratio condition requires the degrees \(N-n_a\) to be constant, equivalently all \(n_a\) being equal. If not, no nonzero map exists in either direction (apply the same theorem after swapping source and target). This includes singular graphs with twin vertices.

## Verification

The standalone script `checker.py` requires only Python 3's standard library. Run `python3 checker.py`. It compares the full multiplication tables entrywise for four exact rational isomorphism examples: a non-monomial tripartite block; a reordered part system; a bipartite weight change; and the adjacency/random-walk isomorphism of a balanced, singular, complete tripartite graph. It also computes the determinant of \(J-I\) independently for \(2\le r\le8\). The observed output was `CHECKER_OK: four exact multiplication certificates and square-class independence r=2,...,8`. These checks test examples, **not** the universal theorem; steps 1–6 above provide the proof for arbitrary allowed parameters.

## Relationship to prior work

Cadavid, Rodiño Montoya and Rodríguez [1] prove the adjacency-versus-random-walk dichotomy for nonsingular graphs, prove the existence of an isomorphism for regular or biregular graphs, and explicitly conjecture the dichotomy and zero-map assertion for singular graphs (Conjecture 1). Their Proposition 2.5 establishes a necessity statement assuming an isomorphism is monomial; that restriction cannot simply be invoked for singular graphs, which may admit orthogonal mixing within twin classes. Here the full non-monomial real homomorphism classification establishes that conjectured outcome for all complete-multipartite graphs.

Cadavid, Rodiño Montoya, Rodríguez and Vidal [2] analyze further specified singular graph families, without stating the all-parameter positive-weight multipartite homomorphism theorem. The later study [3] develops graph-evolution automorphism constructions and does not state the complete equal-dimensional homomorphism classification. Some related structure theorems may impose stronger implications in special families; see limitations. This theorem is not asserted as a resolution of Conjecture 1 for arbitrary finite graphs.

## Limitations

The result relies on positive real weights and equal finite dimensions. It does not classify mappings between algebras of different dimension or with mixed-sign/complex weights. Not all group-theoretic consequences of the orthogonal-block description are developed here. Numerical tests are finite examples only. The checked literature does not rule out differently formulated or unindexed prior general theorems; independent expert verification and literature audit have not been performed. The original general conjecture for all singular graphs remains open insofar as the cited sources establish.

## References

[1] P. Cadavid, M. L. Rodiño Montoya and P. M. Rodríguez, *On the isomorphisms between evolution algebras of graphs and random walks*, arXiv:1710.10516 (first public version 2017-10-28), especially Theorem 2.3, Conjecture 1 and Propositions 2.4–2.7. https://arxiv.org/abs/1710.10516

[2] P. Cadavid, M. L. Rodiño Montoya, P. M. Rodríguez and S. J. Vidal, *On some singular graphs with non-isomorphic associated evolution algebras*, arXiv:2405.12341 (2024-05-20). https://arxiv.org/abs/2405.12341

[3] *Group actions and automorphisms of evolution algebras associated to finite graphs*, arXiv:2505.15604 (2025). https://arxiv.org/abs/2505.15604
