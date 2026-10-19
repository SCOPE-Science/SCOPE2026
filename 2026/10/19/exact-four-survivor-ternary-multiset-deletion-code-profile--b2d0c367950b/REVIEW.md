# Scientific review: exact four-survivor ternary multiset codes

## Correctness
PASS. The four-survivor criterion is exactly the bound \(I(x,y)\le3\). The heavy-coordinate injection gives at most three heavy codewords. All light vectors are excluded at \(n\ge10\), two light vectors are incompatible at \(7\le n\le9\), and certificate counting gives at most three light vectors for \(n=6\). The nine explicit incompatible triples at \(n=5\) each cover mutually incompatible words, and every light word belongs to at least two triples, bounding light codewords by four. Explicit constructions attain every resulting upper bound. The standalone checker confirms all finite certificates and independently computes optima through \(n=10\). The infinite statement rests on the written proof, not on enumerations.

## Originality
PASS within the examined literature and indexed mathematical records. The 2026 primary study of multiset deletion codes (arXiv:2601.05636) covers the related three-survivor regime and ternary one-deletion code size, including the already-known \(n=5\) endpoint, but not the complete four-survivor ternary classification at \(n\ge6\). A published three-survivor ternary exact profile likewise has a different minimum-distance condition. The general discrete-simplex framework (arXiv:1612.08837) and March 2026 deletion-ball work (arXiv:2603.18322) do not imply these exact values in their inspected results. The main residual risk is an equivalent finite-alphabet packing result indexed under other terminology.

## Value
PASS. Fixing the survivor count is a natural high-deletion regime with sharply distinct finite-length behavior. The theorem completely determines the first four-survivor ternary profile, including two nontrivial intermediate plateaux and the exact pure-code stabilization threshold. This is a natural complete classification of an infinite parameter slice; it is not presented as a general-alphabet or general-survivor theorem.

## Limits
There is no census of all optimizing code families. One endpoint, \(n=5\), follows from known single-deletion theory. The result has not received independent external mathematical validation.

Self-review: passed. Independent audit: not yet performed.
