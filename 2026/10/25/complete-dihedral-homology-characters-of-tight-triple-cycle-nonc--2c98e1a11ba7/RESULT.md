# Complete dihedral homology characters of tight triple-cycle noncover complexes

## Finding
For each integer \(n\ge 6\), let \(\mathcal H_n\) be the 3-uniform hypergraph on \(\mathbb Z/n\mathbb Z\) with hyperedges \(\{i,i+1,i+2\}\), and let \(K_n=\operatorname{NC}(\mathcal H_n)\) be the complex of subsets missing at least one hyperedge. The dihedral group \(D_n=\langle r,s:r^n=s^2=1,\ srs=r^{-1}\rangle\) acts by \(r(i)=i+1\), \(s(i)=-i\). The only nonzero reduced rational homology of \(K_n\) is in degree \(d_n\), where, writing \(n=4k+t\) with \(0\le t\le3\),
\[
(d_n,\dim\widetilde H_{d_n}(K_n;\mathbb Q))=
\begin{cases}(2k-2,3),&t=0,\\(2k-1,1),&t=1,2,3.\end{cases}
\]
The **new assertion** is the entire dihedral character \(\chi_n\) of that homology representation:
\[
\begin{array}{c|c|c}
&\chi_n(r^j)&\chi_n(sr^j)\\\hline
 t=0&3\ \text{if }4\mid j,\text{ otherwise }-1&(-1)^{k+1+j}\\
 t=1,2,3&1&(-1)^k
\end{array}
\qquad (0\le j<n).
\]
For \(t=0\), this is the direct sum of the inflated standard two-dimensional rational representation of \(D_4\) and a line on which \(r\) acts as \(-1\) and \(s\) as \((-1)^{k+1}\). For \(t=1,2,3\), it is the line with \(r=1\), \(s=(-1)^k\). Thus the full-group invariant space has dimension one exactly when \(n\equiv1,2,3\pmod8\), and dimension zero otherwise (always with \(n\ge6\)).

Equivalently, \(K_n\) is the ordinary 3-cut complex of the complement of the \(n\)-cycle, using the cut-complex convention of facets complementary to disconnected induced triples. Neither the nonequivariant homotopy classification nor the homology ranks are claimed as new.

## Assumptions and scope
All homology in the character theorem uses rational coefficients and is reduced. The dihedral action is the simplicial action on the actual vertex set \(\mathbb Z/n\mathbb Z\), not an action on a chosen nonequivariant wedge decomposition. The integer \(n\) ranges over all \(n\ge6\). When \(n\ge6\), an induced triple in the complement graph \(\overline{C_n}\) is disconnected precisely when it is the two neighbors and their common center in \(C_n\), hence the cut and noncover descriptions agree. The homology concentration and ranks are those already proved by Kim and Kim [1, Theorem 3.4] at hyperedge length three and deleted-edge parameter zero.

## Proof
**(1) Homology concentration.** Theorem 3.4 of [1] proves \(K_n\simeq\bigvee^3 S^{2k-2}\) for \(n=4k\), and \(K_n\simeq S^{2k-1}\) for \(n=4k+t\), \(t=1,2,3\). For \(n\ge6\), all these degrees are positive. Consequently a single homological character can be recovered from its reduced Lefschetz trace.

**(2) Equivariant Alexander duality and a fixed-orbit sum.** Let \(J_n=\operatorname{Ind}(\mathcal H_n)\) be the complex of vertex subsets that contain no hyperedge. Combinatorial Alexander duality is natural up to the orientation line of the ambient \(n\)-vertex simplex: as \(D_n\)-modules, \(\widetilde H_{d_n}(K_n;\mathbb Q)\cong\operatorname{sgn}_{\mathbb Z/n}\otimes\widetilde H^{n-d_n-3}(J_n;\mathbb Q)\). Since every group element has finite order, cohomology and homology have the same character. Let \(g\in D_n\), let \(c(g)\) be the number of cycles in its permutation of the vertices, and set
\[
F(g)=\sum_{\substack{S\in J_n\\gS=S}}(-1)^{b_g(S)},
\]
where \(b_g(S)\) is the number of vertex-permutation cycles of \(g\) contained in \(S\). For an invariant face, the product of its face-parity sign and its orientation sign is \((-1)^{b_g(S)}\). The signed reduced simplicial Lefschetz sum for \(J_n\), including its empty face, is therefore \(-F(g)\). The permutation orientation sign on all vertices is \((-1)^{n-c(g)}\). Using concentration in complementary dimension yields the exact identity
\[
\boxed{\chi_n(g)=(-1)^{c(g)+d_n}F(g).} \tag{1}
\]
This also fixes the empty-simplex and Alexander-duality sign conventions; no finite computation is being extrapolated here.

**(3) Rotations.** For \(g=r^j\), put \(h=\gcd(n,j)\) (with \(\gcd(n,0)=n\)). Its orbits consist of congruence classes modulo \(h\). An invariant independent set is therefore a binary cyclic word of length \(h\) without three cyclically consecutive ones. Each selected orbit contributes weight \(-1\) to \(F(g)\). The finite transfer matrix, indexed in order by consecutive-bit states \(00,01,10,11\), is
\[
M=\begin{pmatrix}1&-1&0&0\\0&0&1&-1\\1&-1&0&0\\0&0&1&0\end{pmatrix}.
\]
The entry for the transition \((a,b)\to(b,c)\) is \((-1)^c\) unless \(a=b=c=1\), in which case it is zero. This cyclic trace formula remains valid for \(h=1,2\), where the circular word wraps around itself. Direct determinant expansion gives \(\det(xI-M)=x(x-1)(x^2+1)\). Hence for every positive integer \(h\),
\[
F(r^j)=\operatorname{tr}(M^h)=1+i^h+(-i)^h=
\begin{cases}3&h\equiv0\pmod4,\\-1&h\equiv2\pmod4,\\1&h\text{ odd}.\end{cases}
\]
Since \(c(r^j)=h\), insertion in (1) immediately gives the claimed rotation character in all four residue classes of \(n\).

**(4) Reflections.** Write \(g_a(i)=a-i\). A reflection-invariant independent set is determined by orbit bits along a half-cycle. For \(n=2m+1\), the orbits are one vertex and \(m\) pairs, and its successive orbit bits form a path of length \(m+1\). For \(n=2m\), a reflection whose \(a\) is even fixes two vertices, with orbit-bit path of length \(m+1\); if \(a\) is odd it fixes no vertices, with orbit-bit path length \(m\). In each case the forbidden cyclic \(111\) runs translate *exactly* to: no three consecutive selected orbit bits, and neither endpoint pair may be \(11\). There are no omitted endpoint constraints: reflecting an endpoint bit creates the repeated pair that excludes precisely \(11\) at that end.

Let \(T_L\) be the alternating sum of binary words of length \(L\ge2\) satisfying those conditions, weighted by \((-1)^{\#1}\). With
\[
u=(1,-1,-1,0),\qquad v=(1,1,1,0)^{\mathsf T},
\]
we have \(T_L=uM^{L-2}v\). Direct multiplication yields \(T_2=-1,T_3=-1,T_4=1,T_5=1\); the characteristic identity \(M^4-M^3+M^2-M=0\) gives the recurrence \(T_{L+4}-T_{L+3}+T_{L+2}-T_{L+1}=0\) for every \(L\ge2\). These initial values and the recurrence yield
\[
\boxed{T_L=(-1)^{\lfloor L/2\rfloor}\quad\text{for all }L\ge2.}\tag{2}
\]
It follows that \(F(g_a)=T_{m+1}\) for odd \(n=2m+1\); for even \(n=2m\), it is \(T_{m+1}\) for even \(a\) and \(T_m\) for odd \(a\). The corresponding cycle counts are \(m+1,m+1,m\), respectively. Combining these counts, (1), (2), and the stated dimension \(d_n\) yields the reflection character displayed in the finding. Because \(g_a=sr^{-a}\), and \(a\) and \(-a\) have the same parity, the formula for \(sr^j\) follows.

**(5) Module identification and invariants.** When \(4\mid n\), the two-dimensional rational plane with \(r\mapsto\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\), \(s\mapsto\begin{psmallmatrix}1&0\\0&-1\end{psmallmatrix}\) has rotation trace \(2\cos(\pi j/2)\) and reflection trace zero. Adding the line defined in the finding reproduces all character values; rational finite-group representations are determined by their characters. For other \(n\), the specified line reproduces every value. Averaging the character over all \(2n\) dihedral elements gives the stated invariant dimensions. This completes the proof.

## Verification
Run `python3 verify_tight_cycle_dihedral.py` using the accompanying standalone standard-library checker. The checker directly computes signed fixed-simplex traces of the **original noncover complex** for all rotations and reflections at each \(6\le n\le12\) (126 group elements); independently computes alternating fixed-orbit sums of its Alexander-dual independence complex for \(6\le n\le14\) (180 group elements); and checks the exact transfer expressions for 100 exponents and path lengths. These finite tests corroborate, but do not replace, the all-integer algebraic proof given above.

## Relationship to prior work
Kim and Kim [1] proved the full nonequivariant homotopy type of these tight-cycle noncover complexes; that is used, not rediscovered. The original cut-complex paper [2] and its sequel [3] develop cut-complex homotopy and equivariant methods for cycles, paths and other graph families. Their \(\Delta_3(C_n)\) concerns the cut complex of a cycle itself, whereas here the graph is \(\overline{C_n}\), with different disconnected triple facets and different homology dimension. Neither examined article states this dihedral character. Cyclic representations of three-cut complexes of *powers* of cycles concern a different graph and do not imply a character on the complement cycle's three-cut complex. The present contribution is the explicit full \(D_n\)-module, not the already known homotopy ranks.

## Limitations
The result is rational-equivariant, not an integral lattice classification or equivariant homotopy decomposition. It assumes a tight length-three cycle and \(n\ge6\), not arbitrary uniform length or general hypergraphs. While all displayed trace formulas follow exactly, full mathematical originality cannot be guaranteed against unindexed or inaccessible research; independent audit has not been conducted. The stated invariants concern the rational homology representation, not the homology of a topological quotient without further hypotheses.

## References
[1] Jinha Kim and Minki Kim, *Domination numbers and noncover complexes of hypergraphs*, arXiv:2101.01850v1 (public 2021-01-06), particularly Theorem 3.4 and Section 3.2. https://arxiv.org/pdf/2101.01850

[2] Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Rowan Rowlands, Sheila Sundaram and Lei Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675v2, Sections 3, 6, 7. https://arxiv.org/pdf/2304.13675

[3] Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Sheila Sundaram and Lei Xue, *Topology of Cut Complexes II*, arXiv:2407.08158v1, Section 6.2 (direct paths/cycles, not complements). https://arxiv.org/pdf/2407.08158
