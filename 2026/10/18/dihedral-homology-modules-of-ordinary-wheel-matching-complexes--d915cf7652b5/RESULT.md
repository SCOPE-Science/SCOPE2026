# Dihedral homology modules of ordinary wheel matching complexes

## Finding
Let \(n\geq 4\) with \(n\equiv 1\) or \(2\pmod 3\). Write \(n=3k+\varepsilon\), where \(k\geq1\) and \(\varepsilon\in\{1,2\}\). Consider the wheel \(W_n=C_n*K_1\) with rim vertices \(i\in\mathbb Z/n\mathbb Z\), hub \(h\), rim edges \(e_i=\{i,i+1\}\), and spokes \(t_i=\{h,i\}\). Let \(X_n=\operatorname{Match}(W_n)\) be its **ordinary edge-matching complex**, not its discrete-Morse complex. The dihedral group \(D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\) acts by \(r(i)=i+1\), \(s(i)=-i\), fixing \(h\).

Define the signs
\[
\alpha=\begin{cases}(-1)^{k(k+1)/2},&\varepsilon=1,\\(-1)^{k(k-1)/2},&\varepsilon=2,\end{cases}
\qquad u=(-1)^{n+1},\qquad
 b=\begin{cases}\alpha,&\varepsilon=1,\\(-1)^{(k+1)(k+2)/2},&\varepsilon=2.\end{cases}
\]
Let \(E_n=\operatorname{Ind}_{\langle s\rangle}^{D_n}\mathbb Q_{\alpha}\), where the one-dimensional stabilizer module has \(s\) acting by \(\alpha\), and let \(L_n\) be the one-dimensional \(D_n\)-module on which \(r\) acts by \(u\) and \(s\) by \(b\). (Because \(u=1\) when \(n\) is odd, these formulas always define a dihedral character.) Then the **complete reduced rational homology as a dihedral representation** is concentrated in degree \(k\), and
\[
\widetilde H_k(X_n;\mathbb Q)\cong
\begin{cases}
\ker(E_n\twoheadrightarrow L_n),&\varepsilon=1,\\
E_n\oplus L_n,&\varepsilon=2.
\end{cases}
\]
The surjection in the first line is the connecting homomorphism of the spoke-relative long exact sequence; in particular it is an actual module map, not a formal character subtraction.

More explicitly, for \(0\leq j<n\), put \(\eta=-1\) for \(\varepsilon=1\) and \(\eta=1\) for \(\varepsilon=2\), and define
\[
 f_n(j)=\#\{i\in\mathbb Z/n\mathbb Z:2i\equiv j\pmod n\}
 =\begin{cases}1,&n\text{ odd},\\2,&n\text{ even and }j\text{ even},\\0,&n\text{ even and }j\text{ odd}.\end{cases}
\]
Its entire degree-\(k\) character is
\[
\chi_n(r^j)=n\mathbf1_{j=0}+\eta u^j,
\qquad
\chi_n(r^j s)=\alpha f_n(j)+\eta u^j b.
\]
Thus its dimensions are \(n-1\) when \(n\equiv1\pmod3\) and \(n+1\) when \(n\equiv2\pmod3\). The dimensions alone are previously known; the dihedral representations and explicit trace formulas are the asserted refinement.

## Assumptions and scope
All graphs are finite simple undirected graphs; matchings consist of pairwise vertex-disjoint graph edges; each matching is a simplex with its graph edges as vertices. Reduced homology uses coefficients \(\mathbb Q\). The action on oriented simplicial chains includes permutation orientation signs. This result concerns exactly \(n\ge4\) and \(n\equiv1,2\pmod3\); the missing residue class has contractible spoke links and reduces to the already studied rim-cycle matching complex. No integral equivariant splitting or statement about arbitrary wheel modifications is claimed.

## Proof
**1. Spoke filtration.** Put \(B=\operatorname{Match}(C_n)=\operatorname{Ind}(C_n)\), where the latter cycle has vertices indexed by the rim-edge labels. For every spoke \(t_i\), the matching faces containing that spoke are \(t_i*K_i\), with \(K_i\cong\operatorname{Ind}(P_{n-2})\), because the forbidden rim edges are precisely \(e_{i-1}\) and \(e_i\). Distinct spoke cones meet only in \(B\), since two spokes can never belong to the same matching. Hence the relative quotient is equivariantly a wedge of the \(n\) suspended links:
\[
 X_n/B\cong\bigvee_{i\in\mathbb Z/n\mathbb Z}\Sigma K_i.
\]
For the stated residue classes, the classical path recursion gives \(K_i\simeq S^{k-1}\). The stabilizer of \(t_0\) is \(\langle s\rangle\), which reverses its length-\(n-2\) path of rim-edge labels. Denote its scalar action on \(\widetilde H_{k-1}(K_0;\mathbb Q)\) by \(\alpha\). Since the connecting relative chains carry the spoke orientation as an unchanged single extra vertex, no extra suspension sign appears. It follows that
\[
\widetilde H_q(X_n,B;\mathbb Q)=\begin{cases}E_n,&q=k,\\0,&q\ne k.\end{cases}
\]

**2. The rim line and the exact sequence.** The classical cycle recursion yields \(B\simeq S^{k-1}\) for \(\varepsilon=1\), and \(B\simeq S^k\) for \(\varepsilon=2\). Let \(L_n\) denote the corresponding one-dimensional reduced homology of \(B\), with actions of \(r,s\) to be calculated below. If \(\varepsilon=2\), the reduced long exact sequence of \((X_n,B)\) reduces to
\[
0\longrightarrow L_n\longrightarrow\widetilde H_k(X_n;\mathbb Q)
\longrightarrow E_n\longrightarrow0.
\]
This sequence splits as \(D_n\)-modules, since \(\mathbb Q[D_n]\) is semisimple. If \(\varepsilon=1\), the corresponding sequence is
\[
0\longrightarrow\widetilde H_k(X_n;\mathbb Q)\longrightarrow E_n
\xrightarrow{\partial}L_n\longrightarrow\widetilde H_{k-1}(X_n;\mathbb Q)\longrightarrow0.
\]
The map \(K_0\hookrightarrow B\) is a homotopy equivalence: factor it through the path on \(n-1\) consecutive rim-edge labels. Adding each of the two missing endpoint labels is a mapping-cone attachment with link \(\operatorname{Ind}(P_{n-3})\). Here \(n-3=3(k-1)+1\), so each link is contractible by the path recursion. Consequently the composite induces an isomorphism on \(\widetilde H_{k-1}\); the component of \(\partial\) indexed by \(t_0\) is nonzero. Thus \(\partial\) is surjective and \(\widetilde H_{k-1}(X_n;\mathbb Q)=0\). There are no other reduced groups, proving the module descriptions up to identification of their signs.

**3. A signed Lefschetz calculation.** For any simplicial complex \(Y=\operatorname{Ind}(G)\) and graph automorphism \(g\), partition the vertex set into \(g\)-orbits. Discard an orbit containing an edge of \(G\), and on the remaining orbits form a conflict graph \(H_g\): two orbit-vertices are adjacent exactly when an edge of \(G\) joins their original vertices. A \(g\)-invariant independent face is a union of pairwise compatible orbit blocks. If it consists of \(q\) orbit blocks and \(v\) original vertices, the orientation sign of \(g\) on the face is \((-1)^{v-q}\), and its alternating simplicial-chain sign is \((-1)^{v-1}\). Including the empty augmented face yields the exact reduced Lefschetz identity
\[
\widetilde L(g;Y)=-I(H_g;-1),
\qquad I(H;z)=\sum_{S\text{ independent in }H}z^{|S|}.
\]
If \(\widetilde H_*(Y;\mathbb Q)\) is concentrated in degree \(d\), then its unique homology trace is \((-1)^{d+1}I(H_g;-1)\). This identity uses the orientation signs, so fixed faces need not have positive trace.

For a path reversed end-for-end, the valid orbit conflict graph is itself a path \(P_t\), with \(t=(m+1)/2\) if its original number \(m\) of vertices is odd, and \(t=m/2-1\) if \(m\) is even (in the even case the middle exchanged adjacent pair is forbidden). Write \(F_t=I(P_t;-1)\). Deleting the last path vertex gives
\[
F_0=1,\quad F_1=0,\quad F_t=F_{t-1}-F_{t-2}.
\]
This sequence has period six: \(1,0,-1,-1,0,1\). Taking \(m=n-2\) and \(d=k-1\), the identity \(\alpha=(-1)^kF_t\) simplifies, according to \(\varepsilon\), to precisely the two formulas for \(\alpha\) in the finding.

On \(B=\operatorname{Ind}(C_n)\), a one-step rotation has no nonempty invariant independent faces, so its reduced Lefschetz number is \(-1\). Since the unique homology degree is \(k-1\) or \(k\), this yields \(r\mapsto u=(-1)^{n+1}\). When \(\varepsilon=1\), the inclusion \(K_0\hookrightarrow B\) just proved is also \(s\)-equivariant, hence the reflection acts by \(b=\alpha\). When \(\varepsilon=2\), the reflection on rim-edge labels acts by \(e_i\mapsto e_{-i-1}\). Its valid orbit conflict graph is \(P_{(n-1)/2}\) for odd \(n\), or \(P_{n/2-2}\) for even \(n\). Evaluating the same six-periodic sequence and multiplying by \((-1)^{k+1}\) gives \(b=(-1)^{(k+1)(k+2)/2}\). This identifies the rim line \(L_n\) in both cases.

**4. The whole character.** In the induced spoke module \(E_n\), a rotation fixes all \(n\) spokes if it is the identity and none otherwise; thus its trace is \(n\mathbf1_{j=0}\). A reflection \(r^js\) fixes the spokes indexed by solutions of \(2i=j\pmod n\), and on every such stabilizer copy it has trace \(\alpha\). Its trace is therefore \(\alpha f_n(j)\). The one-dimensional line contributes \(u^j\) on \(r^j\) and \(u^jb\) on \(r^js\). Subtraction for the kernel or addition for the direct sum proves both displayed character formulas for every element and every permitted \(n\). \(\square\)

## Verification
The included standalone program `verify_wheel.py` generates all matchings of each wheel independently of the module construction, applies every dihedral automorphism to each oriented face, and computes the reduced simplicial Lefschetz trace including the augmented empty face. The formula is checked for every rotation and reflection at each rim length \(n=4,5,7,8,10,11,13,14,16,17,19,20\). The exact output is in `verification_output.txt`; all twelve cases pass. A separate `verify_mod2.py` computes exact reduced boundary ranks over \(\mathbb F_2\) for the initial seven permitted lengths; its output is `verification_mod2_output.txt`. These finite checks corroborate signs, ranks and normalization, but the infinite-family proof is the four steps above, not enumeration. As sample consequences, for \(n=8\) the top dimension is \(9\) and all reflections have trace \(-1\); for \(n=10\) it is dimension \(9\) and all reflections have trace \(+1\).

## Relationship to prior work
The 2017 manuscript by Boudouris, Kawakami, and Kettinger (Proposition 1.19 and Corollary 1.20, read in full context) already proves the **nonequivariant wheel matching-complex wedge types**, including the sphere multiplicities here; neither the sphere ranks nor the wedge statement are asserted new. Adamaszek's 2011 work recounts the classical Kozlov homotopy recursions for paths and cycles and develops natural cofibre splittings, which supply the baseline for the present proof. Known dihedral character formulas for **cycle** matching complexes govern only \(B\), whereas the induced spoke module and its connecting map carry the new wheel representation. A published wheel **discrete-Morse**-complex formula concerns a different complex of acyclic face matchings, not the ordinary simplicial matching complex used here. The new comparison is a statement-and-implication distinction: nonequivariant ranks and rim-cycle symmetry alone do not determine the wheel's full character without computing its spoke stabilizer sign and the equivariant connecting map.

## Limitations
Only rational group representations are classified; an integral \(D_n\)-lattice splitting is not asserted. The excluded congruence class \(n\equiv0\pmod3\) has contractible spoke links, so the present induced-module extension is not present in that class. The published nonequivariant homotopy result is unchanged. Exhaustive small cases are independent computational checks, not evidence of bibliographic uniqueness; further literature could contain equivalent equivariant statements under different terminology.

## References
1. Michał Adamaszek, *Splittings of independence complexes and the powers of cycles*, arXiv:1106.6250 (first public version 2011-06-30), especially the introduction, classical path/cycle recursion, and Section 3. https://arxiv.org/abs/1106.6250
2. James Boudouris, Sho Kawakami, and Jacob Kettinger, *Summer 2017 CURL Research*, Section 1, Proposition 1.19 and Corollary 1.20. https://jakettinger.github.io/curl.pdf
3. Dmitry Kozlov, classical independence-complex calculations for paths and cycles, as cited and restated in Adamaszek (Reference 1).
