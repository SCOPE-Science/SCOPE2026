# Four semantic classes in the variable-free fragment of KB

## Finding
Let \(\mathbf{KB}\) be the normal propositional modal logic determined by all symmetric Kripke frames, in the language generated from \(\bot\), implication, and \(\Box\). Every variable-free formula \(A\) is \(\mathbf{KB}\)-equivalent to exactly one of
\[
\bot,\qquad \top,\qquad \Box\bot,\qquad \neg\Box\bot.
\]
Consequently, the variable-free Lindenbaum quotient of \(\mathbf{KB}\) has exactly four elements. Equivalently, a variable-free formula is determined by its two truth values at an isolated world and at a nonisolated world.

A direct algorithm follows: compute a profile \(\pi(A)=(a_{\mathrm{iso}},a_{\mathrm{non}})\in\{0,1\}^2\) bottom-up. Variable-free \(\mathbf{KB}\)-validity holds exactly when \(\pi(A)=(1,1)\), so this fragment is decidable in linear time in the syntax-tree size. Together with the known PSPACE-completeness of the one-variable fragment, this locates the first hard finite-variable level of \(\mathbf{KB}\) at one propositional variable.

## Assumptions and scope
A Kripke frame is \((W,R)\) with nonempty \(W\). Symmetry means \(wRv\) implies \(vRw\). A world is isolated when it has no \(R\)-successor. Equivalence is semantic equivalence over all symmetric frames, using the standard Boolean and normal-modal semantics. The result concerns the ordinary one-modal propositional language; additional modalities or propositional quantifiers are outside scope.

## Proof
For a variable-free formula \(A\), define \(\pi(A)=(a_{\mathrm{iso}},a_{\mathrm{non}})\), where the two coordinates are the truth values of \(A\) at, respectively, any isolated world and any nonisolated world of a symmetric frame. We prove simultaneously by structural induction that these values are well-defined and satisfy the following recursion.

First,
\[
\pi(\bot)=(0,0).
\]
Implication is coordinatewise classical implication: if \(\pi(A)=(a_i,a_n)\) and \(\pi(B)=(b_i,b_n)\), then
\[
\pi(A\to B)=(\neg a_i\lor b_i,\neg a_n\lor b_n).
\]
It remains to analyze \(\Box\). At an isolated world, \(\Box A\) is vacuously true. At a nonisolated world \(w\), there is at least one successor. Every successor \(v\) is itself nonisolated, because symmetry gives \(vRw\). By the induction hypothesis, \(A\) therefore has the same truth value \(a_n\) at every successor of \(w\). Hence
\[
\pi(\Box A)=(1,a_n).
\]
These clauses prove that every variable-free formula has one of only four profiles.

All four profiles occur:
\[
\pi(\bot)=(0,0),\qquad
\pi(\top)=(1,1),\qquad
\pi(\Box\bot)=(1,0),\qquad
\pi(\neg\Box\bot)=(0,1).
\]
Distinct profiles are genuinely inequivalent. If two profiles differ in the isolated coordinate, a one-world frame with empty accessibility relation separates them. If they differ in the nonisolated coordinate, a two-world frame with one symmetric edge and no loops separates them. Therefore there are exactly four equivalence classes.

The profile recursion visits each syntax node once, proving the linear-time decision claim. The cited 2018 work establishes PSPACE-hardness for the one-variable fragment of \(\mathbf{KB}\), and the standard PSPACE upper bound for \(\mathbf{KB}\) applies to its fragments, giving the stated complexity threshold.

## Verification
The accompanying `verify_closed_kb.py` independently evaluates generated variable-free formulas by direct Kripke semantics on every symmetric frame with at most four worlds. It checks that direct truth agrees with the two-coordinate recursion and that exactly four profiles occur. This finite computation is a sanity check only; the theorem for arbitrary formulas and arbitrary symmetric frames is supplied by the structural induction above.

## Relationship to prior work
Rybakov and Shkatov's 2018 paper proves that finite-variable fragments of modal logics of symmetric frames remain PSPACE-hard, including the one-variable fragment of \(\mathbf{KB}\). Their 2022 paper on products explicitly notes that \(\mathbf{KB}\) does not have infinitely many pairwise non-equivalent variable-free formulas, but does not give an exact count or the four normal forms in the material inspected. Earlier work on constant formulas and finite-variable complexity was also checked for overlap; the accessible descriptions establish broad decidability and complexity phenomena but did not supply this exact \(\mathbf{KB}\) classification. The present statement sharpens the cited finiteness observation to a complete four-class normal form and makes the zero-to-one-variable complexity jump explicit.

## Limitations
The novelty assessment is literature-search based, not a proof that no inaccessible or differently phrased source contains the same elementary classification. An older paper specifically on constant formulas in modal logics was identifiable bibliographically but its full text was not available in the sources inspected; this remains the principal residual overlap risk. The finite verification script does not replace the induction proof.

## References
1. M. Rybakov and D. Shkatov, “Complexity of finite-variable fragments of propositional modal logics of symmetric frames,” *Logic Journal of the IGPL* 27(1), 60–68. First published online 2 July 2018. DOI: 10.1093/jigpal/jzy018.
2. M. Rybakov and D. Shkatov, “Complexity of finite-variable fragments of products with non-transitive modal logics,” *Journal of Logic and Computation* 32(5), 853–870. First published online 17 January 2022. DOI: 10.1093/logcom/exab080.
3. A. V. Chagrov and M. N. Rybakov, “How Many Variables Does One Need to Prove PSPACE-hardness of Modal Logics?”, *Advances in Modal Logic*, Vol. 4, 71–82, 2003.
4. A. V. Chagrov, “Finite Model Property of Normal Modal Logics and Constant Formulas: an Example,” *Logical Investigations* 21(1), 2015.
