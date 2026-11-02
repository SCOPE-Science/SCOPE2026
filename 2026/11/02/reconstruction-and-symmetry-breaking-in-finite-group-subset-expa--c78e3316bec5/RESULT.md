# Reconstruction and symmetry breaking in finite-group subset expansions

## Finding

Let \(G\) and \(H\) be finite groups, with identities \(1_G\) and \(1_H\). Define the **full subset expansion**
\[
\mathcal S(G)=\mathcal P(G)\rtimes G,
\qquad
(A,g)(B,h)=(A\cup gB,gh),
\]
where \(gB=\{gb:b\in B\}\), and \(A\) and \(B\) may be empty. Define the **pointed subset expansion**
\[
\mathsf{Sz}(G)=\{(A,g)\in\mathcal S(G):\{1_G,g\}\subseteq A\}.
\]
These are finite inverse semigroups. Their respective identities are \((\varnothing,1_G)\) and \((\{1_G\},1_G)\); thus the pointed expansion is a subsemigroup but does not share the full expansion's identity.

**Theorem (all finite groups, including the trivial group).** Every isomorphism \(F:\mathcal S(G)\to\mathcal S(H)\) has the **unique** form
\[
F(A,g)=(\varphi(A)t,\varphi(g)),
\qquad t\in H,
\quad\varphi:G\overset{\sim}{\longrightarrow}H,
\tag{1}
\]
where \(\varphi\) is a group isomorphism and \(\varphi(A)t=\{\varphi(a)t:a\in A\}\). Every isomorphism \(K:\mathsf{Sz}(G)\to\mathsf{Sz}(H)\) has the **unique** form
\[
K(A,g)=(\varphi(A),\varphi(g)),
\qquad\varphi:G\overset{\sim}{\longrightarrow}H.
\tag{2}
\]
Consequently, these expansions determine the isomorphism type of the underlying finite group, and
\[
\operatorname{Aut}(\mathcal S(G))\cong
G\rtimes\operatorname{Aut}(G)=\operatorname{Hol}(G),
\qquad
\operatorname{Aut}(\mathsf{Sz}(G))\cong\operatorname{Aut}(G).
\tag{3}
\]

More precisely, the setwise stabilizer of \(\mathsf{Sz}(G)\) inside \(\operatorname{Aut}(\mathcal S(G))\) is exactly the copy of \(\operatorname{Aut}(G)\) given by \(t=1_G\). The orbit consists of precisely \(|G|\) distinct pointed subsemigroups
\[
\mathsf{Sz}_{t}(G)
=\{(A,g):\{t,gt\}\subseteq A\},\qquad t\in G.
\tag{4}
\]
Every automorphism of \(\mathcal S(G)\) decomposes uniquely as a conjugation by a unit followed by a pointed-expansion-preserving automorphism. Unit conjugations act faithfully, even when \(G\) has nontrivial center.

## Assumptions and scope

All groups are finite, with no commutativity, solvability, or order hypotheses. The powerset contains the empty subset, the multiplication is by **union** and left translate in the first coordinate, and the pointed expansion requires both the identity and the group coordinate to belong to its first coordinate. It must not be confused with the reduced power monoid under setwise group multiplication, which is a different algebra.

The notation \(\operatorname{Hol}(G)\) denotes the standard semidirect product for the natural action of \(\operatorname{Aut}(G)\) on \(G\). The results concern isomorphisms and automorphisms as abstract semigroups; none are assumed to preserve the displayed coordinates in advance. The group \(\operatorname{Aut}(G)\) is intrinsic and need not be computed by a classification of finite groups.

## Proof

**Step 1: Intrinsic structure in the full expansion.** For \((A,g)\in\mathcal S(G)\), its inverse in the inverse semigroup is \((g^{-1}A,g^{-1})\). Indeed both inverse identities follow directly from the multiplication rule. The idempotents are exactly \((A,1_G)\), since the group projection of an idempotent must be \(1_G\). Their multiplication is union, so the idempotent semilattice is the Boolean union-semilattice \(\mathcal P(G)\). The units are precisely \((\varnothing,g)\) for \(g\in G\): if \((A,g)(B,h)=(\varnothing,1_G)\), then \(A=B=\varnothing\). Thus an abstract isomorphism \(F:\mathcal S(G)\to\mathcal S(H)\) necessarily restricts to a group isomorphism \(\varphi:G\to H\) on units and a Boolean semilattice isomorphism \(\sigma:\mathcal P(G)\to\mathcal P(H)\) on idempotents.

The atoms in \(\mathcal P(G)\) are the singleton subsets, because inclusion is definable by the semilattice operation \(\cup\). Therefore \(\sigma(A)=s(A)\) for a unique bijection \(s:G\to H\). Conjugating idempotents by units gives the intrinsic identity
\[
(\varnothing,g)(A,1_G)(\varnothing,g^{-1})=(gA,1_G).
\]
After applying \(F\), this forces \(s(ga)=\varphi(g)s(a)\) for all \(g,a\in G\). Put \(t=s(1_G)\). Then \(s(a)=\varphi(a)t\) for every \(a\), and hence \(\sigma(A)=\varphi(A)t\). Finally every element factors as \((A,g)=(A,1_G)(\varnothing,g)\), so \(F\) has the form (1). The pair \((t,\varphi)\) is unique by restriction to units and singleton idempotents.

Conversely, for any group isomorphism \(\varphi:G\to H\) and \(t\in H\), the map in (1) is bijective and satisfies
\[
\begin{aligned}
F((A,g)(B,h))
&=(\varphi(A)t\cup\varphi(gB)t,\varphi(gh))\\
&=(\varphi(A)t\cup\varphi(g)\varphi(B)t,\varphi(g)\varphi(h))\\
&=F(A,g)F(B,h).
\end{aligned}
\]
This proves the full-expansion isomorphism classification.

**Step 2: Intrinsic structure in the pointed expansion.** Every \((A,g)\in\mathsf{Sz}(G)\) has inverse \((g^{-1}A,g^{-1})\), which lies in \(\mathsf{Sz}(G)\) because \(\{1_G,g\}\subseteq A\). Again the idempotents are precisely \((A,1_G)\), now with \(1_G\in A\). This idempotent semilattice is the Boolean union-semilattice on \(G\setminus\{1_G\}\), with minimum element \((\{1_G\},1_G)\). The pointed expansion itself has trivial group of units (the only possible inverse to the identity \((\{1_G\},1_G)\) forces \(A=\{1_G\}\) and \(g=1_G\)). Its atoms are
\[
e_g=(\{1_G,g\},1_G),\qquad g\ne1_G.
\]
Any abstract isomorphism \(K:\mathsf{Sz}(G)\to\mathsf{Sz}(H)\) therefore induces a bijection \(\sigma:G\setminus\{1_G\}\to H\setminus\{1_H\}\), characterized by \(K(e_g)=e_{\sigma(g)}\). Extend \(\sigma(1_G)=1_H\).

For every nonidentity \(g\), the element
\[
a_g=(\{1_G,g\},g)
\]
is the **unique nonidempotent element having range idempotent** \(a_ga_g^{-1}=e_g\). Indeed a general element \((A,x)\) has range idempotent \((A,1_G)\); requiring this to equal \(e_g\) forces \(A=\{1_G,g\}\) and \(x\in\{1_G,g\}\), of which exactly one choice is nonidempotent. Thus \(K(a_g)=a_{\sigma(g)}\), without any coordinate-preservation assumption.

For \(g,h\ne1_G\), the product
\[
a_ga_h=(\{1_G,g,gh\},gh)
\]
exhibits the group product in intrinsic terms. Its range idempotent is \((\{1_G,g,gh\},1_G)\). Applying \(K\) to that range idempotent yields \((\{1_H,\sigma(g),\sigma(gh)\},1_H)\), whereas computing \(K(a_g)K(a_h)\) yields a range idempotent \((\{1_H,\sigma(g),\sigma(g)\sigma(h)\},1_H)\). If \(gh\ne1_G\), then \(gh\ne g\) and the first set has three elements; the second must have three elements too, so equality forces \(\sigma(gh)=\sigma(g)\sigma(h)\). If \(gh=1_G\), the original product is exactly the idempotent \(e_g\); its image is idempotent, so the second coordinate of \(a_{\sigma(g)}a_{\sigma(h)}\) must be \(1_H\), and again \(\sigma(g)\sigma(h)=\sigma(gh)\). Cases with one identity factor hold by definition. Therefore \(\sigma\) is a group isomorphism.

For every pointed element with \(g\ne1_G\), because \(\{1_G,g\}\subseteq A\), there is a factorization
\[
(A,g)=(A,1_G)a_g.
\]
For \(g=1_G\) the element is an idempotent. Thus the behavior of \(K\) on idempotents and the \(a_g\) determines it everywhere, giving (2). Conversely, each group isomorphism induces the map (2), which is an isomorphism by the multiplication rule. For \(|G|=1\), the pointed inverse semigroup has a single element and the same conclusion is immediate. This completes the pointed isomorphism classification.

**Step 3: The automorphism groups, orbit and factorization.** Specializing to \(G=H\), the full-expansion maps (1) compose according to
\[
F_{t,\varphi}\circ F_{s,\psi}
=F_{\varphi(s)t,\varphi\circ\psi}.
\]
Replacing the translation parameter \(t\) by \(t^{-1}\) gives the standard multiplication law in \(G\rtimes\operatorname{Aut}(G)\). Formula (2) identifies \(\operatorname{Aut}(\mathsf{Sz}(G))\) with \(\operatorname{Aut}(G)\).

The pointed expansion has identity \((\{1_G\},1_G)\). Formula (1) sends this element to \((\{t\},1_G)\); hence it maps \(\mathsf{Sz}(G)\) to itself only if \(t=1_G\). Conversely, \(t=1_G\) preserves it. For arbitrary \(t\), (1) sends it to exactly \(\mathsf{Sz}_{t}(G)\) in (4), independently of \(\varphi\). Distinct values of \(t\) give distinct subsemigroups because their identities \((\{t\},1_G)\) differ. This yields the orbit and stabilizer claims.

The units of \(\mathcal S(G)\) are \(u_t=(\varnothing,t)\). Their inner conjugations are
\[
C_t(A,g)=u_t(A,g)u_t^{-1}=(tA,tgt^{-1})
=F_{t,\operatorname{Ad}_t}(A,g).
\]
The map \(t\mapsto C_t\) is faithful: it sends \((\{1_G\},1_G)\) to \((\{t\},1_G)\). For any automorphism \(F_{t,\varphi}\), put \(\psi=\operatorname{Ad}_{t^{-1}}\circ\varphi\). Then
\[
F_{t,\varphi}=C_t\circ F_{1_G,\psi}.
\]
Its factors are unique, since a unit conjugation fixes the identity of \(\mathsf{Sz}(G)\) only when \(t=1_G\). The unit-conjugation subgroup is normal because semigroup automorphisms preserve units. This finishes the canonical semidirect-product and symmetry-breaking description. \(\square\)

## Verification

The supplied standalone standard-library script `verify.py` constructs the group multiplication tables, both expansions, the complete proposed automorphism families, and their multiplication tables. It checks all claimed maps preserve multiplication for cyclic groups of orders \(1,2,3,4\), the Klein group, and the nonabelian symmetric group on three points. It also checks that each inner conjugation agrees with its proposed formula, that the pointed-expansion orbit has exactly \(|G|\) distinct members, and that the group-automorphism action on them matches the theorem.

For the cases where the expansion has at most eight elements, the script independently enumerates **every** permutation of the expansion and tests the complete automorphism identities, obtaining the claimed orders. Representative counts for the full and pointed expansions are: \(C_2\): \(8\) and \(3\) elements, automorphism-group orders \(2\) and \(1\); \(C_3\): \(24\) and \(8\) elements, orders \(6\) and \(2\); \(C_4\): orders \(8\) and \(2\); \(C_2\times C_2\): orders \(24\) and \(6\); \(S_3\): orders \(36\) and \(6\). The script prints `VERIFY_OK` if every finite check passes. These finite computations are corroboration, not a proof for arbitrary groups; the reconstruction argument above supplies that proof.

## Relationship to prior work

Gould and Johnson introduced and analyzed full subset expansions \(\mathcal S(M)\), explicitly identifying the Szendrei expansion as a smaller related construction. Their 2025 work establishes structural inverse-monoid and finitary properties, not the isomorphism/automorphism classification or the relative stabilizer-and-orbit result proved here. The prefix/Szendrei expansion and its equivalence for groups predate that paper (Szendrei 1989; Fountain and Gomes 1990; Lawson, Margolis and Steinberg 2006). These constructions are prior inputs, not claimed discoveries.

Automorphism groups of reduced power monoids have a separate literature, notably Rago's 2025 treatment of finite abelian groups. Those monoids use setwise group multiplication on identity-containing subsets; their automorphism theorems cannot be substituted for the union-with-translation product studied here. The holomorph is a classical group; the claim is its intrinsic realization as **the entire** automorphism group of the full subset expansion, and the simultaneous exact collapse to \(\operatorname{Aut}(G)\) at the pointed subsemigroup.

No equivalent all-finite-group isomorphism-and-stabilizer theorem was located in the accessible sources and mathematical-record searches. Some earlier literature on prefix expansions and universal constructions was not available in complete text and could imply parts of the result; the present statement is not independently certified as historically first.

## Limitations

The proof is for finite groups. The full-expansion argument extends formally to all groups with arbitrary subsets, and the pointed argument to groups with finite-support pointed pairs; nevertheless these extensions are not part of the stated theorem and are not separately claimed. The work does not classify automorphisms of subset expansions of arbitrary monoids, and it does not treat reduced power monoids under setwise multiplication. Existing universal-property treatments of prefix expansions may imply the pointed rigidity statement, so historical novelty is limited by access to older literature. No independent mathematical audit has been conducted.

## References

1. V. Gould and M. Johnson, “Subset expansions of monoids,” arXiv:2511.13435v1 (first posted 2025-11-17); revised v2 (2025-12-19). https://arxiv.org/abs/2511.13435 ; complete HTML https://arxiv.org/html/2511.13435v2
2. M. B. Szendrei, “A note on the Birget–Rhodes expansion of groups,” *Journal of Pure and Applied Algebra* 58 (1989), 93–99.
3. J. Fountain and G. M. S. Gomes, “The Szendrei expansion of a semigroup,” *Mathematika* 37 (1990), 251–260. https://doi.org/10.1112/S0025579300012973
4. M. V. Lawson, S. W. Margolis and B. Steinberg, “Expansions of inverse semigroups,” *Journal of the Australian Mathematical Society* 80 (2006), 205–228. https://doi.org/10.1017/S1446788700013082
5. C. Hollings, “Conditions for the prefix expansion of a monoid to be (weakly) left ample,” *Acta Scientiarum Mathematicarum (Szeged)* 73 (2007), 519–545.
6. B. Rago, “The automorphism group of reduced power monoids of finite abelian groups,” arXiv:2510.17533 (2025). https://arxiv.org/abs/2510.17533
