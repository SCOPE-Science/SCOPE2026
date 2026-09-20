# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The argument was checked at the level of functions, not merely polynomial parameter tuples. Fan's coprime-index criterion gives the fixed-index exponent classes. The unit reduction map from modulus \(q^e-1\) to modulus \(\ell_e(q)\) gives the stated number of lifts, and the coefficient condition removes exactly \(\ell_e(q)\) nonzero field elements.

The key collision step reduces admissible exponents modulo \(q^e-1\). Neither support exponent is zero modulo \(q^e-1\), and the two support exponents are distinct. Equality on all nonzero field elements therefore forces equality of the reduced two-term polynomials. A cross-index equality must reverse the support, which forces both coefficients to equal 1 and gives \(d'=-d\) and \(r'=r+d(q-1)\). The identity \(q^h\ell_{e-h}=\ell_e-\ell_h\) proves that this reversal maps an admissible exponent at \(d\) to an admissible exponent at \(-d\). The coefficient \(a=1\) satisfies Fan's condition exactly when the characteristic is odd and \(e\) is odd. No unit index is self-antipodal because \(\ell_e(q)>2\) for \(q>2\).

Adversarial checks included possible zero reduced exponents, coincident monomial supports, self-antipodal indices, multiple values of \(h\), and the parity of \((-1)^{\ell_e(q)}\). The exact-integer verification artifact checks the exponent/index involution and the final formulas for several parameters in both exceptional and nonexceptional parity regimes. It is supporting evidence rather than a substitute for the proof.

## Originality

Xiang Fan's arXiv:2609.20354v1 was inspected in the relevant parts. Corollary 1.3 counts distinct permutation functions for the \(d=1\) family. Corollary 6.1 then classifies \(X^r(X^{d(q-1)}+a)\) for every fixed coprime index \(d\). In the inspected version, the explicit distinct-function enumeration remains attached to the \(d=1\) family; no all-coprime-index collision theorem or global count was located in Section 6.

Hou--Pallozzi Lavorante, arXiv:2111.06533, was also inspected in the relevant sections. It defines equivalence of permutation binomials under output scaling, Frobenius, and monomial substitution. That relation preserves permutation behavior but is not equality of functions, so its canonical-form theory does not provide the equality-collision count proved here.

External searches used exact and synonymous formulations involving coprime-index permutation binomials, distinct permutation functions, equality/collisions, antipodal indices, and \(X^r(X^{d(q-1)}+a)\). No matching prior theorem was found. The originality assessment is therefore to the best of our knowledge rather than an exhaustive literature guarantee. The main residual risk is unindexed contemporaneous work, since the motivating classification was submitted on 17 September 2026. No inaccessible paper was identified whose available metadata specifically suggests the same theorem.

## Value

The result closes the natural counting problem left after the fixed-index classification. It identifies the complete cross-index collision mechanism rather than merely producing another parameter count. In particular, it shows that multiplying the fixed-index count by \(\varphi(\ell_e(q))\) is correct except in one parity regime, and supplies the exact correction there. The subset formula also records how collisions behave for arbitrary selected collections of coprime index classes.

## Scope

The theorem counts equality of functions \(\mathbb F_{q^e}\to\mathbb F_{q^e}\), not equivalence under changes of variables or output scaling. It concerns the coprime-index regime \(\gcd(d,\ell_e(q))=1\); it does not address the non-coprime-index classification problem.
