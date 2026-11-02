# Scientific review of four-erasure logical-support spectrum

## Correctness
PASS. The claim identifies one explicit 20-qubit rank-nine commuting stabilizer, with exact erasure correctness defined via the local centralizer modulo local stabilizers. The nine published generators are copied verbatim into both reproducibility checkers. An exact 512-combination stabilizer enumeration confirms minimum stabilizer weight twelve. A complete rank census classifies all \(4845\) four-position subsets into local logical dimensions \((0,1,2)\) with multiplicities \((3840,970,35)\). An independently coded exhaustive local Pauli enumeration checks all \(4^4\) local operators for every four-set, confirming the histogram and that the 35 two-dimensional logical spaces are commuting. The general size-five failure follows from ten local degrees of freedom versus nine commutation equations and the minimum stabilizer weight; all larger erasures fail by monotonicity. The success polynomial follows from independent Bernoulli erasures. The source's 1075 weight-four logical total is reproduced by \(970+3\cdot35\).

## Originality
PASS under accessible publications and mathematical-record searches, with residual risk. Dzoba publishes the nine generators, minimum distance, stabilizer-weight distribution and aggregate 1075 weight-four logical count. That total alone does not determine the *number of distinct supports* nor their logical-dimension and commutation structure. No published support histogram \((3840,970,35)\) or exact four-erasure failure rate for this code was located. Classical stabilizer-erasure rank criteria are fully credited; neither their existence nor the known code parameters are treated as new. Unindexed alternative enumerations of this code could preempt the result.

## Value
PASS. Under known-location qubit erasure, the first nontrivial failure layer is four qubits; the number and type of failing four-sets determine the leading coefficient of actual exact erasure-recovery failure. Distinguishing the 35 erasure sets with two commuting logical degrees of freedom from 970 with one quantifies information loss beyond the known minimum distance and total count of minimum-weight logical operators. The complete exact recovery polynomial is a natural reliability invariant for a new code with optimal parameters, not an arbitrary subset calculation.

## Literature and limitations
Primary source: Dzoba, arXiv:2610.24025v1, available HTML and nine-generator ancillary. General background: Calderbank–Rains–Shor–Sloane 1998. The theorem concerns this *specific* stabilizer and exact known-location erasure recovery; it does not assert optimal recovery performance across all parameter-equivalent codes or independent publication-priority certification.

Self-review: passed. Independent audit: not yet performed.
