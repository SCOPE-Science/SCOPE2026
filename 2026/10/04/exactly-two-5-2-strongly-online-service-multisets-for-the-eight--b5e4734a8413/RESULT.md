# Exactly two \((5,2)\)-strongly-online service multisets for the eight-column example
## Finding
For the binary generator matrix
\[
G=\begin{pmatrix}
1&0&1&0&1&0&1&1\\
0&1&1&0&0&1&1&1\\
0&0&0&1&1&1&1&1
\end{pmatrix},
\]
there are exactly two labeled multisets of minimal services that make \(G\) \((5,2)\)-strongly online in the sense of Definition IV.19 of Düzgün--Hollmann--Riet--Skachek--Taranchuk.

Writing a repeated recovery set twice, the first structure is
\[
\begin{aligned}
\mathcal S_1&=\{\!\{\{1\},\{1\},\{2,3\},\{6,7\},\{6,8\}\}\!\},\\
\mathcal S_2&=\{\!\{\{2\},\{2\},\{4,6\},\{5,7\},\{5,8\}\}\!\},\\
\mathcal S_3&=\{\!\{\{4\},\{4\},\{1,5\},\{3,7\},\{3,8\}\}\!\}.
\end{aligned}
\]
This is the structure displayed in Example IV.22. The only other labeled structure is
\[
\begin{aligned}
\mathcal T_1&=\{\!\{\{1\},\{1\},\{4,5\},\{6,7\},\{6,8\}\}\!\},\\
\mathcal T_2&=\{\!\{\{2\},\{2\},\{1,3\},\{5,7\},\{5,8\}\}\!\},\\
\mathcal T_3&=\{\!\{\{4\},\{4\},\{2,6\},\{3,7\},\{3,8\}\}\!\}.
\end{aligned}
\]
In particular, every \((5,2)\)-structure on this labeled matrix has exactly five service occurrences for each request; no request can carry six or more occurrences while the full cross-request exclusion condition remains valid.

## Assumptions and scope
A recovery set is minimal exactly as in the source paper: it spans the requested unit vector over \(\mathbb F_2\) and no proper subset does. A service is a request together with such a recovery set. Multiplicity is allowed. The claim concerns the fixed labeled matrix \(G\), the exact parameters \(m=5\) and \(L=2\), and all minimal recovery sets, not only the four recovery sets initially used by the paper to show \(3\)-strong online recovery. No claim is made about larger \(L\), about the optimal ratio \(m/L\), or about classification modulo code automorphisms.

## Proof
For each request, direct finite linear-algebra enumeration gives exactly eleven minimal recovery sets. For request \(1\) these are
\[
\{1\},\{2,3\},\{4,5\},\{6,7\},\{6,8\},
\{2,4,7\},\{2,4,8\},\{2,5,6\},\{3,4,6\},\{3,5,7\},\{3,5,8\},
\]
and the other two lists are obtained by the same computation from \(G\).

In a \((5,2)\)-service multiset, the multiplicity of any fixed service is at most \(2\): a recovery set intersects every copy of itself, so three copies would already make that selected service exclude three services for its own request, violating \(L=2\). Therefore each request is described by one of the \(3^{11}\) multiplicity vectors with entries in \(\{0,1,2\}\).

The packaged verifier derives the eleven recovery sets from \(G\), rather than trusting a stored list. It exhausts all \(3^{11}\) vectors for each request, keeps those with at least five occurrences and with same-request exclusion count at most two for every selected service, and obtains exactly \(141\) candidates per request. It then checks every pair of request-candidates against the cross-request exclusion rule. Exactly \(306\) compatible pairs remain for each of the three request pairs. Intersecting these three pairwise compatibility relations leaves exactly two global triples. Their decoded multisets are exactly \(\mathcal S\) and \(\mathcal T\) above. Both have request totals \((5,5,5)\), so the same exhaustive check also rules out any global \((5,2)\)-structure having more than five occurrences for even one request.

This is exhaustive because Definition IV.19 depends only on multiplicities of minimal recovery sets and pairwise intersections of their coordinate sets; those are exactly the objects enumerated.

## Verification
Run `python verify_classification.py`. It reconstructs the minimal recovery sets from the generator matrix, verifies the per-request candidate counts \(141\), verifies the three pair-compatibility counts \(306\), finds exactly two global structures, prints both, and terminates with `VERIFY_OK`. The computation uses only Python's standard library and exact integer/set operations.

## Relationship to prior work
The source paper introduces \((m,L)\)-strongly-online batch codes and Example IV.22 as the first explicit demonstration that allowing service multisets can succeed where service sets fail. It proves that no service *set* on this matrix has \(m\ge 2L+1\), and then displays one multiset \((5,2)\)-structure, namely \(\mathcal S\). The paper does not state a classification of all \((5,2)\)-service multisets for the example and does not display \(\mathcal T\). Focused searches for the example number, generator matrix, \((5,2)\) terminology, and the alternate recovery-set pattern did not locate a prior classification.

## Limitations
The statement is a finite labeled classification for one canonical example. It does not show that the two structures are inequivalent under every natural notion of code equivalence, and it does not solve the paper's open question asking whether every \(t\)-strongly-online code admits an \((m,L)\)-structure with \(\lceil m/L\rceil\ge t\). Literature search cannot by itself prove novelty; an unindexed or unavailable version of the conference submission remains a residual risk.

## References
Düzgün, B.; Hollmann, H. D. L.; Riet, A.-E.; Skachek, V.; Taranchuk, V. *Recovery Models for Linear Batch Codes*. arXiv:2605.09748v2, 2026. The first public version, arXiv:2605.09748v1, was submitted on 10 May 2026. In particular, see Definition IV.19, Theorem IV.20, Example IV.22, and the open question immediately following that example.
