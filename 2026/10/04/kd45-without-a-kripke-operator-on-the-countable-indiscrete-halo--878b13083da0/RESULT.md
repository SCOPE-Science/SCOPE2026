# KD45 without a Kripke operator on the countable indiscrete halo space
## Finding

Let \(I=(\mathbb N,\{\varnothing,\mathbb N\})\) carry the indiscrete topology, and interpret \(\Diamond\) as the purely nonstandard halo modality. By the \(\omega\)-accumulation characterization of that modality, for every \(A\subseteq\mathbb N\),
\[
\omega(A)=
\begin{cases}
\mathbb N,& A\text{ is infinite},\\
\varnothing,& A\text{ is finite}.
\end{cases}
\]
The exact modal logic of this single fixed space is
\[
\operatorname{Log}_\omega(I)=\mathsf{KD45}.
\]
At the same time, \(\omega\) is nontrivial on \(I\), so the halo paper's non-representability theorem implies that no binary relation \(R\subseteq\mathbb N\times\mathbb N\) has
\[
x\in\omega(A)\quad\Longleftrightarrow\quad R(x)\cap A\ne\varnothing
\]
for every \(x\) and every \(A\subseteq\mathbb N\). Thus Kripke equivalence holds at the level of valid formulas but not at the level of the modal operator.

## Assumptions and scope

The modal language is the ordinary unimodal propositional language, with \(\Box\varphi:=\neg\Diamond\neg\varphi\). Validity means truth at every point for every valuation of propositional variables by arbitrary subsets of \(\mathbb N\).

The topology is specifically the countably infinite indiscrete topology. The result does not claim that every non-\(T_1\) space has logic \(\mathsf{KD45}\), nor that the \(\omega\)-accumulation operator is relationally representable.

## Proof

For the indiscrete topology, the only open neighbourhood of any point is \(\mathbb N\). Hence a point is an \(\omega\)-accumulation point of \(A\) exactly when \(A\) is infinite. Therefore \(\Diamond A\) is either \(\mathbb N\) or \(\varnothing\), according as \(A\) is infinite or finite. Dually,
\[
\Box A=\mathbb N\setminus\omega(\mathbb N\setminus A)
\]
is \(\mathbb N\) exactly when \(A\) is cofinite, and is \(\varnothing\) otherwise.

Soundness of \(\mathsf{KD45}\) is immediate. Normality follows from the halo semantics. For axiom \(D\), if \(\Box A=\mathbb N\), then \(A\) is cofinite and therefore infinite, so \(\Diamond A=\mathbb N\). For axiom \(4\), whenever \(\Box A=\mathbb N\), also \(\Box\Box A=\Box\mathbb N=\mathbb N\). For axiom \(5\), whenever \(\Diamond A=\mathbb N\), also \(\Box\Diamond A=\Box\mathbb N=\mathbb N\).

For completeness, let \(\varphi\notin\mathsf{KD45}\). By the standard Kripke completeness theorem for \(\mathsf{KD45}\), there is a serial, transitive, Euclidean model \(M=(W,R,V)\) and a world \(r\) such that \(M,r\not\models\varphi\). Put \(S=R(r)\). Seriality makes \(S\ne\varnothing\). If \(u\in S\), then
\[
R(u)=S.
\]
Indeed, if \(v\in S\), Euclideanness applied to \(rRu\) and \(rRv\) gives \(uRv\), so \(S\subseteq R(u)\). Conversely, if \(uRv\), transitivity with \(rRu\) gives \(rRv\), so \(R(u)\subseteq S\).

Let \(P\) be the finite set of propositional variables occurring in \(\varphi\). Two points of \(S\) have the same \(P\)-type when they agree on every variable in \(P\). Only finitely many \(P\)-types occur in \(S\). For every realized type \(t\), choose a disjoint infinite block \(B_t\subseteq\mathbb N\). If \(r\notin S\), reserve one point \(x_r\) outside the blocks and partition \(\mathbb N\setminus\{x_r\}\) into the blocks. If \(r\in S\), partition all of \(\mathbb N\) into the blocks and choose \(x_r\) inside the block having the type of \(r\).

Define a valuation on \(I\) by making each propositional variable constant on every block according to its \(P\)-type, and, when \(r\notin S\), assigning the reserved point \(x_r\) the same atomic values as \(r\).

An induction on subformulas \(\psi\) of \(\varphi\) now gives two facts. First, every point of \(B_t\) satisfies \(\psi\) exactly when a world of type \(t\) in \(S\) satisfies \(\psi\). Second, \(x_r\) satisfies \(\psi\) exactly when \(r\) satisfies \(\psi\). The Boolean steps are immediate. At the modal step, the truth set of \(\psi\) contains an entire infinite block exactly when some successor type satisfies \(\psi\). Hence it is infinite exactly when some member of \(S\) satisfies \(\psi\), which reproduces \(\Diamond\). Its complement is finite exactly when every realized successor type satisfies \(\psi\), which reproduces \(\Box\). The possible reserved point contributes only a finite exception and so does not affect either test.

Thus \(I,x_r\not\models\varphi\). Every formula outside \(\mathsf{KD45}\) therefore fails on \(I\), proving
\[
\operatorname{Log}_\omega(I)=\mathsf{KD45}.
\]

Finally, \(\omega(\mathbb N)=\mathbb N\), so \(\omega\) is nontrivial. Proposition 6.10 of Montacute's halo-semantics paper then rules out any binary relation on \(\mathbb N\) representing this operator on all subsets.

## Verification

The proof was reconstructed from the definitions. The key semantic calculation is exact: in the indiscrete topology every point has neighbourhood \(\mathbb N\), so \(\omega(A)\) is all of \(\mathbb N\) exactly for infinite \(A\). The completeness construction uses only finitely many atom-types from the counterformula and infinite blocks, so it does not require the finite-model property.

The relational step was checked directly from the serial, transitive, Euclidean frame conditions: every successor of the root has exactly the same successor set \(S\). The block construction was then checked separately for the cases \(r\in S\) and \(r\notin S\).

No finite computation is used as a substitute for the general proof.

## Relationship to prior work

Montacute introduced the purely nonstandard halo modality and proved that it coincides with the \(\omega\)-accumulation operator, that it is normal, that axiom \(4\) is universally valid, and that the operator is not Kripke-representable whenever \(\omega\) is nontrivial [1]. The paper proves \(\mathsf{K4}\) completeness over the class of all infinite spaces and explicitly identifies exact logics of single fixed infinite spaces as a direction for further work [1].

The present result gives an exact single-space logic for a canonical non-\(T_1\) space. Its completeness argument is not a consequence of the \(T_1\) collapse to Cantor-derivative semantics: the indiscrete space is not \(T_1\). Standard modal logic supplies the relational characterization of \(\mathsf{KD45}\) by serial, transitive, Euclidean frames [2]; the new step is the infinite-block simulation showing that every such counterexample relevant to a formula can be reproduced inside one fixed indiscrete \(\omega\)-accumulation model.

The result also separates two notions that can otherwise be conflated: exact agreement of validity logics and pointwise representation of the modal operator by a relation.

## Limitations

The argument uses the countably infinite indiscrete space and arbitrary set-valued propositional valuations. It does not classify the logics of other non-\(T_1\) spaces or of restricted valuation classes. It also does not provide a Kripke representation of the operator; such a representation is impossible by [1].

The originality search found no publication or indexed result stating this exact fixed-space \(\mathsf{KD45}\) characterization, but absence from the searched sources is not a proof that no equivalent observation exists elsewhere.

## References

[1] Yoàv Montacute, “Halo Semantics for Modal Logic,” *Electronic Proceedings in Theoretical Computer Science* 447 (2026), 623–635. arXiv:2606.31885. DOI:10.4204/EPTCS.447.35.

[2] Patrick Blackburn, Maarten de Rijke, and Yde Venema, *Modal Logic*, Cambridge Tracts in Theoretical Computer Science 53, Cambridge University Press, 2001. DOI:10.1017/CBO9781107050884.
