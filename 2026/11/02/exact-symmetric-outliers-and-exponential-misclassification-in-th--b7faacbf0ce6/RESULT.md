# The exact small-class cutoff in weighted approximation of three-class flip games

## Finding

Consider the three-class flip game of Einy and Haimanko [1]. There are three classes \(A,B,C\), each of \(m\ge5\) labelled voters. A coalition with counts \((a,b,c)\) wins if \(H=20a+15b+12c\) equals \(59\) or is at least \(61\). A weighted surrogate has nonnegative voter weights and a real quota, with ties at quota called winning. Count errors over all \(2^{3m}\) labelled coalitions. In a class-symmetric surrogate the weights are constant within each class.

The previously enumerated large-class regime [2] starts at \(m=9\), with exact class-symmetric error count \(\binom m3\). The remaining regime is:

| Voters per class \(m\) | Minimum symmetric error count | Misclassified profile in an optimal symmetric rule |
| --- | ---: | --- |
| 5 | 1 | \((0,0,5)\) |
| 6 | 6 | \((0,0,5)\) |
| 7 | 21 | \((0,0,5)\) |
| 8 | 56 | Either \((0,0,5)\) or \((3,0,0)\), but not both |

In each row the listed choices exhaust the error profiles of optimal symmetric surrogates. Dividing the counts by \(2^{3m}\) gives the corresponding optimal fractions. In particular \(m=8\) is the tie at the switch between sacrifices of \(C\)-only and \(A\)-only coalitions, and the minimum symmetric count over the entire family is \(\min\{\binom m3,\binom m5\}\). At \(m=5\), even if the weights need not be class-symmetric, the minimum is **exactly one** error among \(32768\) coalitions.

## Proof

**Four-profile obstruction.** The profile \(P=(1,1,2)\) wins; \(Q_A=(3,0,0),Q_B=(0,4,0),Q_C=(0,0,5)\) lose. For class weights \(u,v,w\) and quota \(q\), correct classification of the three losing profiles gives \(3u<q,4v<q,5w<q\), hence \(q>0\) and
\[
u+v+2w < (1/3+1/4+2/5)q=59q/60<q.
\]
This would misclassify \(P\), so every symmetric rule errs on at least one of the four profiles. The four error multiplicities are \(m^2\binom m2,\binom m3,\binom m4,\binom m5\), respectively. For \(5\le m\le8\), \(\binom m4>\binom m5\) and \(m^2\binom m2>\binom m3\). Moreover \(\binom m5/\binom m3=(m-3)(m-4)/20\), which is less than one for \(m<8\) and equals one at \(m=8\). Thus at least \(\binom m5\) errors are necessary, and if the bound is attained all errors must be from one of the minimum-size obstruction profiles.

**Sacrificing exactly \(Q_C\).** Use weights \((24,18,16)\) and quota \(73\). When \(H\ge62\) the new score is at least \(6H/5>73\). For \(H\le58\), \(0\le a\le2\); for each feasible \((a,b)\), test the largest \(c=\lfloor(58-20a-15b)/12\rfloor\). The resulting maxima for \(a=0,1,2\) are \(70,72,66\), below quota. The remaining profiles are completely enumerated because \(H\le61\) implies \(a\le3,b\le4,c\le5\):

| \(H\) | Profile | New score |
| ---: | --- | ---: |
| 59 | \((1,1,2)\) | 74 |
| 60 | \((3,0,0)\) | 72 |
| 60 | \((0,4,0)\) | 72 |
| 60 | \((0,0,5)\) | 80 |
| 61 | None | — |

Thus precisely the \(\binom m5\) coalitions with profile \(Q_C\) are mislabeled, for every \(m\ge5\). To attain the other tie at \(m=8\) one may use the \(Q_A\)-only surrogate of [2], whose proof works for all \(m\ge5\). Alternatively the weights \((30,20,16)\) at quota \(81\) do so: the same maximum test below \(59\) gives \(76,78,80\), the successive four attainable rows in the table give \(82,90,80,80\), and \(H\ge62\) gives at least \(4H/3>81\). This proves both sides of the tie and the stated exclusion of other optimal error profiles in the displayed range. For \(m\ge9\), use the established optimum [2]; among the four obstruction profiles only \(Q_A\) has that minimum multiplicity.

**Unrestricted first case.** If any unrestricted rule classified every coalition correctly, average its voter weights over the within-class permutations, retaining its quota. The status of a coalition is unchanged by those permutations; finitely many scores at least the quota still average to at least the quota, and finitely many strictly smaller scores still average to strictly below it. The averaged symmetric rule would therefore be perfect, contradicting the four-profile obstruction. At \(m=5\) there is just one instance of \(Q_C\): the entire \(C\) class. The \(Q_C\)-only surrogate thus proves that the integer lower bound of one error is sharp even without the symmetry restriction.

## Verification

The accompanying `verify.py` checks both complete low-score classifications and the high-score separation, and exhausts all \(32768\) labelled coalitions at \(m=5\). It uses Python 3.10 or newer (for `int.bit_count`). The optimum and the tie follow from the obstruction and exact constructions, not from optimizing over a finite sample of weight vectors.

## Relationship to prior work and limitations

Einy and Haimanko [1, Definition 17, Proposition 18] introduce this precise game and determine its normalized excess-weight deficit. Their Section 6 defines and bounds a different quantity, the minimum misclassification fraction, for general games. The misclassification objective is equivalent up to normalization to the outlier count discussed there and in [3]. The same-family treatment [2, Finding and Proof §2] already gives the large-\(m\) class-symmetric result and the stronger unrestricted asymptotic order \(\Theta(m^3/8^m)\). That coverage is not a contribution here. The exact small-class regime needs the other surrogate (sacrificing \(Q_C\), not \(Q_A\)), and its orbit multiplicity determines the finite crossover and certifies the unrestricted first case. This resolves how the large-class formula starts; it does not determine the unrestricted optimum at general \(m>5\) or assert historical priority.

1. E. Einy and O. Haimanko, *Large player classes and approximately weighted voting*, [arXiv:2610.08968](https://arxiv.org/abs/2610.08968).
2. *Exponentially rare optimal voting misclassification in a three-class flip game*, [Resultary dfb016c86552](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-exponentially-rare-optimal-voting-misclassification-in-a-three-c--dfb016c86552/RESULT.md), Finding and Proof §§1–3.
3. M. Albareda-Sambola, X. Molinero and S. Roura, *Weightedness measures from inequality systems*, *International Journal of Approximate Reasoning* 182 (2025), 109418, [doi:10.1016/j.ijar.2025.109418](https://doi.org/10.1016/j.ijar.2025.109418).
