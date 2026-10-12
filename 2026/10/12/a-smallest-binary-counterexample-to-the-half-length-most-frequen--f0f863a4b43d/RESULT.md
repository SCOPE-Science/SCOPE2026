# A smallest binary counterexample to the half-length most-frequent-subsequence conjecture

## Finding

Let \(\operatorname{occ}(w,u)\) be the number of increasing choices of positions in the finite word \(w\) whose selected letters spell \(u\). Set \(H(w)=\max_u\operatorname{occ}(w,u)\) and \(H_{\leq}(w)=\max_{|u|\leq\lceil |w|/2\rceil}\operatorname{occ}(w,u)\). Fang's revised Conjecture 5.7 asserts \(H(w)=H_{\leq}(w)\) for every word of length at least two. It fails even over the binary alphabet.

The word `01010001110101` has \(H(w)=144\), achieved **uniquely** by `01001101` of length \(8\), while \(H_{\leq}(w)=136\), attained by the length-six word `010101`. Here \(\lceil|w|/2\rceil=7\). The inequation \(144>136\) refutes the conjecture.

Moreover, \(14\) is the shortest length of any binary counterexample. Exactly four binary words of length \(14\) violate the conjecture:

- `01010001110101` and `10101110001010`, whose global maxima are \(144\);
- `01110101010001` and `10001010101110`, whose global maxima are \(147\).

Each has a unique most frequent subword of length \(8\). The four words form two orbits under reversal and bit complementation. For the second representative `01110101010001`, the unique maximizer is `01101001`, with \(147\) occurrences, while the maximum at lengths at most \(7\) is \(144\).

## Assumptions and scope

All words are finite words over \(\{0,1\}\); scattered subwords are obtained by choosing a strictly increasing subset of positions, not necessarily consecutive. The empty subword is included, with exactly one occurrence. Occurrences are counted with multiplicity of the selected position subsets. No equivalence classes are imposed in the exhaustive enumeration; symmetry is discussed only afterward.

## Proof

For any finite binary word \(w\), define \(F_w(u)=\operatorname{occ}(w,u)\) for every binary word \(u\) including the empty word. Appending a letter \(c\) to \(w\) gives the recurrence

\[
F_{wc}(u)=F_w(u)+\mathbf{1}_{u=vc}\,F_w(v),
\]

where the second term is zero unless \(u\) ends in \(c\), in which case \(v\) is \(u\) without its final letter. This is an exact partition of position-subset occurrences by whether they use the newly appended last position. Initialize \(F_\epsilon(\epsilon)=1\) and all other counts zero. Consequently the recurrence computes every \(F_w(u)\), and taking maxima over the dictionary is exhaustive, not an estimate.

The attached `verify.py` enumerates every one of the \(2^n\) binary words separately for each \(2\leq n\leq14\), computes all nonzero \(F_w(u)\), and compares \(H(w)\) with \(H_{\leq}(w)\). It establishes equality for every binary word of lengths \(2\) through \(13\) and exactly the four listed strict inequalities at length \(14\). For `01010001110101` the maxima by subword length from \(0\) to \(14\) are

\[
(1,7,31,67,111,123,136,130,144,72,36,18,9,3,1),
\]

and for `01110101010001` they are

\[
(1,7,30,64,114,129,144,144,147,86,63,27,11,3,1).
\]

The program checks that there is exactly one maximizer in each case. It additionally recomputes **every** subsequence multiplicity for both representatives by independently looping over all \(2^{14}\) position subsets, rather than using the append recurrence. Every count agrees.

Bit complementation bijects occurrence choices for \((w,u)\) with those for their complemented images, and reversal maps any increasing position set to another increasing set after reversing order; both preserve every relevant occurrence count and lengths. Thus the two remaining exceptional words inherit the exact profiles. This completes the binary minimum-length classification and the counterexample.

## Verification

Run `python3 verify.py` from the directory containing the embedded file after extraction. The verifier uses only the Python standard library. A successful run prints a line beginning `VERIFY_OK` and reports exhaustive lengths, four exceptions, both unique maximizers, and both independent position-mask tallies. The program uses exact integer arithmetic and raises an assertion on any mismatch. The stated length profiles are also checked by `verify.py`.

## Relationship to prior work

Wenjie Fang, *Maximal number of subword occurrences in a word*, arXiv:2406.02971, defines subword entropy and maximal scattered-subword occurrence multiplicity. The full 2024-06-05 version has a stronger, differently quantified Conjecture 5.7, but the full 2025-05-14 revision, Section 5, explicitly asks whether **some** most frequent subword always has length at most half the input length, rounded up. The latter nontrivial statement is the one refuted here. The original stronger statement is not relied upon to claim novelty. In contrast, the author's experiments tabulate words that *minimize* entropy, not every binary input word of a given length.

Menon and Singh, *Subsequence frequency in binary words*, study counts of words realizing a specified number of occurrences of a **fixed** pattern, including certain maxima over the ambient word. Those results do not give the argmax length over every possible pattern for a fixed ambient word, and therefore do not imply this binary classification.

## Limitations

The minimality and exactly-four count concern only binary words, and only lengths at most \(14\) were exhaustively examined. The four explicit words refute the unrestricted conjecture for general alphabets, but no classification for alphabets with more than two letters or longer binary words is asserted. No polynomial-time algorithm for unrestricted maximum-subsequence frequency is derived. No assertion of independent audit or unique historical priority is made.

## References

1. Wenjie Fang, *Maximal number of subword occurrences in a word*, arXiv:2406.02971v1 (2024-06-05), https://arxiv.org/html/2406.02971v1; version 3 (2025-05-14), Section 5, Conjecture 5.7, https://arxiv.org/html/2406.02971v3; *Journal of Experimental Mathematics* 1(2) (2025), 218–238, DOI:10.56994/JXM.001.002.002.
2. Krishna Menon and Anurag Singh, *Subsequence frequency in binary words*, *Discrete Mathematics* 347 (2024), 113928; https://arxiv.org/abs/2306.07870.
