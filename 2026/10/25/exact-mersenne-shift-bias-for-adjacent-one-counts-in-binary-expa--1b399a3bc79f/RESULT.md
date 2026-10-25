# Exact Mersenne-shift bias for adjacent-one counts in binary expansions

## Finding

For each nonnegative integer \(n\), let
\[
r(n)=\#\{j\ge0:\text{binary digits }j\text{ and }j+1\text{ of }n\text{ both equal }1\}.
\]
Overlapping occurrences are counted, and leading zeroes do not affect \(r\). For every integer \(k\ge1\), put \(t_k=2^k-1\) and define the natural density
\[
P_k=\lim_{X\to\infty}\frac1X\#\{0\le n<X:r(n+t_k)\ge r(n)\}.
\]
The limit exists, and its exact values are
\[
\boxed{P_1=\frac{13}{16},\quad P_2=\frac{47}{64},\quad P_3=\frac{87}{128},\quad
P_k=\frac{83}{128}\quad(k\ge4).}
\]
In particular, the inequality \(r(n+2^k-1)\ge r(n)\) has natural density at least \(83/128>1/2\), uniformly for every \(k\ge1\). Although the shifts have unbounded binary length, they have exactly one maximal run of ones. The constant value for all \(k\ge4\) is an exact, not asymptotic, stabilization.

## Assumptions and scope

The variable \(k\) ranges over positive integers. The variable \(n\) ranges over nonnegative integers; adding leading zeroes does not create adjacent-one pairs. Natural density is taken over initial intervals of the nonnegative integers. The theorem does not claim the corresponding inequality for every individual \(n\), nor for shifts other than \(2^k-1\). The primary classification is MSC2020 11A63.

## Proof

**1. Increment distribution.** Put \(\Delta(q)=r(q+1)-r(q)\). For even \(q\), adding one flips only its units bit, so \(\Delta(q)\) equals binary digit \(1\) of \(q\). Thus, conditioned on even \(q\), \(\Delta\) equals \(0\) and \(1\) with density \(1/2\) each.

For odd \(q\), let \(\ell\ge1\) be the number of trailing ones. Addition changes those \(\ell\) ones to zeroes and changes the next zero to one. The \(\ell-1\) adjacent-one pairs inside the trailing run disappear, while a pair is created if the digit at position \(\ell+1\) is one. Consequently
\[
\Delta(q)=\operatorname{bit}_{\ell+1}(q)-(\ell-1).
\]
Among odd integers, the event of exactly \(\ell\) trailing ones has conditional density \(2^{-\ell}\), and the indicated higher digit is independently fair. Hence, conditioned on odd \(q\),
\[
\Pr(\Delta=1)=\tfrac14,\qquad
\Pr(\Delta=d)=3\cdot2^{d-3}\quad(d\le0).
\]
It follows that, for integer \(x\), the conditional survival functions are
\[
G_e(x)=\Pr(\Delta+x\ge0\mid q\text{ even})=
\begin{cases}1&x\ge0,\\ 1/2&x=-1,\\0&x\le-2,\end{cases}
\]
\[
G_o(x)=\Pr(\Delta+x\ge0\mid q\text{ odd})=
\begin{cases}1-3/2^{x+3}&x\ge-1,\\0&x\le-2.\end{cases}
\]
The distributions exist as natural densities: truncating the trailing run at length \(L\) gives a finite union of binary residue classes, and the omitted conditional proportion is \(2^{-L}\).

**2. Decomposition at the binary boundary.** Write \(n=2^kq+a\), with \(0\le a<2^k\). If \(a=0\), then
\[
r(n+t_k)-r(n)=k-1+(q\bmod2)\ge0.
\]
If \(a>0\), the relation \(n+t_k=2^k(q+1)+(a-1)\) gives the exact concatenation identity
\[
\begin{split}
r(n+t_k)-r(n)={}&\Delta(q)+r(a-1)-r(a)\\
&+((q+1)\bmod2)\operatorname{bit}_{k-1}(a-1)\\
&-(q\bmod2)\operatorname{bit}_{k-1}(a).
\end{split}
\]
Here \(\operatorname{bit}_j(a)\in\{0,1\}\) is the \(j\)-th binary digit. Set \(d(a)=r(a-1)-r(a)\), \(h(a)=\operatorname{bit}_{k-1}(a)\), and \(h'(a)=\operatorname{bit}_{k-1}(a-1)\). The favorable probability averaged over the high block \(q\) and its parity is therefore
\[
F_k(a)=G_e(d(a)+h'(a))+G_o(d(a)-h(a)),\qquad 1\le a<2^k.
\]
Each residue \(a\) has asymptotic frequency \(2^{-k}\), and both parities of \(q\) occur equally often. Thus the density exists and
\[
P_k=2^{-(k+1)}T_k,\qquad T_k=2+\sum_{a=1}^{2^k-1}F_k(a).
\tag{1}
\]
The initial \(2\) records the two favorable parities for \(a=0\).

**3. Binary carry classes.** For \(a\ge1\), put \(j=\nu_2(a)\). A direct examination of the changed low bits in the subtraction of one gives
\[
d(a)=\begin{cases}
-\operatorname{bit}_1(a),&j=0,\\
j-1-\operatorname{bit}_{j+1}(a),&j\ge1.
\end{cases}
\tag{2}
\]
Digits outside the prescribed \(k\)-bit word are zero.

Suppose \(k\ge4\). If \(0\le j\le k-3\), let \(b=\operatorname{bit}_{j+1}(a)\) and \(h=\operatorname{bit}_{k-1}(a)\). The digits \(b,h\) are independent choices. Each of their four pairs occurs for exactly \(2^{k-j-3}\) integers \(a\) with \(\nu_2(a)=j\). Moreover, \(h'(a)=h\). Defining \(d_j(b)=-b\) for \(j=0\) and \(d_j(b)=j-1-b\) otherwise, the sum of the four associated weights is
\[
W_j=\sum_{b,h\in\{0,1\}}
\bigl(G_e(d_j(b)+h)+G_o(d_j(b)-h)\bigr).
\]
Substitution of the explicitly proved survival functions yields
\[
W_0=W_1=\frac{37}{8},\qquad
W_j=8-\frac{27}{2^{j+2}}\quad(j\ge2).
\tag{3}
\]
For \(j=0,1\), the individual four weights, ordered by \((b,h)=(0,0),(0,1),(1,0),(1,1)\), are \(13/8,5/4,3/4,1\). For \(j\ge2\), all four arguments to \(G_e\) are nonnegative, all four arguments to \(G_o\) are at least \(-1\), and \(\sum_{b,h}2^{b+h}=9\); this proves the second formula in (3) without any omitted boundary cases.

There are two remaining valuation classes. For \(j=k-2\), the possible low words have \(b=h\); their weights add to
\[
U_k=4-\frac{15}{2^k}.
\]
For \(j=k-1\), the sole integer is \(a=2^{k-1}\); here \(h'=0\), \(h=1\), and \(d(a)=k-2\). Its weight is
\[
V_k=2-\frac{3}{2^k}.
\]
Consequently, by (1) and (3),
\[
\begin{split}
T_k&=2+\sum_{j=0}^{k-3}2^{k-j-3}W_j+U_k+V_k\\
&=8-\frac{18}{2^k}+\sum_{j=0}^{k-3}2^{k-j-3}W_j.
\end{split}
\tag{4}
\]
Using the two geometric sums for \(j\ge2\) gives, for every \(k\ge4\),
\[
\sum_{j=0}^{k-3}2^{k-j-3}W_j
=83\cdot2^{k-6}-8+\frac{18}{2^k}.
\]
This identity remains valid at \(k=4\), when the \(j\ge2\) sum is empty. Therefore \(T_k=83\cdot2^{k-6}\), and (1) yields \(P_k=83/128\).

**4. Short shifts.** Direct substitution into the finite exact formula (1), which is valid for every \(k\ge1\), gives
\[
(T_1,T_2,T_3)=(13/4,47/8,87/8).
\]
Dividing by \(2^{k+1}\) proves the three stated initial densities. This completes the proof. \(\square\)

## Verification

The standalone `VERIFY.py` implements the exact survival functions using rational arithmetic. It checks the increment identity for each \(q\) below \(2^{16}\), the exact finite-residue formula for all \(1\le k\le13\), the bulk-weight formulas for \(0\le j<20\), the two boundary identities for \(4\le k<20\), and the finite geometric-sum simplification for those same \(k\). An independent direct integer enumeration checks the sign comparison for shifts \(2^k-1\), \(1\le k\le6\). The direct enumeration is finite evidence only; the uniform infinite assertion is proved by (1)–(4). Run with `python3 VERIFY.py` in the directory containing this file.

## Relationship to prior work

Sobolewski and Spiegelhofer (arXiv:2309.00142, submitted 31 August 2023) establish the difference distributions for adjacent-one counts and ask whether \(\Pr(r(n+t)\ge r(n))>1/2\) for every fixed nonnegative \(t\). Their Proposition 3.2 gives recurrences permitting computation at individual shifts, and their Theorem 2.1 concerns shifts with many runs of ones. These established recurrences are consistent with the formula above, but do not explicitly give a uniform closed value for the infinite one-run family \(t=2^k-1\).

Sobolewski (arXiv:2412.15851, 20 December 2024) extends approximate Gaussian laws to arbitrary binary blocks; the one-run family does not fall into its many-run asymptotic regime. Sobolewski (arXiv:2204.05287, 11 April 2022) determines monochromatic arithmetic-progressions properties for the Rudin–Shapiro parity sequence at differences \(2^k-1\); its object is a mod-two progression property, not the sign of the full integer-valued adjacent-one count difference under addition. The exact stabilizing density here is a distinct explicit infinite-family evaluation. The general distribution recurrences present a residual implication/priority risk; publication priority is not claimed.

## Limitations

The method supplies the nondecrease density only for Mersenne shifts, not arbitrary shifts. It does not determine the complete distribution of \(r(n+2^k-1)-r(n)\) or prove the full adjacent-one analogue of Cusick's conjecture. The originality comparison cannot exclude unindexed earlier specializations of known distribution recurrences. Independent mathematical review has not been performed.

## References

1. B. Sobolewski and L. Spiegelhofer, *Block occurrences in the binary expansion*, arXiv:2309.00142 (first submitted 2023-08-31), https://arxiv.org/html/2309.00142v1 .
2. B. Sobolewski, *On the behavior of binary block-counting functions under addition*, arXiv:2412.15851 (first submitted 2024-12-20), https://arxiv.org/abs/2412.15851 .
3. B. Sobolewski, *On monochromatic arithmetic progressions in binary words associated with pattern sequences*, arXiv:2204.05287 (first submitted 2022-04-11), https://arxiv.org/abs/2204.05287 .
4. OEIS Foundation, *A014081: Number of occurrences of 11 in the binary expansion*, https://oeis.org/A014081 .
