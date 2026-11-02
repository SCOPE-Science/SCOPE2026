# Exact double Roman domination of \(P(20,4)\) and \(P(25,5)\)

## Finding
For the generalized Petersen graphs with twenty and twenty-five outer vertices, respectively, the exact double Roman domination numbers are
\[
\gamma_{dR}(P(20,4))=34,\qquad \gamma_{dR}(P(25,5))=42.
\]
These are the first two cases in the family \(P(5k,k)\), ordered by \(k\), for which the 2022 bounds \(8k\le\gamma_{dR}\le8k+2\) did not determine the exact value. Both previously published upper bounds are attained, and their sharpness is established by the exhaustive finite-column argument below. The two values constitute one finding about the first unresolved boundary instances; no assertion is made for larger \(k\).

## Assumptions and scope
For an integer \(n\ge5\) and \(1\le k<n/2\), the simple undirected graph \(P(n,k)\) has vertices \(u_i,v_i\), with indices \(i\in\mathbb Z_n\). Its edges are \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+k}\), with all indices reduced modulo \(n\). A double Roman dominating function is a map \(f:V(P(n,k))\to\{0,1,2,3\}\). Every vertex labeled \(0\) must have a neighbor labeled \(3\) or at least two neighbors labeled \(2\); every vertex labeled \(1\) must have a neighbor labeled \(2\) or \(3\). The weight is \(\sum_x f(x)\), and its minimum is \(\gamma_{dR}\).

The conclusion is confined to \((n,k)=(20,4)\) and \((25,5)\). The argument works with labeled vertices and does not quotient by automorphisms. The attached standalone C++17 source is a finite exhaustive checker over a mathematically complete partition of the feasible assignments, not a heuristic optimizer.

## Proof
**Reduction to three labels.** An optimal function exists with no value \(1\). Indeed, given any labeled \(1\) vertex \(x\), if it has a neighbor labeled \(3\), change \(f(x)\) to \(0\), strictly decreasing weight. Otherwise it has a neighbor \(y\) labeled \(2\); change \(f(x):1\mapsto0\) and \(f(y):2\mapsto3\). The weight remains the same, \(x\) is protected by \(y\), and no other requirement is weakened because no previous label \(1\) counted toward protecting a zero vertex. Repeat for every remaining \(1\). Therefore minimizing over \(\{0,2,3\}\) is sufficient and exact.

**Column decomposition.** Fix \(k\in\{4,5\}\) and set \(n=5k\). For \(0\le j<k\), \(t\in\mathbb Z_5\), put
\[
U_{j,t}=f(u_{j+kt}),\qquad V_{j,t}=f(v_{j+kt}).
\]
The two inner neighbors of \(v_{j+kt}\) have values \(V_{j,t-1}\) and \(V_{j,t+1}\), while its third neighbor has value \(U_{j,t}\). Thus the legality of all inner zero vertices in column \(j\) depends only on the two five-vectors \(U_j,V_j\), not on any other column.

For a fixed complete assignment of the outer vectors \(U_0,\ldots,U_{k-1}\), define \(d_{j,t}\in\{0,2,3\}\) as the least value required of the spoke neighbor \(V_{j,t}\) to protect \(u_{j+kt}\): set it to \(0\) if \(U_{j,t}\ne0\), or if the two outer neighbors already contain a \(3\) or two \(2\)'s; set it to \(2\) if they contain exactly one \(2\) and no \(3\); otherwise set it to \(3\). Here the outer neighbors are \(U_{j-1,t}\), \(U_{j+1,t}\) for interior columns, and the cyclic boundary is twisted: the previous neighbor of \(U_{0,t}\) is \(U_{k-1,t-1}\), and the next neighbor of \(U_{k-1,t}\) is \(U_{0,t+1}\). Every zero outer vertex is protected exactly when \(V_{j,t}\ge d_{j,t}\).

For five-vectors \(U,D\in\{0,2,3\}^5\), define the finite, exact table
\[
B(U,D)=\min\left\{\sum_{t=0}^4V_t:\begin{array}{l}
V\in\{0,2,3\}^5,\quad V_t\ge D_t\text{ for all }t,\\
V_t=0\implies\bigl(3\in\{V_{t-1},V_{t+1},U_t\}\text{ or }\\
\#\{s\in\{t-1,t+1,*\}:\text{corresponding neighbor}=2\}\ge2\bigr)
\end{array}\right\},
\]
with \(B=+\infty\) when no such \(V\) exists, and with \(*\) denoting the spoke neighbor \(U_t\). This definition is merely a notational abbreviation for the 243 explicitly checked inner-vector possibilities; the checker implements the three-neighbor predicate directly.

The minimum weight among all legal functions with fixed outer vectors is **exactly**
\[
W(U_0,\ldots,U_{k-1})=\sum_{j=0}^{k-1}\left(\sum_t U_{j,t}+B(U_j,d_j)\right).
\]
There is no missing intercolumn condition on the inner vectors because all inner edges and the spoke for a given inner vertex lie within the column. Define \(L(U)=\sum_tU_t+B(U,0)\). Since adding outer demands only reduces inner-vector choices, \(W\ge\sum_jL(U_j)\). Hence if a solution has weight at most \(C\), its outer-vector tuple must satisfy \(\sum_jL(U_j)\le C\).

**Finite exhaustive step.** The attached C++17 checker creates all \(3^5=243\) outer vectors, computes \(B(U,D)\) for all \(243^2\) ordered pairs \((U,D)\) by checking the 243 inner vectors, and exhaustively lists exactly those outer-vector tuples with \(\sum_jL(U_j)\le C\). For each retained tuple it computes the exact \(W\), including the cyclic twist, and tests whether \(W\le C\). No outer-vector tuple that could contribute a feasible function of weight at most \(C\) is pruned. The loop bounds, checks, and integer arithmetic are fully visible in `petersen_exact.cpp`.

For \((k,C)=(4,33)\), precisely **1,912,264** complete outer-vector tuples survive this necessary-cost pruning; none has \(W\le33\). For \((k,C)=(5,41)\), precisely **77,570,086** survive; again none has \(W\le41\). As every optimal function may be taken without label \(1\), the resulting rigorous finite lower bounds are
\[
\gamma_{dR}(P(20,4))\ge34,\qquad\gamma_{dR}(P(25,5))\ge42.
\]
The enumerated domain is exhaustive by the displayed partition and nonnegative lower-bound pruning; these are not extrapolations from a sample of assignments.

**Attaining the bounds.** All vertex values not mentioned next are \(0\), and indices are zero-based. For \(P(20,4)\), assign \(3\) at outer indices \(\{2,5,9,12,15,19\}\) and at inner indices \(\{4,7,10,17\}\), and \(2\) at inner indices \(\{16,18\}\). The weight is \(34\). For \(P(25,5)\), assign \(2\) at outer indices \(\{1,5,7,9,14,16,18,22,24\}\), assign \(2\) at inner indices \(\{2,4,10,13,19,21\}\), and assign \(3\) at inner indices \(\{3,11,12,20\}\). The weight is \(42\). The checker additionally tests every vertex's original protection predicate on both witnesses without relying on the column table. Together with the lower bounds, these yield the claimed equalities.

## Verification
Compile and execute the complete source artifact:

```sh
c++ -O3 -std=c++17 -Wall -Wextra -pedantic petersen_exact.cpp -o petersen_exact
./petersen_exact 4 33
./petersen_exact 5 41
```

The replay performed for this package returned, respectively, complete outer-tuple counts **1,912,264** and **77,570,086**, zero solutions below the proposed optima, certified integer lower bounds **34** and **42**, and independently checked witnesses of precisely those weights. Each invocation terminated successfully. A second numerical cross-check used an independently formulated binary integer program from the original zero-protection constraint and obtained the same optima, but this solver result is only corroborating evidence; it is not the proof of the exhaustive lower bound.

## Relationship to prior work
Rupnik Poklukar and Žerovnik (2022), Theorem 6, established \(8k\le\gamma_{dR}(P(5k,k))\le8k+2\) when \(k\equiv0,1,4\pmod5\) and achieved equality \(8k\) for \(k\equiv2,3\pmod5\). Their Tables 6 and 8 already exhibit weight-\(42\) and weight-\(34\) configurations at the two graphs of this finding. Their concluding open question specifically asks to close the residual lower/upper gaps. The **new content here is solely the sharp lower-bound evidence via an exact local finite decomposition** for the first two unresolved parameters, not the known constructions or general bounds. The 2023 survey provides broader background; neither these inspected materials nor the recorded mathematical-search results establish these two exact equalities.

## Limitations
This is a two-instance, reproducible finite result and proves no new universal formula for the residue classes. Its significance lies in closing two natural first unresolved cases explicitly singled out by published bounds. The certificate relies on implementing the displayed complete finite enumeration correctly; the source and all expected counts are supplied for independent replay, while an independent mathematical audit has not yet been performed. Equivalent earlier unindexed computations or descriptions of these exact cases cannot be excluded by negative search results.

## References
1. D. Rupnik Poklukar and J. Žerovnik, *On the Double Roman Domination in Generalized Petersen Graphs \(P(5k,k)\)*, Mathematics **10** (2022), 119, doi:10.3390/math10010119; publicly published 2022-01-01.
2. R. A. Beeler, T. W. Haynes, and S. T. Hedetniemi, *Double Roman domination*, Discrete Applied Mathematics **211** (2016), 23–29, doi:10.1016/j.dam.2016.03.017.
3. D. Rupnik Poklukar and J. Žerovnik, *Double Roman Domination: A Survey*, Mathematics **11** (2023), 351, doi:10.3390/math11020351.
