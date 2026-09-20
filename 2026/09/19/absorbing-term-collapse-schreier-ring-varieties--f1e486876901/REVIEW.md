# Same-model review

## Correctness

**PASS.** The proof reduces the new structural claim to Theorem 4.1 of Kearnes--Moorhead--Szendrei. For a finite member \(A\), the product \(A\times A\) is finite and therefore permutational. Fixing one absorbing coordinate with a parameter whose second component is the distinguished constant traps a unary polynomial inside the proper slice \(A\times\{e\}\), so it cannot be a permutation. Permutationality makes it constant. Evaluating the variable in a second absorbing coordinate at \(e\) identifies that constant as \((e,e)\). Local finiteness then extends the resulting identity from finite members to all members.

The ring corollary was checked separately. Once multiplication vanishes, the one-generated free ring is a finite cyclic additive group \(\mathbb Z/n\mathbb Z\). If \(n\) is composite, multiplication by a prime divisor of \(n\) is a unary polynomial that is neither constant nor bijective, contradicting minimality. Thus \(n=p\) is prime. The resulting \(p\)-element zero ring generates exactly the zero-multiplication \(\mathbb F_p\)-vector-space variety, proving both necessity and sufficiency. The unital contradiction follows from \(1\cdot1=1\) versus zero multiplication.

Potential edge cases were checked: the one-element finite algebra causes no problem; nontriviality ensures the one-generated free ring is not one-element; and the product-slice argument uses polynomial operations with parameters, exactly as in the definition of a permutational finite algebra.

## Originality

**PASS, to the best of our knowledge.** Kearnes--Moorhead--Szendrei, arXiv:2609.19651v1 (submitted 17 September 2026), prove the general local-finite Schreier/minimality equivalence. The inspected version does not contain the word “absorbing” and does not state a ring specialization. Its closing section treats groups, semigroups, Lie algebras, and \(M\)-sets as classical comparisons.

Burgin (1974) is the closest older source inspected in full-text form. Theorem 3 classifies homogeneous Schreier varieties of linear \(\Omega\)-algebras over a commutative coefficient ring via a residue-field condition and a combinatorial condition; Proposition 4 reduces Schreier \(\Omega\)-ring varieties to linear \(\Omega\)-algebras over a prime residue field. The paper also lists trivial multiplication as a known Schreier example. Those statements are treated as prior art. They do not state the local-finiteness obstruction forcing every two-coordinate absorbing term to collapse, nor the exact conclusion that every nontrivial locally finite Schreier ring variety has zero multiplication and prime exponent.

Targeted searches for “Schreier variety” together with “absorbing term”, “zero multiplication”, “square-zero”, “locally finite rings”, and equivalent ring-language formulations did not locate the theorem proved here. The principal residual originality risk is implicit coverage in older universal-algebra literature or a short corollary of Burgin's framework that was not stated explicitly. Because the new proof is elementary once the 2026 minimality theorem is available, concurrent independent observation is also plausible.

## Value

**PASS.** The absorbing-term theorem extracts a reusable structural mechanism from the abstract 2026 classification. It simultaneously explains why multiplicative or bracket-like structure disappears in locally finite Schreier settings whenever the distinguished constant absorbs in two coordinates. For rings it yields a complete classification, including nonassociative rings, associative rings, unital rings, and fixed-field algebras. It also recovers the abelian collapse in the classical locally finite group case as a consistency check.

## Scope and limitations

The result concerns nontrivial locally finite Schreier varieties with a constant term. The absorbing-term theorem requires absorption in two distinct argument positions. The ring classification uses the standard additive-group ring language, with multiplication not assumed associative unless stated. It does not classify arbitrary locally finite varieties, non-Schreier varieties, or Schreier varieties without local finiteness.

Originality is to the best of our knowledge. No independent validation, formal verification, or peer review is claimed.

**Same-model review: passed. Independent audit: not yet performed.**
