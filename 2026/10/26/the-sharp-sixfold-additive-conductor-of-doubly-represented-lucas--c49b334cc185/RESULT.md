# The sharp sixfold additive conductor of doubly represented Lucas numbers

## Finding
Let \(L_0=2\), \(L_1=1\), and \(L_{j+2}=L_{j+1}+L_j\). A *nonconsecutive Lucas representation* of a positive integer is a sum of distinct terms \(L_j\) with no two selected indices adjacent. Indices \(0\) and \(2\) are permitted together. Let \(K\) be the set of positive integers having exactly two such representations, and, for each positive integer \(h\), write
\[
hK=\{k_1+\cdots+k_h:k_i\in K\},
\]
where repeated summands are allowed.

**Theorem.** The least positive integer \(h\) for which \(hK\) contains every sufficiently large integer is \(h=6\). More precisely,
\[
\{1002,1003,\ldots\}\subseteq6K,\qquad1001\notin6K.
\]
Consequently the greatest nonnegative integer outside the *exactly six-summand* set \(6K\) is \(1001\). For every \(1\le h\le5\), infinitely many positive integers lie outside \(hK\).

## Assumptions and scope
All Lucas indices are nonnegative and all summands are positive. Nonconsecutive means nonadjacent *indices*, not different numerical values; in particular \(L_0=2\) and \(L_2=3\) can occur in one representation. The two representations are distinct sets of indices. The additive set \(hK\) permits repetitions of its summands; it does *not* mean the union of sums using at most \(h\) summands.

Write \(\varphi=(1+\sqrt5)/2\) and \(\alpha=1/\varphi=(\sqrt5-1)/2\). The exact characterization established by Chu, Luo, and Miller [1, Section 5] is
\[
K=\{\kappa(n):n\in\mathbb Z_{\ge0}\},\qquad
\kappa(n)=5+4n+3\lfloor\alpha(n+1)\rfloor.
\]
This characterization is prior work, used as the starting point, not claimed as new. OEIS A342089 [2] independently identifies the same sequence.

## Proof
**1. Uniform gap lemma.** For every \(n\ge0\), since \(0<\alpha<1\),
\[
\kappa(n+1)-\kappa(n)
=4+3\big(\lfloor\alpha(n+2)\rfloor-\lfloor\alpha(n+1)\rfloor\big)
\in\{4,7\}.
\]
Thus \(K\) begins at \(5\), is unbounded, and its consecutive gaps are at most \(7\).

**2. A ten-integer bridge in \(5K\).** The following entries are elements of \(K\), and every row is an exact five-term sum (repetitions are intentional).

| Target | Five elements of \(K\) |
| ---: | --- |
| 997 | 5, 12, 30, 30, 920 |
| 998 | 5, 5, 5, 5, 978 |
| 999 | 5, 16, 16, 121, 841 |
| 1000 | 200, 200, 200, 200, 200 |
| 1001 | 5, 5, 12, 30, 949 |
| 1002 | 5, 5, 5, 5, 982 |
| 1003 | 121, 121, 121, 320, 320 |
| 1004 | 5, 77, 200, 200, 522 |
| 1005 | 5, 5, 5, 12, 978 |
| 1006 | 5, 5, 16, 16, 964 |

All memberships can be checked by the displayed closed form for \(\kappa\); the supplied verifier does so exactly. Hence \([997,1006]\cap\mathbb Z\subseteq5K\). For each \(k\in K\), all integers in \([997+k,1006+k]\) belong to \(6K\). The first interval begins at \(1002\), and the intervals from successive \(k\)'s overlap because \(\kappa(n+1)-\kappa(n)\le7\), less than the interval length \(10\). Their union is therefore every integer at least \(1002\).

**3. Exact exclusion of \(1001\).** Suppose \(1001\in6K\), and write its six summands as \(\kappa(n_i)\), where \(n_i\ge0\). Put \(m_i=n_i+1\ge1\), \(T=\sum n_i\), and \(S=\sum\lfloor\alpha m_i\rfloor\). Then
\[
4T+3S=971,\qquad
\alpha(T+6)-6<S<\alpha(T+6).
\]
(The inequalities are strict since \(\alpha\) is irrational.) The latter inequalities place \(T\) strictly between
\[
\frac{971-18\alpha}{4+3\alpha}\quad\text{and}\quad
\frac{989-18\alpha}{4+3\alpha},
\]
which lie between \(163\) and \(164\), and between \(167\) and \(168\), respectively. Thus \(T\in\{164,165,166,167\}\). Reduction of \(4T+3S=971\) modulo \(3\) leaves only \(T=164\) or \(T=167\).

For \(T=164\), the six positive integers \(m_i\) sum to \(170\), and their fractional parts \(\{\alpha m_i\}\) sum to \(170\alpha-105\). Each therefore has fractional part strictly below \(170\alpha-105\). Exact comparison with the quadratic irrational leaves only
\[
A=\{13,34,47,68,81,89,102,123,136,157\}
\]
as possible \(m_i\). For \(T=167\), the \(m_i\) sum to \(173\) and their fractional parts sum to \(173\alpha-101\). Each complementary fractional part \(1-\{\alpha m_i\}\) is strictly below \(107-173\alpha\). The possible \(m_i\) are precisely
\[
B=\{8,21,29,42,55,63,76,97,110,118,131,144,152,165\}.
\]
Both finite, exact coefficient identities hold:
\[
[z^{170}]\Big(\sum_{a\in A}z^a\Big)^6=0,
\qquad
[z^{173}]\Big(\sum_{b\in B}z^b\Big)^6=0.
\]
For clarity, these identities simply enumerate all ordered six-tuples from the two displayed finite sets; the reproducible exact-integer checker in `verify.py` recomputes the candidate sets and coefficients without floating-point arithmetic. Thus neither permitted value of \(T\) is possible, and \(1001\notin6K\).

**4. Optimal number of summands.** For a fixed \(h\ge1\), every integer in \(hK\) has the form
\[
5h+4T+3S,
\qquad T=\sum_{i=1}^h n_i,\qquad S=\sum_{i=1}^h\lfloor\alpha(n_i+1)\rfloor.
\]
As \(\alpha(T+h)-h<S<\alpha(T+h)\), for each fixed \(T\) there are at most \(h\) possible integers \(S\). Moreover every such sum is strictly larger than \((4+3\alpha)T+(2+3\alpha)h\). Hence, for every fixed \(h\),
\[
\#(hK\cap[0,X])\le\frac{h}{4+3\alpha}X+O_h(1).
\]
Since \(4+3\alpha>5\), the coefficient is strictly below \(1\) for every \(h\in\{1,2,3,4,5\}\). None of these sets is cofinite. Part 2 proves that \(6K\) is cofinite, establishing the minimal order.

## Verification
`verify.py` is standalone Python 3 code using only the standard library. It uses the exact identity
\[
\lfloor m\alpha\rfloor=\left\lfloor\frac{\lfloor\sqrt{5m^2}\rfloor-m}{2}\right\rfloor
\qquad(m\ge1)
\]
to enumerate \(K\) without floating-point rounding. It checks all ten five-summand witnesses; computes sixfold subset-sum reachability through \(1001\); and independently recomputes the two quadratic-irrational candidate sets and zero polynomial coefficients. It also enumerates all nonconsecutive Lucas-index subsets contributing positive integers at most \(1006\) and verifies that exactly the \(171\) predicted terms have two representations. Running `python3 verify.py` prints a `VERIFIED` status.

The infinite part of the theorem is proved by the gap and density arguments above; it does not depend on extrapolating finite checks.

## Relationship to prior work
Chu, Luo, and Miller [1] proved the at-most-two representation theorem, the explicit generalized-Beatty description of the ambiguous set, and its asymptotic density. These are premises, not new conclusions here. OEIS [2] records the sequence under its representation meaning and gives a base-\(\varphi\) interpretation. The exact minimal additive order and sharp sixfold conductor stated here are not given in their inspected material.

Pongsriiam [3] studies sumsets of ordinary Beatty sets generated by powers of the golden ratio, including a general consecutive-block criterion for eventual additive covering. That general mechanism is consonant with Part 2, but the specific generalized-Beatty sequence \(K\), its fivefold bridge, and the exact gap \(1001\) require additional identification and verification. Shallit [4] studies Wythoff sumsets and automata, not the exact sixfold sumset of the Lucas-ambiguity sequence in the accessible description. Schaeffer, Shallit, and Zorcic [5] provide decidability methods for quadratic inhomogeneous Beatty sequences, a related general framework but not a recorded determination of this invariant.

## Limitations
The classification of \(K\) is taken from [1], not reproved in full. The sharp \(1002\) threshold concerns *exactly six* summands with repetition; the minimal number of summands needed when varying the number between one and a fixed upper bound is a different question. The absence of a found identical result in literature and databases does not establish publication priority. The inspected published sources and abstract-level comparisons leave a residual risk of an earlier unindexed computation or uninspected specialized result.

## References
1. H. V. Chu, D. C. Luo, and S. J. Miller, *On Zeckendorf Related Partitions Using the Lucas Sequence*, arXiv:2004.08316, first public version April 17, 2020; Sections 3 and 5. https://arxiv.org/html/2004.08316
2. OEIS Foundation, A342089, *Numbers that have two representations as the sum of distinct non-consecutive Lucas numbers*, https://oeis.org/A342089 (inspected October 2026).
3. P. Pongsriiam, *Combinatorial structure and sumsets associated with Beatty sequences generated by powers of the golden ratio*, Electronic Research Archive 30 (2022), 2385–2405, doi:10.3934/era.2022121.
4. J. Shallit, *Sumsets of Wythoff Sequences, Fibonacci Representation, and Beyond*, arXiv:2006.04177, June 7, 2020.
5. L. Schaeffer, J. Shallit, and S. Zorcic, *Beatty Sequences for a Quadratic Irrational: Decidability and Applications*, arXiv:2402.08331, first version February 13, 2024.
