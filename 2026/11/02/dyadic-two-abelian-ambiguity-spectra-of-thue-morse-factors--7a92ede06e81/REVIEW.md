# Scientific review: dyadic two-Abelian ambiguity spectra

## Correctness — PASS

The claim is restricted to distinct length-\(2^k\) factors of the binary Thue–Morse fixed point, \(k\ge2\). The argument enumerates the factors as precisely \(N\) circular conjugates of \(\mu^k(0)\) and \(2(N-1)\) distinct cut-and-join factors from complementary block pairs. Completeness and distinctness follow from the established Thue–Morse factor-complexity formula \(3N-2\) in Greinecker's introduction. The proof then reconstructs all endpoint and double-letter statistics from the cut edge, a telescoping first-prefix difference, and exact Thue–Morse pair counts. The two parity-specific eight-row tables follow by exhaustive six-case summation. The tables sum to \(3N-2\) for both parities and their smallest cases are included. A separately coded literal-factor checker passed for every \(2\le k\le10\). The checker is finite corroboration; the proof is the unrestricted justification.

## Originality — PASS, subject to historical-priority uncertainty

Greinecker, *On the 2-Abelian Complexity of the Thue–Morse Word* (arXiv:1404.3906, 2014), studies how many signatures occur, not how many distinct factor strings occupy each signature; its introductory ordinary factor-complexity formula is an explicit input here. Parreau–Rigo–Rowland–Vandomme, *A new approach to the 2-regularity of the \(\ell\)-abelian complexity of 2-automatic sequences* (arXiv:1405.3532, 2014), develops number-of-class formulae using two-block codings; the inspected sections do not give this signature-by-signature dyadic cardinality table. Dekking, *On the structure of Thue–Morse subwords* (arXiv:1405.2235, 2014), describes factor sets and block substitutions, not their partition by two-Abelian signature. Searches of published mathematical finding records for the exact dyadic spectrum, adjacent-pair histogram, factor multiplicities, and equivalent formulations found no covering claim. A general binary two-gram spectrum census does not determine the intersection sizes with the Thue–Morse factor language. Previously recorded period-doubling and Thue–Morse binomial findings use different words or different equivalences and do not imply the tables. Search failure is not a mathematical uniqueness proof; an equivalent result elsewhere remains a historical risk.

## Value — PASS

Two-Abelian complexity at powers of two is already known to be eight, but this discards the ambiguity of recovering a particular factor from its local bigram composition and endpoints. The theorem recovers **every individual ambiguity-class cardinality** in an infinite natural family, and demonstrates a genuine even/odd substitution-depth bifurcation in the limiting normalized class-size spectrum. Powers of two are canonical substitution scales rather than an arbitrary computational slice. This is a structural refinement with a clear reconstruction-theoretic motivation, not merely a repeat of the eight-class count.

## Reproducibility and limitations

The accompanying standard-library `checker.py` constructs a guaranteed-exhaustive \(8N\)-symbol prefix for each tested dyadic length, enumerates distinct factor strings, calculates adjacent-pair counts directly, checks all eight signatures, and independently verifies the proposed cut-and-join factor partition. Run `python checker.py 10`. No finite enumeration is claimed to prove the infinite theorem. The result concerns distinct strings rather than occurrence frequencies, and does not cover non-dyadic lengths or higher-order equivalence. An independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
