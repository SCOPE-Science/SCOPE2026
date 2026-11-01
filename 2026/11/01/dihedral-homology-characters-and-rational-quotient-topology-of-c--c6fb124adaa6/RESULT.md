# Dihedral homology characters and rational quotient topology of cycle two-independence complexes

## Finding
For every integer \(n\ge4\), the natural action of the dihedral group \(D_n\) on the two-independence complex \(X_n=\operatorname{Ind}_2(C_n)\) has the complete rational homology character below. Let the vertices be \(\mathbb Z/n\mathbb Z\), let \(r(i)=i+1\), \(s(i)=-i\), and put \(\chi_n(g)=\operatorname{tr}(g\mid\widetilde H_{d_n}(X_n;\mathbb Q))\).

The homology concentration degree is the **previously known** quantity
\[
d_n=\begin{cases}
2k-1,&n=4k\text{ or }4k+1,\\
2k,&n=4k+2,\\
2k+1,&n=4k+3.
\end{cases}
\]
For every integer \(a\), the new complete character is
\[
\begin{array}{c|c|c}
n&\chi_n(r^a)&\chi_n(r^a s)\\\hline
4k&1+2\cos(\pi a/2)&(-1)^k\\
\text{odd }n&1&(-1)^{\lfloor(n+1)/4\rfloor}\\
4k+2&(-1)^a&(-1)^{k+a}
\end{array}
\]
Consequently, the rational homology of the full dihedral quotient \(|X_n|/D_n\) is one-dimensional in degree \(d_n\) exactly when \(n\equiv0,1,7\pmod8\), and is reduced-rationally acyclic otherwise. The rotation quotient \(|X_n|/\langle r\rangle\) has a one-dimensional degree-\(d_n\) class exactly when \(n\not\equiv2\pmod4\); otherwise it is reduced-rationally acyclic.

## Assumptions and scope
The complex \(X_n\) is on the vertices of the simple undirected cycle \(C_n\), with faces all subsets whose induced connected components have at most two vertices. Equivalently, a cyclic binary indicator word has no three consecutive ones. All results hold for \(n\ge4\), including the small boundary case \(n=4\). The group acts simplicially by relabeling vertices. The assertions about quotients are over \(\mathbb Q\), not integral homotopy or contractibility.

## Proof
**Previously established homology concentration.** Theorem 4.6 of Deshpande and Singh (arXiv:2001.05448, originally publicly available 2020-01-15) gives \(X_{4k}\simeq\bigvee^3 S^{2k-1}\), \(X_{4k+1}\simeq S^{2k-1}\), \(X_{4k+2}\simeq S^{2k}\), and \(X_{4k+3}\simeq S^{2k+1}\). In particular there is exactly one nonzero reduced rational homology degree, and its rank is three for \(4\mid n\) and one otherwise. We use this theorem; we do not re-prove or claim novelty for these homotopy types.

**Signed fixed-face formula.** For any simplicial permutation \(g\) of the \(n\) vertices, its reduced Lefschetz number is
\[
\widetilde L(g)=-Z(g),\qquad Z(g)=\sum_{\substack{F\in X_n\\gF=F}}(-1)^{c_g(F)},
\]
where \(c_g(F)\) denotes the number of permutation orbits of \(g\) entirely contained in \(F\), and the empty set is included. Indeed the sign of \(g\) on the oriented simplex \(F\) equals \((-1)^{|F|-c_g(F)}\), so its reduced simplicial alternating trace is \(-(-1)^{c_g(F)}\). Homology concentration therefore implies \(\chi_n(g)=-(-1)^{d_n}Z(g)\).

**Rotations.** Write \(h=\gcd(n,a)\). An \(r^a\)-invariant subset is an \(h\)-periodic binary cycle. Choosing an occupied orbit contributes sign \(-1\); hence \(Z(r^a)\) is the signed independent-run partition function on a cycle of length \(h\). Let \(M\) have row and column states \(00,01,10,11\), with weighted transition \((u,v)\to(v,w)\) of weight \((-1)^w\) unless \(u=v=w=1\):
\[
M=\begin{pmatrix}1&-1&0&0\\0&0&1&-1\\1&-1&0&0\\0&0&1&0\end{pmatrix}.
\]
The transfer trace enumerates cyclic binary words, including for \(h=1\) and \(h=2\): \(Z(r^a)=\operatorname{tr}(M^h)\). Direct multiplication gives characteristic polynomial \(t(t-1)(t^2+1)\), so for every \(h\ge1\),
\[
Z(r^a)=1+2\cos(\pi h/2).
\]
Combining the parity of \(d_n\) with elementary gcd parity yields the rotation formulas in the table.

**Reflections.** Put \(B_L\) equal to the signed sum of binary strings of length \(L\ge2\) that contain no substring \(111\) and have neither initial nor terminal pair equal to \(11\). With the same matrix \(M\) as above,
\[
B_L=vM^{L-2}w,\quad v=(1,-1,-1,0),\quad w=(1,1,1,0)^{\mathsf T}.
\]
Multiplication shows \(v(M^2+I)=0\) while \(B_2=B_3=-1\), whence \(B_L=(-1)^{\lfloor L/2\rfloor}\) for all \(L\ge2\).

When \(n=2m\), the reflection \(r^a s\) has two fixed vertices if \(a\) is even and no fixed vertices if \(a\) is odd. A reflection-invariant cyclic word is a palindrome with \(m+1\) independent orbit-bits in the first case and \(m\) in the second. Avoiding a triple across each reflection axis is exactly the initial/terminal non-\(11\) condition in the definition of \(B_L\). Thus
\[
Z(r^as)=\begin{cases}B_{m+1},&a\text{ even},\\ B_m,&a\text{ odd}.
\end{cases}
\]
For odd \(n=2m+1\), every reflection has one fixed vertex and one doubled edge opposite it; the palindrome has \(m+1\) orbit-bits and the same two endpoint conditions, hence \(Z(r^as)=B_{m+1}\). Substituting the formula for \(B_L\) and the parity of \(d_n\) proves the reflection formulas, including both conjugacy classes when \(n\) is even.

**Representations and quotients.** If \(n=4k\), the table is the direct sum of the two-dimensional plane representation on which \(r\) acts by a quarter-turn and \(s\) by a reflection, and a one-dimensional representation on which \(r\) acts trivially and \(s\) acts by \((-1)^k\). If \(n\) is odd, the homology is one-dimensional with trivial rotations and reflection scalar \((-1)^{\lfloor(n+1)/4\rfloor}\). If \(n=4k+2\), it is one-dimensional with \(r\) acting as \(-1\) and \(s\) as \((-1)^k\). Averaging these characters gives dimensions of the invariant subspaces under \(\langle r\rangle\) and \(D_n\), respectively. A finite simplicial group action admits an invariant triangulation after barycentric subdivision, and over \(\mathbb Q\) the transfer/averaging argument identifies quotient homology with invariant homology. The displayed congruence classes follow.

## Verification
The standalone `cycle_ind2_dihedral_check.py` contains an independent fixed-orbit enumeration for all \(260\) group elements across orders \(4\le n\le16\), exact transfer matrix identities, and quotient invariant checks. Execute `python3 cycle_ind2_dihedral_check.py` using ordinary Python 3. No third-party dependencies are needed. The program finishes with `CYCLE_IND2_DIHEDRAL_CHARACTER_EXACT_CHECK_OK`. The all-order statements are proven above; finite tests do not by themselves establish universality.

## Relationship to prior work
Deshpande and Singh, Theorem 4.6, already give the **entire nonequivariant homotopy classification** for higher-independence complexes of cycles. They do not give an action of the dihedral group on their homology. The current result refines exactly that previously known classification to a full all-order character and determines rational quotient congruences. Closest other retrieved symmetry results concern ordinary cycle matching complexes or distinct bounded-independence-sphere and multipath constructions; those do not directly supply the explicit character here. For the bounded-independence work, the retrievable abstract described a different fixed-dimensional sphere family, but its full source was inaccessible, so equivalent reformulation cannot be excluded absolutely.

## Limitations
The formulas give rational equivariant homology, not integral equivariant chain equivalences. Rational acyclicity of a quotient does not prove its integral acyclicity or contractibility. Originality is supported by the accessible full Deshpande--Singh text and indexed comparisons, not an exhaustive survey of unpublished or inaccessible material. Results requiring the full inaccessible bounded-independence manuscript remain a bibliographic risk.

## References
1. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448 (first public version 2020-01-15), Theorem 4.6; Journal of the Ramanujan Mathematical Society **36** (2021), 53–71. https://arxiv.org/abs/2001.05448
2. Indexed related result, *Dihedral homology characters and quotient congruences for cycle matching complexes* (2026); mathematically different ordinary matching-complex construction.
3. Indexed related result, *Dihedral orientation characters of bounded-independence spheres on cycles* (2026); full source unavailable in this inspection.
