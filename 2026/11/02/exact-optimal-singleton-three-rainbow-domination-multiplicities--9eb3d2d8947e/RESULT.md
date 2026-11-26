# Quadratic optimal singleton three-rainbow domination counts on Möbius ladders

## Finding

Let \(M_n\) be the Möbius ladder, with \(n\ge 6\) even, obtained from a labelled rim cycle \(C_n\) by adding the opposite chords \(v_iv_{i+n/2}\). A singleton three-rainbow dominating function is a map \(f:V(M_n)\to\{0,1,2,3\}\) such that every zero vertex sees all three distinct positive labels among its neighbours. The weight is the number of nonzero labels. When \(n\equiv 2\) or \(10\pmod{12}\) the minimum weight is \(n/2+2\), and the number \(a_n\) of minimum-weight functions with three named positive labels on labelled rim vertices is
\[
a_n=\begin{cases}
9n(3n-2)/2,&n\equiv2\pmod{12},\\
9n(3n-10)/2,&n\equiv10\pmod{12}.
\end{cases}
\]
For comparison, the multiplicity is already known to be \(12\) for \(n\equiv6\pmod{12}\) (minimum weight \(n/2\)) and \(6n\) for \(n\equiv0,4,8\pmod{12}\) (minimum weight \(n/2+1\)); see [4]. The contribution is the two quadratic multiplicities, not the previously established minimum weights or the constant and linear counts.

## Assumptions and scope

The graph is finite, undirected, simple and vertex-labelled. The three positive labels are distinguished; no vertex can carry more than one colour. The counts are of assignments, not orbits under graph automorphisms or colour permutations, and not set-valued rainbow domination counts.

## Proof

Put \(m=n/2\). Every zero has three coloured neighbours, so if there are \(z\) zeros and \(c\) coloured vertices, then \(3z\le 3c\), and the zero set is independent. Thus \(c\ge m\), with equality only when every edge crosses the zero–coloured cut. The graph is connected, so equality can only use one of the two bipartition supports when it is bipartite. For any independent zero support, the colouring constraints are exactly that the three neighbours of each zero form a rainbow triangle: take these triangles on the coloured vertices, with a proper three-colouring of their union.

**Triangle windows on a lifted strip.** Use columns \(i\in\mathbb Z\) and rows \(r\in\{0,1\}\), with the identification \((i+m,r)\sim(i,1-r)\). Rungs connect the two rows, and on the lifted strip consecutive columns connect in each row. There is at most one zero in a column. In any run of filled columns (columns containing a zero), the row of the zero alternates. In lifted columns \(A,\ldots,B\) of a single run, write its zero row as \(p+i\pmod 2\). The three neighbours of its zero at \(i\) are the three vertices in columns \(i-1,i,i+1\) on the complementary track, whose vertex in column \(j\) has row \(1-p+j\pmod 2\). When the list of complementary vertices in columns \(A-1,\ldots,B+1\) has no repeated physical vertex, the constraints are precisely successive rainbow windows of length three. There are six assignments on the list, given by choosing the first three colours in order and repeating with period three. In particular, vertices \(h\) steps apart on the list have equal colours if and only if \(3\mid h\). For a run of length \(m-1\) the two endpoints of this list lie over the same empty column. Their physical vertices are distinct when \(m\) is even and coincide when \(m\) is odd: the track row changes by \(m\bmod 2\) in the lift, while the identification flips the row. In the latter case the period-three sequence on the list must agree at positions separated by \(m\).

**Weight \(m\).** For even \(m\), a rim path of length \(m\) plus an opposite chord makes an odd cycle, excluding weight \(m\). For odd \(m\), all edges join opposite rim parities, and a weight-\(m\) zero support is one of these parities. For even rim zeros, write \(c_a=f(v_{2a+1})\) with \(a\) modulo \(m\) and \(s=(m-1)/2\). The zero at \(2a\) gives a rainbow triple \((c_{a-1},c_a,c_{a+s})\). Comparing the constraints at \(a\) and \(a+s+1\) forces \(c_{a+s+1}=c_{a-1}\), because \(2s+1=m\). Substituting this into the constraint at \(a+1\) makes consecutive triples rainbow and forces \(c_{a+3}=c_a\). This is possible only if \(3\mid m\). For odd \(m\) divisible by three, \(s\equiv1\pmod 3\), and each permutation of the three colours repeated with period three satisfies every constraint. The other parity gives the same count by rim rotation, so \(a_{2m}=12\).

**Weight \(m+1\).** Such a support has \(m-1\) filled columns and one empty column. For each of the \(m\) empty columns there are two row phases for the one run. If \(m\) is even, its complementary list contains all \(m+1\) coloured vertices without repetition. Each support has six colourings, so the minimum is \(m+1\), with \(a_{2m}=12m=6n\). If \(m\) is odd and \(3\nmid m\), the two endpoints of the list coincide but the sequence would force them to have different colours. Hence this weight is impossible there.

**Weight \(m+2\) for odd \(m\) with \(3\nmid m\).** There are two empty columns. Their cyclic distance \(d\) ranges from \(1\) to \(h=(m-1)/2\), and each such distance occurs for exactly \(m\) unordered pairs: the pairs \(\{i,i+d\}\) are distinct as \(i\) varies, since \(2d\not\equiv0\pmod m\). For \(d=1\), there is one run of length \(m-2\) with two possible row phases. Its complementary list contains \(m\) distinct vertices (one in each column); the two other coloured vertices are unconstrained. Each adjacent pair therefore gives \(2\cdot 6\cdot3^2=108\) assignments. This also proves that the minimum is \(m+2\).

For \(2\le d\le h\), the empty columns split the support into two runs of lengths \(d-1\) and \(m-d-1\), each with two phase choices. Because \(m\) is odd, the track index \(r-i\pmod2\) of a physical vertex is independent of its representative in the lift. Accordingly, each complementary list uses just one track. The lists go along opposite arcs between the empty columns, and only the endpoint columns can appear in both lists. For two of the phase choices the lists use different tracks. They are then disjoint and together use all \(m+2\) coloured vertices, yielding \(6^2=36\) assignments per choice. In the other two phase choices the lists use the same track. They share the two vertices in the empty columns; the other vertex in each of those columns is unconstrained. The two shared vertices are \(d\) steps apart on one list and \(m-d\) apart on the other. The lists must agree on whether the shared pair has equal colours. Since \(3\nmid m\), the two separations cannot both be divisible by three. Thus consistent colourings are possible exactly when neither is divisible by three. In that case both lists require distinct endpoint colours, and any ordered distinct pair prescribes the period-three colouring on each list uniquely. This gives \(3\cdot2\cdot3^2=54\) assignments per choice, and otherwise zero.

Let \(g=|\{d:2\le d\le h,\ 3\nmid d,\ 3\nmid(m-d)\}|\). The total is
\[
a_{2m}=108m+72m(h-1)+108mg.
\]
If \(m=6q+1\ge7\), then \(h=3q\), and the qualifying distances are \(d\equiv2\pmod3\), so \(g=q\). This gives \(18m(3m-1)=9n(3n-2)/2\). If \(m=6q+5\ge5\), then \(h=3q+2\), and the qualifying distances are \(d\equiv1\pmod3\), also giving \(g=q\). This gives \(18m(3m-5)=9n(3n-10)/2\).

## Verification

The standalone `verify.py` enumerates independent zero supports on each tested Möbius ladder, constructs the inequality graph on the coloured vertices, and counts its proper three-colourings by exact recursive search. It compares the coefficient at the stated minimum weight for all even orders from 6 through 42. Direct enumeration of all four-label assignments at that weight cross-checks orders 6, 8 and 10. Run `python3 verify.py`; the expected success marker is `VERIFY_OK`. These bounded computations are corroboration only; the all-order weight and multiplicity statements follow from the proof above.

## Relationship to prior work

Lange [1, Theorem 13 and Appendix A] proves the set-valued minimum weights with empty-or-singleton constructions, so the weights also hold for singleton functions. Kuzman [2, Theorem 4.5] determines related numbers for set-valued rainbow domination. The outer-independent set-valued enumeration [4] gives the constant and linear cases above because each optimum there uses only singleton positive sets. For \(n\equiv10\pmod{12}\), that enumeration concerns a smaller set-valued optimum that uses a double-coloured vertex, and does not count the singleton optima of weight \(n/2+2\). It does not treat \(n\equiv2\pmod{12}\). The cycle-prism enumeration [5] treats an untwisted boundary, not the Möbius ladder. Here the local count in the two quadratic cases distinguishes one run, two disjoint runs, and two runs coupled through shared endpoints.

## Limitations

The result gives only the minimum-weight coefficient, not the full weight polynomial. It concerns singleton assignments on labelled Möbius ladders, not functions modulo automorphisms, graph modifications or set-valued assignments. The literature comparison does not certify absolute historical priority.

## References

1. P. Lange, *Complexity, Bounds, and Exact Algorithms for Rainbow k-Domination in Regular Graphs*, arXiv:2610.06906v1, Theorems 7 and 13 and Appendix A. https://arxiv.org/html/2610.06906v1
2. B. Kuzman, *On k-rainbow domination in regular graphs*, arXiv:1907.08430v1, Theorems 3.1 and 4.5. https://arxiv.org/html/1907.08430v1
3. J. Žerovnik, *On Singleton 3-Rainbow Domination of Cylindrical Graphs*, Mathematics 14(16), 2917 (2026). https://www.mdpi.com/2227-7390/14/16/2917
4. *Rigidity and enumeration of minimum outer-independent three-rainbow functions on Möbius ladders*. https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-rigidity-and-enumeration-of-minimum-outer-independent-three-rain--e6c4969c972e/RESULT.md
5. *Exact optimal singleton three-rainbow domination multiplicities of cycle prisms*. https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-exact-optimal-singleton-three-rainbow-domination-multiplicities--6a2d2531557b/RESULT.md
