# Exact second-diagonal greedy 2-sumfree sequences

## Statement

Let \(f\ge 4\). Start the strict greedy \(2\)-sumfree sequence with
\[
S_{f,3f}=(s_0,s_1,\ldots),\qquad s_0=f,\quad s_1=3f,
\]
and thereafter choose the least integer larger than the preceding term that is not the sum of two **distinct** earlier terms.

Put
\[
M=9f-1
\]
and
\[
R_f=\{f,f+1\}\cup[3f,4f-2]\cup[5f+1,6f-1]\cup\{8f-2,8f-1\}
\subset \{0,1,\ldots,M-1\}.
\]

Then
\[
\boxed{
S_{f,3f}
=
\{4f-1,5f\}
\cup
\left(
\{n\ge1:n\bmod M\in R_f\}\setminus\{f+1\}
\right).
}
\]

Consequently, if \(D_{f,3f}=(s_i-s_{i-1})_{i\ge1}\), then
\[
\boxed{
D_{f,3f}
=
\left(
2f,\;1^{f-1},\;f+1,\;1,\;
\overline{
1^{f-2},\,2f-1,\,1,\,2f,\,1,\,2f-1,\,1^{f-2},\,f+3
}
\right).
}
\]
The bar denotes infinite repetition. The displayed preperiod and period are minimal. Hence
\[
\boxed{\text{preperiod length}=f+2,\qquad
\text{period length}=2f+2,}
\]
and the characteristic sequence has eventual translation modulus \(9f-1\).

This proves the period conjecture and the corresponding preperiod prediction of van Berkel--Bosma on the entire ray \(d=g-f=2f\), i.e. \(g=3f\), for every \(f\ge4\). The limiting density is
\[
\frac{2f+2}{9f-1}.
\]

## Context

Van Berkel and Bosma define strict greedy \(2\)-sumfree sequences \(S_{f,g}\) and conjecture explicit minimal period and preperiod lengths for all starting pairs. Their current general theorems cover a large region including \(g\le2f\), while the paper supplies finite computational certification farther out. For \(d=2f\), their period formula predicts \(2f+2\); for \(f\ge5\), their preperiod formula gives \(f+2\). The result above proves this infinite second-diagonal family and also gives the complete residue description.

The terminology overlaps the older literature on \(0\)-additive or non-additive sequences.

## Proof

Let \(T_f\) denote the set on the right-hand side of the boxed set formula. We prove two facts:

1. no element of \(T_f\) is a sum of two distinct elements of \(T_f\);
2. every integer \(x>3f\) outside \(T_f\) is a sum of two distinct earlier elements of \(T_f\).

These two facts force the greedy sequence initialized by \(f,3f\) to be exactly \(T_f\).

### 1. The periodic residue set is sum-free

Write
\[
A=\{f,f+1\},\quad
B=[3f,4f-2],\quad
C=[5f+1,6f-1],\quad
D=\{8f-2,8f-1\},
\]
so \(R_f=A\cup B\cup C\cup D\).

Modulo \(M=9f-1\), the possible sums of pairs of residue blocks lie in the following sets:
\[
\begin{array}{c|c}
\text{pair}&\text{sum residues}\\ \hline
A+A &[2f,2f+2]\\
A+B &[4f,5f-1]\\
A+C &[6f+1,7f]\\
A+D &\{M-1,0,1\}\\
B+B &[6f,8f-4]\\
B+C &[8f+1,M-1]\cup[0,f-2]\\
B+D &[2f-1,3f-2]\\
C+C &[f+3,3f-1]\\
C+D &[4f,5f-1]\\
D+D &[7f-3,7f-1].
\end{array}
\]
For \(f\ge4\), every set in the right column is disjoint from \(R_f\). Thus a sum of two periodically occurring elements never lands in a periodic residue class of \(T_f\).

There are two exceptional elements,
\[
e_1=4f-1,\qquad e_2=5f.
\]
Their sums with the four residue blocks have residues
\[
\begin{array}{c|cccc}
 &A&B&C&D\\ \hline
e_1+(\cdot)&[5f-1,5f]&[7f-1,8f-3]&[1,f-1]&\{3f-2,3f-1\}\\
e_2+(\cdot)&[6f,6f+1]&[8f,9f-2]&[f+2,2f]&\{4f-1,4f\}.
\end{array}
\]
Again none belongs to \(R_f\), and \(e_1+e_2=M\equiv0\pmod M\).

It remains only to rule out a pair sum equal to one of the exceptional values themselves. Below \(e_1=4f-1\), the available elements are \(f\) and the initial part beginning at \(3f\), so no distinct pair sums to \(e_1\). Below \(e_2=5f\), the same observation and the inequality \(f+(4f-1)=5f-1\) exclude \(e_2\). Therefore \(T_f\) is strict \(2\)-sumfree.

### 2. Every excluded integer is saturated

First consider
\[
3f<x<M.
\]
Within this range, the elements of \(T_f\) are
\[
\{f\}\cup[3f,4f-1]\cup[5f,6f-1]\cup\{8f-2,8f-1\}.
\]
The missing intervals are represented as follows:
\[
\begin{aligned}
4f\le x\le5f-1 &: \quad x=f+(x-f),\\
x=6f &: \quad x=f+5f,\\
6f+1\le x\le8f-3 &: \quad
x\in [3f,4f-1]\mathbin{\widehat{+}}[3f,4f-1],\\
8f\le x\le9f-2 &: \quad
x\in[3f,4f-1]+[5f,6f-1].
\end{aligned}
\]
Here \(\widehat{+}\) denotes sums of distinct elements. The restricted sumset of the interval \([3f,4f-1]\) is exactly \([6f+1,8f-3]\).

Now let \(x\ge M\), and write
\[
x=qM+r,\qquad q\ge1,\quad 0\le r<M.
\]
The complement of \(R_f\) consists of
\[
\{0\},\ [1,f-1],\ [f+2,3f-1],\
[4f-1,5f],\ [6f,8f-3],\ [8f,9f-2].
\]
For each excluded residue \(r\), the following table gives a strict pair representation either of \(r\) or of \(M+r\):
\[
\begin{array}{c|c}
r&\text{base representation}\\ \hline
0&M=f+(8f-1)\\
1\le r\le f-1&M+r=(4f-1)+(5f+r)\\
f+2\le r\le2f&M+r=5f+(4f-1+r)\\
2f+1\le r\le3f-2&M+r=(f+1+r)+(8f-2)\\
r=3f-1&M+r=(4f-1)+(8f-1)\\
r=4f-1&M+r=5f+(8f-2)\\
4f\le r\le5f-1&r=f+(r-f)\\
r=5f&r=(4f-1)+(f+1)\\
r=6f&r=5f+f\\
6f+1\le r\le7f-1&r=f+(r-f)\\
r=7f&r=(f+1)+(6f-1)\\
7f+1\le r\le8f-3&r=(4f-1)+(r-(4f-1))\\
8f\le r\le9f-2&r=5f+(r-5f).
\end{array}
\]

In a row representing \(M+r\), translate a periodically occurring summand by \((q-1)M\). In a row representing \(r\), translate a periodically occurring summand by \(qM\). This yields two distinct elements of \(T_f\), both smaller than \(x\), whose sum is \(x\). The only rows using the missing initial value \(f+1\) are base-\(r\) rows; after translation by \(qM\) with \(q\ge1\), that residue-class element does belong to \(T_f\).

Thus every excluded integer after the prescribed second seed is forbidden by an earlier strict pair sum. Since every element of \(T_f\) is admissible, induction on the greedy construction proves \(S_{f,3f}=T_f\).

### 3. Exact minimal preperiod and period

Reading the ordered set \(T_f\) gives
\[
D_{f,3f}
=
\left(
2f,\;1^{f-1},\;f+1,\;1,\;\overline{P_f}
\right),
\]
where
\[
P_f=
\left(
1^{f-2},\,2f-1,\,1,\,2f,\,1,\,2f-1,\,1^{f-2},\,f+3
\right).
\]
The block has
\[
|P_f|=2f+2,\qquad \sum P_f=9f-1=M.
\]
For \(f\ge4\), the entry \(2f\) occurs exactly once in \(P_f\). Hence \(P_f\) is not a proper power, so its period length \(2f+2\) is minimal. Extending the periodic block one place backward would require the preceding difference to be \(f+3\), whereas the actual preceding difference is \(1\). Therefore the preperiod length \(f+2\) is also minimal.

## Example

For \(f=4\), \(M=35\), and
\[
R_4=\{4,5\}\cup[12,14]\cup[21,23]\cup\{30,31\}.
\]
The sequence begins
\[
4,12,13,14,15,20,21,22,23,30,31,39,40,47,48,49,56,57,58,\ldots
\]
and
\[
D_{4,12}
=
(8,1,1,1,5,1,\overline{1,1,7,1,8,1,7,1,1,7}).
\]

## Reproducibility

`artifacts/verify.py` separately implements the greedy rule and the claimed residue formula. It checks the exact formula for \(f=4,\ldots,80\) over 700 generated terms per case, checks the modular sum-free certificate and saturation-witness table for \(f=4,\ldots,200\), and verifies the displayed difference word. `artifacts/verify-output.txt` records the resulting output.

The computation is supporting evidence only; the theorem is proved above for every \(f\ge4\).

## Literature and limitations

The main comparison source is D. van Berkel and W. Bosma, *Periodicity conjectures for all 2-sumfree sequences*, arXiv:2609.18522v1 (16 September 2026). Its conjectures prescribe period and preperiod lengths for all starting pairs, while its proved infinite families do not include the ray \(g=3f\); it also reports extensive finite certification. Their preceding paper, *On \(t\)-sumfree sequences*, arXiv:2609.16843v1 (15 September 2026), proves a broad region closer to the diagonal.

The older \(0\)-additive literature includes Raymond Queneau, *Sur les suites s-additives*, Journal of Combinatorial Theory, Series A 12 (1972), 31--71, DOI 10.1016/0097-3165(72)90083-0, and Steven R. Finch, *Are 0-Additive Sequences Always Regular?*, American Mathematical Monthly 99 (1992), 671--673, DOI 10.1080/00029890.1992.11995911. Their full texts were not independently inspected here. They are the most plausible residual originality risk because they contain extensive work on \(0\)-additive sequences. Exact and synonymous searches for the family \(S_{f,3f}\), modulus \(9f-1\), period \(2f+2\), and corresponding \(0\)-additive/non-additive terminology did not locate this theorem. The 2026 van Berkel--Bosma paper, which surveys the older line and still presents these values beyond the proved range as conjectural/computational, is additional evidence against prior coverage. Originality is therefore asserted only to the best of our knowledge.

## References

1. D. van Berkel and W. Bosma, *Periodicity conjectures for all 2-sumfree sequences*, arXiv:2609.18522v1, 2026. https://arxiv.org/abs/2609.18522
2. D. van Berkel and W. Bosma, *On t-sumfree sequences*, arXiv:2609.16843v1, 2026. https://arxiv.org/abs/2609.16843
3. R. Queneau, *Sur les suites s-additives*, J. Combin. Theory Ser. A 12 (1972), 31--71. DOI: 10.1016/0097-3165(72)90083-0.
4. S. R. Finch, *Are 0-Additive Sequences Always Regular?*, Amer. Math. Monthly 99 (1992), 671--673. DOI: 10.1080/00029890.1992.11995911.
