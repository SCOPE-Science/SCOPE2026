# Restrained Italian domination polynomials of leaf coronas from induced boundary profiles
## Finding
Let \(G\) be any finite simple graph on \(n\ge0\) labeled vertices, and let \(H=G\circ K_1\) be its **leaf corona**: for every \(v\in V(G)\), attach one new private leaf \(v'\). A *restrained Italian dominating function* (RID function) is a labeling \(f:V(H)\to\{0,1,2\}\) such that every zero-labeled vertex has sum of labels in its open neighborhood at least \(2\), and the subgraph induced by all zero-labeled vertices has no isolated vertex. The empty zero set is allowed. Define the full weight enumerator
\[
\mathcal R_H(z)=\sum_{f\text{ an RID function on }H}z^{\sum_{x\in V(H)}f(x)}.
\]
Call \(S\subseteq V(G)\) *admissible* when every vertex of \(S\) has a neighbor in \(S\); the empty set is admissible. Put
\[
b_G(S)=|\{v\in S:N_G(v)\setminus S\ne\varnothing\}|.
\]
Then, for **every** finite simple base graph \(G\), including graphs with isolated vertices,
\[
\boxed{\mathcal R_{G\circ K_1}(z)
=\sum_{\substack{S\subseteq V(G)\\ S\text{ admissible}}}
z^{2n-b_G(S)}(1+z)^{2n-2|S|+b_G(S)}.} \tag{1}
\]
Thus, if \(B(G)=\max\{b_G(S):S\text{ admissible}\}\), then
\[
\boxed{\gamma_{rI}(G\circ K_1)=2n-B(G),\qquad
|\{f:\mathrm{wt}(f)=\gamma_{rI}(G\circ K_1)\}|
=|\{S:S\text{ admissible},\ b_G(S)=B(G)\}|.} \tag{2}
\]
Both formulas include \(G\) empty, for which the right side of (1) equals \(1\).

For the *sunlet* \(H_n=C_n\circ K_1\), let \(n\ge3\). Formula (1) becomes the explicit finite double sum
\[
\boxed{\begin{aligned}
\mathcal R_{H_n}(z)={}&z^{2n}\big((1+z)^{2n}+1\big)\\
&+\sum_{k=1}^{\lfloor n/3\rfloor}\sum_{s=2k}^{n-k}
\frac nk\binom{s-k-1}{k-1}\binom{n-s-1}{k-1}
 z^{2n-2k}(1+z)^{2n-2s+2k}.
\end{aligned}} \tag{3}
\]
In particular, with \(k=\lfloor n/3\rfloor\) and \(r=n-3k\),
\[
\boxed{\gamma_{rI}(C_n\circ K_1)=2n-2\lfloor n/3\rfloor,\qquad
|\{\text{minimum RID functions}\}|=\frac nk\binom{r+2k-1}{2k-1}.} \tag{4}
\]
This counts functions, not merely the number of minimum weights or the number of root subsets.

## Assumptions and scope
All graphs are finite, undirected and simple. Every root \(v\) has exactly one new leaf \(v'\); no other edges are added. In expressions such as \(G[S]\) the induced subgraph is meant. An empty induced graph has no isolated vertices by convention. The polynomial variable \(z\) is formal; formulas are coefficientwise identities of polynomials over the integers, not asymptotic statements. Formulas (1) and (2) hold for every \(n\ge0\), and the cycle formulas (3) and (4) hold for every \(n\ge3\).

## Proof
**Leaf and zero-set lemma.** An RID function cannot assign \(0\) to a private leaf \(v'\). If its unique neighbor \(v\) also has label \(0\), then its open-neighborhood label sum is \(0\), violating Italian domination. If \(v\) has positive label, the zero leaf is isolated among zero vertices, violating restraint. Hence every leaf has label \(1\) or \(2\). It follows that the zero vertices are precisely the zero-labeled roots \(S\), and the restraint condition says exactly that \(S\) is admissible.

Fix an admissible \(S\). A root outside \(S\) has either label \(1\) or \(2\), and so does its leaf, independently, giving \((z+z^2)^2\) per outside root. A zero root \(v\in S\) has at least one zero-labeled root neighbor by admissibility. If \(v\) also has a root neighbor outside \(S\), that positive neighbor together with leaf label \(1\) already gives an open-neighborhood label sum of at least \(2\). Its leaf is freely labeled \(1\) or \(2\). There are \(b_G(S)\) such boundary roots, each contributing \(z+z^2\). For each of the remaining \(|S|-b_G(S)\) zero roots all root neighbors have label \(0\), so its leaf must be labeled \(2\), contributing \(z^2\). No other restrictions remain: every positive vertex imposes no Italian or restraint condition. Hence the contribution of exactly this \(S\) is
\[
(z+z^2)^{2(n-|S|)+b_G(S)}(z^2)^{|S|-b_G(S)}
=z^{2n-b_G(S)}(1+z)^{2n-2|S|+b_G(S)}.
\]
Summing disjointly over all admissible \(S\) proves (1), including isolated vertices of \(G\) (which cannot lie in \(S\)).

Every summand has a nonzero constant coefficient after removing its lowest power of \(z\). There can be no cancellation because coefficients are nonnegative. Thus the least exponent in (1) is \(2n-B(G)\); for each maximizing \(S\), the least-weight labeling is uniquely obtained by giving every outside root and its leaf label \(1\), every boundary-zero leaf label \(1\), and every interior-zero leaf label \(2\). This proves both assertions of (2).

**Cycle decomposition.** For \(G=C_n\), the admissible root sets consist of the empty set, the full vertex set, and proper nonempty sets whose cyclic runs of selected vertices all have length at least \(2\). A proper such set having \(k\) selected runs has at least \(2k\) selected and \(k\) unselected vertices; hence \(1\le k\le\lfloor n/3\rfloor\). Conversely, every cyclic alternating collection of \(k\) selected runs of lengths at least \(2\) and \(k\) gaps of lengths at least \(1\) is admissible. Exactly the two endpoints of each selected run are boundary vertices, including a run of length \(2\); thus \(b_{C_n}(S)=2k\). The empty and full sets have boundary zero.

Fix a selected-set size \(s\). Splitting \(s\) vertices into \(k\) ordered selected runs of lengths at least \(2\) has \(\binom{s-k-1}{k-1}\) possibilities. Splitting the other \(n-s\) vertices into \(k\) ordered positive gaps has \(\binom{n-s-1}{k-1}\) possibilities. There are \(n\) choices for the start of a distinguished selected run; division by \(k\) removes the overcount from the \(k\) possible distinguished runs. Accordingly the coefficient for this selected profile is \(\frac nk\binom{s-k-1}{k-1}\binom{n-s-1}{k-1}\). Inserting the boundary and size statistics into (1), and adding the empty- and full-selected-set contributions, gives (3).

A proper admissible cycle set with \(k\) runs has exactly \(2k\) boundary vertices, while the empty and full sets have zero. Taking \(k=\lfloor n/3\rfloor\) is possible by alternating \(k\) blocks of two selected vertices and one unselected vertex, distributing the remaining \(r\) vertices freely among those runs and gaps. This maximizes boundary, proving the minimum in (4). There are \(\binom{r+2k-1}{2k-1}\) weak compositions of the surplus \(r\) into the \(2k\) cyclic run/gap blocks. With \(n\) choices of an anchored starting position and division by the \(k\) possible anchors, their number is \(\frac nk\binom{r+2k-1}{2k-1}\). Formula (2) identifies that count with the number of minimum RID functions, completing (4).

## Verification
The accompanying pure-standard-library script `verify.py` compares the exact profile polynomial (1) with direct enumeration of **all ternary labels on both roots and leaves**, allowing zero leaves at the outset. It checks all \(76\) simple graphs on at most four vertices, plus \(35\) reproducibly sampled graphs of order five and six. For every cycle order \(3\le n\le11\), it compares the closed polynomial (3) with the profile sum (1), and verifies the minimum and minimum-function count (4). Direct enumeration is also performed on cycles through order seven. Its captured output is `verification_output.txt`; run `python verify.py` from a directory containing the script. These finite checks confirm the implementation on the tested instances; the proof above establishes the statements for all permitted orders.

## Relationship to prior work
Samadi, Alishahi, Masoumi and Mojdeh defined restrained Italian domination (equivalently restrained Roman \(\{2\}\)-domination), established hardness, bounds, and extremal graph characterizations. Those facts and definitions are taken as prior work. The present assertion is the exact all-weight enumerator for every leaf corona, its internal-boundary optimization identity, and the complete sunlet weight polynomial with a minimum-function census; it is not a claim to have introduced the domination parameter or the graph operation.

Velmurugan and Kala studied the *restrained domination polynomial* of corona graphs, which counts sets obeying ordinary restrained domination rather than ternary RID functions. Abdulhasan and Mojdeh studied minimum restrained Italian and total restrained Italian numbers, including some corona graphs. Only abstract-level material was accessible for those two works, so potential overlap with their special numerical cases is explicitly unresolved; no inference of full-document noncoverage is made from their abstracts. A complete, independently checked comparison with every historical article is not claimed.

## Limitations
The exact universal expression (1) sums over admissible vertex subsets and is not claimed to be a polynomial-time algorithm for arbitrary \(G\); hard instances may remain exponential. The run/gap expression (3) concerns single-leaf coronas of simple cycles, not multi-leaf coronas or arbitrary unicyclic graphs. The finite computations are tests, not a proof of an infinite claim. The uninspected full text of a plausible 2023 corona-related paper leaves a genuine originality risk even though its described scalar results do not by themselves imply the complete weight enumerator.

## References
1. B. Samadi, M. Alishahi, I. Masoumi and D. A. Mojdeh, *Restrained Italian domination in graphs*, arXiv:2009.12209v1 (first posted 2020-09-25); RAIRO Operations Research 55 (2021), 319–332, DOI: 10.1051/ro/2021022. https://arxiv.org/abs/2009.12209
2. S. Velmurugan and R. Kala, *Restrained domination polynomial of join and corona of graphs*, Discrete Mathematics, Algorithms and Applications 15 (2023), 2250118, DOI: 10.1142/S179383092250118X.
3. A. M. Ridha Abdulhasan and D. A. Mojdeh, *Further results on (total) restrained Italian domination*, Discrete Mathematics, Algorithms and Applications 16 (2024), 2350017, DOI: 10.1142/S1793830923500179 (online 2023).
4. A. Almulhim and collaborators, *Survey on Roman \(\{2\}\)-Domination*, Mathematics 12 (2024), 2771, DOI: 10.3390/math12172771.
