# Self-review: square-inradius Pythagorean hypotenuse count

## Correctness — PASS

The classical Euclid representation gives \(r=n(m-n)\). Because \(\gcd(n,m-n)=1\), \(r\) is a square exactly when \(n=u^2\) and \(m-n=v^2\). The primitive condition is precisely \(\gcd(u,v)=1\) with \(v\) odd. The hypotenuse becomes \((u^2+v^2)^2+u^4\). Every pair is positive and produces one unordered triangle, and vice versa. A monotone boundary yields the \(O(t+1)\) odd-lattice estimate; Möbius inversion over odd divisors gives factor \(8/\pi^2\), while polar integration yields the stated \(\kappa\). The error is \(O(X^{1/4}\log(2X))\). Two-path integer regression using two different enumerations agreed through hypotenuse two million, but the proof of infinitude is purely mathematical. No assumptions about primality or unverified infinite computation are needed.

## Originality — PASS (with disclosed access risks)

Robbins's two-page original 2006 publication, inspected in full, counts primitive triangles for a **given** inradius; its \(T(r)=2^{\omega_*(r)}\) does not impose the hypotenuse cutoff. OEIS A087459 is an exact database of excess values ordered by hypotenuse, not an unbounded \(X\)-asymptotic. OEIS A020887 indexes the same excess without that order. The closest identified published numeric study of square *perimeters* is not a square-*inradius* study. Searches for alternate square-inradius wording, quartic coordinate formulation, ordered OEIS excess and direct asymptotic terminology found no statement that subsumes this claim. Omland's fixed-inradius paper and O'Loughlin's inradius geometry note were not available in full; their existence and the possibility of an unindexed prior hypotenuse-specific asymptotic remain genuine risks rather than certified absence.

## Mathematical value — PASS

The natural inradius-square subfamily has an exact growth scale and positive explicit constant under the standard hypotenuse height. This is an arithmetic counting problem with nontrivial simultaneous coprimality, parity and quartic region; the main term and quantified error are not inferred by numerically extending a table. The result clarifies the scarcity of a geometric square constraint across primitive right triangles and is meaningful without a broader classification theorem.

## Limits and evidence

The theorem does not concern nonprimitive triangles, square perimeter, optimal error terms or a fixed value of the inradius. The finite regression checks only bounded integer examples; it does not serve as proof of the all-real-\(X\) estimate. Closest literature is Robbins (2006), OEIS A087459/A020887 and Omland (2017). Priority and independent validation are not asserted.

Self-review: passed. Independent audit: not yet performed.
