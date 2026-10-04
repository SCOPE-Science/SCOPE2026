# Review of Exact linear chaining depth in the free-group boundary counterexample

## Correctness
PASS. The lower bound is precisely the obstruction proved for the sets \(L\) and \(B_n=[a^{2n+2}]\) in Proposition 6.13. The matching upper bound is explicit. A positive legal cylinder beginning with \(ab\) lies in \(L\cap a^2L\), because applying \(a^{-2}\) changes its initial pair to \(a^{-1}b\), which is also allowed by the source transition matrix. Measure-class preservation transfers this positive intersection to every consecutive pair \(a^{2j}L,a^{2j+2}L\). A positive legal cylinder beginning with \(b\), translated by \(a^{2n+2}\), gives the final positive intersection with \(B_n\). This constructs an \(n+1\)-chain and matches the lower bound. The boundary case \(n=0\) is covered separately by \(P(a,a)=0\).

## Originality
PASS. The source manuscript was inspected at the chain definition, Markov-measure construction, nonsingularization, and the complete proof of Proposition 6.13. It states the lower bound “not \(n\)-chain” but does not state a matching upper chain or the exact minimum. Searches for the source identifier together with “exact chain length,” “minimal chain,” the cylinder \([a^{2n+2}]\), and predecessor terminology did not reveal an equivalent statement. The nearest predecessor literature concerns weak double ergodicity and isometric-coefficient ergodicity, which do not imply the quantitative cylinder-by-cylinder minimum here.

## Value
PASS. Proposition 6.13 is the paper's separating example for chaining versus bounded chaining, and its witness family already encodes the growing obstruction. Determining the exact minimum \(n+1\), rather than only an unbounded lower bound, gives a natural quantitative invariant of that example and shows that each additional pair of initial \(a\)-letters costs exactly one chain link. This is a complete sharp statement for the canonical witness family and can serve as a baseline for quantitative variants of bounded chaining.

## Closest literature and limitations
The closest source is Tserunyan–Zomback, arXiv:2609.18061v2, Proposition 6.13, which supplies the lower bound. Loh–Silva, arXiv:1512.09340v4, and Haddock–Leng–Silva, arXiv:2011.14278v1, provide predecessor notions around weak double ergodicity but not this chain-depth profile. The conclusion is limited to the source's specific transition matrix and witness cylinders; priority risk remains if an equivalent upper-bound observation exists outside the inspected literature or only implicitly in unpublished discussion.

Same-model review: passed. Independent audit: not yet performed.
