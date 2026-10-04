# The omitted four-weight cases are equivalent and projective
## Finding

Huang--Liang--Jia--Wan--Liao leave the complete weight distributions uncomputed in two four-weight cases: Theorem III.2 when
\[
\gamma\ne\operatorname{Tr}(-\beta/\alpha),
\]
and Theorem III.5 when
\[
\gamma\ne0.
\]
These two cases are in fact the same code family up to a coordinate permutation and a bijective parameter change.

Let
\[
D_1=
\{(x,y)\in\mathbb F_{p^m}^2:
\operatorname{Tr}(\alpha xy+\beta y+x)=\gamma\}
\]
with \(\alpha\ne0\), and let
\[
D_2=
\{(X,y)\in\mathbb F_{p^m}^{\ast}\times\mathbb F_{p^m}:
\operatorname{Tr}(\alpha Xy+X)=\gamma'\}.
\]
Put
\[
X=x+\beta/\alpha,
\qquad
\gamma'=\gamma+\operatorname{Tr}(\beta/\alpha).
\]
Under the Theorem III.2 hypothesis, \(\gamma'\ne0\), so this map sends \(D_1\) bijectively to \(D_2\).

The corresponding augmented codes are permutation equivalent. Therefore they have one common complete weight enumerator. For odd prime \(p\) and \(m\ge2\), define
\[
\begin{aligned}
w_1&=p^{2m-2}(p-1),\\
w_2&=p^{m-1}(p^m-p^{m-1}-1),\\
w_3&=p^{m-1}(p^m-p^{m-1}-2),\\
w_4&=p^{m-1}(p^m-1).
\end{aligned}
\]
Then
\[
W(z)
=
1+A_1z^{w_1}+A_2z^{w_2}+A_3z^{w_3}+A_4z^{w_4},
\]
where
\[
A_1
=
(p^m-1)
\left(
p^{m-1}+1+\frac{p^m(p-1)}2
\right),
\]
\[
A_2
=
(p^m-1)(p-1)(2p^{m-1}+1),
\]
\[
A_3
=
\frac{(p^m-1)p^{m-1}(p-1)(p-2)}2,
\qquad
A_4=p-1.
\]

The dual has
\[
A_1^\perp=A_2^\perp=0
\]
and
\[
A_3^\perp
=
\frac{
p^{m-1}(p-1)(p-2)
(p^{2m-2}-1)(p^m-1)
}{6}
>0.
\]
Hence every code in these two omitted cases is projective and has dual minimum distance exactly \(3\).

The smallest nonzero weight is
\[
d=w_3
=
p^{m-1}(p^m-p^{m-1}-2).
\]
Thus the minimum-distance expression printed in Theorem III.5 is not the distance of the displayed family. The difference between the correct value and the printed value is
\[
p^{m-2}(p^m-p-2)>0.
\]
For \(p=3\) and \(m=2,3,4\), the corrected formula reproduces the paper's own Table III parameters and weight enumerators.

## Assumptions and scope

The field is \(\mathbb F_{p^m}\), where \(p\) is an odd prime and \(m\ge2\). The trace is the absolute trace
\[
\operatorname{Tr}:\mathbb F_{p^m}\to\mathbb F_p.
\]
The codes are the augmented defining-set codes of the source, with codewords
\[
\left(
\operatorname{Tr}(ax+by)
\right)_{(x,y)\in D_i}
+c\mathbf 1,
\]
where \(a,b\in\mathbb F_{p^m}\) and \(c\in\mathbb F_p\).

The result concerns only the nondegenerate hypotheses of Theorems III.2 and III.5. No statement is made here about the source's other two cases.

## Proof

Write
\[
\delta=\beta/\alpha
\]
and set
\[
X=x+\delta.
\]
Then
\[
\alpha xy+\beta y+x
=
\alpha Xy+X-\delta.
\]
Taking traces gives
\[
\operatorname{Tr}(\alpha xy+\beta y+x)=\gamma
\]
if and only if
\[
\operatorname{Tr}(\alpha Xy+X)
=
\gamma+\operatorname{Tr}(\delta)
=
\gamma'.
\]
The Theorem III.2 hypothesis is exactly \(\gamma'\ne0\). If \(X=0\), the left-hand trace is \(0\), so no point of the target defining set has \(X=0\). Hence the affine map gives a bijection
\[
D_1\longrightarrow D_2.
\]

For a codeword parameter triple \((a,b,c)\),
\[
\operatorname{Tr}(ax+by)+c
=
\operatorname{Tr}(aX+by)
+
c-\operatorname{Tr}(a\delta).
\]
Thus
\[
(a,b,c)
\longmapsto
\left(
a,b,c-\operatorname{Tr}(a\delta)
\right)
\]
is a bijection of parameter spaces that preserves the corresponding coordinates after the defining-set permutation. The two codes are therefore permutation equivalent.

It remains to count the four weights in one family. Use the source's notation
\[
l_1=-\gamma,\qquad
l_2=\operatorname{Tr}(-b/\alpha)+c,\qquad
l_3=\operatorname{Tr}(-ab/\alpha),
\]
with \(l_1\ne0\). For each fixed \(b\ne0\), the map
\[
a\longmapsto l_3
\]
is a surjective \(\mathbb F_p\)-linear functional with kernel size \(p^{m-1}\), and for fixed \((a,b)\) the map \(c\mapsto l_2\) is bijective. Hence every pair
\[
(l_2,l_3)\in\mathbb F_p^2
\]
occurs exactly \(p^{m-1}\) times for each \(b\ne0\).

When \(l_3\ne0\), the source's character-sum formula separates according to
\[
\Delta=l_2^2-4l_1l_3.
\]
As \(l_2\) ranges over \(\mathbb F_p\) and \(4l_1l_3\) ranges over \(\mathbb F_p^\ast\), the number of pairs for which \(\Delta\) is zero, a nonzero square, or a nonsquare is respectively
\[
p-1,\qquad
\frac{(p-1)(p-2)}2,\qquad
\frac{p(p-1)}2.
\]
Indeed, the zero count is immediate. For nonzero squares, write
\[
l_2^2-\lambda=y^2
\]
with \(y\ne0\) and \(\lambda\ne0\). There are
\[
(p-1)(p-2)
\]
ordered pairs \((l_2,y)\) with \(l_2^2\ne y^2\), and division by the two choices \(\pm y\) gives the stated square count. The remaining pairs are nonsquares.

Combining these counts with the source's four character-sum weights gives the stated frequencies. Their sum with the zero word is
\[
p^{2m+1},
\]
the full number of parameter triples, so the enumerator is exhaustive.

Applying the MacWilliams transform to this enumerator gives
\[
A_1^\perp=A_2^\perp=0
\]
and the displayed positive formula for \(A_3^\perp\). Hence the dual distance is exactly \(3\).

Finally,
\[
w_1-w_2=p^{m-1},
\qquad
w_2-w_3=p^{m-1},
\]
and \(w_4>w_1\), so \(w_3\) is the true minimum distance. Subtracting the Theorem III.5 printed expression from \(w_3\) yields
\[
p^{m-2}(p^m-p-2)>0.
\]

## Verification

`artifacts/verify.py` uses only the Python standard library.

It checks the frequency formulas and the minimum-distance correction for several primes and dimensions. It also reconstructs both defining-set codes directly over
\[
\mathbb F_{3^2}
\quad\text{and}\quad
\mathbb F_{5^2},
\]
verifies the affine defining-set bijection and the codeword parameter bijection coordinate by coordinate, and exhausts every parameter triple. The direct weight distributions agree exactly with the closed formula.

For the source's ternary examples, the verifier reproduces
\[
1+24z^{12}+112z^{15}+104z^{18}+2z^{24}
\]
for \(m=2\),
\[
1+234z^{144}+988z^{153}+962z^{162}+2z^{234}
\]
for \(m=3\), and
\[
1+2160z^{1404}+8800z^{1431}+8720z^{1458}+2z^{2160}
\]
for \(m=4\).

The verifier also evaluates the MacWilliams transform through weight \(3\) and confirms the closed positive expression for
\[
A_3^\perp.
\]
Successful replay prints `VERIFY_OK`.

## Relationship to prior work

The primary article explicitly says in Remarks III.3 and III.6 that the weight distributions in these two cases are omitted because the relevant trace/discriminant counts are not easy to compute. The article nevertheless prints the four possible weights in the character-sum proof and gives ternary examples in Table III.

The affine equivalence between the two omitted cases is not stated there. It explains why the Table III examples for Theorems III.2 and III.5 have identical parameters and enumerators.

The source's own proof lists the weight
\[
p^{m-1}(p^m-p^{m-1}-2),
\]
while its Theorem III.5 parameter line prints a smaller minimum-distance expression. The closed enumerator resolves the inconsistency and identifies the correct distance.

Focused searches using the article identifier, both theorem numbers, the exact weight formulas, the affine defining-set equivalence, correction terminology, and projectivity did not locate a published correction or a prior statement of this common enumerator. Broader defining-set-code and character-sum literature supplies the standard counting tools but does not provide this source-specific equivalence and frequency computation.

## Limitations

The originality assessment is limited to the inspected public literature and indexed research records. A non-indexed author note may contain the same calculation.

The result closes the two omitted nondegenerate cases only. It does not revise the paper's other defining-set families.

The codes' projectivity is proved from their full weight enumerator via the MacWilliams transform; no stronger classification or uniqueness claim is made.

## References

1. Yue Huang, Zhonghao Liang, Chenlu Jia, Yongkang Wan, and Qunying Liao, *Four classes of few-weight self-orthogonal codes and their applications for LCD codes and quantum codes*, arXiv:2607.07181v1, first public version 8 July 2026.
2. F. J. MacWilliams and N. J. A. Sloane, *The Theory of Error-Correcting Codes*, North-Holland, 1977.
