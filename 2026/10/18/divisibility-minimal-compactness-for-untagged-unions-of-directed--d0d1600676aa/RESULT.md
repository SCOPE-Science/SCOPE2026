# Divisibility-minimal compactness for untagged unions of directed cycles

## Finding
For any nonempty **finite** set \(S\subseteq\{2,3,\ldots\}\), let \(D_S\) be the untagged disjoint union of the directed cycles of lengths in \(S\). Define the divisibility-minimal subset
\[
M(S)=\{m\in S:(d\in S\ \wedge\ d\mid m)\Rightarrow d=m\}.
\]
The following equivalence is provable in Zermelo--Fraenkel set theory **without choice**:
\[
\boxed{K_{D_S}\ \longleftrightarrow\ \bigwedge_{m\in M(S)}K_{C_m}.}
\]
In particular, for \(N\ge 2\),
\[
K_{C_2\sqcup C_3\sqcup\cdots\sqcup C_N}\ \longleftrightarrow\ \bigwedge_{\substack{p\le N\\p\ \mathrm{prime}}}K_{C_p}.
\]
Here each disjoint union has **only the single binary edge relation**. No unary predicate identifies its components.

## Assumptions and scope
The directed \(n\)-cycle \(C_n\), for \(n\ge2\), has carrier \(\{0,\ldots,n-1\}\) and arcs \(i\to i+1\pmod n\). Homomorphisms preserve arcs. Graphs may be arbitrary sets, infinite, disconnected and non-well-orderable. For a fixed nonempty finite directed template \(T\), \(K_T\) means: whenever every finite induced subgraph of a set-sized directed graph \(X\) admits an arc-preserving homomorphism to \(T\), so does \(X\). Empty instances satisfy the assertion by the empty function. These are principles over \(\mathsf{ZF}\), not assertions of graph finiteness or of finite satisfiability in ZFC. The finite set \(S\) has distinct lengths; only the length set, not multiplicities, matters.

## Proof
**1. Elementary cycle lemma.** For integers \(m,n\ge2\), \(C_m\to C_n\) if and only if \(n\mid m\): the successor equations imply that after \(m\) steps the target phase has increased by \(m\) modulo \(n\). Conversely, reduction modulo \(n\) is a homomorphism when \(n\mid m\). Every homomorphism from a weakly connected graph into a disjoint union of digraphs has image in exactly one weak component of the target. Each \(n\in S\) admits a divisor \(m\in M(S)\), so the inclusion \(D_{M(S)}\hookrightarrow D_S\) and the maps \(C_n\to C_m\) show the two templates are homomorphically equivalent. Homomorphic equivalence alone does not supply the required finite conjunction equivalence; this is proved next.

**2. The union principle implies each minimal cycle principle.** Fix \(m\in M(S)\) and an arbitrary directed graph \(X\) each of whose finite induced subgraphs maps to \(C_m\). Form \(Y\) by adjoining for every \(x\in X\) fresh vertices \((x,1),\ldots,(x,m-1)\), together with the arcs
\[
x\to(x,1)\to\cdots\to(x,m-1)\to x,
\]
and keeping every original arc of \(X\). For each finite induced subgraph of \(Y\), only finitely many old vertices or attached cycles are involved. Take the finite set of their old roots, extend an existing map of that finite set into \(C_m\) around every relevant private cycle by successive increments modulo \(m\), and include the designated \(C_m\) in \(D_S\). Thus every finite induced subgraph of \(Y\) maps to \(D_S\). Assuming \(K_{D_S}\), choose a homomorphism \(h:Y\to D_S\). Each private \(C_m\) must map wholly into some \(C_d\) with \(d\in S\). By the cycle lemma, \(d\mid m\); by minimality, \(d=m\). Hence \(h(x)\) lies in the unique \(m\)-cycle component of \(D_S\) for every original \(x\). The restriction \(h\upharpoonright X\) is a map \(X\to C_m\), establishing \(K_{C_m}\). Nothing was chosen for an infinite family of gadgets.

**3. Component-wise finite target stabilization.** Conversely assume every \(K_{C_m}\) for \(m\in M(S)\), and suppose every finite induced subgraph of \(X\) maps to \(D_S\). Let \(A\) be a nonempty weak component of \(X\). Every finite set \(F\subseteq A\) sits inside a **finite weakly connected** induced subgraph \(H\subseteq A\): choose one anchor inside this one component and finitely many finite undirected paths joining its finitely many given vertices. An \(H\to D_S\) map lands in a single \(C_n\), so for every finite \(F\subseteq A\) there exists \(n\in S\) such that \(F\to C_n\).

There is a **single** \(n_A\in S\) such that every finite induced subgraph of \(A\) maps to \(C_{n_A}\). Otherwise, for each of the finitely many \(n\in S\) select a finite induced obstruction \(F_n\subseteq A\) that does not map to \(C_n\). Their finite union is then an obstruction to **all** members of \(S\), contradiction. The finitely many selections are allowed in \(\mathsf{ZF}\). Choosing any divisor \(m\in M(S)\) of \(n_A\) and composing with \(C_{n_A}\to C_m\) shows that every finite subgraph of \(A\) maps to at least one minimal cycle.

**4. Canonical grouping and global assembly.** Define \(m(A)\) to be the **least natural number** \(m\in M(S)\) such that every finite subgraph of \(A\) maps to \(C_m\). This definition makes no simultaneous choices. For each \(m\in M(S)\), let \(X_m\) be the union of all weak components assigned \(m\). For any finite \(F\subseteq X_m\), its intersection with each of finitely many components has a map to \(C_m\); combine these finitely many maps to obtain \(F\to C_m\). By \(K_{C_m}\), there is a map \(g_m:X_m\to C_m\). Since \(M(S)\) is finite, the family of these global maps can be selected using only finite choice. Their disjoint union, followed by the inclusions \(C_m\hookrightarrow D_S\), is a homomorphism \(X\to D_S\). Thus \(K_{D_S}\) holds in \(\mathsf{ZF}\).

**5. Consecutive lengths.** The divisibility-minimal elements of \(\{2,3,\ldots,N\}\) are precisely the primes not exceeding \(N\); every composite has a strictly smaller prime divisor in the set, and no prime has such a divisor. Applying the theorem yields the displayed corollary.

## Verification
The proof checks all quantified steps for set-sized graphs, including weak-component formation by finite paths, finite stabilization without an infinite choice principle, canonical classification by least target length, and finite assembly of global maps. It uses no computational search or machine certificate; the claim is an exact deductive theorem, and no finite enumeration is presented as a replacement for the \(\mathsf{ZF}\) proof.

## Relationship to prior work
Li, Shan, Snodgrass, Thornton and Zhou (2026, arXiv:2609.33873v1) study compactness strength and use **additional unary predicates** to tag the directed-cycle summands of their \(\mathcal D_n\); their Theorem 42 identifies the compactness principle of that tagged signature with finite choice. Removing the unary symbols changes the template signature and is not a formal specialization of that theorem. Rorabaugh, Tardif and Wehlau (arXiv:1609.05221v5, §6) investigate individual directed cycles and weak-choice principles, not the indicated untagged finite-union formula. Long (arXiv:2605.19543v1, §3) explicitly records cycle-length divisibility and disjoint-union homomorphism behavior, which are used as **known** ingredients here, but does not study set-sized compactness principles over \(\mathsf{ZF}\). Previously published results about compactness of individual cycles may simplify the right-hand conjunction further; the new statement concerns the relationship of this conjunction to the untagged union template.

## Limitations
The theorem requires finite nonempty \(S\), finite cyclic components with at least two vertices, and a single untagged binary relation. No analogue for infinite \(S\), arbitrary connected digraph components, general unary-tagged structures, or separation of the resulting logical principles is claimed. The exact classification may have an earlier equivalent formulation under terminology such as finite-template coproducts or weak-choice compactness; historical priority remains uncertain. The known divisibility rule and any independent prime-factorization of single-cycle compactness are not asserted to be original.

## References
1. A. Li, I. Shan, M. Snodgrass, R. Thornton, R. Zhou, *Compactness Principles for CSPs and the Axiom of Choice*, arXiv:2609.33873v1 (2026), §§1.1, 3, https://arxiv.org/html/2609.33873v1.
2. D. Rorabaugh, C. Tardif, D. Wehlau, *Logical Compactness and Constraint Satisfaction Problems*, arXiv:1609.05221v5, §6, https://arxiv.org/html/1609.05221v5.
3. Y. Long, *The Quantum Homomorphism Orders Are Universal*, arXiv:2605.19543v1 (2026), §3 (classical directed-cycle homomorphism facts), https://arxiv.org/html/2605.19543v1.
