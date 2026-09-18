# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.**  The argument uses only the Kummer model and ramification data proved in Ma–Wang together with standard eigenspace and Möbius-transformation facts.

For even \(n\), the source gives \(\gcd(r,q^n+1)=1\) and total ramification at all \(q^2+1\) points of \(\mathbb P^1(\mathbb F_{q^2})\).  Modulo \(m=q^n+1\), the local Kummer exponents are exactly \(1\) on
\(\mathbb P^1(\mathbb F_q)\) (including infinity, since \(-q^n\equiv1\pmod m\)) and \(r\) on its complement.  These values are distinct, nonzero, and their multiplicities \(q+1\) and \(q^2-q\) are unequal.

For an automorphism normalizing the deck group, preservation of the fixed field gives a Möbius transformation on \(u\), while the cyclic eigenspace decomposition forces
\(z\mapsto h(u)z^t\) with \(t\) invertible modulo \(m\).  The Kummer equation then gives the local-exponent rule
\(e(M(Q))\equiv t e(Q)\pmod m\).  Unequal label multiplicities exclude interchange of the two classes; fixing the class labelled \(1\) forces \(t=1\).  Hence the normalizer centralizes the deck group and its base action lies in the stabilizer of
\(\mathbb P^1(\mathbb F_q)\), which is exactly \(\operatorname{PGL}_2(q)\).
Ma–Wang provide all such lifts, giving equality with their subgroup.  The center calculation follows because \(\operatorname{PGL}_2(q)\) is centerless.

Adversarial checks included the exceptional-looking cases \(q=2\), \(n=2\), and odd \(n\).  The proof remains valid for \(q=2\) when \(n\ge4\).  It correctly fails at \(n=2\), where the two labels coincide and the curve is Hermitian, and it does not extend to odd \(n\), where the second local exponent is not a unit modulo \(q^n+1\).

No empirical computation is used as a substitute for the proof.

## Originality

**PASS, to the best of our knowledge.**  Ma–Wang arXiv:2609.19546v1 constructs the subgroup of order
\((q^n+1)q(q^2-1)\) and explicitly distinguishes this from the previously known full automorphism group for odd-\(n\) BM curves.  The paper does not identify the even-\(n\) subgroup as the normalizer or centralizer of the Kummer deck group.

Beelen–Montanucci (2018) determines the full group for the older odd-\(n\) family.  Searches for the new family and equation, the arXiv identifier, Kummer/cyclic deck-group normalizers, branch-exponent formulations, and \(\operatorname{PGL}_2(q)\) stabilizers did not locate the stated even-\(n\) result.  Generalized-superelliptic uniqueness literature is not a substitute: the accessible results found are formulated for complex Riemann surfaces and/or assume centrality or a specified superelliptic structure rather than proving the finite-characteristic normalizer statement here.

The principal residual risk is the recency of arXiv:2609.19546v1: contemporaneous follow-up work may not yet be indexed.  No inaccessible paper was found whose available metadata specifically suggests prior coverage of this theorem.

## Value

**PASS.**  The source paper supplies a large explicit automorphism subgroup for its new even-\(n\) maximal curves but leaves the full automorphism group undetermined.  The theorem gives a sharp structural characterization of that subgroup: it is exactly the complete symmetry group preserving the degree-\(q^n+1\) Kummer cover, and indeed the normalizer equals the centralizer.  Therefore every possible extra automorphism must move the Kummer deck group to a distinct conjugate.  This reduces the remaining full-automorphism problem to the genuinely different question of uniqueness/conjugacy of such cyclic structures rather than further lift calculations over the same quotient.

## Sources checked

- Ma–Wang, arXiv:2609.19546v1: theorem statement, Kummer ramification lemma, and explicit automorphism subgroup section were inspected in full text.
- Beelen–Montanucci, *J. London Math. Soc.* 98 (2018): the odd-\(n\) full automorphism result was checked through the paper/authoritative bibliographic sources.
- Searches covering exact and synonymous normalizer, centralizer, Kummer, cyclic-cover, maximal-curve, and \(\operatorname{PGL}_2(q)\) terminology.
- Generalized superelliptic literature was checked for stronger general coverage; no directly implying finite-characteristic result for this family was found.
