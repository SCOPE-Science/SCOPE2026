# Dihedral homology characters and quotient periodicity for ordinary wheel matching complexes

## Finding
For each integer \(n\ge3\), let \(W_{n+1}=C_n*K_1\) be the wheel with \(n\) rim vertices and an apex, and let \(X_n=\mathcal M(W_{n+1})\) be its **ordinary matching complex**. Its vertices are edges of the wheel, and its simplices are pairwise disjoint sets of edges. The group \(D_n=\langle r,s\mid r^n=s^2=1,\;srs=r^{-1}\rangle\) fixes the apex and acts on rim vertices \(j\in\mathbb Z/n\mathbb Z\) by \(r(j)=j+1\) and \(s(j)=-j\).

The homology-concentration theorem of Vega [1] (NOT newly claimed) gives one nonzero reduced integral homology degree \(h_n\) and its rank \(b_n\):
\[
(h_n,b_n)=\begin{cases}
(k-1,2),&n=3k,\\
(k,3k),&n=3k+1,\\
(k,3k+3),&n=3k+2.
\end{cases}
\]
The **new claim** is the complete rational \(D_n\)-homology character \(\chi_n(g)=\operatorname{tr}(g\mid\widetilde H_{h_n}(X_n;\mathbb Q))\). Put \(p_j=(1,0,-1,-1,0,1)_{j\bmod6}\) for \(j\ge0\) and \(q_j=2\cos(\pi j/3)\) (an integer). Then
\[
\boxed{\begin{aligned}
\chi_n(1)&=b_n,\\
\chi_n(r^a)&=(-1)^{h_n+1}q_{\gcd(n,a)} \quad(1\le a<n),\\
\chi_n(r^as)&=\begin{cases}0,&n\text{ odd},\\(-1)^{h_n}p_{n/2-2},&n\text{ even},\end{cases}\quad(0\le a<n).
\end{aligned}}
\]
For even rim length, **the two distinct conjugacy classes of reflections always have the same trace**; for odd rim length, all reflections have trace zero. The character determines the entire semisimple rational \(D_n\)-module. The rational homology of the full dihedral quotient is concentrated in degree \(h_n\), and
\[
\boxed{\dim_{\mathbb Q}\widetilde H_{h_n}(|X_n|/D_n;\mathbb Q)
=\begin{cases}1,&n\equiv2,5,10,11\pmod{12},\\0,&\text{otherwise}.\end{cases}}
\]
All other reduced rational quotient homology groups vanish. The quotient assertion does not mean a rationally acyclic quotient is contractible.

## Assumptions and scope
The wheel has exactly \(n+1\) graph vertices and exactly \(2n\) edges. All cycles are simple, including the triangle at \(n=3\). Label rim edges \(e_j=\{j,j+1\}\) and spokes \(\ell_j=\{*,j\}\). The line graph has a rim-induced \(C_n\) on the \(e_j\), a complete graph on the \(\ell_j\), and cross-adjacencies \(e_j\sim\ell_j,\ell_{j+1}\). The cyclic action on rim-edge labels is \(r(e_j)=e_{j+1}\), while reflection is \(r^as(e_j)=e_{a-j-1}\); on spoke labels it is \(j\mapsto a-j\). The chain argument uses the augmented simplicial chain complex, counting the empty face with alternating degree \(-1\). Homology characters and quotient are rational, not integral group-module classifications or equivariant homotopy statements.

## Proof
**1. Known homology concentration.** Theorem 5.2 of Vega [1] proves that ordinary wheel matching complexes are wedges of spheres, with exactly the above degrees and multiplicities after replacing her total-vertex parameter by our rim length plus one. Thus \(\widetilde L_{X_n}(g)=(-1)^{h_n}\chi_n(g)\) for every \(g\in D_n\). No equivariant wedge decomposition is assumed.

**2. Exact signed orbit formula.** Let \(Y=\operatorname{Ind}(H)\) be a finite independence complex and \(g\) a graph automorphism. Any setwise \(g\)-fixed independent set is a union of vertex orbits of \(g\), and a nonempty union of \(u\) orbits has signed augmented simplex trace \((-1)^{u-1}\): the orientation permutation has sign \((-1)^{|F|-u}\), and the simplex degree is \(|F|-1\). The empty face contributes \(-1\). Discard orbits containing adjacent vertices, and form the conflict graph \(B_g\) on the remaining orbits, joining two whenever an edge of \(H\) runs between them. With \(I(B,z)=\sum_{A\text{ independent in }B}z^{|A|}\), the exact reduced Lefschetz number is \(\widetilde L_Y(g)=-I(B_g,-1)\).

**3. Wheel decomposition, including signs.** An independent set of the wheel line graph either uses only rim edges or includes exactly one spoke \(\ell_j\), together with a set of rim edges that avoids \(e_{j-1},e_j\). The remaining rim-edge graph is the path \(P_{n-2}\). For a group element \(g\), a setwise-fixed face containing a spoke must use a *fixed spoke* \(\ell_j\), because two distinct spokes cannot coexist. The contribution from faces containing that spoke is the negative of the reduced Lefschetz sum of the action induced on its path link: adjoining the fixed spoke increases simplex dimension by one and adds no permutation sign. Therefore
\[
\widetilde L_{X_n}(g)=\widetilde L_{\operatorname{Ind}(C_n)}(g)
-\sum_{j:g(\ell_j)=\ell_j}\widetilde L_{\operatorname{Ind}(P_{n-2})}(g\mid\ell_j).
\tag{1}
\]
Equation (1) includes the empty-face sign correctly; in the spoke-containing portion only the nonempty faces appear and the corresponding link empty face has reduced degree \(-1\).

**4. Rotation calculation.** For a nonidentity \(r^a\), \(d=\gcd(n,a)\) determines the orbits of the rim-edge indices as residue classes modulo \(d\). All spokes form nonfixed orbits and cannot occur. For \(d\ge3\), the admissible orbit conflict graph is \(C_d\); for \(d=2\), it is an edge, and for \(d=1\) it is empty (the sole orbit contains adjacent vertices). These three cases give the uniform \(I(B_{r^a},-1)=q_d\). One obtains \(I(C_d,-1)=2\cos(\pi d/3)\) for \(d\ge3\) from the path deletion recurrence or direct cycle transfer matrix. Hence \(\widetilde L_{X_n}(r^a)=-q_d\). The identity trace is the previously proved rank \(b_n\). Both cases yield the displayed rotation character.

**5. Reflection calculation.** Write \(p_m=I(P_m,-1)\) with \(p_0=1\), \(p_1=0\), \(p_m=p_{m-1}-p_{m-2}\) for \(m\ge2\). It follows that \(p_{m+6}=p_m\) and \(p_{m+3}=-p_m\). In each reflection, rim-edge labels transform by \(j\mapsto a-j-1\), while spoke labels transform by \(j\mapsto a-j\).

For odd \(n=2m+1\), the reflection has one fixed spoke. The admissible rim-edge orbits form the path \(P_m\); the induced action on the \(P_{n-2}\) link of its fixed spoke also has admissible orbit graph \(P_m\). Their contributions to (1) are \(-p_m-(-p_m)=0\). Thus all odd-rim reflection traces vanish.

For even \(n=2m\), if \(a\) is even there are two fixed spokes and no fixed rim edges. Two end orbit-pairs of rim edges contain adjacent edges, leaving the admissible orbit path \(P_{m-2}\). Each fixed spoke has a reversed link \(P_{2m-2}\) whose admissible orbit graph is also \(P_{m-2}\). Thus (1) gives \(-p_{m-2}-2(-p_{m-2})=p_{m-2}\). If \(a\) is odd there is no fixed spoke and there are two fixed rim edges; their admissible orbits form \(P_{m+1}\). The reduced Lefschetz number is \(-p_{m+1}=p_{m-2}\) by \(p_{j+3}=-p_j\). This proves the same reflection formula for both conjugacy classes. Multiplying by \((-1)^{h_n}\) gives \(\chi_n\).

**6. Quotient congruences.** Barycentric subdivision removes inversions in the simplicial action, and averaging over \(\mathbb Q\) identifies quotient homology with \(D_n\)-invariants. Their dimension is \((2n)^{-1}\sum_{g\in D_n}\chi_n(g)\). To evaluate the rotation part, set \(\varepsilon_n=(1-\mathbf1_{2\mid n})(1-\mathbf1_{3\mid n})\). The cycle values satisfy \(q_d=1-2\mathbf1_{2\mid d}-3\mathbf1_{3\mid d}+6\mathbf1_{6\mid d}\); direct residue counting gives
\[
\sum_{a=0}^{n-1}q_{\gcd(n,a)}=n\varepsilon_n.
\]
At the identity, the wheel’s reduced Lefschetz number differs from the rim-cycle value by \(n p_{n-2}\), by (1). Therefore the dimension of the rotation-invariant rational homology equals
\[
R_n=(-1)^{h_n}\left(p_{n-2}-\varepsilon_n\right)
=\begin{cases}0,&n\equiv0,1,3\pmod6,\\1,&n\equiv2,4\pmod6,\\2,&n\equiv5\pmod6.\end{cases}
\]
For odd \(n\), reflections contribute zero, so the dihedral-invariant dimension is \(R_n/2\). For even \(n\), each of the \(n\) reflections contributes \((-1)^{h_n}p_{n/2-2}\), so the dihedral-invariant dimension is \((R_n+(-1)^{h_n}p_{n/2-2})/2\). Substitution of the period-six sequence proves exactly the four residue classes stated above, including all small \(n\ge3\).

## Verification
The companion standard-library script `code/verify_wheel_character.py` constructs wheel matchings directly from their edges, independently applies each of the \(2n\) geometric edge permutations, and sums **signed** traces of setwise-fixed oriented simplices, including the reduced empty-face contribution. For each \(3\le n\le16\), it exhausts every matching and every group element, comparing all \(266\) exact character values with the theorem. It also checks integer character averages and the quotient congruences for \(3\le n\le240\). Execution records are in `verification/character_checks.txt`. These experiments test signs, base cases, and formulas; the unbounded claim is established by the preceding orbit-counting proof and the previously proved homology-concentration theorem.

## Relationship to prior work
Vega [1, Theorem 5.2] already gives the **full ordinary nonequivariant homotopy type of wheel matching complexes**; those ranks and wedge dimensions are reused, not claimed new. Bayer–Jelić Milutinović–Vega [2] gives broader outerplanar matching-complex homotopy techniques and notes wheels as known nonouterplanar planar examples, not a wheel homology symmetry character. A published calculation [4] gives the **full character of the cycle matching complex**; its rim contribution and orbit formalism overlap, but it does not include the \(n\) mutually conflicting spokes, the fixed-spoke correction in (1), the parity-class cancellation, or the wheel quotient residues. Another calculation [5] studies **wheel discrete-Morse complexes**, whose vertices are oriented vertex–edge incidences and whose Betti rank is cubic in rim size; it is not the ordinary edge-matching complex and cannot imply the present formula. A second cycle computation [6] likewise omits the wheel spokes. These comparisons assess implication, not just titles.

## Limitations
The result computes rational homology representations and rational reduced Betti numbers of orbit spaces; it does not classify integral \(\mathbb Z[D_n]\)-lattices, quotient homotopy types, fixed-point spaces, Borel-equivariant cohomology, or integral torsion of quotients. The nonequivariant homology concentration is a verified literature input, not reproved here. The verifier is finite and cannot by itself prove the theorem for all rim lengths. An equivalent treatment might remain in unindexed publications or a more general equivariant transfer theorem, so the originality comparison is not proof of universal priority.

## References
1. Julianne Vega, *2-matching complexes*, arXiv:1909.10406v2, Theorem 5.2 and proof, https://arxiv.org/html/1909.10406v2 (public version 2021-01-28; earlier first submission 2019).
2. Margaret Bayer, Marija Jelić Milutinović and Julianne Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v1, first public 2024-11-07, Theorem 2 and planar examples; https://arxiv.org/html/2411.04601v2.
3. C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780v1 (2022-07-27), https://arxiv.org/abs/2207.13780 (related methods for matching-complex homotopy).
4. *Complete dihedral homology characters of cycle matching complexes*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-dihedral-homology-characters-of-cycle-matching-complexe--5aa60c866f1d.
5. *Dihedral top homology of wheel discrete-Morse complexes*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-dihedral-top-homology-of-wheel-discrete-morse-complexes--07726f70cc8e.
6. *Dihedral homology characters and quotient congruences for cycle matching complexes*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-dihedral-homology-characters-and-quotient-congruences-for-cycle--6d9fbe47cba0.
