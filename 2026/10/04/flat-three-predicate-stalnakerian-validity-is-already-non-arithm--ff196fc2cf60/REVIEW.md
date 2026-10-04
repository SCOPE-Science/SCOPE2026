# Review

## Correctness

PASS. The source's arithmetic interpretation uses the conditional connective only inside \(N,<,\equiv\). Expanding those abbreviations gives exactly three templates, each with quantifier-free and conditional-free operands. The definitions of zero and successor, \(\mathrm{Ax1}\)--\(\mathrm{Ax8}\), and the relativized arithmetic translation add quantifiers only outside those templates. Therefore every translated arithmetic sentence belongs to the stated flat fragment.

The arithmetic equivalence is used only for sentences. The concrete reverse-direction model was checked directly: its tail-minimum selection function satisfies the four weak Stalnakerian conditions, and at world \(0\) the source's definitions recover ordinary natural-number order and equality while the stipulated ternary predicates give addition and multiplication. Hence true arithmetic computably reduces to restricted validity. If that restricted set were arithmetical, true arithmetic would be arithmetical, a contradiction.

## Originality

PASS. The primary paper proves non-arithmeticity of the full quantified logic, notes that only three predicates are needed, and explicitly asks which natural fragments remain axiomatizable. It does not discuss flatness, conditional nesting depth, or quantifier-free conditional scopes.

The closest published finding on the same source confines the arithmetic lower bound to one explicit frame; that is a semantic frame restriction and does not imply a syntactic flat-fragment lower bound. Standard flat-fragment work in conditional logic is propositional and supplies proof systems rather than this quantified non-arithmeticity result. Targeted searches found no equivalent theorem.

## Value

PASS. The source ends by asking for natural axiomatizable fragments. Flatness is a standard and proof-theoretically meaningful restriction in conditional logic, and banning quantifiers inside conditional scopes is an especially natural first-order simplification. Showing that neither restriction helps, even with only three predicate symbols and three conditional templates, sharply narrows where a positive fragment theorem can still occur.

## Closest literature and limitations

Kocurek--Walsh--Weiss (2026) provides the arithmetic encoding and the open fragment question. Olivetti--Pozzato (2015) demonstrates that flat fragments are an established proof-theoretic boundary in propositional conditional logic. Cresswell (1997) supplies related quantified-modal arithmetic-encoding background.

The result leaves bounded first-order quantifier rank and purely monadic signatures open, and it does not determine the exact complexity above the arithmetical hierarchy.

Same-model review: passed. Independent audit: not yet performed.
