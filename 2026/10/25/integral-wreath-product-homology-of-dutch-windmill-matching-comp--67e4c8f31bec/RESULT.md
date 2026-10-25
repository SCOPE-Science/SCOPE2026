# Integral wreath-product homology of Dutch windmill matching complexes

## Finding
For integers \(n\ge2\) and \(m\ge3\), let \(D_m^n\) be the graph formed by identifying one vertex in each of \(n\) copies of the cycle \(C_m\). Let \(X_m^n=\mathcal M(D_m^n)\) be its ordinary matching complex: vertices are graph edges and simplices are pairwise vertex-disjoint edge sets. The entire graph automorphism group is
\[
G_n=(C_2)^n\rtimes S_n.
\]
An element \(g=(\pi,\epsilon)\), with \(\epsilon=(\epsilon_1,\ldots,\epsilon_n)\in\{0,1\}^n\), permutes the petals by \(\pi\) and reverses the cyclic coordinate in source petal \(i\) when \(\epsilon_i=1\). Write \(e(\epsilon)=\sum_i\epsilon_i\). Let \(\Omega\) be the natural \(G_n\)-set of the \(2n\) graph edges incident with the common vertex; write \(\operatorname{Aug}\mathbb Z[\Omega]=\ker(\mathbb Z[\Omega]\xrightarrow{\sum}\mathbb Z)\). For a sign character \(\alpha\), let \(\mathbb Z_\alpha\) be its rank-one integral module.

**Complete integral classification.** If \(m=3k\), with \(k\ge1\), then \(X_m^n\) is contractible. If \(m=3k+1\), with \(k\ge1\), put
\[
\alpha_{n,k}(g)=(\operatorname{sgn}\pi)^k(-1)^{\lceil k/2\rceil e(\epsilon)}.
\]
Then the only nonzero reduced integral homology is
\[
\widetilde H_{nk-1}(X_{3k+1}^n;\mathbb Z)\cong\mathbb Z_{\alpha_{n,k}}.
\]
If \(m=3k+2\), with \(k\ge1\), put
\[
\beta_{n,k}(g)=(\operatorname{sgn}\pi)^k(-1)^{\lfloor k/2\rfloor e(\epsilon)}.
\]
Then the only nonzero reduced integral homology is
\[
\boxed{\widetilde H_{nk}(X_{3k+2}^n;\mathbb Z)\cong
\mathbb Z_{\beta_{n,k}}\otimes\operatorname{Aug}\mathbb Z[\Omega].}
\]
These are natural isomorphisms of integral \(\mathbb Z[G_n]\)-modules; there is no torsion. In the last case the complete rational character is
\[
\chi(g)=\beta_{n,k}(g)(f_\Omega(g)-1),
\quad f_\Omega(g)=2\#\{i:\pi(i)=i,\ \epsilon_i=0\}.
\]

**Symmetry-quotient consequence.** The only possibly nonzero reduced rational Betti number of the full quotient \(|X_m^n|/G_n\) has dimension one exactly when either \(m=3k+1\) with \(4\mid k\), or \(m=3k+2\) with \(n=2\) and \(k\equiv1\pmod4\). It is zero in all other cases. For the subgroup \((C_2)^n\) of independent petal reflections, the top reduced rational Betti number in the \(m=3k+2\) case equals \(n-1\) when \(k\equiv0,1\pmod4\), and zero when \(k\equiv2,3\pmod4\). These quotient statements concern rational homology only.

## Assumptions and scope
All graph edges have no orientation; the sign actions arise from oriented *simplicial chains*. A petal is labeled cyclically from its common vertex, so the reflection in that petal exchanges its two center-incident edges. Since the center has degree \(2n>2\) and all other vertices have degree two, every graph automorphism fixes the center, permutes the \(n\) cycles, and may independently reverse each cycle. Thus \(G_n\) is the full automorphism group. All homology is reduced unless otherwise stated; assertions apply to every integer in the indicated ranges, not only to finite test cases.

For a path on \(r\) vertices, write \(I_r=\operatorname{Ind}(P_r)\), the simplicial complex of independent vertex subsets. Its standard homotopy calculation is
\[
I_{3t}\simeq S^{t-1},\quad I_{3t+1}\simeq *,\quad I_{3t+2}\simeq S^t
\]
for permissible nonnegative parameters, with \(I_0\) the \((-1)\)-sphere convention. Indeed, deleting the second path vertex gives a cone, its closed-neighborhood deletion is \(I_{r-3}\), and the two-cone decomposition yields \(I_r\simeq\Sigma I_{r-3}\) for \(r\ge3\). The base cases \(I_0,I_1,I_2\) complete the induction. In noncontractible cases the reduced integral homology is \(\mathbb Z\) in the displayed sphere degree.

## Proof
**1. Path-reflection orientation.** Let \(r\) reverse the vertices of the path \(P_N\). On the one nonzero reduced integral homology of \(I_N\), for \(N=3k-1\) and \(N=3k\), its degrees are respectively
\[
\deg(r|I_{3k-1})=(-1)^{\lceil k/2\rceil},\qquad
\deg(r|I_{3k})=(-1)^{\lfloor k/2\rfloor}.
\]
Here is an exact calculation, rather than an assumption about a nonequivariant sphere equivalence. Set \(F_0=1,F_1=0\), and \(F_j=F_{j-1}-F_{j-2}\), so \(F_j=\sum_{S\in I_j}(-1)^{|S|}\), with values \(1,0,-1,-1,0,1\) repeating every six indices. For convenience set \(F_{-1}=1\). In the augmented simplicial chain trace of a reflection, an invariant independent set comprising \(p\) exchanged pairs and \(c\in\{0,1\}\) central fixed vertices contributes \(-(-1)^{p+c}\) to the reduced Lefschetz number. If \(N=2h\), the innermost vertex pair is adjacent and forbidden, and the sum of \((-1)^{p+c}\) over invariant independent sets is \(T_N=F_{h-1}\). If \(N=2h+1\), including the center prohibits the innermost pair and gives \(T_N=F_h-F_{h-1}=-F_{h-2}\). Both relevant path complexes have homology only in degree \(k-1\); therefore the reflection degree equals \((-1)^kT_N\). Substituting \(N=3k-1\) or \(3k\) into the six-periodic recurrence proves the two stated formulas, including \(k=1\).

**2. The common-vertex-free subcomplex.** Fix the center \(c\), and let \(A\subseteq X_m^n\) consist of matchings using no edge incident with \(c\). The \(m-2\) remaining edges of each petal form the vertices of a path conflict graph. Hence
\[
A=I_{m-2}^{*n}.
\]
In the noncontractible cases \(m=3k+1\) and \(m=3k+2\), this is an integral homology sphere in degree \(nk-1\). Permuting two join factors of reduced homology degree \(k-1\) changes orientation by \((-1)^{k^2}=(-1)^k\). Independently reflecting petal \(i\) reverses that path's \(m-2\) vertices. By Step 1, the entire \(G_n\)-action on \(\widetilde H_{nk-1}(A;\mathbb Z)\cong\mathbb Z\) is \(\alpha_{n,k}\) when \(m=3k+1\) and \(\beta_{n,k}\) when \(m=3k+2\).

**3. Attach all center-edge cones.** Every matching contains at most one center-incident edge. For each \(s\in\Omega\), its link in \(A\) is
\[
L_s\cong I_{m-3}*I_{m-2}^{*(n-1)},
\quad X_m^n=A\cup\bigcup_{s\in\Omega}(s*L_s).
\]
Cones for distinct spokes meet only inside \(A\), so the relative quotient splits as a wedge of their suspended links.

If \(m=3k\), each \(I_{m-2}=I_{3k-2}\) is contractible; hence \(A\) and all \(L_s\) are contractible (using \(n\ge2\)). Successively attaching cones over contractible subcomplexes preserves contractibility. Thus \(X_m^n\simeq *\).

If \(m=3k+1\), then \(I_{m-3}=I_{3k-2}\) is contractible, so each \(L_s\) and each relative cone quotient is acyclic. The inclusion \(A\hookrightarrow X_m^n\) induces an integral homology isomorphism. Since the inclusion is \(G_n\)-equivariant, Step 2 gives precisely \(\mathbb Z_{\alpha_{n,k}}\) in degree \(nk-1\) and zero elsewhere.

If \(m=3k+2\), then \(I_{m-2}=I_{3k}\) and \(I_{m-3}=I_{3k-1}\) both have the homotopy type of \(S^{k-1}\). Moreover the natural endpoint-deletion inclusion \(I_{3k-1}\hookrightarrow I_{3k}\) is a homotopy equivalence: its mapping cone is a suspension of \(I_{3k-2}\), which is contractible. The join inclusion \(L_s\hookrightarrow A\) therefore induces an isomorphism on the unique nonzero reduced *integral* homology \(\mathbb Z\) in degree \(nk-1\).

The long exact sequence of \((X_m^n,A)\) contains the exact sequence
\[
0\longrightarrow\widetilde H_{nk}(X_m^n;\mathbb Z)
\longrightarrow\bigoplus_{s\in\Omega}\widetilde H_{nk-1}(L_s;\mathbb Z)
\xrightarrow{\partial}\widetilde H_{nk-1}(A;\mathbb Z)
\longrightarrow\widetilde H_{nk-1}(X_m^n;\mathbb Z)\longrightarrow0.
\]
The direct sum has \(2n\) copies of \(\mathbb Z\), and every coordinate maps by degree \(\pm1\) to the last \(\mathbb Z\). Fix a generator \(u\) of the latter and normalize each summand generator \(e_s\) so that \(\partial e_s=u\). Thus \(\partial\) is the augmentation \(\sum\), is surjective, and its kernel is the integral augmentation lattice. Under \(g\in G_n\), naturality forces \(g e_s=\beta_{n,k}(g)e_{gs}\), since both sides have boundary \(\beta_{n,k}(g)u\) and the corresponding rank-one relative summands map isomorphically to \(\mathbb Z\). This proves the asserted \(\mathbb Z[G_n]\)-module identification, torsion-freeness, and vanishing of all other reduced homology.

**4. Quotients.** For a finite simplicial group action, rational transfer after barycentric subdivision identifies quotient homology with group invariants. In the sphere case, \(\alpha_{n,k}\) is trivial on \(G_n\) exactly when \(4\mid k\). In the augmentation case, the \(G_n\)-set \(\Omega\) is transitive, with the stabilizer of a chosen spoke isomorphic to \((C_2)^{n-1}\rtimes S_{n-1}\). The multiplicity of \(\beta_{n,k}\) in \(\mathbb Q[\Omega]\) is one if this character is trivial on the stabilizer, and zero otherwise; passing to the augmentation kernel subtracts one when \(\beta_{n,k}\) is globally trivial. For \(n\ge3\), these contributions always cancel or vanish. For \(n=2\), one invariant survives exactly when \(k\equiv1\pmod4\). Restriction to the petal-reflection subgroup yields the additional stated \(n-1\)/zero dichotomy. The remaining homology groups vanish by the complete integral classification above.

## Verification
The included standalone Python 3 script `artifacts/verify.py` constructs graph edges and enumerates fixed-orbit matchings **without using the relative-cone construction**. For each tested automorphism it evaluates the signed reduced simplicial Lefschetz sum and compares with the claimed full-wreath character. The tests comprise 1,128 complete automorphism instances covering \(2\le n\le4\) and cycle lengths from 3 to 11, including all three congruence classes. Exact mod-two augmented boundary matrices independently check the complete reduced Betti profiles in 13 representative finite complexes (up to 43,658 faces). Character averaging checks 120 quotient cases. Execute `python3 artifacts/verify.py` in the package root and compare with `artifacts/verification_output.txt`; success markers are `WINDMILL_QUOTIENT_PREDICTIONS_VERIFIED 120` and `WINDMILL_FULL_WREATH_CHARACTER_VERIFIED 1128`. These finite computations are regression tests, not substitutes for the all-parameter integral proof in Steps 1–4.

## Relationship to prior work
Donovan and Scoville (first public arXiv version July 27, 2022; journal 2023), Theorem 5.8, prove exactly the *nonequivariant* homotopy-type trichotomy for Dutch windmill matching complexes. That prior classification, including ranks and dimensions, is not claimed as new here. The published record *Blade-permutation homology of Dutch windmill matching complexes* computes the **rational** representation restricted to the petal-permuting subgroup \(S_n\): \((\operatorname{sgn}\pi)^k\) in the sphere case and \((\operatorname{sgn}\pi)^k(2f(\pi)-1)\) in the wedge case. Restricting the present theorem to elements with no petal reflections recovers precisely those previously known characters; that agreement is not a new contribution. The present theorem instead identifies the complete **integral** module for the **full** automorphism group, including every independent within-petal reflection and the resulting modulo-four quotient consequences. Knowledge of the rational \(S_n\)-restriction does not determine these additional reflection actions or an integral lattice. A published branch-permutation augmentation-lattice result for discrete-Morse complexes of two-edge-arm trees uses a related long-exact-sequence strategy, but has different complexes and no Dutch windmill within-petal reflection action.

## Limitations
The displayed integral isomorphisms are module identifications, not canonical choices of generator; choosing an orientation of \(A\) is necessary to normalize the relative generators. They do not assert an equivariant simple-homotopy equivalence or integral homology of the quotient. Nontrivial torsion may occur in quotient homology even when the rational groups vanish. Only matching complexes of equal-length cycle bouquets with at least two petals are treated. Although the primary and closest published statements have been inspected, an unindexed equivalent full-wreath formulation cannot be categorically ruled out. No independent mathematical audit has been performed.

## References
1. Connor Donovan and Nicholas A. Scoville, “Star clusters in the matching, Morse, and generalized complex of discrete Morse functions,” *New York Journal of Mathematics* 29 (2023), 1393–1412, Theorem 5.8. arXiv:2207.13780 (first public July 27, 2022). https://nyjm.albany.edu/j/2023/29-54v.pdf
2. “Blade-permutation homology of Dutch windmill matching complexes,” published research record (2026), identifier `4a7f2d144faf`. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-blade-permutation-homology-of-dutch-windmill-matching-complexes--4a7f2d144faf
3. “Integral branch-permutation homology of extended-star Morse complexes,” published research record (2026), identifier `348812728b63`. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-integral-branch-permutation-homology-of-extended-star-morse-comp--348812728b63
