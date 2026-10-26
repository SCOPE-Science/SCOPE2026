# Scientific review — Complete Harshad-base classification for even semiprimes

## Correctness — PASS
For every odd prime \(p\), the only possible proper positive digit-sum divisors of \(2p\) are \(1,2,p\). The proof exhausts all three cases. The nontrivial cases are rigid: sum \(p\) implies \(b-1\mid p\), and sum two reduces to either one digit \(2\), or two digits \(1\). Valuations handle the binary branch and the factorization of \(x^h+1\) for odd \(h\) forces every nonbinary higher exponent to be a power of two. All reverse implications are checked, the base-union disjointness is established, and a union bound plus the prime number theorem gives density one. This is a universal proof rather than a finite-data inference. `verify.py` independently checks all bases for 195 odd primes through 1200 and the larger nine-base example.

## Originality — PASS subject to stated priority limitations
The precise all-base count appears in OEIS A080221; OEIS A100263 lists five-base cases and the 2016 entries A271311/A271313 give explicit square-root, fourth-root and Fermat-type examples. Those cases are not claimed novel. The present statement proves exhaustiveness for **all** odd primes, includes every iterated square root, and establishes a quantitative exceptional-prime bound of \(O(\sqrt X)\); no inspected source states an implication covering this combined result. Targeted searches for equivalent formulations and prior digit-sum/Harshad-base classifications did not locate stronger coverage. This search is not a proof of historical uniqueness. Residual risk is that an unlocated earlier characterization already implies the classification or density claim.

## Value — PASS
This solves a natural minimal-divisor-count slice of the all-base Harshad problem singled out by the archived sequence comments. It replaces isolated five-, six-, and seven-base observed patterns by an exact classification at every even semiprime, supplies a rare explicit nine-base prime witness and proves that five bases occur for a density-one subset of primes. The density result makes a precise distinction between the common behavior and exceptional arithmetic power constraints. No assertion about infinitude of the exceptional prime classes is needed.

## Sources and limits
Primary records inspected: OEIS A080221 (2003), A100263 (2004), A271311 and A271313 (2016), including their comments and examples. General fixed-base Harshad literature does not by itself settle a count across all radices. All accessible primary comparisons are documented in AUDIT.json. Priority risks are acknowledged; the standalone verifier is finite, while the theorem is supported by the proof.

Self-review: passed. Independent audit: not yet performed.
