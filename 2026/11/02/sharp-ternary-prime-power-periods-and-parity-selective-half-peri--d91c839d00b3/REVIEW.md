# Scientific review: exact ternary periods of A158690

## Correctness
**PASS.** The exact degree-five coefficient identity for \(G\) is reconstructed from the defining finite products. The Stirling-number expansion has integer coefficients, so factorial divisibility gives a uniform finite exponential representation modulo each \(3^r\). A binomial lifting congruence transfers an exact modulo-nine two-step obstruction to every ternary prime-power level. Euler's theorem proves the proposed period; the two maximal proper divisors are ruled out separately. The supplied program independently checks the initial coefficients and many exact finite cases.

## Originality
**PASS under the available-source comparison, with residual priority risk.** Kallat's published abstract announces Carmichael's function as an *eventual period*, not a *least* period; the precise parity-selective ternary obstruction is not asserted there. The OEIS entry records the modulo-sixteen example and general period conjecture, not a complete ternary minimum. Related Stirling-transform work establishes upper periods, which do not logically imply sharpness. Targeted statement-level searches and accessible earlier research-claim comparisons found no covering exact ternary theorem. Kallat's full PDF could not be read, so an implicit earlier result is not excluded.

## Mathematical value
**PASS.** Determining the *minimal* eventual period across every power of a fixed prime answers a natural quantitative question left open by the general Carmichael upper bound. The answer proves that the upper bound is sharp at all ternary levels and exposes a uniform parity-sensitive obstruction, in contrast to the previously observed smaller dyadic periods. This is a complete, infinite prime-power classification with a structural lifting proof, not a finite table or isolated numerical improvement.

## Closest literature and limitations
The precise source comparisons and inaccessible-full-text risk are given in `AUDIT.json`. Only prime-power moduli for the prime three are classified; the earliest onset of periodicity is not optimized. Direct external independent mathematical audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
