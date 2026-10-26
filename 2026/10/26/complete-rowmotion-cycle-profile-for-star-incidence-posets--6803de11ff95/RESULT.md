# Complete rowmotion cycle profile for star-incidence posets

## Finding

For every integer \(n\ge 2\), let \(P_n\) be the vertex–edge incidence poset of the star \(K_{1,n}\). Classical rowmotion on its lattice \(J(P_n)\) of order ideals has exactly these cycles:

\[
\begin{array}{c|c}
\text{cycle length}&\text{number of cycles}\\\hline
2&1\\
3&1+\dfrac{3^n-3\cdot 2^n+3}{3}\\
8&2^{n-1}-1
\end{array}
\]

No other cycle lengths occur. Consequently, \(|J(P_n)|=2^n+3^n\) and the rowmotion permutation has order \(24\). The principal result is the **complete cycle multiplicity distribution**, not the period alone.

## Assumptions and scope

The poset \(P_n\) has minimal vertex elements \(c,\ell_1,\ldots,\ell_n\) and maximal edge elements \(e_1,\ldots,e_n\), with \(c<e_i\), \(\ell_i<e_i\) and no other distinct-element comparabilities. An order ideal is downward closed. The map is
\[
R(I)=\mathord{\downarrow}\min(P_n\setminus I),
\]
where \(\min\) takes the elements minimal in the induced complementary subposet. All ideals are labeled by the specified star arms; the enumeration is of actual rowmotion orbits, not of orbits modulo automorphisms.

## Proof

**Normal forms.** If \(c\notin I\), then no edge belongs to \(I\), so uniquely \(I=A(S)\), comprising the leaves indexed by \(S\subseteq[n]\). If \(c\in I\), write uniquely \(I=B(w)\), where \(w\in\{0,1,2\}^n\); the digit at arm \(i\) records, respectively, inclusion of neither \(\ell_i\) nor \(e_i\), inclusion of \(\ell_i\) only, or inclusion of both. Thus there are \(2^n+3^n\) ideals.

**Transition lemma.** Direct inspection of minimal complementary elements gives
\[
R(A(S))=B(u_S),\qquad (u_S)_i=\begin{cases}0&i\in S,\\1&i\notin S.\end{cases}
\]
If \(w\) has at least one digit \(1\), the center remains in the image and
\[
R(B(w))=B(w+\mathbf1\pmod 3).
\]
Indeed, each arm state \(0\) contributes its missing leaf to the complement minima, state \(1\) contributes its missing edge, and state \(2\) contributes nothing. If \(w\) has no digit \(1\), no missing edge is minimal and the center leaves the image:
\[
R(B(w))=A(\{i:w_i=0\}).
\]
These equations are valid for all \(n\ge1\).

**Cycles.** The constant words give the disjoint cycles
\[
A([n])\longrightarrow B(0^n)\longrightarrow A([n])
\]
and
\[
A(\varnothing)\longrightarrow B(1^n)\longrightarrow B(2^n)\longrightarrow A(\varnothing).
\]
If a word contains every one of the three digits, coordinatewise addition of \(1\pmod3\) preserves the three-symbol condition and has orbit length exactly \(3\). Inclusion–exclusion counts exactly \(3^n-3\cdot2^n+3\) such words, or \((3^n-3\cdot2^n+3)/3\) additional three-cycles.

It remains to classify nonconstant words with only two symbols and nontrivial subsets \(S\subsetneq[n]\), \(S\ne\varnothing\). Write \(B((a,b)_S)\) for the word equal to \(a\) on \(S\) and \(b\) on its complement \(S^c\). The transition lemma gives the following eight *distinct* ideals in an orbit:
\[
\begin{aligned}
B((0,2)_S)&\to A(S)\to B((0,1)_S)\to B((1,2)_S)\\
&\to B((2,0)_S)\to A(S^c)\to B((1,0)_S)\\
&\to B((2,1)_S)\to B((0,2)_S).
\end{aligned}
\]
Distinctness follows because both \(S\) and \(S^c\) are nonempty and the eight displayed normal forms are distinct. Interchanging \(S\) and \(S^c\) describes the same eight-cycle; no other identification is possible because its only two center-free ideals are \(A(S)\) and \(A(S^c)\). Thus the \(2^n-2\) nonempty proper subsets yield exactly \((2^n-2)/2=2^{n-1}-1\) eight-cycles.

The classified cases exhaust all \(A(S)\) and \(B(w)\), prove the table, and imply that the least common multiple of all occurring cycle lengths is \(\operatorname{lcm}(2,3,8)=24\) for \(n\ge2\). As a checksum, the weighted cycle counts sum to \(2^n+3^n\). \(\square\)

## Verification

The standalone `verify.py` enumerates **all** order ideals independently as bitmasks of the \(2n+1\)-element incidence poset; it computes minimal complements from the order relations (without using the ternary transition lemma) and exhaustively builds rowmotion cycles for \(1\le n\le8\). The observed profiles agree with the formulas. The verifier is a finite consistency check, whereas the case analysis above establishes the unrestricted theorem.

## Relationship to prior work

Grinberg and Roby, *Iterative properties of birational rowmotion I: generalities and skeletal posets* (2016, arXiv first public 2014), develop general period computations for skeletal/graded-forest posets; their Proposition 94 gives the known three-cycle of level ideals, and Proposition 101 relates classical and birational periods. Their fuller arXiv version gives the corresponding statements in Section 10. Those results do **not** themselves state a formula for the entire length-\(2\), length-\(3\), and length-\(8\) orbit multiplicities on the specified star-incidence family. In particular the period \(24\) alone is not asserted to be new.

Striker and Williams treat promotion/rowmotion for other structured poset families. Dangwal and collaborators study *rooted* trees, requiring a unique minimal element; our incidence poset has \(n+1\) minimal elements and its dual has \(n\) minimal elements for \(n\ge2\), so neither orientation satisfies that hypothesis. The cardinality sequence \(2^n+3^n\) appears in OEIS A007689 as a numerical sequence, without thereby covering these rowmotion orbit multiplicities.

## Limitations

This is a classical order-ideal rowmotion result for this graph-incidence family; it does not classify rowmotion for general graph-incidence posets or the birational orbit geometry. The explicit cycle decomposition is proved for every integer \(n\ge2\), but the attached exhaustive program tests only \(1\le n\le8\). Literature search cannot exclude every unindexed computation or unpublished derivation.

## References

1. D. Grinberg and T. Roby, *Iterative properties of birational rowmotion I: generalities and skeletal posets*, Electronic Journal of Combinatorics 23(1), P1.33 (2016), Sections 10–11, Propositions 94 and 101–105; earliest arXiv record dated 2014-02-25, arXiv:1402.6178. https://arxiv.org/abs/1402.6178 ; https://www.combinatorics.org/ojs/index.php/eljc/article/download/v23i1p33/pdf/
2. J. Striker and N. Williams, *Promotion and rowmotion*, European Journal of Combinatorics 33 (2012), 1919–1942, arXiv:1108.1172. https://arxiv.org/abs/1108.1172
3. P. Dangwal, J. Kimble, J. Liang, J. Lou, B. E. Sagan, and Z. Stewart, *Rowmotion on rooted trees*, dated 2022-08-25, especially Sections 1 and 3. https://users.math.msu.edu/users/bsagan/Papers/Old/rrt.pdf
4. OEIS Foundation, A007689, \(2^n+3^n\). https://oeis.org/A007689
