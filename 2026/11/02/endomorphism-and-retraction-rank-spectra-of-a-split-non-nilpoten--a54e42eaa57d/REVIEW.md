# Scientific assessment: Leibniz endomorphism and retraction rank spectra

## Correctness — PASS

The algebra is defined explicitly by its sole nonzero bracket \([v,u]=u\). Preservation of that bracket is equivalent to the outer-product identity \(\beta_f\otimes\alpha_f=a\beta\otimes\alpha\). Its split into the nonzero-derived-scalar family and two linear-space families is exhaustive and disjoint after inclusion-exclusion. Rank counts use the standard finite-field surjection formula. Idempotency is separately derived in each family: for the first singular family it requires \(T^2=T\), \(\ell T=\ell\), \(Tw_0=w_0\), and \(b=\ell(w_0)\); for the nonzero-scalar family it requires \(a=1\), \(T^2=T\), and \(Tw_0=0\). These imply the displayed polynomial expressions without unproved classification lemmas. A total-variation comparison with two full square-matrix parameter spaces establishes the limiting rank law. Exhaustive brute force independently verifies six small prime-field cases, including \(n=4,q=2\); symbolic checks cover a further 30 dimension/field-size pairs. Computation corroborates but does not replace the proof. No characteristic-two claim about the external classification theorem is made.

## Originality — PASS relative to checked material

Di Bartolo, La Rosa, and Mancini (2023), arXiv:2307.09102, is the closest primary source: its Theorem 2.2 identifies the nonnilpotent non-Lie derived-one-dimensional class in odd characteristic and Theorem 2.4(ii) gives the automorphisms. The inspected relevant sections do **not** enumerate singular endomorphisms, idempotent retractions, or their rank spectra, nor the limiting square-matrix law. The automorphism count here is a consequence of their established matrix description, and is not claimed as an independent discovery. Kurdachenko, Subbotin, and Yashchuk (2021), arXiv:2104.05922, concerns infinite-dimensional cyclic Leibniz algebras: its abstract does not imply the finite-dimensional formulas, though its full text could not be inspected. Taş and Özkurt (2023/2024) concern orbit-preserving maps on a rank-two free metabelian Leibniz algebra, with a different algebra and question. Known Gaussian-binomial idempotent counts for full matrix monoids are incorporated as tools; the new result is their nontrivial assembly after classifying the two singular components of this particular endomorphism monoid. No searched source provided a covering theorem or exact matching table. Searches cannot prove priority, and the residual risk of an equivalent formula in older literature remains.

## Mathematical value — PASS

The 2023 classification leaves the endomorphism semigroup's singular geometry and retractions quantitatively unresolved in the inspected treatment. The proposed theorem gives a **complete** rank profile for all linear algebra endomorphisms and all retracts over every finite field and every dimension, not a special-case census. Its geometric two-component decomposition explains why random endomorphisms have the same limiting corank law as arbitrary square matrices one dimension smaller, despite the noncommutative Leibniz bracket. The automorphism density has a precise exponentially small leading term. These are intrinsic, natural semigroup invariants of a classification-wide family (for odd characteristic), rather than an arbitrarily selected coefficient or elementary example. The value is exact structural enumeration, not a claimed broad downstream theorem.

## Closest sources and limitations

- A. Di Bartolo, G. La Rosa, M. Mancini, *Non-nilpotent Leibniz algebras with one-dimensional derived subalgebra* (first public 2023-07-18), arXiv:2307.09102, especially Sections 2.2–2.3 and Theorems 2.2 and 2.4.
- L. A. Kurdachenko, I. Ya. Subbotin, V. S. Yashchuk, *On the endomorphisms and derivations of some Leibniz algebras*, arXiv:2104.05922 (abstract inspected; full text not obtained).
- T. Adiyaman Taş, Z. Özkurt, *Endomorphisms which preserve orbits of free metabelian Leibniz algebras*, *Communications in Algebra* 52 (2024), 566–571, DOI 10.1080/00927872.2023.2245888 (abstract and subject inspected).

Residual risk: a prior rank-refined count for the same algebra under another name could remain undiscovered. The new formulas are algebra-intrinsic but do not classify all derived-one-dimensional non-Lie Leibniz algebras in characteristic two. The brute-force verifier only checks the explicit finite instances described in the result.

Self-review: passed. Independent audit: not yet performed.
