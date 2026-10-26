# Interlaced divisor chains are binomid at every level

## Finding
For a sequence of positive integers \(f=(f_n)_{n\ge1}\), define its generalized factorial \(f_n!=\prod_{i=1}^n f_i\) (with \(f_0!=1\)) and its generalized binomial coefficient
\[B_f(n,k)=\frac{f_n!}{f_k!f_{n-k}!}\qquad(0\le k\le n).\]
Define the width-\(j\) column of the binomid pyramid by \(C_j(n)=B_f(n+j-1,j)\), for integers \(j,n\ge1\). A sequence is *binomid at every level* if for every \(j\ge1\), all \(B_{C_j}(n,k)\) are integers.

**Theorem.** If \(f_1\mid f_2\) and \(f_n\mid f_{n+2}\) for all integers \(n\ge1\), then \(f\) is binomid at every level. The hypothesis permits sequences that are not ordinary divisor chains and that are not divisor-product sequences.

## Assumptions and scope
All terms are positive integers. No regularity, boundedness or recurrence assumption is imposed beyond the two divisibilities. The statement holds simultaneously for every prime valuation, every positive column width and every pair of generalized-binomial indices. The initial relation \(f_1\mid f_2\) is used for odd-length intervals starting at even positions.

## Proof
**Interval lemma.** Let \((a_n)_{n\ge1}\) be a sequence of real numbers with \(a_1\le a_2\) and \(a_{n+2}\ge a_n\) for all \(n\ge1\). For all integers \(s,L\ge1\),
\[\sum_{i=s}^{s+L-1}a_i\ge\sum_{i=1}^L a_i.\tag{1}\]
For odd \(s\), each shifted term is at least its corresponding initial term by the same-parity inequalities. For even \(s\), write \(s=2r+2\), \(r\ge0\). When \(L=2h\), compare the \(h\) even-position shifted terms with \(a_2,a_4,\ldots,a_{2h}\) and the \(h\) odd-position shifted terms with \(a_1,a_3,\ldots,a_{2h-1}\). Each comparison follows from monotonicity along the appropriate parity class. When \(L=2h+1\), compare the first \(h\) shifted even-position terms with \(a_2,a_4,\ldots,a_{2h}\), the next \(h\) shifted odd-position terms with \(a_3,a_5,\ldots,a_{2h+1}\), and the last shifted even-position term with \(a_1\). The last comparison uses \(a_{s+2h}\ge a_2\ge a_1\). This includes \(h=0\), proving (1).

Fix a prime \(p\), and set \(a_n=\nu_p(f_n)\). The hypotheses give \(a_1\le a_2\), \(a_{n+2}\ge a_n\). By (1),
\[\nu_p(B_f(N,K))=\sum_{i=N-K+1}^{N}a_i-\sum_{i=1}^{K}a_i\ge0\]
for every \(N\ge K\ge0\), with the empty-sum convention. Thus all column terms are positive integers. Fix now a width \(j\ge1\), and define \(b_n=\nu_p(C_j(n))\). Then
\[b_n=\sum_{i=n}^{n+j-1}a_i-\sum_{i=1}^{j}a_i.\]
We have \(b_1=0\) and \(b_2=a_{j+1}-a_1\ge0\), since every \(a_{j+1}\ge a_1\). Also, for every \(n\ge1\),
\[b_{n+2}-b_n=\sum_{i=0}^{j-1}(a_{n+i+2}-a_{n+i})\ge0.\]
The interval lemma applied to \((b_n)\) now gives \(\nu_p(B_{C_j}(N,K))\ge0\) for every \(N\ge K\ge0\). As \(p\) and \(j\) were arbitrary, all levels are integral.

**A natural non-divisor-chain subclass.** Fix an integer \(q\ge2\) and a prime \(p\), and let \(H_q=\langle2,2q+1\rangle\subseteq\mathbb N_0\). Set \(f_n=p\) if \(n\in H_q\), and \(f_n=1\) otherwise. Since \(2\in H_q\), membership is closed under addition by \(2\), while \(f_1=1\) and \(f_2=p\). The theorem applies. Closure of \(H_q\) under addition proves the ComboSum condition \(\gcd(f_m,f_n)\mid f_{m+n}\). Yet \(f_2=p\nmid f_3=1\). Moreover, this is not a divisor-product sequence: for an odd prime \(r\ge2q+1\), a putative divisor-product factor at index \(2r\) would have the nonintegral value \(f_{2r}f_1/(f_2f_r)=1/p\). Hence Shapiro's ordinary divisor-chain and divisor-product sufficient criteria do not subsume these examples.

**Boundary at three-step divisibility.** Put \(f_n=2^{a_n}\), where \((a_n)=(0,1,1,0,1,1,\ldots)\). This has \(f_1\mid f_2\mid f_3\) and \(f_n\mid f_{n+3}\) for all \(n\). Its width-two column has exponent sequence \((0,1,0,0,1,0,\ldots)\), so \(B_{C_2}(4,2)=1/2\), not an integer. Thus replacing the two-step hypothesis by an analogous three-step hypothesis fails even with a stronger initial segment.

## Verification
Run `python verify_binomid.py` with Python 3. The standalone program checks nonnegative prime-exponent inequalities across 400 pseudorandom interlaced sequences and 159 finite numerical-semigroup indicator examples, and checks the explicit three-step counterexample. Its successful finite checks are corroborative, not an exhaustive proof of the universally quantified theorem. The proof above supplies the unbounded argument.

## Relationship to prior work
Shapiro's *Divisibility Properties for Integer Sequences* (2023), Proposition 5(a), establishes all-level binomidness for ordinary divisor chains; its Theorem 15 provides a divisor-product sufficient condition, and its Question 24 asks whether every ComboSum sequence is binomid at every level. The present interlaced-chain theorem is a separate all-level sufficient condition, and the family \(H_q\) resolves a strict non-divisor-chain, non-divisor-product subfamily of that question, **not the full question**. Caalim and Tanaka (2024) study lexicographically minimal extensions of finite binomid indexes rather than the two-step all-level condition. General implicit sufficient criteria in other work may cover the statement and remain an originality risk.

## Limitations
This is not a characterization of all all-level-binomid sequences; it does not resolve the unrestricted ComboSum problem. Failure of a three-step analogue does not establish optimality among all other hypotheses. The scientific originality comparison is limited to the inspected publications and searched records; an implicit or unindexed prior theorem remains possible. No independent mathematical audit has been performed.

## References
1. D. B. Shapiro, *Divisibility Properties for Integer Sequences*, arXiv:2302.02243v1 (2023); *Integers* 23 (2023), A57. https://math.colgate.edu/~integers/x57/x57.pdf
2. J. Caalim and Y.-i. Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, *Integers* 24 (2024), A53. https://math.colgate.edu/~integers/y53/y53.pdf
