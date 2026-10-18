# Uniform integral homotopy classification of cyclic clique expansions

## Finding
For integers \(n\ge7\), \(m\ge2\), let \(C_n[K_m]\) be the lexicographic graph product, and set \(X_{n,m}=\operatorname{Ind}(C_n[K_m])\). Thus \(C_n[K_m]\) has vertices \((i,c)\), with \(i\in\mathbb Z/n\mathbb Z\), \(1\le c\le m\). Vertices are adjacent when their cycle indices agree and colors differ, or their cycle indices are consecutive (regardless of colors). Its independent sets choose at most one colored vertex from each selected cycle position and no two consecutive cycle positions.

All these complexes have integral homotopy types of wedges of spheres. Write \(X_{n,m}\simeq\bigvee_{d\ge0}\bigvee^{r_d}S^d\). Initialize the nonnegative integers \(r_d\) from the base cycle:
\[
\begin{array}{c|c}
 n=3k&r_{k-1}=2\\
 n=3k+1&r_{k-1}=1\\
 n=3k+2&r_k=1.
\end{array}
\]
When \(n=3k\), increase \(r_{k-1}\) by \(3(m^k-1)\). For every integer \(t\) satisfying
\[
1\le t\le\lfloor n/2\rfloor,\quad n+t\equiv0\pmod3,\quad h=(n+t)/3\ge t,
\]
increase \(r_{h-1}\) by the integer
\[
B_{n,m}(t)=\frac nt\binom{h-1}{t-1}(m-1)^t m^{h-t}.
\]
All other multiplicities are zero; multiplicities in equal degrees are added. In particular,
\[
\begin{aligned}
X_{7,2}&\simeq S^1\vee\bigvee^{14}S^2,\\
X_{8,2}&\simeq\bigvee^{33}S^2\vee\bigvee^2S^3,\\
X_{9,2}&\simeq\bigvee^{23}S^2\vee\bigvee^{18}S^3,\\
X_{7,3}&\simeq S^1\vee\bigvee^{84}S^2.
\end{aligned}
\]

## Assumptions and scope
Graphs are finite, undirected, and simple. The lexicographic product is **not** the categorical/tensor product or the Cartesian product. All homotopy equivalences are ordinary integral homotopy equivalences of geometric realizations. The restriction \(n\ge7\) guarantees the original cycle independence complex is connected and gives a parameter range distinct from the previously calculated six-cycle geometric-quotient case. The theorem concerns positive integer multiplicity \(m\ge2\), not arbitrary topological fibers.

We use the standard augmented simplicial join convention: the face complex \(\{\varnothing\}\) is the formal \((-1)\)-sphere for join calculations; its join is an identity. Empty links produce a sphere in degree one below their suspension exponent.

## Proof
**1. A vertex-replication splitting.** Let \(K\) be any finite simplicial complex on a vertex set containing \(v\), and replace \(v\) by \(m\) distinct clones with no two clones permitted in one face. Write \(L=\operatorname{lk}_K(v)\). The original \(K\) contains the cone \(v*L\). Each extra clone adds another cone on \(L\). Since \(L\hookrightarrow K\) factors through \(v*L\), its attaching map is nullhomotopic. The mapping-cone pushout therefore has homotopy type
\[
 K^{(m)}_v\simeq K\vee\bigvee^{m-1}\Sigma L.
\]
For the augmented link \(L=\{\varnothing\}\), a new clone is an isolated vertex, which agrees with the formula using the reduced \((-1)\)-sphere convention. For nonempty links the ordinary unreduced suspension appears. This argument also applies to disconnected intermediate links: suspending their cone attachments is the same mapping-cone construction. The exact suspension is based at the original cone point, so there is no connectivity assumption on \(L\).

Replicate the vertices of \(K\) one by one. Taking a link and replicating a distinct vertex commute: \(\operatorname{lk}_{K^{(m)}_w}(v)=(\operatorname{lk}_K(v))^{(m)}_w\) for \(v\ne w\). Repeatedly applying the preceding splitting, including to suspended links, proves by induction the full formula
\[
 K^{[m]}\simeq K\vee\bigvee_{\varnothing\ne S\in K}
 \bigvee^{(m-1)^{|S|}}\Sigma^{|S|}\operatorname{lk}_{K}(S).
\tag{1}
\]
Here the outer index runs over nonempty simplices \(S\) of \(K\); when a link is contractible its summand is contractible, and when the link has only the empty face the summand is \(S^{|S|-1}\). The based splitting is valid in the present application because \(K=\operatorname{Ind}(C_n)\) is connected for \(n\ge7\). By definition of the lexicographic product, \(K^{[m]}=\operatorname{Ind}(C_n[K_m])\) as simplicial complexes.

**2. Compute every link.** Write a nonempty independent set \(S\) of the cycle as \(s\) cyclically ordered selected vertices with positive cyclic gaps \(g_1,\ldots,g_s\). These satisfy \(g_i\ge2\) and \(\sum_i g_i=n\). Removing each selected vertex and both its cycle neighbors leaves exactly the disjoint union of paths with \(\max(g_i-3,0)\) vertices. Therefore,
\[
\operatorname{lk}_{\operatorname{Ind}(C_n)}(S)
=\operatorname{Ind}(C_n-N[S])
=\mathop{\ast}\limits_{i=1}^{s}\operatorname{Ind}(P_{\max(g_i-3,0)}).
\tag{2}
\]
The standard path calculation is \(\operatorname{Ind}(P_{3a})\simeq S^{a-1}\), \(\operatorname{Ind}(P_{3a+1})\simeq\mathrm{pt}\), \(\operatorname{Ind}(P_{3a+2})\simeq S^a\), taking \(P_0\) as the augmented join unit. Hence a term of (1) vanishes precisely when at least one gap is congruent to \(1\) modulo \(3\). In a surviving term every gap has the form \(3a_i\) with \(a_i\ge1\) or \(3a_i+2\) with \(a_i\ge0\). Let \(t\) count the gaps of the second kind and set \(h=(n+t)/3\), so \(\sum_i a_i=h-t\), and \(s\le h\). The join in (2) is a sphere of dimension \(h-s-1\). The suspension in (1) has sphere dimension exactly \(h-1\).

**3. Count surviving colored gaps.** For fixed \(s,t\) with \(t\le s\le h\), choose the \(t\) gaps of the second type in \(\binom{s}{t}\) ways. Writing the first-type coefficients as \(a_i=1+b_i\) and second-type as \(a_i=b_i\), the nonnegative \(b_i\) sum to \(h-s\), giving \(\binom{h-1}{s-1}\) choices. A choice of starting vertex and ordered gaps labels each independent set exactly \(s\) times, so the number of such \(S\) is
\[
 N_{n,s,t}=\frac ns\binom{s}{t}\binom{h-1}{s-1}.
\tag{3}
\]
Each carries \((m-1)^s\) copies of the sphere. For \(t\ge1\), the identities
\[
\frac1s\binom st=\frac1t\binom{s-1}{t-1},\qquad
\binom{s-1}{t-1}\binom{h-1}{s-1}
=\binom{h-1}{t-1}\binom{h-t}{s-t}
\]
and the binomial theorem yield the exact total multiplicity
\[
 \sum_{s=t}^{h}N_{n,s,t}(m-1)^s
 =\frac nt\binom{h-1}{t-1}(m-1)^t m^{h-t}=B_{n,m}(t).
\tag{4}
\]
For \(t=0\), necessarily \(n=3h\). Summing (3) with \(t=0\) and \(s\ge1\) gives
\[
\sum_{s=1}^{h}\frac ns\binom{h-1}{s-1}(m-1)^s
 =\frac nh\sum_{s=1}^{h}\binom hs(m-1)^s=3(m^h-1).
\tag{5}
\]

**4. Add the original cycle.** The classical cycle calculation is
\[
\operatorname{Ind}(C_{3k})\simeq S^{k-1}\vee S^{k-1},\quad
\operatorname{Ind}(C_{3k+1})\simeq S^{k-1},\quad
\operatorname{Ind}(C_{3k+2})\simeq S^k.
\]
Substituting (2)--(5) into the homotopy splitting (1) gives the claimed integer sphere multiplicities in every degree. Since these are homotopy equivalences built using honest cones and joins, the result includes the absence of integral torsion. \(\square\)

## Verification
The included standalone script `verify.py` computes the predicted wedge ranks symbolically and then constructs all faces of the actual lexicographic-product independence complex. For \((n,m)=(7,2),(8,2),(9,2),(7,3)\), it checks the exact face vector against \(\frac{n}{n-j}\binom{n-j}{j}m^j\) for each valid size \(j\), computes all reduced simplicial homology dimensions over \(\mathbb F_2\) by bit-exact Gaussian elimination, and compares with the theorem's multiplicities. This finite cross-check is supplementary and is *not* the proof of the infinite-parameter statement; that proof is given above.

## Relationship to prior work
Okura's March 2023 polyhedral-join theorem applies to forest-based independence complexes and computes lexicographic-product examples over paths. Cycles are not forests; the explicit all-\(n\), all-\(m\) cyclic binomial multiplicity and integral homotopy formula here are not stated in the inspected paper. Earlier work on vertex expansions establishes combinatorial-algebraic behavior (for example shellability), not this cyclic homotopy classification. Known homotopy types for the categorical product \(C_n\times K_m\) and the Cartesian product \(C_n\square K_m\) concern graphs with different adjacencies, so they neither cover nor imply the formula above.

## Limitations
The classification is restricted to \(n\ge7\), complete fiber graphs, and uniform fiber size \(m\ge2\). It does not determine equivariant actions of graph automorphisms or general graph fibers. No independent mathematical audit has yet been carried out; unindexed equivalent previous work remains possible. The finite script verifies only four parameters and cannot replace the all-parameter argument.

## References
1. K. Okura, *On the Homotopy Type of the Polyhedral Join over the Independence Complex of a Forest*, arXiv:2303.11984v1, publicly posted 2023-03-21, https://arxiv.org/abs/2303.11984.
2. K. Okura, *Independence Complex of the Lexicographic Product of a Forest*, arXiv:2109.04181v1, publicly posted 2021-09-09, https://arxiv.org/abs/2109.04181.
3. K. N. Vander Meulen and A. Van Tuyl, *Shellability, vertex decomposability, and lexicographical products of graphs*, arXiv:1505.02838, https://arxiv.org/abs/1505.02838.
4. S. Moradi and F. Khosh-Ahang, *Expansion of a simplicial complex*, arXiv:1601.00456, https://arxiv.org/abs/1601.00456.
5. Standard path and cycle independence-complex calculations, as cited and used in references 1--2.
