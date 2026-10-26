# The complete spectrum of distinct semiprime unit fractions and a sharp prime-zeta threshold

## Finding

An **unrestricted semiprime** is the product of two primes, counted with multiplicity, so that squares of primes are admitted. Let \(\mathcal E\) be the set of finite sums of pairwise distinct unit fractions \(1/(pq)\), with primes \(p\le q\). All sums are finite and nonempty.

**Exact spectrum theorem.** Let \(x=a/b>0\), where \(a,b\) are coprime positive integers. Let \(S(b)=\{p:\nu_p(b)=2\}\), and put \(Q(b)=\sum_{p\in S(b)}1/p^2\). Then \(x\in\mathcal E\) if and only if the following hold:

1. \(\nu_p(b)\le2\) for every prime \(p\).
2. \(a\equiv b/p^2\pmod p\) for every \(p\in S(b)\).
3. \(a/b\ge Q(b)\).

For every representation of \(x\), the prime-square unit fractions are **forced uniquely**: they are precisely \(\{1/p^2:p\in S(b)\}\). If \(x=Q(b)\), these are the entire representation. If \(x>Q(b)\), the positive remainder is a sum of distinct reciprocals \(1/(pq)\) with \(p<q\).

**Sharp universal boundary.** Let \(\mathsf P_2=\sum_{p\text{ prime}}p^{-2}\) (the convergent prime-zeta constant at two). Among positive reduced rationals satisfying conditions 1 and 2, every \(x\ge\mathsf P_2\) belongs to \(\mathcal E\); the threshold is best possible: nonrepresentable, locally admissible rationals approach \(\mathsf P_2\) from below.

**Fixed-denominator frequency.** If every prime exponent in \(b\) is at most two, the number of reduced positive numerators \(1\le a\le X\) such that \(a/b\in\mathcal E\) equals

\[
\frac{\varphi(b)}{b}\left(\prod_{p\in S(b)}\frac{1}{p-1}\right)X+O_b(1).
\]

Equivalently, the limiting proportion among numerators coprime to \(b\) is \(\prod_{p\in S(b)}(p-1)^{-1}\). For other denominators no representations exist.

## Assumptions and scope

The one non-elementary input is the **squarefree-denominator semiprime-fraction theorem**, proved by Shisheng Li (2026, arXiv:2609.32140): every positive rational whose reduced denominator is squarefree is a finite sum of distinct reciprocals \(1/(pq)\) with \(p\ne q\). The present results are conditional only on that published theorem, not on any numerical experiment. No upper bound is claimed for the number or size of the required denominators.

A representation cannot reuse a denominator. The condition of distinctness is essential for the forced-square argument. An empty residual sum is permitted after removing forced square terms, but the original sum is nonempty because \(x>0\).

## Proof

**Prime-square forcing.** Consider any finite sum \(x\) over distinct unrestricted semiprimes. Fix a prime \(p\). Every summand other than \(1/p^2\) has \(p\)-adic valuation at least \(-1\). Since the square denominator can occur at most once, inclusion of \(1/p^2\) makes the entire sum have valuation exactly \(-2\); omission makes that valuation at least \(-1\). Hence \(\nu_p(b)=2\) if and only if \(1/p^2\) occurs. This establishes condition 1 and the uniqueness of the square part \(Q(b)\).

**Residual congruences.** If condition 1 holds, then \(x-Q(b)\) has a squarefree reduced denominator exactly when, for each \(p\in S(b)\), its numerator over the common denominator \(b\) is divisible by \(p\). In that numerator \(a-\sum_{q\in S(b)}b/q^2\), all terms indexed by \(q\ne p\) are divisible by \(p\). Thus the criterion is precisely \(a\equiv b/p^2\pmod p\). As every original summand is positive, \(x\ge Q(b)\), proving necessity.

**Sufficiency.** Suppose the three conditions hold. If \(x=Q(b)\), the nonzero target is already the displayed distinct prime-square sum. If \(x>Q(b)\), the residual \(r=x-Q(b)\) is positive and, by the congruences above, has squarefree reduced denominator. Apply Li's 2026 theorem to \(r\), obtaining distinct squarefree-semiprime reciprocals. Their denominators cannot equal any prime square and are distinct from each other, so adding the forced square fractions represents \(x\) as required.

**Best universal threshold.** Because \(S(b)\) is finite, \(Q(b)<\mathsf P_2\); hence conditions 1 and 2 imply condition 3 whenever \(x\ge\mathsf P_2\). To show sharpness, let \(p_1=2,p_2=3,\ldots\) be the primes and for \(k\ge2\) set \(R_k=\prod_{i=1}^k p_i\), \(Q_k=\sum_{i=1}^k p_i^{-2}\), and \(x_k=Q_k-1/R_k\). This is positive. Writing \(Q_k=A_k/R_k^2\) with \(A_k=\sum_{i=1}^k(R_k/p_i)^2\), we have \(x_k=(A_k-R_k)/R_k^2\). For each \(p_i\), its numerator is congruent to \((R_k/p_i)^2\ne0\pmod {p_i}\); thus the fraction is reduced and has denominator \(R_k^2\), and satisfies condition 2 at every square-prime support. Nevertheless \(x_k<Q_k\), so it is not representable. As \(k\to\infty\), \(Q_k\to\mathsf P_2\) and \(1/R_k\to0\), whence \(x_k\uparrow\) in limit to \(\mathsf P_2\) from below (no monotonicity of the sequence itself is needed).

**Numerator frequency.** Fix \(b\) with exponents at most two. By the Chinese remainder theorem, the local restrictions cut the \(\varphi(b)\) reduced residue classes modulo \(b\) by the factor \(\prod_{p\in S(b)}(p-1)^{-1}\): modulo \(p^2\), exactly \(p\) of the \(p(p-1)\) units lift the prescribed nonzero residue modulo \(p\). All but finitely many positive numerators in these classes also satisfy the threshold \(a/b\ge Q(b)\). Counting complete residue periods gives the claimed asymptotic with error \(O_b(1)\).

## Verification

The standalone `verify.py` uses exact rational arithmetic to check every subset of the 15 semiprime denominators supported on the five primes \(2,3,5,7,11\). In all 32768 cases it verifies the local necessary conditions and matches prime-square inclusion to exact denominator valuation. It also checks four sharpness examples and ten full residue periods for the predicted fixed-denominator factor. It checks \(7/36\notin\mathcal E\) against the exact inequality, whereas \(13/36=1/4+1/9\) and \(19/36=1/4+1/9+1/6\) are explicit representations. These calculations do not independently prove the infinite existence theorem used for the residual sums.

Run with `python3 verify.py` using only the Python standard library.

## Relationship to prior work

Li's September 2026 paper, arXiv:2609.32140, establishes universal representability when the **reduced target denominator is squarefree**, and its summand denominators have two **distinct** prime factors. Its June 2026 predecessor, arXiv:2606.15159, proves results for integers and certain large rational targets. Those results are credited as the indispensable existence inputs, not newly reproved here.

The present classification permits semiprime denominators \(p^2\) in addition to \(pq\) for distinct primes, and determines the exact new congruence-and-positivity obstructions for **all** positive rational targets. The sharp prime-zeta cutoff and the rational-numerator density quantify these obstructions. A prior short-expansion result for prime reciprocals concerns a different length-constrained squarefree-semiprime problem. The local lifting and counting arguments are elementary deductions from the cited universal existence theorem; they do not constitute an independent proof of that theorem.

## Limitations

The main cited September preprint's abstract and explicit theorem statement were accessible for verification; the complete manuscript could not be inspected in this research pass. Equivalent corollaries in other literature may have been missed, and independent literature review remains appropriate. The sharpness construction supplies an approaching sequence and does not claim that the prime-zeta constant is itself rational or representable. Counting estimates are for a **fixed** reduced denominator; no uniformity in \(b\) is proved.

## References

- Shisheng Li, *Unit fractions with semiprime denominators: an elementary proof of Erdős Problem #306*, arXiv:2609.32140 (first public version 2026-09-26), https://arxiv.org/abs/2609.32140.
- Shisheng Li, *Every natural number is a sum of distinct semiprime unit fractions*, arXiv:2606.15159 (2026-06), https://arxiv.org/abs/2606.15159.
- MSC2020 11D68: Rational numbers as sums of fractions.
