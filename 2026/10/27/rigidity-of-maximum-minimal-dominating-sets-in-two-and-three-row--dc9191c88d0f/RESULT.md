# The four maximum minimal dominating sets of even-length three-row grids

## Finding

Let \(G=P_3\square P_n\) with even \(n\ge2\), and label vertices by \((i,j)\), \(0\le i<n\), \(0\le j<3\). There are exactly four inclusion-minimal dominating sets of maximum cardinality \(3n/2\). Two are the two checkerboards, consisting of all vertices with a fixed parity of \(i+j\). The other two consist of all vertices in columns \(i\equiv0,3\pmod4\) or in columns \(i\equiv1,2\pmod4\), respectively. The count distinguishes labelled vertex sets.

## Assumptions and scope

Adjacency is Cartesian path adjacency: vertices differ by exactly one in one coordinate and agree in the other. The closed neighborhood is \(N[v]\). For a dominating set \(D\), minimality means that each \(v\in D\) has a private witness \(u\in N[v]\) with \(N[u]\cap D=\{v\}\), possibly \(u=v\). We maximize cardinality among sets minimal in this sense, not among minimum dominating sets.

## Proof

Each checkerboard is an independent dominating set and is therefore minimal; it has size \(3n/2\). The two column patterns select exactly half the columns when \(n\) is even. Every omitted column is horizontally adjacent to a selected column. Each selected column has a neighboring omitted column whose other horizontal neighbor is omitted or absent: the omitted runs have length two in the interior and may have length one at an endpoint. For each selected vertex, the vertex in the same row in such a neighboring omitted column is a private witness. The four constructions are distinct, including at \(n=2\).

We prove exhaustiveness by a finite-state induction. Each real column is a three-bit mask. Write \(\bot\) for an absent column. For a column \(i\), whether every vertex in that column is dominated and each selected vertex there has a private witness is determined by the five masks \((v_{i-2},\ldots,v_{i+2})\): a witness can be only in column \(i\) or an immediate neighbor and its own closed neighborhood uses masks at distance at most two from \(i\). In this test an absent vertex is never used as a witness. The enclosed verifier implements the test by checking the closed-neighborhood intersections.

Keep the last four masks as a state, initially \((\bot,\bot,\bot,\bot)\). Append a real mask, test the middle column of the resulting five-mask window if real, shift the four-mask state, and add the weight (number of set bits) of the appended mask. At a state \(s\) and length \(k\), store the largest prefix weight \(M_k(s)\) and its multiplicity \(C_k(s)\). On a transition keep the better weight, or add the multiplicities on a tie. A lighter prefix at the same state cannot become optimal: subsequent constraints and increments depend only on the four retained masks. After the last real mask append \(\bot\) twice with zero weight, testing the last two columns. Take the greatest weight over surviving final states and sum the counts for ties. This is exactly the maximum size and number of maximum minimal dominating sets, by the private-witness characterization.

The relevant maximum-weight and count vectors have equal state supports of size \(1285\) at lengths \(16,20,24\). The exact identities checked by `verify.py` (use `proof(3,16)`) are, for every state in that support,
\[
M_{20}=M_{16}+6,\qquad M_{24}=M_{16}+12,\qquad C_{24}-2C_{20}+C_{16}=0.
\]
The additive weight identities are coordinatewise on the whole support. Let \(L\) denote the action on multiplicities of taking four real-column transitions, using only the maximizing paths from the weights at length \(16\). Adding a common constant to the initial weights preserves all maximizing paths and hence leaves this same integer linear action on multiplicities. Thus \(C_{20}=LC_{16}\), \(C_{24}=LC_{20}\), and \(L(C_{20}-C_{16})=C_{20}-C_{16}\). It follows inductively that at length \(16+4q\) the weight vector is \(M_{16}+6q\) and the count vector is \(C_{16}+q(C_{20}-C_{16})\).

Taking zero or two further real-column transitions and then terminating also preserves the weight translation and acts by a fixed linear map on the corresponding count vectors. The finite certificate gives final weight and count \((24,4),(27,4),(30,4),(33,4)\) respectively at lengths \(16,18,20,22\). Hence in each even residue class the final count, affine in \(q\), has slope zero, and the final weight gains six per four columns. The even lengths \(2,4,6,8,10,12,14\) have terminal pairs \((3,4),(6,4),(9,4),(12,4),(15,4),(18,4),(21,4)\), from the same recurrence. This gives exactly four maxima of the asserted size at every even length. Since the four constructions already attain that size, the list is exhaustive.

## Verification

The unchanged standard-library Python 3.10+ file `verify.py` implements the five-mask predicate and exact integer certificate. Running it as supplied also checks other heights and parities; the argument here uses only the height-three state identities, the two even terminal residues, and the even base lengths. A bounded replay of just the height-three computation is `python3 -c 'import verify; print(verify.proof(3,16))'` from the directory containing the script. The finite computation certifies the state identities; the weight-translation and count-linearity induction supplies the unbounded conclusion. Direct small-graph enumeration in the script is secondary evidence.

## Relationship to prior work

The known bipartite identity \(\Gamma=\alpha\), as recorded by Fischermann and Volkmann [1, Theorem 2.3], gives the scalar size bound by pairing consecutive columns and taking a checkerboard. On an odd-length three-row grid, uniqueness already follows from their Theorem 3.5: a serpentine Hamilton path has odd order and its unique largest independent set is the larger checkerboard, so this is also the unique maximum minimal dominating set. Neither fact gives the even-length classification. On the open ladder \(P_2\square P_n\) the complete classification and counts 4 for odd lengths and 6 for even lengths are already given in the earlier Resultary record [2]; no height-two finding is claimed here. That work uses the same five-column locality and a weighted automaton, with a ladder-specific potential and tight-language certificate. The present proof instead certifies the statewise weight translation and count evolution on the larger three-row masks. Prisms \(C_n\square K_2\) have cyclic rather than path boundaries. OEIS A286847 counts minimal dominating sets summed over cardinalities, not the four sets at maximum size. Burdett, Haythorpe and Newcombe [3] study optimization formulations rather than the exhaustive structural list here. The inspected comparisons do not establish absolute historical priority.

## References

1. M. Fischermann and L. Volkmann, *Unique Independence, Upper Domination and Upper Irredundance in Graphs*, J. Combin. Math. Combin. Comput. 47 (2003), 237–249. https://combinatorialpress.com/article/jcmcc/Volume%20047/vol-047-paper%2018.pdf
2. *All maximum minimal dominating sets of ladder graphs*, Resultary record `SCOPE-all-maximum-minimal-dominating-sets-of-ladder-graphs--ee60eed8ab77`. https://github.com/Resultary/2026/tree/main/2026/10/12/SCOPE-all-maximum-minimal-dominating-sets-of-ladder-graphs--ee60eed8ab77
3. R. Burdett, M. Haythorpe and A. Newcombe, *Binary programming formulations for the upper domination problem*, Math. Methods Oper. Res. 98 (2023), 155–168, doi:10.1007/s00186-023-00831-2.
