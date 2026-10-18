# Uniform integral homology of full strong Morse matching complexes of cycles

## Finding

For every integer \(n\ge 6\), let \(C_n\) denote the one-dimensional simplicial cycle on vertices \(\mathbb Z/n\mathbb Z\), and let \(\mathcal{SM}(C_n)\) be the **full** complex of strong discrete Morse matchings arising from strict vertex filtrations, with all filtration-induced matching subsets included. Its complete **integral reduced homology** is determined by the following two elementary residue-class functions.

Define \((d_1(n),a_1(n))\) and \((d_2(n),a_2(n))\) by
\[
(d_1(n),a_1(n))=\begin{cases}
(k-1,2),&n=3k,\\
(k-1,1),&n=3k+1,\\
(k,1),&n=3k+2,
\end{cases}
\]
\[
(d_2(n),a_2(n))=\begin{cases}
(2k-1,3),&n=4k,\\
(2k-1,1),&n=4k+1,\\
(2k,1),&n=4k+2,\\
(2k+1,1),&n=4k+3.
\end{cases}
\]
Then, for every integer \(i\ge0\),
\[
\boxed{\widetilde H_i(\mathcal{SM}(C_n);\mathbb Z)
\cong \mathbb Z^{\,a_2(n)\mathbf{1}_{\{i=n-2-d_2(n)\}}}
\oplus \mathbb Z^{\,2a_1(n)\mathbf{1}_{\{i=n-3-d_1(n)\}}}.}
\]
The indicator exponent is \(1\) exactly when its displayed equality holds, otherwise \(0\); ranks are **added** if the two degrees coincide. In particular all reduced integral homology groups are torsion-free, and every other reduced group is zero. At the first previously untabulated value \(n=22\), this gives
\[
\widetilde H_i(\mathcal{SM}(C_{22});\mathbb Z)
\cong\begin{cases}
\mathbb Z,&i=10,\\
\mathbb Z^2,&i=13,\\
0,&\text{otherwise}.
\end{cases}
\]
The statement is about **integral homology**, not a claimed wedge decomposition or integral equivariant representation.

## Assumptions and scope

The abstract cycle has edges \(e_i=\{i,i+1\}\), indices modulo \(n\), with no filled two-simplex. A matching vertex is a vertex-edge incidence arising in a strong gradient field from an injective filtration of the cycle's vertices. For a filtration \(h\), write \(s_i=+\) if \(h(i)<h(i+1)\) and \(s_i=-\) otherwise. When \(s_{i-1}=s_i=+\), the filtration matches \(i\) with \(e_{i-1}\); when both signs are \(-\), it matches \(i\) with \(e_i\). Otherwise it makes no matching at \(i\). The full complex is the downward closure of such complete matching collections. In particular, it differs from both the ordinary discrete Morse complex and the **pure** strong-matching subcomplex. We use the conventional empty face only for augmented chain complexes and combinatorial duality.

For any cycle \(C_n\), write \(\operatorname{Ind}_1(C_n)\) for the ordinary independence complex (sets without consecutive indices), and \(\operatorname{Ind}_2(C_n)\) for the higher independence complex (sets without three cyclically consecutive indices). The latter description is equivalent, for \(n\ge6\), to every component of the induced subgraph having at most two vertices. Both complexes have known integral wedge-of-spheres homotopy types [2].

## Proof

**1. A word model for the full strong complex.** Associate to a face the cyclic word \((w_i)_{i\in\mathbb Z/n\mathbb Z}\) over \(\{0,+,-\}\), with \(w_i=+\) recording the vertex-edge matching \(i\leftrightarrow e_{i-1}\), \(w_i=-\) recording \(i\leftrightarrow e_i\), and \(w_i=0\) recording no selected matching at that vertex. Each selected sign forces both adjacent edge-orientation signs to agree with it. Thus a word extends to a filtration-induced matching exactly when (a) adjacent nonzero signs are not opposite, and (b) if all selected nonzero signs have a common sign, there are two cyclically consecutive zeros. For necessity, adjacent opposite signs force an inconsistent orientation of their common edge, while a monochromatic word with no consecutive zeros forces the full cycle to be coherently oriented and hence directed cyclically. Conversely, whenever both signs occur, the forced edge orientations are nonconstant; if only one sign occurs, an edge between consecutive zeros can be oriented oppositely. A nonconstant oriented cycle is acyclic, so a linear extension realizes the orientation by distinct filtration heights. The all-zero word also extends. This proves the criterion for **every** \(n\ge6\), without relying on finite face enumeration. The same criterion appears in the independently published face-enumeration and Euler-characteristic study [3].

**2. A larger bipartite independence complex.** Let \(X=\{x_i:i\in\mathbb Z/n\mathbb Z\}\) and \(Y=\{y_i:i\in\mathbb Z/n\mathbb Z\}\) encode \(+\) and \(-\) matching vertices, respectively. Let \(B_n\) be the bipartite graph with edges \(x_i y_j\) precisely for \(j\in\{i-1,i,i+1\}\). Put \(L=\operatorname{Ind}_1(B_n)\). Its faces are exactly the three-symbol words obeying condition (a): a face cannot take both signs at the same site or opposite signs at adjacent sites. Hence \(K=\mathcal{SM}(C_n)\) is a subcomplex of \(L\). An allowed word in \(L\) fails condition (b) exactly when it consists entirely of a single nonzero sign and its marked vertex set meets every edge of the underlying cycle. In particular, **every mixed-sign face of \(L\) lies in \(K\)**.

For a complex \(Q\) on the fixed ground set \(X\), define its combinatorial Alexander dual \(Q^{\vee}=\{S\subseteq X:X\setminus S\notin Q\}\). The pure \(X\)-subcomplex of \(K\) is
\[
A_X=K\cap\Delta_X=\operatorname{Ind}_1(C_n)^{\vee},
\]
where \(\Delta_X\) is the full simplex on \(X\). Indeed, a pure plus-sign subset extends exactly when its complement contains two consecutive vertices. There is an identical subcomplex \(A_Y\) in \(\Delta_Y\). Because the omitted faces of \(L\) are exclusively pure and monochromatic, the **relative simplicial chain complex** splits integrally as
\[
C_*(L,K;\mathbb Z)\cong
C_*(\Delta_X,A_X;\mathbb Z)\oplus
C_*(\Delta_Y,A_Y;\mathbb Z).
\]
Both summands are actual relative chain complexes: the boundary of a monochromatic omitted simplex cannot acquire a mixed sign, and any newly admissible boundary face becomes zero in the quotient. Since each full simplex is contractible, the relative long exact sequence and integral combinatorial Alexander duality yield, for \(j\ge1\),
\[
H_j(L,K;\mathbb Z)\cong
\left(\widetilde H^{\,n-j-2}(\operatorname{Ind}_1(C_n);\mathbb Z)\right)^{\oplus2}.
\]
Here the dimension conversion is \(\widetilde H_{j-1}(Q^{\vee})\cong\widetilde H^{n-(j-1)-3}(Q)\), and no field coefficients or universal-coefficient shortcuts are used.

**3. Compute the homology of the larger complex.** Let \(\operatorname{st}_{L}(y_j)\) be the closed simplicial star of \(y_j\), and set \(U=\bigcup_{j}\operatorname{st}_{L}(y_j)\). Every finite nonempty intersection of these stars is a cone: the vertices \(y_j\) are pairwise independent in the bipartite graph, so any face compatible with all of a specified finite set of \(y\)'s can be enlarged by any one of these vertices, while remaining compatible with all. All such intersections are nonempty. The simplicial nerve lemma, whose nerve is the full simplex on \(Y\), therefore gives \(U\simeq\{\mathrm{point}\}\).

Every face of \(L\) either is pure \(X\) or contains a \(y_j\), so \(L=\Delta_X\cup U\). Their intersection consists of the pure \(X\)-subsets which can be enlarged by at least one \(y_j\); equivalently their complement contains the triple \(\{j-1,j,j+1\}\) for some \(j\). Consequently,
\[
D=\Delta_X\cap U=\operatorname{Ind}_2(C_n)^{\vee}.
\]
The two cover pieces are contractible, and their inclusion diagrams form a homotopy pushout because simplicial subcomplex inclusions are cofibrations. Hence \(L\simeq\Sigma D\), the suspension of their intersection (up to homotopy). In particular integral Alexander duality gives
\[
\widetilde H_i(L;\mathbb Z)\cong
\widetilde H_{i-1}(D;\mathbb Z)
\cong \widetilde H^{\,n-i-2}(\operatorname{Ind}_2(C_n);\mathbb Z).
\]
This suspension argument uses the contractibility of the **union of stars**, not the false assertion that a single star contains every mixed face.

**4. Apply known higher-independence homotopy theorems.** The ordinary cycle independence complex is \(\bigvee^{a_1(n)}S^{d_1(n)}\) (Kozlov's cycle calculation, reproduced as Proposition 4.1 of [2]). The higher complex \(\operatorname{Ind}_2(C_n)\) is \(\bigvee^{a_2(n)}S^{d_2(n)}\) by Deshpande–Singh [2, Theorem 4.6 with parameter \(d=4\)]. These are wedge-of-spheres homotopy equivalences, so their integral cohomology groups are free and concentrated in the displayed degrees. Thus \(\widetilde H_i(L)\) is free of rank \(a_2(n)\) in degree \(\ell=n-2-d_2(n)\), and \(H_j(L,K)\) is free of rank \(2a_1(n)\) in degree \(j=n-2-d_1(n)\); all other positive-degree groups vanish.

For all \(n\ge6\), the displayed residue formulas give \(d_2(n)>d_1(n)\), equivalently \(\ell<j\). In the long exact homology sequence of \((L,K)\), the only potential extensions are therefore between adjacent nonzero degrees, with no nonzero map from \(\widetilde H_j(L)\) into \(H_j(L,K)\) and no nonzero map from \(\widetilde H_{\ell}(L)\) into \(H_{\ell}(L,K)\). The sequence yields, in every degree \(i\ge1\),
\[
0\longrightarrow H_{i+1}(L,K;\mathbb Z)
\longrightarrow \widetilde H_i(K;\mathbb Z)
\longrightarrow \widetilde H_i(L;\mathbb Z)
\longrightarrow0.
\]
All possible nonzero right-hand terms are free abelian, so each short exact sequence splits (noncanonically). Connectedness also follows from the exact sequence because \(L\) is connected and the relative groups vanish below degree two. This gives exactly the boxed formula, including coincidence-of-degree cases. Inserting \(n=22\) into the two residue tables gives \((d_1,a_1)=(6,1)\), \((d_2,a_2)=(10,1)\), and homology in degrees \(22-3-6=13\) and \(22-2-10=10\), of ranks two and one. This finishes the integral proof.

## Verification

The self-contained standard-library Python program `verify_strong_cycle_homology.py` constructs all strict vertex filtrations and their downward-closed matching faces for \(3\le n\le8\); independently constructs the three-symbol word complex, the bipartite independence supercomplex, and its excluded monochromatic vertex covers; and confirms the face criterion exactly. It also computes degree-by-degree boundary ranks over \(\mathbb F_2\) for \(6\le n\le9\) and compares them with the theorem's predicted integral-free ranks. For the published underlying higher-independence complexes, a separate vertex-by-vertex acyclic matching computes critical-cell dimensions and counts for \(\operatorname{Ind}_2(C_n)\), \(6\le n\le22\), and \(\operatorname{Ind}_1(C_n)\), \(6\le n\le16\). All tests print `VERIFY_OK`. Direct finite-field ranks cannot on their own establish the absence of integral torsion; that conclusion uses the proved integral exact sequence and the integral wedge-of-spheres theorems in Step 4.

The formula independently reproduces the reduced homology ranks in [1, Table 1] for every \(6\le n\le21\). The new \(n=22\) groups agree with the separately known reduced Euler characteristic \(-1\), because \((-1)^{10}-2=-1\), but agreement of Euler characteristic is far weaker than this complete group calculation.

## Relationship to prior work

Knudson–Owens-White [1] define full and pure strong Morse matching complexes, prove the pure-cycle homotopy classification, and list the full-cycle homology through \(n=21\). Their published Table 1 explicitly records the \(n=22\) homology computation as out of memory, and does not give the all-length formula above. Deshpande–Singh [2] determine both ingredients \(\operatorname{Ind}_1(C_n)\) and \(\operatorname{Ind}_2(C_n)\), but not their relation to the **full strong matching complex**. The earlier face-polynomial calculation [3] characterizes cyclic matching words and their Euler characteristics, but explicitly does not determine individual homology groups. A separate equivariant Euler-characteristic study [4] computes alternating traces for the full strong complex, but expressly does not determine the graded or integral homology. None of these preceding statements alone implies the stated complete integral classification; the new ingredient is the relative homology decomposition through the bipartite independence complex and two Alexander-dual cycle complexes.

## Limitations

The proof determines abstract integral reduced homology groups for every \(n\ge6\). It **does not** establish a wedge-of-spheres homotopy equivalence for the full strong complex, compute attaching maps or cup products, or determine the dihedral representation on these groups. The splitting is noncanonical. The direct computations are finite corroboration, not an exhaustive enumeration of the full complex at \(n=22\), which has hundreds of millions of faces. The originality comparison includes the named and inspected sources but cannot exclude unindexed or unpublished equivalent arguments.

## References

[1] K. P. Knudson and A. Owens-White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1, first public 2026-09-06, especially Definition 4.2, Section 8, and Table 1, https://arxiv.org/abs/2609.06844.

[2] P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first public 2020-01-15, especially Proposition 4.1 and Theorem 4.6, https://arxiv.org/abs/2001.05448.

[3] *Face enumeration and Euler periodicity of strong Morse cycle complexes*, publicly accessible result, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-face-enumeration-and-euler-periodicity-of-strong-morse-cycle-com--7ecee706974b.

[4] *Dihedral Euler characters of full strong Morse complexes of cycles*, publicly accessible result, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-dihedral-euler-characters-of-full-strong-morse-complexes-of-cycl--4819a9d67705.
