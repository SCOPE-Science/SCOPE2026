# Same-model review

## Correctness
PASS. The odd-part definition gives exact recurrences for the prefix sum \(S(N)\). Two inductions yield
\[
S(2^m-1)=2^{m-1}-1
\]
and
\[
S(L_m)=\left\lfloor\frac{L_m}{2}\right\rfloor-\left\lfloor\frac{m-1}{2}\right\rfloor
\]
for \(L_m=\lfloor2^m/3\rfloor\). Because \(L_m+L_{m+1}=2^m-1\), the factor from \(L_{m+1}+1\) through \(2^m-1\) has length \(L_m\) and exactly \(m-1\) more \(1\)s than the prefix of that length. Choosing \(m\ge c+2\) defeats every fixed prepended block \(1^c\). The finite verifier replays the identities but is not used as an infinite proof.

## Originality
PASS. The closest inspected full text, Cicalese--Lipták--Rossi, directly studies finite prepending and separately treats paperfolding prefix normal forms. It gives the positive Thue--Morse and negative Champernowne examples but does not state the paperfolding finite-prepending verdict. Madill--Rampersad give unbounded paperfolding abelian complexity but not the comparison with the actual paperfolding prefixes. Targeted published-finding corpus and web searches under equivalent formulations found no implication of the displayed witness family.

Residual risk remains from unindexed notes, theses, or discrepancy formulas phrased outside prefix-normal terminology.

## Value
PASS. The claim resolves a natural qualitative property of a classical automatic word explicitly treated by the anchor literature. It also gives a structural logarithmic obstruction at the natural lengths \(L_m=\lfloor2^m/3\rfloor\), rather than only a finite failed test.

Same-model review: passed. Independent audit: not yet performed.
