# Middle-tier cardinality governs reductivity in three-level Hibi toric varieties

## Finding
Let \(P=A\oplus C\oplus B\) be the ordinal sum of antichains of sizes \(a\), \(c\), and \(b\), with \(a,b\ge2\) and \(c\ge1\). Let \(X_P\) be the complex projective toric variety of the order polytope \(\mathcal O(P)\), and write \(\epsilon_z\) for a standard character-lattice basis vector indexed by a poset element \(z\). Set \(d=a+b+c\).

**Theorem (middle-tier symmetry transition).** The complete set \(\mathcal R(X_P)\) of Demazure roots is
\[
\mathcal R(X_P)=
\begin{cases}
\{\pm\epsilon_z:z\in A\cup B\},&c=1,\\
\{\epsilon_u:u\in A\}\cup\{-\epsilon_w:w\in B\},&c\ge2.
\end{cases}
\]
Consequently, for \(c=1\) the connected algebraic automorphism group is reductive, with semisimple root system of type \(A_1^{a+b}\) and dimension \(3(a+b)+1\). For \(c\ge2\), it has no semisimple roots and
\[
\operatorname{Aut}(X_P)^\circ\simeq
\mathbb G_a^{a+b}\rtimes\mathbb G_m^{a+b+c},
\qquad
\dim \operatorname{Aut}(X_P)^\circ=2(a+b)+c.
\]
The torus action in this semidirect product is by the indicated Demazure characters. In particular, replacing a singleton middle antichain by one of size two changes the connected group from reductive to nonreductive. At \(a=b=2\), the dimension decreases from \(13\) to \(10\), even as \(\dim X_P\) increases from \(5\) to \(6\).

## Assumptions and scope
All varieties and groups are over \(\mathbb C\). The order polytope is the full-dimensional lattice polytope
\[
\mathcal O(P)=\left\{(x_z)_{z\in P}\in\mathbb R^d:\quad
0\le x_u\le x_v\le x_w\le1\quad
(u\in A,v\in C,w\in B)\right\}.
\]
Its normal fan is complete. Its lattice of normal-fan rays is \(N=\mathbb Z^P\), with dual character lattice \(M=\mathbb Z^P\); \(\epsilon_z\) denotes the natural basis of \(M\). The theorem concerns the identity component of the abstract algebraic automorphism group, not only automorphisms preserving the toric embedding. It does not determine the disconnected components.

## Proof
**1. Facets and primitive rays.** All defining inequalities are consequences of the following facet inequalities: \(x_u\ge0\) for \(u\in A\); \(x_w\le1\) for \(w\in B\); \(x_u\le x_v\) for \((u,v)\in A\times C\); and \(x_v\le x_w\) for \((v,w)\in C\times B\). None is redundant: for each selected inequality, choose a point making it an equality while placing all other comparable coordinates at strictly separated nearby levels. For example, to make only \(x_u\le x_v\) an equality, assign their common value near \(1/2\), all other lower coordinates slightly below it, all other middle coordinates slightly above it, and all upper coordinates higher still. The analogous construction works for the other types. Thus the primitive outward rays of the normal fan are exactly
\[
-e_u\ (u\in A),\quad e_w\ (w\in B),\quad
p_{uv}=e_u-e_v\ (u\in A,v\in C),\quad
q_{vw}=e_v-e_w\ (v\in C,w\in B),
\]
where \(e_z\) are the standard basis vectors of \(N\). 

**2. Root criterion.** A character \(m\in M\) is a Demazure root precisely if its pairing with one primitive ray equals \(-1\), while its pairing with every other ray is nonnegative. This criterion and the connected-automorphism dimension formula are general toric results [1, Definition 2.1 and Proposition 2.2]. We exhaust the four possible distinguished ray types.

**3. A lower-boundary ray.** Suppose the distinguished ray is \(-e_u\) for \(u\in A\). Then \(m_u=1\), all other lower coordinates are at most zero, all upper coordinates are at least zero, and all cover inequalities give \(m_{u'}\ge m_v\ge m_w\) except for the distinguished boundary inequality. For any \(v\in C\) and \(w\in B\), choose \(u'\in A\setminus\{u\}\). It follows that \(0\ge m_{u'}\ge m_v\ge m_w\ge0\). Thus every coordinate other than \(m_u\) is zero. Conversely, \(\epsilon_u\) satisfies the root criterion for the ray \(-e_u\).

**4. An upper-boundary ray.** The order-dual argument, using \(b\ge2\), shows that a root distinguished at \(e_w\) is exactly \(-\epsilon_w\) for \(w\in B\). Every such vector satisfies the criterion.

**5. A lower-to-middle cover ray.** Suppose \(e_u-e_v\) is distinguished. As in step 3, choose a different lower vertex \(u'\in A\setminus\{u\}\). All paths \(u'\to v'\to w\), with \(v'\in C\) and \(w\in B\), avoid the distinguished ray. Hence \(0\ge m_{u'}\ge m_{v'}\ge m_w\ge0\), forcing all middle and upper coordinates and all lower coordinates other than \(m_u\) to vanish. The distinguished equation gives \(m_u=-1\). If \(c\ge2\), choosing \(v'\ne v\) forces \(m_u-m_{v'}=-1<0\), contradicting the nondistinguished cover inequality. If \(c=1\), no such second cover exists and \(-\epsilon_u\) satisfies every other ray inequality. Hence this ray contributes \(-\epsilon_u\) exactly for \(c=1\).

**6. A middle-to-upper cover ray.** Suppose \(e_v-e_w\) is distinguished. Choose \(w'\in B\setminus\{w\}\). All paths \(u\to v'\to w'\), with \(u\in A\) and \(v'\in C\), avoid the distinguished cover, yielding \(0\ge m_u\ge m_{v'}\ge m_{w'}\ge0\). All lower and middle coordinates and all upper coordinates except \(m_w\) therefore vanish. The distinguished equation gives \(m_w=1\). For \(c\ge2\), another middle element \(v'\ne v\) makes \(m_{v'}-m_w<0\), impossible at its nondistinguished cover ray. For \(c=1\), \(\epsilon_w\) satisfies all inequalities. This exhausts all roots.

**7. Algebraic group consequences.** When \(c=1\), each listed root comes with its negative; all are semisimple and independent coordinate pairs, giving root system \(A_1^{a+b}\). Demazure's structure theorem gives reductivity. When \(c\ge2\), none has its negative, and the distinct root subgroups are pairwise orthogonal in the ray-root pairing (each root vanishes on every other root's distinguished ray), so they commute. The connected group is the stated semidirect product of the \(d\)-dimensional torus and \(a+b\) additive groups. For any complete toric variety, its connected group dimension is \(d+|\mathcal R|\) [1]; substituting the two exact root cardinalities proves the formulas.

## Verification
The bundled `three_tier_roots_check.py` constructs the primitive rays independently from the inequalities, enumerates integer characters in \([-2,2]^d\), applies the distinguished-ray criterion, and compares the resulting exact sets against the theorem for ten triples with \(a,b\ge2\) and \(c\in\{1,2,3\}\). All ten checks pass. The output is bundled as `three_tier_roots_check_output.txt`. These tests are bounded regression checks; the exhaustive symbolic proof above covers every allowed integer parameter and all integer characters.

## Relationship to prior work
Nill [1] states the general complete-toric Demazure root criterion, the dimension formula, and reductivity equivalence. It does **not** evaluate these for the three-tier order-polytope normal fans. Lakshmibai and Mukherjee [2] study Hibi toric varieties, their affine cones, and singular loci, rather than connected automorphism groups of this three-parameter projective family. Biswal and Fourier [3] study order and chain polytopes in toric degenerations of minuscule Schubert varieties, not the present root bifurcation. Thus the input construction and general mechanism are prior work; the special-family root classification and the singleton-versus-multiple middle-tier group transition are the assessed claim. Literature coverage remains subject to independent review.

## Limitations
The result does not identify all components of the full (possibly disconnected) automorphism group or provide a presentation of the derived reductive group up to its finite central isogenies when \(c=1\). No assertion is made about posets outside the stated three-tier ordinal-sum family. A matching equivalent specialization in unindexed literature remains possible. No independent audit has been performed.

## References
[1] B. Nill, *Complete toric varieties with reductive automorphism group*, arXiv:math/0407491v1, first public posting 2004-07-28, especially §2, Definition 2.1 and Proposition 2.2; https://arxiv.org/abs/math/0407491.

[2] V. Lakshmibai and H. Mukherjee, *Singular Loci of Hibi toric varieties*, arXiv:0706.2686v1, first public posting 2007-06-18, especially §4 and Theorems 4.5 and 6.9; https://arxiv.org/abs/0706.2686.

[3] R. Biswal and G. Fourier, *Minuscule Schubert varieties: Poset polytopes, PBW-degenerated Demazure modules, and Kogan faces*, arXiv:1410.1126, first public posting 2014-10-05, especially §§1 and 4; https://arxiv.org/abs/1410.1126.
