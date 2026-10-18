# Mathematical review

## Correctness
**PASS.** A circular ordered-pair spectrum is exactly the adjacency-count matrix of a connected (on active vertices) balanced directed multigraph. The proof uniquely parameterizes all ternary balanced matrices by three loops, three antiparallel-pair counts and a signed triangle flux; connectivity is accounted for by three disjoint component partitions. The resulting rational function, pole orders, and constants are algebraically determined for every positive length. Two independently implemented finite enumerations corroborate the coefficients. The finite checks are not used as infinite proof.

## Originality
**PASS, with residual literature risk.** Bernardini et al. (2022, complete open-access primary paper inspected) give a set-substring reconstruction problem and Eulerian-walk algorithms, not a count of ternary circular directed-pair multiset spectra. Ota and Manada (2023, complete open-access primary paper inspected in its relevant sections) study binary circular reconstruction from supplied substring frequencies, not global ternary observation-space counts. Indexed binary linear ordered-pair observation counts and ternary unrelated code calculations do not imply the connected ternary circular formula. Search terms included directed ternary cyclic bigram spectra, Eulerian balanced matrices and connected flows; no exact same or stronger formula was identified. A differently indexed combinatorial enumeration remains possible; search absence alone is not a novelty proof.

## Mathematical value
**PASS.** This is the complete, all-length observation-space count for the first nonbinary circular directed two-read model, a natural information-theoretic reconstruction invariant. The exact connectivity exclusion and the sharp \(2160/n^3\) failure fraction identify when balanced candidate observations fail to represent any circular source; this is not a single-size census or a trivial restatement of Euler's criterion. The result gives the exact maximum zero-error code size for the specified noise-free observation model. It does not claim noisy-channel coding bounds or classifications for other alphabets/read lengths.

## Closest sources and limitations
G. Bernardini et al., *On Strings Having the Same Length-k Substrings* (CPM 2022; DOI 10.4230/LIPIcs.CPM.2022.16) and T. Ota–A. Manada, *A Reconstruction of Circular Binary String Using Substrings and Minimal Absent Words* (IEICE, 2023; DOI 10.1587/transfun.2023TAP0015). The classical Euler-circuit theorem and flow constraints are established tools. An equivalent generating function in an unindexed matrix-enumeration source is a residual originality risk. Finite checks confirm only specified small lengths.

Self-review: passed. Independent audit: not yet performed.
