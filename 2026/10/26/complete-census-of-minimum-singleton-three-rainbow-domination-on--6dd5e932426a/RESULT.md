# Completing the weight-(n+2) census for singleton three-rainbow domination on prisms

## Finding

Let \(G_n=C_n\square K_2\) be the labeled simple prism, \(n\ge3\). Assign each vertex a label in \(\{0,1,2,3\}\) such that every vertex labeled zero has neighbors with all three positive labels. The weight of an assignment is the number of nonzero labels. Let \(a_{n,j}\) be the number of these assignments of weight \(j\), counted with named colors and distinguished vertices. Then

\[
a_{n,n+2}=
\begin{cases}
36n(2n-3),& n\text{ odd},\\
108n(n-2),& 6\mid n.
\end{cases}
\]

These are the two regimes in which weight \(n+2\) is not optimal: it is one above the minimum for odd \(n\) and two above it for \(6\mid n\). Thus the theorem supplies the nonminimum branches needed for the exact weight-\(n+2\) coefficient over all circumferences. It does not claim the minimum weights or minimum multiplicities as new.

## Assumptions and scope

The vertices are \((i,r)\) with \(i\in\mathbb Z/n\mathbb Z\), \(r\in\{0,1\}\). Each vertex is adjacent to its rung-mate and to the two cyclic neighbors in its row. Even at \(n=3\) the cyclic neighbors are distinct. Assignments are not quotiented by a color permutation, rotation, reflection, or row exchange. A vertex cannot carry a multiset of colors.

## Proof

The zero vertices form an independent set, because their three neighbors must carry three different positive labels. Each rung has at most one zero. At weight \(n+2\) exactly two rungs therefore have no zero; call these holes. On each intervening nonempty run of rungs the zeros alternate rows, with two possible orientations.

**Run colorings.** For a run of length \(\ell\ge1\), write its sequence of positive rung-mate colors between the two colors at its boundary holes that are adjacent to the end zeros. The zero constraint is exactly that every consecutive triple in this sequence of length \(\ell+2\) has distinct colors. There are six such sequences, uniquely specified by the initial ordered pair of unequal colors and the forced cyclic repetition of the three colors. The endpoints lie \(\ell+1\) positions apart. They must therefore agree when \(\ell\equiv2\pmod3\) and differ otherwise. For a given ordered equal pair in the first case there are two sequences, and for a given ordered unequal pair in the second case there is one. Thus the matrix of endpoint-color counts is \(R_\ell=2I_3\) if \(\ell\equiv2\pmod3\) and \(R_\ell=J_3-I_3\) otherwise. Every row and column sums to two.

**Adjacent holes.** There are \(n\) unordered adjacent pairs. Each gives one run of length \(n-2\), including a length-one run when \(n=3\). Each sequence fixes one vertex at each hole, leaving its other vertex free. The number of assignments per pair is \(2\cdot6\cdot3^2=108\).

**Nonadjacent holes.** With directed cyclic distance \(d\), \(2\le d\le n-2\), the run lengths are \(p=d-1\), \(q=n-d-1\). There are four orientation choices. At either hole the two run-end constraints can refer to the same vertex, or to different vertices. Following a run of length \(\ell\) changes the zero row exactly \(\ell-1\) times. Hence the same/different relation is reversed between holes precisely when \((p-1)+(q-1)=n-4\) is odd.

For odd \(n\), exactly one hole shares its constrained vertex in every orientation. Matching the color there yields \(3\cdot2^2\) pairs of sequences by the constant row and column sums of the run matrices. The other vertex at that shared hole is free; every other hole color is determined. Thus the count per nonadjacent unordered pair is \(4\cdot3\cdot2^2\cdot3=144\). The total is \(108n+144(\binom n2-n)=36n(2n-3)\).

For \(6\mid n\), two choices of orientations share the two constrained vertices (one at each hole) and two choices refer to different vertices at both holes. In the latter case there are \(6^2\) sequence pairs, with nothing free. In the shared case match corresponding endpoint colors between runs, giving \(\operatorname{tr}(R_pR_q)\) pairs by symmetry of the matrices. Each of the two remaining vertices is free. Hence the count for distance \(d\) is
\[
B_n(d)=2\bigl(36+9\operatorname{tr}(R_pR_q)\bigr).
\]
For \(n=6s\), the distances \(2,\ldots,n-2\) contain \(2s-1\) of each class modulo three. For \(d\equiv0\pmod3\) both matrices are \(2I_3\) and the trace is 12, giving \(B_n(d)=288\). In the other two classes both matrices are \(J_3-I_3\) and the trace is 6, giving 180. Each unordered nonadjacent pair arises twice in the directed-distance sum over the \(n\) starting positions (also at diametrical separation). The total is \(108n+\tfrac n2(2s-1)(288+180+180)=108n(n-2)\), as required.

## Verification and limits

The accompanying `verify.py` can be run with the Python 3 standard library and compared with `verify_output.txt`. It tests these coefficients as part of a larger finite comparison, using direct vertex assignments at \(n=3,4,5\) and exact support-and-color counting at \(3\le n\le24\). The finite checks corroborate rather than replace the all-circumference proof. No formula for weights above \(n+2\) is established here.

## Relationship to other results

Lange, *Complexity, Bounds, and Exact Algorithms for Rainbow k-Domination in Regular Graphs*, arXiv:2610.06906v1, Theorem 19, gives the optimal weight \(n+1\) for odd \(n\), \(n\) for \(6\mid n\), and \(n+2\) for the other even \(n\). Žerovnik, *On Singleton 3-Rainbow Domination of Cylindrical Graphs*, DOI:10.3390/math14162917, gives bounds and exact weights for cylinder subfamilies, not the nonminimum counts shown here. The indexed *Exact optimal singleton three-rainbow domination multiplicities* result (Resultary 6a2d2531557b) gives the labeled minima for all \(n\), the two lower candidate coefficients, and the weight-\(n+2\) coefficient in the other even classes, where it equals the optimal count. The table there does not give the two nonminimum branches addressed in this theorem. This comparison does not establish priority. Allagan et al., DOI:10.1155/ijmm/1411005, enumerate ordinary minimum dominating sets, a different invariant.
