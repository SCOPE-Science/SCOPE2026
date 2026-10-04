# Review

## Correctness
PASS. The source fixes the exact 18-point configuration, proves splitting type \((7,10)\), and gives a unique minimal unexpected octic for a general assigned point. For the rational witness \(P_0=[3:5:1]\), the packaged verifier checks the 18 point equations and all 28 order-\(<7\) jet equations, exhibits a nonzero kernel vector, and obtains interpolation rank \(44\) modulo several primes. The translated curve is exactly \(A_7+B_8\) with \(\gcd(A_7,B_8)=1\). The degree-minus-multiplicity argument proves that any reducible degree-\(8\), multiplicity-\(7\) curve must have a line factor through \(P_0\), which is impossible. Generic irreducibility then follows from algebraic variation of the one-dimensional kernel and closedness of the reducible locus.

Risk: the openness step uses the source's generic uniqueness theorem, not an exhaustive symbolic computation in the two parameters of the assigned point. The use is legitimate: generic rank \(44\) forces all maximal minors to vanish identically, while the exact rank-\(44\) witness supplies a nonempty rank-constant open set.

## Originality
PASS. The closest primary source is Malara--Pokora--Tutaj-Gasińska, Example 5.10. It computes the arrangement exponents, Tjurina number, splitting type, and the existence range \(j\in\{8,9\}\), but does not state that the minimal octic for this example is irreducible. Its Theorem 5.1 records a general irreducibility criterion. Cook II--Harbourne--Migliore--Nagel provide the broader unexpected-curve framework and irreducibility criteria, not this configuration-specific certificate. Exact-coordinate, exponent-triple, source-identifier, and alias searches did not locate a publication or database finding that states or implies this explicit result.

Residual risk: a downstream paper, supplementary calculation, thesis, or other unindexed source could contain the same explicit octic or an equivalent deletion-splitting computation.

## Value
PASS. For this source example, existence of an unexpected octic was known but its basic geometric status as irreducible or reducible was left unresolved in the example itself. Irreducibility is not cosmetic here: the general theory singles it out through a deletion/splitting-type criterion, and it distinguishes one integral unexpected curve from a reducible fixed-component phenomenon. The exact witness also gives a compact reproducible method for deciding that structural question without requiring a full classification of the exceptional assigned-point locus.

## Closest literature and limitations
The lead source is arXiv:2007.04162v1 / doi:10.1007/s10711-021-00602-5, especially Theorem 5.1 and Example 5.10. The broader comparison is arXiv:1602.02300 / doi:10.1112/S0010437X18007376. The result does not classify exceptional assigned points, other singularities, or the degree-\(9\) system.

Same-model review: passed. Independent audit: not yet performed.
