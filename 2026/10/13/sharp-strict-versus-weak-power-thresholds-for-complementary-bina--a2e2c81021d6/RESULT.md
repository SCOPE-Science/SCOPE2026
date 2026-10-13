# Sharp strict-versus-weak power thresholds for complementary binary morphisms of lengths five and seven

## Finding
For a binary word \(v\), define the complementary uniform morphism \(h_v(0)=v\) and \(h_v(1)=\overline v\), where \(\overline v\) replaces every bit by its complement. A morphism is \(\alpha\)-free if it sends every word with critical exponent strictly less than \(\alpha\) to another such word; \(\alpha^{+}\)-free means the corresponding weak inequality holds on both input and output.

**Theorem.** Among complementary binary morphisms of length \(5\), none is \(8/3\)-free, and precisely four are \((8/3)^{+}\)-free. Their images of zero are
\[
\{\mathtt{01001},\mathtt{01101},\mathtt{10110},\mathtt{10010}\}.
\]
Among complementary binary morphisms of length \(7\), none is \(5/2\)-free, and precisely four are \((5/2)^{+}\)-free. Their images of zero are
\[
\{\mathtt{0100110},\mathtt{0110010},\mathtt{1011001},\mathtt{1001101}\}.
\]
These are exact statements for every finite binary input word, not merely for a tested prefix or a fixed point.

## Assumptions and scope
For a nonempty word \(w\), a positive integer \(p\) is a period when \(w[i]=w[i+p]\) whenever both positions lie in the word. Its critical exponent \(\operatorname{ce}(w)\) is the maximum of \(|u|/\operatorname{per}(u)\) over all nonempty contiguous factors \(u\) of \(w\), where \(\operatorname{per}(u)\) is the least period. Equivalently, \(w\) is \(\alpha\)-free if no factor has exponent at least \(\alpha\), and it is \(\alpha^{+}\)-free if no factor has exponent strictly greater than \(\alpha\). The threshold at equality is part of the statement. No restriction is imposed on the length or recurrence of the input word.

Complementing both images complements the entire output, so it preserves all factor exponents. Accordingly, only words \(v\) beginning with zero require direct enumeration: there are \(2^{4}=16\) at length five and \(2^{6}=64\) at length seven.

## Proof
**Finite obstruction and exhaustive classification.** For each length \(k\in\{5,7\}\), each normalized \(v\) beginning with zero, and the corresponding threshold \(\alpha\), enumerate every nonempty binary input \(x\) of length at most four whose critical exponent meets the selected strict or weak freeness condition. There are exactly 22 such inputs for either threshold and either inequality. Form \(h_v(x)\). Examine all factor starts, all factor lengths, and all possible periods; the exact integer inequalities \(3\ell\ge8p\) or \(3\ell>8p\), respectively, test the strict and weak \(8/3\) bounds, while \(2\ell\ge5p\) or \(2\ell>5p\) test the \(5/2\) bounds. A period is verified by all its required bit equalities. Thus a recorded violating factor is a finite proof that the proposed morphism fails globally.

The complete enumeration in `verify.py` and `witnesses.tsv` gives the following exact numbers among the normalized images:

| Image length | Threshold | Failing strict cases | Failing weak cases | Weak-freeness survivors |
| --- | --- | ---: | ---: | --- |
| \(5\) | \(8/3\) | 16 of 16 | 14 of 16 | `01001`, `01101` |
| \(7\) | \(5/2\) | 64 of 64 | 62 of 64 | `0100110`, `0110010` |

All 156 exclusions have an explicit source word and violating factor recorded in the certificate. The strict nonexistence and the absence of any other weakly free morphisms therefore follow without any extension of finite observations to infinite words.

**Proving global preservation for survivors.** Apply the sufficient criterion of Kobayashi, in the form stated as Theorem 4 by Shallit, Shur, and Zorcic [1]. For \(\alpha=(8/3)^{+}\) or \(\alpha=(5/2)^{+}\), this criterion says a \(k\)-uniform morphism is \(\alpha\)-free if (a) each single-letter image has exponent less than two; (b1,b2) distinct input letters have images with distinct initial and terminal letters; (b3) a prefix of any image of length at least \(k/2\) that is also a suffix of an image has the matching residual words prescribed by the criterion; and (c) every \(\alpha\)-free input of length at most \(\lceil\alpha\rceil+1=4\) has an \(\alpha\)-free image.

For all four normalized survivors the least period of each single-letter image is three at length five, and six at length seven, so (a) holds; complements share the same least period. Condition (b1,b2) holds by the bit complement. To check (b3), inspect all ordered pairs of images and all overlap lengths \(\lceil k/2\rceil\le r<k\). In these four cases no prefix of length \(r\) of either image equals a suffix of length \(r\) of either image. Thus the implication (b3) holds vacuously. Finally, the exhaustive factor-period check for all 22 admissible input words of lengths one through four verifies (c). Consequently the criterion establishes preservation for **all** weakly free input words, not just the tested finite ones. Output complementation gives the two additional morphisms at each length.

This supplies both directions and completes the classification.

## Verification
In the directory containing `verify.py` and `witnesses.tsv`, run `python3 verify.py` with Python 3 standard library only. The program rebuilds every certificate row and compares it byte-for-value after TSV parsing, reconstructs all 22 admissible inputs in each case, and checks Kobayashi conditions (a), (b1), (b2), (b3), and (c) for each surviving normalized image. Exact integer comparisons handle equality at the boundary; an independent fraction-based computation of each finite image's maximal exponent checks that the weak boundary is attained rather than merely bounded above.

Successful completion reports `VERIFY_OK normalized_candidates=80 failed_strict=80 failed_plus=76 surviving_plus=4 finite_source_words=22 boundaries=8/3,5/2`. The finite verification is a rigorous certificate because the excluded cases each have a finite bad input and the positive cases invoke the published global sufficient criterion. A run of the code alone, without the criterion, would not prove the infinite statement.

## Relationship to prior work
Shallit, Shur, and Zorcic [1] study complementary power-free binary morphisms and explicitly ask for phase transitions between \((7/3)^{+}\) and \(3\), including a conjectured transition at \(8/3\). Their Theorem 9 proves that for lengths other than three and six there exists a complementary morphism preserving some exponent below three, but does not give the two exact short-length strict/weak classifications above. Their cited Kobayashi criterion is used here as a proof tool, not claimed as a new lemma. The theorem supplies two fully classified test lengths and exhibits the boundary distinction at each specified exponent. It does not assert a complete transition classification at arbitrary lengths.

## Limitations
Only complementary morphisms of lengths five and seven, at the indicated exponents, are classified. No claim is made about arbitrary noncomplementary uniform morphisms, other exponents, other image lengths, or monotonicity of the full admissible-length spectrum. The argument relies on the published Kobayashi sufficient criterion for the positive direction. An unpublished or unindexed prior classification could affect historical priority, even though none was identified in the inspected literature.

## References
[1] Jeffrey Shallit, Arseny M. Shur, and Stefan Zorcic, *Power-free Complementary Binary Morphisms*, arXiv:2310.15064, first public version 23 October 2023; especially Theorems 4, 5, 9 and Section 4. https://arxiv.org/abs/2310.15064 ; https://arxiv.org/html/2310.15064v3 .

[2] Y. Kobayashi, *Repetition-free words*, Theoretical Computer Science 44 (1986), 175–197; sufficient condition restated explicitly in [1, Theorem 4].
