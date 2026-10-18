# Uniform integral homotopy and permutation characters of multipartite path-free complexes

## Finding

For a complete multipartite graph \(G=K_{n_1,\ldots,n_m}\) with \(m\ge3\) nonempty parts, \(N=\sum_i n_i\), and \(5\le t\le N\), let \(\operatorname{PF}_t(G)\) consist of vertex sets whose induced graph has **no simple path on \(t\) distinct vertices** (the path need not be induced). Set \(h=\lfloor t/2\rfloor-1\) and
\[
R(\mathbf n,t)=\binom{N-1}{t-1}-\sum_{i=1}^m\sum_{q=0}^{h}\binom{N-n_i}{q}\binom{n_i-1}{t-1-q},
\]
where out-of-range binomial coefficients are zero. Then \(R(\mathbf n,t)\) is a nonnegative integer and
\[
\operatorname{PF}_t(G)\simeq\bigvee^{R(\mathbf n,t)}S^{t-2}.
\]
A zero-fold wedge means a point. In particular its reduced integral homology is free, concentrated in degree \(t-2\), and of rank \(R(\mathbf n,t)\). As a concrete nonbipartite example, the sphere multiplicities for \(K_{4,3,2}\) at thresholds \(t=5,6,7,8,9\) are respectively \(65,46,28,8,1\), in degrees \(3,4,5,6,7\).

There is also a natural *integral equivariant presentation*. Let \(\Gamma=\prod_iS_{n_i}\) permute vertices within the parts, let \(B=\operatorname{sk}_{t-2}\Delta(V(G))\), and let \(A_i\) be the \(i\)-th part, \(W_i=V(G)\setminus A_i\), and \(C_i=\Delta(A_i)*\operatorname{sk}_{h-1}\Delta(W_i)\). Then inclusion gives a \(\Gamma\)-equivariant short exact sequence of free abelian groups
\[
0\longrightarrow \bigoplus_{i=1}^m\widetilde H_{t-2}(\operatorname{sk}_{t-2}C_i;\mathbb Z)
\longrightarrow\widetilde H_{t-2}(B;\mathbb Z)
\longrightarrow\widetilde H_{t-2}(\operatorname{PF}_t(G);\mathbb Z)\longrightarrow0.
\]

The entire rational homology character can be evaluated from permutation cycle lengths. For \(g\in\Gamma\), let \(\lambda_i(g)\) be the multiset of lengths of cycles on \(A_i\), and set
\[
P_i(z)=\prod_{\ell\in\lambda_i(g)}(1-z^\ell),\qquad P(z)=\prod_iP_i(z),\qquad P_{-i}(z)=\prod_{j\ne i}P_j(z).
\]
Writing \([z^j]Q\) for a coefficient, the character in degree \(t-2\) is
\[
\begin{aligned}
\chi_t(g)=(-1)^{t-1}\Bigg(&\sum_{j=0}^{t-1}[z^j]P(z)\\
&+\sum_{i=1}^m\sum_{q=0}^{h}[z^q]P_{-i}(z)\sum_{p=t-q}^{n_i}[z^p]P_i(z)\Bigg).
\end{aligned}
\]
The result describes the character for *every* element of the product group, not merely a trace for selected generators.

## Assumptions and scope

All graphs are finite, simple, undirected, and complete multipartite with disjoint nonempty parts. A path here is an ordinary (not necessarily induced) subgraph path. We require \(m\ge3\), \(N\ge t\ge5\); smaller-threshold and bipartite cases are not claimed as new. The geometric realization of the abstract simplicial complex is used. Homology has integer coefficients unless otherwise indicated. All displayed direct sums and module maps respect the class-preserving permutation action. The theorem does not assert an equivariant homotopy equivalence to a wedge with any chosen group action.

## Proof

**1. Exact face classification.** Consider a vertex set \(S\), with \(a\) the maximum number of vertices in a single part and \(b=|S|-a\). The maximum length in vertices of a simple path in the complete multipartite induced graph is \(\min\{|S|,2b+1\}\). The upper bound follows because each vertex in a largest part must be separated from the next by one of the \(b\) outside vertices. For attainability, when \(a>b+1\), alternate all outside vertices with \(b+1\) vertices from the largest part. When \(a\le b+1\), rearrange the multiset of part labels without equal consecutive labels (the usual necessary-and-sufficient maximum-multiplicity criterion), yielding a path using all \(|S|\) vertices. Consequently \(S\) has no path of length \(t\) vertices precisely if \(|S|\le t-1\), or some part contains all but at most \(h\) vertices of \(S\). Thus
\[
K=\operatorname{PF}_t(G)=B\cup\bigcup_{i=1}^m C_i,
\]
with \(B,C_i\) as stated in the finding.

**2. Disjoint top-dimensional supports.** Each \(C_i\) is contractible: \(\Delta(A_i)\) is a nonempty simplex, hence its join with any complex is a cone. Every simplex with at least \(t\) vertices belongs to at most one \(C_i\): belonging to \(C_i\) implies at least \(|S|-h\) vertices in \(A_i\), and \(2(|S|-h)>|S|\) for \(|S|\ge t\). More strongly, the \((t-2)\)-simplices of \(\operatorname{sk}_{t-2}C_i\) and \(\operatorname{sk}_{t-2}C_j\) are disjoint for \(i\ne j\). Such a simplex has \(t-1\) vertices, at least \(t-1-h\) of them in its designated part, and \(2(t-1-h)>t-1\).

**3. Exact relative homology.** Put \(d=t-2\). The relative simplicial chain complex \(C_*(K,B)\) splits as \(\bigoplus_i C_*(C_i,\operatorname{sk}_d C_i)\), because all simplices above dimension \(d\) lie in exactly one \(C_i\), as do their faces above that dimension. Since each \(C_i\) is contractible and \(\operatorname{sk}_dC_i\) has precisely the same cells through dimension \(d\), its only possibly nonzero reduced homology is in degree \(d\). Hence the only nonzero relative group is
\[
H_{d+1}(K,B)\cong\bigoplus_i\widetilde H_d(\operatorname{sk}_dC_i;\mathbb Z).
\]
The full simplex skeleton \(B\) likewise has only \(\widetilde H_d(B;\mathbb Z)\cong\mathbb Z^{\binom{N-1}{d+1}}\). The connecting map in the pair sequence is precisely inclusion of the top-dimensional simplicial cycles. By the disjoint support proved in step 2, this map is injective: neither \(B\) nor any \(\operatorname{sk}_d C_i\) has \((d+1)\)-simplices, so their top homology groups are literally kernels of their \(d\)-boundary operators inside groups of \(d\)-chains. The long exact sequence gives the displayed equivariant sequence and proves that all reduced homology of \(K\) outside degree \(d\) vanishes.

**4. No torsion.** The sublattice \(\widetilde H_d(\operatorname{sk}_d C_i;\mathbb Z)=\ker\partial_d\) is saturated in the free abelian group on the \(d\)-simplices of \(C_i\), since the target of \(\partial_d\) is torsion-free. Different \(i\) have disjoint top-face supports, so the sum of these kernels is saturated in the free \(d\)-chain group of \(B\). It follows that \(\widetilde H_d(B;\mathbb Z)\) modulo their direct sum embeds into a torsion-free quotient of the whole \(d\)-chain group. Thus \(\widetilde H_d(K;\mathbb Z)\) is free.

**5. Exact rank.** Write \(a=n_i\), \(b=N-a\), and \(r=t-1=d+1\). The number of \((j-1)\)-simplices of \(C_i\) is \(\sum_{q=0}^{h}\binom bq\binom a{j-q}\). The top-skeleton homology rank, from its truncated Euler characteristic and the alternating-binomial identity \(\sum_{p=0}^u(-1)^p\binom ap=(-1)^u\binom{a-1}{u}\), is
\[
\operatorname{rank}\widetilde H_d(\operatorname{sk}_d C_i;\mathbb Z)
=\sum_{q=0}^{h}\binom bq\binom{a-1}{r-q}.
\]
Subtracting these ranks from \(\binom{N-1}{r}\) gives \(R(\mathbf n,t)\).

**6. Homotopy type.** The full \(d\)-skeleton of an \((N-1)\)-simplex is simply connected for \(d\ge2\). Every \(C_i\) is contractible, and its intersection with \(B\) is its \(d\)-skeleton, which is connected. Attaching the \(C_i\) successively preserves simple connectivity by van Kampen; at each step the intersection is the connected \(\operatorname{sk}_d C_i\) (other \(C_j\) add no new simplices to that intersection beyond dimension \(d\)). Thus \(K\) is simply connected. Choose maps of \(R\) copies of \(S^d\) representing an integral basis of \(H_d(K)\), possible by Hurewicz because \(K\) has the same \((d-1)\)-connectivity as \(B\). The resulting map \(\bigvee^R S^d\to K\) is an integral homology isomorphism. The homological Whitehead theorem for simply connected CW complexes makes it a homotopy equivalence. When \(R=0\), the same theorem makes \(K\) contractible.

**7. Complete rational character.** Each \(g\)-fixed oriented simplex corresponds to a union of permutation cycles. If it uses \(c\) cycles and \(j\) vertices, its orientation sign is \((-1)^{j-c}\). Its contribution to the signed augmented simplicial Euler trace with degree convention \((-1)^j\) is therefore \((-1)^c\). The polynomial \(P_i(z)\) enumerates exactly these signed cycle unions in part \(A_i\) by cardinality. Split allowable unions into those of size at most \(t-1\), counted by the first sum, and those of size at least \(t\), which have a **unique** majority part \(i\), counted by the second sum with at most \(h\) outside vertices. Since reduced homology is concentrated in dimension \(t-2\), the Hopf trace identity multiplies this augmented signed Euler trace by \((-1)^{t-1}\). This is the stated character formula.

## Verification

Two standalone standard-library Python programs accompany this result. `pft_general_verify.py` compares the majority characterization against direct depth-first enumeration of forbidden simple paths, then calculates every mod-two simplicial boundary rank. It passed 67 graph/threshold instances on multipartite graphs having up to nine vertices, with all predicted homology profiles. `pft_symmetry_verify.py` independently compares the signed count of invariant faces with the stated cycle-polynomial formula for every class-preserving permutation of five small multipartite graphs, a total of 1,008 comparisons. The packaged text files record exact command output. These finite checks do not prove the infinite theorem; steps 1–7 above supply the proof over \(\mathbb Z\) and \(\mathbb Q\).

## Relationship to prior work

Deshpande, Goyal, and Sawant (arXiv:2607.05358, first public July 6, 2026) supply the motivating multipartite path-free structural decomposition and a complete homotopy treatment for **complete bipartite graphs**. Their reported decomposition is used as a starting point but was also rederived in step 1. The contribution here is the uniform all-threshold sphere-wedge classification for arbitrary numbers \(m\ge3\) of parts, a saturated integral homology quotient, and a closed character formula for the complete class-preserving permutation group. The full primary manuscript was not accessible during this comparison; its full body could conceivably contain a more general result than its available abstract and secondary summary indicate. The earlier work of Grinberg, Katthän, and Lewis concerns a different edge-subset directed source-to-target path-free construction and does not directly give these vertex-subset formulas.

## Limitations

No claim of novelty is made for the complete bipartite case, thresholds below five, or any equivalent result that may be in a currently inaccessible manuscript. The integral module is presented as a quotient, not decomposed into irreducible integral representations (which need not split integrally). The sphere-wedge equivalence is nonequivariant, while the character is rational and the short exact sequence is integral and equivariant. No independent external mathematical audit has been conducted.

## References

1. P. Deshpande, S. Goyal, and R. Sawant, *On a complete characterization of path-free complexes associated with complete multipartite graphs*, arXiv:2607.05358 (first posted July 6, 2026), https://arxiv.org/abs/2607.05358 .
2. D. Grinberg, L. Katthän, and J. B. Lewis, *The path-missing and path-free complexes of a directed graph*, arXiv:2102.07894 (2021), https://arxiv.org/abs/2102.07894 .
