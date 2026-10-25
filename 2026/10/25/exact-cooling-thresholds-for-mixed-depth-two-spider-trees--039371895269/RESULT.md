# Exact cooling thresholds for mixed depth-two spider trees

## Finding
Let \(T_{a,b}\) be the tree formed from a central vertex \(o\) by attaching \(a\) arms of length one and \(b\) arms of length two. For all integers \(a,b\ge1\) with \(a+b\ge3\), its cooling number is
\[
\operatorname{CL}(T_{a,b})=\begin{cases}
3,&b=1,\ a=2,\\
4,&b=1,\ a\ge3,\\
4,&b=2,\\
4,&b=3,\ a=1,\\
5,&b=3,\ a\ge2,\\
5,&b\ge4.
\end{cases}
\]
In particular, when \(b\ge2\), the diameter is four and the graph attains the diameter bound \(\operatorname{CL}=5\) precisely if \(b\ge4\) or \(b=3\) and \(a\ge2\). Within this mixed family the two inclusion-minimal five-round witnesses are \(T_{1,4}\) and \(T_{2,3}\), respectively of orders ten and nine.

## Assumptions and scope
All graphs are finite, simple, undirected and connected. An arm of length one consists of a short leaf \(u_i\) adjacent to the center \(o\). An arm of length two consists of an inner vertex \(y_j\) adjacent to \(o\), and an outer leaf \(x_j\) adjacent only to \(y_j\). The indices satisfy \(1\le i\le a\) and \(1\le j\le b\). The center has degree \(a+b\ge3\).

Cooling starts with all vertices uncooled. In round one, a source is cooled; in every subsequent round the current cooled vertices first cool all their neighbors, and then one still-uncooled vertex is chosen as an additional source if any remains. The process stops at the first round by whose end all vertices are cooled. The cooling number \(\operatorname{CL}(G)\) is the largest possible stopping round, maximizing over source choices. A source first chosen in round \(i\) can cool a vertex at distance at most \(t-i\) by the end of round \(t\). Therefore a feasible ordered source list \((s_1,\ldots,s_k)\) must satisfy \(d(s_i,s_j)\ge j-i+1\) for \(i<j\). A vertex \(v\) remains uncooled after the \(k\)-th source iff \(d(v,s_i)\ge k-i+1\) for every \(1\le i\le k\). These two distance tests will be used below.

## Proof
**Universal upper bounds.** A first source \(s_1\) cools all vertices at distance at most \(t-1\) by the end of round \(t\), irrespective of later sources. Consequently \(\operatorname{CL}(G)\le\operatorname{diam}(G)+1\). For \(b=1\), the diameter is three, giving at most four rounds. For \(b\ge2\), the diameter is four, giving at most five rounds.

**One long arm.** Suppose \(b=1\), with outer leaf \(x\), inner vertex \(y\), and \(a\ge2\) short leaves. Choose \(x\) in round one and any short leaf in round two. At least one unchosen short leaf remains uncooled at the end of round two, so at least three rounds are possible. When \(a\ge3\), choose \(x,u_1,u_2\) in rounds one, two and three. These satisfy the source-distance inequalities (distances \(3,3,2\) compared with thresholds \(2,3,2\)); a third short leaf survives through round three, yielding four rounds.

For \(a=2\), four rounds would require at least two uncooled vertices immediately after propagation in round three: one to select and one to survive after the selection. A first source with eccentricity below three cannot leave any uncooled vertex at that stage. If the first source is a short leaf, the only vertex at distance three from it is \(x\), so no two survivors are possible. If the first source is \(x\), the only distance-three vertices are the two short leaves. The round-two source must be at distance at least two from \(x\), hence is either the center or one short leaf. The former cools both short leaves by propagation in round three; the latter eliminates one short leaf by selection. In neither case can two short leaves remain before selection in round three. Hence \(\operatorname{CL}(T_{2,1})=3\).

**At least two long arms: a four-round construction.** Choose different long arms \(A,B\), with outer leaves \(x_A,x_B\) and inner vertex \(y_B\). Fix any short leaf \(u\). The source list \((x_A,u,y_B)\) is feasible: its pairwise distances are \(3,3,2\), meeting the required bounds \(2,3,2\). At the end of round three, \(x_B\) is still uncooled, as its distances to those sources are \(4,3,1\), respectively. Thus \(\operatorname{CL}\ge4\) whenever \(b\ge2\).

**Excluding five rounds when \(b=2\).** If cooling were to last five rounds, after propagation in round four there would have to be at least two uncooled vertices: one for the round-four source and one to survive it. Any first source with eccentricity at most three has already cooled the graph by that point, so the first source must be an outer long-arm leaf \(x_A\). Every vertex at distance at most three from \(x_A\) is cooled by propagation in round four; the only possible uncooled vertices are outer leaves of other long arms. With \(b=2\) only one such leaf exists. Hence five rounds are impossible.

**Excluding five rounds for \(b=3,a=1\).** Suppose the first source is \(x_A\). For five rounds, both other long outer leaves \(x_B,x_C\) must remain uncooled before choosing the round-four source, because these are the only vertices potentially uncooled then. Thus the round-two source \(s_2\) must be at distance at least three from each of \(x_B,x_C\), as well as distance at least two from \(x_A\). Among the vertices not already selected, only the single short leaf \(u\) satisfies these three conditions, so \(s_2=u\). The round-three source \(s_3\) would have to be at distance at least two from each of \(x_B,x_C\), at least three from \(x_A\), and at least two from \(u\). No vertex satisfies all four conditions: the center is too close to \(x_A\); \(y_A\) is too close to \(x_A\); the inner/outer vertices on arms \(B,C\) are too close to their own outer leaves; and there are no additional short leaves. This contradiction proves \(\operatorname{CL}=4\).

**Five-round constructions.** First suppose \(b\ge4\). Choose four distinct long arms \(A,B,C,D\), and a short leaf \(u\). Use sources \((x_A,y_B,u,x_C)\) in rounds one through four. The six source pairwise distances in lexicographic pair order are \((3,3,4,2,3,3)\), meeting the required lower bounds \((2,3,4,2,3,2)\). The other outer leaf \(x_D\) has distances \((4,3,3,4)\) from the sources, meeting the survival bounds \((4,3,2,1)\). Thus at least five rounds are possible.

Finally suppose \(b=3\) and \(a\ge2\). Choose distinct long arms \(A,B,C\) and two distinct short leaves \(u,v\). Select \((x_A,u,v,x_B)\) in four rounds. The pairwise source distances are \((3,3,4,2,3,3)\), again meeting the required bounds \((2,3,4,2,3,2)\). The outer leaf \(x_C\) has distances \((4,3,3,4)\) from the sources, so is still uncooled after round four. Hence five rounds occur. The diameter upper bounds finish all cases. \(\square\)

The two claimed minimal witnesses follow directly from the classification and deletion of arms: within the mixed family, a five-round spider either has at least four long arms, hence contains \(T_{1,4}\), or has at least three long arms and two short arms, hence contains \(T_{2,3}\); neither smaller mixed subspider has five rounds.

## Verification
The supplementary standard-library-only script `verify_mixed_cooling.py` constructs the graphs and independently computes the longest process by dynamic programming over cooled-vertex bitmasks. For every \(1\le a,b\le6\) satisfying \(a+b\ge3\), the computed optimum equals the formula (35 graph instances). A second implementation checks existence of round-four and round-five sequences using all-pairs distances and source/survival inequalities (30 independent threshold comparisons for \(a,b\le4\)). Both methods agree. The actual executable output is embedded in `verify_mixed_cooling_output.txt`. These are finite cross-checks; the proof above establishes all parameters.

## Relationship to prior work
Bonato, Marbach, Milne and Mishura [1] introduced the cooling number and proved the general diameter bound. Their Theorem 4 discusses spiders with an even number of **equal-length** arms. In particular, the already known even-four-arm length-two result, together with preservation of the distances between vertices of that spider, also implies the \(b\ge4\) portion of the present formula; that portion is not claimed as an independently new extremal principle. The present result instead treats the **mixed** short/long arm class uniformly, identifies the exceptional failures of the diameter bound, and supplies the sharp additional witness \(T_{2,3}\) with three two-edge arms and two pendant edges.

Bonato, Marbach, Marcoux and Mishura [2] study liminal burning, of which cooling is a limiting case, but do not give the present mixed-depth spider classification. Bonato, Carr, Jones, Marbach and Mishura [3], first publicly available June 10, 2026, analyze graph cooling for standard graph products, additional classes of trees, and present open questions on spider cooling. Their graph-product results do not state or imply these one-/two-edge-arm thresholds. A related source about \(2\)-burning spiders [4] concerns a distinct propagation protocol and is not a cooling-number formula.

## Limitations
The classification applies only to mixed spiders with arms of lengths exactly one and two, with at least one arm of each type. It says nothing about arbitrary arm lengths, weighted/directed contagion, or counts of maximizing source sequences. The searched literature and mathematical records do not establish exhaustive publication novelty; an equivalent unindexed characterization remains possible. Independent mathematical review has not been performed.

## References
[1] A. Bonato, T. G. Marbach, H. Milne, T. Mishura, *How to cool a graph*, arXiv:2401.03496 (first posted January 7, 2024). https://arxiv.org/abs/2401.03496

[2] A. Bonato, T. G. Marbach, J. Marcoux, T. Mishura, *Between burning and cooling: liminal burning on graphs*, arXiv:2505.10727 (first posted May 15, 2025). https://arxiv.org/abs/2505.10727

[3] A. Bonato, M. Carr, C. Jones, T. G. Marbach, T. Mishura, *Cooling graph products*, arXiv:2606.12330 (first posted June 10, 2026). https://arxiv.org/abs/2606.12330

[4] C. B. Jacobs et al., *The 2-burning number of a graph*, Ars Combinatoria 161 (2024). https://combinatorialpress.com/article/ars/Volume%20161/the-2-burning-number-of-a-graph.pdf
