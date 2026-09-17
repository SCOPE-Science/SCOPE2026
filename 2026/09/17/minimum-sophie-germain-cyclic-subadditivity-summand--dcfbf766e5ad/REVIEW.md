# Review

**Same-model review: passed. Cross-model review: not yet performed.**

The finding was assessed separately for correctness, originality to the best of our knowledge, and scientific value. This status is not independent validation or peer review.

## Correctness

The proof was checked at the points most likely to fail.

1. **Cyclic-number structure.** For every cyclic integer r > 2, evenness is impossible because phi(r) is even, and a repeated prime factor is impossible because p^2 | r implies p | phi(r). Thus the oddness and squarefreeness claims used in the residue lemma are valid.
2. **Residue translation.** For Sophie Germain cyclic a > 2, squarefreeness of a excludes a = 0 mod 9, while squarefreeness of 2a+1 excludes a = 4 mod 9. Intersecting these exclusions with odd residues modulo 18 gives exactly {1,3,5,7,11,15,17}.
3. **Window convention.** Subadditivity fails exactly when the window (n,n+m] contains more Sophie Germain cyclic integers than [1,m]. For 2 <= m <= 20 and n >= m, this window starts above 2, so every Sophie Germain cyclic in it obeys the residue lemma. The m=1 case is handled separately.
4. **Packing table.** Exhausting the 18 starting residues modulo 18 gives maximum allowed-residue counts 1,1,2,2,3,3,4,4,5,5,6,6,6,6,7,7,7,7,8,8 for lengths 1 through 20. These are termwise at most C_sigma(m), computed from the exact initial list 1,2,3,5,7,11,15,17.
5. **Sharp witness.** The window (87088,87109] contains exactly nine Sophie Germain cyclic integers: 87089, 87091, 87095, 87099, 87101, 87103, 87105, 87107, 87109. Since C_sigma(21)=8, this gives a counterexample at (21,87088). The compact verification artifact independently recomputes the relevant factorizations, totients and gcds using only the Python standard library.

No cumulative evaluation of C_sigma(87088) is needed.

## Originality

### Prior literature inspected

- Cohen, *Conjectures about Primes and Cyclic Numbers* (J. Integer Sequences 28 (2025), Article 25.4.7; arXiv:2508.08335), states Conjecture 66 as the subadditivity inequality for C_sigma and reports no counterexample in his tested range.
- Ibarra, arXiv:2607.09793 (2026), disproves Conjecture 66 at (31,3928). The paper describes the window interpretation and notes that counterexamples are not rare, but its stated theorem and exhibited construction do not minimize the shorter summand.
- OEIS A397387 records the Sophie Germain cyclic sequence and links Cohen and Ibarra.
- The withdrawn preprint arXiv:2509.26138 concerns many other conjectures about cyclic numbers; its current abstract identifies Sophie Germain cyclic results for Cohen's Conjectures 36 and 37, not the subadditivity Conjecture 66.

Searches were made for exact and synonymous formulations involving the minimum or smallest shorter summand, Sophie Germain cyclic subadditivity, m=21, 87088, and 87109, as well as the Ibarra paper identifier and follow-up citations. No covering result was located. Current SCOPE records were also searched for the mathematical object and claim family; no overlapping record was found.

### Residual originality risk

Originality remains to the best of our knowledge rather than exhaustive. The main residual risk is an unindexed or very recent follow-up to Ibarra's July 2026 note that sharpens his counterexample without appearing in the searches above. No specifically identified inaccessible paper was found whose title or available metadata suggested it likely contains this minimum-summand result.

## Value

The contribution is not another arbitrary counterexample. It converts Ibarra's shorter summand 31 into an exact optimum and supplies a global obstruction proving that every smaller value is impossible. The same mod-18 argument explains why the transition occurs at 21: the local packing maximum is at most the initial counting function through length 20 and first exceeds it at length 21. This is a concise structural sharpening of a recently disproved conjecture.
