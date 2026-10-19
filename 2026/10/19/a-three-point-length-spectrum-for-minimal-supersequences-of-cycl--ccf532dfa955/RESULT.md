# A three-point length spectrum for minimal supersequences of cyclically shifted permutations

## Finding
Let \(n\ge3\), let \(\Sigma_n=\{0,1,\ldots,n-1\}\), and put
\[
 A_n=0\,1\cdots(n-1),\qquad B_n=1\,2\cdots(n-1)\,0.
\]
A word \(W\) is a *minimal common supersequence* if it contains both inputs as scattered subsequences, but deleting any single position destroys at least one of those two embeddings (possibly both). Then **every** minimal common supersequence \(W\) satisfies precisely one of the following descriptions:

1. \(W=A_n0\), of length \(n+1\);
2. \(W=B_n(1\,2\cdots(n-1))\), of length \(2n-1\);
3. \(|W|=2n\), with exactly two occurrences of every alphabet symbol.

Both displayed shorter words are minimal and are the *only* minimal common supersequences shorter than \(2n\). There is at least one minimal word in the third class for every \(n\ge3\). Consequently the full set of achievable lengths is
\[
 \{n+1,\ 2n-1,\ 2n\}.
\]
In particular, no length from \(n+2\) through \(2n-2\) is achieved when that interval is nonempty. The two shorter minimal words are uniquely determined, not just their lengths. For \(n=2\) the only minimal words are \(010\) and \(101\), both of length three.

## Assumptions and scope
All alphabet symbols are distinct within either input, all supersequences are finite words, and subsequence embeddings need not use consecutive positions. A *minimal* common supersequence means minimal in the deletion/subsequence partial order; it is not synonymous with a shortest common supersequence. The main assertion ranges over every integer \(n\ge3\) and considers supersequences over any ambient alphabet: an extraneous symbol could never occur in a minimal word, so restricting to \(\Sigma_n\) loses nothing.

## Proof
**Essential-position lemma.** Fix embeddings \(\alpha\) of \(A_n\) and \(\beta\) of \(B_n\) in a minimal word \(W\). Every position of \(W\) belongs to at least one of these two embeddings. Otherwise deleting a position outside their union preserves both embeddings, contradicting minimality. Because each input uses each symbol precisely once, no symbol occurs more than twice in \(W\). Every symbol occurs at least once because it occurs in each input.

**Case of one zero.** Both embeddings must use that unique zero. Since \(B_n\) requires the full string \(C=1\,2\cdots(n-1)\) *before* zero and \(A_n\) requires the same \(C\) *after* zero, every prefix position before zero belongs to the \(B_n\)-embedding, and every suffix position after zero belongs to the \(A_n\)-embedding: a position on the wrong side cannot help the other input. No extra positions are possible by the essential-position lemma. Thus \(W=C0C=B_nC\), of length \(2n-1\). This word is minimal, since each side of its only zero is the unique possible embedding of the corresponding \(C\).

**Case of two zeros.** The two zero positions must be essential, so the chosen two embeddings use different zeros. The \(A_n\)-embedding uses the *first* zero and the \(B_n\)-embedding uses the *second*: if \(B_n\) used the first zero, it could also use the later zero after its already embedded \(C\), making the first zero inessential to \(B_n\). The first zero would then be used by neither the fixed \(A_n\)-embedding nor essentially by \(B_n\), a contradiction. The other assignments either leave one zero unused or reduce to this contradiction.

Suppose some nonzero symbol \(j\in\{1,\ldots,n-1\}\) occurs only once in \(W\). It must be used by both embeddings, and lies between the zeros. Split \(W=L\,j\,R\). To embed \(A_n\), the left factor \(L\) must contain \(0\,1\cdots(j-1)\); to embed \(B_n\), it need only contain \(1\cdots(j-1)\). The latter required prefix is already a subsequence of the former. Fix the \(A_n\)-embedding on \(L\), and the \(B_n\)-embedding to the right of \(j\). A position of \(L\) outside the chosen \(A_n\)-prefix embedding could be removed while leaving \(A_n\) intact, and \(B_n\) could use that same chosen prefix, contradicting minimality. Therefore \(L=0\,1\cdots(j-1)\), with no additional positions. Symmetrically, the \(B_n\)-required right suffix \((j+1)\cdots(n-1)\,0\) contains the \(A_n\)-required suffix \((j+1)\cdots(n-1)\). Fixing the \(B_n\)-embedding on \(R\) forces \(R=(j+1)\cdots(n-1)\,0\). Therefore \(W=0C0=A_n0\). Both zeros and every letter of \(C\) are essential in this word, so it is minimal.

If no nonzero symbol is singleton, the essential-position lemma forces it to occur *exactly twice*, and the two zeros already occur twice. Hence \(|W|=2n\). This exhausts all possible minimal supersequences.

**Existence at full length.** For \(n\ge3\), form
\[
 E_n=(1\,0)(2\,1)(3\,2)\cdots((n-1)\,(n-2))(0\,(n-1)).
\]
The displayed pairs are concatenated; \(|E_n|=2n\). In the \(A_n\)-embedding, the early zero and then the *second* occurrence of each nonzero symbol are forced: the first copy of \(1\) precedes the early zero, and inductively the first copy of \(j\ge2\) precedes the forced second copy of \(j-1\). The late zero cannot serve \(A_n\) because fewer than \(n-1\) nonzero symbols follow it. In the \(B_n\)-embedding, the *first* occurrence of each nonzero symbol and then the late zero are forced, working backwards: the second copy of \(n-1\) lies after the late zero, and the second copy of \(j<n-1\) follows the forced first copy of \(j+1\). The early zero cannot serve \(B_n\) because fewer than \(n-1\) nonzero symbols precede it. Hence each input has a unique embedding in \(E_n\), and those embeddings are disjoint and cover every position. Deleting any position destroys one of these unique embeddings. Thus \(E_n\) is minimal, completing the proof.

The \(n=2\) boundary follows directly by considering the six binary words containing two copies of each symbol: none is minimal, while \(010\) and \(101\) are minimal. This final small check does not enter the proof for \(n\ge3\).

## Verification
Run `python3 verify.py` with Python 3. The included checker enumerates all distinct order-preserving merges of the two source words, tests every single-position deletion, and compares the result with the rigid three-point theorem for \(2\le n\le8\). Its finite counts at full length for \(n=3,4,5,6,7,8\) are respectively \(1,8,34,122,417,1416\); it also confirms exactly one shorter word at each of the two advertised lengths. An independent direct enumeration over the complete alphabet-product search space for \(n=2,3,4\) agrees with the merge enumeration. The script additionally verifies the explicit full-length witness for every tested \(n\ge3\). These finite calculations are checks, not a replacement for the proof of all \(n\).

## Relationship to prior work
Sopp, Liyanage, Gong, and Zhu (2026) study construction and enumeration of minimal common supersequences for arbitrary pairs of strings, characterize essential positions, and give an enumeration data structure. Their accessible complete paper does not state the cyclic-permutation input family, its exact length spectrum, or the uniqueness of its two submaximal words. Our essential-position observation is compatible with their general lemma; the new step is a family-specific infinite structural classification showing an expanding forbidden interval of lengths. Fraser, Irving, and Middendorf (1996) developed earlier general algorithms for longest minimal common supersequences. The accessible abstract establishes that algorithmic background but does not settle this symbolic length spectrum. See the documented access limitation below.

## Limitations
The theorem is for two distinct-letter permutations related by moving the first letter to the end; it does not classify all full-length minimal words and does not extend as stated to arbitrary strings with repeated letters. The full text of the 1996 article could not be inspected through accessible routes; differently formulated antecedents in that or other literature remain a novelty risk. The finite enumeration counts are verified only through \(n=8\), while the proof itself is uniform in \(n\).

## References
1. B. Sopp, A. Liyanage, M. Gong, and B. Zhu, *Computing and Enumerating Minimal Common Supersequences Between Two Strings*, arXiv:2603.22591v1, originally public 2026-03-23. https://arxiv.org/html/2603.22591v1 ; https://arxiv.org/abs/2603.22591 . In particular, the essential-index characterization and the enumeration theorems in Sections 3 and 5.
2. C. B. Fraser, R. W. Irving, and M. Middendorf, *Maximal Common Subsequences and Minimal Common Supersequences*, Information and Computation 124 (1996), 145–153, doi:10.1006/inco.1996.0011. https://doi.org/10.1006/inco.1996.0011 . Abstract and bibliographic data inspected; full text was unavailable.
