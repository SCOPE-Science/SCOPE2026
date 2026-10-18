# Two marked cells in cyclic Latin tables: an exact subgroup partition and one exceptional orbit-recovery case

## Finding
Let \(n\ge2\), let \(g\in\mathbb Z/n\mathbb Z\setminus\{0\}\), and consider the finite relational structure on \(X=(\mathbb Z/n\mathbb Z)^2\) with three **separately named**, reflexive equivalence relations
\[
E_R((x,y),(x',y'))\iff x=x',\qquad
E_C((x,y),(x',y'))\iff y=y',\qquad
E_S((x,y),(x',y'))\iff x+y=x'+y'\pmod n.
\]
Start synchronous one-dimensional counting colour refinement with distinct singleton colours at \(A=(0,0)\) and \(B=(0,g)\), and one common colour on every other cell. Put \(H=\langle g\rangle\), \(h=|H|=n/\gcd(n,g)\), and \(k=[\mathbb Z/n\mathbb Z:H]=n/h\).

**Theorem.** The stable classes are exactly the following nonempty sets:
\[
\begin{array}{ll}
P_{a,b}=\{(a,b)\},& a,b\in H;\\
R_a=\{(a,y):y\notin H\},&a\in H;\\
C_b=\{(x,b):x\notin H\},&b\in H;\\
S_c=\{(x,y):x,y\notin H,\ x+y=c\},&c\in H;\\
Z=\{(x,y):x,y,x+y\notin H\}.&
\end{array}
\]
The classes \(R_a,C_b,S_c\) occur exactly when \(k\ge2\); the class \(Z\) occurs exactly when \(k\ge3\). Their sizes are, respectively, \(1\), \(n-h\), and \((n-h)(n-2h)\). Consequently, the exact stable colour-class count is
\[
\boxed{h^2+3h\,\mathbf1_{k\ge2}+\mathbf1_{k\ge3}}.
\]
These stable classes equal the orbits of the full automorphism group of this **three-relation, two-marked structure** if and only if
\[
\boxed{k=1\quad\text{or}\quad (n,h)=(4,2)}.
\]
In particular, when the marked column difference does not generate the cyclic group, the only orbit-exact case is the opposite-pair marking of the four-element cyclic group.

## Assumptions and scope
All groups are finite additive cyclic groups. The three equivalence relations remain separately named; this is not colour refinement of the unlabelled Latin-square graph formed by their union. The two marked cells have *different* named initial colours. For a cyclic addition table and any two distinct marked cells in the same row, an unmarked affine translation, column translation, and multiplication by a unit transport the configuration to the stated form with the same value of \(h\). No claim is made for arbitrary Latin squares, noncyclic groups, two marks not sharing a row, or identification among different structures.

The group-theoretic orbit comparison uses all automorphisms fixing both singleton colours individually, not just translations, multiplications, or one selected subgroup of automorphisms.

## Proof
**1. Every point of \(H^2\) becomes a singleton.** Call a cell *isolated* when its refinement colour is unique. Any two isolated cells \(u,v\) make the unique intersection \(E_R[u]\cap E_C[v]\) isolated after at most one more refinement round: a cell in that intersection is the only cell whose row-neighbourhood contains the unique colour of \(u\) and whose column-neighbourhood contains the unique colour of \(v\). The same statement holds with any two *different* named relations \(E_R,E_C,E_S\), since any pair of corresponding Latin-square lines has a unique intersection.

Initially \((0,0)\) and \((0,g)\) are isolated. Their column and symbol lines isolate \((g,0)=E_C[(0,0)]\cap E_S[(0,g)]\). Suppose \((tg,0)\) is isolated. Taking its row line with the column line of \((0,g)\) isolates \((tg,g)\). Intersecting that cell's symbol line with the column line of \((0,0)\) isolates \(((t+1)g,0)\). Induction isolates \((tg,0)\) for all \(t\ge0\), hence every \((a,0)\) for \(a\in H\). Intersecting the symbol line of \((a,0)\) with the row line of \((0,0)\) isolates \((0,a)\). Intersecting the row line of \((a,0)\) with the column line of \((0,b)\) isolates \((a,b)\) for all \(a,b\in H\).

**2. The asserted partition is stable under all three counting operations.** Write \(\mathcal P\) for the displayed partition. Its pieces are disjoint and cover \(X\). For a fixed cell, any row, column, or symbol line has \(n\) cells. Each equation \(x=a\), \(y=b\), or \(x+y=c\) with a prescribed value in \(H\) has either one solution on such a line (if the equation is of a *different* type) or all or none (if it is the defining equation of that line). These one-solution intersections partition lines according to membership in \(H\); each residual count is \(n-h\) or \(n-2h\), independent of the cell chosen in its part.

For completeness, consider representative line counts. At a singleton \((a,b)\in H^2\), the row has precisely the \(h\) singleton cells \((a,b')\) with \(b'\in H\) and \(n-h\) cells of \(R_a\); columns and symbols have the analogous description with \(C_b\) and \(S_{a+b}\). At a cell of \(R_a\), its row again contains those \(h\) singletons and \(n-h\) cells of \(R_a\). Its column meets each \(R_{a'}\) once and each \(S_c\) once (\(a',c\in H\)), with \(n-2h\) remaining cells of \(Z\); its symbol line meets each \(R_{a'}\) and each \(C_b\) once, with the same remaining count. Exchanging rows and columns gives the counts for a cell of \(C_b\). At a cell of \(S_c\), its symbol line has \(h\) singleton cells summing to \(c\) and \(n-h\) cells of \(S_c\); its row meets each \(C_b\) and each \(S_{c'}\) once, and its column meets each \(R_a\) and each \(S_{c'}\) once, with \(n-2h\) cells of \(Z\) on either line. Finally, each row of a cell in \(Z\) meets every \(C_b\) and every \(S_c\) once, each column meets every \(R_a\) and \(S_c\) once, and each symbol line meets every \(R_a\) and \(C_b\) once; all three have \(n-2h\) cells of \(Z\). These formulas also cover the absent-part cases by omitting empty parts.

Thus \(\mathcal P\) is equitable simultaneously for all three named relations and refines the initial colouring. Every refinement colour is consequently a union of its parts. Conversely, by step 1 every \(P_{a,b}\) eventually becomes a singleton colour. One subsequent round distinguishes \(R_a\) via the row relation to \((a,0)\), \(C_b\) via the column relation to \((0,b)\), and \(S_c\) via the symbol relation to \((0,c)\). The remaining \(Z\) has no neighbour among those singleton cells in any of the three relations. Distinct parts therefore receive distinct stable colours. This proves the exact partition and, by counting its parts, the class-count and class-size formulas.

**3. Full automorphisms and orbit exactness.** A permutation preserving the separately named row and column equivalences must act as \((x,y)\mapsto(\alpha(x),\beta(y))\), with permutations \(\alpha,\beta\). Preserving the named symbol relation means that a permutation \(\gamma\) exists with \(\alpha(x)+\beta(y)=\gamma(x+y)\). Writing \(a=\alpha(0)\) and \(b=\beta(0)\), first set \(y=0\), then \(x=0\), to obtain \(\alpha(x)=a+u(x)\), \(\beta(y)=b+u(y)\), where \(u(x+y)=u(x)+u(y)\). Bijectivity implies \(u(x)=tx\) for a unit \(t\pmod n\). Fixing \((0,0)\) requires \(a=b=0\); fixing \((0,g)\) requires \(tg=g\). Since \(g\) has order \(h\), the complete pointwise stabilizer is exactly
\[
(x,y)\longmapsto(tx,ty),\quad \gcd(t,n)=1,\quad t\equiv1\pmod h.
\]
If \(k=1\), all stable classes are singleton, hence orbit exact. For \((n,h)=(4,2)\), the two permitted multipliers \(1,3\) fix the four \(H^2\) cells and act transitively on each of the six other two-point parts, giving orbit exactness.

If \(k\ge3\), then \((0,1)\) and \((0,2)\) lie in the same part \(R_0\), since \(H\) consists of multiples of \(k\). No permitted multiplier maps the first to the second: that would require \(t\equiv2\pmod n\), contradicting \(t\equiv1\pmod h\), since \(h\ge2\). If \(k=2\) and \(h\ge3\), similarly \((0,1)\) and \((0,3)\) lie in \(R_0\), but a multiplier mapping one to the other would satisfy both \(t\equiv3\pmod n\) and \(t\equiv1\pmod h\), which is impossible because \(h\nmid2\). The only remaining non-generator case is \(k=h=2\), already handled. This proves the exact if-and-only-if assertion.

## Verification
Three standalone Python 3 scripts using only the standard library accompany the finding. `verify/direct_refinement.py` constructs and stabilizes the relation-wise counting refinement independently for all \(231\) parameters \(2\le n\le22\), \(1\le g<n\), comparing whole partitions rather than merely class counts. `verify/equitability_and_orbits.py` directly checks every equitable neighbour-count vector and the complete modular-unit orbits for all \(190\) pairs \(2\le n\le20\). `verify/autotopism_independent.py` enumerates arbitrary row-column-symbol permutation triples for every cyclic addition table of order \(2\) through \(5\), and confirms they equal the derived affine description. The measured outputs are embedded. The all-order result rests on the proof, not a finite extrapolation.

## Relationship to prior work
Latin squares as orthogonal arrays and their autotopisms are classical; McKay, Meynert and Myrvold study isotopy and symmetry, and Stones, Vojtěchovský and Wanless classify possible autotopism cycle structures. Bailey's 1982 paper determines a sharp unmarked *unordered-pair orbit* property of Latin squares, a different action and criterion. Bailey, Cameron, Gavrilyuk and Goryainov classify certain equitable partitions of **the graph joining cells sharing any one of the three coordinates**; that merged-adjacency graph is not the separately labelled relational structure here, and their classification explicitly restricts the allowable quotient spectrum. Their work supplies relevant context rather than the claimed two-marked cyclic subgroup formula.

A previously established binary-vector addition-table theorem gives orbit recovery for arbitrary two marked cells over elementary abelian \(2\)-groups, with an analogous subgroup-size pattern. The cyclic result here is not implied by that special characteristic-two result: in cyclic groups the same-looking refinement classes generally **fail** to be automorphism orbits, with exactly the stated exceptional non-generator case. This distinction between local counting regularity and true symmetry is the motivation for the present comparison. Neither an earlier manuscript nor the inspected general primary sources has been shown to contain the precise all-order cyclic classification, but absence from a finite search is not proof of publication priority.

## Limitations
The result concerns one-dimensional counting refinement with exactly two distinctly coloured cells in the same row of a cyclic addition table and separately named row/column/symbol equivalences. The formulas do not apply unchanged if the three relations are merged into a simple graph or if arbitrary quasigroup tables replace addition. The theorem does not give optimal refinement-round counts or establish any broad graph-isomorphism complexity bound. Specialized literature on coherent configurations or Latin-square cell schemes may contain equivalent statements; independent review and exhaustive publication-priority verification are not asserted.

## References
1. D. S. Stones, P. Vojtěchovský, and I. M. Wanless, *Cycle structure of autotopisms of quasigroups and Latin squares*, arXiv:1509.05655v1, posted 2015-09-18. https://arxiv.org/abs/1509.05655
2. B. D. McKay, A. Meynert, and W. Myrvold, *Small Latin Squares, Quasigroups and Loops*. https://users.cecs.anu.edu.au/~bdm/papers/ls_final.pdf
3. R. A. Bailey, *Latin squares with highly transitive automorphism groups*, Journal of the Australian Mathematical Society Series A 33 (1982), 18–22. https://doi.org/10.1017/S1446788700017560
4. R. A. Bailey, P. J. Cameron, A. L. Gavrilyuk, and S. V. Goryainov, *Equitable partitions of Latin-square graphs*, arXiv:1802.01001v1, 2018. https://arxiv.org/abs/1802.01001
