# One spare color forces a unique split part in complete multipartite graphs

## Finding
Let \(r\ge3\), and let \(G=K_{n_1,\ldots,n_r}\) have \(r\) nonempty independent parts of orders \(n_i\ge1\). Give the graph a palette of \(r+1\) distinguishable colors. The following theorem simultaneously characterizes **every** forcing partial proper coloring and gives its entire size distribution.

**Theorem.** A partial proper coloring forces a full coloring under the local missing-color rule if and only if it is in exactly one of the following two classes:

1. It is already a total proper coloring with exactly one distinct color on each part (one palette color remains unused).
2. There is a unique **split part** \(j\): every vertex of that part is colored initially, exactly two distinct colors occur there, each other part has its own distinct singleton color, and at most one of these other parts has no initially colored vertex. Every initially colored vertex of a nonsplit part has the color of its eventual entire part.

For \(N=\sum_i n_i\), put \(A_i(z)=(1+z)^{n_i}-1\). The forcing-seed enumerator by initial colored-domain size is
\[
H_G(z)=(r+1)!z^N+\frac{(r+1)!}{2}\sum_{j=1}^r(2^{n_j}-2)z^{n_j}\left(\prod_{i\ne j}A_i(z)+\sum_{h\ne j}\prod_{i\notin\{j,h\}}A_i(z)\right).
\]
Here and below an empty product is one. Its coefficient of \(z^s\) counts forcing initial assignments with exactly \(s\) colored vertices, including the choice of color labels.

For independent vertex states in which each color has probability \(p\in[0,1/(r+1)]\) and blank has probability \(q=1-(r+1)p\), define
\[
U_i(p)=(p+q)^{n_i}-q^{n_i},\qquad V_i(p)=q^{n_i}.
\]
The forced-coloring probability is exactly
\[
\operatorname{FC}_{r+1}(G;p)=(r+1)!p^N+\frac{(r+1)!}{2}\sum_{j=1}^r(2^{n_j}-2)p^{n_j}\left(\prod_{i\ne j}U_i(p)+\sum_{h\ne j}V_h(p)\prod_{i\notin\{j,h\}}U_i(p)\right).
\]

If all parts are singletons, the minimum number of initial colored vertices is \(N=r\), with \((r+1)!\) forcing initial assignments. Otherwise put \(m=\min\{n_i:n_i\ge2\}\). The minimum seed size is \(m+r-2\), and the number attaining it is
\[
\frac{(r+1)!}{2}(2^m-2)\sum_{j:n_j=m}\sum_{h\ne j}\prod_{i\notin\{j,h\}}n_i.
\]

## Assumptions and scope
All graphs are finite, simple, and complete multipartite, with \(r\ge3\) nonempty parts; singleton parts are allowed. Proper means that adjacent colored vertices have distinct colors. Each uncolored vertex sees the set of colors already assigned to its neighbors. If it sees exactly \(r\) distinct colors among the \(r+1\) available colors, it is assigned the sole missing color. Continue until no force is possible. An initial assignment is *forcing* if the process fully and properly colors the graph. The final coloring is unique whenever forcing succeeds; the order of valid forces does not affect success. The main claim concerns the precise palette size \(r+1\), not larger palettes or arbitrary graphs.

## Proof
**1. Exhaustion of possible final color patterns.** In every proper coloring, colors on different parts are disjoint. Each of the \(r\) nonempty parts uses at least one color, and there are only \(r+1\) colors. Thus either every part is monochromatic with one unused color, or exactly one part, denoted \(j\), uses exactly two colors while every other part is monochromatic. There can be no second split part.

**2. No nontrivial propagation in the first pattern.** Suppose every part is monochromatic in the final proper coloring. Any blank vertex in any part sees at most \(r-1\) colors outside that part, throughout the forcing process, since only those \(r-1\) other parts can supply neighbor colors. It can never see \(r\) colors. Hence a successful initial assignment of this type must be the complete coloring itself. There are \((r+1)!\) such colorings: choose the unused color and assign the other \(r\) colors bijectively to parts.

**3. Rigidity of a split part.** Suppose the final coloring has unique split part \(j\). Every vertex of that part has neighbors only in the other \(r-1\) monochromatic parts, and thus sees at most \(r-1\) colors. Consequently no blank vertex in the split part can ever be forced: every one must have been colored initially. Both of the split part's final colors must therefore already appear. The nonsplit parts have distinct singleton colors, disjoint from these two.

If at least two nonsplit parts are initially uncolored, no first forcing step is possible: each blank vertex of a nonsplit part sees both colors in the split part, together with at most \(r-3\) colors from seeded other nonsplit parts, a total of at most \(r-1\), while blanks in the split part are impossible. Thus no forcing initial assignment can have two entirely blank nonsplit parts.

Conversely, suppose the split part is fully colored with both of its colors and every nonsplit part is seeded except possibly one part \(h\). If such a blank part \(h\) exists, its vertices see \(r\) colors immediately (two from the split part and one from each of the other \(r-2\) nonsplit parts), so they are forced to the unique missing color of \(h\). Now each nonsplit part has a seed; every remaining blank vertex outside the split part sees exactly \(r\) distinct colors and is forced. If no part is wholly blank, the latter argument applies immediately. These forces are proper because the recovered color is distinct from the colors on every other part. This proves the if-and-only-if classification and unique completion.

**4. Exact enumeration.** For a chosen split part \(j\), select an unordered pair of distinct colors for it and assign the remaining \(r-1\) colors bijectively to other parts. There are \(\binom{r+1}{2}(r-1)!=(r+1)!/2\) choices. Assign the two colors to the \(n_j\) split vertices with both occurring: \(2^{n_j}-2\) possibilities; all those vertices are seeded, contributing \(z^{n_j}\) to the size enumerator. In another part \(i\), a nonempty seed subset contributes \(A_i(z)\); a blank part contributes \(1\). At most one is blank, producing the bracket in the stated formula for \(H_G(z)\). The classes and split-part choices are disjoint by Steps 1–3. Together with the \((r+1)!z^N\) fully colored monochromatic cases, this proves the polynomial identity.

For independent vertex probabilities, a split part contributes \(p^{n_j}\); an initially seeded monochromatic part contributes \(U_i(p)\), and an entirely blank part contributes \(V_i(p)\). The same disjoint decomposition proves the displayed probability identity. Equivalently, \(\operatorname{FC}_{r+1}(G;p)=\sum_{s=0}^N[z^s]H_G(z)\,p^s q^{N-s}\).

**5. Minimum initial domain and its count.** If every part is a singleton, no split part exists and all vertices must be seeded. Otherwise a split part of minimum admissible order \(m\) needs all \(m\) vertices; at most one of the other \(r-1\) parts may be blank, so at least \(r-2\) other seeded vertices are necessary and sufficient. To attain exactly \(m+r-2\), choose the split part \(j\) of order \(m\), the unique blank part \(h\ne j\), one seeded vertex in each other part, and a surjective two-color assignment on part \(j\). Multiplying and summing yields the claimed count. Full monochromatic colorings have \(N\ge m+r-1\) seeds and cannot tie. This completes the proof.

## Verification
The standalone, dependency-free C++17 program `verify.cpp` independently enumerates every \((r+2)\)-state partial coloring (blank or one of \(r+1\) colors), excludes initially improper assignments, carries out the missing-color forcing process vertex by vertex, and compares the resulting exact initial-domain counts against an independently evaluated combinatorial coefficient formula. It exhaustively checks all nondecreasing part-size profiles with \(2\le r\le4\), every part of size at most four, and total order at most eight. The included output records **34 profiles and 9,213,533 initial assignments, all passing**, and displays representative exact coefficient vectors. The \(r=2\) cases are checks of the already known boundary case, not a new claim. Compile and run with `g++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify && ./verify`; expected console output is in `verification_output.txt`. These finite experiments are independent checks, not the proof of the universal theorem.

## Relationship to prior work
G. E. Farr's 2026 paper introduces the forced-coloring function, its local rule, fundamental graph-polynomial properties and complexity results, along with small examples and the two-color bipartite setting. The present result addresses a distinct infinite family at precisely **one extra color beyond its chromatic number**, for three or more parts, and supplies every coefficient rather than selected instances. Earlier palette-three results for complete bipartite graphs are boundary cases and are **not** claimed as new here. Existing descriptions of complete multipartite graphs at exactly their chromatic number do not imply the spare-color split-part mechanism. The color-changing processes in Bozeman and coauthors' multicolor forcing theory have different definitions and do not furnish this formula.

## Limitations
The theorem applies only to the complete multipartite graph class with at least three parts, one spare color, and Farr's missing-color forcing rule. It does not characterize palettes with two or more spare colors or arbitrary graph classes. The cited research may contain equivalent results under other terms; published and unindexed literature cannot be exhausted by search. Independently checked finite cases do not validate every parameter; the universal proof is the argument above.

## References
1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1, first posted 15 September 2026, https://arxiv.org/abs/2609.17108.
2. Chassidy Bozeman and collaborators, *Multi-color forcing in graphs*, arXiv:1912.02001, https://arxiv.org/abs/1912.02001 (a different forcing convention, included for terminology comparison).
