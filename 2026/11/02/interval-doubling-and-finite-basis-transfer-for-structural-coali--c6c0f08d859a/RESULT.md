# Interval doubling and finite-basis transfer for structural coalition logics

## Finding

Let the agent set \(N\) be finite with \(|N|\ge 2\). Let \(\mathscr L_N\) be the inclusion lattice of structural logics between minimal coalition logic \(\mathsf{MCL}\) and classical coalition logic \(\mathsf{CL}\), with modus ponens, uniform substitution, and conditional necessitation retained in all extensions. Put
\[
e=[\varnothing]\top,\qquad \Box\varphi=(e\to[\varnothing]\varphi),
\]
\[
S=\operatorname{Cn}(e),\qquad U=\operatorname{Cn}(\Box e),\qquad
C=\operatorname{Cn}(\mathsf{IA},\mathsf{Det},\Box e).
\]
Here \(\operatorname{Cn}(\Gamma)\) is structural theorem-set closure over \(\mathsf{MCL}\), and the abbreviations \(\mathsf{IA}\) and \(\mathsf{Det}\) stand for their full axiom schemes.

**Theorem (paired intervals).** The maps
\[
J:[U,C]\longrightarrow[S,\mathsf{CL}],\quad J(K)=S\vee K,
\qquad
R:[S,\mathsf{CL}]\longrightarrow[U,C],\quad R(L)=L\cap C
\]
are mutually inverse order and complete-lattice isomorphisms. In particular, \(S\cap C=U\). The whole lattice \(\mathscr L_N\) is the interval doubling of its lower segment \([\mathsf{MCL},C]\) along \([U,C]\): keep every lower element \(P\le C\), introduce a distinct upper copy \(K^{+}\) for each \(U\le K\le C\), order each layer as before, put \(P\le K^{+}\) exactly when \(P\le K\), and put no upper element below a lower one.

**Theorem (uniform relative presentation).** For every set \(\Gamma\subseteq\mathsf{CL}\), with the axiom-scheme closure implicit, one has
\[
\boxed{\operatorname{Cn}(\{e\}\cup\Gamma)\cap C
=\operatorname{Cn}\bigl(\{\Box e\}\cup\{e\to\gamma:\gamma\in\Gamma\}\bigr).}
\]
Consequently, the isomorphisms preserve finite axiomatizability and compactness of their elements in the entire extension lattice: a serial intermediate logic is finitely axiomatizable if and only if its intersection with the nonserial coatom is finitely axiomatizable. Finite axiom presentations translate explicitly in either direction. These statements are for *all* structural extensions in the indicated intervals, not just the eight basic coalition logics.

## Assumptions and scope

For every coalition \(D\subseteq N\), the MCL language has a strategic ability connective \([D]\). The system has the standard axiom schemes MG, MC, Live and inference rules MP, US, CN, where CN infers \([D]\chi\to[\varnothing]\psi\) from a theorem \(\psi\). An extension is a theory closed under all three rules; CN acts on theorems, not on open local assumptions. The derived \(\Box\) is normal and admits necessitation and the K distribution axiom; MCL proves \([D]\chi\to e\). All logics considered lie between MCL and CL, and the agent set is held fixed. The statement does not concern arbitrary nonstructural theories or other modalities.

We use three published inputs, citing their precise locations below: (i) soundness and completeness of MCL for general concurrent game models, (ii) the fixed-frame soundness and normal-box derivations for this presentation, and (iii) Wang--Dou's splitting theorem \(L\le C\iff e\notin L\) and their identification of the displayed \(C\) as the unique nonserial coatom. The interval isomorphism and explicit presentations below are proved from these inputs rather than assumed as part of them.

## Proof

**1. Dead-end separation.** A one-state general concurrent game with no available full profile validates the schemes IA, Det and \(\Box e\), along with all MCL axioms; all ability formulas \([D]\theta\) are false there, so CN, MP and US preserve frame validity. Therefore every \(\psi\in C\) is valid under every propositional assignment at that dead end. In any general concurrent game state where \(\neg e\) holds, all ability formulas \([D]\theta\) are again false, regardless of the truth of their nested arguments. Induction on formula syntax transfers the truth value of \(\psi\) at such a state to that one-state frame under the same propositional assignment. The formula \(\neg e\to\psi\) is thus valid on *all* general concurrent games. Completeness of MCL yields
\[
\tag{1}\mathsf{MCL}\vdash\neg e\to\psi\quad\text{for every }\psi\in C.
\]
Notice that this assertion is *not* made for arbitrary CL formulas: membership in \(C\) is essential.

**2. A relativization induction.** Fix any structural theory \(T\) with \(U\subseteq T\) and any set of formulas \(\Gamma\) such that \(e\to\gamma\in T\) for each \(\gamma\in\Gamma\). For every \(\varphi\in\operatorname{Cn}(\{e\}\cup\Gamma)\), we claim
\[
\tag{2} e\to\varphi\in T.
\]
Induct on a Hilbert derivation of \(\varphi\). MCL axioms, the new axiom \(e\), and generators \(\Gamma\) satisfy (2); MP preserves it propositionally. US preserves it because \(e\) contains no propositional variable. For the CN rule suppose \(\varphi\) has already been handled. By normality and necessitation of the derived box, \(T\) proves \(\Box(e\to\varphi)\); since \(\Box e\in U\subseteq T\), K gives \(\Box\varphi=e\to[\varnothing]\varphi\). The MCL theorem \([D]\chi\to e\) then yields \([D]\chi\to[\varnothing]\varphi\) in \(T\), in particular its implication from \(e\). This is precisely the CN conclusion. Every possible derivation step has been covered, including substitution and conditional necessitation.

**3. Recovery from the serial layer.** For an arbitrary \(L\in[S,\mathsf{CL}]\), the inclusion \(S\vee(L\cap C)\subseteq L\) is immediate. For any \(\varphi\in L\), the published relativization step for the nonserial coatom gives \(e\to\varphi\in C\) because \(\varphi\in\mathsf{CL}\); propositional closure gives \(e\to\varphi\in L\). Hence \(e\to\varphi\in L\cap C\), and because \(e\in S\) this implies \(\varphi\in S\vee(L\cap C)\). Thus
\[
\tag{3} S\vee(L\cap C)=L.
\]

**4. Recovery from the nonserial layer.** Take \(K\in[U,C]\) and \(\varphi\in(S\vee K)\cap C\). Apply (2) with \(T=K\) and \(\Gamma=K\) (every generator in \(K\) implies its conditional version) to obtain \(e\to\varphi\in K\). Since \(\varphi\in C\), (1) gives \(\neg e\to\varphi\in\mathsf{MCL}\subseteq K\). By propositional excluded middle \(\varphi\in K\). The opposite inclusion is obvious. Hence
\[
\tag{4} (S\vee K)\cap C=K.
\]
Together (3)--(4) establish the inverse order isomorphisms. Their domains are complete lattices, so arbitrary joins and meets are preserved. Taking \(K=U\), and using \(S\vee U=S\) (derived necessitation applied to \(e\)), gives \(S\cap C=U\).

**5. Entire-lattice doubling.** Wang--Dou's splitting theorem says every \(L\in\mathscr L_N\) satisfies \(L\le C\) or \(L\ge S\). Equations (3)--(4) make the latter layer a second copy of \([U,C]\). If \(P\le C\) is a lower element and \(K\in[U,C]\), then
\[
P\le S\vee K\quad\Longleftrightarrow\quad P\le(S\vee K)\cap C=K.
\]
No upper element is below a lower element, since every upper element contains \(e\), while no element \(P\le C\) does. These are exactly the order relations stated for interval doubling; importantly, a mere splitting pair in an arbitrary lattice would not alone have supplied the inverse identities (3)--(4).

**6. Uniform axiom translation.** Let \(L=\operatorname{Cn}(\{e\}\cup\Gamma)\) and
\[
T=\operatorname{Cn}\bigl(\{\Box e\}\cup\{e\to\gamma:\gamma\in\Gamma\}\bigr).
\]
Since \(\Gamma\subseteq\mathsf{CL}\), the published CL-relativization theorem puts every \(e\to\gamma\) in \(C\), whence \(T\subseteq C\). Conversely \(L\) proves \(\Box e\) by necessitation and proves every conditional generator, so \(T\subseteq L\cap C\). For \(\varphi\in L\cap C\), the induction (2) applied to \(T\) yields \(e\to\varphi\in T\). The dead-end lemma (1) yields \(\neg e\to\varphi\in T\), hence \(\varphi\in T\). This proves the boxed equality. The result holds for infinite as well as finite \(\Gamma\); no claim of an algorithm deciding semantic equivalence is implicit.

**7. Compactness and finite bases.** Proposition 3.1 of Wang--Dou characterizes compact elements of \(\mathscr L_N\) precisely as extensions \(\operatorname{Cn}(\Delta)\) for finite \(\Delta\). If \(L\ge S\) is compact, express it as \(\operatorname{Cn}(\{e\}\cup\Delta)\) for finite \(\Delta\subseteq L\); the formula in step 6 gives a finite basis for \(L\cap C\). If \(K\ge U\) is compact with finite basis \(\Delta\), then \(S\vee K=\operatorname{Cn}(\{e\}\cup\Delta)\) is compact. The two constructions are inverse because of (3)--(4). QED.

## Verification

The proof is symbolic and makes no numerical assertion needing a computational certificate. Every nonstandard step has been independently unfolded in steps 1--7: completeness is invoked only for formulas valid on *all* general concurrent game models; conditional necessitation is checked explicitly in the relativization induction; arbitrary axiom sets are admitted, including empty sets; and the interval-doubling order is checked across layers. All three pivotal displayed identities (3), (4), and the uniform presentation are proved in both directions rather than inferred only from a lattice-theoretic analogy. No finite sample is presented as proof of an infinite identity.

Boundary checks: \(\Gamma=\varnothing\) gives \(S\cap C=U\); \(K=U\) maps to \(S\), while \(K=C\) maps to \(\mathsf{CL}\) because the cited nonserial-coatom theorem gives \(C\vee S=\mathsf{CL}\). No assertion about nonstructural logics or local assumptions is used.

## Relationship to prior work

Wang and Dou [1], Theorem 5.1, prove the splitting coatom \(C\) and its two crucial ingredients: (a) serial-state relativization of CL theorems and (b) the dead-end characterization. Their Proposition 3.1 proves the compactness/finite-basis equivalence, and their Section 6 studies compact meets of basic extensions. We reuse these results explicitly. The present claim is *not* the splitting theorem and is *not* a new proof of its source results: it is the complete paired-interval isomorphism, the whole-lattice interval-doubling normal form, and the explicit arbitrary-generator transfer of finite bases. Those statements and translation formulas were not located in the inspected complete text of [1]. Li and Ju [2] provide the MCL completeness theorem used in step 1. Thus this result depends materially on recent work, rather than preceding it. Comparable abstract constructions may exist under terminology for splitting pairs, doubling, or modal-extension lattices.

## Limitations

The theorem applies to the structural MCL--CL interval for a fixed finite agent set with at least two agents. It does not enumerate the serial coatoms, characterize arbitrary meets of compact logics, solve the general compact-meet problem for incomparable non-basic logics, or establish decidability of axiom equivalence. Its finite-basis transfer does not certify that an unknown particular coatom has a finite basis. Relative historical priority is limited by the inspected sources: an older abstract lattice-doubling theorem or an equivalent unindexed coalition-logic translation may subsume the construction. No independent audit or formal proof-assistant certification has been performed.

## References

[1] S. Wang and Y. Dou, *The Lattice of Coalition Logics between MCL and CL: Coatoms and Compact Meets*, arXiv:2610.24466v1, publicly posted 2026-10-17. Full text: https://arxiv.org/html/2610.24466v1. Relevant: Definitions 2.1, equations (9)--(10), Proposition 3.1, Theorem 5.1 and its proof, Remark 5.2, Lemma 6.6, Section 7.

[2] Y. Li and F. Ju, *A minimal coalition logic*, arXiv:2403.14704, first posted 2024-03-21; version 3 accessible as https://arxiv.org/html/2403.14704v3. Relevant: the MCL completeness theorem for general concurrent game models and derived box semantics.
