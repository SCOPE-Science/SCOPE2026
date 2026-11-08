# A double-toppling extreme avalanche on cocktail-party graphs

## Finding

Let \(m\ge2\) be an integer, and let \(G_m=K_{2m}\setminus M\), where \(M\) is a perfect matching. Choose one matched pair \(\{s,u\}\), declare \(s\) the sink, and add one grain at \(u\). Each vertex has degree \(d=2m-2\). The initial sandpile is uniform on the recurrent stable configurations for the usual undirected Abelian sandpile.

Write \(T\) for the total **individual topplings** in the resulting principal avalanche. Then

\[
\max T=2m,\qquad
\Pr(T=2m)=\frac{(2m-3)^{m-1}(2m-1)^{m-2}}{(2m-2)^m(2m)^{m-2}},\qquad
\mathbb E[T]=\frac{2m}{2m-2}.
\]

The event \(T=2m\) occurs **exactly** when \(u\) topples twice and each of the other \(2m-2\) non-sink sites topples once. Its maximizing recurrent configurations are in bijection with the recurrent configurations of the smaller graph obtained by deleting \(u\), retaining \(s\) as the sink, and retaining the original edges. There are exactly

\[
(2m-3)^{m-1}(2m-1)^{m-2}
\]

such configurations. As \(m\to\infty\),

\[
\Pr(T=2m)\sim\frac{1}{2em},\qquad
\frac{(2m)\Pr(T=2m)}{\mathbb E[T]}\longrightarrow e^{-1}.
\]

Thus a probability-order-\(m^{-1}\) class of system-spanning events, each with one double toppling, carries a nonzero limiting fraction of the total mean toppling activity.

## Assumptions and scope

Every edge of \(G_m\) has weight one; there is exactly one absorbing sink and the drive is its unique nonneighbor \(u\). A stable height at each nonsink vertex lies in \(\{0,1,\ldots,d-1\}\). A vertex topples upon reaching height at least its degree, sending one grain along each incident edge, with grains reaching \(s\) removed. The uniform measure is over **all recurrent stable heights**, not over all stable heights. The theorem applies to all integers \(m\ge2\), including \(G_2=C_4\), and concerns single-grain additions only.

For reference, the exact probabilities for \(m=2,3,4\) are \(1/4\), \(15/128\), and \(6125/82944\), respectively, and the corresponding means are \(2,3/2,4/3\).

## Proof

**1. An upper bound on the odometer.** Let \(\Delta\) be the reduced graph Laplacian. Index the nonsink sites with \(u\) first, followed by \(W=V(G_m)\setminus\{s,u\}\), so \(|W|=d\). The vector \(q\) with \(q_u=2\) and \(q_v=1\) for \(v\in W\) satisfies

\[
\Delta q=d\,\mathbf e_u.
\]

Indeed, \(u\) has all \(d\) vertices of \(W\) as neighbors; each \(v\in W\) has \(u\), the sink, and exactly \(d-2\) other neighbors in \(W\). For any stable \(c\), the coordinate values of \(c+\mathbf e_u-\Delta q\) are at most \(d-1\): they are \(c_u+1-d\le0\) at \(u\) and \(c_v\le d-1\) elsewhere. The least-action upper-bound lemma therefore implies that the actual legal stabilization odometer \(t\) satisfies \(0\le t\le q\) coordinatewise. The lemma holds even when the *comparison* configuration has negative entries: at the first attempted toppling exceeding \(q\), its site would have height below the instability threshold, since no other site has yet exceeded \(q\). Consequently \(T\le2+d=2m\) for every stable initial state. Equality forces \(t=q\).

**2. Burning reduction and exact equality characterization.** Define \(H_m=G_m-u\), retaining the sink \(s\). The vertices of \(W\) form a cocktail-party graph on \(2m-2\) vertices; in \(H_m\), each is additionally adjacent to \(s\). Its degree is \(d-1\). Let \(h=(h_v)_{v\in W}\) be a stable configuration on \(H_m\), with \(0\le h_v\le d-2\). Define \(c(h)\) on \(G_m\) by

\[
c(h)_u=d-1,\qquad c(h)_v=h_v+1\quad(v\in W).
\]

The following equivalence is exact:

\[
\bigl(c(h)\text{ is recurrent and its addition at }u\text{ has }t=q\bigr)
\quad\Longleftrightarrow\quad h\text{ is recurrent on }H_m.
\]

For the forward implication, \(t=q\) first requires \(c_u=d-1\), since \(u\) is initially the only site that can be unstable. It then topples, leaving zero grains at \(u\), and cannot topple a second time until **every** site of \(W\) has toppled once. To make a vertex of \(W\) topple, its initial height must be at least one: it can receive at most \(1+(d-2)=d-1\) grains from other sites before its first toppling. Thus all \(c_v-1\) are nonnegative. After the first toppling of \(u\), the remaining sites begin at \(c_v+1=(c_v-1)+2\); compare this with Dhar's sink-burning test for \(H_m\), which starts at \((c_v-1)+1\) and uses thresholds \(d-1\) instead of \(d\). The heights in the two tests differ constantly by one at every stage. Hence all sites of \(W\) topple exactly once in the original process if and only if \(h_v=c_v-1\) passes the burning test on \(H_m\). This proves necessity.

For sufficiency, take an \(H_m\)-recurrent \(h\). By the burning criterion on \(H_m\), after the sink contributes one grain to every vertex in \(W\), there exists a legal sequence toppling each \(W\)-site once. Adding one grain at \(u\) to \(c(h)\) makes \(u\) topple first. The subsequent \(W\)-process is precisely the \(H_m\) burning sequence with each height and its threshold increased by one; thus each \(W\)-site topples once, after which \(u\) has received its \(d\) grains and topples a second time. The resulting heights are stable, and the odometer equals \(q\). Moreover, \(c(h)\) is recurrent: in the sink-burning test for \(G_m\), topple the \(W\) sites according to the same \(H_m\) burning order and then topple \(u\) last. Every step is legal, and this restores \(c(h)\), completing Dhar's criterion. Therefore the maximizing configurations correspond bijectively to \(\operatorname{Rec}(H_m)\).

**3. Exact enumeration.** The Laplacian of the cocktail-party graph on \(2r\) vertices has eigenvalues \(0\) once, \(2r-2\) with multiplicity \(r\), and \(2r\) with multiplicity \(r-1\). To see this, write its adjacency matrix as \(\mathbf J-\mathbf I-P\), where \(P\) exchanges the matched partners; separate constants, pair-antisymmetric vectors, and zero-sum pair-symmetric vectors.

With \(r=m-1\), the sink-reduced Laplacian of \(H_m\) is the internal cocktail-party Laplacian plus the identity. Its eigenvalues are \(1\) once, \(2m-3\) with multiplicity \(m-1\), and \(2m-1\) with multiplicity \(m-2\). The matrix-tree theorem and sandpile-group cardinality give

\[
|\operatorname{Rec}(H_m)|=\det\Delta_{H_m}=(2m-3)^{m-1}(2m-1)^{m-2}.
\]

Similarly, \(G_m\) has \(\det\Delta_{G_m}=(2m-2)^m(2m)^{m-2}\) spanning trees and recurrent configurations. Dividing yields the stated probability.

**4. Exact expectation.** Grain addition at \(u\) permutes the finite recurrent-state group, so if \(t\) is the random odometer, stationarity yields \(\Delta_{G_m}\mathbb E[t]=\mathbf e_u\). By the symmetries fixing \(s,u\), every vertex of \(W\) has the same mean topplings \(x\), while \(u\) has mean \(y\). The reduced Laplacian equations give \(dy-dx=1\) and \(2x-y=0\), hence \(x=1/d\) and \(y=2/d\). Summation gives \(\mathbb E[T]=(d+2)/d=2m/(2m-2)\).

**5. Rare-event limit.** Algebraically,

\[
(2m-2)\Pr(T=2m)=
\left(1-\frac1{2m-2}\right)^{m-1}
\left(1-\frac1{2m}\right)^{m-2}\longrightarrow e^{-1}.
\]

Multiplying by \(2m/(\mathbb E[T])=2m-2\) gives the limiting share of the mean.

## Verification

The self-contained programs `verify_exhaustive.py` and `verify_reduction.py`, included with this result, independently test the theorem. From the directory containing those files, run:

```bash
python verify_exhaustive.py
python verify_reduction.py
```

The first independently enumerates every stable configuration for \(m=2,3,4\), applies Dhar's burning test, stabilizes each recurrent configuration by explicit legal topplings, and checks the extremal event counts, sharp maximum and mean. The second computes exact determinants of both relevant reduced Laplacians for \(2\le m\le10\), checks the exact Green-function system, enumerates recurrent configurations of the deleted-vertex graph through \(m=4\), and verifies the explicit bijection and extreme-event stabilization. Finite checks confirm cases; the all-\(m\) statements depend on the proof above.

## Relationship to prior work

The original Abelian sandpile and Dhar's burning criterion are foundational. Austin et al. (2016), specifically their sections on complete graphs and wheels, give exact avalanche polynomials for other graph families and state the one-toppling bound when the drive vertex is **adjacent** to the sink. Here the driving vertex is instead the sink's unique nonneighbor, with a sharp **two-toppling** extreme event; the explicit cocktail-party enumeration is not implied by the complete-graph formula. Dukes and Selig (2016) develop recurrence decompositions for edge-duplicated graphs and cut-vertex constructions; neither mechanism directly yields the dense, two-connected cocktail-party family with this event condition. Aval et al. (2013) classify recurrent configurations for complete bipartite graphs, whose sink-drive adjacency and missing-edge geometry differ. The exact one-vertex-deletion burning reduction and \(e^{-1}\) activity-share law are the specific contributions proposed here. No universal priority claim is made outside examined literature.

## Limitations

The theorem is for equal unit edges, one sink, the matched drive vertex, and uniform recurrent initial data. It does not give the entire avalanche-size polynomial, other drive locations, disorder, stochastic toppling, or a thermodynamic-limit law for all avalanche sizes. The mathematical proof is analytic; exhaustive testing covers only indicated finite cases. A self-review was performed, but there is no independent audit, and unindexed prior statements could affect historical priority.

## References

1. D. Dhar, “Self-organized critical state of sandpile automaton models,” *Physical Review Letters* **64** (1990), 1613–1616. https://doi.org/10.1103/PhysRevLett.64.1613
2. D. Austin, M. Chambers, R. Funke, L. D. García Puente and L. Keough, “The Avalanche Polynomial of a Graph,” first public arXiv version May 9, 2016. https://arxiv.org/abs/1605.02713
3. J.-C. Aval, M. D'Adderio, M. Dukes and Y. Le Borgne, “Two operators on sandpile configurations, the sandpile model on the complete bipartite graph, and a Cyclic Lemma,” arXiv first public July 29, 2013. https://arxiv.org/abs/1307.7740
4. M. Dukes and T. Selig, “Decomposing recurrent states of the abelian sandpile model,” *Electronic Notes in Discrete Mathematics* **54** (2016), 97–102. https://doi.org/10.1016/j.endm.2016.09.018
5. R. Cori, A. Micheli and D. Rossin, “Avalanche polynomials,” arXiv first public May 18, 2009. https://arxiv.org/abs/0905.2823
