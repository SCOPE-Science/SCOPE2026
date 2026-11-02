# Complete welfare and optimal-partition counts on cyclic social-distance networks

## Finding

**Theorem.** Let \(C_n\) be the *labeled simple cycle* on \(n\ge3\) vertices. Under the canonical normalized social-distance utility defined below, the exact maximum total welfare \(M_n\) and the number \(N_n\) of maximizing *set partitions* are:

| Cycle order | Maximum welfare \(M_n\) | Number \(N_n\) | All maximizing coalition patterns |
|---|---|---|---|
| \(n=3\) | \(2\) | \(1\) | grand coalition |
| \(n=4\) | \(5/2\) | \(1\) | grand coalition |
| \(n=5\) | \(3\) | \(1\) | grand coalition |
| \(n=6\) | \(10/3\) | \(4\) | grand coalition, or any of the three two-triple arc partitions |
| \(n=3q\ge9\) | \(5q/3\) | \(3\) | \(q\) consecutive triples |
| \(n=3q+1\ge7\) | \(5q/3+1/2\) | \(n\) | one consecutive quadruple and \(q-1\) consecutive triples |
| \(n=3q+2\ge8\) | \(5q/3+1\) | \(n(q+1)/2\) | either one consecutive pair with \(q\) triples, or two consecutive quadruples with \(q-2\) triples |

Within each row, every cyclic placement of the listed blocks is a maximizer, and no other set partition is. The count treats cycles as labeled, does not identify rotations or reflections, and does not order the coalitions. In particular, the grand coalition ceases to be optimal exactly after order six; at order six it ties with fragmented optima, and at order seven it loses strictly.

## Assumptions and scope

For a finite undirected simple social network \(G\), a coalition is any nonempty vertex subset \(S\). Write \(d_{G[S]}(v,w)\) for the shortest-path length **inside the induced subgraph**, with \(1/\infty=0\). Every agent \(v\in S\) receives

\[
u(v,S)=\frac{1}{|S|}\sum_{w\in S\setminus\{v\}}\frac{1}{d_{G[S]}(v,w)}.
\]

For a set partition \(\Pi\) of all vertices, its welfare is \(\Phi_G(\Pi)=\sum_{S\in\Pi}\sum_{v\in S}u(v,S)\). No connectivity or cardinality restriction is imposed on partitions. All cycles have unit edge lengths, and the objective is the sum, *not* the average, of agent utilities. The theorem is not about Nash stability or the non-normalized score-based variant.

Let \(H_k=\sum_{j=1}^k1/j\), with \(H_0=0\), and set

\[
F(k)=2(H_k-1)\quad(k\ge1),\qquad
Q_n=2H_{\lfloor(n-1)/2\rfloor}+\frac{2}{n}\mathbf1_{2\mid n}.
\]

These are respectively the welfare of the grand coalition of a path of order \(k\) and of the cycle of order \(n\). In particular, \(F(1)=0\), \(F(2)=1\), \(F(3)=5/3\), and \(F(4)=13/6\).

## Proof

**1. Coalition structure and the cost of leaving an isolated vertex.** Splitting any coalition into the connected components of its induced subgraph cannot decrease welfare: the positive distance reciprocals inside each component stay unchanged while the common denominator is replaced by the smaller component order. Splitting is strict if a disconnected coalition has a component of size at least two. Therefore, if an optimum contains any disconnected coalition, every one of its components must be an isolated vertex; refining all disconnected coalitions produces another optimal partition with a singleton.

But no optimal partition with connected coalitions can contain a singleton \(v\). Choose a neighbor of \(v\) in the cycle; its coalition \(S\) is a connected induced path (or another singleton). Joining \(v\) to \(S\) gives a path with one extra vertex, except possibly when \(S\) contains all other cycle vertices, in which case it gives the entire cycle. In the path case the welfare increases by \(F(k+1)-F(k)=2/(k+1)>0\) for \(k=|S|\). In the exceptional cycle-closing case the increase is \(Q_n-F(n-1)>0\), as follows from

\[
Q_{2m}-F(2m-1)=2-2\sum_{j=m}^{2m-1}\frac1j+\frac1m>0,
\]

and

\[
Q_{2m+1}-F(2m)=2-2\sum_{j=m+1}^{2m}\frac1j>0.
\]

Both finite sums are strictly less than one for their relevant indices. Thus every optimum has connected coalitions, none a singleton. A proper connected induced subgraph of \(C_n\) is a consecutive path arc.

**2. Exact optimal *path* arc lengths.** For a path coalition of length \(k\), summing the reciprocal distances over all pairs gives

\[
F(k)=\frac2k\sum_{d=1}^{k-1}\frac{k-d}{d}=2(H_k-1).
\]

For \(k\ge5\), splitting an arc into lengths \(3\) and \(k-3\) strictly improves welfare, since

\[
F(k)-F(k-3)=2\left(\frac1{k-2}+\frac1{k-1}+\frac1k\right)
\le\frac{47}{30}<\frac53=F(3).
\]

Therefore every non-grand optimal cycle partition uses only arcs of lengths two, three or four. More generally, for a path with at least two vertices, every optimal path partition has exactly these lengths and no singleton, by the same argument as step 1 (on a path, an adjacent singleton can be merged at a path end).

Let \(a,b,c\) be the numbers of arcs of lengths \(2,3,4\). Their total length is \(n=2a+3b+4c\), and their welfare equals

\[
a+\frac53b+\frac{13}{6}c=\frac{5n}{9}-\frac{2a+c}{18}.
\]

Maximizing welfare is therefore exactly minimizing the nonnegative integer \(t=2a+c\) with \(t\equiv n\pmod3\). For \(n\ge2\), the minimum and all attaining pairs \((a,c)\) are: \(t=0,(0,0)\) when \(n\equiv0\); \(t=1,(0,1)\) when \(n\equiv1\); and \(t=2,(1,0)\) or, when \(n\ge8\), \((0,2)\) when \(n\equiv2\). All the remaining blocks are triples. In particular the exact optimal path welfare for \(n\ge2\) is

\[
W_n=\begin{cases}
5q/3&n=3q,\\
5q/3+1/2&n=3q+1,\\
5q/3+1&n=3q+2.
\end{cases}
\]

This path classification is also a previously established result of Okubo–Hanaka–Ono (2018), whose theorem and appendix cover precisely these block types. It is used here as a credited input and is included algebraically for a self-contained cycle proof.

**3. Reduction of every proper cycle partition to a path.** Any non-grand cycle partition into connected arcs has at least two blocks. Deleting a cycle edge between two distinct blocks turns \(C_n\) into \(P_n\) *without changing any induced distance inside any block*. Hence every such partition has welfare at most \(W_n\). Conversely, for \(n\ge5\), each optimal path block pattern has at least two blocks, and placing it around the cycle produces a proper cyclic partition with the same welfare. Thus for \(n\ge5\) the optimal proper-partition welfare is exactly \(W_n\); for \(n=3,4\) it is at most \(W_n\).

**4. The sharp grand-coalition transition.** In \(C_n\), each pair at cyclic distance \(d<n/2\) appears \(n\) times; if \(n\) is even, the \(n/2\) antipodal pairs contribute the additional term \(2/n\). This gives \(Q_n\) above. Directly,

\[
(Q_3,Q_4,Q_5,Q_6)=(2,5/2,3,10/3),
\qquad
(W_3,W_4,W_5,W_6)=(5/3,13/6,8/3,10/3).
\]

Moreover, for \(n\ge5\),

\[
Q_{n+1}-Q_n=\frac1{\lceil n/2\rceil}\le\frac13,
\]

whereas \(W_{n+1}-W_n\) is always either \(1/2\) or \(2/3\). Consequently \(W_6=Q_6\), with \(W_n>Q_n\) for every \(n\ge7\); at orders three through five the grand coalition beats even the path upper bound. This proves the welfare values and the grand-versus-proper classification.

**5. Counting every optimizer.** At \(n=6\), the proper maximizers are the three partitions into two triples; adding the grand coalition yields four. At \(n\ge7\), let \(q=\lfloor n/3\rfloor\). For \(n=3q\), equal-length triple blocks give \(n/q=3\) partitions. For \(n=3q+1\), the unique quadruple can start at any of the \(n\) vertices. For \(n=3q+2\), the unique pair similarly gives \(n\) partitions. The alternative block multiset contains two quadruples and \(q-2\) triples; choosing a cyclic boundary and arranging \(q\) blocks, then dividing by the \(q\) equivalent choices of starting block, gives

\[
\frac n q\binom q2=\frac{n(q-1)}2
\]

more partitions. Their sum is \(n(q+1)/2\). The strict inequalities in steps 1–4 exclude every other set partition. \(\square\)

## Verification

The accompanying `VERIFY_EXACT.py` computes all utilities from induced-subgraph shortest paths with exact rational arithmetic. It checks **every set partition**, including disconnected ones, for \(P_n\) at \(1\le n\le9\) and \(C_n\) at \(3\le n\le9\), comparing both maximum welfare and the number of maximizers. Separately, it checks optimal path welfare and counts against exact dynamic programming for \(1\le n\le100\), and performs exact cyclic-cut enumeration for \(3\le n\le16\). All checks pass. These are finite corroborations; the theorem for every \(n\) follows from the proof above, not from enumeration.

Run with `python3 VERIFY_EXACT.py`. Only Python standard-library modules are needed. No approximations or numerical tolerances are used.

## Relationship to prior work

Brânzei and Larson (2011) introduced this **normalized** induced-distance model and obtained welfare facts for complete and complete-bipartite graphs, covering \(C_3\) and \(C_4\) as known special cases. Okubo, Hanaka and Ono (2018), *Optimal Partition of a Tree with Social Distance*, Section 3, Theorem 3.1 and its appendix, **already characterize optimal path partitions** with blocks of lengths \(2,3,4\) and give a linear-time solution on all trees. Those path results are not claimed as new. Neither theorem covers a cycle's grand coalition, the exact order-six tie, or the enumeration of all labeled optimal cycle partitions.

Ganian and collaborators (2023) study a different **non-normalized score-based** model and explicitly cite the known normalized-tree result. Their treewidth and coalition-structure algorithms do not establish this canonical cycle theorem. The present contribution is the explicit optimum/optimizer classification on the first elementary connected family beyond trees, with a sharp transition from one cycle-spanning coalition to small cyclic blocks.

## Limitations

The theorem assumes a simple unweighted cycle and the original utility denominator \(|S|\). It does not cover weighted cycles, arbitrary unicyclic networks, negative distance scores, Nash-stable partitions, or optimizing an average across coalitions. It makes no claim about a general formula for all bounded-treewidth graphs. The priority comparison used the relevant accessible full texts and targeted mathematical searches, but an equivalent specialist result outside the inspected corpus cannot be ruled out. No external independent audit has been performed.

## References

1. Simina Brânzei and Kate Larson, *Social Distance Games*, IJCAI 2011, pp. 91–95, DOI: 10.5591/978-1-57735-516-8/IJCAI11-027. https://ijcai.org/proceedings/2011/27
2. Masahiro Okubo, Tesshu Hanaka and Hirotaka Ono, *Optimal Partition of a Tree with Social Distance*, arXiv:1809.03392, first posted 2018-09-10; see Section 3, Theorem 3.1 and Appendix Section 7. https://arxiv.org/abs/1809.03392
3. Robert Ganian, Thekla Hamm, Dušan Knop, Sanjukta Roy, Šimon Schierreich and Ondřej Suchý, *Maximizing Social Welfare in Score-Based Social Distance Games*, arXiv:2307.05061, first posted 2023-07-11; EPTCS 379 (2023), pp. 272–286. https://arxiv.org/abs/2307.05061
