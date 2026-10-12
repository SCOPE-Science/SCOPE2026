# Exact multiset two-insertion reconstruction for two-symbol words

## Finding
For every integer alphabet size \(q\ge2\), the largest possible intersection of the exact-two-insertion **multiset** spheres of two distinct length-two words is
\[
\max_{x\ne z}\lvert M_2(x)\cap M_2(z)\rvert=8q-5.
\]
Equivalently, in the usual notation of the multiset reconstruction model, \(N_q^{\mathrm m}(2,2)=8q-5\). Equality holds if and only if the unordered center pair is \(\{aa,ab\}\) or \(\{aa,ba\}\) for some distinct letters \(a,b\). There are exactly \(2q(q-1)\) such labeled unordered center pairs. Thus, when every channel uses a different insertion vector, the exact number of observations guaranteeing reconstruction of any two-letter source word from the **multiset of received words** is \(8q-4\).

## Assumptions and scope
Let \(\Sigma\) be an alphabet with \(|\Sigma|=q\ge2\); no field structure is assumed. A source word \(x=(x_1,x_2)\in\Sigma^2\) receives exactly two inserted letters, placed in the three gaps before, between, and after its original letters. Different gap-words of total length two are different insertion vectors, even when they produce identical four-letter outputs. In particular, the original characters are retained in order.

Write \(e_x(y)\), for \(y=(y_1,y_2,y_3,y_4)\in\Sigma^4\), for the number of insertion vectors producing \(y\) from \(x\). Deleting the inserted positions shows that
\[
e_x(y)=\sum_{1\le i<j\le4}{\mathbf{1}}\{(y_i,y_j)=(x_1,x_2)\}.
\]
The multiset sphere \(M_2(x)\) contains \(y\) with multiplicity \(e_x(y)\). Its multiset intersection has cardinality
\[
I_q(x,z)=\lvert M_2(x)\cap M_2(z)\rvert
 =\sum_{y\in\Sigma^4}\min\{e_x(y),e_z(y)\}.
\]
The theorem concerns this multiplicity-sensitive quantity, **not** the intersection of ordinary sets of insertion outputs or the non-multiset reconstruction model.

## Proof
First observe that \(I_q(x,z)\) depends only on the equality pattern of the four letters \((x_1,x_2,z_1,z_2)\): any bijection of the alphabet preserves all subsequence embeddings. Encode each equality pattern canonically by its restricted-growth tuple \(p=(p_1,p_2,p_3,p_4)\), starting with \(p_1=0\) and introducing each new symbol with the smallest unused index. There are 15 set partitions of four positions; excluding the two patterns for identical center words leaves exactly 13 possible patterns.

Fix a pattern \(p\), let \(s=1+\max_i p_i\), let \(S=\{0,\ldots,s-1\}\), and take centers \(x=(p_1,p_2)\), \(z=(p_3,p_4)\). The pattern is available only when \(q\ge s\). Define the following finite, explicit integers:
\[
C_p=\sum_{y\in S^4}\min\{e_x(y),e_z(y)\},\qquad
E_p=\sum_{\substack{y\in(S\cup\{s\})^4\\|\{i:y_i=s\}|=1}}\min\{e_x(y),e_z(y)\}.
\]
In \(E_p\), the symbol \(s\) denotes one **fixed** letter outside the center alphabet. If a four-letter output contains two or more letters outside \(S\), at most two positions remain for the two center symbols. Were it to embed *both* distinct centers, both embeddings would use those same two positions, forcing \(x=z\), a contradiction. Thus the only contributing outputs either use no outside symbols or use exactly one outside symbol. The value for a fixed outside symbol is \(E_p\), independently of that symbol. It follows **for every \(q\ge s\)**, with no extrapolation from small alphabets, that
\[
I_q(x,z)=C_p+(q-s)E_p.\tag{1}
\]

The entire finite coefficient calculation is given below. Each entry is obtained by substituting the two ordered letter pairs represented by \(p\) into the displayed embedding formula and summing over at most four-symbol outputs. The standalone `verify.py` reproduces every coefficient directly from those sums.

| Restricted-growth pattern \(p\) | \(s\) | \(C_p\) | \(E_p\) | \(I_q\) |
|:--|--:|--:|--:|:--|
| `0001`, `0010`, `0100`, `0111` | 2 | 11 | 8 | \(8q-5\) |
| `0110` | 2 | 10 | 8 | \(8q-6\) |
| `0011` | 2 | 6 | 0 | \(6\) |
| `0102`, `0121` | 3 | 18 | 8 | \(8q-6\) |
| `0112`, `0120` | 3 | 12 | 4 | \(4q\) |
| `0012`, `0122` | 3 | 6 | 0 | \(6\) |
| `0123` | 4 | 6 | 0 | \(6\) |

For \(q\ge2\), the expression \(8q-5\) strictly exceeds every other admissible entry in this table: \(8q-6\), \(4q\), and \(6\). Its four equality patterns correspond exactly to one constant word \(aa\) and one length-two word containing exactly one \(a\) and one different \(b\), in either order. Choosing \(a\), then \(b\), then one of the two orders yields \(2q(q-1)\) different unordered pairs; none is counted twice because the constant word is unique within each pair.

Finally, the standard adversarial reconstruction argument is exact: any two distinct centers can produce a common multiset of precisely \(I_q(x,z)\) output observations by choosing the minimum common multiplicity of each output. Conversely, no common output multiset of more than \(I_q(x,z)\) observations can be generated from both centers using distinct insertion vectors. Maximizing over centers establishes the sharp universal threshold \(1+8q-5=8q-4\), as claimed. \(\square\)

## Verification
Run `python3 verify.py` with Python 3's standard library. It enumerates the complete set of 13 canonical distinct-center patterns, independently computes all \(C_p\) and \(E_p\) coefficients by the finite definitions above, checks relation (1) on four alphabet sizes per pattern, and directly enumerates *all* unordered center pairs for each \(q=2,3,4,5,6\), confirming both the maximum and exact number and form of maximizers. Expected output begins `VERIFY_OK`.

The proof for arbitrary \(q\) is the support reduction (no two outside symbols) together with the exhaustive finite pattern classification. Spot checks for \(q\le6\) are not used to infer the general statement.

## Relationship to prior work
Junnila, Laihonen, Lehtilä, and Padavu Devaraj define the multiset insertion-reconstruction threshold by pairwise multiset-ball intersections in their extended 2026 manuscript, Section II-A, equations (3)–(4). Their Example 4 computes \(I_2(01,11)=11\), giving one instance of the present extremal pattern; it does **not** establish a global maximum or classify all alphabets. Their Theorems 27–28 give general bounds at larger insertion counts without an exact formula for this case. The underlying 2025 workshop publication has an earlier verified public date of 21 November 2025.

The 2026 ISIT proceedings article by the same authors describes a distinct max-Levenshtein model and another error-diversity model in its abstract, with an exact two-insertion statement for the latter. That work should not be conflated with the **multiplicity-sensitive multiset-sphere intersection** proved here; the full proceedings text was not available for complete comparison, and potential overlap remains a genuine limitation. Results for the non-multiset threshold or ordinary insertion-sphere intersections are neither asserted nor claimed as new here.

## Limitations
Only source length two and exactly two inserted symbols are covered, without channel noise other than insertions. The model requires distinct insertion vectors across observations and observes a multiset, not just a set. The classification is conditional on these definitions. Source comparison with all possible earlier publications has not been independently validated; an inaccessible closely related 2026 proceedings paper and unindexed enumerations leave originality uncertainty.

## References
- V. Junnila, T. Laihonen, T. Lehtilä, P. Padavu Devaraj, *On Levenshtein's Reconstruction Problem for Channels with Unique Insertion Error Patterns*, IEEE Information Theory Workshop (2025), DOI `10.1109/ITW62417.2025.11240278` (IEEE Xplore public listing: 21 November 2025).
- V. Junnila, T. Laihonen, T. Lehtilä, P. Padavu Devaraj, *Unique Insertion Error Patterns in Levenshtein's Reconstruction Problem*, arXiv:`2607.06181`, first posted 7 July 2026, particularly Section II, Example 4, Theorems 27–28, and Section VI.
- V. Junnila, T. Laihonen, T. Lehtilä, P. Padavu Devaraj, *Number of Channels with Different Insertion Errors Required for the Levenshtein's Reconstruction Problem*, IEEE ISIT (2026), DOI `10.1109/ISIT62367.2026.11653882` (abstract available; full text not inspected).
- V. Junnila, T. Laihonen, T. Lehtilä, *On Unique Error Patterns in the Levenshtein's Sequence Reconstruction Model*, arXiv:`2406.14125`, first posted 20 June 2024 (background on distinct-error-pattern models).
