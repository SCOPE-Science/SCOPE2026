# Independent mathematical audit

## correctness

PASS

For dyadic windows of size 2^(h+1), either starting parity gives exactly 2^(h-1) ones from the even-indexed alternating sequence, and the remaining symbols are the length-2^h window at the halved start. The displayed transition for the centered weight, first/last bits and starting parity is therefore an equality and stabilizes at the full 24 states. The blocks (0,e,1,b) have a triple histogram determined by parity and their fourth symbol. Indexing starts 0 through 3 in each block verifies the two omitted triples at offsets 0,1,2; at offset 3 the extra offset-zero triple cancels the removed one since the first block and the block one full window later have equal parity. The correct terminal pair determines shorter counts by appending its two-gram and then its final bit. Thus the full signatures depend only on the state, block parity and offset, each combination actually witnessed. For fixed state set increasing k changes every signature by the same baseline vector (and changes its weight by precisely the new minus old half-length), proving stability of both equivalence partitions and centered weights. My separate direct enumeration used a provably complete prefix of length 7n: for starts fixed modulo 2n all bits of the n-window are fixed except the single one-based position divisible by n. At starts below 2n that position has quotient 1 or 2, and shifting by 2n or 4n respectively changes it to 3 or 6, giving the other possible bit. This gives full direct censuses for k=4,…,9 and independently checks the smaller state sets. Results: n=16 has 32 full classes, with two fibers of size one and ten of size three; n>=32 has 36 with twelve fibers of size three and twelve per centered weight -1,0,1. Replay: python3 /workspace/branches/independent_paperfolding.py. The affine argument and exact transition, not the bounded list of k, justify all higher dyadic levels.

## originality

PASS

In the inspected literature and catalogue comparisons there are exact ordinary Abelian counts on the same paperfolding word, binomial counts using scattered subwords, and higher-Abelian counts on a different word. None of these statements yields the dyadic contiguous triple-count partition or its precise refinement of the 2-Abelian fibers. This is a bounded comparison, not a uniqueness claim.

## value

PASS

This is a natural higher-order invariant of a canonical automatic word. The result describes how a whole dyadic family changes under the refinement, with an exact exceptional length and uniform fibers rather than just the headline complexity. A small stabilized state set explains why the result extends across dyadic scales. No general-length or generalized-paperfolding claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
