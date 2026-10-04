# Minimal permutative lifts preserve linear recurrence
## Finding
Let \(Y\) be a two-sided linearly recurrent subshift and let \(h\) be a permutative sliding block code with finite window length. Write \(X=\eta_h^{-1}(Y)\) for the full lift. If \(X\) is minimal, then \(X\) is linearly recurrent.

Kang and Jäger identify \(X\) with a finite skew product \(T(y,u)=(\sigma y,\Phi_{y_0}(u))\), where the fiber is finite and each \(\Phi_a\) is a permutation. In this representation the result is the following permanence statement: a minimal finite permutation extension of a linearly recurrent subshift by a locally constant permutation cocycle is linearly recurrent.

As a consequence, every such minimal lift is uniquely ergodic, since linearly recurrent subshifts are uniquely ergodic.
## Assumptions and scope
The base \(Y\) is a two-sided linearly recurrent subshift over a finite alphabet. The fiber is finite, and the cocycle takes values in a finite permutation group and is locally constant. Passing to a higher-block presentation makes the cocycle one-block without changing linear recurrence up to its constant. The extension itself is assumed minimal. The periodic base case is finite and immediate, so the substantive argument concerns the aperiodic case.

For the permutative-code application, \(h\) is as in Kang and Jäger's finite-window permutative class, and their conjugacy theorem supplies precisely the finite permutation skew-product representation used below.
## Proof
Fix a linear-recurrence constant \(L\) for \(Y\). After higher-block recoding, write the extension as
\[
T(y,u)=(\sigma y,\rho(y_0)u),
\]
with finite fiber \(F\) and \(\rho(a)\in\operatorname{Sym}(F)\).

A lifted word \(W\) of length \(n\) is determined by its base word \(w\in\mathcal L_n(Y)\) together with its initial fiber state \(u\in F\): all later fiber symbols are obtained by multiplying the successive permutations prescribed by the letters of \(w\).

Consider successive returns of the base orbit to the cylinder \([w]\). Linear recurrence gives two uniform facts. First, every return word to \(w\) has length at most \(L|w|\). Second, the alphabet of return words has uniformly bounded cardinality, and the derived systems obtained from cylinders of \(Y\) range over only finitely many systems up to the standard return-word conjugacies. These are the return-word finiteness properties used in the finite-extension argument of Bruin.

Induce \(T\) on the clopen set \([w]\times F\). Because \(T\) is minimal, this first-return system is minimal. In return-word coordinates it is a finite permutation extension of the derived shift: a return word \(r\) acts on \(F\) by the product of the one-step permutations encountered along \(r\). The fiber group is finite. Combining the finite family of derived systems with the finite set of possible permutation labels gives a constant \(N\), independent of \(w\), such that in every one of these minimal induced extensions any prescribed fiber state is revisited within at most \(N\) return steps. This is exactly the compact finiteness mechanism in Bruin's finite permutation-extension lemma; no metric estimate depends on the chosen cylinder.

Each of those return steps has ordinary length at most \(L|w|\). Thus, once an occurrence of \(w\) is reached, the same base word with the same initial fiber state recurs within at most \(NL|w|\) further symbols. Reaching the first occurrence of \(w\) costs at most another \(L|w|\) symbols. Therefore every length-\(n\) lifted word recurs with gaps bounded by
\[
(N+1)Ln.
\]
This is linear recurrence of the coded skew product. Kang and Jäger's conjugacy transfers the property back to \(X\).
## Verification
The proof uses only three structural inputs that were checked in the cited sources: the exact finite permutation skew-product representation of a permutative lift; the standard uniform return-word bounds and finite-derived-system property of a linearly recurrent subshift; and the finite permutation-extension recurrence argument in Bruin's treatment of linearly recurrent speedups.

The crucial quantifier is uniformity in the cylinder word \(w\). It is supplied by finiteness of the derived-system family together with finiteness of the permutation fiber, not by checking individual cylinders. No finite computation or experimental enumeration is used as a substitute for the argument.
## Relationship to prior work
Kang and Jäger prove that permutative lifts are finite permutation skew products and characterize minimality through transitivity of return permutations. They state that a minimal permutative lift of a primitive substitution subshift is linearly recurrent, while noting that a general proof for primitive substitutions belongs to work in preparation; their paper supplies a direct argument for noble-means examples. The statement here replaces the primitive-substitution hypothesis by the intrinsic assumption that the base is linearly recurrent.

Bruin proves that transitive homeomorphic speedups of linearly recurrent subshifts are linearly recurrent. A key lemma in that proof controls a finite permutation-group extension over derived shifts by exploiting the finiteness of derived systems. The present argument isolates that mechanism from the speedup construction and applies it to the finite skew products arising from permutative lifts. Bruin's theorem does not itself state permanence for arbitrary minimal finite permutation extensions or for permutative lifts.

Durand's return-word theory supplies the standard quantitative recurrence and finite-derived-system background. Searches using the phrases “linearly recurrent finite group extension subshift”, “linearly recurrent skew product subshift permutation”, “permutative lift linearly recurrent subshift minimal finite extension”, and close variants did not locate a published theorem with the statement above.
## Limitations
Minimality of the finite extension is essential to the proof: without it, an induced fiber state can lie in a proper invariant component, so the uniform fiber-return step fails. The result is qualitative with respect to the final recurrence constant; it proves existence of a global linear constant but does not optimize it in terms of the base constant, fiber size, or coding window.

A closely related manuscript announced by Kang and Jäger as work in preparation was not publicly available in the checked sources. It is therefore a residual literature-overlap risk. The result here should not be read as a claim about that unavailable manuscript.
## References
- A. Kang and T. Jäger, *On lifts of strictly ergodic subshifts by permutative sliding block codes*, arXiv:2609.01140v1, first public 2026-09-01.
- H. Bruin, *Speedups of linearly recurrent subshifts*, arXiv:2602.13652v1, first public 2026-02-14.
- F. Durand, *Linearly recurrent subshifts have a finite number of non-periodic subshift factors*, arXiv:0807.4430v1.
