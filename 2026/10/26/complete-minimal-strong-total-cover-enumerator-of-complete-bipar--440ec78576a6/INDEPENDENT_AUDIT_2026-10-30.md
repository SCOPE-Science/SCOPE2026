# Independent mathematical audit

## correctness

PASS

Classify omitted vertices U=A\X and W=B\X. For U,W both nonempty, all edges UxW are mandatory; any other selected edge is removable, so canonical covers with size m+n-a-b+ab, count binom(m,a)binom(n,b). If U nonempty,W empty, each omitted vertex must select exactly one incident edge; selected B vertices all indispensable iff its function U->B is nonconstant, giving n^a-n choices. Symmetric degeneration gives m^b-m, and all-vertex selection is unique. Subtract overlap of a=1/b=1 to count minimum covers, rewrite exponent m+n-1+(a-1)(b-1), and maximize product for terminal gaps. Direct definition exhaustively classified 575,744 candidate subsets across K2,2 K2,3 K2,4 K3,3 K3,4. Independent paper Claim13 gives prior nondegenerate structural trichotomy but not the degenerate function counts.

## originality

PASS

Best-of-knowledge: The concept is equivalent to minimal dominating sets of the subdivision/incidence graph, not ordinary domination in K_m,n. Earlier structural trichotomy is properly credited; the full coefficients and gap spectrum are additional results, derived from a refined treatment of degenerate cases. The full counting theorem is an extension, not the prior minimum result disguised. The first-case binomial term is a straightforward enumeration of prior canonical covers; the new statement is the complete total including degenerate structures and gap law. Priority and access limits explicitly preserved.

## value

PASS

A complete exact coefficient census and sharp missing-cardinality spectrum for natural incidence-graph dominating sets is useful beyond the previously known optimization minimum. The arbitrarily long gap family supplies a structural boundary showing minimal covers need not populate an interval of sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
