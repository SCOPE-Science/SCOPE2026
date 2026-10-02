# Independent mathematical audit

## correctness

PASS

The one-deletion problem is exactly the 0-1 packing of 625 words against 125 length-three output constraints. Independently executed the actual package's artifacts/verify_q5.py with installed SciPy 1.17.1; it verified all 42 witness shadows pairwise disjoint, reproduced N(4,4,1)=24, and returned N(4,5,1)=42 with HiGHS status optimal and reported zero MIP gap. The proof is computer-assisted and relies on the solver's numerical branch-and-bound correctness; it does not provide a stand-alone exact dual/branch certificate.

## originality

PASS

The nearest complete primary theorem treats even alphabet sizes and expressly says its odd-size upper bound is not sharp. The quinary exact value is not implied by that theorem, by perfect-code existence, or by general hypergraph/LP formulations. Best-of-knowledge with a specific uninspected 2012 computational-paper risk.

## value

PASS

This odd-alphabet length-four case is a natural exact coding invariant, and the computer-assisted value42 improves the already published q=5 upper bound45. Such exact small-parameter values benchmark code constructions and bounds; no general theorem is required by the standard. Priority remains best-of-knowledge with the specifically named2012 source risk; this is not a claim of an exact rational certificate or universal first publication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
