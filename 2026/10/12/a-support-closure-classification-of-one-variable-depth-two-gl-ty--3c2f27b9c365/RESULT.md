# A support-closure classification of one-variable depth-two GL types
## Finding

For the one-variable modal language over transitive conversely well-founded Kripke frames, let \(V=\{0,1\}\) be the two valuations of the variable and encode the depth-one type of a world by \((v,T)\in V\times\mathcal P(V)\), where \(v\) is its own valuation and \(T\) is the set of valuations occurring at its accessible successors. A candidate successor spectrum \(S\subseteq V\times\mathcal P(V)\) occurs below a world if and only if the least support closure beginning with all \((v,\varnothing)\in S\) and repeatedly adding \((v,T)\in S\) whenever every \(q\in T\) has an already-supported witness \((q,U)\in S\) with \(U\subseteq T\), eventually equals \(S\). Exactly \(85\) of the \(256\) candidate spectra satisfy this criterion. Hence there are exactly \(170\) pointed semantic types of modal depth at most \(2\) with one propositional variable, and therefore exactly \(2^{170}\) semantic equivalence classes of one-variable formulas of modal depth at most \(2\), even when countable conjunctions and disjunctions are allowed.

The support-closure criterion is valid more generally for every finite valuation alphabet \(V\): a finite set
\[
S\subseteq V\times\mathcal P(V)
\]
is realizable as the set of depth-one types of successors of a point in a transitive conversely well-founded frame exactly when the same support closure reaches all of \(S\).

For one propositional variable, \(|V|=2\), so there are eight possible depth-one types and \(256\) candidate spectra. Exhaustive evaluation of the proved criterion gives the size distribution
\[
1,2,5,12,21,22,15,6,1
\]
for realizable spectra of cardinalities \(0,1,\ldots,8\), respectively; these entries sum to \(85\).

## Assumptions and scope

A Kripke frame is a pair \((W,R)\). The relation \(R\) is assumed transitive and conversely well-founded, hence irreflexive. A valuation of the single propositional variable \(p\) is coded by \(0\) or \(1\). Accessibility means the full Kripke relation \(R\), not merely the cover relation of a transitive reduction.

For a world \(x\), write
\[
v(x)\in V=\{0,1\},\qquad T(x)=\{v(y):xRy\}.
\]
Its depth-one type is
\[
\tau_1(x)=(v(x),T(x)).
\]
For a distinguished root \(r\), its successor spectrum is
\[
S(r)=\{\tau_1(x):rRx\}.
\]

For a candidate \(S\subseteq V\times\mathcal P(V)\), define \(C_0\) to be the members \((v,\varnothing)\) of \(S\). Inductively, let \(C_{n+1}\) contain \(C_n\) together with every \((v,T)\in S\) such that
\[
\forall q\in T\ \exists (q,U)\in C_n\quad U\subseteq T.
\]
Because \(S\) is finite, this stabilizes; write \(C_\infty\) for the stable set.

The semantic-equivalence count concerns formulas using only \(p\), Boolean operations, the modal operator, and optionally countable conjunctions or disjunctions, with modal depth at most \(2\). It is not a count for the unrestricted-depth language.

## Proof

Assume first that \(S=S(r)\) in a transitive conversely well-founded model. For every type \(s=(v,T)\in S\), choose an occurrence \(x_s\) of type \(s\) with minimum converse-well-founded rank. If \(T=\varnothing\), then \(s\in C_0\). Otherwise fix \(q\in T\). There is \(y\) with \(x_sRy\) and \(v(y)=q\). Put \(\tau_1(y)=(q,U)\). Transitivity gives
\[
U\subseteq T.
\]
Moreover \(y\) has strictly smaller rank than \(x_s\), so the minimum rank of the type \((q,U)\) is strictly below the minimum rank of \(s\). Induction on these minimum ranks therefore shows that every member of \(S\) enters the support closure. Thus \(C_\infty=S\).

Conversely suppose \(C_\infty=S\). Give each \(s\in S\) the least stage \(h(s)\) at which it enters the closure. For each \(s=(v,T)\) and each \(q\in T\), choose a witness
\[
t_{s,q}=(q,U)\in S
\]
with \(U\subseteq T\) and \(h(t_{s,q})<h(s)\). Create one world \(x_s\) for every \(s\in S\), put an edge from \(x_s\) to each chosen \(x_{t_{s,q}}\), and take the transitive closure. Heights strictly decrease along generating edges, so the resulting relation is finite, transitive, and irreflexive.

For \(s=(v,T)\), every \(q\in T\) occurs at a chosen successor, hence \(T\) is contained in the set of successor valuations of \(x_s\). In the other direction, along every generated edge \(s\to(q,U)\) one has \(q\in T\) and \(U\subseteq T\). Consequently every valuation appearing farther down any path also lies in \(T\). Thus \(x_s\) has depth-one type exactly \(s\). Add one new root and connect it to every \(x_s\); after transitive closure its successor spectrum is exactly \(S\). This proves the criterion.

For one variable there are exactly
\[
2\cdot 2^2=8
\]
depth-one types, hence \(2^8=256\) candidate spectra. The accompanying checker exhausts all \(256\) candidates. It evaluates the support closure and, independently, searches all linear orders of each candidate spectrum for an order in which every required witness occurs earlier. The two tests agree on all \(256\) cases and accept exactly \(85\); it also constructs and rechecks a finite transitive irreflexive witness frame for every accepted spectrum. The two possible root valuations therefore give exactly
\[
2\cdot85=170
\]
realizable pointed depth-two types.

Finally, each finite-depth type has a finitary characteristic formula. For a depth-one type \((v,T)\), take the literal describing \(v\), require every successor valuation to lie in \(T\), and require a successor of each valuation in \(T\). Apply the same construction one level higher to a root valuation and a realizable successor spectrum. Hence distinct realized depth-two types are separated by formulas of depth at most \(2\), and every subset of the \(170\) realized types is definable by a finite disjunction of characteristic formulas. Every infinitary formula of this fragment denotes such a subset, so the semantic quotient has exactly
\[
2^{170}
\]
classes.

## Verification

The structural equivalence above is proved without computation. Computation is used only for the finite cardinality \(85\).

The supplied `verify_depth2.py` exhausts all \(256\) spectra. It compares two decision procedures: fixed-point support closure and an exhaustive permutation criterion. It reports zero mismatches. For every accepted spectrum it separately builds the finite witness frame from closure stages, takes its transitive closure, and recomputes every node's depth-one type and the root spectrum; it reports zero construction failures.

The exact checker output is recorded in `checker_output.txt`. No sampling, timeout inference, or unbounded search is used.

## Relationship to prior work

Mojtahedi, Pakhomov and Soldà introduce a countably infinitary version of Gödel-Löb provability logic and study proof systems against transitive conversely well-founded Kripke semantics. Their paper supplies the immediate literature setting for asking what the infinitary language can distinguish in low modal depth, but the inspected statements do not give an exact one-variable depth-two semantic quotient or the support-closure criterion above.

Classical GL completeness already identifies transitive conversely well-founded frames as the relevant semantics, and standard bounded-bisimulation or characteristic-formula methods explain why a fixed finite variable set and fixed finite modal depth yield only finitely many semantic types. Those general facts do not determine which of the \(256\) one-variable depth-two successor spectra survive the GL frame condition. The new point is the exact support obstruction and its complete converse, from which the count \(85\), the \(170\) pointed types, and the \(2^{170}\) quotient follow.

Recent work on uniform interpolation for GL gives effective elimination of propositional variables, but its advertised result is different: it does not state the support-closure classification or the exact shallow type counts used here.

## Limitations

The exact numerical count is only for one propositional variable and modal depth at most \(2\). The support-closure theorem itself allows any finite valuation alphabet, but no closed formula is asserted here for the number of realizable spectra in larger alphabets.

The result is semantic. It does not settle the global comparison between the infinitary Hilbert-style and deep-inference proof systems, nor does it claim a new unrestricted decision procedure for infinitary GL.

The originality search cannot exclude an older equivalent formulation hidden in universal-model or finite-type literature under different terminology; no such statement or the numbers \(85\) and \(170\) were located in the targeted searches described in the review.

## References

1. Mojtaba Mojtahedi, Fedor Pakhomov, Giovanni Soldà, “Infinitary provability logic,” arXiv:2609.24795v1, first posted 21 September 2026.
2. Hugo Férée, Iris van der Giessen, Sam van Gool, Ian Shillito, “Mechanised Uniform Interpolation for Modal Logics K, GL, and iSL,” arXiv:2402.10494v2; IJCAR 2024, pp. 43–60.
3. Stanford Encyclopedia of Philosophy, “Provability Logic,” section on modal completeness, for the classical completeness of GL with respect to transitive conversely well-founded frames and finite transitive irreflexive trees.
