# A cyclic Gray code at six couples and a parity obstruction for odd ménage sizes

## Finding
Let \(\mathcal U_n\) consist of the permutations \(\pi\) of \(\{0,1,\ldots,n-1\}\) such that \(\pi(i)\notin\{i,i+1\pmod n\}\) at every position. Make a graph \(\mathcal T_n\) on \(\mathcal U_n\) by joining permutations differing by swapping the entries at exactly two positions, where the resulting permutation must remain in \(\mathcal U_n\).

**Theorem.** For every odd integer \(n\ge5\), the difference between the numbers of even and odd vertices of \(\mathcal T_n\) is exactly \(n-2\), so \(\mathcal T_n\) has **no Hamiltonian path**. In contrast, \(\mathcal T_6\) has a Hamiltonian cycle (a cyclic transposition Gray code) through all 80 ménage permutations. Its graph has 207 edges, radius 5 and diameter 6, with 48 vertices of eccentricity 5 and 32 of eccentricity 6. Immediately below, \(\mathcal T_5\) has two isolated vertices and a remaining component of 11 vertices and 15 edges; \(\mathcal T_4\) consists of two isolated vertices. No Hamiltonian-cycle assertion is made for even \(n>6\).

More precisely, for every integer \(n\ge3\), the even-minus-odd permutation count equals \(0\) for even \(n\) and \(n-2\) for odd \(n\). The unrestricted ménage numbers \(|\mathcal U_n|\) themselves are classical and are not claimed here.

## Assumptions and scope
Positions and values are labelled by residues modulo \(n\); no quotient by rotation, reflection, or relabelling is taken. A legal edge is a *single transposition of entries at arbitrary two positions*, not a neighboring-position swap. The graph is simple and undirected. A Hamiltonian path visits each of its vertices exactly once, while a Hamiltonian cycle also closes its final-to-first edge. The results for odd \(n\) are symbolic and unbounded; the Hamiltonian cycle, distances, and boundary component counts are finite statements for the stated orders.

## Proof
Let \(A_n\) be the \(n\)-by-\(n\) zero-one matrix with \((A_n)_{ij}=1\) precisely when the pair \((i,j)\) is permitted. Write \(A_n=J_n-I_n-P_n\), where \(P_n\) is the permutation matrix of the one-step cyclic shift. Its permanent is \(|\mathcal U_n|\), while its determinant is the sum of \(\operatorname{sgn}(\pi)\) over \(\mathcal U_n\), hence the difference between the two parity classes.

On the constant vectors, \(A_n\) has eigenvalue \(n-2\). On the other Fourier modes of the cyclic shift, its eigenvalues are \(-1-\zeta^k\), with \(1\le k<n\), where \(\zeta=e^{2\pi i/n}\). Thus
\[
\det A_n=(n-2)(-1)^{n-1}\prod_{k=1}^{n-1}(1+\zeta^k).
\]
For even \(n\), the factor with \(k=n/2\) vanishes. For odd \(n\), evaluating \(z^n-1\) at \(z=-1\) gives \(\prod_{k=0}^{n-1}(1+\zeta^k)=2\), so the indicated product is \(1\), and \((-1)^{n-1}=1\). This proves the parity formula without relying on finite enumeration.

Every legal move is a transposition and reverses permutation parity, so \(\mathcal T_n\) is bipartite with precisely these two parity classes. A Hamiltonian path in a bipartite graph must alternate between the classes, and therefore their cardinalities can differ by at most one. For every odd \(n\ge5\), the difference \(n-2\ge3\) excludes such a path.

For \(n=6\), the accompanying `hamiltonian_cycle.txt` lists exactly 80 zero-based indices in the **lexicographically ordered list of all permitted six-permutations**. The file gives the explicit finite certificate. `verify_menage.py` generates the full ordered state set, checks that these indices use every state once and that each successive pair, **including the last-to-first pair**, differs by one legal transposition. `verify_menage_alt.cpp` independently reconstructs the same set by C++ standard-library next-permutation and directly checks the certificate entry-by-entry. Both checkers thereby reduce the Hamiltonian-cycle assertion to elementary finite comparisons.

For the radius/diameter and \(n=5\) boundary, the Python checker constructs all transposition neighbors and performs a breadth-first search from each state; the C++ checker independently compares each pair of six-permutations and performs its own all-source breadth-first searches. These exhaust all 80 states and establish the numerical counts above; direct enumeration of the 13 five-permutations establishes the claimed three components. No computational evidence is needed for the unbounded parity obstruction.

## Verification
Place `verify_menage.py`, `verify_menage_alt.cpp`, and `hamiltonian_cycle.txt` beside one another. Run `python3 verify_menage.py`; compile with `g++ -std=c++17 -O2 verify_menage_alt.cpp -o verify_menage_alt` and run `./verify_menage_alt` in the same directory. The first checker prints `CYCLIC_MENAGE_GRAY_CODE_OK`, the second prints `ALTERNATE_HAMILTON_CYCLE_OK`; each asserts all its reported counts. The C++ checker also exhausts permutation parities for \(3\le n\le9\), corroborating but not replacing the determinant argument.

## Relationship to prior work
The classical Tait/Muir/Cayley–Lucas/Touchard ménage problem enumerates the valid permutations. Shevelev and Moses, arXiv:1101.5321 (first posted 2011-01-26), explicitly identify the matrix \(J_n-I-P_n\) and the permanent enumeration; their inspected paper studies counts conditioned on one placement, not transposition Gray codes. Zeilberger, arXiv:1401.1089 (first posted 2014-01-06), develops rigorous algorithms for the numbers of permutations with restricted positions, not their legal-transposition adjacency or Hamiltonicity. Bonamy et al., arXiv:1904.06184 (2019), introduce general four-cycle perfect-matching reconfiguration, but their theorems about graph classes do not supply this explicit 80-state Gray code or the signed ménage obstruction. Ordinary full-permutation transposition Gray codes do not enforce the two cyclic forbidden positions. Known ménage counts \(13\) and \(80\) are inputs, not claimed new results.

## Limitations
The negative statement excludes Hamiltonian **paths** for odd \(n\ge5\), but does not establish that the corresponding reconfiguration graph is disconnected: indeed Hamiltonian pathlessness is compatible with connectivity. The positive Gray code is certified only for \(n=6\). The index list is a finite proof witness, not an all-even-orders construction. The originality comparison is based on accessible primary literature and identified records; unindexed descriptions of the same restricted Gray code may exist. No independent scholarly audit is asserted.

## References
1. V. Shevelev and P. J. C. Moses, *The ménage problem with a known mathematician* (first posted 2011-01-26), arXiv:1101.5321, https://arxiv.org/abs/1101.5321.
2. D. Zeilberger, *Automatic Enumeration of Generalized Ménage Numbers* (2014), arXiv:1401.1089, https://arxiv.org/abs/1401.1089.
3. M. Bonamy et al., *The Perfect Matching Reconfiguration Problem* (2019), arXiv:1904.06184, https://arxiv.org/abs/1904.06184.
4. OEIS A000179, *Ménage numbers*, https://oeis.org/A000179 (only as a check on previously known scalar counts).
