# Anonymous-atom collapse in the powerset binary-join modal language

## Finding

Let \(n\ge1\) and \(0\le k\le n\). In the marked powerset binary-join modal frame described below, two states have the same complete modal theory exactly when they have the same named coordinates and agree on whether they contain an unnamed coordinate. Consequently, the observational quotient has exactly \(2^{k+1}\) states if \(k<n\), and \(2^k\) states if \(k=n\). A concrete ternary back-and-forth quotient realizes this minimum, independent of the number of unnamed coordinates.

## Assumptions and scope

Take the carrier \(W=\mathcal P([n])\) with ternary relation \(R(S,Y,Z)\) defined by \(S=Y\cup Z\). The language has classical Boolean constants and connectives, the binary modality \(\langle\vee\rangle(\alpha,\beta)\) with the truth clause \(S\vDash\langle\vee\rangle(\alpha,\beta)\) iff \(R(S,Y,Z)\) for some \(Y\vDash\alpha\), \(Z\vDash\beta\), a bottom marker \(b\) true only at \(\varnothing\), and markers \(p_i\) true only at the singleton \(\{i\}\), for each \(i\in K=\{1,\ldots,k\}\). This is a fixed, explicitly stated atomic valuation, not an arbitrary valuation. The unnamed set is \(H=[n]\setminus K\).

For nonempty \(H\), introduce one fresh symbol \(\star\), put \(W'=\mathcal P(K\cup\{\star\})\), and define the map

\[
q(S)=(S\cap K)\cup\begin{cases}\{\star\}&S\cap H\ne\varnothing,\\\varnothing&S\cap H=\varnothing.\end{cases}
\]

If \(H=\varnothing\), instead set \(W'=\mathcal P(K)\) and let \(q\) be the identity. On \(W'\), use the same union relation and the same singleton and empty-set markers.

## Proof

**Ternary bounded morphism.** The map \(q\) is onto and obeys \(q(Y\cup Z)=q(Y)\cup q(Z)\). Conversely, suppose \(q(S)=A\cup B\). Construct \(Y,Z\subseteq S\) as follows: place each named member of \(S\) into \(Y\) exactly when it lies in \(A\), and into \(Z\) exactly when it lies in \(B\); if \(\star\in A\), place *all* unnamed members of \(S\) in \(Y\); if \(\star\in B\), place all of them in \(Z\). Every member of \(S\) is placed in at least one part, so \(S=Y\cup Z\), and \(q(Y)=A\), \(q(Z)=B\). The marker valuations are inverse images of their target valuations: \(q(S)=\varnothing\) holds only for \(S=\varnothing\), while \(q(S)=\{i\}\) holds only for \(S=\{i\}\). Thus induction over Boolean connectives and the binary modality yields

\[
S\vDash\varphi\quad\Longleftrightarrow\quad q(S)\vDash\varphi
\]

for **every** formula \(\varphi\) in the specified language.

**Separating all distinct fibres.** Define \(m_i=\langle\vee\rangle(p_i,\top)\). By the exact-union semantics, \(S\vDash m_i\) if and only if \(i\in S\). Each named-only subset \(J\subseteq K\) is also definable *as one exact state*: \(\delta_\varnothing=b\), \(\delta_{\{i\}}=p_i\), and for any nonempty \(J\) not containing \(i\), set \(\delta_{J\cup\{i\}}=\langle\vee\rangle(\delta_J,p_i)\). An induction on \(|J|\) verifies that \(\delta_J\) holds exactly at \(S=J\). The finite disjunction \(\eta=\bigvee_{J\subseteq K}\delta_J\) therefore holds exactly when \(S\cap H=\varnothing\). Any two states with distinct named parts differ on some \(m_i\); states with equal named parts but different unnamed-nonemptiness differ on \(\eta\).

**Sharpness.** The first step proves that the truth theory depends only on \(q(S)\). The second proves that different values of \(q(S)\) have distinct theories. Since every target state has a preimage, there are exactly \(|W'|\) distinct theories, namely \(2^{k+1}\) if \(H\ne\varnothing\), otherwise \(2^k\). Every state quotient preserving all formulas must put states with distinct theories in different classes, so it needs at least \(|W'|\) classes; \(q\) attains that bound.

## Verification

The included standalone `checker.py` computes the least stable partition obtained by modal partition refinement, starting from the atomic marker valuations and closing under the complete binary union relation. It verifies for every \(1\le n\le5\) and \(0\le k\le n\) that the refined modal classes are precisely the fibres of \(q\), that the cardinality formula holds, and that every target union of a quotient state lifts to a source union. Run with `python checker.py`; successful completion prints `ALL_CHECKS_OK`. The infinite quantification over \(n\) is established by the symbolic proof rather than finite testing.

## Relationship to prior work

The binary supremum modality over semilattices is part of the classical-modal framework used by Aloni, Baltag, van Benthem, Bezhanishvili and Knudstorp (2026) to translate truthmaker/team logics. The present calculation concerns a particular marked full powerset frame and gives a sharp observational quotient, not a new semantic translation. General results on coalgebraic modal bisimulation provide conceptual context but do not directly state this precise finite quotient. Relevant literature on locality in union-closed team logics describes a different semantic signature; the relationship has been considered but historical priority is not independently certified.

## Limitations

The count requires the exact singleton markers and the bottom marker as defined. Arbitrary valuations, graded modalities, non-idempotent combinations, or additional modalities may distinguish states that this language identifies. The formula concerns equivalence of states within one fixed labelled frame, not equivalence of all frames. The calculation does not claim to prove a general result about the full translation language or complexity of satisfiability. Related formulas might occur in older semilattice/coalgebra literature under other terminology. The 2026 motivating source was available for detailed review of the semantic clause and early development, but its complete later text was not accessible for direct comparison.

## References

1. M. Aloni, A. Baltag, J. van Benthem, N. Bezhanishvili and S. B. Knudstorp, *Teams, Truthmakers, Translations*, arXiv:2610.15680, first public 2026-10-11. https://arxiv.org/abs/2610.15680
2. *Bisimulation for Weakly Expressive Coalgebraic Modal Logics*, CALCO 2017, DOI:10.4230/LIPIcs.CALCO.2017.4. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CALCO.2017.4
3. *Propositional union closed team logics*, Annals of Pure and Applied Logic (2022), DOI:10.1016/j.apal.2022.103102. https://doi.org/10.1016/j.apal.2022.103102
