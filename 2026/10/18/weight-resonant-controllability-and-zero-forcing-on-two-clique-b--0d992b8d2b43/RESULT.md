# Weight-resonant controllability and zero forcing on two-clique barbells

## Finding

Let \(p,q\ge3\). Take a clique of order \(p\) and one of order \(q\); join one designated vertex from each clique by a single bridge. Assign common positive edge conductance \(a\) inside the first clique, common positive conductance \(b\) inside the second, and any positive bridge conductance \(c\). Let \(L\) be the weighted combinatorial Laplacian. For a set \(T\) of controlled vertices, let \(B_T\) have the distinct coordinate vectors at those vertices as its columns, so the controlled dynamics is \(\dot z=-Lz+B_Tu\).

Write \(U\) and \(V\) for the sets of nonbridge vertices in the first and second cliques, of sizes \(p-1\) and \(q-1\). **Complete leader-set theorem.** For *every* \(T\subseteq V(G)\), the pair \((-L,B_T)\) is controllable if and only if
\[
|T\cap U|\ge p-2,\qquad |T\cap V|\ge q-2,
\]
and, when \(ap=bq\), additionally \(|T|\ge p+q-3\). No extra requirement occurs when \(ap\ne bq\). In particular the criterion is independent of every \(c>0\).

Thus the exact minimum number of independently actuated vertices is
\[
\gamma(G;a,b,c)=\begin{cases}p+q-4,&ap\ne bq,\\p+q-3,&ap=bq.\end{cases}
\]
In the nonresonant case, the \((p-1)(q-1)\) minimum sets consist of all but one nonbridge vertex in each clique, without either bridge vertex. At resonance, the \(2pq-p-q\) minimum sets consist of such a baseline set plus exactly one of its four omitted vertices.

Define the controllability-set enumerator \(\mathcal C(x)=\sum_{T:\,(-L,B_T)\text{ controllable}}x^{|T|}\). Its exact polynomial is
\[
\mathcal C(x)=x^{p+q-4}(x+p-1)(x+q-1)(1+x)^2-\mathbf{1}_{\{ap=bq\}}(p-1)(q-1)x^{p+q-4}.
\]
The zero-forcing sets of the underlying unweighted graph are **exactly** the sets satisfying the two nonbridge count inequalities and \(|T|\ge p+q-3\). Hence at resonance every controllable set is zero forcing, while off resonance the only extra controllable sets are precisely those \((p-1)(q-1)\) smaller baseline sets. The previously established zero-forcing polynomial is recovered at resonance, not claimed anew.

## Assumptions and scope

The vertex sets of the two cliques are disjoint. Their distinguished bridge endpoints are \(s\) and \(t\); the unmarked vertices are \(U\) and \(V\). All internal edges of each clique have the same indicated positive weight; the single cross-clique edge has weight \(c>0\). The Laplacian is \(L_{ii}=\sum_{j\ne i}w_{ij}\) and \(L_{ij}=-w_{ij}\) for distinct vertices. Each selected vertex has **its own independently adjustable scalar input**, not one broadcast control. A finite undirected graph with the given fixed weighted Laplacian is considered, not generic structural controllability under arbitrary edge weights.

A zero-forcing process begins with \(T\) colored blue and repeatedly colors a white vertex blue whenever it is the only white neighbor of some blue vertex. The result applies for every integer \(p,q\ge3\), all positive real \(a,b,c\), and every vertex subset \(T\). The bridge-weight boundary \(c=0\), nonuniform weights within a clique, and cliques of order below three are excluded.

## Proof

**1. Twin-eigenspace necessity.** Every vector supported on \(U\) whose coordinates there sum to zero is an eigenvector of \(L\) with eigenvalue \(ap\). The space has dimension \(p-2\). Likewise the zero-sum space on \(V\) has dimension \(q-2\) and eigenvalue \(bq\). The symmetric-matrix Popov--Belevitch--Hautus criterion states that \((-L,B_T)\) is controllable exactly when no nonzero eigenvector of \(L\) vanishes on \(T\). If fewer than \(p-2\) vertices of \(U\) are selected, the first eigenspace contains a nonzero vector vanishing on \(T\); likewise for \(V\). Therefore both count inequalities are necessary.

**2. The only possible obstruction after twin coverage.** Suppose the count inequalities hold. Choose \(T_0\subseteq T\) containing exactly \(p-2\) vertices of \(U\) and exactly \(q-2\) vertices of \(V\). Write \(u\) and \(v\) for the coordinates of a hypothetical eigenvector at the unique vertices of \(U\setminus T_0\) and \(V\setminus T_0\); write \(s_0,t_0\) for its coordinates at the bridge endpoints. Assume all coordinates on \(T_0\) vanish. At any selected nonbridge vertex of the first clique, the eigenvector equation gives \(-a(u+s_0)=0\), hence \(s_0=-u\); similarly \(t_0=-v\). Because the clique coordinate sums now vanish, the equations at the two omitted nonbridge vertices give
\[
(ap-\lambda)u=0,\qquad (bq-\lambda)v=0.
\]
The equation at the first bridge endpoint, after substituting \(s_0=-u\), gives
\[
(\lambda-ap)u+c(v-u)=0.
\]
If \(u=0\), positivity of \(c\) forces \(v=0\), and the eigenvector is zero. Thus a nonzero invisible eigenvector has \(u\ne0\), whence \(\lambda=ap\), \(v=u\), and \(\lambda=bq\). Conversely, if \(ap=bq\), the vector taking value \(+1\) at each omitted nonbridge vertex, \(-1\) at each bridge endpoint, and \(0\) at \(T_0\) is directly checked to be a Laplacian eigenvector with eigenvalue \(ap=bq\). Therefore \(T_0\) is controllable if and only if \(ap\ne bq\); at equality, its entire invisible eigenspace is the one-dimensional span of this explicit vector.

**3. Additional actuators and exact counts.** The resonant invisible vector is nonzero at all four vertices outside \(T_0\). Choosing *any* additional vertex for actuation eliminates it, so the PBH criterion holds. Conversely at resonance, a set of total size \(p+q-4\) satisfying both twin coverage conditions must be one such \(T_0\) and is uncontrollable. Controllability is monotone in the controlled set. This proves the complete leader-set criterion, the minimum counts and the count \(2(p-1)(q-1)+(p-1)+(q-1)=2pq-p-q\) of resonant minima. The nonresonant minimum count is \((p-1)(q-1)\). The enumerator follows by independently choosing either \(p-2\) or \(p-1\) vertices of \(U\), either \(q-2\) or \(q-1\) vertices of \(V\), and any subset of the two bridge endpoints, then deleting precisely the resonantly forbidden baseline choices.

**4. Exact comparison with zero forcing.** If two or more nonbridge vertices of either clique start white, no first forcing step can color any of them: every blue vertex adjacent to one is also adjacent to the other. Thus both count inequalities are necessary for zero forcing. With exactly \(p-2\) initial blue nonbridge vertices in each clique and neither bridge endpoint blue, every blue vertex has two white neighbors; no forcing step is possible. In all other cases meeting twin coverage, there is an extra selected vertex: either all nonbridge vertices on one side are already blue, allowing the nearby bridge endpoint to be forced, or a bridge endpoint is blue, allowing the one omitted nonbridge vertex to be forced. Once that side is completely blue, the bridge forces the opposite bridge endpoint, after which any remaining single white vertex in the other clique is forced. Hence zero forcing holds exactly for the criterion stated above with the extra total-size condition, regardless of conductances. This completes the claimed equivalence at resonance and the exact description of the nonresonant difference.

## Verification

Run the self-contained `python3 verify.py` script supplied with this result. It builds the weighted Laplacian, constructs the Kalman reachability matrix, computes its rank over the prime field with modulus \(1000000007\), and independently runs the zero-forcing process for all vertex subsets in \(36\) weighted examples with \(3\le p,q\le5\). It checks the full leader-set criterion, polynomial coefficients, minimum actuator counts, and the inclusion of zero-forcing sets among controllable sets. The completed run reported `VERIFY_OK 37704 finite assertions across 36 weighted cases (3<=p,q<=5), using exact prime-field ranks`. Prime-field rank is a finite consistency check only; it does not replace the real-field proof or prove the infinite-family claim.

## Relationship to prior work

Parlangeli and Notarstefano developed multi-input Laplacian PBH criteria and complete classifications for paths and cycles [1]. Notarstefano and Parlangeli treated Cartesian grid networks [2]. Aguilar and Gharesifard studied graph controllability classes, emphasizing binary broadcast-input vectors rather than complete independent-terminal-input enumeration on weighted bridge barbells [3]. Hsu analyzed composites of single-input-controllable cell graphs [4], a different domain because cliques of order at least three do not have single-vertex Laplacian controllability. Dai's later general minimal-leader framework studies different families [5]. A published result gives the zero-forcing polynomial of two cliques joined by one bridge [6]. The zero-forcing enumeration and zero-forcing minimum are therefore background, while the conductance resonance, the full fixed-Laplacian controllability classification, and its exact agreement/divergence from zero forcing are the subject here.

The literature searches included the aliases *two-clique barbell*, *dumbbell*, *bridge-linked cliques*, *minimum leader selection*, *PBH vertex controllability*, *twin eigenspaces*, and *zero forcing*. No inspected result explicitly provided the weight-resonant iff criterion. This is a comparison of inspected materials, not a proof of absolute originality.

## Limitations

The theorem assumes two complete components connected by exactly one positive bridge and uniform positive conductance in each component. It does not describe generic arbitrary internal edge weights, multiple bridge edges, single broadcast actuation, controllability Gramian conditioning, or robustness under measurement noise. At exact resonance an arbitrarily small perturbation of the internal conductance ratio restores the additional minimum placements, but near-resonant numerical conditioning is not quantified. The finite verification covers small instances only. Distinctly worded or unindexed coverage in the general control literature remains a residual originality risk. Independent mathematical audit has not been performed.

## References

[1] G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556 (first posted 2011-09-16), https://arxiv.org/abs/1109.3556.

[2] G. Notarstefano and G. Parlangeli, *Controllability and observability of grid graphs via reduction and symmetries*, arXiv:1203.0129 (first posted 2012-03-01), https://arxiv.org/abs/1203.0129.

[3] C. O. Aguilar and B. Gharesifard, *Graph Controllability Classes for the Laplacian Leader-Follower Dynamics*, IEEE Transactions on Automatic Control 60 (2015), 1611–1623, DOI 10.1109/TAC.2014.2381435.

[4] S.-P. Hsu, *Laplacian Controllability of Interconnected Graphs*, arXiv:1808.03022 (2018), https://arxiv.org/abs/1808.03022.

[5] L. Dai, *Minimum leader selection for controllability of undirected graphs with leader–follower framework*, IET Control Theory & Applications 17 (2023), 505–515, DOI 10.1049/cth2.12385.

[6] *Zero forcing polynomial of bridge barbells*, published mathematical research record (2026-10-04), identifier 5431b532d7f2. Its zero-forcing enumeration is prior work, not claimed here.
