# The first three-position circular Chacon attractor and its 546 optima

## Finding

For \(C_0=a\) and \(C_{k+1}=C_kC_kbC_k\), let \(\gamma_c(C_k)\) be the minimum number of positions meeting an occurrence of every nonempty circular factor of length at most \(|C_k|\). The complete first four stages have
\[
(\gamma_c(C_1),\gamma_c(C_2),\gamma_c(C_3),\gamma_c(C_4))=(2,2,2,3).
\]
The respective numbers of minimum position sets are \(3,3,1,546\). In particular \(C_4\), of length \(121\), is the first nontrivial stage of this Chacon construction whose circular attractor requires three positions. One optimal triple is \(\{0,16,80\}\).

## Assumptions and scope

All strings use the alphabet \(\{a,b\}\), concatenation is juxtaposition, and positions are zero-based. For a word \(w\) of length \(N\), a circular factor of length \(\ell\), where \(1\le\ell\le N\), is the length-\(\ell\) prefix of a rotation of \(w\). Its occurrence starting at \(i\) covers the cyclic interval \(\{i,i+1,\ldots,i+\ell-1\}\) modulo \(N\). A circular attractor is a position set intersecting at least one occurrence of every such factor. Distinct sets are counted in the fixed zero-based representative \(C_k\), rather than modulo rotations of the position sets. No claim for \(k\ge5\) follows from this finite result.

## Proof

The word recurrence yields lengths \(4,13,40,121\) for \(C_1,C_2,C_3,C_4\). Each word contains both letters, so the factors \(a\) and \(b\) force every circular attractor to contain at least two positions. The direct complete circular-factor test described below finds exactly \(3,3,1\) attracting pairs for the first three words; examples of such pairs are respectively \(\{0,2\}\), \(\{0,8\}\), and \(\{4,26\}\). This proves the first three minima.

For the fourth word, define the coverage \(B(f)\) of a circular factor \(f\) as the union of all cyclic positions on all its occurrences. Direct expansion of the recurrence and literal substring comparison gives the following five factors and **all** their zero-based circular starting positions:

| factor | length | circular starts |
| --- | ---: | --- |
| `baabaaababaabab` | 15 | 66 |
| `aaabaaababaabaa` | 15 | 39, 120 |
| `aaabaaababaabab` | 15 | 12, 52, 93 |
| `baabaaababaabaa` | 15 | 26, 80, 107 |
| `aaabab` | 6 | 3, 16, 30, 43, 56, 70, 84, 97, 111 |

Write these five coverage sets as \(B_1,\ldots,B_5\). The first is the integer interval \([66,80]\); the second is \([0,13]\cup[39,53]\cup\{120\}\); the third is \([12,26]\cup[52,66]\cup[93,107]\); and the fourth is \([26,40]\cup[80,94]\cup[107,120]\). The fifth is the union of the nine six-position intervals beginning at the displayed starts. All intervals here use the same zero-based coordinates, without wrapping except as displayed for \(B_2\).

Notice \(B_1\cap B_2=\varnothing\). A pair meeting both must have one position \(i\in[66,80]\) and the other \(j\in B_2\). If \(67\le i\le79\), it also requires \(j\in B_2\cap B_3\cap B_4\), which is empty because \(B_2\cap B_3=\{12,13,52,53\}\) does not meet \(B_4\). If \(i=66\), the candidate \(j\) must be in \(B_2\cap B_4=\{39,40,120\}\), none of which lies in \(B_5\); also \(66\notin B_5\). If \(i=80\), the candidate \(j\) must be in \(B_2\cap B_3=\{12,13,52,53\}\), again disjoint from \(B_5\), and \(80\notin B_5\). Thus no pair meets all five factors, and \(\gamma_c(C_4)\ge3\).

It remains to prove an upper bound and the exact multiplicity. For a finite word \(w\), initialize an empty dictionary indexed by literal factors. For every length \(1\le\ell\le|w|\) and each circular start \(0\le i<|w|\), read the literal factor from \(ww\) and add its cyclic length-\(\ell\) interval to its dictionary entry. By definition, a position set is a circular attractor **if and only if** it intersects every stored dictionary mask. Thus the finite computation is exhaustive, without a sampling assumption or hash collisions. The embedded standalone checker implements this direct construction and evaluates every unordered position subset of sizes two and (for \(C_4\)) three. It finds exactly \(546\) attracting triples in \(C_4\), including \(\{0,16,80\}\), proving the upper bound and the stated exact count.

## Verification

Run `python3 check.py` from this package with Python 3. It uses only the standard library; `check_output.txt` records its complete output. The checker directly forms all \(10,582\) distinct circular factors of \(C_4\) and tests all \(\binom{121}{2}=7,260\) pairs and all \(\binom{121}{3}=287,980\) triples. The resulting numbers of attracting pairs and triples are \(0\) and \(546\). It verifies the five explicit occurrence lists, the five-factor pair obstruction, and the proposed attracting triple independently of the multiplicity count. For the smaller words the distinct circular-factor counts are \(13\), \(124\), and \(1,159\).

## Relationship to prior work

Béal, Crochemore, and Romana study linear word attractors and give Chacon-sequence experiments; their word construction motivates the present problem but does not provide the asserted circular-stage classification. Basiricò gives explicit size-three attractors for finite Chacon words in the **linear** setting, which neither implies that a circular three-set exists nor supplies this optimal circular count. Romana's circular-attractor work develops general checking algorithms, not these Chacon-specific factor and optimal-position counts. The structural five-factor argument separates this finite claim from a mere generic application of the definitions.

## Limitations

This is an exact finite classification through order four, not an infinite-order theorem. An independent audit has not been performed. Basiricò's complete paper was not accessible for full-text inspection; its available abstract concerns linear attractors. Priority under alternative terminology or overlooked finite tables remains possible. The numerical count is supported by exhaustive executable verification, not an independently formalized certificate.

## References

1. M.-P. Béal, M. Crochemore, and G. Romana, *Checking and producing word attractors*, arXiv:2509.08503, initially public 2025-09-10, revised 2026-10-09. https://arxiv.org/abs/2509.08503
2. G. Romana, *Algorithmic View on Circular String Attractors*, ICTCS 2023, pp. 169–180. https://ceur-ws.org/Vol-3587/9885.pdf
3. E. Basiricò, *String Attractors of Finite Chacon Words*, SSRN 7147229 (2026). https://ssrn.com/abstract=7147229
