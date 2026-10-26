# Sparse-support large deviations for odd binary partitions and sharp semi-Pell growth

## Finding

For a positive **odd** integer \(n\), let \(\mathcal B(n)\) be the set of partitions of \(n\) into powers of two in which every occupied power occurs with a positive odd multiplicity. Write \(J(\lambda)\) for the number of occupied powers in \(\lambda\), \(b(n)=|\mathcal B(n)|\), and \(p(n)=\frac12\sum_{\lambda\in\mathcal B(n)}2^{J(\lambda)}\). The established partition correspondences identify \(b(n)=\operatorname{sf}(n)\) and \(p(n)=\operatorname{sp}(n)\), the semi-Fibonacci and semi-Pell sequences, respectively.

Put \(k=\lfloor\log_2 n\rfloor\). For each fixed real \(0<\varepsilon<1\), let \(t=\lfloor(1-\varepsilon)k\rfloor\) and let \(b_{\le t}(n)\) count the partitions with \(J(\lambda)\le t\). As \(n\to\infty\) through odd integers,

\[
\log_2 b_{\le t}(n)=\frac{1-\varepsilon^2}{2}k^2+O_{\varepsilon}(k\log(k+2)),\qquad
\log_2 b(n)=\frac12 k^2+O(k\log(k+2)).
\]

In particular,

\[
\log_2\!\left(\frac{b_{\le t}(n)}{b(n)}\right)
=-\frac{\varepsilon^2}{2}k^2+O_{\varepsilon}(k\log(k+2)).
\]

Furthermore the odd-index semi-Pell and semi-Fibonacci sequences have an exact polynomial separation exponent:

\[
\boxed{\displaystyle\lim_{\substack{n\to\infty\\ n\ \mathrm{odd}}}
\frac{\log(\operatorname{sp}(n)/\operatorname{sf}(n))}{\log n}=1.}
\]

Equivalently, \(\operatorname{sp}(n)/\operatorname{sf}(n)=n^{1+o(1)}\) as odd \(n\to\infty\). The sharp support-deviation exponent \(\varepsilon^2/2\) describes a distributional phenomenon not implied by the leading growth of either unweighted sequence alone.

## Assumptions and scope

A partition is unordered. Each part has size \(2^j\) for an integer \(j\ge0\). For an occupied size \(2^j\), its multiplicity is \(2m_j+1\) for an integer \(m_j\ge0\); an unoccupied size has multiplicity zero. Every \(n\) in the theorem is positive and odd. The asymptotic constants in terms marked \(O_{\varepsilon}\) can depend on the fixed parameter \(\varepsilon\), but not on \(n\). The semi-Pell overpartition model allows overlining the first occurrence of each occupied part size, requires the largest occupied size to be overlined, and leaves the other occupied sizes independently optional. Therefore precisely \(2^{J(\lambda)-1}\) admissible overpartitions lie above any \(\lambda\in\mathcal B(n)\), giving the displayed formula for \(p(n)\).

## Proof

**1. Universal support upper bound.** For every \(n\ge1\) and \(k=\lfloor\log_2 n\rfloor\), any occupied exponent belongs to \(\{0,\ldots,k\}\). If a support \(S\) is fixed, its multiplicity parameters satisfy \(0\le m_j\le\lfloor n/2^{j+1}\rfloor\). Disregarding the sum constraint bounds the number of partitions with support \(S\) by

\[
\prod_{j\in S}\left(1+\left\lfloor\frac{n}{2^{j+1}}\right\rfloor\right)
\le\prod_{j\in S}2^{k-j+1}.
\]

For a support of size \(s\), this product is at most \(2^{s(k+1)-s(s-1)/2}\), maximized by selecting the \(s\) smallest exponents. There are at most \(2^{k+1}\) supports, and for \(0\le s\le t\le k+1\) this exponent is nondecreasing. Hence

\[
\log_2 b_{\le t}(n)
\le k+1+t(k+1)-\frac{t(t-1)}2
=tk-\frac{t^2}2+O(k).
\]

Taking \(t=k+1\) also yields \(\log_2 b(n)\le\frac12 k^2+O(k)\).

**2. Matching lower bound at a prescribed support size.** Choose an integer \(1\le s\le k\) such that \(2^s-1\le n/4\), and fix the support \(S=\{0,\ldots,s-1\}\). Put \(M=2^s-1\), its minimal odd-multiplicity contribution. For every \(1\le j\le s-1\), choose independently

\[
0\le m_j\le\left\lfloor\frac{n}{4s\,2^{j+1}}\right\rfloor.
\]

Then \(\sum_{j=1}^{s-1}2^{j+1}m_j\le n/4\). As \(n\) and \(M\) are odd, the integer

\[
m_0=\frac{n-M-\sum_{j=1}^{s-1}2^{j+1}m_j}{2}
\]

is nonnegative. It completes a unique partition of \(n\) with exactly \(s\) occupied part sizes. Thus, writing \(b_{=s}(n)\) for the number of partitions of support size exactly \(s\),

\[
 b_{=s}(n)\ge\prod_{j=1}^{s-1}\left(1+\left\lfloor\frac{n}{4s\,2^{j+1}}\right\rfloor\right)
 \ge\prod_{j=1}^{s-1}\frac{n}{4s\,2^{j+1}}.
\]

Since \(k\le\log_2 n<k+1\), taking logarithms gives

\[
\log_2 b_{=s}(n)\ge sk-\frac{s^2}{2}-O(k\log(k+2))
\]

uniformly for all such \(s\le k\). For a fixed \(\varepsilon\), use \(s=t=\lfloor(1-\varepsilon)k\rfloor\); for sufficiently large \(k\), \(2^t-1\le n/4\). The upper and lower bounds match at \(tk-t^2/2=(1-\varepsilon^2)k^2/2+O(k)\), proving the first assertion.

**3. Total-count lower bound.** Set \(s=k-\lceil2\log_2(k+2)\rceil\) when \(k\) is large enough to make \(s\ge1\). Then \(2^s-1\le n/(k+2)^2\le n/4\), and the preceding construction gives

\[
\log_2 b(n)\ge\log_2 b_{=s}(n)\ge\frac12 k^2-O(k\log(k+2)).
\]

Together with Step 1 this proves the total-count asymptotic and, after subtraction, the sharp support large-deviation formula.

**4. Semi-Pell separation.** The overpartition interpretation yields

\[
\frac{p(n)}{b(n)}=\frac1{b(n)}\sum_{\lambda\in\mathcal B(n)}2^{J(\lambda)-1}.
\]

Since \(J(\lambda)\le k+1\), the ratio is at most \(2^k\). On the other hand, for any fixed \(\varepsilon\in(0,1)\), the proportion having \(J(\lambda)\le t\) equals

\[
\frac{b_{\le t}(n)}{b(n)}
=2^{-\varepsilon^2 k^2/2+O_{\varepsilon}(k\log(k+2))}=o(1).
\]

Thus the ratio is at least \(2^t(1-o(1))\), because the complementary partitions have \(J(\lambda)\ge t+1\). Dividing the base-two logarithm by \(\log_2 n\sim k\), the lower limit is at least \(1-\varepsilon\) and the upper limit at most \(1\). Sending the arbitrary fixed \(\varepsilon\) to zero proves the sharp exponent \(1\).

## Verification

The standalone `check.py` computes the coefficient arrays for all powers of two with absent-or-odd-positive multiplicity by a finite generating-function dynamic program. It separately constructs the semi-Fibonacci and semi-Pell recurrences and checks \(b(n)=\operatorname{sf}(n)\) and \(2\operatorname{sp}(n)=\sum_{\lambda\in\mathcal B(n)}2^{J(\lambda)}\) for every integer \(1\le n\le2048\). This is a finite consistency check only: the unlimited assertions follow from Steps 1–4, including the explicit error control.

## Relationship to prior work

Andrews (2019), Theorem 1, establishes \(\operatorname{sf}(n)=|\mathcal B(n)|\), and studies parity. Ballantine and Beck (2023), Theorem 6.1, identify semi-Pell partitions with odd binary overpartitions whose largest part is overlined. Their concluding Section 12 explicitly proposes comparing the growth of odd-index sub-sequences, including \(\operatorname{sf}\) and \(\operatorname{sp}\). The 2023 paper of Keith and Munagi gives composition interpretations, generating functions and congruences, not the support large-deviation rate or the odd-index ratio exponent. Relevant OEIS entries tabulate the individual recurrences but do not state these asymptotic comparisons. These literature distinctions motivate the new asymptotic problem; they do not assert independent priority certification.

## Limitations

The exponent result applies along positive odd indices, not uniformly over all integers: both sequences equal one at powers of two. The result establishes the logarithmic-scale support large-deviation exponent and a polynomial ratio exponent, not an asymptotic multiplicative constant or a local limit theorem. It does not compare every self-similar family mentioned in the motivating paper. A previously unindexed general theorem about joint support statistics might imply these results; no independent validation or exhaustive historical search is claimed.

## References

1. C. Ballantine and G. Beck, *Partitions enumerated by self-similar sequences*, arXiv:2303.11493v1 (20 March 2023), especially Section 6, Theorem 6.1, and Section 12. https://arxiv.org/pdf/2303.11493
2. G. E. Andrews, *Binary and Semi-Fibonacci Partitions*, J. Ramanujan Soc. Math. Math. Sci. 7 (2019), 1–6, Theorem 1. https://georgeandrews1.github.io/pdf/Binary%20and%20Semi-Fibonnaci.pdf
3. W. J. Keith and A. O. Munagi, *Power compositions and semi-Pell compositions*, Online J. Analytic Combin. 18 (2023), Paper 2. https://combinatorialpress.com/article/ojac/vol18/276.pdf
4. OEIS A030067 (semi-Fibonacci), A129095 (semi-Pell), and A129096 (odd-index semi-Pell). https://oeis.org/A030067 ; https://oeis.org/A129095 ; https://oeis.org/A129096
