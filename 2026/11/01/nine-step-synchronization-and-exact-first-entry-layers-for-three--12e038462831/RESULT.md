# Nine-step synchronization and exact first-entry layers for three-color fireflies on bridged cliques

## Finding

For integers \(a,b\geq2\), let \(B_{a,b}\) be the graph obtained from disjoint complete graphs \(K_a\) and \(K_b\) by joining one distinguished vertex of each with a single edge. Give every vertex one of the states \(0,1,2\). At each simultaneous update, \(0\mapsto1\) and \(1\mapsto2\), while \(2\mapsto0\) unless a neighbor is currently in state \(1\), in which case state \(2\) is held.

**Theorem.** For every initially labelled coloring of \(B_{a,b}\), the first time \(T\) at which all vertices share a color satisfies \(0\leq T\leq9\); the upper bound \(9\) is attained for every \(a,b\geq2\). Thereafter, every vertex follows the same primitive three-cycle. Thus there are no asynchronous recurrent states.

The complete exact distribution of \(T\) is as follows. Write
\[
\sigma_j(r)=\sum_{h=0}^j(-1)^{j-h}\binom jh h^r\qquad (1\leq j\leq3,\ r\geq1).
\]
For each \(0\leq t\leq9\), let \(C_t\) denote the following integer matrix, where rows and columns have indices \(1,2,3\):

| \(t\) | \(C_t\) |
|:--:|:--|
| 0 | \(\begin{pmatrix}3&0&0\\0&0&0\\0&0&0\end{pmatrix}\) |
| 1 | \(\begin{pmatrix}8&6&0\\6&4&0\\0&0&0\end{pmatrix}\) |
| 2 | \(\begin{pmatrix}10&17&10\\17&25&15\\10&15&9\end{pmatrix}\) |
| 3 | \(\begin{pmatrix}8&6&0\\6&4&0\\0&0&0\end{pmatrix}\) |
| 4 | \(\begin{pmatrix}4&1&0\\1&0&0\\0&0&0\end{pmatrix}\) |
| 5 | \(\begin{pmatrix}12&10&3\\10&8&2\\3&2&0\end{pmatrix}\) |
| 6 | \(\begin{pmatrix}8&8&4\\8&6&2\\4&2&0\end{pmatrix}\) |
| 7 | \(\begin{pmatrix}4&5&0\\5&4&0\\0&0&0\end{pmatrix}\) |
| 8 | \(\begin{pmatrix}12&14&7\\14&12&4\\7&4&0\end{pmatrix}\) |
| 9 | \(\begin{pmatrix}12&14&3\\14&18&4\\3&4&0\end{pmatrix}\) |

The number \(N_t(a,b)\) of labelled initial colorings that first synchronize at update \(t\) is exactly
\[
\boxed{N_t(a,b)=\sum_{i=1}^3\sum_{j=1}^3 C_t[i,j]\,\sigma_i(a-1)\,\sigma_j(b-1).}
\]
In particular, \(N_1(a,b)=N_3(a,b)\), and \(\sum_{t=0}^9N_t(a,b)=3^{a+b}\). If initial colors are independently uniform, \(\Pr(T=2)\to1\) whenever \(\min(a,b)\to\infty\). The probability of a two-step synchronization is bounded below by
\[
\prod_{r\in\{a-1,b-1\}}\left(1-3\left(\frac23\right)^r+3\left(\frac13\right)^r\right).
\]

## Assumptions and scope

Both clique sizes are integers at least two; clique vertices are distinguishable. Each clique has exactly one bridge endpoint, and there are no other interclique edges. All updates are deterministic and simultaneous. Synchronization means *global* equality of all \(a+b\) vertex colors at a single integer time; \(T\) is the least such time, including \(T=0\). The theorem is about this particular three-state inhibitory rule, not cyclic cellular automata or Greenberg–Hastings excitation.

## Proof

Call the two bridge endpoints \(u\) and \(v\), and their sets of nonbridge clique neighbors \(A'\) and \(B'\). At time zero, each nonempty initial color class in \(A'\), and likewise \(B'\), is a **cohort**. Each class remains monochromatic at every subsequent time. Indeed, all vertices in a class have the same state; when that state is \(2\), none of those vertices is itself blinking, so the possible presence of a state-\(1\) neighbor does not depend on which vertex of the class is inspected. Consequently all vertices of that class update identically. The assertion is also immediate for classes in states \(0\) and \(1\).

Represent each cohort by a 3-entry vector, ordered by its *initial* colors. Entry \(-1\) means the class was initially absent; otherwise an entry is its current color. Retain the two special colors at \(u,v\). For any such four-block representative \((u,v,P,Q)\), define the Boolean signals
\[
I_u=[v=1\ \text{or}\ 1\in P],\quad I_v=[u=1\ \text{or}\ 1\in Q],
\]
\[
I_P=[u=1\ \text{or}\ 1\in P],\quad I_Q=[v=1\ \text{or}\ 1\in Q].
\]
Here \([\cdots]\) is an indicator. The complete update is obtained by applying \(f(c,I)=c+1\pmod3\) for \(c=0,1\), \(f(2,1)=2\), and \(f(2,0)=0\), separately to each existing entry, with its corresponding signal; absent entries remain absent. This transition is **exact**, because bridge endpoints see each other and their own clique interiors, whereas an interior vertex sees its own bridge endpoint and all other interior vertices in its clique. For an interior vertex in state \(2\), exclusion of itself does not alter the state-\(1\) test. No multiplicities beyond whether each initial cohort exists are used.

There are precisely \(3^2(2^3-1)^2=441\) initial representatives: three choices at each endpoint and seven nonempty initial color-support masks for each interior. Their iterations give the matrices \(C_t\) in the Finding section. The complete executable enumeration is `verify_symbolic.py`. It enumerates each of those 441 initial representatives, uses the displayed exact update rule until all nonabsent entries coincide, asserts the maximum is nine, and independently tallies the first-hitting matrix by support sizes. The full ten-matrix tally is also explicitly supplied in the theorem, so each loop and sum is inspectable and independently reproducible. Therefore the finite enumeration proves the statement for **all** positive interior sizes, not only for the labelled sizes tested separately.

For sharpness choose initial colors \(u=v=0\), all vertices of \(A'\) colored \(0\), and all vertices of \(B'\) colored \(2\). For each time \(t=0,1,\dots,9\), the ordered colors \((u,v,A',B')\) are

| \(t\) | \((u,v,A',B')\) |
|:--:|:--|
| 0 | \((0,0,0,2)\) |
| 1 | \((1,1,1,0)\) |
| 2 | \((2,2,2,1)\) |
| 3 | \((0,2,0,2)\) |
| 4 | \((1,0,1,0)\) |
| 5 | \((2,1,2,1)\) |
| 6 | \((2,2,0,2)\) |
| 7 | \((0,0,1,0)\) |
| 8 | \((1,1,2,1)\) |
| 9 | \((2,2,2,2)\) |

Hence the first synchronization occurs at exactly nine, for any \(a,b\geq2\).

For a specified initial support of size \(j\) among \(r\) labelled interior vertices, the number of onto assignments is \(\sigma_j(r)\), by inclusion–exclusion. Each of the 441 representatives contributes the product \(\sigma_i(a-1)\sigma_j(b-1)\), where \(i,j\) are its two support sizes. Grouping by first synchronization time yields the displayed exact expression for \(N_t(a,b)\). The identity \(\sum_tN_t(a,b)=3^{a+b}\) follows since the 441 representatives partition all initial colorings; the separately executed arithmetic test checks the resulting formulas on a parameter rectangle.

If both interior groups initially contain all three colors, the 9 endpoint-color choices have time exactly two, as recorded by \(C_2[3,3]=9\) and \(C_t[3,3]=0\) for all other times. A length-\(r\) iid uniformly colored interior contains all three colors with probability \(1-3(2/3)^r+3(1/3)^r\); independence of the two interiors gives the lower bound and limit. Finally, a global constant configuration increments in unison through \(0,1,2\) indefinitely and is a primitive three-cycle.

## Verification

Run `python3 verify_symbolic.py` to reproduce all 441 exact cohort cases, the 10 coefficient matrices, sharpness, the sum identity and the full-support two-step property. Run `c++ -std=c++17 -O2 verify_labeled.cpp -o verify_labeled && ./verify_labeled` for a separately written, direct vertex-by-vertex test of all \(1{,}185{,}921\) labelled configurations across \(25\) clique-size pairs with \(2\leq a,b\leq6\). Text outputs are included as `symbolic_output.txt` and `labeled_output.txt`. The finite all-size proof rests on the exact cohort quotient plus complete 441-case enumeration, not on extrapolation of the labelled tests.

## Relationship to prior work

Lyu introduced this inhibitory oscillator update and established synchronization theorems on paths and low-degree trees [1]. His theorem implies synchronization on the member \(B_{2,2}=P_4\), but is not a theorem for the whole bridged-clique family; graphs with \(a\geq3\) or \(b\geq3\) contain cycles. The later tree analysis [2] likewise does not give the exact nine-step cutoff or two-parameter first-entry distribution on these cyclic graphs. The known global small-width criterion only applies to a subset of initial configurations, while the theorem above includes all three-color full-support states. Related exact censuses on complete bipartite and complete split graphs study different adjacency structures and do not imply these first-entry counts; the Greenberg–Hastings rule on a similar bridge graph is a different transition law. The reported contribution is the sharp deterministic synchronization cutoff and all-ten-layer census for bridged cliques, not the introduction of the firefly rule or general path/low-degree-tree synchronization.

## Limitations

The proof is computer-assisted by an exhaustive, fully specified **finite** quotient whose exactness is justified above. The two programs were separately implemented but have not been externally audited; testing many labelled instances is corroboration, not a proof for unbounded clique sizes. We do not claim the same bound for longer chains of cliques, different numbers of colors, stochastic updates, or multiple bridging edges. A prior equivalent analysis outside inspected literature remains possible; publication priority requires further human review. The model has no independent validation attached.

## References

[1] Hanbaek Lyu, *Synchronization of finite-state pulse-coupled oscillators*, arXiv:1407.1103, first posted 2014-07-04. https://arxiv.org/abs/1407.1103

[2] Hanbaek Lyu, *Time complexity of Synchronization of discrete pulse-coupled oscillators on trees*, arXiv:1610.00837, first posted 2016-10-04. https://arxiv.org/abs/1610.00837
