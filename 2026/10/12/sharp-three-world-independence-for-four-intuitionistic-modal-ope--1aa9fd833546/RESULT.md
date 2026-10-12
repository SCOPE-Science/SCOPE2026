# Sharp three-world independence for four intuitionistic modal operators

## Finding

For each of the four operators in Balbiani and Gencer's intuitionistic modal semantics, there exist **two three-world frames with identical intuitionistic order** such that the three other modal truth-set operations agree on *every* upward-closed set, while the omitted operation differs. Both relations lie in the relevant threefold-confluence class, and the two relations differ by exactly one added edge. No analogous common-carrier pair exists with one or two worlds, for any preorder on that carrier. Therefore three worlds are the exact minimum for this strong operator-table separation, simultaneously for all four omissions.

In more detail, write \(P\) for Přenosil possibility, \(B\) for its box dual, \(W\) for Wijesekera possibility, and \(N\) for the other box. The relevant class is \(C_{bdu}\) for omission of \(P\) or \(W\), and \(C_{fbu}\) for omission of \(B\) or \(N\). For each omission, equality of the other three set operations implies semantic indistinguishability by *all* formulas omitting that connective, including arbitrary nesting, Heyting implication, and coimplication. The omitted connective is not expressible in the corresponding fragment.

## Assumptions and scope

A frame is \((X,\leq,R)\) where \(X\) is a nonempty finite set, \(\leq\) is a preorder, and \(R\subseteq X\times X\) is arbitrary. A valuation assigns an upward-closed set to each propositional letter. On an upward-closed input \(U\), define the following upward-closed outputs:

\[
\begin{aligned}
P_R(U)&=\{s:\exists t\leq s\;\exists u\ (tRu\land u\in U)\},\\
B_R(U)&=\{s:\forall t\geq s\;\forall u\ (tRu\Rightarrow u\in U)\},\\
W_R(U)&=\{s:\forall t\geq s\;\exists u\ (tRu\land u\in U)\},\\
N_R(U)&=\{s:\exists t\leq s\;\forall u\ (tRu\Rightarrow u\in U)\}.
\end{aligned}
\]

Composition \(A\circ B\) means that an \(A\)-edge followed by a \(B\)-edge is possible. Let \(\geq\) be the converse preorder. The four confluence conditions are
\[
\begin{aligned}
f&:\quad(\geq)\circ R\subseteq R\circ(\geq),\\
b&:\quad R\circ(\leq)\subseteq(\leq)\circ R,\\
d&:\quad(\leq)\circ R\subseteq R\circ(\leq),\\
u&:\quad R\circ(\geq)\subseteq(\geq)\circ R.
\end{aligned}
\]

The class \(C_{bdu}\) satisfies \(b,d,u\), and \(C_{fbu}\) satisfies \(f,b,u\). In a **common-carrier comparison**, both frames have the same \(X\) and \(\leq\); only \(R\) may change. Agreement of an operator means equality as a function from the set of *all* upsets of \((X,\leq)\) to itself. This is stronger than matching at one selected valuation and is narrower than comparisons using different preorders or carriers.

## Proof

**Three-world witnesses.** Use the chain \(X=\{0,1,2\}\) with \(0<1<2\). The full list of its upsets is \(\varnothing,\{2\},\{1,2\},X\). For each row, start with \(R\) and let \(R'=R\cup\{e\}\), where the added edge is displayed. The two relations are in the stated confluence class. Their three retained operators give the same full maps on all four upsets.

| Omitted operator | Class | \(R\) as ordered-pair set | Added edge \(e\) | \(O_R(\{2\})\) | \(O_{R'}(\{2\})\) |
|---|---|---|---|---|---|
| \(P\) | \(C_{bdu}\) | \(\{(0,0),(0,1),(1,2)\}\) | \((0,2)\) | \(\{1,2\}\) | \(X\) |
| \(B\) | \(C_{fbu}\) | \(\{(1,0),(1,1),(2,2)\}\) | \((2,1)\) | \(\{2\}\) | \(\varnothing\) |
| \(W\) | \(C_{bdu}\) | \(\{(0,0),(0,1),(0,2),(1,1),(2,2)\}\) | \((1,2)\) | \(\{2\}\) | \(X\) |
| \(N\) | \(C_{fbu}\) | \(\{(0,0),(0,1),(1,2),(2,1),(2,2)\}\) | \((1,1)\) | \(\{1,2\}\) | \(\varnothing\) |

Directly substituting the four possible upsets into the displayed semantic clauses verifies both the stated target discrepancies and equality of the other three entire input-output tables. For reproducibility, the relation masks in the checker, using bit \(3i+j\) for \((i,j)\), are respectively \((35,39)\), \((280,408)\), \((279,311)\), and \((419,435)\).

**Minimality at at most two worlds.** This is a complete finite classification, not an inference from sample tests. On one world there is one preorder and two modal relations. On two labeled worlds there are exactly four preorders (the discrete order, the two oriented chains, and the indiscrete preorder), with sixteen candidate relations per preorder. For each missing operator, enumerate every candidate relation satisfying its designated confluences. Compute the full truth table of all four modal operations on all upsets and index the resulting relations by the *triple* of retained operation tables. In every index class the omitted operation table is constant. The per-preorder admissible relation counts on two worlds are \(16,6,6,8\), independent of which operator is omitted; the numbers of distinct retained-table signatures are \(16,6,6,2\), respectively, and none has two different missing tables. The one-world counts are two admissible relations and two signatures. The standalone checker performs this explicit exhaustive quantification using the elementary definitions above and asserts the absence of collisions; hence a separating common-carrier pair cannot exist below three worlds.

**Arbitrary-depth nondefinability.** Fix one row and any valuation by upsets on the common preorder, identically in both frames. Atomic truth sets and the interpretations of \(\top,\bot,\wedge,\vee,\to\), and coimplication agree, since their truth clauses depend only on the preorder and argument truth sets. By structural induction, if a formula contains only the three retained modal symbols, its truth set is equal in both frames: at a modal induction step, the argument is the same upset and the retained modal operations agree on *all* upsets. But the omitted operator applied to a letter assigned \(\{2\}\) has different truth sets. This contradicts any purported definition using the three retained modalities, regardless of formula depth.

## Verification

Run `python3 verify_minimal_separation.py` (Python standard library only). Its final line must be `VERIFY_OK`. For one and two worlds the checker traverses every labeled preorder and every possible modal relation, filtering the precise three confluence axioms. It then checks the full finite operation tables, not just a distinguished upset. On three worlds it checks that each pair differs by one added edge, satisfies the required confluences, agrees on all upsets for every retained operator, and differs for the omitted operator at \(\{2\}\). Recorded output:

```
SMALL [(1, 'P', 2), (1, 'B', 2), (1, 'W', 2), (1, 'N', 2), (2, 'P', 36), (2, 'B', 36), (2, 'W', 36), (2, 'N', 36)]
WITNESSES [('P', 35, 39, [1, 2], [0, 1, 2]), ('B', 280, 408, [2], []), ('W', 279, 311, [2], [0, 1, 2]), ('N', 419, 435, [1, 2], [])]
VERIFY_OK
```

## Relationship to prior work

Balbiani and Gencer introduce these four semantic operations and prove their non-eliminability under the relevant confluence conditions, including their Proposition 21 [1]. Their larger separating frames demonstrate fragment nondefinability; they do not provide the sharp common-carrier lower bound or the four one-edge three-world witnesses proved here. The new structural statement adds an exact minimum and a uniform comparison on one fixed intuitionistic chain, without claiming that every form of modal inexpressibility requires three worlds. Earlier studies of constructive modal systems [2,3] give related semantics but do not state this four-operator finite-table threshold.

## Limitations

The lower bound applies to paired frames with a common underlying preorder and to equality of the three retained **full operation tables**. It does not classify arbitrary nonisomorphic frames on different orders, nor does it give minimal formula sizes. The four witness constructions suffice for general nondefinability in the stated frame classes, but say nothing about classes with additional constraints such as seriality, transitivity, or reflexivity of \(R\). The two-world lower-bound computation is exhaustively finite; the induction, not that computation, establishes the unlimited formula-depth assertion. Published sources may contain an equivalent reformulation under alternative terminology; the literature comparison is not a proof of absolute novelty.

## References

[1] P. Balbiani and Ç. Gencer, *Four intuitionistic modal connectives*, arXiv:2606.07348v1 (first publicly available 2026-06-05), especially the semantic definitions and Proposition 21. https://arxiv.org/abs/2606.07348

[2] P. Balbiani, H. Gao, Ç. Gencer and N. Olivetti, *A Natural Intuitionistic Modal Logic: Axiomatization and Bi-Nested Calculus*, CSL 2024. https://doi.org/10.4230/LIPIcs.CSL.2024.13

[3] A. Das and S. Marin, *On Intuitionistic Diamonds (and Lack Thereof)*, TABLEAUX 2023. https://doi.org/10.1007/978-3-031-43513-3_16
