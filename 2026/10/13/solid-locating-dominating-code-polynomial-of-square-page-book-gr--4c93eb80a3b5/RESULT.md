# Solid-locating-dominating code polynomial of square-page book graphs
## Finding
For every integer
\[
m\ge1,
\]
let \(B_m\) be the square-page book graph with adjacent spine vertices \(x,y\) and page vertices
\[
U=\{u_1,\ldots,u_m\},\qquad V=\{v_1,\ldots,v_m\},
\]
where the \(i\)-th page is the four-cycle
\[
xu_iv_iyx.
\]

For a code \(C\subseteq V(B_m)\), write
\[
I_C(w)=N[w]\cap C.
\]
A code is solid-locating-dominating when every non-codeword has a nonempty identifying set and, for every two distinct non-codewords \(s,t\),
\[
I_C(s)\setminus I_C(t)\ne\varnothing.
\]

Define the code-size polynomial
\[
\mathcal D_m(z)=\sum_C z^{|C|},
\]
where the sum ranges over all solid-locating-dominating codes of \(B_m\). Then
\[
\boxed{\mathcal D_m(z)=2z^{m+1}(1+z)^m+(m+1)z^{2m}+z^{m+2}(z+2)^m.}
\]

Equivalently, every solid-locating-dominating code belongs to exactly one of the following four families.

1. \(x\notin C\), \(y\in C\), every \(v_i\in C\), and the vertices \(u_i\) are arbitrary.
2. \(y\notin C\), \(x\in C\), every \(u_i\in C\), and the vertices \(v_i\) are arbitrary.
3. \(x,y\notin C\), and every page vertex \(u_i,v_i\) belongs to \(C\).
4. \(x,y\in C\), and either every page pair \(\{u_i,v_i\}\) meets \(C\), or exactly one page pair is disjoint from \(C\) and every other page pair is fully contained in \(C\).

Consequently,
\[
\gamma_{DLD}(B_m)=m+1.
\]
For \(m=1\), there are four minimum codes. For every \(m\ge2\), there are exactly two minimum codes,
\[
\{x,u_1,\ldots,u_m\}
\quad\text{and}\quad
\{y,v_1,\ldots,v_m\}.
\]
The total number of solid-locating-dominating codes is
\[
\mathcal D_m(1)=2^{m+1}+m+1+3^m.
\]

## Assumptions and scope
All graphs are finite, simple, connected, and undirected. The book graph here is the square-page book: all \(m\) copies of \(C_4\) share exactly the spine edge \(xy\). Thus
\[
N[x]=\{x,y\}\cup U,
\qquad
N[y]=\{x,y\}\cup V,
\]
and
\[
N[u_i]=\{u_i,x,v_i\},
\qquad
N[v_i]=\{v_i,u_i,y\}.
\]

The result classifies every solid-locating-dominating code, not merely minimum ones. It uses the standard closed-neighborhood identifying sets associated with solid location-domination.

## Proof
Suppose first that \(x\notin C\). If some \(v_i\notin C\), then
\[
I_C(v_i)=C\cap\{u_i,y\}
\subseteq
C\cap(\{y\}\cup U)=I_C(x).
\]
This contradicts the solid condition for the ordered pair \((v_i,x)\). Hence every \(v_i\) lies in \(C\).

If also \(y\notin C\), then if some \(u_i\notin C\), the already proved membership \(v_i\in C\) gives
\[
I_C(u_i)=\{v_i\}\subseteq I_C(y)=V,
\]
another contradiction. Therefore all page vertices belong to \(C\), giving Family 3.

If instead \(y\in C\), then every \(v_i\in C\) while the \(u_i\) can be chosen independently. To verify sufficiency, the non-codewords are \(x\) and whichever \(u_i\) were omitted. Their identifying sets are
\[
I_C(x)=\{y\}\cup(C\cap U)
\]
and, for every omitted \(u_i\),
\[
I_C(u_i)=\{v_i\}.
\]
The singleton sets \(\{v_i\}\) are pairwise distinct, none is contained in \(I_C(x)\), and \(I_C(x)\) contains \(y\), which is absent from every \(\{v_i\}\). Hence Family 1 is valid. By symmetry, Family 2 is exactly the family obtained when \(y\notin C\) and \(x\in C\).

It remains to consider \(x,y\in C\). Classify each page by its selected page vertices: both selected, only \(u_i\), only \(v_i\), or neither selected. Suppose one page, say page \(i\), has neither page vertex selected. Then
\[
I_C(u_i)=\{x\},
\qquad
I_C(v_i)=\{y\}.
\]
If a vertex \(u_j\) on any other page were also outside \(C\), its identifying set would contain \(x\), so
\[
I_C(u_i)\subseteq I_C(u_j),
\]
which is forbidden. Similarly, no \(v_j\) on any other page can be outside \(C\). Therefore an entirely omitted page is unique and every other page is fully selected. This gives the exceptional part of Family 4. It is valid because its only non-codewords have the incomparable identifying sets \(\{x\}\) and \(\{y\}\).

Finally assume that \(x,y\in C\) and no page is completely omitted. An omitted \(u_i\) has identifying set
\[
I_C(u_i)=\{x,v_i\},
\]
while an omitted \(v_j\) has
\[
I_C(v_j)=\{y,u_j\}.
\]
Two omitted vertices of the same type have distinct page-specific codewords, while two of opposite types differ by the spine codewords \(x\) and \(y\). Hence these identifying sets form an antichain under inclusion, so every selection meeting each page pair is valid. This completes the structural classification.

The polynomial follows by counting the four disjoint families. Families 1 and 2 contribute
\[
2z^{m+1}(1+z)^m.
\]
Family 3 contributes \(z^{2m}\), and the unique-omitted-page subfamily of Family 4 contributes \(mz^{2m}\), giving together
\[
(m+1)z^{2m}.
\]
The no-empty-page subfamily of Family 4 has both spine vertices selected and, independently on each page, one of three states with weight polynomial
\[
2z+z^2.
\]
It therefore contributes
\[
z^2(2z+z^2)^m=z^{m+2}(z+2)^m.
\]
Adding the contributions proves the displayed formula.

For \(m\ge2\), the only term of degree \(m+1\) is the first one, and its coefficient is \(2\). These two minimum codes are obtained by choosing no optional page vertex in Family 1 or Family 2. At \(m=1\), the term \((m+1)z^{2m}\) contributes two additional minimum codes, so the minimum-code count is four.

## Verification
The included checker independently constructs \(B_m\), computes every closed neighborhood, and tests the defining solid-location-domination condition directly on every subset.

For every
\[
1\le m\le8,
\]
it compares the exact set of accepted codes against a separately generated structural family and compares every coefficient by code size with the closed polynomial. In total it checks \(349{,}520\) vertex subsets. It also verifies the minimum value and the minimum-code counts for each tested \(m\).

The finite check is corroborative only. The result for arbitrary \(m\) follows from the structural proof above.

## Relationship to prior work
The 2018 paper introducing self- and solid-locating-dominating codes defines the same solid condition through identifying sets and studies optimal codes in rook graphs and binary Hamming spaces. Its published scope does not include square-page books or generalized theta graphs, and it does not enumerate all solid-locating-dominating codes by cardinality.

A 2019 continuation develops general structural bounds, trees, Cartesian products, ladders, and selected rook graphs. In particular, it proves the Dilworth-number lower bound
\[
|V(G)|-\nabla(G)\le\gamma_{DLD}(G),
\]
where \(\nabla(G)\) is the Dilworth number of the vicinal preorder. This general inequality does not determine the book value or the all-code polynomial. The inspected full text contains no occurrence of “book” or “theta”.

Later work continues the same code family on other graph classes, including Hamming and grid-type settings. Targeted literature and database searches under solid-location-domination, book-graph, generalized-theta, and polynomial/enumerator terminology did not locate a statement implying the structural four-family classification or the closed polynomial above.

## Limitations
The theorem is for the square-page book graph whose pages are four-cycles sharing one edge. It does not assert an analogous formula for triangular books, longer-cycle books, or arbitrary generalized theta graphs.

The finite checker covers \(1\le m\le8\) only and is not used as an infinite proof.

The originality search cannot exclude a differently named or non-indexed all-code enumeration that does not use standard solid-location-domination or book-graph terminology.

## References
1. V. Junnila, T. Laihonen, T. Lehtilä, “On regular and new types of codes for location-domination,” Discrete Applied Mathematics 247 (2018), 225–241, DOI 10.1016/j.dam.2018.03.050; available online 13 April 2018.
2. V. Junnila, T. Laihonen, T. Lehtilä, M. L. Puertas, “On Stronger Types of Locating-dominating Codes,” Discrete Mathematics and Theoretical Computer Science 21(1) (2019), article 1, arXiv:1808.06891, DOI 10.23638/DMTCS-21-1-1.
3. V. Junnila, T. Laihonen, T. Lehtilä, “New Optimal Results on Codes for Location in Graphs,” arXiv:2306.07862v1 (2023), later Fundamenta Informaticae, DOI 10.46298/fi.11468.
