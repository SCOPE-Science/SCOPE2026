# The majority C-colouring spectrum of square-page book graphs

## Finding
For every integer \(b\ge1\), let \(B_b=K_2\square K_{1,b}\) be the graph with two spine vertices \(s_0,s_1\) and, for each page index \(1\le i\le b\), two further vertices \(u_i,v_i\), with edges \(s_0s_1\), \(s_0u_i\), \(u_iv_i\), and \(v_is_1\). A majority C-colouring partitions its vertices into nonempty colour classes so that every vertex has at least half its (open) neighbours in its own class. No proper-colouring restriction is imposed.

Write \(P_{b,k}\) for the number of such **unlabelled colour partitions** into exactly \(k\) classes. Define \(S(j,r)\) as a Stirling number of the second kind, with \(S(0,0)=1\) and \(S(j,r)=0\) outside \(0\le r\le j\). Put \(L=\lfloor b/2\rfloor\) and \(H=L+1\). Then for all \(k\ge1\),
\[
P_{b,k}=\sum_{t=L}^{b}\binom bt S(b-t,k-1)
+\sum_{\substack{p,x,y,z\ge0,\\p+x+y+z=b,\\p+x\ge H,\ p+y\ge H}}
\frac{b!}{p!x!y!z!}\,S(z,k-2).
\]
Consequently the majority C-chromatic number and number of unlabelled optimal partitions are, respectively,
\[
\overline\chi_{\ge}(B_b)=1+\left\lceil\frac b2\right\rceil,
\qquad P_{b,\,1+\lceil b/2\rceil}=\binom{b+1}{\lfloor b/2\rfloor+1}.
\]
For a palette of exactly \(k\) named colours all of which must occur, the number of surjective majority C-colourings is \(k!P_{b,k}\). Thus the formula determines the complete feasible-colour spectrum and every associated named-colouring count, not just its maximum.

Every optimal partition is of precisely one of the following two forms. (A) Both spine vertices have one colour; exactly \(L\) complete pages have that colour, and each remaining complete page has its own different colour. (B) The spine vertices have two different colours; exactly \(H\) pages have their respective adjacent-spine colours at opposite ends, and each other complete page has its own non-spine colour. The two types contribute \(\binom bL\) and \(\binom bH\) optimal partitions.

## Assumptions and scope
All graphs are finite, simple and undirected. The parameter \(b\) is an arbitrary integer at least one. The two spine vertices and the page indices are distinguished by the given graph construction, but colours are unlabelled in \(P_{b,k}\). The majority condition uses the *open* neighbourhood, so the spine threshold is \(H=\lceil(b+1)/2\rceil\), whereas each page vertex has degree two and therefore must share its colour with at least one neighbour. The theorem describes all possible numbers of colours \(k\), including \(k=1\) and values outside the feasible range, where the formula gives zero.

## Proof
Fix a majority C-colouring. Write \(X\) for the colour of \(s_0\), and \(Y\) for the colour of \(s_1\).

**Case 1: \(X=Y\).** Each page vertex has exactly two neighbours. If either vertex in a page differs from \(X\), its neighbour toward its incident spine has a different colour, forcing the other page vertex to have the same colour as it. Conversely, if both page vertices have colour \(X\), or both have some common colour different from \(X\), the degree-two requirements hold. Therefore every page is monochromatic and its colour may be \(X\) or another colour. Let \(t\) be the number of pages of colour \(X\). Each spine has exactly \(t+1\) same-colour neighbours among its \(b+1\) neighbours, so its majority condition is precisely \(t+1\ge\lceil(b+1)/2\rceil\), equivalently \(t\ge L\). Choose those \(t\) page indices in \(\binom bt\) ways. The other \(b-t\) full pages may be partitioned into exactly \(k-1\) nonempty non-spine colour classes in \(S(b-t,k-1)\) ways. This is exactly the first displayed sum, with no duplication.

**Case 2: \(X\ne Y\).** For each page, the degree-two conditions force exactly one of four types: \((X,Y)\), \((X,X)\), \((Y,Y)\), or \((Z,Z)\) for some colour \(Z\notin\{X,Y\}\). Indeed, a page vertex that disagrees with the colour of its adjacent spine must agree with its other page vertex; applying this to both ends proves the list. Conversely each listed type satisfies both page-vertex majority conditions. Let the numbers of the four types be \(p,x,y,z\), respectively. The spine vertex \(s_0\) has \(p+x\) matching neighbours and \(s_1\) has \(p+y\), as their common spine edge is heterochromatic. Therefore both spine conditions hold exactly when \(p+x\ge H\) and \(p+y\ge H\). A fixed feasible quadruple produces \(b!/(p!x!y!z!)\) choices of type-labelled page indices. Its \(z\) remaining monochromatic non-spine pages can be partitioned into \(k-2\) nonempty colour classes in \(S(z,k-2)\) ways. The spine colours \(X\) and \(Y\) are distinguished by their vertices, even though their names are not: the two spine-containing colour classes are uniquely identifiable. This proves the second sum and the exact count without overcounting.

In Case 1, the number of colours is at most \(1+(b-t)\le1+b-L=1+\lceil b/2\rceil\). Equality forces \(t=L\) and gives type (A). In Case 2, the inequalities imply \(p+x+y\ge H\), hence \(z\le b-H\). There are at most \(2+z\le2+b-H=1+\lceil b/2\rceil\) colours. To attain equality one must have \(z=b-H\) and every non-spine page in its own class; now \(p+x+y=H\) together with \(p+x,p+y\ge H\) forces \(x=y=0\), so \(p=H\), giving type (B). Both types are actual colourings for each \(b\ge1\), establishing the maximum and the full extremal classification. Their respective counts add to \(\binom bL+\binom bH=\binom{b+1}H\) by Pascal's identity. Every unlabelled partition with \(k\) nonempty blocks has exactly \(k!\) surjective assignments of \(k\) named colours. QED.

## Verification
The accompanying standalone `verify.py` constructs the actual adjacency lists of \(B_b\) and enumerates **all set partitions of the vertex set** for \(1\le b\le4\), testing each vertex's open-neighbourhood majority directly. It compares the resulting colour-count spectrum with an independent implementation of both Stirling-number sums, and checks the maximum and extremal count. An additional arithmetic check verifies the extremal identities through \(b=20\). Run `python3 verify.py`; the included `verify_output.txt` reports all outputs. These finite checks corroborate but do not replace the proof for unbounded \(b\).

## Relationship to prior work
Bujtás, Dettlaff, Furmańczyk and Laskowska introduced the majority C-colouring terminology and its graph invariant in 2026 [1]. The underlying local condition was also studied earlier as a sum-satisfactory multi-partition and as partitioning into defensive zero-alliances; these are **equivalent formulations, not separate inventions** [1,3]. Their subsequent 2026 investigation of Cartesian products [2] gives general bounds and exact values for other product families, but not a formula for the entire colour-partition spectrum of \(K_2\square K_{1,b}\).

Yero and collaborators [3] discuss the particular graph \(K_{1,4}\square K_2\) in connection with a **defensive two-alliance** (rather than defensive zero-alliance) parameter and general product results; that statement does not establish the present majority C-colouring spectrum. Work on the exact majority C-colouring numbers of grid and Hamming products [4] concerns different factors. The result here supplies a full Stirling-number enumeration and all extremal partitions for the square-page book family.

## Limitations
The theorem is specific to four-cycle pages sharing a single spine edge. No formula is claimed for books with different page lengths, general Cartesian products, or the defensive \(k\)-alliance condition when \(k\ne0\). Priority searches are not proofs of global novelty; an equivalent statement in older work on sum-satisfactory partitions or defensive zero-alliance partitions remains possible. The independent mathematical audit has not been performed.

## References
[1] C. Bujtás, M. Dettlaff, H. Furmańczyk, A. Laskowska, *Majority C-coloring of graphs*, arXiv:2604.20752v1 (22 April 2026), https://arxiv.org/html/2604.20752.

[2] C. Bujtás, M. Dettlaff, H. Furmańczyk, A. Laskowska, Z. Tuza, *Majority C-coloring in Cartesian products*, arXiv:2608.27669v1 (27 August 2026), https://arxiv.org/pdf/2608.27669.

[3] I. G. Yero, S. Bermudo, J. A. Rodríguez-Velázquez, J. M. Sigarreta, *Partitioning a graph into defensive k-alliances*, arXiv:0901.4923v1 (30 January 2009), https://arxiv.org/pdf/0901.4923.

[4] Z. Lu, *Exact majority C-colourings of balanced Hamming graphs and grids*, arXiv:2609.31674 (2026), https://arxiv.org/abs/2609.31674.
