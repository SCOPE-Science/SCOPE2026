# Parity Separation for the Binomial Family f_n = a^n b a^n − b^{n+1} in Q<a,b>

## Context

Let A = Q<a,b> be the free associative algebra on two generators over the rationals and for each integer n ≥ 2 let f_n = a^n b a^n − b^{n+1}. Let I = (f_n : n ≥ 2) be the two-sided ideal they generate. The ambient investigation asks whether I is finitely generated: either a finite subfamily generates all f_n via explicit two-sided ideal-membership expressions, or for arbitrarily large finite subfamilies there are finite-dimensional separating representations killing the subfamily while keeping some later f_N nonzero. The monomial cycle-plus-projector ansatz is a natural first attack surface for the non-generation direction. This record establishes its M = 2 base step rigorously plus a classification delimiting that ansatz.

## Definitions

Let P ∈ M_4(Z) be the 4-cycle shift with P[i][(i+1) mod 4] = 1 and 0 elsewhere, i.e.
P = [[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]].
Let B = diag(1,0,1,0) ∈ M_4(Z). By the universal property of the free algebra, a ↦ P, b ↦ B extends uniquely to a unital Q-algebra homomorphism ρ: Q<a,b> → M_4(Q). Write ρ(f_n) = P^n B P^n − B^{n+1}. B is an idempotent diagonal projector: B^2 = B, hence B^k = B for all k ≥ 1. More generally, for L ≥ 1 let A_L be the L-cycle shift and D_S = diag(1_S) for S ⊆ Z/L.

## Result

Theorem A (parity separation). With P, B, ρ as above, ρ(f_n) = 0 if and only if n is even. In particular ρ(f_2) is the zero matrix while ρ(f_3) = [[−1,0,0,0],[0,0,0,1],[0,0,−1,0],[0,1,0,0]] ≠ 0. Consequently f_3 ∉ (f_2) and (f_2) ⊊ (f_2, f_3, …) ⊆ I.

Lemma B (monomial classification). For A = L-cycle shift and B = diag(1_S) with S nonempty, the induced representation kills f_n iff 2n ≡ 0 (mod L) and S + n = S; if S = ∅ every f_n vanishes (zero representation). Hence no representation in this class kills f_2 and f_3 while keeping some later f_N nonzero: even-index zero sets come in full even families.

## Proof / Evidence

Write P^n = Σ_i E_{i,i+n} and B = Σ_k b_k E_{k,k} with b = (1,0,1,0), indices mod 4. Matrix multiplication gives the exact sandwich formula P^n B P^n = Σ_i b_{i+n} E_{i,i+2n}. Thus the diagonal entry (P^n B P^n)[i][i] equals b_{i+n} when 2n ≡ 0 (mod 4) and 0 otherwise. If n is even, 2n ≡ 0 (mod 4) and 2-periodicity b_{i+n} = b_i gives P^n B P^n = B = B^{n+1}, so ρ(f_n) = 0. If n is odd, 2n ≡ 2 (mod 4) ≠ 0, so P^n B P^n is purely off-diagonal with zero diagonal; then ρ(f_n) = (off-diagonal) − B has diagonal (0,0,0,0) − (1,0,1,0) = (−1,0,−1,0) and is explicitly nonzero, e.g. the displayed ρ(f_3). Since ρ(f_2) = 0, ρ factors as σ ∘ π through π: A → A/(f_2); σ(π(f_3)) = ρ(f_3) ≠ 0 forces π(f_3) ≠ 0, i.e. f_3 ∉ (f_2). Lemma B follows by the same rotation computation with period L: A^n B A^n combines rotation of support S by n with a shift by A^{2n}, and diagonality plus idempotence give exactly the stated arithmetic condition; the S = ∅ case gives B = 0 so all f_n map to 0.

Machine verification uses exact integer arithmetic, hence valid over Q: output/artifacts/verify_parity.py asserts ρ(f_n) == 0 ⟺ n even for n = 2..12 with printed f_2, f_3 witnesses (PASS); output/artifacts/verify_monomial.py checks Lemma B for all L ≤ 8 and n = 2..10 (4590 checks, 0 mismatches) and the corollary that no triple (L ≤ 8, S) has f_2 = f_3 = 0 with some f_4..f_10 nonzero (PASS). Bounded-degree two-sided membership linear programs over Q independently returned NONMEMBER for f_3 ∈ (f_2) at degree ≤ 8 and f_4 ∈ (f_2,f_3) at degree ≤ 9, consistent with but weaker than Theorem A. Full proof text is in output/artifacts/parity_theorem.md.

## Limitations

This record does not decide finite generation of the whole infinite ideal I = (f_n : n ≥ 2). No proof is given that every finite subfamily fails to generate I, nor any finite generating set with full membership certificates. Non-monomial separators beyond M = 2 remain undiscovered; lane searches found negative signals (10704-element f_2 = f_3 = 0 locus in M_3(F_2) with no separator; Jordan-deformation kernel collapse for sizes up to 8; Lemma B monomial no-go) delimiting but not closing the tail. Bounded LP checks are degree-truncated consistency evidence only.

## Reproducibility

Run python3 output/artifacts/verify_parity.py and python3 output/artifacts/verify_monomial.py with any Python 3 interpreter (no dependencies); both use exact integer matrix arithmetic and assert the claimed parities and classification. Recompute P^n B P^n − B^{n+1} by hand from the sandwich formula to confirm the diagonal argument.

## References

- Parity theorem proof text: output/artifacts/parity_theorem.md.
- Exact scripts: output/artifacts/verify_parity.py, output/artifacts/verify_monomial.py.
- Draft summary: DRAFT context in lane inputs (not part of public record).
- Background: Bergman diamond lemma / noncommutative Gröbner-basis enumeration; Hofstadler–Levandovskyy modular Gröbner bases in free algebras (classical infinitely generated example ⟨xy^nx⟩); Shibuta on finite generating sets of infinitely generated ideals (commutative setting); Eto on binomial/lattice ideals (commutative setting). None states or implies the submitted parity claim.
