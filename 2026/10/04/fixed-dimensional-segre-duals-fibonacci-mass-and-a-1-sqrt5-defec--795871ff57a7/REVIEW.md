# Same-model review

## Correctness
PASS. The dual determinantal identification follows directly from the Segre tangent space. Giambelli--Thom--Porteous gives the claimed degree. The ratio polynomial, exact crossing rule, asymptotic defect fraction, and Fibonacci sum were algebraically reconstructed, and `artifacts/verify.py` provides exact-integer regression checks through \(n=1000\).

## Originality
PASS, with a bounded residual risk. Kaji covers the dual codimension, Fulton covers the degeneracy-locus class, and Ottaviani--Sodomaco--Ventura cover other Segre dual-degree asymptotics. Targeted statement, alias, implication, and database searches did not locate the fixed-total-dimension theorem, its \(1/\sqrt5\) mode, or its Fibonacci total. Because the synthesis is elementary, an unindexed prior occurrence remains possible.

## Value
PASS. The result links two standard projective-duality invariants—degree and defect—across a natural family at fixed intrinsic dimension. Its sharp mode says that the most degree-complex dual is asymptotically genuinely defective, and the exact Fibonacci total gives a family-wide invariant rather than a single numerical example.

## Closest literature and limitations
The closest inspected sources are Kaji for Segre dual defect, Fulton for determinantal degeneracy classes, and Ottaviani--Sodomaco--Ventura for family-level asymptotics of Segre dual degrees. The theorem is limited to standard two-factor Segre embeddings and does not address higher-factor tensors, ED degrees, or finer singularities of the dual.

Same-model review: passed. Independent audit: not yet performed.
