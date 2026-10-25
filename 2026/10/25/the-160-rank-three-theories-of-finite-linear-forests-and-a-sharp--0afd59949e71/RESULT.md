# The 160 rank-three theories of finite linear forests and a sharp 23-vertex kernel

## Finding
Let \(\mathcal L\) be the class of all **nonempty finite simple undirected linear forests**, meaning graphs whose connected components are paths, with isolated vertices allowed. Two graphs satisfy \(G\equiv_3H\) when they satisfy the same first-order sentences of quantifier rank at most three in the language containing equality and one adjacency relation \(E\). Then
\[
  |\mathcal L/{\equiv_3}|=160,
  \qquad
  \max_{[G]\in\mathcal L/{\equiv_3}}\ \min_{H\in[G]} |V(H)|=23.
\]
The sharp lower-bound class has a 23-vertex representative
\[
 W=2P_1\sqcup P_2\sqcup P_3\sqcup P_4\sqcup P_5\sqcup P_7,
\]
where \(P_i\) denotes the undirected path on \(i\) vertices and \(\sqcup\) disjoint union. Thus every rank-three theory realized by a nonempty finite linear forest has a representative on at most 23 vertices, and the number 23 cannot be decreased.

## Assumptions and scope
All structures are nonempty, finite, loopless, and undirected. The first-order signature is exactly \(\{E,=\}\); there are no colors, constants, component predicates, order, or counting quantifiers. Quantifier rank measures the maximum nesting depth of quantifiers, not their total number. Isolated vertices count as one-vertex paths.

## Proof
**Step 1: a uniform path cutoff.** For a graph \(G\) and vertices \(x,y\), define the one-move pointed-pair invariant \(t_G(x,y)\). If \(x\ne y\), record \(E(x,y)\) and, for each \((a,b)\in\{0,1\}^2\), whether some \(z\notin\{x,y\}\) has \((E(x,z),E(y,z))=(a,b)\). If \(x=y\), record whether there exists a different neighbor of \(x\) and whether there exists a different nonneighbor. Equality and all relations involving \(z=x\) or \(z=y\) are already determined. Hence \(t_G(x,y)\) is a complete quantifier-rank-one type of an ordered pair with its two entries named.

For a path \(P_n\) with \(n\ge7\), a pair of distinct vertices is of one of three forms: at distance one, at distance two, or at distance at least three. In the first two forms, the record above depends only on whether each vertex is an endpoint: a pair at distance one has no common neighbor, a pair at distance two has exactly its middle common neighbor, and the existence of an exclusive neighbor on either side is governed by endpoint status. In the third form, both vertices have exclusive neighbors, have no common neighbor, and have a vertex adjacent to neither, because their closed neighborhoods together contain at most six vertices. The corresponding nonneighbor also exists in the first two forms. These observations determine every \(t_{P_n}(x,y)\) for \(n\ge7\).

For a fixed first vertex \(x\), the set \(\{t_{P_n}(x,y):y\in V(P_n)\}\) therefore depends only on
\[
  \min\{3,\operatorname{dist}(x,\{\text{two endpoints}\})\}\in\{0,1,2,3\}.
\]
Indeed, an endpoint at distance one is visible only in the distance-one case, an endpoint at distance two is visible only in the distance-two case, and other endpoint information is invisible in the distance-at-least-three case. All four possibilities occur for every \(n\ge7\). Thus the set of pointed rank-two types and hence the rank-three sentence type of \(P_n\) are constant for all \(n\ge7\). Equivalently, \(P_n\equiv_3P_7\) for every \(n\ge7\). This also follows from the path theorem of Brown and Hoshino, but the argument above independently establishes the needed special case.

**Step 2: disjoint-union normalization.** The three-round Ehrenfeucht–Fraïssé game admits a componentwise strategy: replace every component by a rank-three-equivalent component, and, for each component type, truncate its number of copies to three. Duplicator pairs each entered component with an unused equivalent component, or continues the existing within-component winning strategy when the same component is entered again. At most three components of any one type can be entered in three rounds. Partial isomorphisms within mapped components combine because there are no edges between components. Consequently, every \(G\in\mathcal L\) is rank-three equivalent to a graph of the form
\[
  G_{\mathbf c}=\bigsqcup_{i=1}^{7} c_iP_i,
  \qquad \mathbf c\in\{0,1,2,3\}^{7}\setminus\{\mathbf0\}.
\]
Replacement and truncation never increase order. There are exactly \(4^7-1=16,383\) such canonical graphs and each has at most 84 vertices. This normalization yields coverage, not a claim that all canonical graphs are inequivalent.

**Step 3: a complete exact rank-three signature.** Encode \(t_G(x,y)\) numerically as follows. For \(x\ne y\), let \(p\) be the four-bit mask of witnessed adjacency patterns \(00,10,01,11\) among vertices other than \(x,y\), in that order, and set
\[
 t_G(x,y)=16\,[E(x,y)]+p.
\]
For \(x=y\), set
\[
 t_G(x,x)=32+[\exists z\ne x:E(x,z)]+2[\exists z\ne x:\neg E(x,z)].
\]
Square brackets take values zero or one. Put
\[
 M_G(x)=\bigvee_{y\in V(G)}2^{t_G(x,y)},\qquad
 S(G)=\{M_G(x):x\in V(G)\},
\]
where the join means bitwise OR and the final braces denote a set, not a multiset. By the standard back-and-forth recursion for quantifier-rank types, \(t_G(x,y)\) is the complete rank-one ordered-pair type, \(M_G(x)\) the complete rank-two pointed type, and \(S(G)\) the complete rank-three sentence type. Therefore, for all nonempty finite graphs, without a degree restriction,
\[
 G\equiv_3H\quad\Longleftrightarrow\quad S(G)=S(H).
\]
This equivalence is exact: it includes alternating quantifiers and formulas with repeated variables, not merely existential three-vertex patterns.

**Step 4: exhaustive finite reduction and the sharp minimum.** The included `verify_rank3.py` enumerates every nonzero base-four code \(c=\sum_{i=1}^{7} c_i4^{i-1}\), constructs \(G_{\mathbf c}\), evaluates \(S(G_{\mathbf c})\) using the formula above, and groups equal signatures. Its exhaustive table `canonical_manifest.csv` contains one record for each of the 16,383 canonical graphs; `class_representatives.csv` contains a minimum-order canonical representative and its signature for each distinct class. There are 160 different signatures. The exact histogram of minimum representative orders is
\[
\begin{array}{c|rrrrrrrrrrrr}
\text{order}&1&2&3&4&5&6&7&8&9&10&11&12\\
\text{classes}&1&2&3&4&5&8&9&9&11&11&12&13\\[2pt]
\text{order}&13&14&15&16&17&18&19&20&21&22&23\\
\text{classes}&11&11&10&10&8&7&5&4&3&2&1
\end{array}
\]
The histogram sums to 160. The unique class with canonical minimum 23 is represented by the base-four code 4438, with component multiplicities \((2,1,1,1,1,0,1)\), which is exactly \(W\). Since every linear forest normalizes to a **no-larger** canonical forest of the same rank-three theory, no noncanonical representative can beat any minimum found in the exhaustive canonical search. Thus 23 is the sharp global bound. This completes the proof.

## Verification
Reproduction from a directory containing the attached files requires Python 3 with only the standard library; a C++17 compiler supplies a separate optimized implementation. Run `python verify_rank3.py` to regenerate both CSV certificates; run `g++ -O3 -std=c++17 verify_rank3.cpp -o verify_rank3 && ./verify_rank3` to compare the exact class count, sharp bound, multiplicity witness, and histogram. Run `python crosscheck_ef.py` for an additional recursive, direct game computation. The commands run in the directory of the sources and do not require downloaded datasets. The Python and C++ exhaustive implementations agree on 16,383 candidates, 160 signatures, the histogram, and the sharp maximum 23; the direct three-round game confirms fingerprint equivalence on 901 pairs among all 52 canonical linear forests having at most eight vertices.

`canonical_manifest.csv` contains 16,383 data records (plus header). Its SHA-256 is `46ee98611900697f41471945a629deb920125e8e4e869bc9199222dc3f279a9e`. `class_representatives.csv` contains 160 data records (plus header). Its SHA-256 is `d416fa08b4bebeb0568c06a00b573080dd13465156214d0f6f3d9f206beeeae8`. Both scripts implement the explicit mathematical signature; these finite enumerations are used only after the all-order normal-form proof.

## Relationship to prior work
Brown and Hoshino (2007, Theorem 3.1) completely classify three-round indistinguishability **between individual undirected paths**, including the exceptional length cutoff seven, and explicitly identify extensions to other graph families as open directions. That theorem supplies the component-level phenomenon but does not give the rank-three quotient or the sharp representative bound for arbitrary **disjoint unions** of paths. Verbitsky (arXiv:math/0401361, first public 2004-01-26) proves logarithmic definability bounds for connected bounded-degree trees and uses separator strategies; an asymptotic quantifier-rank bound does not determine this exact low-rank quotient of disconnected forests. The separate successor-only directed-path classification concerns a different binary relation and connected structures. General disjoint-union composition yields the 16,383-case upper-bound reduction, but neither that bound nor the single-path theorem implies the observed 160 classes or the sharp 23-vertex representative maximum.

## Limitations
The count and cutoff concern only rank-three first-order logic in the uncolored undirected graph language, restricted to nonempty linear forests. Nothing is asserted about higher ranks, general forests, additional predicates, graph isomorphism, or independent external validation. The 160-class and sharp-23 facts use reproducible finite certificates coupled to a symbolic normalization argument; raw enumeration without normalization would not establish the infinite-family theorem. An equivalent exact census in unindexed literature or folklore cannot be excluded by the searches performed.

## References
1. Jason I. Brown and Richard Hoshino, “The Ehrenfeucht-Fraïssé Game for Paths and Cycles,” *Ars Combinatoria* 83 (2007), 193–212, published 2007-04-30. https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf
2. Oleg Verbitsky, “The First Order Definability of Graphs with Separators via the Ehrenfeucht Game,” arXiv:math/0401361, first submitted 2004-01-26. https://arxiv.org/abs/math/0401361
3. “Exact quantifier-rank threshold for finite directed paths,” publicly available research record, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-quantifier-rank-threshold-for-finite-directed-paths--75a6b05e7112/RESULT.md
