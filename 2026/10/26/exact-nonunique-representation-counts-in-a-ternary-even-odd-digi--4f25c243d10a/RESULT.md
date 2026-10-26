# Exact nonunique-representation counts in a ternary even–odd digit basis

## Finding
Let \(W_0=\{0,2,4,\ldots\}\), \(W_1=\{1,3,5,\ldots\}\), and let \(A=A_3(W_0)\cup A_3(W_1)\), where \(A_3(W)\) consists of positive integers whose base-three nonzero digits occur only at positions in \(W\). For \(n\ge0\), let
\[
R(n)=\#\{(a,b):a,b\in A,\ a\le b,\ a+b=n\}.
\]
For **every integer** \(k\ge1\), the exact number of integers with at least two representations below the natural two-digit-block cutoff is
\[
\boxed{\#\{0\le n<9^k:R(n)\ge2\}=8\cdot5^{k-1}-2^{2k-1}-5k.}
\]
Moreover \(R(n)=0\) holds exactly for \(n=0,1\); hence
\[
\#\{0\le n<9^k:R(n)=1\}=9^k-8\cdot5^{k-1}+2^{2k-1}+5k-2.
\]
In particular the nonunique-representation count is asymptotic to \((8/5)5^k\), giving the **sharp exceptional exponent** \(\log_9 5\) along \(x=9^k\), rather than only a zero-density assertion.

## Assumptions and scope
Digits are indexed from zero. The two parts of \(W_0\sqcup W_1=\mathbb Z_{\ge0}\) are both infinite; a basis element is strictly positive, and repeated summands are permitted but counted once as an unordered pair. All integers \(k\ge1\) are included without limiting the number of digits in a summand, since \(a+b<9^k\) forces both below \(9^k\). The exact count concerns this specified ternary periodic partition, not arbitrary partitions or all bases.

## Proof
**1. Exact pointwise representation formula.** Put \(B=A_3(W_0)\). In base nine, its elements have digits in \(\{0,1,2\}\), while \(A_3(W_1)=3B\). Every unordered two-summand representation falls into one of three disjoint types: two in \(B\), two in \(3B\), or one in each. The mixed representation is unique when it exists: writing each base-nine digit as \(t=u+3v\), \(0\le u,v\le2\), gives unique components \(b\in B\cup\{0\}\) and \(3c\in3B\cup\{0\}\). Thus the indicator \(M(n)\) for a **positive mixed** representation equals one precisely when some base-nine digit of \(n\) has nonzero residue modulo three and some base-nine digit is at least three.

Let \(C(n)\) count unordered positive pairs from \(B\) summing to \(n\), and put \(C(0)=0\). If a base-nine digit of positive \(n\) exceeds four then \(C(n)=0\). Otherwise, for base-nine digits \(t_0,t_1,\ldots\in\{0,1,2,3,4\}\), set
\[
P(n)=\prod_j r(t_j),\qquad(r(0),r(1),r(2),r(3),r(4))=(1,2,3,2,1).
\]
There is no carry between base-nine positions in a sum of two elements of \(B\): each digit sum is at most four. The product \(P(n)\) counts ordered pairs allowing zero. Removing the two zero-summand representations if \(n\in B\), and then reinstating the diagonal contribution if each digit \(t_j\) is even, gives the exact identity
\[
C(n)=\tfrac12\bigl(P(n)-2\mathbf1_{n\in B}+\mathbf1_{\forall j,\ 2\mid t_j}\bigr)\quad(n>0).
\]
Consequently, with \(C(n/3)=0\) when \(3\nmid n\),
\[
\boxed{R(n)=C(n)+\mathbf1_{3\mid n}C(n/3)+M(n).}
\]
This identity also establishes \(R(n)\ge1\) for every \(n\ge2\): mixed-support numbers have \(M(n)=1\); a pure \(B\)-number has either a two-element split in \(B\) or is a single unit \(9^j\), which for \(j\ge1\) equals \(3\cdot9^{j-1}+6\cdot9^{j-1}\); similarly a pure \(3B\)-number has a split or is \(3\cdot9^j\), which equals \(9^j+2\cdot9^j\). The exceptional \(n=1\) has no split, nor does zero.

**2. Counting ambiguous numbers with both digit colors present.** Restrict to \(0\le n<9^k\), and let \(M\) denote the set of numbers with the mixed-support property. Let \(E\) consist of numbers with every base-nine digit at most four, and let \(O\) consist of \(n=3u<9^k\) whose base-nine digits in \(u\) are at most four. On \(M\), the pointwise formula shows that \(R(n)\ge2\) exactly when \(n\in E\cup O\).

The following counts are exact:
\[
\begin{aligned}
|M\cap E|&=5^k-3^k-2^k+1,\\
|M\cap O|&=3\cdot5^{k-1}-3^k-2^{k-1}+1,\\
|M\cap E\cap O|&=2^{2k-1}-2^k-2^{k-1}+1.
\end{aligned}
\]
For the first, there are \(5^k\) digit strings in \(E\), while pure even support contributes \(3^k\) and pure odd support contributes \(2^k\), with their common zero counted twice. For the second, \(n=3u<9^k\) forces the highest of the \(k\) base-nine digits of \(u\) to be at most two: there are \(3\cdot5^{k-1}\) choices; the pure odd and even subclasses contribute \(3^k\) and \(2^{k-1}\), respectively, again meeting only at zero.

For the intersection, multiply \(u\) by three in base nine with a carry state \(c\in\{0,1\}\). Regardless of the incoming carry, exactly two permitted digits \(u_j\in\{0,1,2,3,4\}\) yield an output digit at most four with outgoing carry zero, and two yield an output digit at most four with outgoing carry one. Starting and ending with carry zero therefore gives \(|E\cap O|=2^{2k-1}\) for \(k\ge1\). Its pure even and pure odd subclasses have sizes \(2^{k-1}\) and \(2^k\). Inclusion–exclusion yields
\[
\#\{n\in M:R(n)\ge2\}=8\cdot5^{k-1}-2\cdot3^k-2^{2k-1}+1.
\]

**3. Counting ambiguous pure-support numbers.** Every pure even-support number below \(9^k\) has all digits in \(\{0,1,2\}\), hence belongs to a set of size \(3^k\). By the pointwise formula, those with at most one representation are **exactly** zero, the \(k\) integers \(9^j\), the \(k\) integers \(2\cdot9^j\), and the \(k-1\) integers \(1+9^j\) for \(1\le j<k\). These are \(3k\) distinct integers; thus the pure even contribution is \(3^k-3k\). To check completeness, an element with any digit two and any second nonzero digit has at least two positive same-even splits, while a binary-digit element with at least three nonzero digits has multiple splits. The remaining two-unit cases have one same-even split; if neither position is zero, the carry split in \(3B\) provides a second representation.

A pure odd-support number is \(3u\) with \(u\) having \(k\) base-nine digits in \(\{0,1,2\}\), giving \(3^k\) choices including zero. Here the only elements with at most one representation are zero, \(3\cdot9^j\) and \(6\cdot9^j\) for \(0\le j<k\): there are \(2k+1\) of them. Indeed, if \(u\) has a digit two and a further nonzero digit, there are multiple two-summand splits in \(3B\); if \(u\) has \(t\ge2\) digits equal to one and no digit two, then the same-odd and same-even representation counts are \(2^{t-1}-1\) and \(2^{t-1}\), so their sum is \(2^t-1\ge3\). Thus the pure odd contribution is \(3^k-2k-1\).

The mixed, pure even, and pure odd sets are disjoint except for zero, which is not ambiguous. Adding the three counts gives
\[
(8\cdot5^{k-1}-2\cdot3^k-2^{2k-1}+1)+(3^k-3k)+(3^k-2k-1)
=8\cdot5^{k-1}-2^{2k-1}-5k,
\]
as claimed. The uniqueness and asymptotic conclusions follow immediately.

## Verification
The standard-library script `verify.py` constructs the positive basis elements below \(9^k\), counts all unordered sums, and compares the resulting full representation function to the digit formula for \(1\le k\le4\). It separately checks the exact exceptional count obtained by the digit formula for \(k=5,6\). The attached `verification-output.txt` records the completed checks, including `CERTIFICATE_OK`. Finite verification corroborates, but is not the proof of, the universal statement.

## Relationship to prior work
Tang's *Minimal asymptotic \(g\)-adic bases from arbitrary partitions* (arXiv:2610.23152v1, 2026-10-16), Theorem 1.1 and Corollary 1.3, proves minimality for all \(g>h\) and density-one uniqueness. Here \(g=3\), \(h=2\), and the partition by parity gives the simplest periodic instance. The new invariant is the exact number of **nonunique** representations at each full two-digit-block cutoff, including its sharp growth exponent; a density-one uniqueness theorem does not determine this count. Tang and Ling's earlier work (arXiv:1810.10925v1) establishes existence/nonminimality criteria for digit-partition bases, not a representation-multiplicity census. The proof uses the special carry structure of base-nine blocks, so it does not claim a general theorem for arbitrary partitions.

## Limitations
The exact enumeration covers the specified ternary residue-class partition, not a general value of \(g\), a general number of summands, or arbitrary exponent partitions. The asymptotic exponent is established on the natural geometric subsequence \(x=9^k\); no full continuous-scale asymptotic with a fixed prefactor is claimed. This is an original-analysis claim based on the sources inspected; an unindexed equivalent earlier count remains a residual originality risk. No independent mathematical audit has been performed.

## References
1. Min Tang, *Minimal asymptotic \(g\)-adic bases from arbitrary partitions*, arXiv:2610.23152v1, first posted October 16, 2026; Theorem 1.1, Corollary 1.3, Sections 1–4. https://arxiv.org/html/2610.23152v1
2. Min Tang and Deng-Rong Ling, *On asymptotic bases and minimal asymptotic bases*, arXiv:1810.10925v1, first posted October 25, 2018; introduction and Theorems 1–2. https://arxiv.org/abs/1810.10925
3. Melvyn B. Nathanson, *Minimal bases and powers of 2*, Acta Arithmetica 49 (1988), 525–532 (cited for the original alternating-digit minimal-basis construction in Reference 1).
