# All minimal zero forcing sets and the upper zero forcing number of spider trees
## Finding
Let \(T=S(\ell_1,\ldots,\ell_k)\) be a spider tree with center \(c\), \(k\ge3\), and leg \(i\) written \(v_{i,1},\ldots,v_{i,\ell_i}\) from the center outward. Every minimal zero forcing set meets exactly \(k-1\) legs. It is either centered, namely \(\{c\}\cup\{v_{i,1}:i\ne j\}\) for one omitted leg \(j\), with every represented leg satisfying \(\ell_i\ge2\); or it is noncentered, with one omitted leg and each represented leg contributing exactly one root singleton \(\{v_{i,1}\}\) (allowed when \(\ell_i\ge2\)), one leaf singleton \(\{v_{i,\ell_i}\}\), or one adjacent non-leaf pair \(\{v_{i,t},v_{i,t+1}\}\) with \(1\le t\le\ell_i-2\). In the noncentered case at least one leaf singleton or adjacent pair is required, and if a pair with \(t=1\) occurs then it is the unique such trigger. Conversely every set of these forms is minimal zero forcing. If \(q=|\{i:\ell_i=1\}|\) and \(L=|\{i:\ell_i\ge4\}|\), then \[\overline Z(T)=k-1+\max\!\left(\mathbf 1_{\{q\le1\}},\min(k-1,L)\right).\]

## Assumptions and scope
All graphs are finite and simple. A spider tree has one center \(c\) of degree \(k\ge3\), with \(k\) path legs. Write leg \(i\) as
\[
v_{i,1},v_{i,2},\ldots,v_{i,\ell_i},
\]
where \(v_{i,1}\) is adjacent to \(c\) and \(v_{i,\ell_i}\) is the leaf. A zero forcing set is an initial blue set from which the standard rule—any blue vertex with exactly one white neighbor forces that neighbor blue—eventually colors the whole graph. A minimal zero forcing set has no proper zero forcing subset. The upper zero forcing number \(\overline Z(T)\) is the maximum size of a minimal zero forcing set.

## Proof
A zero forcing set must meet at least \(k-1\) legs. If two legs contain no initially blue vertex, the center has at least two white neighbors until one of those legs is entered, so it cannot force into either one. For a minimal zero forcing set, exactly \(k-1\) legs are represented; this is the standard generalized-star observation, and it also follows by deleting a redundant seed when all \(k\) legs are represented.

First suppose \(c\notin S\), and let leg \(j\) be the unique omitted leg. Until the center becomes blue, it cannot help a represented leg while the omitted root remains white. Thus every represented leg must either already contain its root or be able to force inward to the root by itself.

The inclusion-minimal local possibilities on a represented path are exactly:
\[
\{v_{i,1}\}\quad(\ell_i\ge2),\qquad
\{v_{i,\ell_i}\},\qquad
\{v_{i,t},v_{i,t+1}\}\quad(1\le t\le\ell_i-2).
\]
The first is a passive root singleton. A leaf singleton forces inward and is a trigger. An adjacent non-leaf pair forces in both directions and is also a trigger. A pair containing the leaf is not minimal because the leaf alone suffices; a nonadjacent pair cannot start the required inward forcing without containing a smaller sufficient seed; and three or more selected vertices on one leg contain a proper sufficient local subset.

At least one trigger is necessary, since root singletons alone never color the center. Once a trigger colors the center, every passive root singleton can finish its leg, and after the represented legs are complete the center enters the omitted leg.

There is one compatibility rule. If the shallow pair \(\{v_{i,1},v_{i,2}\}\) occurs together with another trigger, deleting \(v_{i,2}\) leaves a passive root singleton, and the other trigger still colors the center; hence the set was not minimal. If the shallow pair is the unique trigger, deleting either member destroys the only mechanism that colors the center. For a deep pair with \(t\ge2\), deleting either member leaves a single internal vertex that cannot start a force even after the center is colored, so both vertices are essential. Removing a root singleton or leaf trigger leaves two legs without usable initial data: its leg and the omitted leg. Hence the noncentered classification is necessary and sufficient.

Now suppose \(c\in S\). Minimality excludes leaves and vertices farther than one step from the center: such a vertex either supplies a forcing chain that makes the center redundant, or can later be forced from the center side. Therefore every represented leg contributes exactly its nonleaf root \(v_{i,1}\), and exactly one leg is omitted. Thus
\[
S=\{c\}\cup\{v_{i,1}:i\ne j\},
\]
with \(\ell_i\ge2\) for every represented leg. This set is zero forcing: the center fills the omitted leg, then the selected roots fill their legs. It is minimal because deleting the center leaves every selected root with two white neighbors, while deleting a selected root leaves two unseeded legs.

For the maximum size, the baseline is one selected local seed on each of \(k-1\) represented legs. A centered set adds one vertex and exists exactly when at most one leg has length one, so it contributes the alternative \(\mathbf 1_{\{q\le1\}}\).

In a noncentered set, every adjacent pair contributes one extra vertex. If two or more pair triggers occur, no pair may be shallow, so every doubled leg must support a deep pair and therefore have length at least four. Hence at most \(\min(k-1,L)\) extra vertices are possible, and this bound is attained by using a deep pair on every represented long leg and suitable singleton seeds elsewhere. Therefore
\[
\overline Z(T)=k-1+\max\!\left(\mathbf 1_{\{q\le1\}},\min(k-1,L)\right).
\]
Since the ordinary zero forcing number of a \(k\)-leg spider is \(k-1\), the spider is well-forced exactly when \(q\ge2\) and \(L=0\), recovering the known criterion that at least two legs have length one and every leg has length at most three.

## Verification
The included checker constructs every spider arm-length profile of orders \(4\) through \(13\). For each graph it tests every vertex subset by directly simulating standard zero forcing and checks inclusion-minimality by deleting each selected vertex. Independently, it generates exactly the centered and noncentered families in the theorem and compares the collections. It also checks the upper formula and the minimum value \(k-1\).

## Relationship to prior work
The 2022 paper *Minimal Zero Forcing Sets* introduced the upper zero forcing number and already used spiders as a major source of nonminimum minimal sets. It constructs minimal sets from adjacent internal pairs on long legs and explicitly classifies a special spider with many length-one legs and one long leg. Those results are contained in the theorem above, but they do not give an all-spider classification or a closed upper-zero-forcing formula.

The 2023 paper *Well-forced graphs* proves that a minimal zero forcing set on a generalized star meets exactly all but one leg. It also characterizes well-forced generalized stars: at least two legs have length one and every leg has length at most three. The present formula strictly refines that equality criterion by determining the exact upper value in every remaining arm-length profile, while the local description classifies every minimal set.

Targeted searches for the upper zero forcing number and minimal zero forcing sets together with spider or generalized-star terminology located these primary sources and later zero-forcing work on different questions, but no equivalent all-profile formula or classification.

## Limitations
The theorem concerns standard zero forcing on spiders with one branching center. It does not classify minimal zero forcing sets of arbitrary trees with several major vertices. The exhaustive computation through order \(13\) is finite corroboration only; the arbitrary-length result follows from the proof. Literature searches cannot exclude a differently phrased or non-indexed equivalent result.

## References
1. B. Brimkov, J. Carlson, “Minimal Zero Forcing Sets,” arXiv:2204.01810v1, 4 April 2022; Australasian Journal of Combinatorics 90 (2024), 363–377.
2. C. Grood, R. Haas, B. Jacob, E. King, S. Nasserasr, “Well-forced graphs,” arXiv:2312.14298v1, 21 December 2023; Graphs and Combinatorics 40 (2024), 129, DOI 10.1007/s00373-024-02827-z.
