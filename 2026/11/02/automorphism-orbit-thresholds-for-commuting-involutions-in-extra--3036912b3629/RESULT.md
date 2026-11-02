# Automorphism-orbit thresholds for commuting involutions in extraspecial \(2\)-groups

## Finding
For each integer \(m\ge1\), let \(G_\epsilon=2_\epsilon^{1+2m}\) be an extraspecial group of order \(2^{2m+1}\), where \(\epsilon=+\) or \(-\) denotes its quadratic (Arf) type. For every integer \(r\ge0\), set
\[
X_r(G_\epsilon)=\operatorname{Hom}((C_2)^r,G_\epsilon),\qquad
\mathcal O_\epsilon(m,r)=\#(\operatorname{Aut}(G_\epsilon)\backslash X_r(G_\epsilon)).
\]
Write \(w_+=m\) and \(w_-=m-1\); denote by \({r\brack d}_2\) the Gaussian binomial coefficient over \(\mathbb F_2\). Then
\[
\boxed{\mathcal O_\epsilon(m,r)=\sum_{d=0}^{\min(r,w_\epsilon)}2^{r-d}{r\brack d}_2.}
\]
An individual orbit is completely determined by a pair \((K,\chi)\), where \(K\le (C_2)^r\) has codimension \(d\le w_\epsilon\) and \(\chi:K\to C_2\) is a group homomorphism. More precisely, for \(\varphi\in X_r(G_\epsilon)\), take the induced projection \(\bar\varphi:(C_2)^r\to G_\epsilon/Z(G_\epsilon)\), put \(K=\ker\bar\varphi\), and identify \(\chi=\varphi|_K\) with a central character. Every such pair occurs and two maps are automorphism-equivalent precisely when their pairs agree.

Consequently, for \(r<m\), the two types have the same orbit number, whereas for every \(r\ge m\),
\[
\boxed{\mathcal O_+(m,r)-\mathcal O_-(m,r)=2^{r-m}{r\brack m}_2.}
\]
In particular, \(r=m\) is the **first rank at which these automorphism-orbit invariants distinguish the two types**, with a difference of exactly one orbit. This delayed separation concerns **orbit counts**, not raw involution counts (which already distinguish the types at rank one).

A compatible formula for the total number of homomorphisms is
\[
|X_r(G_\epsilon)|=2^r\sum_{d=0}^{\min(r,w_\epsilon)}T_\epsilon(m,d)\prod_{j=0}^{d-1}(2^r-2^j),
\]
where empty products equal one and
\[
T_+(m,d)={m\brack d}_2\prod_{j=0}^{d-1}(2^{m-j-1}+1),\qquad
T_-(m,d)={m-1\brack d}_2\prod_{j=0}^{d-1}(2^{m-j}+1).
\]
The relevant domain is \(0\le d\le w_\epsilon\); otherwise \(T_\epsilon(m,d)=0\). These \(T_\epsilon\) are the classical counts of totally singular subspaces of dimension \(d\), included to give the full rank-refined count rather than asserted as independently new formulas.

## Assumptions and scope
All groups are finite. For an extraspecial \(2\)-group \(G\), its center \(Z=Z(G)=G'\) has order two; write its nonidentity element as \(z\). The quotient \(V=G/Z\) is a \(2m\)-dimensional vector space over \(\mathbb F_2\). The squaring map defines a nondegenerate quadratic form \(q:V\to\mathbb F_2\) by \(\tilde v^2=z^{q(v)}\); its polar form \(b(u,v)=q(u+v)+q(u)+q(v)\) is the nondegenerate commutator form: \([\tilde u,\tilde v]=z^{b(u,v)}\). The plus type has Witt index \(m\), the minus type Witt index \(m-1\). The source \((C_2)^r\) is an **ordered/labeled** vector space (its own automorphisms are **not** quotiented out). The acting group is the full \(\operatorname{Aut}(G)\), not merely conjugation by \(G\). The theorem includes \(r=0\), with one trivial homomorphism and one orbit.

## Proof
**Step 1: projected images are totally singular, and every such image lifts.** Let \(E=\mathbb F_2^r\) and \(\varphi:E\to G\) be a homomorphism. Every \(\varphi(x)\) is an involution (identity allowed), hence \(q(\bar\varphi(x))=0\). Because \(E\) is abelian, \(b(\bar\varphi(x),\bar\varphi(y))=0\) for all \(x,y\); thus \(U=\bar\varphi(E)\) is totally singular. Its dimension \(d\) is at most \(w_\epsilon\). Conversely, if \(U\le V\) is totally singular, choose lifts of a basis \(u_1,\dots,u_d\). They square to one and commute, generating an elementary abelian subgroup; the choice of their central multiples is arbitrary. Therefore any linear map \(E\to U\) lifts to a homomorphism \(E\to G\), with exactly \(2^r\) lifts (one independent central choice per source basis vector).

**Step 2: the automorphism group acts through the full orthogonal group.** Each automorphism of \(G\) fixes \(z\) and induces an isometry of \((V,q)\). Conversely, choose a quadratic basis \(\bar g_1,\ldots,\bar g_{2m}\) of \(V\) with representatives in \(G\). Their squares, commutators, and \(z\) form a presentation of \(G\). For any \(L\in O(V,q)\), lifts of \(L\bar g_i\) satisfy the same square and commutator relations; sending \(g_i\) to these lifts and \(z\) to \(z\) defines an automorphism. Thus \(\operatorname{Aut}(G)\to O(V,q)\) is surjective. Its kernel consists of the central twists \(g\mapsto g z^{\lambda(\bar g)}\) with \(\lambda\in V^*\). By nondegeneracy of \(b\), any such twist is conjugation by a lift of an appropriate \(t\in V\). In particular the central twists act as all linear functionals on every subspace \(U\le V\).

**Step 3: invariant pairs classify orbits.** Let \(K=\ker\bar\varphi\) and \(\chi=\varphi|_K\in\operatorname{Hom}(K,Z)\). Both are invariant under postcomposition by any automorphism: the induced quotient map is invertible and \(Z\) is fixed pointwise. Suppose \(\varphi,\psi:E\to G\) give the same \((K,\chi)\). The rule \(\bar\varphi(x)\mapsto\bar\psi(x)\) defines a linear isomorphism of their image subspaces; as both subspaces are totally singular, it preserves \(q\) and \(b\). By Witt's extension theorem for nonsingular quadratic spaces, it extends to \(L\in O(V,q)\). By Step 2, an automorphism realizing \(L\) changes \(\varphi\) so its projection agrees with that of \(\psi\). Now the pointwise discrepancy is a central linear character \(\delta:E\to Z\). Since both original maps agree on \(K\), \(\delta|_K=0\), so \(\delta\) factors as a linear functional on \(U\). Again Step 2 provides an inner automorphism that induces this central twist. Thus \(\varphi\) and \(\psi\) lie in the same orbit.

Conversely, any subspace \(K\le E\) of codimension \(d\le w_\epsilon\) occurs by choosing a quotient map \(E/K\cong U\) onto a fixed totally singular \(d\)-space \(U\). Its central character can be prescribed arbitrarily on \(K\) by choosing a vector-space complement \(E=K\oplus L\), assigning lifts of a basis of \(U\) to the basis of \(L\), and setting the restriction on \(K\) equal to \(\chi\). This proves existence and completeness.

**Step 4: orbit count and type-separation threshold.** There are \({r\brack d}_2\) possible codimension-\(d\) subspaces \(K\) and \(2^{\dim K}=2^{r-d}\) characters \(\chi:K\to Z\). Summing for \(0\le d\le\min(r,w_\epsilon)\) gives the displayed orbit formula. Both types have identical summands for \(d\le m-1\). The plus type alone contributes the \(d=m\) term when \(r\ge m\); hence the sharp threshold and difference formula.

**Step 5: raw homomorphism counts.** For any fixed totally singular \(d\)-space \(U\), the number of surjective linear maps \(E\to U\) equals \(\prod_{j=0}^{d-1}(2^r-2^j)\), and each has \(2^r\) central lifts by Step 1. The number of possible \(U\) is \(T_\epsilon(m,d)\). To derive the stated classical formulas, count ordered bases of totally singular \(d\)-spaces recursively. If an isotropic \(j\)-space \(W\) has been chosen, the induced quadratic space \(W^\perp/W\) has dimension \(2(m-j)\) and the same orthogonal type. Its number of nonzero singular vectors is \(2^{2(m-j)-1}+\epsilon 2^{m-j-1}-1\), where \(\epsilon\) is numerically \(+1\) or \(-1\). Every such vector has \(2^j\) lifts in \(W^\perp\), giving the number of admissible next basis vectors. Divide the product over \(j\) by \(|\operatorname{GL}_d(\mathbb F_2)|=\prod_{j=0}^{d-1}(2^d-2^j)\). Simplification gives \(T_+\) and \(T_-\) as displayed. This counts all homomorphisms with no overlap between different image subspaces.

## Verification
The standalone file `verify_extraspecial_involution_orbits.py` constructs the plus and minus extraspecial groups of orders \(8\) and \(32\) from their multiplication laws (without invoking an external algebra system). For each type and \(r=1,2,3\), it enumerates all commuting involution tuples, all quadratic isometries of the quotient, the induced group automorphisms and central twists, and computes the actual automorphism orbits by a union-find graph search. It independently evaluates both closed formulas and checks that the proposed \((K,\chi)\)-invariant is constant on each orbit and separates distinct orbits.

Reproduce with `python3 verify_extraspecial_involution_orbits.py` using Python 3 and only the standard library. All twelve instances returned `PASS` and the final line was `VERIFY_OK`. For \(m=2\), the orbit counts for \(r=1,2,3\) are respectively \((3,11,50)\) for plus type and \((3,10,36)\) for minus type. These finite checks are corroborations, not a proof for arbitrary \(m,r\); the universal proof is given above.

## Relationship to prior work
Levit and Shwartz (2026, arXiv:2605.02071v1 and arXiv:2605.17171v1) study higher commuting probabilities \(\operatorname{Hom}(\mathbb Z^r,G)\) and **inner-conjugacy** orbits. Their work motivates examining a more constrained source and more extensive symmetry action. Here the source is \((C_2)^r\), forcing involution constraints and the quadratic refinement, and the acting group is the **full** automorphism group. Their symplectic/Heisenberg counts do not give the stated parameterized orbit classification or the Arf-type threshold. Classical extraspecial-group theory supplies the quadratic model and orthogonal quotient, and classical finite orthogonal geometry supplies the totally singular subspace numbers; those ingredients are not independently claimed as new. The combination yields an exact full-automorphism orbit profile, including the central-kernel-character invariant.

## Limitations
The orbit theorem is proved for extraspecial \(2\)-groups, not arbitrary special \(2\)-groups or odd-prime groups. The rank threshold distinguishes the *number of full-automorphism orbits*, not the raw count of homomorphisms. The closed subspace-count expressions are classical. Older literature on elementary abelian subgroups of extraspecial groups and their fusion may imply parts of the classification; no absolute historical-priority claim is made. Independent external mathematical audit has not been performed.

## References
1. V. E. Levit and R. Shwartz, *Higher Commutativity in Finite Groups: Exact Asymptotics and Finite Spectrum*, arXiv:2605.02071v1 (first public 2026-05-03), https://arxiv.org/abs/2605.02071 .
2. V. E. Levit and R. Shwartz, *Higher Commutativity in Finite Groups, Rigidity, Extremal bounds, and Heisenberg-Type Families*, arXiv:2605.17171v1 (first public 2026-05-16), https://arxiv.org/abs/2605.17171 .
3. Classical results: Witt's extension theorem for nondegenerate quadratic forms; structure of extraspecial \(2\)-groups and orthogonal groups; counts of totally singular subspaces in finite orthogonal spaces. A background description is accessible at https://finitegroupdatabase.com/c/extraspecial .
4. D. Quillen, *The mod 2 cohomology rings of extra-special 2-groups and the spinor groups*, Math. Ann. 194 (1971), 197–212. This is related prior background on elementary abelian subgroup geometry, not asserted to lack orbit-profile consequences.
