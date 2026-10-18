# The unique shortest overlap-free binary products of nine squares

## Finding

A **square** is a nonempty word of the form \(xx\). An **overlap** is a word of the form \(axaxa\), where \(a\) is one symbol and \(x\) may be empty. A word is overlap-free when none of its contiguous factors is an overlap.

Among all overlap-free binary words that can be written as a concatenation of **exactly nine nonempty squares**, the minimum length is

\[
\boxed{48}.
\]

Exactly two words attain this minimum:

`001001101001011010011001011001101001011010011011`

and its bitwise complement, equivalently its reversal,

`110110010110100101100110100110010110100101100100`.

Each has **exactly one factorization into nine nonempty squares**. For the first word the sequence of square roots is

`001`, `10`, `01`, `10`, `011001`, `10`, `01`, `10`, `011`.

Thus the nine root lengths are \((3,2,2,2,6,2,2,2,3)\), and the square-block lengths sum to \(48\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). Factors are contiguous, overlaps include the length-three factors \(000\) and \(111\), every square root is nonempty, and a factorization records an ordered list of nine square blocks. The classification concerns word lengths at most \(48\) to establish the global shortest length; it does not assert that longer nine-square products are unique or impossible.

## Proof

**Overlap test.** A word has an overlap if and only if there are an integer \(p\ge1\) and a contiguous factor of length \(2p+1\) with period \(p\). Indeed, such a factor begins and ends with the same symbol and has the form \(axaxa\), with \(|x|=p-1\). If a word \(v\) is overlap-free, then appending one letter creates an overlap if and only if some overlap ends at the newly appended letter. Consequently the following exhaustive recursion lists every overlap-free binary word of length at most \(48\): begin with the empty word and append each of `0` and `1`, rejecting precisely those extensions having a periodic suffix of length \(2p+1\) and period \(p\), for some \(1\le p\le\lfloor(|v|-1)/2\rfloor\).

**Square-product recurrence.** Define \(D_j(v)\) as the number of ordered factorizations of \(v\) into exactly \(j\) nonempty squares; set \(D_0(\epsilon)=1\) and \(D_0(v)=0\) otherwise. For every \(j\ge1\) and nonempty \(v\),

\[
D_j(v)=\sum_{r=1}^{\lfloor |v|/2\rfloor}
\mathbf{1}\bigl\{v[|v|-2r:|v|-r]=v[|v|-r:|v|]\bigr\}
D_{j-1}\bigl(v[0:|v|-2r]\bigr).
\]

The displayed slices use zero-based, half-open indexing. This equality is exact because every such factorization has a uniquely determined final square with root length \(r\), and deleting it leaves exactly \(j-1\) square blocks. Every prefix of an overlap-free word is overlap-free, so all terms are available in the enumerated prefix set.

The complete exact-integer evaluation of this recurrence on **all 7,867 overlap-free binary words of lengths \(0\) through \(48\)** gives no word with \(D_9(v)>0\) below length \(48\). At length \(48\), it gives \(D_9(v)=1\) for precisely the two displayed words, and \(D_9(v)=0\) for the other \(414\) overlap-free words of that length. This establishes the asserted global minimum and the unique factorization of each minimizer. The source code `exhaustive_prefix_dp.py` gives the complete recurrence and exact test; `prefix_dp_output.txt` records the per-length counts and the two witnesses.

**Independent finite exhaustiveness route.** In any product of nine nonempty squares with total length at most \(48\), eight of the squares consume at least \(16\) letters. Hence each square has length at most \(32\), so its root length is at most \(16\). Enumerating all binary roots of length at most \(16\) whose doubles are overlap-free gives exactly \(74\) possible square blocks, with block-length multiplicities \(2,2,6,4,12,8,24,16\) at lengths \(2,4,6,8,12,16,24,32\). A second algorithm independently checks every possible concatenation of these blocks, rejecting overlapped prefixes and pruning only when the remaining blocks cannot fit below length \(49\). Its depth-by-depth numbers of distinct surviving prefixes for depths \(1\) through \(9\) are

\[
74,\ 52,\ 56,\ 54,\ 32,\ 24,\ 26,\ 16,\ 2.
\]

The two depth-nine words both have length \(48\), each occurring with factorization multiplicity one. This independently establishes the same exhaustive conclusion. The executable source and output are `square_block_bfs.py` and `block_bfs_output.txt`.

## Verification

Execute `python3 exhaustive_prefix_dp.py` and `python3 square_block_bfs.py` with Python 3.9 or later. Both use only the Python standard library. The first independently derives the count of \(416\) overlap-free binary words at length \(48\), agreeing with OEIS A007777, and tests every possible square suffix of each word. The second enumerates square blocks first, uses a global all-start-position overlap test, and explores products rather than individual-letter extensions. Both produce the same two words, the same length bound, and factorization multiplicity one. The recorded outputs terminate with `PASS`.

## Relationship to prior work

Shallit's *Ten Squares Force an Overlap* (arXiv:2605.28570, first submitted 27 May 2026) proves that ten nonempty binary squares cannot be concatenated without an overlap and supplies the first displayed length-\(48\) nine-square word as a sharpness witness. The cited theorem and witness give the upper bound \(48\) for the present shortest-length problem, **but they do not exclude shorter nine-square words or classify length-\(48\) witnesses or their factorizations**. This work supplies those additional assertions.

Mol, Rampersad, and Shallit (arXiv:2006.10152) classify different *extension-extremal* overlap-free words: there extremality concerns insertion of a symbol, not maximization of the number of square blocks. OEIS A007777 enumerates all overlap-free binary words by length, and OEIS A368707 enumerates overlap-free words that are single squares; neither database determines the nine-square factorization multiplicities here.

## Limitations

This is a rigorous but finite, computer-assisted classification. The proof of the global shortest length is exhaustive because all shorter candidates are covered; it is not an infinite theorem about every nine-square product. The underlying general ten-square impossibility theorem is due to the cited work, not re-proved here. Unindexed earlier computations or unpublished sharpness classifications remain possible. No independent external scientific audit has been performed.

## References

1. Jeffrey Shallit, *Ten Squares Force an Overlap*, arXiv:2605.28570v1 (27 May 2026), https://arxiv.org/abs/2605.28570.
2. Lucas Mol, Narad Rampersad, and Jeffrey Shallit, *Extremal overlap-free and extremal β-free binary words*, arXiv:2006.10152 (2020), https://arxiv.org/abs/2006.10152.
3. OEIS A007777, *Number of overlap-free binary words of length n*, https://oeis.org/A007777.
4. OEIS A368707, *Number of length-n overlap-free binary words that are squares*, https://oeis.org/A368707.
5. Mathematical Reviews, MSC2020 `68R15`, *Combinatorics on words*, https://mathscinet.ams.org/msc/msc2020.html?btn=Current&t=68R15.
