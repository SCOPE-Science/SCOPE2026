# Symplectic parametrization and central-fiber counts for group Rota–Baxter operators

## Finding
Let \(p\) be an odd prime and \(n\ge 2\). Let \((V,\omega)\) be a \(2n\)-dimensional symplectic vector space over \(\mathbb F_p\). Write the exponent-\(p\) extraspecial group as
\[
G=V\times\mathbb F_p,\qquad
(v,z)(w,t)=(v+w,z+t+\tfrac12\omega(v,w)).
\]
A group Rota–Baxter operator is any map \(B:G\to G\) such that \(B(g)B(h)=B(gB(g)hB(g)^{-1})\) for all \(g,h\in G\); no linearity is assumed.

**Complete operator parametrization.** Every such operator, uniquely and without quotienting by automorphisms, has the form
\[
B_{L,\alpha,\ell}(v,z)
 =\bigl(Lv,\ \alpha z+\ell(v)-\tfrac{\alpha}{2}\omega(Lv,v)\bigr),
\]
where \(\alpha\in\mathbb F_p\), \(\ell\in V^*\), and \(L\in\operatorname{End}_{\mathbb F_p}(V)\) satisfies the explicit symplectic matrix condition
\[
\boxed{\quad
\omega(Lv,Lw)=\alpha\bigl(\omega(v,w)+\omega(Lv,w)+\omega(v,Lw)\bigr)
\quad(v,w\in V).\quad}
\tag{1}
\]
Conversely each triple meeting (1) yields a group Rota–Baxter operator.

**Two exactly counted central-action fibers.** The action of \(B\) on \(Z(G)\) is multiplication by \(\alpha\). For \(\alpha=0\), (1) is equivalent to \(\operatorname{im}L\) being totally isotropic; for \(\alpha=-1\), it is equivalent to \(\operatorname{im}(I+L)\) being totally isotropic. Define \(r=\operatorname{rank}L\) in the first fiber and \(r=\operatorname{rank}(I+L)\) in the second. For each \(0\le r\le n\), the number of operators in either fiber with this indicated rank is exactly
\[
\boxed{
N_{p,n,r}=p^{2n}\binom{n}{r}_{p}
\left(\prod_{j=0}^{r-1}(p^{n-j}+1)\right)
\left(\prod_{i=0}^{r-1}(p^{2n}-p^i)\right),
}
\tag{2}
\]
where \(\binom{n}{r}_{p}=\prod_{i=0}^{r-1}(p^{n-i}-1)/(p^{r-i}-1)\) is the Gaussian binomial coefficient and empty products are \(1\). Thus both fibers have the same total size \(\sum_{r=0}^n N_{p,n,r}\). For example, at \(p=3,n=2\), each fiber has exactly \(20{,}476{,}881\) operators.

**Balanced-rank locus for the other central actions.** If \(\alpha\notin\{0,-1\}\), then the operators with \(\operatorname{rank}L=\operatorname{rank}(I+L)=n\) are precisely those with \(L=-P_U\), where \(V=U\oplus W\) is an ordered decomposition into complementary Lagrangian subspaces and \(P_U\) is the projection onto \(U\) along \(W\). Their exact number, for each fixed such \(\alpha\), is
\[
\boxed{p^{2n+n(n+1)/2}\prod_{i=1}^n(p^i+1).}
\tag{3}
\]
This is a rank-stratum count, not a closed count of all operators with the remaining central actions.

## Assumptions and scope
The field is the prime field \(\mathbb F_p\), with \(p\ge3\), and \(n\ge2\). Every exponent-\(p\) extraspecial group of order \(p^{2n+1}\) is isomorphic to the displayed central extension because its commutator form is nondegenerate alternating. The coordinates use an arbitrary fixed symplectic identification; equations and counts are invariant under changing it. The statement concerns group Rota–Baxter operators of weight \(1\), not linear Rota–Baxter operators on a group algebra. A previous classification handles the dimension-three group; the new family starts at order \(p^5\).

## Proof
**Center preservation without a linearity assumption.** First \(B(1)=1\) by the defining identity. If \(z\in Z(G)\), then for any \(g\in G\), \(B(gz)=B(g)B(z)\), since conjugating \(z\) does nothing. In particular, \(B|_{Z(G)}\) is a homomorphism. Put \(a=B(z)\). Using the identity first on \((z,g)\), then on \((g,z[a,g])\), where \([a,g]=aga^{-1}g^{-1}\in Z(G)\), gives
\[
aB(g)=B(zaga^{-1})=B(g)\,a\,B([a,g]).
\]
Consequently \(B([a,g])=(B(g)a)^{-1}aB(g)\in Z(G)\), since \(G\) has class two. If \(a\) were noncentral, nondegeneracy of the commutator pairing would make \(g\mapsto[a,g]\) surjective onto the order-\(p\) center, forcing \(B(Z(G))\subseteq Z(G)\), contradicting \(a\notin Z(G)\). Thus \(B(Z(G))\subseteq Z(G)\), and \(B(0,z)=(0,\alpha z)\) for a unique \(\alpha\in\mathbb F_p\).

**Linear quotient and the central correction.** Center preservation and \(B(gz)=B(g)B(z)\) show that \(B\) induces a well-defined map on \(G/Z(G)\cong V\). The group Rota–Baxter identity modulo the center makes this map additive and hence \(\mathbb F_p\)-linear. Thus \(B(v,z)=(Lv,\alpha z+f(v))\) for some \(L\) and \(f(0)=0\). Substituting into the defining identity and using the displayed group law gives, for every \(v,w\in V\),
\[
f(v+w)-f(v)-f(w)
=\tfrac12\omega(Lv,Lw)-\alpha\omega(Lv,w)-\tfrac\alpha2\omega(v,w).
\tag{4}
\]
The left side is symmetric in \(v,w\). Comparing (4) with its transposition yields precisely (1). Under (1), the right side of (4) is symmetric bilinear with diagonal \(-\alpha\omega(Lv,v)\). Since \(p\ne2\), every solution has
\[
f(v)=-\tfrac\alpha2\omega(Lv,v)+\ell(v),
\]
where \(\ell:V\to\mathbb F_p\) is additive, hence linear. Reversing the calculation proves sufficiency and uniqueness.

**Isotropic-fiber enumerators.** For \(\alpha=0\), (1) says \(\omega(Lv,Lw)=0\). For \(\alpha=-1\), use the equivalent identity \((1+\alpha)\omega(Lv,Lw)=\alpha\omega((I+L)v,(I+L)w)\) to see that \(T=I+L\) has isotropic image. This gives an explicit bijection between the fibers by \(L\mapsto-I-L\), with \(\ell\) chosen arbitrarily in either fiber.

For a fixed rank \(r\), the number of totally isotropic \(r\)-subspaces of \(V\) is
\[
I_{p,n,r}=\binom{n}{r}_{p}\prod_{j=0}^{r-1}(p^{n-j}+1).
\]
Indeed, count ordered isotropic independent vectors successively: the \((j+1)\)-st belongs to the perpendicular of the existing \(j\)-space but not to that space, yielding \(p^{2n-j}-p^j\) choices, then divide by the \(\prod_{j=0}^{r-1}(p^r-p^j)\) ordered bases of an \(r\)-space. Once an isotropic image \(U\) is selected, the number of surjections \(V\twoheadrightarrow U\) is \(\prod_{i=0}^{r-1}(p^{2n}-p^i)\). Independently \(\ell\) has \(p^{2n}\) choices. Their product is (2).

**Balanced-rank sector.** Assume \(\alpha\ne0,-1\) and both indicated ranks equal \(n\). The images \(U=\operatorname{im}L\) and \(W=\operatorname{im}(I+L)\) span \(V\) because \(v=(I+L)v-Lv\), and their dimensions add to \(2n\). Therefore they are complementary and \(L=-P_U\). Applying the equivalent form of (1) to vectors in \(U\) and in \(W\) separately forces \(\omega|_U=\omega|_W=0\). Conversely every ordered complementary Lagrangian pair makes both alternating forms in that identity vanish and gives an admissible \(L\). The number of Lagrangian \(U\) is \(\prod_{i=1}^n(p^i+1)\), while for each such \(U\), complementary Lagrangians \(W\) are graphs of symmetric linear maps from a fixed complement to \(U\), giving \(p^{n(n+1)/2}\) choices. Multiply by \(p^{2n}\) choices of \(\ell\) to obtain (3).

## Verification
Run `python3 verify.py` using only the Python standard library. The verifier independently executes finite-group multiplication and the group Rota–Baxter identity for every one of the \(243\) pairs \((L,\alpha)\) in dimension \(2\) over \(\mathbb F_3\), checking equivalence to (1), and checks every central linear twist on each admissible pair. It enumerates the \(40\) isotropic lines and \(40\) Lagrangian planes of a four-dimensional symplectic space over \(\mathbb F_3\), including \(27\) complements of a fixed Lagrangian. It also evaluates dimension-two parameter counts over \(\mathbb F_5\), checks complete \(\mathbb F_3\) group laws for explicit five-dimensional examples, and samples \(\mathbb F_5\) cases. The expected final marker is `VERIFY_OK`.

These finite calculations are regression and boundary checks, not proofs for all primes or dimensions. The unrestricted proof is given above.

## Relationship to prior work
Savelyev, *Rota—Baxter operators on extraspecial groups* (arXiv:2608.28291, first posted August 28, 2026), proves center invariance for general extraspecial groups and classifies operators on the two groups of order \(p^3\). That center lemma is reproved here; the all-dimensional symplectic parametrization and the rank-resolved cardinalities (2) and (3) are different statements, applying for every \(n\ge2\). Guo–Lang–Sheng developed the group operator identity and its involution, but no corresponding higher-dimensional finite-field enumerator is identified there. Bardakov and collaborators treat relative operators, semidirect constructions and verbal solutions for class-two groups; these do not provide the displayed classification or its isotropic-rank distributions. Literature overlap remains a live risk rather than a claim of exhaustive novelty.

## Limitations
The result does not classify automorphism orbits of \(L\) or give one closed polynomial for the total number of all operators across arbitrary \(\alpha\); for other central scalars only the balanced-rank stratum is enumerated explicitly. It does not cover characteristic two, exponent-\(p^2\) extraspecial groups, or central extensions with a larger center. The closest 2026 manuscript was accessible in substantive portions but its entire classification section could not be independently inspected during the comparison, leaving residual risk of a related higher-dimensional interpretation. The dimension-three specialization is acknowledged as substantially covered by that paper.

## References
1. A. Savelyev, *Rota—Baxter operators on extraspecial groups*, arXiv:2608.28291v1 (August 28, 2026), https://arxiv.org/abs/2608.28291.
2. L. Guo, H. Lang, Y. Sheng, *Integration and geometrization of Rota–Baxter Lie algebras*, Advances in Mathematics 387 (2021), article 107834, https://doi.org/10.1016/j.aim.2021.107834.
3. V. G. Bardakov, T. A. Kozlovskaya, P. P. Sokolov, K. V. Zimireva, M. N. Zonov, *Some properties of relative Rota–Baxter operators on groups*, arXiv:2404.12632v1 (April 19, 2024), https://arxiv.org/abs/2404.12632.
