# Scientific review: exact block-palindrome widths of Dyck words

## Correctness — PASS

Every ordinary border of a Dyck word has nonnegative balance as a prefix and nonpositive balance as a suffix, forcing balance zero; this verifies the decisive Dyck-border lemma. The shortest border is unbordered and nonoverlapping, and removal of its two copies leaves a Dyck center. The converse construction is bijective, proving the coefficient recurrence and generating function. An exchange argument demonstrates that iterated shortest-border peeling reaches maximum width. Catalan square-root transfer applied to the analytic multiplier \(U(z^2)\) proves the limiting odd-geometric distribution and mean. Direct exhaustive enumeration of all \(290511\) nonempty Dyck words through semilength \(12\), together with exact coefficient recurrences through semilength \(80\), corroborates—not replaces—the infinite proof. Potential subtlety about overlapping borders is explicitly handled by the unbordered shortest-border property.

## Originality — PASS, with disclosed risk

The closest full-text source is Gabrić–Shallit (2023), which provides a greedy block-palindrome framework and unrestricted fixed-alphabet enumeration, not the Catalan-restricted width series or an odd-geometric law. Barcucci–Bernini–Pinzani (2021) construct selected non-overlapping Dyck codes rather than enumerating all Dyck words by literal border structure. Mol–Rampersad–Shallit (2023) treat pattern avoidance and automatic-word factors. Blanchet-Sadri–Chen–Hawes (2017) concern Abelian borders, which are not literal borders. Searches for Dyck block-palindromes, bifix-free Dyck-path enumeration, ordinary versus Abelian borders, and the exact initial unbordered-Dyck coefficient list found no explicit coverage. Relevant general border-decomposition machinery is acknowledged as prior; an alternative formulation in uncatalogued enumerative combinatorics remains a residual risk.

## Mathematical value — PASS

The result unifies two natural objects—Catalan balanced-parenthesis languages and greedy block-palindrome decompositions—by a structural border-closure property not shared by arbitrary context-free word languages. It gives every finite semilength/width count and establishes a limiting odd-geometric law with an explicitly computable parameter and mean. The limiting law goes beyond running an existing fixed-alphabet recurrence and answers an intrinsic average-case question about balanced words. It makes no claim about general multitype Dyck languages or unrelated code families.

Self-review: passed. Independent audit: not yet performed.
