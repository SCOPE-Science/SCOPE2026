# Scientific review: complete null-polynomial module of a 128-element ring

## Correctness — PASS

The ring is the seven-dimensional \(\mathbb F_2\)-algebra \((A,B)\) with multiplication \((A,B)(C,D)=(AC,AD+BC)\). The seven proposed generators are shown null for every ring element through the exact identities for \(t(r)\), \(t(r)^2\), and \(t(r)^3\), where \(t=x+x^2\). Their leading coefficients are linearly independent, giving a reduction to thirty normal monomials. An explicitly indexed thirty-by-thirty evaluation matrix has determinant one in \(\mathbb F_2\); `verify.py` constructs the matrix from the multiplication law and checks this determinant by exact elimination. Thus the generators are complete for **all** polynomial degrees. The Smith invariants follow from a two-by-two presentation matrix, and the constant stabilizer and sharp degree-six threshold follow by coefficient multiplication. The checker was run successfully on the actual supplied file.

No finite sampling is extrapolated: the finite certificate proves exact independence, while the leading-term argument proves the unbounded-degree claim. A separate independent audit is still outstanding.

## Originality — PASS, with stated residual risks

V. Havlovec, *Null polynomials over a finite ring need not form a two-sided ideal* (arXiv:2608.13251, first submitted 2026-08-13), is the closest result. Its explicit counterexample uses the **same ring** and its degree-six null polynomial is precisely the final generator of the present presentation. These known facts are not claimed as original. Inspection of the complete accessible paper's introduction, counterexample proof, and subsequent remarks showed no seven-generator description, no Smith invariant factors, no exact constant right-stabilizer, and no lower bound on the degree of a failing null polynomial.

Havlovec, *Integer-valued polynomials over structural matrix rings* (arXiv:2608.13242, also first submitted 2026-08-13), was inspected through its structural matrix hypotheses and main ideal and polynomial-characterization results, especially Theorems 4.9/4.13 and Corollary 4.15. Those results concern rings specified by allowed positions; the equality between diagonal blocks makes the present ring a different object, and the structural-matrix positive theorems do not imply this description. Werner, *Polynomials that kill each element of a finite ring* (2014), establishes positive classes and the original conjectural setting, not the claimed module structure, as far as accessible abstract/publisher preview and later citations establish. Targeted exact-title and algebraic-equivalence searches found no covering theorem. An unindexed treatment of this exact example or a stronger polynomial-function presentation remains possible and is the principal residual risk.

## Value — PASS

The source's single degree-six obstruction was a counterexample to a long-standing finite-ring conjecture. This result determines **all** null polynomials for that canonical counterexample, the complete finite polynomial-function module and its \(2^{30}\) function count, and the exact index-two ring of allowable constant right multipliers. It also proves that the original degree-six witness has the smallest possible degree even when multiplied on the right by an arbitrary polynomial, a natural sharp bound on the first occurrence of the obstruction. The full presentation explains the failure mechanism rather than adding an isolated example or a routine numerical count. The theorem is intentionally restricted to this motivated finite ring; extrapolation to arbitrary finite rings is not claimed.

Self-review: passed. Independent audit: not yet performed.
