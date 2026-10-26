# Uniform order 24 and exact cycle census for rowmotion on complete-bipartite incidence posets

## Finding

Let \(n\ge2\), let \(P_n\) be the vertex–edge incidence poset of the complete bipartite graph \(K_{2,n}\), and let \(\rho\) denote classical rowmotion on its lower order ideals. If \(c_d(n)\) denotes the number of distinct \(\rho\)-orbits of exact length \(d\), then

\[
\begin{aligned}
c_2(n)&=2^{n-1}, &c_3(n)&=3^{n-1}-2^n+2,\\
c_4(n)&=2^n-2, &c_6(n)&=\frac{5^n-7\cdot3^n+11\cdot2^n-6}{6},\\
c_8(n)&=3\cdot2^{n-1}-2, &c_{24}(n)&=3^{n-1}-2^n+1.
\end{aligned}
\]

Every other orbit length is absent. The order of the rowmotion permutation is exactly \(24\) for **every** \(n\ge2\). Orbits of length \(24\) occur if and only if \(n\ge3\). In particular, \(c_3(n)=c_{24}(n)+1\). The total number of ideals is \(2^n+2\cdot3^n+5^n\).

This is an all-parameter result, not an extrapolation from small numerical examples.

## Assumptions and scope

There are two distinguished vertices \(u_0,u_1\) and \(n\) labeled other vertices \(v_1,\ldots,v_n\). The elements of \(P_n\) are all these vertices and the \(2n\) edges \(e_{ij}=\{u_i,v_j\}\). The only strict comparabilities are \(u_i<e_{ij}\) and \(v_j<e_{ij}\). An ideal \(I\) contains every predecessor of each element it contains. Rowmotion is \(\rho(I)=\downarrow\min(P_n\setminus I)\). Both hubs and all leaves and edges are distinguished in the labeled count; cycles are orbits of ideals, not orbits modulo graph automorphisms.

## Proof

**1. Five column types and the exact update.** Write \(h\in\{0,1,2,3\}\) for the two-bit mask of hubs in an ideal. At each leaf, record the three bits \((a,b_0,b_1)\), denoting its presence and the presence of its two incident edges. The allowed types, represented by digits, are

\[
0=(0,0,0),\quad1=(1,0,0),\quad2=(1,1,0),\quad3=(1,0,1),\quad4=(1,1,1).
\]

If \(A_h\) is the allowable column alphabet given hub mask \(h\), then \(A_0=\{0,1\}\), \(A_1=\{0,1,2\}\), \(A_2=\{0,1,3\}\), and \(A_3=\{0,1,2,3,4\}\). Conversely, every hub mask and word in the corresponding alphabet defines exactly one ideal. Thus there are \(2^n+2\cdot3^n+5^n\) ideals.

For each selected ideal edge, its endpoints are already selected. Hence the minimal complement consists exactly of the unselected vertices and the unselected edges **whose endpoints are both selected**. Generating the next ideal adds the endpoints of those minimal complement edges. This gives the local type update \(f_h\), fully displayed below (a dash indicates an impossible input):

| \(h\) | \(f_h(0)\) | \(f_h(1)\) | \(f_h(2)\) | \(f_h(3)\) | \(f_h(4)\) |
|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 0 | – | – | – |
| 1 | 1 | 2 | 0 | – | – |
| 2 | 1 | 3 | – | 0 | – |
| 3 | 1 | 4 | 3 | 2 | 0 |

A new hub is present if it was previously absent, or if at least one resulting column has its corresponding edge present. More precisely, if \(T\subseteq A_h\) is the **nonempty support** of the word, define \(T'=f_h(T)\) and let

\[
h'_i=(1-h_i)\lor\bigvee_{x\in T'} b_i(x),\qquad i\in\{0,1\},
\]

where \(b_i(x)\) is the associated edge bit of column type \(x\). The support successor is \((h,T)\mapsto(h',T')\). It acts on the \(48\) possible pairs consisting of a hub mask and a nonempty subset of its valid alphabet, because \((2^2-1)+2(2^3-1)+(2^5-1)=48\).

**2. The finite support classification.** The following table completely lists the support cycles. Its columns are support size \(k\), support-cycle length \(p\), order \(q\) of the permutation induced on the \(k\) symbols after one full support cycle, and exact ideal orbit length \(p q\). Representatives use the hub mask and the support digits from step 1.

| \(k\) | \(p\) | \(q\) | \(pq\) | Representative \((h,T)\) |
|---:|---:|---:|---:|---|
| 1 | 2 | 1 | 2 | \((0,\{1\})\) |
| 1 | 3 | 1 | 3 | \((0,\{0\})\) |
| 1 | 8 | 1 | 8 | \((1,\{0\})\) |
| 2 | 1 | 2 | 2 | \((3,\{2,3\})\) |
| 2 | 4 | 1 | 4 | \((1,\{1,2\})\) |
| 2 | 4 | 2 | 8 | \((0,\{0,1\})\) |
| 2 | 8 | 1 | 8 | \((1,\{0,1\})\) |
| 3 | 1 | 3 | 3 | \((3,\{0,1,4\})\) |
| 3 | 3 | 2 | 6 | \((3,\{0,2,3\})\) |
| 3 | 8 | 3 | 24 | \((1,\{0,1,2\})\) |
| 4 | 2 | 3 | 6 | \((3,\{0,1,2,4\})\) |
| 4 | 3 | 2 | 6 | \((3,\{0,1,2,3\})\) |
| 5 | 1 | 6 | 6 | \((3,\{0,1,2,3,4\})\) |

Directly applying the displayed five-symbol transition and hub rule gives these \(13\) cycles and accounts for all \(48\) support states (the values of \(p\) sum to \(48\)). The finite check is fully reproducible by `verify_rowmotion.py`, which derives the transitions from ideal membership bits rather than inserting the displayed table as a lookup.

**3. Lift from support cycles to all ideals.** Define the onto-word count

\[
B_k(n)=\sum_{j=0}^k(-1)^{k-j}\binom{k}{j}j^n=k!\,\left\{\begin{matrix}n\\ k\end{matrix}\right\}.
\]

For a support orbit of length \(p\) and size \(k\), there are exactly \(pB_k(n)\) ideals projecting into that support orbit: at any support state the labeled word must use every symbol of its support. After \(p\) applications of rowmotion, its columns are acted on by the permutation \(\sigma\) listed in the table, of order \(q\). Since every symbol occurs, a nonidentity power of \(\sigma\) changes at least one labeled column. Hence every such ideal has orbit length **exactly** \(p q\), and this support orbit contributes exactly \(B_k(n)/q\) rowmotion orbits. This argument applies for every \(n\) and does not rely on extrapolating an experimental sequence.

Summing the \(13\) rows gives

\[
\begin{aligned}
c_2&=1+B_2/2,&c_3&=1+B_3/3,\\
c_4&=B_2,&c_6&=B_3/2+5B_4/6+B_5/6,\\
c_8&=1+3B_2/2,&c_{24}&=B_3/3.
\end{aligned}
\]

Expanding the inclusion–exclusion expressions yields precisely the formulas in the Finding. Because the support cycles include lengths \(3\) and \(8\) already with one symbol, the permutation order is at least their least common multiple, \(24\). Every listed orbit length divides \(24\), proving equality. Finally \(B_3(n)>0\) precisely when \(n\ge3\), which proves the primitive-\(24\)-cycle assertion.

## Verification

Execute `python3 verify_rowmotion.py` with a standard Python interpreter. The included checker independently constructs all \(48\) support states using the bit definition, verifies that the support successor permutes them, derives the \(13\) cycles and their induced type permutations, recomputes the cycle formulas from surjections, and validates all cardinality identities for \(2\le n\le19\). It additionally generates every ideal for \(2\le n\le6\), checks the minimal-complement transition against a separate top-to-bottom toggle implementation, and compares their complete orbit histograms. The successful output is `VERIFY_OK: 48 support states; 13 support orbits; order 24; formulas through n=19; independently enumerated n=2..6`.

The exhaustive all-parameter proof is the reduction to \(48\) support states, **not** the checks at bounded values of \(n\).

## Relationship to prior work

Striker and Williams (2011 preprint, 2012 publication) provide the classical rowmotion definition, toggle-group framework, and periodicity for important root and product posets, but not this graph-incidence family or its cycle census. Grinberg and Roby (first posted 2014) study birational rowmotion, with a section on classical rowmotion for skeletal posets; its stated family results do not give this incidence-poset classification. Striker's generalized toggle-group paper (first posted 2016) supplies the broad algebraic setting but not these cycle counts. Plante and Roby (first posted 2024) treat products \(C_m\times[k]\) of a claw poset and a chain, rather than vertex–edge incidence posets of \(K_{2,n}\); in particular their objects have a different rank structure and their periodicity results do not imply the present formulas.

The star incidence-poset case is a different graph family and is not claimed here. In particular, this result is restricted to \(n\ge2\) and does not claim novelty for rowmotion order \(24\) in isolation: its central contribution is the all-parameter **complete orbit census** with its support/surjection proof.

## Limitations

The result concerns ordinary finite order ideals, not birational or piecewise-linear rowmotion, unlabeled or symmetry-quotiented dynamics, or larger complete bipartite graphs \(K_{m,n}\) with \(m\ge3\). The finite support enumeration can be independently replayed, but it has not been subjected to an independent external audit. Published-record and literature checks cannot exclude all earlier unpublished or unindexed enumerations.

## References

1. J. Striker and N. Williams, *Promotion and Rowmotion*, arXiv:1108.1172, originally submitted 2011-08-04; European Journal of Combinatorics 33 (2012).
2. D. Grinberg and T. Roby, *Iterative properties of birational rowmotion*, arXiv:1402.6178, originally submitted 2014-02-25 (later revised).
3. J. Striker, *Rowmotion and generalized toggle groups*, arXiv:1601.03710, originally submitted 2016-01-14; DMTCS 20 (2018).
4. M. Plante and T. Roby, *Rowmotion on the chain of V's poset and whirling dynamics*, arXiv:2405.07984, originally submitted 2024-05-13.
