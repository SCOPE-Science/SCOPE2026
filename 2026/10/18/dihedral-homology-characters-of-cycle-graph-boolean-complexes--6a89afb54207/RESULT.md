# Dihedral homology characters of cycle-graph Boolean complexes

## Finding
For every integer \(n\ge3\), the natural dihedral action on the top homology of the Boolean complex of the cycle \(C_n\) has the following complete character. Set \(D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\), with \(r(i)=i+1\) and \(s(i)=-i\) on \(\mathbb Z/n\mathbb Z\). Let \(L_0=2\), \(L_1=1\), and \(L_{t+2}=L_{t+1}+L_t\) be the Lucas numbers. The only nonzero reduced integral homology group of \(\mathcal B(C_n)\) is free of rank \(L_n-2\) in degree \(n-1\).

Writing \(\chi_n\) for the character of the rationalized top homology, every rotation satisfies
\[
\chi_n(r^j)=(-1)^{n+\gcd(n,j)}\bigl(L_{\gcd(n,j)}-2\bigr),\qquad 0\le j<n,
\]
where \(\gcd(n,0)=n\). For reflections, define the Fibonacci numbers by \(F_{-1}=1\), \(F_0=0\), \(F_1=1\), and \(F_{t+2}=F_{t+1}+F_t\) for \(t\ge1\). If \(n=2k+1\) is odd, then
\[
\chi_n(r^j s)=(-1)^{k+1}F_{k-1}.
\]
If \(n=2k\) is even, then
\[
\chi_n(r^j s)=\begin{cases}(-1)^{k+1}F_k,&j\text{ even},\\(-1)^{k-2}F_{k-3},&j\text{ odd}.\end{cases}
\]
The sign conventions distinguish axes through opposite vertices (even \(j\)) from axes through opposite edges (odd \(j\)) in the even case.

## Assumptions and scope
Let \(C_n\) be the simple undirected cycle with vertices \(\mathbb Z/n\mathbb Z\), including the ordinary triangle for \(n=3\). The **Boolean complex** \(\mathcal B(C_n)\) is the regular Boolean cell complex whose cells of dimension \(k-1\) are equivalence classes of injective words of length \(k\) in cycle vertices, where neighboring letters may be interchanged precisely if they are not adjacent in \(C_n\). Faces are classes of subwords. Equivalently, a cell is a pair \((S,\omega)\), where \(\varnothing\ne S\subseteq V(C_n)\) and \(\omega\) is an acyclic orientation of the induced graph \(C_n[S]\). Its topological realization, rather than an abstract simplex on the vertices, is understood throughout. The dihedral group acts by relabeling vertices and hence cells.

Integral homology is used for the statement of freeness and degree concentration. The character is taken after tensoring the top integral homology with \(\mathbb Q\). This is not a classification of the integral representation up to lattice isomorphism; a rational character alone does not determine the integral module.

## Proof
**1. Homology concentration.** Ragnarsson and Tenner's Boolean-complex homotopy theorem gives \(\mathcal B(G)\simeq\bigvee^{\beta(G)}S^{|V(G)|-1}\) for every finite simple graph. Their affine type-A cycle entry has \(\beta(C_n)=L_n-2\). Thus \(\widetilde H_q(\mathcal B(C_n);\mathbb Z)=0\) for \(q\ne n-1\), and \(\widetilde H_{n-1}\cong\mathbb Z^{L_n-2}\) for every \(n\ge3\). This theorem is **prior literature**, not part of the new assertion.

**2. Signed fixed-cell trace.** Orient the cell \((S,\omega)\) by the increasing order on \(S\). A graph automorphism \(g\) sends that oriented cell to the relabeled cell with coefficient \(\operatorname{sgn}(g|_S)\). A fixed basis cell is exactly a \(g\)-stable pair \((S,\omega)\). With \(a_g(S)\) denoting the number of \(g\)-fixed acyclic orientations of \(C_n[S]\), the augmented cellular Lefschetz formula gives
\[
\chi_n(g)=(-1)^n\sum_{\substack{S\subseteq V(C_n)\\gS=S}}(-1)^{|S|}\operatorname{sgn}(g|_S)\,a_g(S),
\]
where the empty set is included with \(a_g(\varnothing)=1\) and sign one. Indeed, the reduced alternating chain trace equals \((-1)^{n-1}\chi_n(g)\), while a nonempty set of size \(k\) indexes a \((k-1)\)-cell, so that the empty-cell contribution is \(-1\). This also fixes all sign and normalization conventions.

**3. Rotations.** For \(g=r^j\) put \(d=\gcd(n,j)\) and \(h=n/d\). A fixed vertex set \(S\) is the inverse image of some \(T\subseteq\mathbb Z/d\mathbb Z\); it has \(h|T|\) vertices. Every selected orbit is an \(h\)-cycle of the permutation on \(S\). Consequently
\[
(-1)^{|S|}\operatorname{sgn}(g|_S)=(-1)^{|T|}.
\]
If \(T\ne\mathbb Z/d\mathbb Z\), the edges of the selected graph project to a forest; each selected quotient edge has exactly one independently chosen invariant direction. Thus \(a_g(S)=2^{e(T)}\), where \(e(T)\) counts adjacency edges in the cyclic quotient. If \(T\) is full, there are \(2^d\) invariant directions, with exactly the two consistently directed cycles forbidden, giving \(a_g(S)=2^d-2\). The same interpretation is valid when \(d=1\) or \(d=2\) by treating the cyclic quotient as a loop or a double edge for the full set; proper subsets are handled directly.

We therefore obtain \(\chi_n(r^j)=(-1)^n Z_d\), where
\[
Z_d=\sum_{T\subsetneq[d]}(-1)^{|T|}2^{e(T)}+(-1)^d(2^d-2).
\]
For \(d\ge3\), the acyclic-orientation identity \(a(H)=(-1)^{|V(H)|}P_H(-1)\), with \(P_H(q)\) the chromatic polynomial, transforms this into \(Z_d=\sum_{T\subseteq[d]}P_{C_d[T]}(-1)\). For a positive integer \(q\), the polynomial \(\sum_T P_{C_d[T]}(q)\) counts cyclic words over \(q\) ordinary colors and one vacant symbol, where only adjacent equal ordinary colors are forbidden. Its transfer matrix has eigenvalues \(-1\) (multiplicity \(q-1\)) and the two roots of \(\lambda^2-q\lambda-1=0\). Hence polynomial continuation to \(q=-1\) gives
\[
Z_d=(-1)^d\bigl(L_d-2\bigr).
\]
For \(d=1\) or \(2\) the direct fixed-orientation sum gives respectively \(Z_1=1\) and \(Z_2=1\), which agree with \((-1)^d(L_d-2)\). Substitution establishes the rotation formula for all \(j\), including the identity.

**4. Reflections.** Write \(g=r^j s\). A reflected edge whose endpoints are interchanged cannot both be selected in any \(g\)-fixed oriented cell, because an orientation of that edge would have to equal its reverse. Remove the corresponding forbidden vertex orbit(s). The remaining reflection orbits, linked by adjacency of the cycle, form a quotient path: it has \(k\) vertices when \(n=2k+1\); it has \(k+1\) vertices when \(n=2k\) and \(j\) even (a vertex-axis reflection); it has \(k-2\) vertices when \(n=2k\) and \(j\) odd (an edge-axis reflection). These are all nonnegative for \(n\ge3\).

Each chosen orbit contributes exactly \(-1\) to \((-1)^{|S|}\operatorname{sgn}(g|_S)\), whether it consists of one fixed vertex or of a transposed vertex pair. A chosen quotient path edge contributes two possible invariant orientations, independently of other edges, and no directed cycle occurs. Thus the fixed-cell sum is the path polynomial
\[
Q_\ell=\sum_{T\subseteq V(P_\ell)}(-1)^{|T|}2^{e(P_\ell[T])}.
\]
Splitting according to inclusion of the final path vertex gives \(Q_0=1\), \(Q_1=0\) and \(Q_\ell=Q_{\ell-2}-Q_{\ell-1}\) for \(\ell\ge2\). Induction proves \(Q_\ell=(-1)^\ell F_{\ell-1}\), interpreting \(F_{-1}=1\). Applying the prefactor \((-1)^n\) from Step 2 to \(Q_k\), \(Q_{k+1}\), or \(Q_{k-2}\) gives exactly the stated reflection formulas.

Since rotations and reflections exhaust \(D_n\), this completes the character determination. A rational representation of a finite group is determined up to rational isomorphism by its character.

## Verification
The included `verify_orbit_counts.py` independently enumerates every invariant vertex subset and every invariant acyclic orientation, retaining cellular orientation signs, for all dihedral elements with \(3\le n\le11\). It agrees with each displayed formula. The included `verify_cellular_chains.py` constructs signed cellular boundaries, computes exact rational ranks and restricts signed dihedral matrices to the top-cycle kernel for \(3\le n\le6\), checking every group element. Both scripts run with Python 3; the chain script also requires SymPy. Run `python verify_orbit_counts.py` and `python verify_cellular_chains.py` in the directory containing those extracted files. The second method does not evaluate the cycle-transfer formula. The finite checks corroborate, but do not substitute for, Steps 1–4.

## Relationship to prior work
Ragnarsson and Tenner (arXiv:0806.0906, Theorem 3.4 and affine-type table) proved the wedge-of-spheres homotopy type and cycle Lucas number. Their later work (arXiv:1005.4411, Sections 2–3) constructs homology bases over \(\mathbb F_2\), with no signed integral/rational dihedral character formula established in the inspected sections. Jonsson and Welker (arXiv:0712.2143, Theorems 1.2–1.4 and Lemma 3.4) establish shellability and acyclic-orientation indexing for commutation-class word complexes; these statements alone do not determine the character under cycle rotations/reflections. Reiner–Webb's symmetric-group modules for unrestricted injective-word complexes concern a different commutation relation and do not specialize to the cycle case. The new result is specifically the **complete dihedral homology character**, not the already-known Betti numbers or homotopy type.

## Limitations
The result classifies the rational dihedral representation by its character and does not classify integral \(\mathbb Z[D_n]\)-lattices or equivariant homotopy types. It applies to the ordinary simple cycle \(n\ge3\), not other Coxeter graphs. Exhaustive numerical verification stops at \(n=11\) for orbit counts and \(n=6\) for full chains; the all-parameter assertion rests on the proof. The literature comparison does not establish absolute priority against inaccessible or unindexed sources.

## References
Ragnarsson, K., and Tenner, B. E., *Homotopy Type of the Boolean Complex of a Coxeter System*, arXiv:0806.0906 (first public 2008-06-05), Theorem 3.4 and Corollary 3.6, https://arxiv.org/pdf/0806.0906.

Ragnarsson, K., and Tenner, B. E., *Homology of the Boolean Complex*, arXiv:1005.4411 (first public 2010-05-24); Journal of Algebraic Combinatorics 34 (2011), 617–639, https://doi.org/10.1007/s10801-011-0285-5.

Jonsson, J., and Welker, V., *Complexes of Injective Words and Their Commutation Classes*, arXiv:0712.2143 (first public 2007-12-13), https://arxiv.org/pdf/0712.2143.
