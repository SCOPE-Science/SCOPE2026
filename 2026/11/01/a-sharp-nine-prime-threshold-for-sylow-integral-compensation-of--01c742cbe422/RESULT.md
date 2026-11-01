# A sharp nine-prime threshold for Sylow-integral compensation of \(A_5\)

## Finding

Let \(\pi(H)\) denote the prime divisors of the order of a finite group \(H\), and let \(\omega(|H|)=|\pi(H)|\). For each prime \(p\in\pi(H)\), let \(\nu_p(H)\) be the number of Sylow \(p\)-subgroups and let \(\sigma_p(H)\) be their common order. Define
\[
\gamma(H)=\sum_{p\in\pi(H)}\frac{\nu_p(H)}{\sigma_p(H)+1}.
\]

**Theorem.** For every nontrivial finite nilpotent group \(N\) satisfying
\[
\gamma(A_5\times N)=\gamma(A_5)=\frac92,
\]
one has \(\omega(|N|)\ge9\). This bound is attained. Moreover, every equality case with \(\omega(|N|)=9\) has a Sylow \(2\)-subgroup of order exactly \(2\), has no prime divisors \(3\) or \(5\), and has exactly eight distinct prime divisors greater than \(5\).

In particular, the nine-prime nilpotent factor in the published central-compensation example is optimal in *number of distinct prime divisors*, not necessarily in group order. The arithmetical obstruction is the absence of an identity
\[
\sum_{i=1}^r\frac1{p_i^{e_i}+1}=\frac49
\]
for distinct primes \(5<p_1<\cdots<p_r\), positive integers \(e_i\), and \(r\le7\). With \(r=8\), such an identity exists.

## Assumptions and scope

All groups are finite; \(N\) is nilpotent and nontrivial. The bound counts *distinct primes* dividing \(|N|\), rather than prime factors with multiplicity or direct factors in a chosen group decomposition. Nonabelian Sylow subgroups and arbitrary prime-power Sylow orders are allowed in the lower bound. The theorem concerns direct products with \(A_5\), not arbitrary nonsolvable groups or nonsplit extensions.

The first public motivating source is the May 20, 2026 preprint of Zhang and Yang, arXiv:2605.20976, with primary MSC2020 20D20. Its compensation formula and nine-prime example are prior work. The proof below adds the sharp *lower* bound, including the prime-power case, and the necessary structure of equality cases.

## Proof

**1. Compensation equation.** The Sylow \(2,3,5\) subgroups of \(A_5\) have orders \(4,3,5\) and counts \(5,10,6\), respectively. Therefore \(\gamma(A_5)=1+5/2+1=9/2\). Write \(d_p\) for the order of the Sylow \(p\)-subgroup of \(N\), with \(d_p=1\) when \(p\nmid|N|\). As \(N\) is nilpotent, each of its Sylow subgroups is unique. Multiplication of the Sylow orders in a direct product yields the exact equivalence
\[
\sum_{q\in\pi(N)\setminus\{2,3,5\}}\frac1{d_q+1}
=\Delta_2(d_2)+\Delta_3(d_3)+\Delta_5(d_5),
\]
where
\[
\Delta_2(d)=1-\frac5{4d+1},\quad
\Delta_3(d)=\frac52-\frac{10}{3d+1},\quad
\Delta_5(d)=1-\frac6{5d+1}.
\]
Every defect is nonnegative and is positive exactly when its old prime divides \(|N|\). At least one old prime and one new prime must appear for equality with nontrivial \(N\).

**2. Few-prime reduction.** The seven smallest possible new primes are \(7,11,13,17,19,23,29\). Since \(d_q\ge q\), any collection of at most seven new primes contributes at most
\[
\frac18+\frac1{12}+\frac1{14}+\frac1{18}+\frac1{20}+\frac1{24}+\frac1{30}=\frac{29}{63}<\frac12.
\]
A nontrivial \(3\)-component contributes \(\Delta_3(d_3)\ge3/2\), and a nontrivial \(5\)-component contributes \(\Delta_5(d_5)\ge10/13\). If \(d_2\ge4\), then \(\Delta_2(d_2)\ge12/17\). Each of these exceeds \(29/63\). Consequently, whenever \(\omega(|N|)\le8\), the only possible old-prime contribution is \(d_2=2\), \(d_3=d_5=1\). Its defect is \(4/9\). The six smallest new primes contribute only
\[
\frac18+\frac1{12}+\frac1{14}+\frac1{18}+\frac1{20}+\frac1{24}=\frac{269}{630}<\frac49.
\]
Thus the only remaining hypothetical case with at most eight total prime divisors involves **exactly seven** distinct new primes \(p_1<\cdots<p_7\), all at least seven, with Sylow orders \(p_i^{e_i}\), and sum \(4/9\).

**3. A finite rational obstruction, including all prime powers.** Suppose such seven terms exist. Starting with the smallest allowable prime and proceeding from left to right, compare two alternatives at each of the first five positions: (a) skip the next expected prime, or (b) use that prime with exponent at least two. In either case, maximize every remaining term by using the next available distinct primes to the first power. The resulting exact upper bounds are:

| Position | Forced next prime | Upper bound if skipped | Upper bound if exponent \(\ge2\) |
|---|---:|---:|---:|
| 1 | 7 | \(739/2016\) | \(4477/12600\) |
| 2 | 11 | \(823/2016\) | \(5921/15372\) |
| 3 | 13 | \(121/288\) | \(302/765\) |
| 4 | 17 | \(293/672\) | \(1243/3045\) |
| 5 | 19 | \(4451/10080\) | \(94207/228060\) |

Every displayed bound is **strictly smaller than \(4/9\)**, by exact cross-multiplication. Thus \((p_1,\ldots,p_5)=(7,11,13,17,19)\), and their five exponents equal one. Their sum is \(971/2520\), leaving \(149/2520\) for the last two terms.

If \(p_6\ge31\), then \(p_7\ge37\) and the two terms total at most
\[
\frac1{32}+\frac1{38}=\frac{35}{608}<\frac{149}{2520}.
\]
If the sixth exponent is at least two, then even the maximal possibility is
\[
\frac1{23^2+1}+\frac1{30}=\frac{28}{795}<\frac{149}{2520},
\]
so the sixth exponent is one. The only remaining sixth primes are \(23\) and \(29\). For \(p_6=23\), the seventh term must be \(11/630\), requiring the integer \(p_7^{e_7}+1=630/11\), impossible. For \(p_6=29\), the seventh term must be \(13/504\), requiring \(p_7^{e_7}+1=504/13\), also nonintegral. This contradiction rules out seven or fewer new prime-power terms and proves \(\omega(|N|)\ge9\).

**4. Attainment and extremal old-prime structure.** Let
\[
N_0=C_2\times C_7\times C_{11}\times C_{13}\times C_{17}\times C_{19}\times C_{29}\times C_{71}\times C_{83}.
\]
The exact identity
\[
\frac18+\frac1{12}+\frac1{14}+\frac1{18}+\frac1{20}+\frac1{30}+\frac1{72}+\frac1{84}=\frac49
\]
implies \(\gamma(A_5\times N_0)=9/2\), while \(\omega(|N_0|)=9\). This example and its compensation equality are reproduced from Zhang and Yang, not asserted to be new.

Finally, if \(\omega(|N|)=9\), at most eight new primes can occur. Their combined contribution is at most
\[
\frac18+\frac1{12}+\frac1{14}+\frac1{18}+\frac1{20}+\frac1{24}+\frac1{30}+\frac1{32}=\frac{991}{2016}.
\]
The larger old-prime defects \(3/2\), \(10/13\), and \(12/17\) are all greater than this bound. Hence \(d_2=2\) and \(d_3=d_5=1\), with precisely eight new prime divisors. This proves the theorem.

## Verification

`CHECK.py` is a standalone standard-library program using exact rational arithmetic. It independently recomputes the two extremal prime-sum bounds, each of the ten rational bounds in the forcing table, the last-two-prime obstruction, the original nine-prime witness, and the final eight-new-prime bound. It reports `VERIFY_OK` only if all assertions pass. The recorded `CHECK_OUTPUT.txt` is generated from the packaged program. The finite computation validates the explicit small rational comparisons; the unrestricted statement for all groups and all prime exponents is proved symbolically above.

## Relationship to prior work

Zhang and Yang (2026), arXiv:2605.20976, derive the full nilpotent direct-product compensation equation and exhibit several nine-prime examples. Their Theorem 12.1 reduces the squarefree problem to the equation \(\sum_{q\in Q}1/(q+1)=4/9\); their Corollary 13.1 allows prime powers. The present theorem does *not* re-claim that characterization or any example. It solves the complementary extremal Diophantine problem: **no nontrivial nilpotent compensator can have fewer than nine distinct prime divisors**, even with arbitrary Sylow prime powers, and a minimal one has the stated old-prime structure. In the inspected primary full text, no lower bound on the number of distinct prime divisors was asserted.

Anabanti and Asboei (2024) establish a characterization among finite noncyclic simple groups. Their result does not address nilpotent direct-product compensation or minimal support. No equivalent minimization theorem was found in the recorded literature and research-record comparisons; this does not certify absolute historical priority.

## Limitations

The theorem optimizes \(\omega(|N|)\), not \(|N|\), the number of generators of \(N\), or the order of \(A_5\times N\). It does not classify all eight-prime solutions or all equality groups with nine prime divisors, and it makes no statement about nonsplit extensions or arbitrary nonsolvable groups. The new lower bound uses the published compensation identity and new exact rational inequalities; independent review has not been performed. Older or inaccessible sources may contain an equivalent extremal argument.

## References

1. Y. Zhang and Y. Yang, *A compensation theorem for the Sylow-integral invariant and counterexamples to an \(A_5\)-characterization conjecture*, arXiv:2605.20976 (first submitted May 20, 2026); *European Journal of Mathematics* **12** (2026), article 40, doi:10.1007/s40879-026-00920-6. The full-text version used for comparison includes Sections 3–5 and 11–13.
2. C. S. Anabanti and A. K. Asboei, *On the Integral of the Sylow Polynomial of a Finite Simple Group*, *Siberian Mathematical Journal* **65** (2024), 1402–1406, doi:10.1134/S0037446624060156.
