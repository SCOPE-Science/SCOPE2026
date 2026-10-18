# Exact phase rigidity of dyadic sliding lag-one correlation in the Rudin–Shapiro word

## Finding
Let \(r_n\) be the parity of the number of overlapping occurrences of two consecutive one-bits in the binary expansion of \(n\), starting with \(r_0=0\). Define \(s_n=(-1)^{r_n+r_{n+1}}\). **For every integer \(k\ge3\) and every starting index \(j\ge0\)**, put \(q=\lfloor j/2^{k-1}\rfloor\). Then
\[
\sum_{i=j}^{j+2^k-1}s_i=(-1)^{k-2+q}(s_q-s_{q+1})\in\{-2,0,2\}.
\]
Thus all \(2^{k-1}\) consecutive starts with the same \(q\) have exactly the same dyadic lag-one correlation. The three values all occur. For every \(m\ge2\), among all starts \(0\le j<2^{m+k-1}\), exactly \(2^{m+k-2}\) yield zero and exactly \(2^{m+k-3}\) yield each of \(+2\) and \(-2\).

Equivalently, every length-\(2^k+1\) factor of the Rudin–Shapiro word has a number of unequal neighboring pairs belonging to
\[
\{2^{k-1}-1,\ 2^{k-1},\ 2^{k-1}+1\}.
\]
The exact phase formula determines which one occurs at each starting position.

## Assumptions and scope
Indices are nonnegative integers, the binary expansion of zero is treated as having no adjacent one-pair, and all blocks are in the one-sided infinite Rudin–Shapiro word. The summation contains exactly \(2^k\) adjacent-pair products, so it acts on \(2^k+1\) underlying binary symbols. The conclusion holds for arbitrarily large starts, not only for dyadically aligned or finite-word starts. The sharp three-value statement is asserted for \(k\ge3\); no extrapolation outside that range is needed.

## Proof
Write \(\varepsilon_t=(-1)^t\). Appending a zero to a binary integer adds no \(11\) pair, whereas appending one adds a \(11\) pair precisely when the previous low bit was one. Hence
\[
r_{2t}=r_t,\qquad r_{2t+1}=r_t+(t\bmod2)\pmod2.
\]
It follows directly that
\[
s_{2t}=\varepsilon_t,\qquad s_{2t+1}=\varepsilon_t s_t.\tag{1}
\]
For every integer \(l\ge1\) and \(j\ge0\), define the two window sums
\[
S_l(j)=\sum_{i=j}^{j+2^l-1}s_i,\qquad
U_l(j)=\sum_{i=j}^{j+2^l-1}\varepsilon_i s_i.
\]
For \(l\ge2\), pairing the terms at \(2t\) and \(2t+1\) using (1) gives
\[
S_l(2h)=\sum_{t=h}^{h+2^{l-1}-1}\varepsilon_t(1+s_t)
=U_{l-1}(h),\tag{2}
\]
because the sum of the even number \(2^{l-1}\) of alternating signs vanishes. Moreover, \(s_{2h+2^l}=\varepsilon_{h+2^{l-1}}=\varepsilon_h=s_{2h}\). Sliding the sum by one term therefore gives \(S_l(2h+1)=S_l(2h)\). Together,
\[
S_l(j)=U_{l-1}(\lfloor j/2\rfloor)\quad(l\ge2).\tag{3}
\]
Likewise, pairing for the signed sum gives
\[
U_l(2h)=\sum_{t=h}^{h+2^{l-1}-1}\varepsilon_t(1-s_t)
=-U_{l-1}(h),\tag{4}
\]
again because the alternating-sign sum vanishes. Here the summand \(\varepsilon_{2h}s_{2h}=\varepsilon_h\) agrees with \(\varepsilon_{2h+2^l}s_{2h+2^l}\), so sliding by one term yields \(U_l(2h+1)=U_l(2h)\). Thus
\[
U_l(j)=-U_{l-1}(\lfloor j/2\rfloor)\quad(l\ge2).\tag{5}
\]
Iterating (3) and (5) for \(k\ge3\) proves
\[
S_k(j)=(-1)^{k-2}U_1(\lfloor j/2^{k-1}\rfloor).
\]
Finally \(U_1(q)=\varepsilon_q s_q-\varepsilon_{q+1}s_{q+1}
=\varepsilon_q(s_q-s_{q+1})\), which yields the main identity and its three-value restriction.

For the exact distribution, (1) gives, for every \(h\ge0\),
\[
U_1(2h)=\varepsilon_h(1-s_h),\qquad
U_1(2h+1)=-\varepsilon_h(1+s_h).
\]
Exactly one term in each pair vanishes and the other equals \(-2\varepsilon_hs_h\). For \(m\ge2\), half of the indices \(0\le q<2^m\) therefore give zero. The nonzero signs balance: their signed sum is \(-2U_{m-1}(0)\), while \(U_1(0)=0\) (because \(s_0=s_1=1\)) and (5) shows inductively that \(U_{m-1}(0)=0\). Therefore exactly one quarter of these \(q\) values give \(+2\) and one quarter give \(-2\). Each such \(q\) appears for exactly \(2^{k-1}\) successive starts \(j\), proving the stated frequencies. In particular all three values occur.

In a block of \(2^k+1\) symbols, let \(E\) be the number of adjacent unequal pairs. Each equal pair contributes \(+1\) to \(S_k\) and each unequal pair contributes \(-1\), hence \(S_k=2^k-2E\) and \(E=2^{k-1}-S_k/2\). This proves the factor formulation.

## Verification
The accompanying standalone `verify_phase.py` computes the Rudin–Shapiro sign word both from its digit definition and from the independent binary recurrences. It tests the exact formula for 1,175,569 dyadic sliding windows, verifies the complete frequencies at twelve powers of two, and checks the closed form at eighty large, non-prefix starting positions. The verifier output is:

`VERIFY_OK independent_generators=131074 sliding_windows=1175569 dyadic_histograms_m2_to13=12 large_offset_checks=80`

The finite checks are reproducibility checks only. The proof above establishes the theorem for all stated \(k\) and \(j\).

## Relationship to prior work
The parity-of-adjacent-one-bits word is the classical Rudin–Shapiro automatic word. Parreau, Rigo, Rowland and Vandomme (2014/2015) develop an approach to \(\ell\)-abelian complexity and prove specific \(2\)-abelian regularity results for Thue–Morse and period-doubling words, not the present Rudin–Shapiro dyadic sliding-window identity. Marcovici, Stoll and Tahay (2020) establish estimates for generalized Rudin–Shapiro pair correlations averaged from the origin; their published asymptotic bounds do not specify the all-starting-position exact dyadic phase formula or its exact distribution. Katz and van der Linden (2021) study peak sidelobe levels and crosscorrelation of finite Golay–Rudin–Shapiro sequences, whose extremal shift correlations have different indexing and summation quantifiers. No equivalent formula was found in the inspected literature; this is not a proof of priority.

## Limitations
This is a lag-one statement at dyadic lengths; the argument makes no claim about other lags, arbitrary window lengths, or stronger spectral claims. Originality assessment is based on accessible published sources and database searches rather than an exhaustive historical search. No independent scientific validation has been performed.

## References
- A. Parreau, M. Rigo, E. Rowland and E. Vandomme, *A new approach to the 2-regularity of the ℓ-abelian complexity of 2-automatic sequences*, arXiv:1405.3532 (first posted 2014-05-14), *Electronic Journal of Combinatorics* 22 (2015), P1.27. https://arxiv.org/abs/1405.3532
- I. Marcovici, T. Stoll and M. Tahay, *Discrete correlations of order 2 of generalised Rudin–Shapiro sequences: a combinatorial approach*, arXiv:2006.13162 (first posted 2020-06-23). https://arxiv.org/abs/2006.13162
- D. J. Katz and C. M. van der Linden, *Peak Sidelobe Level and Peak Crosscorrelation of Golay–Rudin–Shapiro Sequences*, arXiv:2108.07318 (first posted 2021-08-16). https://arxiv.org/abs/2108.07318
