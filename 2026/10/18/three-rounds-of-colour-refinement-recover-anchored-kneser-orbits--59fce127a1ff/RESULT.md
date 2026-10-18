# Three rounds of colour refinement recover anchored Kneser orbits

## Finding
For integers \(k\ge 2\) and \(n\ge 3k-1\), let \(KG(n,k)\) be the graph of \(k\)-subsets of an \(n\)-element ground set, adjacent when disjoint. Individually colour any two distinct vertices \(A\) and \(B\); give every other vertex a common third colour. Ordinary simultaneous vertex colour refinement produces **exactly the orbits of automorphisms fixing \(A\) and \(B\) individually** after **at most three rounds**.

Write \(b=|A\cap B|\), where \(0\le b<k\), and set \(c=n-2k+b\). The stable colour of a vertex \(X\) is determined precisely by the four intersection counts
\[
(r,\ s-r,\ t-r,\ k-s-t+r),\qquad
s=|X\cap A|,\quad t=|X\cap B|,\quad r=|X\cap A\cap B|.
\]
The number of stable classes is
\[
[z^k]\Bigl(\sum_{i=0}^{b}z^i\Bigr)
\Bigl(\sum_{i=0}^{k-b}z^i\Bigr)^2
\Bigl(\sum_{i=0}^{c}z^i\Bigr).
\]
For a feasible four-tuple \((u,v,w,z)\) summing to \(k\), its class contains exactly
\[
\binom{b}{u}\binom{k-b}{v}\binom{k-b}{w}\binom{c}{z}
\]
vertices. Three rounds are sometimes necessary: this occurs in \(KG(8,3)\) when \(|A\cap B|=1\).

## Assumptions and scope
A refinement round replaces each colour by the pair consisting of its preceding colour and the multiset of preceding colours on its **open neighbourhood**. The two anchors have different singleton initial colours and every remaining vertex a third colour. Round zero is the initial colouring. The theorem concerns the actual graph \(KG(n,k)\) with its ordinary disjointness edges, not its complement or a Johnson graph. No restriction on the intersection of the two distinct anchors beyond \(b<k\) is imposed. Because \(n\ge3k-1\) and \(k\ge2\), the graph has \(n>2k\).

## Proof
**Step 1 (recover the two anchor intersections by round two).** Fix any vertex \(X\), and put \(s=|X\cap A|\), \(t=|X\cap B|\). In round one, the colour of any vertex \(Y\) records whether \(Y\) is adjacent to \(A\) and whether \(Y\) is adjacent to \(B\), because the anchors have distinct initial singleton colours. Consequently, in round two, the colour of \(X\) determines the numbers of neighbours \(Y\) simultaneously adjacent to \(X\) and \(A\), respectively to \(X\) and \(B\):
\[
C_A(X)=\binom{n-2k+s}{k},\qquad
C_B(X)=\binom{n-2k+t}{k}.
\]
Indeed, such a neighbour is a \(k\)-subset disjoint from the union of the corresponding pair. Since \(n-2k\ge k-1\), the values of \(\binom{n-2k+j}{k}\) for \(j=0,\ldots,k\) are strictly increasing: the first is zero or positive, and each increment equals \(\binom{n-2k+j-1}{k-1}>0\) for \(j\ge1\). Hence the round-two colour of \(X\) determines both \(s\) and \(t\).

**Step 2 (recover the triple intersection by round three).** The round-two colour of any neighbour \(Y\) of \(X\) determines \(|Y\cap A|\) and \(|Y\cap B|\). Thus round three determines the weighted sum
\[
M(X)=\sum_{Y:\,Y\cap X=\varnothing}|Y\cap A|\,|Y\cap B|.
\]
Set \(N=n-k\), \(A'=A\setminus X\), \(B'=B\setminus X\), and \(u=|A'\cap B'|=b-r\). To evaluate the sum, count triples \((Y,a_0,b_0)\) with \(Y\) a \(k\)-subset of the \(N\)-point complement of \(X\), with \(a_0\in A'\cap Y\) and \(b_0\in B'\cap Y\). Of the \((k-s)(k-t)\) ordered candidate pairs, exactly \(u\) have \(a_0=b_0\), and all other pairs use two distinct points. Therefore
\[
M(X)=(k-s)(k-t)\binom{N-2}{k-2}
      +(b-r)\binom{N-2}{k-1}.
\]
Here \(N\ge2k-1\) and \(k\ge2\), so the coefficient \(\binom{N-2}{k-1}\) is strictly positive. The already recovered \(s,t\), the anchor intersection \(b\), and \(M(X)\) uniquely determine \(r\):
\[
r=b-\frac{M(X)-(k-s)(k-t)\binom{n-k-2}{k-2}}{\binom{n-k-2}{k-1}}.
\]
Thus the round-three colour determines the four intersection counts displayed in the finding.

**Step 3 (the recovered classes are exactly the stabilizer orbits).** The four regions \(A\cap B\), \(A\setminus B\), \(B\setminus A\), and the complement of \(A\cup B\) have respective sizes \(b,k-b,k-b,c\). Every permutation of the ground set preserving each region individually induces a graph automorphism fixing \(A\) and \(B\). These permutations act transitively on vertices with any fixed feasible quadruple. Conversely, every automorphism fixing the two distinguished anchors preserves all refinement colours, so cannot map vertices with distinct round-three colours to each other. Hence the round-three classes are exactly the automorphism orbits, and refinement remains unchanged subsequently. Choosing the subsets inside the four disjoint regions gives the stated class sizes and coefficient formula.

**Step 4 (sharpness).** Take \(n=8,k=3\), with \(A=\{0,1,2\}\), \(B=\{0,3,4\}\), and \(X=\{0,5,6\}\), \(X'=\{1,3,5\}\). Both vertices have \(s=t=1\). At round one they are both nonadjacent to both anchors. Each has exactly ten neighbours in total, of which zero are adjacent to both anchors, one is adjacent only to \(A\), one only to \(B\), and eight to neither anchor. Neither distinguished anchor is a neighbour of either vertex. Thus the full multiset of round-one colours on the neighbourhoods agrees, so their round-two colours coincide. Their four-region profiles are respectively \((1,0,0,2)\) and \((0,1,1,1)\). The preceding formula gives \(M(X)=12\) and \(M(X')=15\), so round three separates them. The respective numbers of colour classes in rounds \(0,1,2,3\) are \(3,6,13,14\); the general proof establishes that the last partition is stable.

## Verification
Two standalone, dependency-free Python programs accompany this proof. `verify_refinement.py` constructs Kneser graphs from subsets, performs exactly three rounds, and compares the resulting colour equivalence relation in both directions with the four-region orbit relation. It passed 42 configurations comprising 9,263 vertex instances, and independently checked the explicit sharpness case. `verify_moments.py` directly enumerates disjoint neighbours to test the weighted-moment identity, reconstructs all feasible orbit profiles and their binomial class cardinalities, and checks the sharpness moments. It passed 28 configurations comprising 4,723 vertex instances. The two tests use different constructions and check different implications. They are corroborative finite tests, not proofs of unbounded parameters; the preceding counting argument proves the quantified theorem.

## Relationship to prior work
The foundational correspondence between equitable partitions, ordinary colour refinement and two-variable counting logic is developed by Kiefer–Schweitzer–Selman, *Graphs Identified by Logics with Counting* (arXiv:1503.08792v1, March 30, 2015). Their general results do not state this three-round two-anchor Kneser-orbit theorem, and orbit recovery must not be confused with identification against arbitrary other graphs.

Boutin, *Identifying Graph Automorphisms Using Determining Sets* (2006), studies determining numbers and sets in ordinary Kneser graphs, including the intersection-incidence representation of stabilizers; the paper does not study iterative colour refinement. Albertson–Boutin, *Using Determining Sets to Distinguish Kneser Graphs* (2007), establishes distinguishing labelings, not recovery by three rounds of refinement after marking two arbitrary vertices. Those results alone imply no bounded refinement-depth statement, and this theorem does not claim that two marked vertices form a determining set. An earlier two-anchor orbit theorem for individually marked Johnson graphs concerns adjacency by one-element exchange, not Kneser disjointness; neither its proof nor its intersection-count formulas apply directly.

## Limitations
The proved parameter range is \(k\ge2,n\ge3k-1\); smaller ambient sets and the edgeless boundary are not covered. The universal three-round bound is shown sharp by one concrete example, not by a classification of all sharp parameters. The theorem says that the stable colours equal the automorphism-orbit partition **in the given graph**. It does not say that two-variable counting logic uniquely identifies the whole graph among arbitrary graphs, nor that any two vertices form a determining set. Priority against all historical or unpublished specialist literature has not been independently certified.

## References
1. S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792v1 (first publicly posted 2015-03-30), https://arxiv.org/abs/1503.08792.
2. D. L. Boutin, *Identifying Graph Automorphisms Using Determining Sets*, *Electronic Journal of Combinatorics* 13 (2006), R78, https://doi.org/10.37236/1104.
3. M. O. Albertson, D. L. Boutin, *Using Determining Sets to Distinguish Kneser Graphs*, *Electronic Journal of Combinatorics* 14 (2007), R20, https://doi.org/10.37236/938.
