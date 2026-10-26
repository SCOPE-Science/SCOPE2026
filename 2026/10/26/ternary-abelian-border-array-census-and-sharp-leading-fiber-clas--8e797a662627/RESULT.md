# Ternary Abelian-border-array census and sharp leading fiber classification

## Finding
Let \(\Sigma=\{0,1,2\}\). For a word \(w=w_1\cdots w_n\), let \(\pi_w(i)\) be the largest \(j\) with \(1\le j<i\) such that the first \(j\) and last \(j\) letters of \(w_1\cdots w_i\) have equal Parikh vectors, or zero if no such \(j\) exists. Two words have the same *observation* if their full vectors \(\pi_w=(\pi_w(1),\ldots,\pi_w(n))\) coincide. Write \(T_3(n)\) for the number of attainable observations.

**Theorem.** For each \(1\le n\le16\), the following exact table gives \(T_3(n)\):

| \(n\) | \(T_3(n)\) | \(n\) | \(T_3(n)\) |
|---:|---:|---:|---:|
|1|1|9|795|
|2|2|10|2170|
|3|4|11|5904|
|4|9|12|16702|
|5|20|13|47014|
|6|49|14|136189|
|7|119|15|391967|
|8|308|16|1151825|

Moreover, for **every \(n\ge4\)**, the largest observation fiber (counting actual labeled ternary words) has exactly \(6\cdot2^{n-2}\) words, and the *unique* observation attaining it is \((0,0,\ldots,0)\). The next-largest fiber size is exactly \(6\cdot2^{n-3}\); precisely two observations attain it:

\[\bigl(0,1,0,\ldots,0\bigr),\qquad\bigl(0,0,\ldots,0,n-1\bigr).\]

The finite table and the all-length fiber classification are parts of one result about the attainable signatures and their ambiguity under the same observation map. In a zero-error reconstruction model that returns only this signature, \(T_3(n)\) is also the largest possible cardinality of a uniquely decodable length-\(n\) code.

## Assumptions and scope
Positions and letters are labeled. An Abelian border compares **multisets** of letters, not literal strings. Every prefix length \(i\) is observed, and only *proper*, nonempty borders enter \(\pi_w(i)\). The exact \(T_3(n)\) table is established only for \(1\le n\le16\); no table value beyond length 16 and no all-length formula for \(T_3(n)\) is asserted. The leading-fiber statements are proved for all integers \(n\ge4\).

## Proof
**1. The complete finite census.** Relabeling the alphabet does not alter any Parikh-vector equality. Every relabeling class of nonempty ternary words therefore has exactly one restricted-growth representative \(r_1\cdots r_n\), defined by \(r_1=0\) and
\[0\le r_i\le\min\bigl(2,1+\max\{r_1,\ldots,r_{i-1}\}\bigr)\quad(2\le i\le n).\]
The algorithm `artifacts/abelian_census.cpp` recursively visits every such representative exactly once. For each \(0\le i\le n\), define \(P_s(i)\) as the count of symbol \(s\) among the first \(i\) positions, with \(P_s(0)=0\). Then the algorithm computes the uniquely specified value
\[\pi_r(i)=\max\Bigl(\{0\}\cup\{j:1\le j<i,\ \forall s\in\Sigma,\ P_s(j)=P_s(i)-P_s(i-j)\}\Bigr).\]
For \(n\le16\), all these values are integers between zero and 15, so packing them into disjoint four-bit fields is injective. Sorting the complete list of packed arrays and counting distinct values gives precisely the table. The number of canonical representatives visited at each length is \((3^n+3)/6\), independently giving a check on the completeness of this traversal.

The independent `artifacts/abelian_independent.cpp` enumerates **all** words beginning with zero, without restricted-growth normalization, and encodes the three prefix counts as distinct base-32 digits. Because each count is at most 16, subtraction of packed prefix counts has no cross-digit borrows, making its Parikh equality test exact. Any ternary word can be globally relabeled to begin with zero. Therefore this second traversal also covers every attainable array, with a different input set and different Parikh arithmetic. After deduplication it gives the same 16 integers. These are exhaustive finite certificates, not extrapolations.

**2. Normalized fiber sizes.** A canonical nonconstant ternary word has exactly six labeled relabelings, whether it uses two or three symbols. The unique constant canonical word has three. It suffices to classify canonical fibers. For a fixed array, the first canonical symbol is zero. The second is forced to be zero if \(\pi(2)=1\), and one if \(\pi(2)=0\). At any later position, equality \(\pi(i)=i-1\) is equivalent to the new symbol being zero, while \(\pi(i)\ne i-1\) restricts it to one or two. Thus every canonical fiber has at most \(2^{n-2}\) members.

The all-zero observation has exactly \(2^{n-2}\) canonical realizations: the words beginning with zero and then one, followed by an arbitrary sequence over \(\{1,2\}\). Indeed, a proper prefix of any positive length includes the first zero, whereas a suffix ending at any later prefix contains no zero. Every alternative realizing an all-zero array also avoids zero after its first position, because a new final zero would force the Abelian border of length \(i-1\). Hence this fiber has exactly \(6\cdot2^{n-2}\) labeled words.

**3. Uniqueness and the second-largest fibers.** Suppose first that \(\pi(2)=1\), forcing the canonical prefix \(00\). For \(\pi(3)=0\), its third symbol is forced to be one; for \(\pi(3)=2\), the third symbol is forced to be zero. In the latter case, the possible fourth symbols give distinct fourth border values, so for \(n\ge4\) this case has fewer than \(2^{n-3}\) canonical realizations. In the former case, words starting \(001\) and thereafter using only \(\{1,2\}\) have zero border at every prefix of length at least three: a proper suffix either contains no zero or contains only one of the initial two zeros. Hence the observation \((0,1,0,\ldots,0)\) has exactly \(2^{n-3}\) canonical realizations. Any further occurrence of zero would force a subsequent large border and lose a two-way continuation, so every other array with \(\pi(2)=1\) has strictly fewer.

Now let \(\pi(2)=0\), forcing canonical prefix \(01\). If every later entry is zero, this is the unique largest fiber already described. Otherwise let \(t\ge3\) be the first index with \(\pi(t)\ne0\). All positions from two through \(t-1\) avoid zero, and at position \(t\) the new symbol must be zero, giving \(\pi(t)=t-1\). Thus at most \(2^{t-3}\) canonical prefixes reach length \(t\), with at most \(2^{n-t}\) further continuations: a bound of \(2^{n-3}\). When \(t=n\), every one of the \(2^{n-3}\) prefixes with zero only in the first position admits the final zero, so \((0,\ldots,0,n-1)\) attains equality.

If \(t<n\), examine the particular canonical prefix \(0\,1^{t-2}\,0\), which realizes the chosen array through index \(t\). Appending one creates a length-two Abelian border \(01\), whereas appending two produces no nonempty Abelian border, since the prefix has no two. Appending zero produces the length-\(t\) border. These three continuations therefore give different next array entries, rather than the two continuations required for equality in the bound. Hence the bound is strict for \(t<n\). This also excludes every other second-largest fiber. Finally, six labeled relabelings per nonconstant representative convert both canonical sizes into the stated word counts. For \(n\ge4\), the constant observation fiber of size three cannot interfere with the two leading sizes.

## Verification
`artifacts/verify.py` compiles both independent C++17 programs with a standard `g++` compiler, recomputes all 16 values, checks the canonical partition count, all finite fiber-size histograms, the singleton counts, and the leading and runner-up class counts at lengths four through sixteen. Its expected values are kept in `artifacts/expected_counts.tsv`; the exact finite table is justified by complete enumeration, not by the expected file. The independent method enumerates \(3^{n-1}\) words at each length and uses a different representation of Parikh sums.

## Relationship to prior work
Habib, Shamil and Rahman (2021, arXiv:2111.00259), Proposition 3.1, proved the binary count \(2^{n-1}\). Their Section 4 explicitly treats the ternary case as more difficult and establishes only the upper bound \(T_3(n)\le(3^{n-1}+1)/2\). The new table evaluates that question through length sixteen rather than restating this upper bound. Their statement about equivalence under alphabet relabeling motivates the restricted-growth reduction; that reduction is not claimed as novel. The sharp all-length leading and runner-up **fiber classifications** are additional results on the same observation equivalence. Work on binary Abelian borders and Dyck paths concerns individual word borders, not these ternary full-array fiber distributions.

## Limitations
No formula for the total number of attainable ternary arrays at arbitrary length is proved. The sharp fiber classification does not classify every fiber. Both enumeration procedures are finite exact computations; the structural extremal argument is the all-length proof. Independently audited validation has not been performed. Equivalent statements may exist under Parikh-prefix or jumbled-border terminology.

## References
Habib, M., Shamil, M. S. and Rahman, M. S. (2021), *Counting and Verifying Abelian Border Arrays of Binary Words*, arXiv:2111.00259v1, October 30, 2021, https://arxiv.org/html/2111.00259v1.

Christodoulakis, M., Christou, M., Crochemore, M. and Iliopoulos, C. S. (2014), *Abelian borders in binary words*, *Discrete Applied Mathematics*; abstract and bibliographic record: https://kclpure.kcl.ac.uk/portal/en/publications/abelian-borders-in-binary-words/.
