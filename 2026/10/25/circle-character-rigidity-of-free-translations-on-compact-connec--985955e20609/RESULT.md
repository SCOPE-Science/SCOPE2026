# Circle-character rigidity of free translations on compact connected abelian groups

## Finding
Let \(K\) be a compact connected Hausdorff abelian topological group, and let \(G\subseteq K\) be any nontrivial compact subgroup. Let \(G\) act freely on \(K\) by right translations. Then **no continuous \(G\)-equivariant map**
\[
K*G\longrightarrow K
\]
exists, where the join carries the diagonal right action.

More generally, let \(G\) be a compact Hausdorff group acting continuously on a nonempty connected space \(X\), and suppose there is a nontrivial continuous character \(\chi:G\to S^1\) and a continuous function \(p:X\to S^1\) with \(p(xg)=p(x)\chi(g)\). Then every \(G\)-equivariant self-map of \(X\) is non-nullhomotopic.

For each prime \(p\), the additive group \(\mathbb Z_p\) has a free translation action on the connected countable torus \(\prod_{k\ge1}S^1\) to which the result applies. This stands in contrast to a different free action of the same group on \(\prod_{k\ge1}S^3\) allowing an equivariant join map [1, Corollary 1.3].

## Assumptions and scope
All spaces and groups are Hausdorff when indicated. The circle \(S^1\) is the unit complex circle; a character is a continuous homomorphism into \(S^1\). Actions are on the right. Nullhomotopy means an *ordinary*, not equivariant, homotopy to a constant map. The connectedness assumption concerns \(X\), not \(G\); compactness is needed for \(G\), not for the auxiliary \(X\). The closed subgroup \(G\subseteq K\) is nontrivial and need not be connected, finite, or Lie.

We use the classical diagonal join \(X*G\). The standard join/nullhomotopy correspondence used below is stated in [1, Section 1, Proposition 1.1] and attributed there to [2, Lemma 4.1].

## Proof
**Circle-character lemma.** Assume that an equivariant self-map \(h:X\to X\) were nullhomotopic. The composite \(f=p\circ h:X\to S^1\) is then nullhomotopic. The covering map \(\exp(2\pi i\cdot):\mathbb R\to S^1\) admits a lift \(u:X\to\mathbb R\) of \(f\): lift the terminal constant of a nullhomotopy of \(f\), then lift the homotopy backwards using the covering-homotopy property. Thus \(f(x)=\exp(2\pi i u(x))\).

For any fixed \(g\in G\), equivariance gives
\[
\exp(2\pi i[u(xg)-u(x)])=\chi(g).
\]
As a function of \(x\in X\), the bracket is continuous and takes its values in a single discrete coset of \(\mathbb Z\). Since \(X\) is connected, it is constant. Write its value as \(a(g)\). At any chosen \(x_0\in X\), the formula \(a(g)=u(x_0g)-u(x_0)\) proves continuity of \(a:G\to\mathbb R\). Moreover,
\[
\begin{aligned}
a(gh)&=u(xgh)-u(x)\\
&=[u((xg)h)-u(xg)]+[u(xg)-u(x)]\\
&=a(h)+a(g).
\end{aligned}
\]
Hence \(a\) is a continuous homomorphism to the additive reals. The continuous image of compact \(G\) is a compact subgroup of \(\mathbb R\), and therefore zero. Consequently \(\chi(g)=\exp(2\pi i a(g))=1\) for every \(g\), contradicting the choice of nontrivial \(\chi\). So no such nullhomotopic \(h\) exists.

**Translation corollary.** Continuous circle characters separate points of every compact Hausdorff abelian group (Pontryagin separation). Choose \(g\in G\setminus\{e\}\) and a character \(\lambda:K\to S^1\) for which \(\lambda(g)\ne1\). Then \(p=\lambda\) satisfies \(p(xg)=p(x)(\lambda|_G)(g)\), with a nontrivial restricted character. The circle-character lemma prevents nullhomotopic equivariant self-maps of \(K\). By the join/nullhomotopy correspondence [1, Proposition 1.1; 2, Lemma 4.1], the stated map \(K*G\to K\) does not exist. The action is free because \(xg=x\) implies \(g=e\).

**Explicit torsion-free profinite example.** For a prime \(p\), identify \(\mathbb Z_p=\varprojlim_k\mathbb Z/p^k\mathbb Z\). The continuous homomorphism
\[
\iota:\mathbb Z_p\longrightarrow\prod_{k\ge1} S^1,\qquad
z\longmapsto\bigl(\exp(2\pi i (z\bmod p^k)/p^k)\bigr)_{k\ge1}
\]
is injective because an element vanishing in every residue ring is zero. Its image is closed because the domain is compact and the product torus Hausdorff. The product torus is compact and connected. The translation corollary applies to the embedded subgroup \(\iota(\mathbb Z_p)\).

## Verification
All proof steps are symbolic and hold for every group/space satisfying the quantified hypotheses. The only external standard inputs are the covering-homotopy property for \(\mathbb R\to S^1\), separation by characters of compact abelian groups, and the join/nullhomotopy correspondence [1,2]. The key equality for \(a(gh)\) is shown explicitly. Nontriviality of the restricted character follows from the chosen \(g\), not from an assumed faithful action on \(S^1\). The inverse-limit embedding is checked coordinatewise for continuity, injectivity, and closed image. No finite computation is being used as proof of an infinite assertion.

## Relationship to prior work
Chirvasitu–Dąbrowski [1, Theorem 0.2 and Corollary 1.3] characterize which compact abelian **acting groups admit at least one** free compact-space action with an equivariant join map; in particular they construct such an action for every \(\mathbb Z_p\) on a countable product of 3-spheres. That existential result does not imply that a join map exists on each free action of such a group. The theorem above instead gives an **action-specific obstruction** for a natural and broad family of connected translation spaces, producing both positive and negative answers for the same \(\mathbb Z_p\) as the acting group. It does not contradict [1].

Chirvasitu–Passer [2, Section 3] study the general join obstruction and reduce its previously unresolved compact-group cases to \(p\)-adic subgroups; their join/nullhomotopy reduction is used here. The topological torus-translation obstruction for all nontrivial closed subgroups of arbitrary compact connected abelian \(K\) is not stated in the inspected relevant sections [1,2]. The character lift argument is distinct from the source paper's higher-dimensional sphere construction and the known acting-group torsion obstruction.

## Limitations
The proof concerns translation actions on connected compact abelian groups, or more generally connected actions admitting a nontrivial circle-valued eigenfunction; it does not give an obstruction for arbitrary free actions, arbitrary disconnected spaces, or actions without such eigenfunctions. Character separation is a standard imported theorem, not proved here. The comparison with [1] is about existence for a specific space, not uniqueness of any free action. Searches of indexed literature and published records cannot exclude every equivalent unpublished or differently named criterion; no independent review has been performed.

## References
[1] A. Chirvasitu and A. Dąbrowski, *Nullhomotopic equivariant shifts and Borsuk-Ulam-compatible compact abelian groups*, arXiv:2610.10111v1 (7 October 2026), https://arxiv.org/html/2610.10111v1.

[2] A. Chirvasitu and B. Passer, *Compact Group Actions on Topological and Noncommutative Joins*, arXiv:1604.02173v4, https://arxiv.org/pdf/1604.02173.

[3] Pontryagin duality, standard character-separation theorem for compact Hausdorff abelian groups (used only for the translation corollary).
