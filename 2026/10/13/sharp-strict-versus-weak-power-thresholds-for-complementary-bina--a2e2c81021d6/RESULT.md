# The strict and weak 5/2 boundary for complementary binary morphisms of length seven

## Finding

For a finite binary word \(w\), let \(\operatorname{ce}(w)\) be the maximum of \(|u|/\operatorname{per}(u)\) over its nonempty contiguous factors \(u\), with \(\operatorname{per}(u)\) the least positive period. Set the exponent of the empty word to zero. For \(|v|=7\), define \(h_v(0)=v\), \(h_v(1)=\bar v\), and extend by concatenation.

No such morphism sends every finite word with \(\operatorname{ce}<5/2\) to one with \(\operatorname{ce}<5/2\). In fact `01` witnesses failure for every \(v\). The morphisms preserving \(\operatorname{ce}\le5/2\) on every finite word are exactly those with
\[
v\in\{\mathtt{0100110},\mathtt{0110010},\mathtt{1011001},\mathtt{1001101}\}.
\]
For every other \(v\), `001` witnesses failure of weak preservation. The two input words have critical exponents 1 and 2, respectively.

## Proof

Output complementation does not change exponents, so normalize \(v\) to start in zero. For any fixed period candidate \(p\) in a word \(y\), a consecutive run of \(r\) matches in the comparison \(y_i=y_{i+p}\) is equivalent to a corresponding factor of length \(p+r\) having period \(p\). The condition \(2(p+r)\ge5p\) therefore detects a factor of exponent at least \(5/2\); replacing \(\ge\) by \(>\) detects a factor above that bound. It suffices to test \(p<|y|\), since a factor admitting no shorter period has exponent 1. Testing a period that is not the least cannot give a false violation, since the least period is at most the tested one.

The following finite table uses every normalized \(v\), i.e. every six-bit suffix of the initial zero. The accompanying `verify_length7.js` computes each table entry by the distance comparisons just described.

| Input | Condition on its image | Normalized images \(v\) that pass |
|---|---|---|
| `01` | critical exponent \(<5/2\) | none |
| `001` | critical exponent \(\le5/2\) | `0100110`, `0110010` |

The first row excludes all strict preservers, and the second excludes all other weak preservers. For the positive direction use Kobayashi's sufficient criterion, in [1, Theorem 4], at \((5/2)^+\). Both remaining normalized images and their complements have least period 6, hence exponent \(7/6<2\). The two images of each morphism start with distinct bits, and end with distinct bits. For every ordered pair of images, there is no equality of a prefix of the first image and a suffix of the second of lengths 4, 5, or 6, as the finite check confirms. Thus the long-overlap requirement of the criterion holds; length 7 cannot match distinct images, and full self-overlaps have empty residuals. Finally, the criterion tests each \((5/2)^+\)-free input of length at most \(\lceil5/2\rceil+1=4\). The empty word is automatic. There are 22 nonempty admissible inputs, and for each remaining normalized \(v\) all 22 outputs obey the weak bound, by the same exact distance comparison. The criterion yields preservation for inputs of every length. Taking output complements produces the displayed four maps.

## Scope and relationship to prior work

The distinction is between forbidding equality and allowing equality at the same exponent, within complementary uniform binary morphisms of length seven. This is not an admissible-length theorem at arbitrary thresholds or a classification of noncomplementary maps. Shallit, Shur and Zorcic [1] give a classification up to \(7/3\), existence results below 3, and pose the wider transition problem in Section 4. Their construction for odd lengths in the proof of Theorem 9 gives \((3-1/k)^+\) for the selected length-\(k\) morphism; at \(k=7\) this does not give a \((5/2)^+\) classification. A public length-set announcement [2] covers the strict/weak distinction at length five and \(8/3\) and addresses the weak stability interval starting at \((8/3)^+\), not this length-seven classification at \(5/2\). Equivalent unpublished or unindexed results may exist.

## Reproduction

Run `node verify_length7.js` in this directory. The exact finite tests establish both rows of the table and the hypotheses of the cited criterion. The all-input positive conclusion is an application of that criterion, not an extrapolation from the finite computation.

[1] J. Shallit, A. M. Shur and S. Zorcic, *Power-free Complementary Binary Morphisms*, J. Combin. Theory Ser. A 207 (2024), 105910; [arXiv:2310.15064v3](https://arxiv.org/html/2310.15064v3), Theorems 4, 5 and 9 and Section 4. Theorem 4 restates Y. Kobayashi, *Repetition-free words*, Theoret. Comput. Sci. 44 (1986), 175–197.

[2] [*The 8/3-plus stability conjecture for power-free binary morphism lengths*](https://vibemathed.com/problem/the-8-3-plus-stability-conjecture-for-power-free-binary-morphism-lengths), public result announcement marked candidate/review pending.
