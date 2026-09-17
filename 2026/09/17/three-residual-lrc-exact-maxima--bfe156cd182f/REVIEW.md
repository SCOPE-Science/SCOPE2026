# Review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

**PASS.** The two locality-one upper bounds follow from a self-contained
partition argument that applies to nonlinear codes. For all-symbol
\((1,\delta)\)-locality, every recovery view has exactly \(\delta\) coordinates,
and all coordinates in a recovery view induce the same equality partition on
the codewords. The resulting coordinate equivalence classes each have size at
least \(\delta\), and representative coordinates give an injective description
whose weighted Hamming distance is exact.

For \((q,n,d,r,\delta)=(2,15,5,1,3)\), either there are at most four classes,
giving at most \(16\) codewords, or there are five classes of size three; the
representative binary code then has length five and distance at least two, so a
fixed perfect matching of the five-cube gives the same upper bound \(16\).
The repeated even-parity construction attains it.

For \((3,7,3,1,3)\), there are at most two classes and hence at most nine
codewords; the displayed two-class ternary code attains nine.

For \((2,14,4,2,2)\), the exact rational three-block LP value reported by Kang
and Xiong is below \(2^8\), so a binary linear code has dimension at most seven.
The displayed generator has rank seven, minimum distance four, and five local
triples whose punctures have minimum distance two. The deterministic verifier
enumerates all codewords and checks these properties.

## Originality

**PASS, to the best of our knowledge.** Kang and Xiong's September 2026 v1
explicitly leaves exactly these three parameter rows outside its exact
linear-dimension conclusion. Searches were performed for the exact parameter
tuples, synonymous locally recoverable/local repairable terminology, the
reported rational LP values, and stronger constructions or bounds.

Important prior coverage was found and is incorporated rather than claimed as
new. Yang et al. record existence of a binary \([14,7,4;2]\) LRC. Xia and Chen
give a 2019 characterization of optimal linear locality-one
\((r,\delta)\)-LRCs, so the binary \([15,4,6]\) linear construction is also not
claimed as a new construction. The locality-one partition lemma used here is
elementary and is not presented as a novelty claim by itself.

No inspected source stated the combined exact conclusions
\(A_2(15,5;1,3)=16\), \(A_3(7,3;1,3)=9\), and
\(K_2(14,4;2,2)=7\) as a closure of the three residual rows of the new
three-block bounds. The originality claim is therefore the exact synthesis and
closure, with nonlinear exactness in the two locality-one rows.

The Kang-Xiong paper is a preliminary v1, so a later revision or a
contemporaneous note could independently add the same observations. This is
the principal residual originality risk.

## Value

**PASS.** The result removes all three exceptions in the exact
linear-dimension statement attached to the new three-block LP table. Two of
the three rows are strengthened further to exact maximum sizes for arbitrary,
possibly nonlinear codes. The result also distinguishes clearly between prior
construction ingredients and the new exact consequences of the recent upper
bounds.

## Source inspection and limitations

The full Kang-Xiong preprint, including its certified-bounds table and
Corollary V.2, was inspected. The Yang et al. preprint table recording
\([14,7,4;2]\) existence was inspected, along with the published bibliographic
record. The Xia-Chen article text giving the locality-one characterization was
inspected.

No claim is made that every item in the coding-theory literature has been
exhausted. The binary nonlinear maximum for \((14,4,2,2)\) remains open within
the evidence considered here: the explicit size-\(128\) construction and the
three-block upper bound \(158\) do not coincide.
