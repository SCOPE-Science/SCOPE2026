# Sharp positivity threshold for the parity bias of partitions into squares

## Finding

Let \(E(n)\) (respectively \(O(n)\)) count partitions of \(n\) into positive squares with an even (respectively odd) number of parts; parts may repeat and the empty partition is allowed. For every integer \(n\ge0\), put \(A(n)=(-1)^n(E(n)-O(n))\). Then

\[
A(n)>0\quad\Longleftrightarrow\quad n\notin\{4,5,6,7,13,14,15,16,22,23,24,31,39,47,48,56,64\}.
\]

In particular the inequalities \(E(n)>O(n)\) for even \(n\) and \(O(n)>E(n)\) for odd \(n\) both hold for every \(n\ge65\), and the uniform cutoff \(65\) is optimal because \(A(64)=0\). This establishes the finite-threshold conjecture described in Remark 4 of Ciolan's *Asymptotics and inequalities for partitions into squares*.

## Assumptions and scope

All partitions are unrestricted except that every part is a positive perfect square. Counts include the unique empty partition of zero. The statement is for **every** integer \(n\ge0\); it makes no asymptotic or numerical-cutoff assumption. We use formal power series with integer coefficients, so analytic convergence is unnecessary.

## Proof

**1. Exact positivity interpretation.** For partitions into squares, weighting each part by its parity yields
\[
\sum_{n\ge0}(E(n)-O(n))q^n=\prod_{j\ge1}\frac{1}{1+q^{j^2}}.
\]
Replacing \(q\) by \(-q\), and using \(1/(1+x)=(1-x)/(1-x^2)\), gives the exact formal-series factorization
\[
\begin{aligned}
\sum_{n\ge0}A(n)q^n
&=\prod_{j\ge1}\frac{1}{1+(-q)^{j^2}}\\
&=\left(\prod_{j\ge1\atop j\ \mathrm{odd}}(1+q^{j^2})\right)
\left(\prod_{m\ge1}(1+q^{2m^2})\right).
\end{aligned}
\]
For completeness, the second equality follows by splitting \(j\) into odd and even, writing \(1/(1-q^{j^2})=(1+q^{j^2})/(1-q^{2j^2})\) for odd \(j\), and collecting the even-numerator factors \(1-q^{(2m)^2}\): their ratio to \(\prod_{m\ge1}(1-q^{2m^2})\) equals \(\prod_{m\ge1}(1+q^{2m^2})\). Thus \(A(n)\) counts subsets of the **distinct** numbers
\[
\mathcal B=\{j^2:j\ge1\text{ odd}\}\cup\{2m^2:m\ge1\}
\]
whose sum is \(n\). The two displayed sets are disjoint (their elements have opposite parity). Therefore \(A(n)\ge0\), and strict positivity is equivalent to subset-sum representability.

**2. Complete finite base certificate.** Consider these ten elements of \(\mathcal B\):
\[
\mathcal B_6=\{1,2,8,9,18,25,32,49,50,72\},\qquad T_6=\sum_{b\in\mathcal B_6}b=266.
\]
Exact enumeration of the \(2^{10}=1024\) subsets (and independent coefficient accumulation for \(\prod_{b\in\mathcal B_6}(1+q^b)\)) proves that its support comprises \(233\) integers, including **every** integer in \([65,201]\). It also proves that the missing integers in \([0,64]\) are exactly
\[
\{4,5,6,7,13,14,15,16,22,23,24,31,39,47,48,56,64\}.
\]
This finite certificate is reproduced in `verify.py` through transparent, exhaustive integer arithmetic. No element of \(\mathcal B\setminus\mathcal B_6\) is \(\le64\), so those missing integers are also precisely the true zeros of \(A(n)\) in \([0,64]\).

**3. Infinite interval propagation.** For integer \(m\ge7\), let
\[
\mathcal B_m=\mathcal B_6\cup\{2j^2:7\le j\le m\},\qquad T_m=266+\sum_{j=7}^{m}2j^2.
\]
We inductively establish that **every** integer in the interval \([65,T_m-65]\) is a subset sum of \(\mathcal B_m\). This holds for \(m=6\) by step 2, since \(T_6-65=201\). If it holds for \(m-1\), then by either omitting or including the new element \(b_m=2m^2\), all integers in
\[
[65,T_{m-1}-65]\ \cup\ [65+2m^2,T_m-65]
\]
are represented. The two integer intervals meet or are adjacent when
\[
2m^2\le T_{m-1}-129.
\]
For \(m=7\), the right side is \(266-129=137\) whereas \(2m^2=98\), leaving margin \(39\). Defining \(\Delta_m=T_{m-1}-129-2m^2\), we have for every \(m\ge7\)
\[
\Delta_{m+1}-\Delta_m=2m^2-4m-2>0.
\]
Hence the needed overlap holds at every induction step. Since \(T_m\to\infty\), the represented intervals exhaust every integer \(n\ge65\). Together with step 2 and the exact generating function, this proves both directions and sharpness. \(\square\)

## Verification

Run `python3 verify.py` in the same directory as this file; no third-party modules or data are needed. It checks all \(1024\) base subsets, the \(233\) distinct sums, the complete interval \([65,201]\), the precise seventeen missing values below \(65\), and a second polynomial-coefficient certificate. It independently compares the formal signed-partition generating series with the positive subset generating series through degree \(500\) and checks \(494\) finite instances of the symbolic induction inequality. These checks validate finite premises; the argument in Proof §3 is the infinite proof.

## Relationship to prior work

Ciolan, *Asymptotics and inequalities for partitions into squares* (arXiv:1806.00708, first posted 2018; Remark 4 of the publicly available 2019 revision) proved the parity inequalities for sufficiently large \(n\) and conjectured that they already hold for all \(n\ge65\), after numerical tests through \(50{,}000\). Ciolan, *Equidistribution and inequalities for partitions into powers* (arXiv:2002.05682, posted 2020), provided a broad nonnegativity identity implying \(A(n)\ge0\) but did not establish the exact positivity threshold. The formal product identity and nonnegativity are **prior results**; the new assertion here is the proved optimal finite-to-infinite subset-sum covering threshold and complete equality classification.

## Limitations

This theorem treats positive squares, not other powers or arbitrary sets of parts. The originality comparison is limited to the accessible identified literature; an unindexed equivalent proof may exist. Finite verification supplements rather than replaces the symbolic induction.

## References

1. A. Ciolan, *Asymptotics and inequalities for partitions into squares*, arXiv:1806.00708 (initial public submission 2018-06-02; revised 2019-10-01), Theorem 1 and Remark 4, https://arxiv.org/pdf/1806.00708.
2. A. Ciolan, *Equidistribution and inequalities for partitions into powers*, arXiv:2002.05682 (initial public submission 2020-02-13), §§2–3 and Theorem 3, https://arxiv.org/pdf/2002.05682.
