# Complete census of minimum singleton three-rainbow domination on cycle prisms

## Finding

Let \(G_n=C_n\square K_2\) be the simple labeled prism with \(n\ge3\) rungs. A singleton three-rainbow dominating function assigns each vertex a value from \(\{0,1,2,3\}\); every vertex labeled \(0\) must have neighbors carrying all three distinct positive labels. Its weight is the number of nonzero labels. Define \(a_{n,j}\) as the number of these functions of weight \(j\), with the three positive labels **named** and all vertices **distinguished**.

For every integer \(n\ge3\), \(a_{n,j}=0\) for \(j<n\), and the first three candidate weight coefficients are exactly

\[
a_{n,n}=\begin{cases}12,&6\mid n,\\0,&6\nmid n;\end{cases}
\]

\[
a_{n,n+1}=\begin{cases}12n,&n\text{ odd},\\36n,&6\mid n,\\0,&\text{otherwise};\end{cases}
\]

\[
a_{n,n+2}=\begin{cases}
36n(2n-3),&n\text{ odd},\\
108n(n-2),&n\equiv0\pmod6,\\
18n(3n-5),&n\equiv2\pmod6,\\
18n(3n-1),&n\equiv4\pmod6.
\end{cases}
\]

In particular, **the exact number of minimum functions** is

\[
\#\operatorname{Min}(G_n)=
\begin{cases}
12,&n\equiv0\pmod6,\\
12n,&n\text{ odd},\\
18n(3n-5),&n\equiv2\pmod6,\\
18n(3n-1),&n\equiv4\pmod6.
\end{cases}
\]

The minimum weights themselves are \(n\), \(n+1\), and \(n+2\), respectively, agreeing with the previously established minimum-weight formula. The new assertion is an exact all-order **multiplicity classification**, including the complete first three coefficients, not merely the minimum weight.

## Assumptions and scope

The graph \(G_n\) has vertices \((i,r)\) for \(i\in\mathbb Z/n\mathbb Z\), \(r\in\{0,1\}\), with edges between \((i,0)\) and \((i,1)\), and between \((i,r)\) and \((i\pm1,r)\). For \(n=3\) the two cyclic neighbors are distinct, so every vertex has degree three. Rungs, rows, cyclic origins, and colors are not identified under automorphisms. The singleton model is distinct from classical rainbow domination, where one vertex may carry multiple colors.

The coefficients count assignments of a fixed weight, not automorphism orbits. All statements concern integer \(n\ge3\); no infinite-length limiting claim is made.

## Proof

**1. Uncolored-rung structure.** Write \(U=\{v:f(v)=0\}\). Since every uncolored vertex needs three differently colored neighbors and \(G_n\) is cubic, \(U\) is independent. In particular, every rung contains at most one member of \(U\), so \(|U|\le n\), proving the zero coefficients below weight \(n\).

If \(|U|=n-h\), exactly \(h\) rungs are entirely colored, and each other rung contains exactly one uncolored vertex. Call the entirely colored rungs *holes*. On each maximal consecutive run of non-hole rungs, the row occupied by \(U\) alternates: two horizontally adjacent uncolored vertices are forbidden. Every valid assignment with \(h\le2\) arises in this way.

**2. A two-terminal color kernel.** Consider a run of \(\ell\ge1\) consecutive rungs with exactly one uncolored vertex per rung, alternating rows. Let \(c_1,\ldots,c_\ell\) be the positive colors on their rung-mates. Let \(x\) and \(y\) be the colors on the two boundary-hole vertices adjacent to the uncolored vertices at the ends. The local conditions require the three labels around each uncolored vertex to be distinct. For prescribed \(x=a\) and \(y=b\), the number of valid internal color sequences is the entry \(R_\ell(a,b)\) of the matrix

\[
R_\ell=\begin{cases}2I_3,&\ell\equiv2\pmod3,\\J_3-I_3,&\ell\not\equiv2\pmod3,\end{cases}
\]

where \(I_3\) is the identity and \(J_3\) the all-one matrix. Indeed, for \(\ell=1\), the three labels \(x,c_1,y\) must all differ, giving \(J_3-I_3\). For \(\ell=2\), both boundary labels must be the color absent from \(\{c_1,c_2\}\), giving \(2I_3\). For \(\ell\ge3\), consecutive triples of companion colors are permutations of \(\{1,2,3\}\), hence \(c_{j+3}=c_j\) whenever both indices are present. The left boundary color is the third color of \(c_1,c_2\); the right boundary color is the third color of \(c_{\ell-1},c_\ell\). These boundary colors are equal exactly when \(\ell\equiv2\pmod3\). In that congruence class each prescribed equal pair has exactly two internal sequences and unequal pairs have none; otherwise each prescribed unequal pair has exactly one sequence and equal pairs have none. This proves the kernel in all lengths.

Every row sum and every column sum of \(R_\ell\) is \(2\), and the sum of all nine entries is \(6\). We will also use

\[
\operatorname{tr}(R_pR_q)=
\begin{cases}12,&p\equiv q\equiv2\pmod3,\\
0,&\text{exactly one of }p,q\equiv2\pmod3,\\
6,&p,q\not\equiv2\pmod3.
\end{cases}
\]

This follows directly from \(J_3^2=3J_3\).

**3. No holes (weight \(n\)).** All uncolored rows must alternate cyclically. This requires \(n\) even and gives two choices. The companion color sequence must satisfy that every consecutive triple consists of three different colors, hence has period three and requires \(3\mid n\). When \(6\mid n\), each of the two uncolored configurations has six color sequences, yielding exactly \(12\) functions. In every other case there are none.

**4. One hole (weight \(n+1\)).** Choose its position in \(n\) ways. The remaining \(n-1\) rungs form one run, with two alternating-row choices. For odd \(n\), the uncolored vertices at the two ends occupy opposite rows. They constrain different vertices in the same hole, so the kernel yields \(\sum_{a,b}R_{n-1}(a,b)=6\) colorings per row choice, hence \(12n\) assignments.

For even \(n\), the two ends occupy the same row and constrain the same hole vertex. Their prescribed colors must match, and the other hole vertex may receive any of three colors. Thus the number per row choice is \(3\operatorname{tr}(R_{n-1})\), equal to \(18\) if \(n\equiv0\pmod6\) and \(0\) otherwise. Multiplying by \(2n\) choices proves the second coefficient.

**5. Two adjacent holes (part of weight \(n+2\)).** There are \(n\) unordered adjacent pairs. The remaining rungs form one run of length \(n-2\), with two alternating-row choices. Its six internal colorings determine one vertex color at each hole, while the other vertex in each hole is unrestricted among three colors. Every adjacent pair therefore contributes \(2\cdot6\cdot3^2=108\) functions. This remains valid for \(n=3\), where the run has one rung.

**6. Two nonadjacent holes.** Fix ordered hole positions \(0\) and \(d\), with \(2\le d\le n-2\). The two nonempty runs have lengths \(p=d-1\) and \(q=n-d-1\). Each run has two row orientations, for four choices in total. At a hole, the runs may constrain the same colored vertex or two different colored vertices. The same/different relation at the second hole agrees with that at the first precisely when \(n\) is even: crossing the two runs toggles it \(n-4\) times modulo two.

For odd \(n\), each of the four row-orientation choices has one hole with a shared constrained vertex and the other with two distinct constrained vertices. Forcing equality of the two endpoint colors at only one hole leaves \(3\cdot2\cdot2=12\) pairs of run colorings, since each kernel has constant row and column sums \(2\). The other vertex of the shared hole is freely colored in three ways. Thus each nonadjacent unordered hole pair contributes \(4\cdot12\cdot3=144\). Combining \(n\) adjacent pairs with \(\binom n2-n\) nonadjacent pairs gives

\[
a_{n,n+2}=108n+144\left(\binom n2-n\right)=36n(2n-3),\qquad n\text{ odd}.
\]

For even \(n\), two orientations constrain the same vertex at **both** holes, and two orientations constrain distinct vertices at both. In the shared/shared case the two unconstrained hole vertices contribute \(3^2\), and the matching of endpoint-color pairs between runs contributes \(\operatorname{tr}(R_pR_q)\). In the distinct/distinct case the runs contribute \(6^2\) assignments. Therefore each nonadjacent hole pair with cyclic separation \(d\) contributes

\[
B_n(d)=2\left(9\operatorname{tr}(R_{d-1}R_{n-d-1})+36\right).
\]

In particular \(B_n(d)\) equals \(288\), \(72\), or \(180\), respectively, when both run lengths are congruent to two modulo three, exactly one is, or neither is. Each unordered pair is counted twice in the directed-distance sum, so

\[
a_{n,n+2}=\frac n2\left(216+\sum_{d=2}^{n-2}B_n(d)\right),\qquad n\text{ even}.
\]

For \(n=6s\), the three residue classes of \(d\) modulo three each occur \(2s-1\) times in the summation. The corresponding \(B_n(d)\) values are \(288,180,180\). For \(n=6s+2\), the residue class with \(B_n(d)=180\) occurs \(2s-1\) times, and the two classes with \(B_n(d)=72\) occur \(2s\) times each. For \(n=6s+4\), the class with \(B_n(d)=180\) occurs \(2s+1\) times, and each class with \(B_n(d)=72\) occurs \(2s\) times. Substitution yields, respectively,

\[
108n(n-2),\qquad18n(3n-5),\qquad18n(3n-1).
\]

This calculation includes the smallest admissible even circumference \(n=4\). No other two-hole configurations exist, completing all coefficient formulas.

**7. Minimum-weight census.** Weight below \(n\) is impossible by Step 1. Steps 3–6 show the first positive coefficient at weight \(n\) for \(6\mid n\), weight \(n+1\) for odd \(n\), and weight \(n+2\) for even \(n\not\equiv0\pmod6\). Choosing that coefficient proves the displayed complete census of minimum functions without assuming the previously published minimum-weight theorem. \(\square\)

## Verification

The standalone `verify.py` uses direct graph-neighborhood checks to enumerate **all** four-symbol vertex assignments for \(n=3,4,5\) and compares the three predicted coefficients. A second, independent constraint-graph counting method enumerates every allowed uncolored support for \(3\le n\le24\), builds a triangle of pairwise color inequalities at each uncolored vertex, and counts all positive color assignments using exact backtracking. It also directly enumerates the two-terminal kernel for run lengths one through eight. The saved output in `verify_output.txt` ends with `VERIFY_OK`.

The computations are finite corroboration, not a proof of the unrestricted statement. The unrestricted claim is established by the arguments in the preceding section.

## Relationship to prior work

Lange's arXiv preprint [1], first made public on 2026-10-01 (arXiv version 1), studies **singleton** rainbow domination in regular graphs. Its Theorem 19 gives the **minimum weight** of such functions on the same prism family, distinguished by circumference modulo six. Theorem 7 characterizes cubic equality at half the vertex order, and the appendices supply constructions and numerical bounds. None of these statements gives the number of functions attaining the minimum, the weight-\(n+1\) count, or the complete weight-\(n+2\) count. The present proof reconstructs those coefficients independently; it is not an alteration of the known minimum-weight theorem.

Žerovnik [2] studies singleton three-rainbow domination of cylindrical graphs, including the two-row cylinder, and derives bounds and constructive examples. The accessible material concerns optimal weight, rather than a census of named-color labelings; the complete publisher PDF was inaccessible during the literature inspection. Allagan and collaborators [3] enumerate **ordinary minimum dominating vertex sets** of the same prism family; those have neither a three-color requirement nor singleton rainbow weight, so their modulo-four dominion formulas cannot imply this modulo-six census.

A searched public research record on Roman \(\{3\}\)-domination of \(K_n\square K_2\) concerns a different graph (complete-prism layers rather than cycle-prism layers) and a different domination invariant. Related upper-domination and convex-set enumerations likewise do not cover this claim.

## Limitations

Only the coefficients at weights \(n,n+1,n+2\) are computed; the theorem makes no assertion about the full domination polynomial at higher weights. Labels are named, not quotiented by symmetry. Literature search and self-review are not an independent audit or a proof that no earlier equivalent formula exists. In particular, a complete review of all possibly relevant inaccessible journal texts remains a bibliographic priority risk. The direct enumeration checks stop at finite sizes and should not be interpreted as an infinite certificate.

## References

[1] Piotr Lange, *Complexity, Bounds, and Exact Algorithms for Rainbow \(k\)-Domination in Regular Graphs*, arXiv:2610.06906v1, posted 2026-10-01. See §§2, 3, 5.3, and Appendix B. https://arxiv.org/abs/2610.06906

[2] Janez Žerovnik, *On Singleton 3-Rainbow Domination of Cylindrical Graphs*, *Mathematics* 14(16), 2917 (2026), published 2026-08-12. DOI:10.3390/math14162917. https://doi.org/10.3390/math14162917

[3] Julian Allagan et al., *Exact Dominion of the Prism Graph: Enumeration by Congruence Class via Cyclic Words*, *International Journal of Mathematics and Mathematical Sciences* (2026), first published 2026-06-12. DOI:10.1155/ijmm/1411005. https://doi.org/10.1155/ijmm/1411005
