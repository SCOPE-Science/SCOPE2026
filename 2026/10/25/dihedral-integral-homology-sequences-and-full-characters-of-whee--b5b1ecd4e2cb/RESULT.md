# Dihedral integral homology sequences and full characters of wheel matching complexes

## Finding

Let \(n\geq3\), let \(W_{n+1}\) be the wheel with rim vertices \(\mathbb Z/n\mathbb Z\), rim edges \(e_j=\{j,j+1\}\), one hub, and spokes \(u_j\) from the hub to rim vertex \(j\). Let \(X_n=\mathcal M(W_{n+1})\) be its *ordinary* matching complex. The dihedral group \(D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\) acts by \(r(j)=j+1\) and \(s(j)=-j\) on rim vertices, fixing the hub. Write \(R_n=\mathcal M(C_n)=\operatorname{Ind}(C_n)\) for the subcomplex using only rim edges, and let \(J_n=\ker(\mathbb Z[\mathbb Z/n\mathbb Z]\xrightarrow{\mathrm{sum}}\mathbb Z)\), with its natural permutation action. All homology is reduced and has integral coefficients unless specified.

**Integral equivariant statement.** In the following three cases, the displayed group is the *only* nonzero reduced homology group of \(X_n\), and it is free abelian:

1. If \(n=3k\), \(k\ge1\), the natural inclusion induces an isomorphism of \(\mathbb Z[D_n]\)-modules \(\widetilde H_{k-1}(X_n)\cong\widetilde H_{k-1}(R_n)\cong\mathbb Z^2\).
2. If \(n=3k+1\), \(k\ge1\), there is a natural \(\mathbb Z[D_n]\)-module isomorphism \(\widetilde H_k(X_n)\cong\widetilde H_{k-1}(R_n)\otimes_{\mathbb Z}J_n\). Here \(\widetilde H_{k-1}(R_n)\) has rank one and the tensor action is diagonal.
3. If \(n=3k+2\), \(k\ge1\), there is a natural exact sequence of integral \(D_n\)-modules
   \[
   0\longrightarrow\widetilde H_k(R_n)\longrightarrow\widetilde H_k(X_n)\longrightarrow\operatorname{Ind}_{\langle s\rangle}^{D_n}\mathbb Z_{\varepsilon_k}\longrightarrow0,
   \qquad \varepsilon_k=(-1)^{k(k-1)/2}.
   \]
   The left module has rank one; \(\mathbb Z_{\varepsilon_k}\) denotes the one-dimensional integral representation on which \(s\) acts by \(\varepsilon_k\). In this third case the sequence splits over \(\mathbb Q\); **no integral equivariant splitting is claimed**.

**Explicit full rational character.** Put \(d_n=k-1\) when \(n=3k\) or \(n=3k+1\), and \(d_n=k\) when \(n=3k+2\). Define integers \(p_{-1}=p_0=1\), \(p_1=0\) and \(p_j=p_{j-1}-p_{j-2}\) for \(j\ge2\); thus \(p_j\) is six-periodic. Put \(c_j=2\cos(j\pi/3)\), an integer in \(\{-2,-1,1,2\}\). For \(0\le a<n\), define
\[
\Lambda_n(r^a)=-c_{\gcd(n,a)},
\]
where \(\gcd(n,0)=n\), and
\[
\Lambda_n(r^a s)=
\begin{cases}
-p_{q-1}+p_{q-2},&n=2q+1,\\
-p_{q-2},&n=2q\text{ and }a\text{ even},\\
-p_{q+1},&n=2q\text{ and }a\text{ odd}.
\end{cases}
\]
Let \(\chi_R(g)=(-1)^{d_n}\Lambda_n(g)\), and let \(f(g)\) be the number of rim vertices fixed by \(g\): \(f(1)=n\), all other rotations have \(f=0\), odd-rim reflections have \(f=1\), and for even \(n\) the reflection \(r^a s\) has \(f=2\) for even \(a\) and \(f=0\) for odd \(a\). The complete character of the unique nonzero rational homology group of \(X_n\) is
\[
\chi_X(g)=
\begin{cases}
\chi_R(g),&n\equiv0\pmod3,\\
\chi_R(g)(f(g)-1),&n\equiv1\pmod3,\\
\chi_R(g)+T_n(g),&n\equiv2\pmod3,
\end{cases}
\]
where \(T_n(1)=n\), \(T_n(r^a)=0\) for nonidentity rotations, and \(T_n(r^a s)=\varepsilon_k f(r^a s)\) in the last case \(n=3k+2\). These formulas include every rotation and both reflection conjugacy classes when \(n\) is even.

## Assumptions and scope

Graphs are finite, simple, undirected; a matching consists of pairwise vertex-disjoint edges. The wheel has exactly one hub plus \(n\) rim vertices; this avoids conflicting wheel-index conventions. The statement concerns the natural rim-dihedral subgroup of automorphisms (for the tetrahedral wheel, the full automorphism group can be larger). The induced module in the third case is a **relative-homology quotient**, not an assertion that integral absolute homology splits as a direct sum. Only ordinary matching complexes are considered, not the higher bounded-degree or discrete-Morse matching complexes.

## Proof

**1. Equivariant cone decomposition.** An allowed matching contains zero or one spoke. Define \(A_i\subseteq R_n\) to be the rim matchings avoiding rim edges \(e_{i-1}\) and \(e_i\), namely \(A_i\cong\operatorname{Ind}(P_{n-2})\). There is a literal simplicial decomposition
\[
X_n=R_n\ \cup\ \bigcup_{i\in\mathbb Z/n\mathbb Z}(u_i*A_i).
\]
Different cone interiors do not intersect because two spokes share the hub. The group permutes the cones and preserves \(R_n\). Consequently the relative chain complex of \((X_n,R_n)\) is canonically a direct sum of shifted *augmented* chain complexes of the \(A_i\). In every degree, its relative-homology module is therefore
\[
H_j(X_n,R_n;\mathbb Z)\cong\bigoplus_i\widetilde H_{j-1}(A_i;\mathbb Z).
\]
Choosing each cone vertex first in the orientation makes this identification equivariant without an additional permutation sign. The boundary map in the long exact sequence of the pair sends the summand belonging to \(i\) to the inclusion-induced homomorphism \(\widetilde H_{j-1}(A_i)\to\widetilde H_{j-1}(R_n)\).

**2. Path and cycle topology.** The standard independence-complex recurrence, obtained from vertex deletion and its cone on the link, gives \(\operatorname{Ind}(P_{3k})\simeq S^{k-1}\), \(\operatorname{Ind}(P_{3k+1})\simeq\mathrm{pt}\), and \(\operatorname{Ind}(P_{3k+2})\simeq S^k\), with the usual valid smallest cases. The corresponding cycle formula is \(\operatorname{Ind}(C_{3k})\simeq S^{k-1}\vee S^{k-1}\), \(\operatorname{Ind}(C_{3k+1})\simeq S^{k-1}\), and \(\operatorname{Ind}(C_{3k+2})\simeq S^k\). These well-established formulas apply integrally and show that the groups appearing below are free.

For \(n=3k\), every \(A_i\cong\operatorname{Ind}(P_{3k-2})\) is contractible, so the relative groups vanish and the inclusion \(R_n\hookrightarrow X_n\) induces all the asserted integral equivariant homology isomorphisms.

For \(n=3k+1\), every \(A_i\cong\operatorname{Ind}(P_{3k-1})\) is a \((k-1)\)-sphere up to homotopy. Its inclusion in \(R_n\) is a homotopy equivalence. Indeed, insert first one of the two deleted adjacent rim-edge vertices to pass to the induced path complex \(\operatorname{Ind}(P_{3k})\), then insert the other to pass to \(\operatorname{Ind}(C_{3k+1})\). At each insertion the added cone attaches along \(\operatorname{Ind}(P_{3k-2})\), which is contractible; hence each inclusion is a homotopy equivalence. In the relative exact sequence, the resulting boundary \(\bigoplus_i\widetilde H_{k-1}(A_i)\to\widetilde H_{k-1}(R_n)\) becomes the **sum map** after identifying each summand by its own inclusion isomorphism. These identifications commute with the dihedral action. Its kernel is precisely \(\widetilde H_{k-1}(R_n)\otimes J_n\); it is the only nonzero reduced homology of \(X_n\).

For \(n=3k+2\), each \(A_i\cong\operatorname{Ind}(P_{3k})\) has a single integral homology group in degree \(k-1\), while \(R_n\) has a single group in degree \(k\). The exact sequence of the pair therefore reduces to the short exact sequence
\[
0\to\widetilde H_k(R_n)\to\widetilde H_k(X_n)\to\bigoplus_i\widetilde H_{k-1}(A_i)\to0.
\]
The dihedral group acts transitively on spoke positions, with stabilizer \(\langle s\rangle\) of \(u_0\). Its action on \(A_0\) reverses the path with \(3k\) vertices. Step 3 computes its degree \(\varepsilon_k\). Thus the right side is the claimed induced integral module. The sequence splits rationally by Maschke's theorem; no integral splitting is necessary for the character formula. Its abelian middle group is free since both outer groups are free.

**3. Reversal sign and explicit character.** Let \(p_j\) be the alternating independence-set count of a path with \(j\) vertices; deletion of an endpoint proves \(p_j=p_{j-1}-p_{j-2}\). A reflection-invariant simplex contributes its simplicial orientation sign to the reduced Lefschetz number, including \(-1\) for the empty simplex. On \(\operatorname{Ind}(P_m)\), reversal has reduced Lefschetz number \(-p_{q-1}\) for \(m=2q\), and \(-p_q+p_{q-1}\) for \(m=2q+1\): select mirror-paired vertices, forbidding adjacent pairs, and optionally the fixed middle vertex. Since \(\operatorname{Ind}(P_{3k})\) has just one reduced homology group, of degree \(k-1\), division by its alternating sign gives the reversal degree \((-1)^{k(k-1)/2}\).

For \(R_n=\operatorname{Ind}(C_n)\), a rotation by \(a\) fixes independent subsets that are unions of its cyclic vertex orbits. Their signed contributions are the alternating independent-set count of the cycle on \(\gcd(n,a)\) orbit classes (with the evident conventions for one or two orbit classes), yielding reduced Lefschetz number \(-2\cos(\gcd(n,a)\pi/3)\). For a reflection, selecting mirror pairs and optional fixed vertices yields respectively \(-p_{q-1}+p_{q-2}\) when \(n=2q+1\), and \(-p_{q-2}\) or \(-p_{q+1}\) when \(n=2q\), according to whether the wheel reflection fixes rim vertices or rim edges. This proves \(\Lambda_n\). Since \(R_n\) has reduced homology in precisely degree \(d_n\), the Lefschetz formula gives \(\chi_R=(-1)^{d_n}\Lambda_n\).

Finally, in the first residue case the character is unchanged; in the second it is the tensor-product character of a rank-one rim module and the spoke augmentation module, giving \(\chi_R(f-1)\). In the third the character is the sum of the rim character and the induced character of the spoke-stabilizer sign; the latter evaluates to \(n\) at the identity, zero on other rotations, and \(\varepsilon_k\) times the fixed-spoke count on reflections. This proves every displayed formula and all homological vanishing statements.

## Verification

Execute `python3 check_wheel.py` with Python 3 and no nonstandard dependencies. It enumerates every wheel matching simplex and its orientation sign for each dihedral element at each \(3\le n\le18\), comparing the resulting reduced Lefschetz trace to the theorem; it also checks the rim-cycle formula. There are 672 character comparisons (wheel and rim) and eight independent mod-two simplicial-boundary computations for wheel sizes \(3\le n\le10\). These finite checks exercise normalization, reflection parity, and the transition between residues. They are not a substitute for the general equivariant exact-sequence proof.

## Relationship to prior work

Vega's *2-Matching Complexes* (arXiv:1909.10406, Theorem 5.2) gives the nonequivariant homotopy type of the ordinary matching complex of every wheel. Bayer, Jelić Milutinović, and Vega's *Matching Complexes of Outerplanar Graphs* (arXiv:2411.04601, public 2024-11-07) situates wheels among nonouterplanar planar examples, with its general result concerning outerplanar graphs. Neither inspected theorem specifies the integral \(D_n\)-module structure, the spoke augmentation sequence, or the full wheel character. Separate work on dihedral homology of **cycle** matching complexes supplies related rim information but cannot alone determine the attaching maps from the spoke-cone links. This result concerns the missing equivariant wheel calculation; it does not claim novelty for the homotopy types or cycle characters already known.

## Limitations

Only the natural dihedral action and ordinary matching complexes are classified. The exact integral sequence in the third residue class is not asserted to split integrally. A rational character determines a rational representation but not an arbitrary integral lattice up to isomorphism. The result does not provide an equivariant homotopy equivalence. Equivalence to a source not inspected in full remains a literature risk; independent scientific audit has not been performed.

## References

- Julianne Vega, *2-Matching Complexes*, arXiv:1909.10406v2, Section 5, Theorem 5.2 (2021 revision; first public 2019-09-23). https://arxiv.org/html/1909.10406v2
- Margaret Bayer, Marija Jelić Milutinović, and Julianne Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v1, first public 2024-11-07; the 2026 revision is also inspected. https://arxiv.org/html/2411.04601v2
- Dmitry N. Kozlov, *Complexes of directed trees*, Journal of Combinatorial Theory, Series A 88 (1999), 112–122; standard path and cycle independence-complex formulas quoted in Vega, Proposition 5.1.
