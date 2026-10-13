# Parity dichotomy for strong odd colorings of bipartite cubelike graphs

## Finding

**Theorem.** Let \(d\ge 1\), let \(V=\mathbb F_2^d\), and let \(\varnothing\ne S\subseteq V\setminus\{0\}\) be a set for which there exists a linear functional \(\ell:V\to\mathbb F_2\) satisfying \(\ell(s)=1\) for every \(s\in S\). Form the simple cubelike Cayley graph \(G=\operatorname{Cay}(V,S)\), in which \(x\sim y\) precisely when \(x+y\in S\). Then

\[
\chi_{\mathrm{so}}(G)=\begin{cases}
2,& |S|\text{ is odd},\\
4,& |S|\text{ is even}.
\end{cases}
\]

The result holds whether or not \(S\) generates \(V\). For even \(|S|\), a four-coloring is explicitly computable from a coordinate subset \(I\): each of the \(2^{|I|}\) coordinate patterns is attained an odd number of times by \(S\), and the four colors are \(\bigl(\ell(x),\mathbf1_{\{x|_I=0\}}\bigr)\). Consequently, for every \(1\le r\le d\) with \(r\) odd, the graph on binary words of length \(d\) adjacent at Hamming distance exactly \(r\) has strong odd chromatic number \(2\) when \(\binom dr\) is odd and \(4\) when it is even.

## Assumptions and scope

A *strong odd coloring* is a proper vertex coloring such that every color appearing in the open neighborhood of any vertex appears there an odd number of times. The minimum number of colors is \(\chi_{\mathrm{so}}\). All graph edges are simple, unordered, and loopless, and no generator is repeated. We use \(\mathbb F_2\) arithmetic, so subtraction and addition coincide. The condition \(\ell(s)=1\) gives a bipartition, since every edge reverses \(\ell\). The graph is \(|S|\)-regular, and \(|S|>0\).

## Proof

**1. Odd valency.** When \(|S|\) is odd, the two values of \(\ell\) give a proper bipartition coloring. Each vertex has \(|S|\) neighbors, all of the opposite color, and this positive count is odd. Thus two colors suffice. At least two are required because the graph has an edge.

**2. A parity-fiber lemma.** Let \(S\) be any nonempty subset of \(\{0,1\}^d\) having even size. For a set of coordinates \(J\subseteq[d]\), define over \(\mathbb F_2\)

\[
a_J=\sum_{s\in S}\prod_{i\in J}s_i.
\]

Here \(a_\varnothing=|S|=0\). At least one \(a_J\) is nonzero: take an element \(s\in S\) with inclusion-maximal support \(J=\operatorname{supp}(s)\); since no *other* member of \(S\) contains that support, \(a_J=1\). Choose \(I\) of minimum cardinality such that \(a_I=1\). It is nonempty, and \(a_J=0\) for every proper subset \(J\subsetneq I\).

For any pattern \(p\in\mathbb F_2^I\), its fiber parity is

\[
\sum_{s\in S}\mathbf1_{\{s|_I=p\}}
=\sum_{s\in S}\prod_{i\in I}(1+s_i+p_i)
=a_I=1\quad\text{in }\mathbb F_2.
\]

Indeed, expanding the product, the sole term with coordinate support \(I\) is \(\prod_{i\in I}s_i\), while every other term has a proper subset of \(I\) and hence sums to zero. Thus *every* pattern on \(I\) occurs an odd number of times among the generators.

**3. Four-color construction at even valency.** Take \(I\) from step 2 and put \(f(x)=\mathbf1_{\{x|_I=0\}}\). For any vertex \(x\), its neighbors are exactly \(x+s\) for \(s\in S\), and

\[
\sum_{s\in S}f(x+s)
=\#\{s\in S:s|_I=x|_I\}\equiv1\pmod2.
\]

Because \(|S|\) is even, the number of neighbors satisfying \(f=0\) is odd as well. Color each vertex by the ordered pair \(c(x)=(\ell(x),f(x))\). Adjacent vertices have opposite first coordinate, so the coloring is proper. All neighbors of a fixed \(x\) lie in one opposite first-coordinate class and divide into *two* second-coordinate classes, each with odd multiplicity. It is therefore strong odd and uses at most four colors.

**4. Excluding three colors at even valency.** Work over \(\mathbb F_2\), and for each \(s\in S\) let \(T_s\) translate functions on \(V\) by \(s\). The adjacency operator is \(A=\sum_{s\in S}T_s\). The translations commute and \(T_s^2=1\), so

\[
A^2=\sum_{s\in S}T_s^2
+\sum_{\{s,t\}\subset S}(T_sT_t+T_tT_s)
=|S|\,\mathrm{Id}=0.
\]

Also \(A\mathbf1=|S|\mathbf1=0\). A proper strong odd coloring with two colors is impossible: at each vertex the entire positive, even-sized neighborhood has one color. A purported three-coloring must therefore use all three colors. At any vertex, at most two distinct colors are available to its neighbors. Since the degree is positive and even, and each neighbor color must appear an odd number of times, *exactly both* available colors occur and both counts are odd. For any one color class with indicator \(x_c\), it follows vertexwise that

\[
Ax_c=\mathbf1+x_c.
\]

Applying \(A\), the left side becomes \(A^2x_c=0\); the right side becomes \(A\mathbf1+Ax_c=\mathbf1+x_c\). Hence \(x_c=\mathbf1\), impossible for a color class in a proper coloring of a graph with an edge. So no three-coloring exists, and \(\chi_{\mathrm{so}}(G)\ge4\). Combined with step 3, this completes the dichotomy.

**5. Odd-distance consequence.** Let \(S\) contain all vectors of Hamming weight \(r\) for odd \(r\). The coordinate-sum linear functional is \(1\) on every generator and \(|S|=\binom dr\). Apply the theorem. By the usual binary binomial-parity criterion, \(\binom dr\) is odd precisely when every one-bit of \(r\) is also a one-bit of \(d\). Indeed, over \(\mathbb F_2[t]\), the identity \((1+t)^{2^j}=1+t^{2^j}\) factors \((1+t)^d\) into one factor for each one-bit of \(d\); uniqueness of binary subset sums identifies exactly the odd coefficients.

## Verification

The standalone standard-library script `verification/check.py` enumerates all \(3,940\) nonempty admissible functional/generator pairs in dimensions \(1\) through \(4\), checks another \(240\) seeded cases in dimensions \(5\) and \(6\), and checks \(20\) odd-distance shells through dimension \(8\). It independently constructs the proposed color classes and directly tests adjacency, neighborhood color multiplicities, odd-fiber claims, and the even-valency square-zero parity identity. Run it from the artifact root using `python3 verification/check.py`; deterministic expected results appear in `verification/output.txt`.

These finite computations are consistency checks, *not* a proof of the theorem for arbitrarily large dimension. The infinite argument is given in steps 1–5.

## Relationship to prior work

Kwon and Park introduced strong odd coloring and proved sparse-graph bounds; their result does not imply a degree-independent exact statement for arbitrary, potentially dense cubelike graphs. Caro, Petruševski, Škrekovski, and Tuza proved broad bounds for graph products, including submultiplicativity, but their product inequalities do not force the above uniform four-color bound for an arbitrary generator set. Later work explicitly determines the hypercube subcase \(S=\{e_1,\ldots,e_d\}\), giving \(2\) for odd dimension and \(4\) for even dimension. **That hypercube subcase is prior work, not claimed as new.** The theorem here instead addresses all bipartite cubelike Cayley graphs, including dependent generator systems and odd Hamming-distance graphs of larger radius.

## Limitations

The hypothesis that all generators lie in an affine hyperplane \(\ell=1\) is essential to the present proof and the stated class. No formula is claimed for nonbipartite cubelike graphs or for arbitrary bipartite Cayley graphs of groups outside elementary abelian \(2\)-groups. Novelty comparisons considered the sources below and related semantic and terminology searches; equivalent older results under other naming conventions cannot be categorically excluded without wider literature review. No independent external audit has been performed.

## References

1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653, initially submitted 22 January 2024. https://arxiv.org/abs/2401.11653
2. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336, initially submitted 3 October 2024, especially Section 4. https://arxiv.org/abs/2410.02336
3. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, *The odd independence number of graphs, I: Foundations and classical classes*, arXiv:2509.20763, initially submitted 25 September 2025, Proposition 26. https://arxiv.org/abs/2509.20763
4. V. Dujmović, P. Morin, and S. Odak, *Odd colourings of graph products*, arXiv:2202.12882, initially submitted 25 February 2022. https://arxiv.org/abs/2202.12882
