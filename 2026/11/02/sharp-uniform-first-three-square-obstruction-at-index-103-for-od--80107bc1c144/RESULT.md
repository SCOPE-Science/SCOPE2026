# Sharp uniform first three-square obstruction at index \(103\) for odd-colored binary partitions

## Finding

For positive integers \(m\) and nonnegative integers \(n\), let \(b_m(n)\) be the number of partitions of \(n\) into powers of two, with each part given one of \(m\) colors. Define \(\rho(m)\) to be the least \(n\ge0\) for which \(b_m(n)\) is not a sum of three integer squares, provided such an index exists. Then

\[
\boxed{\max_{\substack{m\ge1\\m\text{ odd}}}\rho(m)=103,\qquad \rho(613)=103.}
\]

In particular every positive odd color count has a nonrepresentable coefficient among the first \(104\) coefficients, and the bound cannot be lowered. The result is not a classification of all nonrepresentable indices.

## Assumptions and scope

The generating function, as a formal power series over the integers, is
\[
B_m(x)=\sum_{n\ge0}b_m(n)x^n=\prod_{j\ge0}(1-x^{2^j})^{-m}.
\]
All quantified colors \(m\) are positive odd integers. Three-square representability permits zero, negative or positive integer square roots. Let \(\nu_2(t)\) be the exponent of two in a positive integer \(t\). By Legendre's three-square theorem, a positive integer \(t\) is not a sum of three squares exactly when \(\nu_2(t)\) is even and the odd part \(t/2^{\nu_2(t)}\) is \(7\pmod8\).

## Proof

**Coefficient recurrence.** Logarithmic differentiation of the formal product gives
\[
\frac{xB_m'(x)}{B_m(x)}=m\sum_{k\ge1}(2^{\nu_2(k)+1}-1)x^k.
\]
Indeed, the coefficient at \(x^k\) is \(m\sum_{2^j\mid k}2^j=m(2^{\nu_2(k)+1}-1)\). Therefore \(b_m(0)=1\) and, for each \(n\ge1\),
\[
 n b_m(n)=m\sum_{k=1}^{n}(2^{\nu_2(k)+1}-1)b_m(n-k). \tag{1}
\]
This identity supplies exact integer coefficients for the sharpness check.

**Uniform modular continuity in the color.** Suppose \(n\ge1\), \(q\ge1\), \(L\ge q+\lfloor\log_2n\rfloor\), and positive \(a,m\) satisfy \(m\equiv a\pmod{2^L}\). Then
\[
 b_m(n)\equiv b_a(n)\pmod{2^q}. \tag{2}
\]
To prove (2), write \(B_1(x)=1+f(x)\) with \(f(x)\in x\mathbb Z[[x]]\). In the expansion
\[
B_1(x)^{2^L}=\sum_{k=0}^{2^L}\binom{2^L}{k}f(x)^k,
\]
only \(1\le k\le n\) contribute at positive degrees at most \(n\). Here \(n<2^L\), and
\[
\nu_2\binom{2^L}{k}=L-\nu_2(k)\ge L-\lfloor\log_2n\rfloor\ge q.
\]
Thus \(B_1(x)^{2^L}\equiv1\pmod{(2^q,x^{n+1})}\). The least positive representative \(a\) of its residue class modulo \(2^L\) has \(m=a+2^Lt\) for some \(t\ge0\), so raising the last congruence to \(t\) proves (2). The same conclusion for arbitrary positive representatives follows by choosing that least representative.

**A finite residue-cylinder certificate proving the infinite upper bound.** The supplied `COVER.tsv` has exactly \(156\) data rows, each \((a,L,n,v)\) satisfying all of the following conditions:

1. \(a\) is odd, \(1\le a<2^L\), \(1\le L\le15\), \(1\le n\le103\), and \(v\ge0\) is even.
2. \(L\ge v+3+\lfloor\log_2n\rfloor\), and the exact integer coefficient satisfies
   \[
   b_a(n)\equiv7\cdot2^v\pmod{2^{v+3}}. \tag{3}
   \]
3. The classes \(m\equiv a\pmod{2^L}\) are pairwise disjoint and jointly comprise all positive odd integers. Their disjointness and completeness follow from a direct check of the \(2^{14}=16384\) odd classes modulo \(2^{15}\), together with the certificate's depth bound \(L\le15\).

Conditions (2) and (3), with \(q=v+3\), imply that every integer \(m\) in each certificate class has \(\nu_2(b_m(n))=v\) and odd part congruent to \(7\pmod8\). Legendre's theorem therefore excludes three-square representability of \(b_m(n)\). Because the disjoint classes cover all positive odd \(m\), this proves \(\rho(m)\le103\) for every such \(m\). The finite check is exhaustive for the **explicit finite collection of residue classes**, not a finite approximation to the infinite color range.

**Sharpness.** Independently applying (1) with \(m=613\), the exact \(104\) tuples \((n,\nu_2(b_{613}(n)),\operatorname{oddpart}(b_{613}(n))\bmod8)\), for \(0\le n\le103\), are printed in `SHARPNESS.tsv`. For every \(n<103\), either the valuation is odd or the odd part is not \(7\pmod8\). At \(n=103\), the exact tuple is \((103,6,7)\), giving \(b_{613}(103)\equiv448\pmod{512}\). All indices from zero through \(102\) are thus three-square representable; the index \(103\) is not. Hence \(\rho(613)=103\), and the previously proved universal upper bound is sharp.

## Verification

Place `COVER.tsv`, `SHARPNESS.tsv`, and `verify.py` in one directory and run `python3 verify.py` (Python standard library only). The checker directly multiplies the truncated factors \((1-x^{2^j})^{-a}\) modulo the exact \(2^{v+3}\) required by each cover row; checks all residue, valuation, precision, disjointness and completeness conditions; independently computes the \(613\)-color coefficients using recurrence (1), compares with independently multiplied generating factors, and checks all \(104\) sharpness entries. Expected output:

`VERIFY_OK leaves=156 covered_odd_classes=16384 maximum_index=103 maximum_depth=15 sharp_color=613 sharp_index=103 crosscheck=product_vs_derivative`

The proof above establishes why these exact finite checks suffice for all positive odd color counts. The checker's coverage of the finite certificate is exhaustive; it does not assert any unexamined infinite search is exhaustive.

## Relationship to prior work

Sobolewski and Ulas, *Values of Binary Partition Function Represented by a Sum of Three Squares* (preprint first publicly available 29 November 2022; subsequently published in 2023), determine representations for the special parameter family \(m=2^k-1\) and in their Problem 7.2 ask for a characterization for arbitrary positive \(m\). Their Proposition 7.3 supplies automaticity modulo fixed powers of two for each fixed \(m\), but does not give the sharp color-uniform first-obstruction bound obtained here. The coefficient-level congruence exploited here is standard in character and is not claimed separately as a new theorem. Gawron, Miska, and Ulas (2017) study the same generating-function family, including specific two-adic valuation results, but their inspected results do not give this sharp global odd-color bound.

An independently studied high-two-adic-valuation class, namely color counts divisible by \(64\), has a substantially earlier obstruction and does not imply the present odd-color claim. A previously considered two-color family also concerns even rather than odd color counts. Bibliographic searches did not identify an equivalent global odd-color result; this absence is not a proof of absolute priority.

## Limitations

Only odd positive numbers of colors are covered. No classification of all indices of nonrepresentable coefficients, no uniqueness claim about the maximizing color count, and no claim of optimal depth \(15\) or minimality of the \(156\)-row certificate is made. The numerical certificate is exact and independently replayable, but the mathematical proof and originality analysis have not undergone independent external audit. Unindexed work might contain a stronger equivalent theorem.

## References

1. B. Sobolewski and M. Ulas, *Values of binary partition function represented by a sum of three squares*, arXiv:2211.16622 (29 November 2022), https://arxiv.org/abs/2211.16622 ; *Results in Mathematics* **78**, article 188 (2023), https://doi.org/10.1007/s00025-023-01966-8 . See Problem 7.2 and Proposition 7.3.
2. M. Gawron, P. Miska and M. Ulas, *Arithmetic properties of coefficients of power series expansion of an infinite binary product*, arXiv:1703.01955 (6 March 2017), https://arxiv.org/html/1703.01955v1 . See Theorem 3.3 and valuation families.
3. Legendre's three-square theorem, classical representation criterion for sums of three integer squares.
