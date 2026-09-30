# Schematic validity of \(\mathrm{InqB}\) is \(\Pi^0_1\)-complete
## Finding
Let \(\mathrm{{InqB}}\) be propositional inquisitive logic over a countably infinite set of propositional variables. Define its schematic theorem fragment by
\[
\operatorname{{Sch}}(\mathrm{{InqB}})=\{{\varphi: \text{{for every uniform substitution }}\sigma,\ \sigma(\varphi)\in\mathrm{{InqB}}\}}\}.
\]
The known identification
\[
\operatorname{{Sch}}(\mathrm{{InqB}})=\mathrm{{ML}}
\]
with Medvedev's logic \(\mathrm{{ML}}\), together with Pawlowski's 2026 theorem that \(\mathrm{{ML}}\) is \(\Pi^0_1\)-complete under computable many-one reductions, gives
\[
\operatorname{{Sch}}(\mathrm{{InqB}})\text{{ is }}\Pi^0_1\text{{-complete}}.
\]
Consequently schematic validity for \(\mathrm{{InqB}}\) is undecidable and not recursively enumerable, and no recursively enumerable sound-and-complete proof calculus can enumerate all schematic validities.

This creates a sharp complexity separation. Ordinary propositional \(\mathrm{{InqB}}\) has the finite model property and is decidable, while its schematic fragment is \(\Pi^0_1\)-complete. Nakov and Quadrellaro also prove that \(\mathrm{{InqB}}\) is strictly algebraizable as a weak logic. Thus strict algebraizability and decidability of a weak logic do not prevent its maximal substitution-invariant fragment from being non-recursively-enumerable.

More generally, Nakov and Quadrellaro record that every intermediate inquisitive logic \(L\) in the family they study has
\[
\operatorname{{Sch}}(L)=\mathrm{{ML}}.
\]
Hence the schematic theorem problem is \(\Pi^0_1\)-complete for every such \(L\).

## Assumptions and scope
The set of propositional variables is assumed countably infinite, matching the standard statement under which the schematic-fragment identification with \(\mathrm{{ML}}\) is formulated. Complexity is measured for any fixed effective coding of formulas; changing to another computably equivalent coding does not affect the completeness statement.

The finding concerns theoremhood, equivalently validity of formulas without premises. The consequence-relation version of a schematic fragment is stronger data, but no additional complexity claim for arbitrary finite or infinite premise sets is needed here.

The phrase “intermediate inquisitive logic” is used for the family discussed by Nakov and Quadrellaro, for which they explicitly state that all members have schematic fragment \(\mathrm{{ML}}\).

## Proof
A standard result about propositional inquisitive logic identifies its schematic fragment with Medvedev's intermediate logic:
\[
\varphi\in\operatorname{{Sch}}(\mathrm{{InqB}})
\quad\Longleftrightarrow\quad
\varphi\in\mathrm{{ML}}.
\]
This is equality of sets of formulas, not merely a semantic interpretation requiring a nontrivial translation.

Pawlowski proves in 2026 that the set of theorems of \(\mathrm{{ML}}\) is \(\Pi^0_1\)-complete under computable many-one reductions. Therefore, under the same effective coding of formulas,
\[
\operatorname{{Sch}}(\mathrm{{InqB}})=\mathrm{{ML}}
\]
is immediately \(\Pi^0_1\)-complete. No loss of complexity can occur because the reduction is the identity on output formulas once the \(\mathrm{{ML}}\) theorem problem is viewed as the schematic-validity problem for \(\mathrm{{InqB}}\).

A \(\Pi^0_1\)-complete set is undecidable. It cannot be recursively enumerable: if it were both \(\Pi^0_1\) and recursively enumerable, it would be both co-recursively-enumerable and recursively enumerable, hence decidable. The same observation rules out a recursively enumerable sound-and-complete proof calculus for the schematic theorems.

Independently, propositional \(\mathrm{{InqB}}\) has the finite model property; its usual finite semantic decision method therefore gives decidability of ordinary theoremhood. Nakov and Quadrellaro prove that this same weak logic is strictly algebraizable. Combining these established facts yields the advertised separation between ordinary theoremhood and schematic theoremhood.

Finally, for every intermediate inquisitive logic \(L\) in the cited family, Nakov and Quadrellaro state
\[
\operatorname{{Sch}}(L)=\mathrm{{ML}}.
\]
The identical argument transfers Pawlowski's \(\Pi^0_1\)-completeness result to each such schematic theorem problem.

## Verification
The central transfer was checked at the level of exact set equality, so there is no hidden blow-up, encoding assumption, or one-way interpretation: schematic theoremhood for \(\mathrm{{InqB}}\) is precisely membership in \(\mathrm{{ML}}\).

The complexity implications were checked separately. Pawlowski's result is stated as \(\Pi^0_1\)-completeness under computable many-one reductions, which directly implies undecidability and non-recursive-enumerability. The finite-model-property premise used for ordinary \(\mathrm{{InqB}}\) is standard and independently recorded in the inquisitive-logic literature. The strict-algebraizability statement and the equality \(\operatorname{{Sch}}(\mathrm{{InqB}})=\mathrm{{ML}}\) are explicit in Nakov and Quadrellaro.

A parallel 2026 preprint by Almeida and Knudstorp independently proves undecidability of \(\mathrm{{ML}}\) and notes implications for schematic fragments. Its abstract does not state the exact \(\Pi^0_1\)-classification used here, so the exact complexity transfer is anchored to Pawlowski's earlier \(\Pi^0_1\)-completeness theorem.

## Relationship to prior work
Ciardelli's work on propositional inquisitive logic established the connection between schematic validity and Medvedev logic. Nakov and Quadrellaro formulate the schematic fragment for weak logics, explicitly record \(\operatorname{{Sch}}(\mathrm{{InqB}})=\mathrm{{ML}}\), prove strict algebraizability of \(\mathrm{{InqB}}\), and note that all intermediate inquisitive logics in their family have the same schematic fragment.

Pawlowski's September 2026 result settles the exact recursion-theoretic complexity of \(\mathrm{{ML}}\) as \(\Pi^0_1\)-complete. Putting these results together yields an immediate but structurally informative consequence not contained in the older schematic-fragment literature: schematic validity of \(\mathrm{{InqB}}\), and of the whole intermediate inquisitive family just described, has exact \(\Pi^0_1\) complexity. In particular, schematic closure can move from a decidable strictly algebraizable weak logic to a non-recursively-enumerable standard logic.

The Almeida--Knudstorp preprint, posted one day after Pawlowski's first version, proves undecidability of \(\mathrm{{ML}}\) by an independent route and explicitly points to schematic-fragment applications. That parallel result corroborates the undecidability consequence but does not, in its publicly indexed statement, subsume the exact \(\Pi^0_1\)-classification used here.

## Limitations
The result is a sharp transfer consequence of existing theorems, not a new lower-bound construction. Its value is the exact complexity localization to schematic validity and the separation from the complexity of the underlying weak logic.

No claim is made here about the complexity of schematic consequence with arbitrary premise sets, nor about first-order inquisitive logic. The countably infinite supply of propositional variables is part of the standard schematic-fragment setup.

The family-wide statement is limited to the intermediate inquisitive logics for which the cited algebraic-logic source establishes the common schematic fragment \(\mathrm{{ML}}\).

## References
Pawel Pawlowski, “Medvedev Logic is Not Decidable. It is \(\Pi^0_1\)-complete. Who Would Have Guessed?”, arXiv:2609.11576, first public version 2026-09-10.

Georgi Nakov and Davide Emilio Quadrellaro, “Algebraizable Weak Logics”, Journal of Symbolic Logic, 2026, DOI 10.1017/jsl.2026.10180.

Nick Bezhanishvili, Gianluca Grilletti, and Davide Emilio Quadrellaro, “An Algebraic Approach to Inquisitive and DNA-Logics”, Review of Symbolic Logic, 2021.

Rodrigo Nicolau Almeida and Søren Brinck Knudstorp, “Medvedev logic is undecidable”, arXiv:2609.13359, first public version 2026-09-11.
