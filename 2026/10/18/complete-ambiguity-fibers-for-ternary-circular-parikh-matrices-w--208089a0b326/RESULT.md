# Complete ambiguity fibers for ternary circular Parikh matrices with one middle letter and two first letters

## Finding

Fix the ordered ternary alphabet \(a<b<c\). For every integer \(h\geq0\), consider circular words with exactly two occurrences of \(a\), one occurrence of \(b\), and \(h\) occurrences of \(c\). Two circular words are equivalent when their **rotation-averaged Parikh matrices** agree. All equivalence classes have size at most two. When \(h\geq2\), the **entire set of non-singleton classes** consists of the \(h-1\) pairs

\[
\big\{\,[b\,c^{j-1}aa\,c^{h+1-j}],\ [b\,c^{j-2}a\,cc\,a\,c^{h-j}]\,\big\},\qquad 2\leq j\leq h.
\]

Here brackets mean cyclic conjugacy classes (not linear words). No two displayed pairs overlap, and every other circular word in the fixed composition is distinguished by its matrix. Thus the exact number of attainable matrices, equivalently the largest collection of circular words distinguishable by this observation, is

\[
K(h)=\binom{h+2}{2}-\max\{h-1,0\}=
\begin{cases}
1,&h=0,\\
(h^2+h+4)/2,&h\geq1.
\end{cases}
\]

There are precisely \(h-1\) doubleton classes and \((h^2-h+6)/2\) singleton classes for \(h\geq1\). The fraction of all such circular words that are uniquely recoverable tends to one. In contrast, with exactly one \(a\), one \(b\) and any number of \(c\)'s, the rotation-averaged Parikh matrix is always injective.

## Assumptions and scope

For a linear word \(v\) over \(\{a,b,c\}\), let \(|v|_u\) count position-distinct *scattered subsequence embeddings* of the word \(u\) in \(v\). Its standard ternary Parikh matrix is

\[
\Psi(v)=\begin{pmatrix}
1&|v|_a&|v|_{ab}&|v|_{abc}\\
0&1&|v|_b&|v|_{bc}\\
0&0&1&|v|_c\\
0&0&0&1
\end{pmatrix}.
\]

Write \([v]\) for its cyclic rotations and \(\Psi([v])=|[v]|^{-1}\sum_{u\in[v]}\Psi(u)\), as defined in Poovanandran--Simpson--Teh. For the stated composition, \(b\) occurs once, so every circular word has precisely \(n=h+3\) rotations and has a unique representative beginning with \(b\). Index the remaining \(h+2\) positions by \(1,\ldots,h+2\), and denote by \(W_{h;t,u}\) the class with \(a\)'s at positions \(1\leq t<u\leq h+2\), with \(c\)'s at the others. Thus there are exactly \(\binom{h+2}{2}\) input necklaces, not length-\(n\) linear words.

## Proof

**A positional evaluation of every matrix.** Set \(n=h+3\), \(s=t+u\), and \(d=u-t>0\). Sum over the \(n\) ways of cutting the anchored circle to obtain a linear rotation. For an \(a\) at position \(v>0\), the ordered pair \(ab\) appears in precisely \(v\) cuts; hence the sum of the \(ab\)-counts is \(s\). For a \(c\) at position \(v>0\), the pair \(bc\) appears in precisely \(n-v\) cuts. The \(c\)-positions sum to \(n(n-1)/2-s\), so the sum of the \(bc\)-counts is \(nh-n(n-1)/2+s\).

For an ordered triple \((a,b,c)\) with its \(a\) at position \(v\) and its \(c\) at position \(w\), the cyclic order can become \(abc\) under a cut exactly if \(w<v\), and then it does so in precisely \(v-w\) cuts. The \(a\) at \(t\) contributes \(t(t-1)/2\) to the sum of the \(abc\)-counts. The \(a\) at \(u\) contributes \(u(u-1)/2-(u-t)\), since the earlier \(a\) must be excluded from the potential \(c\)-positions. Consequently the sum is

\[
Y(t,u)=\frac{t(t-1)+u(u-1)}{2}-(u-t)
=\frac{s^2-2s+(d-2)^2-4}{4}.
\]

Dividing these rotation sums by \(n\) gives the full matrix

\[
\Psi(W_{h;t,u})=
\begin{pmatrix}
1&2&s/n&Y(t,u)/n\\
0&1&1&h-(n-1)/2+s/n\\
0&0&1&h\\
0&0&0&1
\end{pmatrix}.
\]

The displayed entries, together with the fixed letter counts, show that two such matrices agree if and only if both \(s=s'\) and \((d-2)^2=(d'-2)^2\). Because \(d,d'\) are positive integers, the latter equality implies either \(d=d'\) or \(\{d,d'\}=\{1,3\}\). In the first case equality of \(s\) also forces \(t=t'\) and \(u=u'\); this is the same necklace. In the second case the only possible distinct pairs of positions are \((j,j+1)\) and \((j-1,j+2)\), for \(2\leq j\leq h\). These are exactly the displayed doubleton classes. No third configuration can share their matrix, proving both completeness and the size-two bound.

There are \(h-1\) such pairs when \(h\geq2\) and none when \(h\leq1\). Subtracting one from the number of inputs for each merged pair yields \(K(h)\). Subtracting two for each merged pair yields the singleton count. For \(h\geq1\), the singleton fraction is

\[
\frac{h^2-h+6}{h^2+3h+2}\longrightarrow1.
\]

Finally, if there is only one \(a\), its position \(t\) after the unique \(b\) gives the summed \(ab\)-entry \(t\). Hence every such necklace has a distinct averaged Parikh matrix, proving the asserted sharp boundary between one and two occurrences of the first letter.

## Verification

Run `python3 verify_circular_parikh.py` using Python's standard library. The independent oracle directly forms each anchored circular word, enumerates every cyclic rotation, and counts its \(ab\), \(bc\), and \(abc\) subsequences by a streaming recurrence rather than the positional proof formula. It confirms exact rational matrices, the complete list of doubletons, and singleton/profile counts for every \(h\) from \(0\) through \(35\): \(8436\) anchored two-\(a\) words in total. It also checks the one-\(a\) injectivity boundary through \(h=35\). These finite tests corroborate; the unrestricted result is proved above.

## Relationship to prior work

Poovanandran, Simpson, and Teh (2021 preprint, 2024 journal) introduced the rotation-averaged Parikh matrix, formulated the general ternary equivalence problem, and proved the conditional circular rewriting rule \(CE_1\) (their Theorem 5.4). In particular, their already-known \(CE_1\) rule covers the local exchange \(caac\leftrightarrow acca\), explaining **sufficiency** of the displayed pairs; that local exchange is **not** claimed as new. The present contribution is an exact **converse** for the specified infinite fixed-composition family: the matrix formula excludes every other collision, completely gives all fibers, and yields their exact sizes and attainable-matrix count. The earlier paper does not state this fixed-composition classification or count.

The 2025 work of Janaki and collaborators studies polynomial \(q\)-weighted *circular* Parikh matrices and their different ambiguity relation; its inspected results do not provide this fixed-composition unweighted fiber census. Dick and collaborators study ambiguity reduction using Parikh matrices of Lyndon conjugates and projections, a different observation map. The restriction to one \(b\) and two \(a\)'s is motivated by the least multiplicity supporting non-injectivity in the anchored singleton-middle-letter family, rather than by choosing a random finite length.

## Limitations

The theorem does not classify ternary circular words with two or more \(b\)'s, nor the full family with one \(b\) and three or more \(a\)'s. It concerns the unweighted, uniform rotation-average of the standard Parikh matrix, not the direct circular subword count, the matrix of a single Lyndon representative, or a polynomial \(q\)-matrix. Only a self-review has been performed; no independent audit or external formal proof certification is asserted. A previously overlooked equivalent fixed-composition classification remains possible.

## References

1. G. Poovanandran, J. Simpson, and W. C. Teh, *Counting Subwords in Circular Words and Their Parikh Matrices*, arXiv:2110.14858v1, first submitted 28 October 2021; later *Theoretical Computer Science* 985 (2024), 114344. https://arxiv.org/html/2110.14858v1 . See especially Definition 4.1, Question 5.2, Theorem 5.4, and Rule \(CE_1\).
2. K. Janaki, M. Sivaji, R. Suresh, R. Elayaraja, and S. Felixia, *Parikh q-Matrices for Circular Words*, *IAENG International Journal of Computer Science* 52(4) (2025), 1023--1029. https://www.iaeng.org/IJCS/issues_v52/issue_4/IJCS_52_4_13.pdf .
3. J. Dick, L. K. Hutchinson, R. Mercaş, and D. Reidenbach, *Reducing the Ambiguity of Parikh Matrices*, LATA 2020, pp. 397--411. https://pmc.ncbi.nlm.nih.gov/articles/PMC7206623/ .
