# Six optimal perfect Italian functions on triangular clique paths

## Finding
For every integer \(n\ge 4\), the Cartesian product \(G_n=K_3\square P_n\) has perfect Italian domination number
\[
\gamma_I^p(G_n)=n+2.
\]
Moreover, **exactly six** functions attain this weight, with labeled vertices and distinguishable labels \(0,1,2\). Every minimum function uses only \(0\) and \(1\), and the six form one orbit under the six permutations of the three row labels.

## Assumptions and scope
The graph is finite, simple, undirected. Label its vertices \((r,j)\), where \(r\in\{0,1,2\}\) is a row and \(1\le j\le n\) is a path column. Edges join distinct rows in the same column, and equal rows in consecutive columns. A perfect Italian dominating function is a map \(f:V(G_n)\to\{0,1,2\}\) such that every zero vertex has total label **exactly** \(2\) over its open neighborhood. Its weight is \(\sum_v f(v)\). Nonzero vertices need satisfy no local condition. The claim covers \(n\ge4\); the short lengths \(n=2,3\) do not have the same six-minimum conclusion.

To specify the six minima, choose an arbitrary permutation \(\pi\) of the row set. Put \(r_j=\pi((j-1)\bmod3)\). In column \(1\), place ones exactly at \(r_1,r_2\); in each column \(j\) with \(2\le j<n\), place one at \(r_j\); in column \(n\), place ones at \(r_{n-1},r_n\). All unmentioned positions have label zero. These are all six minimum functions.

## Proof
For a column \(b=(b_0,b_1,b_2)\in\{0,1,2\}^3\), write \(w(b)=b_0+b_1+b_2\). Introduce a zero phantom column outside each end of the path. For three consecutive columns \(a,b,c\), the condition on every zero in the middle column is
\[
 E(a,b,c):\quad b_r=0\Longrightarrow w(b)+a_r+c_r=2
 \quad(r=0,1,2).
\]
This identity is exact: \(w(b)\) counts both clique neighbors because the tested entry \(b_r\) is zero, and the two other terms count longitudinal neighbors. It is also sufficient for valid domination.

Number the 27 possible column vectors. Let \(D_\ell(b,c)=(d_\ell(b,c),m_\ell(b,c))\) record the **least** total weight and the exact number of tied column sequences of length \(\ell\) ending in columns \(b,c\), with constraints already checked at columns \(1,\ldots,\ell-1\). An impossible state has weight \(\infty\) and multiplicity \(0\). For \(\ell=2\), each \(E(0,b,c)\)-admissible pair receives \((w(b)+w(c),1)\). For every next vector \(d\), admissibility requires \(E(b,c,d)\), and the transition to the pair \((c,d)\) adds \(w(d)\); take the minimum over all preceding \(b\) and sum multiplicities on ties. Acceptance for length \(\ell\) requires the last-column predicate \(E(b,c,0)\). These rules exhaust all labelings exactly once, so the minimum final weight and summed tied multiplicity are the required global minimum and number of minimum functions.

**Finite exact certificate and infinite induction.** The standalone `verify.py` contains the explicit 27-vector alphabet, the neighborhood predicate, the recurrence, and a complete exact-integer evaluation of all 729 column-pair states. It verifies the full-state identity
\[
 D_{14}=\operatorname{shift}_1(D_{13}),
\]
where \(\operatorname{shift}_1\) increases every finite state weight by one and leaves every state multiplicity unchanged (including all unreachable states). There are 306 reachable states in each vector. Its second check evaluates the final objective for **every** length from 4 through 14, yielding exactly \((n+2,6)\) in each case. This is a finite check of fully specified integer identities, not an extrapolation.

Let \(T\) be the exact state transition. By construction \(T(\operatorname{shift}_1D)=\operatorname{shift}_1(TD)\): adding the same constant to every finite prefix weight preserves which predecessors minimize and their tie counts. Thus \(D_{14}=\operatorname{shift}_1D_{13}\) implies inductively
\[
 D_{\ell+1}=\operatorname{shift}_1D_\ell\quad\text{for all }\ell\ge13.
\]
The final acceptance operation also commutes with a uniform shift, proving by induction that for **every** length \(n\ge4\) the minimum and exact multiplicity are \((n+2,6)\).

Finally, the six permutation constructions above have weights \(2+(n-2)+2=n+2\). Each zero in an interior column sees exactly two ones: the clique choice in its own column and exactly one longitudinal one as required by the period-three row pattern; endpoint zeros see both ones inside their endpoint clique column and no positive longitudinal neighbor. This follows directly by considering the three consecutive distinct row labels; `verify.py` also checks each construction independently for lengths 4 through 49. The six choices of \(\pi\) produce distinct assignments for \(n\ge4\). Since the exact count of minima is six, these are **all** the minima, and no minimum contains a label \(2\).

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter. The program checks the full 729-state stationarity equality, the 11 consecutive base lengths \(4\) through \(14\), the six explicit periodic witnesses for lengths \(4\) through \(49\), and an independent exhaustive vertex-neighborhood search through every labeling of weight at most \(n+2\) for \(n\in\{4,5,6\}\). Its final output begins `VERIFY_OK`. The normalized length-13 state-vector SHA-256 digest is `0bdb58621f1fc0b6e856772936a4aa4ba48fd51886d2e1d3f9d27cafbd2db188`.

The infinite theorem is established by the fully specified finite recurrence and its exact algebraic shift induction; the short independent graph searches are corroborating checks, not the infinite proof.

## Relationship to prior work
Lauri and Mitillos (2019) define perfect Italian domination, connect binary-valued perfect Italian functions with 2-fair dominating sets, and evaluate selected regular graphs, including the two-column triangular prism. Varghese and Lakshmanan (2019 preprint; published 2023) give general Cartesian-product bounds and exact numerical results for \(P_2\square P_n\) and \(K_m\square K_n\), but do not state this triangular-clique path theorem or count its minimum functions. The 2019 two-fair-domination literature treats related toroidal graphs. Almulhim (2024) studies hardness and upper bounds on Cartesian products; only abstract-level material from that article could be inspected. The present result supplies the exact three-row infinite strip value and all equality cases rather than a general upper bound.

## Limitations
This result concerns **only** \(K_3\square P_n\) with \(n\ge4\), ordinary perfect Italian domination (not perfect Roman or nonperfect Italian domination), and labeled vertices. No extrapolation to wider clique strips, closed-neighborhood constraints, or cyclic paths is asserted. Originality is a literature-supported priority assessment, not an independently certified worldwide uniqueness claim. A potentially relevant 2024 Cartesian-product article was not read in full. No independent mathematical audit has been performed.

## References
1. J. Lauri and C. Mitillos, *Perfect Italian domination on planar and regular graphs* (first public 2019-05-15), arXiv:1905.06293. https://arxiv.org/html/1905.06293v2
2. J. Varghese and A. Lakshmanan S., *Perfect Italian Domination Number of Graphs* (first public 2019-10-27), arXiv:1910.12260; Palestine Journal of Mathematics 12(1), 158–168 (2023). https://arxiv.org/html/1910.12260v2
3. *On the two Fair domination in graphs* (2019), International Journal of Advanced Trends in Computer Science and Engineering 8(6). https://kalaharijournals.com/resources/DEC_637.pdf
4. A. Almulhim, *Perfect Roman and Perfect Italian Domination of Cartesian Product Graphs*, Scientific Journal of King Faisal University 25, 63–68 (2024), published 2024-11-28. https://doi.org/10.37575/b/sci/240037
