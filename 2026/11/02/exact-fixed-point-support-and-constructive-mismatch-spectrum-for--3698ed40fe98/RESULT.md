# Exact fixed-point support and constructive mismatch spectrum for multiset permutations

## Finding
Let \(a_1,\ldots,a_k\) be positive integers, \(n=\sum_{i=1}^k a_i\), and let \(Y\) be a uniform distinct permutation of the multiset containing \(a_i\) copies of symbol \(i\). Compare \(Y\) with the canonical sorted word \(w=1^{a_1}\cdots k^{a_k}\). Write \(W=|\{j:Y_j=w_j\}|\) and \(M=n-W\). The *complete* exact support of \(W\), for every finite multiplicity profile, is as follows.

1. For \(k=1\), \(\operatorname{supp}(W)=\{n\}\).
2. For \(k=2\), \(\operatorname{supp}(W)=\{n-2j:0\le j\le\min(a_1,a_2)\}\).
3. For \(k\ge3\), define \(m_{\max}=\min\{n,2(n-\max_i a_i)\}\). Then
   \[\operatorname{supp}(W)=\{n\}\cup\{n-m:2\le m\le m_{\max}\}.\]

More generally, for every \(k\ge1\) and integer \(m\) in \([0,n]\), the exact feasibility condition is
\[\Pr(M=m)>0\ \Longleftrightarrow\ m=0\ \text{or}\ \bigl(m\ge2\ \text{and}\ \sum_{i=1}^k\min\{a_i,\lfloor m/2\rfloor\}\ge m\bigr).\]
The proof supplies an explicit rearrangement realizing every feasible value, without randomized sampling or asymptotics.

## Assumptions and scope
All multiplicities are positive integers. The uniform law is over the \(n!/\prod_i a_i!\) *distinct* words with the prescribed multiplicities, so every such word has positive probability. A fixed point means a matching *position*, not a fixed labeled copy, and mismatch counts refer to the canonical block word. There is no restriction on \(k\), \(n\), or the relative sizes of the multiplicities.

## Proof
**Step 1: reduction to a balanced mismatch profile.** For a candidate word, let \(d_i\) be the number of wrong symbols in the \(a_i\) positions belonging to block \(i\). Since the total number of occurrences of symbol \(i\) is preserved, exactly \(d_i\) copies of symbol \(i\) must be placed *outside* block \(i\). Consequently \(\sum_i d_i=m\), \(0\le d_i\le a_i\), and the number of non-\(i\) destinations available to those copies is \(m-d_i\). Thus \(d_i\le m-d_i\), so \(d_i\le\lfloor m/2\rfloor\). Summing yields the stated capacity inequality, necessary for every positive \(m\). A single mismatch is impossible because the multiset counts are preserved.

**Step 2: constructive sufficiency of the capacity inequality.** Suppose \(m\ge2\) and \(\sum_i\min(a_i,\lfloor m/2\rfloor)\ge m\). Greedily choose integers \(d_i\) satisfying \(0\le d_i\le\min(a_i,\lfloor m/2\rfloor)\) and \(\sum_i d_i=m\). Form the length-\(m\) cyclic word \(u\) with \(d_1\) consecutive copies of symbol \(1\), followed by \(d_2\) copies of \(2\), and so forth. Put \(b=\lfloor m/2\rfloor\), and construct the new mismatch-site labels by \(v_j=u_{j+b\bmod m}\). Every contiguous monochromatic cyclic block has length at most \(b\), while the shorter circular separation of sites \(j\) and \(j+b\) is exactly \(b\). Hence \(u_j\ne v_j\) at every site. In original block \(i\), replace any \(d_i\) positions by the corresponding \(d_i\) labels from the consecutive segment of \(v\), leaving the other positions unchanged. The rotation preserves each symbol's total count, and all selected positions change while all unselected positions remain fixed. This gives precisely \(m\) mismatches. The construction uses \(O(n)\) elementary operations once the multiplicities are given. The identity arrangement covers \(m=0\).

**Step 3: specialize to two symbols.** Every mismatch from symbol \(1\) to \(2\) must be matched by one from \(2\) to \(1\). Therefore \(m=2j\), where \(0\le j\le\min(a_1,a_2)\). Swapping \(j\) sites of each color attains every such \(j\). One symbol has no mismatches.

**Step 4: specialize to three or more symbols.** Clearly \(m\le n\). If \(a_*\) is a largest multiplicity, the number \(d_*\) of mismatches in its block is at most the number \(n-a_*\) of its copies that can be placed elsewhere. Other blocks altogether have at most \(n-a_*\) mismatches. Thus \(m\le2(n-a_*)\). Conversely suppose \(2\le m\le\min(n,2(n-a_*))\), and let \(b=\lfloor m/2\rfloor\). If all \(a_i\le b\), the total capped capacity equals \(n\ge m\). Otherwise \(a_*>b\). Write \(q=n-a_*\); the assumed maximum bound gives \(q\ge\lceil m/2\rceil\). If every other multiplicity is at most \(b\), their capped sum is \(q\), so the full capacity is at least \(b+\lceil m/2\rceil=m\). If a different multiplicity also exceeds \(b\), that second block contributes \(b\) and a third, nonempty block contributes at least \(1\); hence the capped sum outside the largest block is at least \(b+1\ge\lceil m/2\rceil\). The same capacity bound follows. Step 2 then constructs the witness for each integer \(m\) in the asserted range. No other values occur. This completes the proof.

## Verification
The bundled, standard-library-only `check_support.py` computes exact integer counts of \(W\) by independent dynamic programming over the remaining symbol inventory. It tests all \(2^{11}-1=2047\) ordered positive multiplicity profiles with \(1\le n\le11\), verifies that the sum of counts is the multinomial coefficient, and compares their positive-count supports to *both* formulas. For each of \(19{,}714\) positive support cells, it independently constructs a prescribed-mismatch rearrangement and checks all multiplicities and exact matches. Executing `python3 check_support.py` produces the four lines stored in `CHECK_LOG.txt`.

The dynamic-programming enumeration is finite. It is not the proof for unbounded \(n\); Steps 1–4 establish the theorem for every positive integer profile.

## Relationship to prior work
Stark's 2026 paper studies this exact random variable \(W\), derives its moments, and bounds Poisson approximation error. Its sections 1–4 do not supply the exact finite-sample support classification or an all-profile witness construction. Earlier multiset derangement results, including the 2017 work of Kim, Kim and Seo and the inclusion–exclusion formula in Stanley's *Enumerative Combinatorics*, count the special event \(W=0\); that endpoint does not by itself specify every feasible \(W\). General permutation enumeration can encode exact coefficients, and classical matching conditions motivate the capacity inequality, but the claimed contribution is the closed all-profile support spectrum and constructive realization, not a new general matching theorem or a complete distribution formula.

## Limitations
This determines *which values have positive probability*, not their probabilities, asymptotic rates, modes, or coupling distances. The explicit classification is elementary and may be implicit in older unexamined multiset-rearrangement, matching, or rook-polynomial literature; no definitive historical-priority claim is made. The finite verifier cannot establish the general theorem independently of the analytical proof.

## References
- Dudley Stark, "Poisson approximations of the number of fixed points in random multiset permutations," first posted 2026-08-01, https://arxiv.org/abs/2608.00710 .
- Dongsu Kim, Jang Soo Kim, Seunghyun Seo, "Colored permutations with no monochromatic cycles," *Journal of the Korean Mathematical Society* (2017), author manuscript https://mathsci.kaist.ac.kr/~dskim/papers/J160392AOP.pdf .
- Richard P. Stanley, *Enumerative Combinatorics*, vol. 1, 2nd ed. (2012), Problem 2.12 (multiset derangements).
