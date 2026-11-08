# A central-layer obstruction to cyclic subgroup-factorization chains

## Finding

Let \(G\) be a cyclic group of squarefree order \(p_1\cdots p_r\), where the \(p_i\) are pairwise distinct primes and \(r\ge5\). A *factorization cycle* is a cyclically ordered list of at least three **distinct**, nonidentity, proper subgroups \(H_1,\ldots,H_m\) such that \(H_iH_{i+1}=G\) for every index, including the last-to-first pair. Several factorization cycles are *disjoint* if they have no subgroup in common. Put
\[
 c_r=\binom{r}{\lfloor r/2\rfloor},\qquad
 U_r=2^r-2-\left\lceil\frac{c_r}{2}\right\rceil.
\]
**Theorem.** Every union of mutually disjoint factorization cycles uses at most \(U_r\) distinct subgroups. Equivalently, every 2-regular subgraph (not necessarily connected or induced) of the factorization graph \(\Gamma(G)\) has at most \(U_r\) vertices; in particular,
\[
 \operatorname{circ}(\Gamma(G))\le U_r.
\]
There are exactly \(2^r-r-2\) nonpendant vertices; hence at least \(\lceil c_r/2\rceil-r\) of them must be missed by **every** vertex-disjoint collection of cycles. This forced deficit is positive for \(r\ge6\) and grows as \(2^{r-1}\sqrt{2/(\pi r)}\) when \(r\to\infty\). The theorem does not claim equality in the circumference bound for all \(r\).

The bound evaluates to \(25,52,108,219,447,896\) at \(r=5,6,7,8,9,10\), respectively. Explicit vertex-disjoint cycle certificates attain the 2-regular coverage bound for \(r=5,6,7\). Thus it is an exact 2-regular coverage invariant for these three ranks; the cited 2026 paper independently establishes the corresponding **single-cycle** circumference equalities.

## Assumptions and scope

All groups here are finite cyclic groups of squarefree order with at least five distinct prime factors; the numerical prime values are immaterial. The factorization graph has one vertex per nonidentity proper subgroup, with distinct vertices adjacent precisely when their subgroup product is \(G\). A 2-regular subgraph is a disjoint union of simple cycles, each of length at least three, and is not required to span all vertices. The coverage bound is for the union of all cycles, not for their number or sum of lengths with repetitions.

For a subgroup \(H\), let \(J(H)\subset [r]\) be the indices of prime factors dividing \(|H|\), and define the complementary support \(S(H)=[r]\setminus J(H)\). Uniqueness of subgroups of each order in a cyclic group identifies vertices with nonempty proper subsets \(S\subset[r]\). The condition \(HK=G\) is equivalent to \(S(H)\cap S(K)=\varnothing\), since the subgroup product has the least-common-multiple order. The sets of cardinality \(r-1\) are the \(r\) pendant vertices, each adjacent only to its complementary singleton; these cannot belong to a cycle. We work from now on in the remaining vertex set \(V=\{S:1\le |S|\le r-2\}\).

## Proof

Fix an arbitrary 2-regular subgraph \(F\) of the disjointness graph on \(V\). Partition \(V=A\sqcup B\) as specified below. Let \(a\) and \(b\) be the numbers of vertices of \(F\) lying in \(A\) and \(B\), and let \(e_A,e_B,e_\times\) count its edges inside \(A\), inside \(B\), and crossing between the classes. Because every used vertex has degree exactly two,
\[
 2a=2e_A+e_\times,\qquad
 2b=2e_B+e_\times.
\]
Therefore \(a-b=e_A-e_B\) and
\[
 |V(F)|=a+b=2b+e_A-e_B\le2|B|+e_A.\tag{1}
\]
This balance identity holds equally for disconnected collections of cycles.

**Even rank.** Write \(r=2k\), \(k\ge3\), and take \(B=\{S\in V:|S|<k\}\), \(A=V\setminus B\). The middle level \(M=\{S:|S|=k\}\) has size \(c_r=\binom{2k}{k}\), while symmetry of binomial coefficients gives \(|B|=2^{r-1}-1-c_r/2\). If disjoint sets \(S,T\) both lie in \(A\), then \(|S|,|T|\ge k\) and \(|S|+|T|\le2k\), forcing \(|S|=|T|=k\) and \(T=[r]\setminus S\). Thus edges internal to \(A\) form a matching of \(c_r/2\) complementary pairs, so \(e_A\le c_r/2\). Substitution into (1) gives
\[
 |V(F)|\le 2(2^{r-1}-1-c_r/2)+c_r/2
 =2^r-2-c_r/2=U_r.
\]

**Odd rank.** Write \(r=2k+1\), \(k\ge2\), and take \(B=\{S\in V:|S|<k\}\), \(A=V\setminus B\). The level \(M=\{S:|S|=k\}\) has size \(c_r=\binom{2k+1}{k}\); binomial symmetry yields \(|B|=2^{r-1}-1-c_r\). For an internal edge in \(A\), the endpoint sizes must be \((k,k)\) or \((k,k+1)\). In the second case, the larger set is uniquely the complement of the smaller. Write \(x\) for the number of \((k,k+1)\)-edges of \(F\) and \(y\) for its number of \((k,k)\)-edges. Each edge counted by \(x\) contributes one incidence to a vertex of \(M\), and each edge counted by \(y\) contributes two. Hence \(x\le c_r\), \(x+2y\le2c_r\), and
\[
 e_A=x+y\le c_r+\lfloor c_r/2\rfloor
 =\lfloor3c_r/2\rfloor.
\]
Equation (1) now gives
\[
 |V(F)|\le2(2^{r-1}-1-c_r)+\lfloor3c_r/2\rfloor
 =2^r-2-\lceil c_r/2\rceil=U_r.
\]
Both cases prove the asserted uniform upper bound. The number of nonpendant vertices is \(|V|=2^r-r-2\), so the number missed is at least \(|V|-U_r=\lceil c_r/2\rceil-r\). By the standard central-binomial asymptotic \(c_r\sim2^r\sqrt{2/(\pi r)}\), the claimed growth follows.

For \(r=5,6,7\), the accompanying certificate contains respectively one, two, and three disjoint cycles whose combined lengths are \(25,52,108\), proving sharpness **for 2-regular coverage** in those cases. A separate explicit 25-cycle is included for the first case. These finite witnesses do not establish sharpness for \(r\ge8\).

## Verification

Run `python3 verify.py` with the Python standard library from this file's package directory. It reconstructs the Boolean-support graph directly, checks every edge of each supplied disjoint-cycle witness, confirms vertex uniqueness and coverage \(U_r\) for ranks 5, 6, and 7, and separately checks the single 25-cycle. It recomputes the binomial level partitions and verifies that **all** internal edges of \(A\) have the two structural forms used above for ranks 5 through 10. The recorded output is in `verification_output.txt`. Earlier independent mixed-integer optimization using degree-two constraints attained the same maximum cycle-cover sizes for ranks 5, 6, and 7, but this numerical optimization is supplementary: the universal upper bound is proved symbolically and the lower witnesses can be checked without an optimization solver.

## Relationship to prior work

Gutiérrez, Zuleta and García-Claro (arXiv:2610.40860v1, first publicly posted 2026-10-29) defined the relevant squarefree-cyclic factorization-graph model, established its pendant/core structure and non-Hamiltonicity properties, and computed circumferences \(25,52,108\) for \(r=5,6,7\) (as well as the smaller ranks). Those exact examples are **prior**, not new claims here. The present result supplies an explicit **all-r** upper bound on the number of vertices in any disjoint union of subgroup-factorization cycles, hence on a longest cycle, by a uniform central-layer incidence argument. It neither reproduces a claimed general exact circumference formula nor asserts that the bound is always attained.

Farrokhi Derakhshandeh Ghouchan and Azimi (arXiv:1911.12594v1) introduced factorization graphs of finite groups and studied their global group-theoretic properties and forbidden subgraphs. General Kneser-graph Hamiltonicity results concern fixed-size levels, rather than cycle coverage of the full mixed-level Boolean-support graph. The derivation above uses the actual subgroup-product relation and does not assume a Hamiltonicity theorem for the mixed-level graph.

## Limitations

The upper bound need not be exact at ranks \(r\ge8\); the exact circumference, even when 2-regular coverage reaches the bound, is not determined here. The result applies only to cyclic groups with squarefree order, not to groups with repeated prime-power factors or noncyclic groups. Prior theoretical results on generalized disjointness graphs may imply similar estimates under other terminology; no claim of exhaustive historical priority or independent audit is made. The verification is finite for its witnesses; the all-r statement depends on the combinatorial proof above.

## References

1. I. Gutiérrez, Y. Zuleta and E. J. García-Claro, *On the factorization graph of finite groups*, arXiv:2610.40860v1 (2026-10-29), https://arxiv.org/abs/2610.40860.
2. M. Farrokhi Derakhshandeh Ghouchan and A. Azimi, *Factorization graphs of finite groups*, arXiv:1911.12594v1 (2019-11-28), https://arxiv.org/abs/1911.12594.
3. A. Merino, T. Mütze and Namrata, *Kneser graphs are Hamiltonian*, arXiv:2212.03918 (2022), https://arxiv.org/abs/2212.03918. Used only to distinguish fixed-level graphs from the mixed-level problem; the present proof does not depend on it.
