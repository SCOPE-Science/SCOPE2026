# Rational reflection and page-permutation character of pentagonal edge-book matching complexes

## Finding
For each integer \(n\ge2\), construct the *pentagonal edge-book* \(B_n\) by gluing \(n\) pentagons along one common edge \(uv\). More explicitly, its vertices are \(u,v,a_i,b_i,c_i\) (\(1\le i\le n\)), and its edges are the common edge \(F=uv\) and, in each page, \(A_i=ua_i\), \(B_i=a_ib_i\), \(C_i=b_ic_i\), \(D_i=c_iv\). Let \(\operatorname{Match}(B_n)\) denote the ordinary matching complex: the vertices are edges of \(B_n\), and simplices are matchings of those edges.

The automorphisms permuting pages and simultaneously reversing each page generate \(S_n\times C_2\). Write \(\tau\) for reversal of \(u,v\), so \(\tau(A_i)=D_i\) and \(\tau(B_i)=C_i\). The complete **reduced rational homology representation** is
\[
\widetilde H_j(\operatorname{Match}(B_n);\mathbb Q)\cong
\begin{cases}
(\operatorname{sgn}_{n}\otimes\mathbb Q^{n})\boxtimes\varepsilon^{\otimes n},&j=n,\\
0,&j\ne n,
\end{cases}
\]
where \(\mathbb Q^n\) is the natural page-permutation representation of \(S_n\), and \(\varepsilon\) is the sign character of \(C_2\). Equivalently, for \(\pi\in S_n\), \(h\in\{0,1\}\), and \(f(\pi)=\#\{i:\pi(i)=i\}\),
\[
\operatorname{tr}\bigl(\pi\tau^h\mid\widetilde H_n(\operatorname{Match}(B_n);\mathbb Q)\bigr)
=(-1)^{nh}\operatorname{sgn}(\pi)f(\pi).
\]
The \(S_n\) factor decomposes as \(\operatorname{sgn}_n\oplus\operatorname{Sp}^{(2,1^{n-2})}\). This is an exact all-parameter **equivariant homology classification**, not a claim of an equivariant wedge-of-spheres decomposition.

## Assumptions and scope
The graph is simple, undirected, and exactly the edge-book described above. Every page has three distinct internal vertices; no other identifications or edges are allowed. The group action is the natural page permutation and global reversal. All representation statements are over \(\mathbb Q\). The theorem applies to every integer \(n\ge2\) and to every group element, including permutations with no fixed pages. The reduced homology is in the standard simplicial orientation convention.

## Proof
**1. Concentration in degree \(n\).** Work with the augmented face poset, including the empty matching. For a matching \(S\), choose the least index \(i\) with neither \(A_i\) nor \(C_i\) in \(S\), if it exists, and match \(S\) with \(S\triangle\{B_i\}\). This is legal because \(B_i\) conflicts only with \(A_i\) and \(C_i\). Pages for which neither \(A_i\) nor \(C_i\) occurs can never change under this toggle. Within a fixed pattern of these endpoint blockers, the least such page is fixed, and the matching toggles a cone vertex, so the matching is acyclic. Along unmatched face deletions, the set of pages lacking both blockers can only increase; consequently an alternating closed path cannot move between these patterns.

The remaining faces have, for each \(i\), at least one of \(A_i,C_i\). At most one \(A_i\) can occur, because all \(A_i\) meet \(u\). Put \(C=\{C_1,\ldots,C_n\}\). The residual faces are exactly \(C\), \(C\cup\{F\}\), and, for each \(i\),
\[
U_i=C\cup\{A_i\},\qquad
T_i=(C\setminus\{C_i\})\cup\{A_i\},\qquad
V_i=T_i\cup\{D_i\}.
\]
Match \(C\) to \(C\cup\{F\}\), and \(T_i\) to \(U_i\). All these pairs are covering relations. In the residual directed Hasse graph the only unmatched arrows not entering the already matched part are \(V_i\to T_i\) and \(U_i\to C\), so it has no directed cycle. From a residual face, deleting a blocker can only move into a first-stage stratum, never back. This proves acyclicity of the combined augmented matching. Exactly the \(n\) faces \(V_i\), each of cardinality \(n+1\), remain critical. Augmented discrete Morse theory gives vanishing of reduced homology except in degree \(n\), with rank \(n\); it also yields the nonequivariant wedge \(\bigvee^n S^n\). The latter type is obtainable from existing nonequivariant contraction tools and is **not** the originality claim.

**2. The signed orbit formula.** Let \(g\) be any simplicial automorphism. For a \(g\)-invariant matching \(S\), let \(o_g(S)\) be the number of cycles of its permutation on the edges belonging to \(S\). The contribution of \(S\) to the signed augmented simplicial trace is \((-1)^{o_g(S)}\): an orbit contributes one negative factor, since the parity of its permutation on vertices is \((-1)^{|S|-o_g(S)}\). Hence, setting
\[
Z_g=\sum_{S:\,gS=S}(-1)^{o_g(S)},
\]
the reduced Lefschetz trace is \(-Z_g\). Since all reduced homology lies in degree \(n\), the actual degree-\(n\) character is \(\chi_n(g)=(-1)^{n+1}Z_g\). In particular \(Z_1=(-1)^{n+1}n\).

**3. Pure page permutations.** Let \(\pi\in S_n\), with \(f\) fixed pages and \(t\) page cycles of length at least two. For each nontrivial page cycle, an invariant matching may select one of the two admissible orbits consisting entirely of page-middle edges \(B\) or entirely of \(C\), or select neither, but never both. Their signed orbit sum is \(1-1-1=-1\); orbits involving \(A\) or \(D\) fail the matching condition. Fixed pages together with \(F\) have signed orbit sum \((-1)^{f+1}f\), including \(f=0\), when \(F\) cancels the empty matching. Thus
\[
Z_{\pi}=(-1)^t(-1)^{f+1}f,\qquad
\chi_n(\pi)=(-1)^{n+f+t}f=\operatorname{sgn}(\pi)f.
\]
The final equality holds because \(n-f-t\) is the total of \(\ell-1\) over all nontrivial cycle lengths \(\ell\), modulo two.

**4. Permutations followed by global reversal.** Let \(e\) be the number of even cycles of \(\pi\). Under \(\tau\pi\), an odd cycle of length at least three has no selectable full edge orbit: the \(A/D\) orbit repeats \(u,v\), and the \(B/C\) orbit meets itself within each page. An even cycle of length at least four has exactly two individually admissible \(B/C\) orbits, mutually incompatible, so has signed sum \(-1\). For a cycle of length two the same two middle-edge orbits occur, and there are two additional admissible endpoint \(A/D\) orbits; any choice involving an endpoint orbit cancels via toggling its unique compatible middle-edge orbit. Therefore every even page cycle again contributes \(-1\). A fixed page has a single admissible endpoint orbit \(\{A_i,D_i\}\), with weight \(-1\); such orbits from different fixed pages conflict with each other and with \(F\). Their total signed contribution, including \(F\), is \((1-f)-1=-f\). Combining factors gives
\[
Z_{\tau\pi}=(-1)^e(-f),\qquad
\chi_n(\tau\pi)=(-1)^n(-1)^ef=(-1)^n\operatorname{sgn}(\pi)f.
\]
Here \(\operatorname{sgn}(\pi)=(-1)^e\), since precisely even cycles contribute negative signs.

**5. Representation identification.** The natural permutation module \(\mathbb Q^n\) has character \(f(\pi)\). Tensoring by the alternating character of \(S_n\) and the \(n\)-fold sign of \(C_2\) gives exactly the computed character on every element of \(S_n\times C_2\). Rational representations of this finite group are semisimple and the displayed rational character determines the module, proving the claim. The Specht decomposition follows by tensoring the trivial-plus-standard decomposition of the permutation module with the sign character.

## Verification
Two standalone Python programs are included: `checks/pentabook_verify.py` enumerates every face, tests each proposed augmented Morse matching pair and every critical simplex, and topologically sorts the **entire** oriented Hasse graph for \(1\le n\le7\). It processed 70,713 faces at \(n=7\). The other, `checks/pentabook_character.py`, independently enumerates invariant faces with their permutation-orientation signs and verifies the closed formula for **all** \(2n!\) group elements for \(1\le n\le5\). Both programs completed with `MATCHING_OK` and `CHAR_OK`. Run them together from the containing directory using `python3 checks/pentabook_verify.py` and `python3 checks/pentabook_character.py`. Finite calculations serve as consistency checks only; Steps 1–5 prove the assertions for all permitted \(n\).

## Relationship to prior work
Donovan and Scoville, arXiv:2207.13780, §5, Theorem 30 classify matching complexes of *vertex*-glued Dutch windmills, not edge-books, and do not compute the present group character. Bayer, Jelić Milutinović and Vega, arXiv:2211.12559, Propositions 10–11 provide contractions sufficient for a nonequivariant wedge calculation for these edge-books, while Theorem 19 treats *linear* pentagonal tilings, in which no three polygons share one edge. The nonequivariant wedge is therefore not presented as novel. Bate, Everitt, Ford and Ramos, arXiv:2312.13750, study equivariant homology of matching complexes of complete hypergraphs and asymptotic fibre-closed families; their examined general statements do not calculate this edge-book character. The new statement is the exact \(S_n\times C_2\) rational action, including its reflection parity and Specht summands.

## Limitations
No integral \(\mathbb Z[S_n\times C_2]\)-module decomposition, canonical equivariant collapse, equivariant wedge splitting, or higher homotopy action is asserted. The proof fixes the given graph structure; it does not cover arbitrary polygonal lines, other page lengths, or n=1 with its differently presented full automorphism group. The literature comparison reduces but cannot eliminate the risk of an unindexed equivalent result.

## References
1. C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780, first posted 27 July 2022. Section 5, especially Theorem 30. https://arxiv.org/html/2207.13780v1
2. M. Bayer, M. Jelić Milutinović and J. Vega, *General polygonal line tilings and their matching complexes*, arXiv:2211.12559, first posted 22 November 2022. Propositions 10–11 and Theorem 19. https://arxiv.org/pdf/2211.12559
3. M. Bate, B. Everitt, S. Ford and E. Ramos, *Homology of matching complexes and representations of symmetric groups*, arXiv:2312.13750, first posted 21 December 2023. Sections 1–3. https://arxiv.org/pdf/2312.13750
