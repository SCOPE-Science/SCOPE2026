# Scientific review of the first-slack Lyndon rigidity theorem

## Correctness
PASS. Both possible second letters of a binary Lyndon word are treated separately, after establishing the first and last letters and the minimum arch length. The start-\(01\) case uses the exact number of zeros and a rotation that moves the unique double-one run to the last gap. The start-\(00\) case forces an initial length-three arch; a precisely specified rotation at the final \(10\)-to-\(01\) boundary excludes all other arch sequences. The two remaining words are separately checked for Lyndon status and universality. The exact unrestricted count and \(k=1\) boundary follow by unique greedy factorizations. Exhaustive and independently implemented finite checks through \(k=9\) support, but do not replace, the written infinite proof.

## Originality
PASS on the inspected evidence, with an unresolved possibility of unindexed earlier work. The closest references are Barker et al. (2020), which gives universal spectra and circular operations but not this constrained Lyndon class; Adamson (2023), which counts unrestricted universal words; Bannai et al. (2022), which finds Lyndon subsequences of a host; and Adamson et al. (2023), which counts universal members of regular languages. The theorem concerns words simultaneously Lyndon and linearly universal at the first length beyond the binary minimum, something not stated by those inspected results. A prior circular-necklace count cannot directly determine whether a Lyndon orbit representative retains linear universality. No independence or external novelty certification is claimed.

## Mathematical value
PASS. The first-slack layer of maximally rich binary subsequence supersequences is large (\((k+2)2^k\)), but its intersection with the canonical primitive rotation representatives has exactly two elements for *every* order. The proof identifies a structural rigidity principle and a sharp one-letter threshold, which is more informative than an isolated enumeration or a restatement of universal-word counting. This natural conjunction of full subsequence coverage and Lyndon canonicality can guide restricted supersequence constructions and boundary analysis; no broader application is asserted as proved.

## Scope and risks
Only binary ordered words and lengths \(2k\), \(2k+1\) are classified. General-length Lyndon enumeration is open here. The general arch criterion and unrestricted count are prior background. The scientific novelty judgment rests on inspected full texts plus searches and may be revised if an equivalent unindexed result is located.

Self-review: passed. Independent audit: not yet performed.
