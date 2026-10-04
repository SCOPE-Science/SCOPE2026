# Same-model review

## Correctness
PASS. The claim is reconstructed from the standard IPP1/IPP2 criterion. The packaged verifier checks the ambient MDS property, derives every forbidden three- and four-word configuration, enumerates all \(65536\) subcodes without pruning by unproved assumptions, and verifies the two affine-line profile counts. The claim is finite; no experiment is extrapolated to an infinite statement.

## Originality
PASS. The closest primary source, IACR ePrint 2007/276, proves the prolific length-four boundary and supplies the IPP criterion, but it does not optimize IPP subcodes of the quaternary MDS code. Exact-parameter searches under IPP, MDS, orthogonal-array and Latin-square formulations did not find the threshold \(8\), the count \(48\), or the \(24+24\) affine-profile split. An unindexed finite computation remains a residual risk.

## Value
PASS. The quaternary \([4,2,3]\) MDS code is the first alphabet-size boundary immediately beyond the sporadic ternary prolific example emphasized in the primary source. Determining that only half of its words can survive under IPP, together with a complete extremal census and two geometric profiles, gives a natural quantitative measure of that obstruction rather than an arbitrary parameter slice.

## Closest literature and limitations
Blackburn, Etzion and Ng classify prolific nonbinary length-four IPP codes and exclude the quaternary full-code case. The present result is narrower in ambient object but sharper in deletion distance. It does not determine unrestricted quaternary length-four IPP maxima, and it does not claim a full automorphism-orbit classification of the forty-eight extremizers.

Same-model review: passed. Independent audit: not yet performed.
