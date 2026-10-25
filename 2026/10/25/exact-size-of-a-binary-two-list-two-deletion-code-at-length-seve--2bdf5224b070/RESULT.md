# Exact size of a binary two-list, two-deletion code at length seven

## Finding

Let \(\mathcal C\subseteq\{0,1\}^7\). Call \(\mathcal C\) two-list-decodable after two deletions if every binary word \(y\in\{0,1\}^5\) is a subsequence of at most two members of \(\mathcal C\). The exact maximum is

\[
\max |\mathcal C|=11.
\]

## Assumptions and scope

A deletion removes one symbol while preserving the order of the remaining symbols. A received word is considered for every possible choice of two deleted positions, so the condition is equivalent to requiring at most two codewords to contain each length-five word as a subsequence. Repeated embeddings of the same received word in one codeword count only once. The claim concerns binary length-seven codewords and exactly two deletions; it makes no asymptotic or larger-blocklength assertion.

## Proof

For the lower bound, the following eleven words form a code:

\[
\begin{aligned}
\mathcal C_0=\{&0000000,0000111,0001000,0011101,0100011,\\
&0110101,1001100,1100010,1111000,1111110,1111111\}.
\end{aligned}
\]

For the thirty-two received words in lexicographic order, the numbers of members of \(\mathcal C_0\) containing them as subsequences are

\[
\begin{array}{c|rrrrrrrr}
y&00000&00001&00010&00011&00100&00101&00110&00111\\
\#&2&2&2&2&2&2&2&2\\[2pt]
y&01000&01001&01010&01011&01100&01101&01110&01111\\
\#&2&2&1&2&2&2&2&2\\[2pt]
y&10000&10001&10010&10011&10100&10101&10110&10111\\
\#&2&2&2&2&1&1&1&0\\[2pt]
y&11000&11001&11010&11011&11100&11101&11110&11111\\
\#&2&2&2&1&2&2&2&2
\end{array}
\]
Every load is at most two, so \(|\mathcal C_0|=11\) is a valid lower bound.

For the upper bound, assign a nonnegative integer weight \(w_y\) to each \(y\in\{0,1\}^5\) as follows. Entries are numerators; the actual weight is \(\lambda_y=w_y/59\).

\[
\begin{array}{c|rrrrrrrr}
y&00000&00001&00010&00011&00100&00101&00110&00111\\
w_y&52&7&0&26&7&5&4&26\\[2pt]
y&01000&01001&01010&01011&01100&01101&01110&01111\\
w_y&0&1&2&5&4&1&16&7\\[2pt]
y&10000&10001&10010&10011&10100&10101&10110&10111\\
w_y&7&16&1&4&5&2&1&0\\[2pt]
y&11000&11001&11010&11011&11100&11101&11110&11111\\
w_y&26&4&5&7&26&0&7&52
\end{array}
\]
Their sum is \(\sum_y w_y=326\). For every \(x\in\{0,1\}^7\), put

\[
S(x)=\sum_{y\preceq x}w_y,
\]

where \(y\preceq x\) means that \(y\) is a subsequence of \(x\), counted once per distinct \(y\). Direct exhaustive integer checking of all \(128\) words gives \(S(0000000)=S(1111111)=52\), and \(S(x)\ge59\) for every other \(x\). Equivalently, for all length-seven words,

\[
S(x)+7\,\mathbf 1_{\{0000000,1111111\}}(x)\ge59.
\]

If \(\mathcal C\) is any valid code, sum this inequality over \(x\in\mathcal C\). Each length-five word is contained in at most two codewords, and only two words have the extra indicator, hence

\[
59|\mathcal C|\le 2\sum_y w_y+14=666.
\]
Thus \(|\mathcal C|\le666/59<12\). Since cardinality is an integer, \(|\mathcal C|\le11\), matching the explicit construction.

The accompanying standard-library verifier recomputes all thirty-two codeword loads and all one hundred twenty-eight dual inequalities using integer arithmetic. This is an exhaustive finite certificate, not an inference from sampled cases or solver output.

## Verification

The witness has eleven distinct length-seven words. The verifier checks all \(32\times11\) subsequence incidences for the lower bound, all \(128\) length-seven words for the dual inequality, the weight sum \(326\), and the strict rational inequality \(666/59<12\). All checks use exact integer arithmetic and Python's standard library only.

## Relationship to prior work

Lin's 2026 preprint defines binary \(t\)-list-decodable \(k\)-deletion codes by bounding the number of codewords containing each length-\((n-k)\) subsequence, and proves asymptotic lower bounds for all admissible \(k,t\). It does not state this exact length-seven optimum. A separate recent published-finding corpus record gives the adjacent length-six case, with optimum seven; that record is used as a neighboring finite-parameter comparison, not as evidence for the length-seven upper bound. The length-seven claim is proved here by its own explicit witness and rational dual certificate.

## Limitations

This result determines only the single finite parameter \((n,k,t)=(7,2,2)\). It does not classify all optimal codes, count optimal codes up to symmetries, or imply a formula for any other length, deletion count, list size, or alphabet. A residual risk remains that an unindexed source has independently recorded the same finite optimum.

## References

1. Andrew D. Lin, “Lower Bounds for all List-Decodable Deletion Codes,” arXiv:2609.26650, first submitted 22 September 2026. Full text: https://arxiv.org/abs/2609.26650.
2. published-finding corpus record, “Exact length-six binary two-list two-deletion code size,” dated 4 October 2026: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-length-six-binary-two-list-two-deletion-code-size--9d20b24dd814. The repository's full record was not accessible during this run; its indexed title and summary are used only to locate the adjacent parameter.
