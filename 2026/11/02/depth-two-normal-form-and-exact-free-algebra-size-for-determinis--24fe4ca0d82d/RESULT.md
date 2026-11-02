# Depth-two normal form and exact free-algebra size for deterministic weakly transitive modal logic

## Finding

Let \(\mathcal C\) be the class of all Kripke frames \((W,R)\), including arbitrary nonempty infinite frames, satisfying both **partial functionality** \(xRy\land xRz\Rightarrow y=z\) and **weak transitivity** \(xRy\land yRz\Rightarrow(z=x\lor xRz)\). Consider ordinary Boolean propositional modal logic with one accessibility modality, with \(\Diamond\) existential and \(\Box\) its dual. For every integer \(k\geq0\), let \(q=2^k\), the number of possible truth assignments to its \(k\) propositional letters.

**Theorem.** There are exactly \(3q^2\) distinct complete pointed \(k\)-variable modal theories on \(\mathcal C\). Every one has a defining formula of modal depth at most two. Each subset of the \(3q^2\) types is definable, and hence the Boolean-modal algebra of formulas over \(k\) variables modulo validity on \(\mathcal C\) has **exactly**

\[
\bigl|F_{\mathcal C}(k)\bigr|=2^{3q^2}=2^{3\cdot4^k}.
\]

Its Boolean reduct is the powerset of the explicitly described type set, with \(\Diamond\) given by inverse image along its partial successor function. The depth-two bound is optimal for every \(k\geq0\). Moreover, one \(k\)-valued Kripke model representing *all* pointed types needs at least \(3q^2\) worlds, and this lower bound is attained by a model in \(\mathcal C\).

For example, \(F_{\mathcal C}(0)\) has \(8\) elements, \(F_{\mathcal C}(1)\) has \(4096\) elements, and \(F_{\mathcal C}(2)\) has \(2^{48}=281474976710656\) elements. No special rule for the zero-variable case is necessary: the empty conjunction fixing the sole colour is \(\top\).

## Assumptions and scope

The relation \(R\) is not required to be serial, reflexive, symmetric, or transitive. Each point has at most one accessible world (which may be the starting world itself), so a self-loop is permitted, and a missing successor is permitted. Both finite and infinite frames are included. The only syntax is ordinary finitary Boolean modal syntax generated from \(k\) variables and \(\Diamond\), with its usual \(\Box\) dual; no hybrid nominals, counting, global modalities, or extra constants occur. Logical equivalence means agreement at every world under every valuation on every frame in \(\mathcal C\).

A colour \(a\in Q\) is one of the \(q=2^k\) valuations of the propositional variables. Let \(\kappa_a\) be the complete conjunction of positive/negative literals specifying colour \(a\). A type label below records colour and accessibility, not the number or identity of other, unrelated worlds in the frame.

## Proof

**Step 1: every pointed generated subframe has one of five shapes.** Since every world has at most one successor, denote that possible successor by \(f(x)\), and let \(f(x)\) be undefined for terminal worlds. If \(f(x)=y\ne x\) and \(f(y)=z\), weak transitivity says \(z=x\) or \(xRz\). Functionality and \(xRy\) force the second alternative to be \(z=y\). Thus \(z\in\{x,y\}\). The entire forward behaviour from \(x\) is therefore either (i) no successor, (ii) a loop, (iii) one edge to a sink, (iv) one edge to a loop, or (v) a two-cycle. The same argument applies even if the ambient frame is infinite. In shapes (iv) and (v), if the two participating worlds have the same colour, the rooted modal theory is identical to a monochromatic self-loop: the colour-preserving relation identifying these states with one loop is a bisimulation.

**Step 2: complete type set.** Define the following disjoint labels, with \(a,b\in Q\):

* \(T(a)\): colour \(a\), no successor; there are \(q\) such labels.
* \(F(a)\): colour \(a\), a perpetual monochromatic successor stream; there are \(q\).
* \(L(a,b)\): colour \(a\), one successor of colour \(b\) with no successor; there are \(q^2\).
* \(R(a,b)\): colour \(a\), successor of *different* colour \(b\) which loops; there are \(q(q-1)\).
* \(P(a,b)\): colour \(a\), successor of *different* colour \(b\) returning to the starting world; there are \(q(q-1)\).

The total is \(q+q+q^2+2q(q-1)=3q^2\). Define a canonical frame whose worlds are exactly these labels. The successor of \(T(a)\) is undefined; \(F(a)\) succeeds to itself; \(L(a,b)\) to \(T(b)\); \(R(a,b)\) to \(F(b)\); and \(P(a,b)\) to \(P(b,a)\). Assign the indicated colour to each label. This canonical relation is partial-functional and weakly transitive. For every pointed model in \(\mathcal C\), the colour-preserving rooted successor stream agrees with exactly one canonical type; the preceding shape classification supplies a bisimulation. Hence every formula's truth value depends only on its type.

**Step 3: define each type by a depth-two formula.** For any \(a,b\in Q\), define

\[
\begin{aligned}
\chi_{T(a)}&=\kappa_a\land\neg\Diamond\top,\\
\chi_{F(a)}&=\kappa_a\land\Diamond(\kappa_a\land\Diamond\kappa_a),\\
\chi_{L(a,b)}&=\kappa_a\land\Diamond(\kappa_b\land\neg\Diamond\top),\\
\chi_{R(a,b)}&=\kappa_a\land\Diamond(\kappa_b\land\Diamond\kappa_b),\quad a\ne b,\\
\chi_{P(a,b)}&=\kappa_a\land\Diamond(\kappa_b\land\Diamond\kappa_a),\quad a\ne b.
\end{aligned}
\]

On any canonical state, these formulas identify exactly the corresponding label: a missing edge distinguishes \(T\); a terminal child distinguishes \(L\); two consecutive occurrences of the root colour distinguish \(F\); for different colours at the first two steps, equality of the second and third colours distinguishes \(R\) from \(P\). At no point is a deeper observation required. Therefore distinct canonical labels are modally inequivalent, and the \(3q^2\) canonical labels exhaust all pointed modal theories.

**Step 4: free-algebra identification.** Write \(\mathcal T_k\) for the canonical type set. The truth set of every \(k\)-variable formula is a subset of \(\mathcal T_k\), and this truth-set map preserves Boolean operations and \(\Diamond\); its kernel is exactly equivalence modulo \(\mathcal C\). For every \(S\subseteq\mathcal T_k\), the finite disjunction \(\bigvee_{t\in S}\chi_t\) has precisely truth set \(S\). Thus the map is surjective onto \(\mathcal P(\mathcal T_k)\) and induces a Boolean-modal algebra isomorphism \(F_{\mathcal C}(k)\cong\mathcal P(\mathcal T_k)\). In particular \(\bigl|F_{\mathcal C}(k)\bigr|=2^{3\cdot4^k}\). The modal operation in this isomorphism is \(\Diamond S=\{t:\operatorname{succ}(t)\in S\}\), with undefined successors contributing no elements.

**Step 5: depth and size sharpness.** Choose any colour \(a\). A self-loop of colour \(a\) and a two-world path with colours \(a,a\) ending in a sink agree at the root for all modal formulas of depth at most one, because each root and its unique successor have the same propositional colour in both models. Yet \(\Diamond\Diamond\top\) is true in the self-loop and false in the two-world path. Therefore modal depth one cannot define every complete theory (or every term function), and depth two is sharp. Finally, in any single fixed-valuation model representing all complete pointed theories, each of the mutually exclusive formulas \(\chi_t\) requires a distinct witness world. There must be at least \(3q^2\) such worlds, and the canonical model above has exactly that many. The minimum refers to one model with one fixed valuation, not to a family of smaller models under changing valuations.

## Verification

The included standalone `checker.py` evaluates the structural condition on all partial successor functions on labelled carriers of sizes one through six. It exhaustively checks every binary colouring and every pointed world in these frames, comparing actual depth-two semantic signatures with the predicted canonical types (5,596,204 rooted coloured cases). It also tests pairwise distinctness and characteristic formulas for \(q=1,2,3\), and verifies the depth-one versus depth-two witness. Its observed final line is `ALL_CHECKS_OK; examined rooted coloured cases= 5596204`. These finite tests corroborate but do not prove the universal all-size statements; Steps 1–5 constitute the proof.

To reproduce, run `python3 checker.py` using only the Python standard library. The program operates in finite memory and does not require other files.

## Relationship to prior work

Santschi and Vooijs, *Logics Containing wK4: Selection à la Fine* (public preprint June 30, 2026), studies general weakly transitive frames and their selection/finite-model methods, providing the recent context and definition of weak transitivity. Its Theorems A–C address finite model properties and finite width, not this partial-functional free-algebra count. General local-tabularity results for extensions of weakly transitive modal logic establish finite-type behaviour under height restrictions but do not, in the inspected statements, give the above explicit rank-dependent formula. Standard one-successor bisimulation principles and Boolean modal algebra duality are used, not claimed as discoveries. The contribution asserted here is the complete five-family type classification **together with** exact free-algebra cardinalities, depth-two tightness, and the jointly minimal universal coloured model for this particular intersection of frame conditions.

The older 2012 *Canonical Formulas for wK4* article proves general axiomatizability results, not the stated explicit census in its accessible abstract. The previously reported partial-function characterization of marked modal measurable quotients concerns a different representation problem and cannot imply the count without imposing and analyzing weak transitivity. An earlier equivalent presentation under monounary-algebra or locally tabular modal-logic terminology remains possible: a failed literature search is not a uniqueness proof.

## Limitations

This is an exact result for frames satisfying **both** weak transitivity and partial functionality; it does not apply to arbitrary weakly transitive branching frames or all deterministic frames without weak transitivity. The algebra counts equivalence classes of finitary formulas, not syntactic formulas. It does not determine the complexity of arbitrary proof search, axiomatization length, or higher-arity modalities. The historical-priority comparison remains limited by inaccessible earlier full texts and may require specialist verification. No independent audit has been performed.

## References

1. Simon Santschi and Niels C. Vooijs, *Logics Containing wK4: Selection à la Fine*, arXiv:2606.31920 (first publicly posted June 30, 2026), *Advances in Modal Logic 2026*, EPTCS 447, 674–690. DOI:10.4204/EPTCS.447.38. https://arxiv.org/abs/2606.31920
2. Guram Bezhanishvili and Nick Bezhanishvili, *Canonical Formulas for wK4*, *Review of Symbolic Logic* 5 (2012), 731–762. DOI:10.1017/S1755020312000251.
3. Valentin Shehtman and Ilya Shapirovsky, *Local Tabularity Without Transitivity*, publicly available presentation (2016), https://www.sambuz.com/doc/local-tabularity-without-transitivity-ppt-presentation-823192 .
4. Guram Bezhanishvili, Silvio Ghilardi, and Mamuka Jibladze, *An Algebraic Approach to Subframe Logics. Modal Case*, *Notre Dame Journal of Formal Logic* (2011), foundational finite-model treatment over weak transitivity.
