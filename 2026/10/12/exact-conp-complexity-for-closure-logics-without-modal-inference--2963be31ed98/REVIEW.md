# Review

## Correctness

PASS. The propositional lower bounds are immediate. For the upper bound, the primary source supplies one-point countermodels with finite syntactic generators for every no-inference system. The potentially infinite \(\mathsf C\)-closure is handled by a relevance normalization: a conjunction created outside the input-relevant subformula set cannot contribute new information by later \(\mathsf M\)-decomposition, and implications used by \(\mathsf K\) are never manufactured by the conjunction rules. Hence all closure facts needed to evaluate the input are obtained by a worklist saturation over a polynomial-size finite set. A guessed one-point model is therefore polynomially checkable, giving NP satisfiability and coNP validity.

## Originality

PASS. The primary source proves only primitive-recursive decidability and explicitly identifies exact computational complexity as a remaining problem. The closest exact complexity literature concerns the classical congruential non-normal cube whose minimal logic already contains replacement of equivalents. That literature therefore does not imply the result for Nishimura's systems with no modal inference rules. Focused searches under closure-semantics, non-congruential, least-modal, and NP/coNP formulations did not locate an equivalent classification.

## Value

PASS. This closes the explicit complexity question for the entire no-inference half of the source's closure-semantics family: all sixteen systems remain exactly at propositional NP/coNP complexity. It also exposes a meaningful boundary with the classical congruential cube, where adding agglomeration can produce PSPACE complexity. The distinction shows that modal inference/congruence, not merely the presence of \(\mathsf C\), is computationally decisive in these weak systems.

## Closest literature and limitations

Nishimura (2026) supplies the new closure semantics, singleton completeness construction, finite model property, and primitive-recursive decision procedure. Dalmonte--Mazzullo (2023) is the closest exact complexity comparison, but its systems extend a minimal logic containing replacement of equivalents. Pascucci--Sedlár supplies relevant non-congruential semantic background; only its abstract and bibliographic metadata were available in the lawful noninteractive access paths checked, so overlap hidden in the full paper remains a stated residual risk.

The theorem does not cover systems containing \(\mathsf E\) or \(\mathsf G\), and it does not assert finiteness of unrestricted closures.

Self-review: passed. Independent audit: not yet performed.
