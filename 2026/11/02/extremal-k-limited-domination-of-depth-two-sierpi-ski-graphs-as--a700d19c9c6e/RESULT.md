# Extremal \(k\)-limited domination of depth-two Sierpiński graphs as symmetric regular binary matrices

## Finding

**Theorem.** For every integer \(m\ge2\) and \(1\le k\le m-1\), put \(r=m-k\). On the depth-two Sierpiński graph \(S(2,m)\),
\[
\gamma_k^{\mathrm L}(S(2,m))=mr.
\]
Label the vertices \((i,j)\), where \(i,j\in\{1,\dots,m\}\), and write \(a_{ij}=1\) if and only if \((i,j)\) belongs to a chosen set. Then **all** minimum \(k\)-limited dominating sets, without exception, are the binary symmetric matrices \(A=(a_{ij})\) having every row sum equal to \(r\). Their exact number is
\[
N_{m,k}=[x_1^r\cdots x_m^r]\prod_{i=1}^{m}(1+x_i)\prod_{1\le i<j\le m}(1+x_ix_j).
\]
In particular, \(N_{m,k}=N_{m,m-k}\). At either boundary \(k=1\) or \(k=m-1\),
\[
N_{m,1}=N_{m,m-1}=\sum_{j=0}^{\lfloor m/2\rfloor}\frac{m!}{2^j j!(m-2j)!},
\]
the number of involutions on \(m\) labelled symbols.

For \(r=2\), equivalently \(k=m-2\) with \(m\ge3\), the selected symmetric matrices are precisely unions of labelled paths of at least two vertices, with a selected diagonal at each endpoint, and ordinary cycles of length at least three, without diagonals. Consequently, with the conventions \(N_{0,\bullet}=1\) and \(N_{1,\bullet}=0\) for this degree-two counting problem,
\[
\sum_{m\ge0} N_{m,m-2}\frac{z^m}{m!}
=\exp\!\left(\sum_{\ell\ge2}\frac{z^\ell}{2}+\sum_{\ell\ge3}\frac{z^\ell}{2\ell}\right).
\]
Here the index \(m-2\) on the left is merely a notation for the row-sum-two enumeration at small formal values \(m=0,1\), where it does not denote an admissible domination parameter.

## Assumptions and scope

The graphs are finite, simple and undirected. The vertex set of \(S(2,m)\) is \(\{(i,j):1\le i,j\le m\}\). Distinct \((i,j)\), \((p,q)\) are adjacent when either \(i=p\) (the \(i\)-th row is a complete graph), or \(i\ne j\) and \((p,q)=(j,i)\) (the transposition linking edge). Thus each diagonal vertex \((i,i)\) has no linking edge. A \(k\)-limited dominating set is a dominating set \(D\) for which each \(v\in D\) has at most \(k\) neighbours outside \(D\). All counts refer to subsets of the labelled vertex set, not symmetry orbits. Only \(m\ge2\) and \(1\le k\le m-1\) are claimed for domination.

## Proof

**Lower bound.** Write \(R_i=\{(i,j):1\le j\le m\}\) and \(t_i=|D\cap R_i|\). Because \((i,i)\) has neighbours only within its row, a row with \(t_i=0\) would leave \((i,i)\) undominated. Thus \(t_i\ge1\). Pick any \(v\in D\cap R_i\). The \(m-t_i\) unchosen vertices of that row are all adjacent to \(v\), independently of its linking edge. The capacity condition implies \(m-t_i\le k\), or \(t_i\ge r\). Summing over all rows yields \(|D|\ge mr\).

**Sharpness.** There exists a symmetric binary matrix with row sum \(r\) for every \(1\le r\le m-1\). Explicitly index rows modulo \(m\): if \(r=2s\), choose matrix entries \((i,i\pm h)\) for \(1\le h\le s\); if \(r=2s+1\), additionally choose all diagonal entries and entries \((i,i\pm h)\) for \(1\le h\le s\). As \(r\le m-1\), the indicated residues are distinct. The rows have exactly \(r\) selected entries, and the selected set dominates within every row because \(r\ge1\). Each selected vertex has exactly \(m-r=k\) unselected neighbours in its row. Any linking neighbour is selected as well, by symmetry. Hence this set is \(k\)-limited, proving the stated optimum.

**Equality classification.** If \(|D|=mr\), the established rowwise inequalities force \(t_i=r\) for each row. Every chosen \((i,j)\) then has exactly \(k\) unchosen row neighbours. If \(i\ne j\) and \((j,i)\notin D\), its additional linking neighbour would give \(k+1\), a contradiction. Thus every off-diagonal entry occurs together with its transpose, i.e., \(A=A^{\mathsf T}\). Conversely, any symmetric binary matrix with constant row sum \(r\) defines a valid minimum set by the sharpness argument. This is a bijection, including diagonal choices.

**Enumerator and duality.** For each index \(i\), a diagonal choice adds one to row \(i\), yielding \(1+x_i\). For each unordered pair \(\{i,j\}\), choosing its symmetric off-diagonal entries adds one to each of rows \(i,j\), yielding \(1+x_ix_j\). Extracting coefficient \([x_1^r\cdots x_m^r]\) counts every permitted matrix exactly once. The binary complement of a symmetric row-sum-\(r\) matrix is a symmetric row-sum-\((m-r)\) matrix, giving \(N_{m,k}=N_{m,m-k}\).

**Explicit endpoints.** For row sum one, the unique 1 in each row either lies on its diagonal (a fixed point) or forces a mutual pair of off-diagonal ones (a transposition). Hence matrices are in bijection with involutions on \(m\) labels. Choose \(j\) disjoint transpositions, obtaining \(m!/(2^j j!(m-2j)!)\); sum and apply complement duality to the opposite capacity endpoint.

**The row-sum-two refinement.** Regard each off-diagonal symmetric pair as an ordinary edge, and each selected diagonal as a loop contributing **one** unit to its vertex's required row sum. Because the row sum is two, a component without a selected loop is a simple cycle of length at least three. Any component with a loop is a simple path on at least two vertices, with loops exactly at its two endpoints. There is no one-vertex component because only one diagonal entry is available. There are \(\ell!/2\) undirected labelled paths of order \(\ell\ge2\) and \((\ell-1)!/2\) undirected labelled cycles of order \(\ell\ge3\). The labelled-set construction yields the displayed exponential generating function. This completes the proof.

## Verification

The accompanying standalone source `verify_sierpinski2_limited.py` constructs all actual graph neighbourhoods. It exhaustively compares all optimum-cardinality subsets with the symmetric-matrix classification for every admissible \(k\) at \(m=2,3,4\). It separately enumerates symmetric matrices and checks the domination rule, complement counts, involution formula and degree-two component recurrence for \(2\le m\le6\). The successful run printed:

`VERIFY_OK exhaustive_graph_cases=6 matrix_sizes=2..6 exact_counts=[(2, {1: 2}), (3, {1: 4, 2: 4}), (4, {1: 10, 2: 18, 3: 10}), (5, {1: 26, 2: 112, 3: 112, 4: 26}), (6, {1: 76, 2: 820, 3: 1760, 4: 820, 5: 76})]`

These finite computations are corroboration only. The proof for all parameters consists of the rowwise lower bound, explicit symmetric construction, linking-edge equality argument, and exact combinatorial enumeration.

## Relationship to prior work

Božović's October 2026 study [1], particularly Section 5 and Conjecture 12, gives the minimum \(1\)-limited number for every Sierpiński graph, the two capacities of the planar alphabet-three family, and proposes the general value \((m-k)m^{n-1}\). Our cardinality equality is **already known when \(k=1\)**, and for the alphabet-three specializations; it proves the conjectured cardinality for the depth-two family and all remaining capacities, but not for greater depths. The complete equality classification and its exact optimum-set enumeration are not stated in the inspected primary source. The foundational definition and its relation to other domination parameters appear in [2]. Earlier ordinary domination of Sierpiński graphs [3] concerns a different constraint. The equivalent \((0,k)\)-pitchfork terminology is discussed in [2]; this should be considered in future historical-priority checks. No independent comprehensive priority audit has been conducted.

## Limitations

This does not resolve the conjecture for \(S(n,m)\) at depths \(n\ge3\), does not enumerate nonminimum sets, and counts matrices on labelled symbols rather than up to automorphisms. The coefficient formula is an exact finite expression, not an elementary closed form for every intermediate row sum. Historical priority remains qualified by incomplete exhaustive coverage of equivalent domination nomenclature, though the closest primary full texts and targeted searches were inspected. No external independent validation has been performed.

## References

[1] D. Božović, *On \(k\)-limited domination: complexity and Sierpiński graphs*, arXiv:2610.01584v1 (first posted 2026-10-01), Section 5 and Conjecture 12. https://arxiv.org/html/2610.01584v1

[2] D. Božović, G. Radić, Ž. Kovijanić-Vukićević, A. Tepeh, *On \(k\)-limited domination in graphs*, arXiv:2606.22422; open-access journal text, https://link.springer.com/article/10.1007/s40314-026-03902-2

[3] C.-A. Liu, *Domination in the Sierpiński graphs*, arXiv:2008.09807 (2020); journal version on Roman and double Roman domination, 2021. https://arxiv.org/abs/2008.09807
