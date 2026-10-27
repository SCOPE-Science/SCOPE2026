# Sharp five- and six-vertex separation of finite Henson type spectra

## Finding
Let \(\mathcal H_3\) be the countable universal homogeneous triangle-free graph. Over a finite individually named induced triangle-free parameter graph \(G\), define \(I_G(z)=\sum_{S\subseteq V(G),\;S\mathrm{\ independent}}z^{|S|}\). Let \(N_G^0\) and \(N_G^1\) respectively count complete types of ordered, distinct new vertices \((x,y)\), both outside \(G\), with \(x\not\sim y\) and \(x\sim y\). Define \(\Phi(G)\) to be the number of ordered disjoint pairs of independent vertex subsets of \(G\). Then
\[
N_G^0=I_G(1)^2,\qquad N_G^1=\Phi(G).
\]
The general type-count reduction to independent neighborhoods is standard background, not the novelty assertion. The new claim is the following sharp failure of reconstruction from the *entire* one-point neighborhood-size polynomial:

**Theorem.** Among triangle-free parameter graphs, the least size of two nonisomorphic graphs with equal \(I_G(z)\) but unequal ordered two-type profiles \((N_G^0,N_G^1)\) is **five**. Up to graph isomorphism, the only independence-polynomial collision on five vertices within the triangle-free class is the pair \(C_4\sqcup K_1\) and the five-vertex fork tree (degree multiset \((3,2,1,1,1)\)). For these graphs,
\[
I_G(z)=1+5z+6z^2+2z^3,
\quad (N_G^0,N_G^1)=(196,105)\ \text{and}\ (196,103),
\]
so their total ordered two-type counts are \(301\) and \(299\).

If both parameter graphs are additionally required to be connected, the sharp minimum is **six**. It remains six even if they must have the same degree multiset. Explicit witnesses are a four-cycle with a two-edge pendant path attached at one cycle vertex and a five-cycle with one pendant leaf, both on six vertices. They have the same degree multiset \((3,2,2,2,2,1)\) and
\[
I_G(z)=1+6z+9z^2+3z^3,
\quad (N_G^0,N_G^1)=(361,209)\ \text{and}\ (361,203),
\]
so their total counts are \(570\) and \(564\). All statements concern individually named parameters and injective ordered pairs of new vertices, not automorphism quotients of the parameter graphs.

## Assumptions and scope
Graphs are finite simple undirected loopless graphs. The background structure \(\mathcal H_3\) is the unique countable homogeneous universal triangle-free graph. Every parameter graph is embedded *inducedly* and named pointwise; the finite extension age is exactly the triangle-free graphs. Types are complete over this finite named base. The one-point invariant contains every coefficient of \(I_G\), not merely \(I_G(1)\). Only injective ordered two-types with both new elements outside the base are counted. The two witnesses of each size are nonisomorphic. The assertion of uniqueness concerns the sole independence-polynomial collision at size five *among triangle-free graphs*; no uniqueness of six-vertex connected witnesses is asserted.

## Proof
**Extension types.** By universality and homogeneity of \(\mathcal H_3\), every finite triangle-free extension of the named base is realized and two tuples have the same complete type precisely when they induce the same finite adjacency diagram. A new vertex has any independent neighborhood \(S\subseteq V(G)\), and no other neighborhood, giving \(I_G\). For an ordered pair of distinct new vertices, put \(S=N(x)\cap G\) and \(T=N(y)\cap G\). Both must be independent. If \(xy\) is absent there is no further condition; if it is present then \(S\cap T=\varnothing\), since a common neighbor would complete a triangle. Conversely these conditions make the finite extension triangle-free. Thus \(N_G^0=I_G(1)^2\), while \(N_G^1=\Phi(G)=\sum_{S\in\mathcal I(G)}I_{G-S}(1)\). Equivalently \(\Phi(G)\) counts three-colourings of \(V(G)\) by states \(0,1,2\) with no edge having both endpoints in state \(1\) or both in state \(2\). Note that differently coloured adjacent vertices in states \(1\) and \(2\) are permitted.

**Five-vertex witnesses.** For \(G=C_4\sqcup K_1\), multiplying the independence polynomial of the square by \(1+z\) yields \(1+5z+6z^2+2z^3\). For the fork, let \(v\) be its degree-three vertex, with two leaf-neighbors and one degree-two neighbor (whose other neighbor is a leaf). Removing \(v\) leaves an edge and two isolated vertices; selecting \(v\) leaves one optional vertex. Therefore the polynomial is \((1+2z)(1+z)^2+z(1+z)=1+5z+6z^2+2z^3\). To compute the three-state counts, \(\Phi(K_1)=3\) and \(\Phi(C_4)=7+4\cdot5+2\cdot4=35\), hence \(\Phi(C_4\sqcup K_1)=105\). For the fork, condition on the state at \(v\): state \(0\) contributes \(3^2\cdot7=63\), and each of states \(1,2\) contributes \(2^2\cdot5=20\). Thus \(\Phi(\text{fork})=103\).

**Sharpness and uniqueness through five vertices.** Up to four vertices, the triangle-free graph types are respectively \(1,2,3,7\) in sizes \(1,2,3,4\); their independence polynomials are pairwise distinct at each size. On four vertices the complete list is \(4K_1\), \(K_2\sqcup2K_1\), \(2K_2\), \(P_3\sqcup K_1\), \(P_4\), \(K_{1,3}\), and \(C_4\); after the common constant and linear terms, their respective coefficient tails \((i_2,i_3,i_4)\) are \((6,4,1),(5,2,0),(4,0,0),(4,1,0),(3,0,0),(3,1,0),(2,0,0)\), all distinct. On five vertices there are fourteen triangle-free isomorphism types. Their degree-multiset and coefficient-tail pairs \((i_2,i_3,i_4,i_5)\), grouped by edge count, are:

| Edges | Degree multiset (increasing) | \((i_2,i_3,i_4,i_5)\) |
|---:|:---|:---|
|0|0,0,0,0,0|(10,10,5,1)|
|1|0,0,0,1,1|(9,7,2,0)|
|2|0,1,1,1,1|(8,4,0,0)|
|2|0,0,1,1,2|(8,5,1,0)|
|3|1,1,1,1,2|(7,2,0,0)|
|3|0,1,1,2,2|(7,3,0,0)|
|3|0,1,1,1,3|(7,4,1,0)|
|4|1,1,2,2,2|(6,1,0,0)|
|4|1,1,1,2,3|(6,2,0,0)|
|4|0,2,2,2,2|(6,2,0,0)|
|4|1,1,1,1,4|(6,4,1,0)|
|5|2,2,2,2,2|(5,0,0,0)|
|5|1,2,2,2,3|(5,1,0,0)|
|6|2,2,2,3,3|(4,1,0,0)|

The enumeration in the table is exhaustive: `verify.py` independently loops through each of the \(2^{\binom52}\) labelled graphs, discards those containing a triangle, and identifies isomorphic graphs by examining every permutation of five vertices. Thus there are precisely fourteen types, with exactly one polynomial collision, and both members of that collision are the stated witnesses. This also proves that every connected triangle-free graph with at most five vertices has a unique independence polynomial among connected triangle-free graphs of its size.

**Connected six-vertex witnesses.** Give the first graph edge list \((0,4),(0,5),(1,3),(1,4),(2,3),(2,4)\). Its four-cycle is \(1-3-2-4-1\), and the path \(4-0-5\) is attached. Give the second edge list \((0,1),(0,4),(1,2),(1,5),(2,3),(3,4)\). Its five-cycle is \(0-1-2-3-4-0\), with a leaf at \(1\). They are connected and triangle-free, and have the same degree multiset, but different cycle lengths, so are nonisomorphic. For the first, condition on whether the degree-two vertex \(0\) on the tail is independent-set selected: \(I_G(z)=(1+z)I_{C_4}(z)+zI_{P_3}(z)=1+6z+9z^2+3z^3\). For the second, condition on its pendant leaf: \(I_G(z)=I_{C_5}(z)+zI_{P_4}(z)=1+6z+9z^2+3z^3\). In the three-state model, condition on the cycle vertex to which the tail/leaf attaches. For the four-cycle witness, state \(0\) gives \(\Phi(P_3)\Phi(P_2)=17\cdot7=119\), while states \(1\) and \(2\) each give \(9\cdot5=45\), so the total is \(209\). For the five-cycle witness, state \(0\) gives \(\Phi(P_4)\cdot3=41\cdot3=123\), and states \(1,2\) each contribute \(20\cdot1=40\), so the total is \(203\). The factors \(9,5,20\) count the corresponding paths with forbidden endpoint state(s), verified directly by the same three-state edge rule; the supplied checker also enumerates each complete six-vertex assignment independently. Since no connected collision exists on five or fewer vertices, six is sharp.

## Verification
`verify.py` is a standalone standard-library-only exhaustive checker. It generates every labelled simple graph for orders \(1\) through \(5\), detects forbidden triangles, canonicalizes all surviving graphs under all \(n!\) permutations, computes the complete independence polynomials and three-state counts, and confirms the unique size-five collision and absence of smaller (including connected) collisions. It independently evaluates both explicit six-vertex graphs, their connectedness, triangle-freeness, degree multisets, and invariants. Its output finishes `ALL_CHECKS_PASS`; see `verification_output.txt`. Complete enumeration applies only to graphs of size at most five, and does not purport to classify all six-vertex graphs.

## Relationship to prior work
Henson's 1971 construction and Conant's 2014 treatment give the homogeneous triangle-free graph and the finite-extension / quantifier-elimination framework. The equality between the nonalgebraic one-type neighborhood polynomial and the graph independence polynomial has already been published, as have the existence of graphs sharing an independence polynomial. A previous general tuple-extension formula also counts arbitrary ordered injective types from independent-set constructions; therefore the abstract two-type counting identity and raw graph-by-graph substitutions are not claimed as independent discoveries. The present specific finding is the **sharp first-separation classification**, the unique five-vertex triangle-free collision, the connected six-vertex threshold, and six-vertex witnesses retaining the same degree multiset. Full-text inspection of Henson and Conant, plus the accessible published type-count discussion and targeted bibliographic searches, did not locate this joint threshold theorem. An unindexed enumeration or a different formulation of this same sharp comparison could cover it; the available evidence does not prove absolute novelty.

## Limitations
The conclusion concerns only finite triangle-free parameter graphs of the homogeneous triangle-free graph, and only complete one-point neighborhood-size spectra versus counts of distinct ordered two-types. The two-point *full labelled diagram* is richer than its scalar orbit count and is not classified here. The six-vertex connected example is not claimed unique. The finite certificate is exhaustive through five vertices only; it is not an infinite-size classification. The general type-count formula is prior mathematics. No independent scientific audit has been carried out.

## References
1. C. W. Henson, “A family of countable homogeneous graphs,” *Pacific Journal of Mathematics* 38 (1971), 69–83. DOI: 10.2140/pjm.1971.38.69. https://msp.org/pjm/1971/38-1/pjm-v38-n1-p09-p.pdf. Section 2, especially Theorem 2.3.
2. G. Conant, “Forking and dividing in Henson graphs,” arXiv:1401.1570v1 (first public 2014-01-08), later *Notre Dame Journal of Formal Logic* 58 (2017), 555–566. https://arxiv.org/html/1401.1570v1. Section 3.
3. “Exact finite-parameter 1-type counting in Henson graphs is #P-complete,” publicly accessible mathematical record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-finite-parameter-1-type-counting-in-henson-graphs-is-p-com--7c84dde7c650. Explicit polynomial identity is prior.
4. H. Zhang, “A way to construct independence equivalent graphs,” *Applied Mathematics Letters* 25 (2012), 1304–1308. DOI: 10.1016/j.aml.2011.11.033. Only abstract-level access was obtained; this limits coverage assessment.
5. E. W. Weisstein, “Independence Polynomial,” *MathWorld*, https://mathworld.wolfram.com/IndependencePolynomial.html. Lists small independence-equivalent graph examples; their equivalence is not claimed as new here.
