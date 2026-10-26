# Review of the exact cycle formula

## Correctness — PASS

The proof establishes \(T\equiv q-1\pmod{q^n-1}\), and thus the exact factorization \(K^\times=HL^\times\) with \(H\cap L^\times=\mathbb F_q^\times\) and \(q-1\) representations per nonzero element. It then derives \(F^m(uz)=u^{r^m}\mathcal L^m(z)\), solves a cyclic power equation with exactly \(\gcd(r^m-1,S)\) roots when permitted, and counts precisely the nonzero vectors in each scalar eigenspace. The fixed-point and Möbius inversion identities follow without asymptotic assumptions. The self-contained checker directly verifies all cycles and all predicted iterate counts for seven parameter cases in three exact finite fields.

## Originality — PASS, with documented residual risk

The precise all-iterate scalar-eigenspace and gcd formula is not stated in the motivating 2026 lift paper, which treats inverses and selected involutions. The 2026 linearized-cycle paper treats the smaller field without this nonlinear lift. Bors and Wang's full Section 6.2 provides a broad, pre-existing wreath-product cycle algorithm for generalized cyclotomic permutations, and hence an overarching route to calculate any particular example; this is acknowledged rather than misrepresented. Their general algorithm does not itself state the direct closed scalar-eigenkernel expression here. Multiple mathematical-result searches found no same claim. Residual risk remains that the expression is implicit or independently recorded in another treatment of cyclotomic maps.

## Value — PASS

The source construction introduces a new infinite family of nonlinear sparse permutation maps whose inverses are tractable but whose full iteration dynamics are not given. This formula recovers all periodic data for arbitrary exponents in that family through smaller-field linear algebra instead of enumerating the large extension. It unifies cycle lengths, order, and sign for exponent-one lifts and exhibits nontrivial cycle transitions for other exponents. The mathematical object and invariant are natural: full orbit decomposition of explicit permutation polynomial constructions.

## Scope and risks

No statement is made for arbitrary sparse maps. The existence of general cyclotomic cycle algorithms remains explicit prior art. The finite checker is a corroboration, not an infinite-domain proof or an independent certification.

Self-review: passed. Independent audit: not yet performed.
