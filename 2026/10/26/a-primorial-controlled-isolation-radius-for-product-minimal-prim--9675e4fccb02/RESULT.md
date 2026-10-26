# A primorial-controlled isolation radius for product-minimal prime partitions

## Finding
Let \(p_1=2,p_2=3,\ldots\) be the primes in increasing order, and define \(P_0=1\) and \(P_j=\prod_{i=1}^{j}p_i\) for \(j\ge1\). For every integer \(M\ge2\), define the finite index
\[
\Lambda(M)=\max\{k\ge1:P_{k-1}<kM\},\qquad H(M)=M\Lambda(M).
\]
A nonempty finite set \(A\) of distinct primes is *product-minimal* if its product is minimal among products of distinct-prime sets having the same sum. Write \(s=\sum_{p\in A}p\) and \(M=\prod_{p\in A}p\).

**Theorem.** For every such product-minimal \(A\), and every prime \(q>H(M)\) that is the unique prime in the closed interval \([q-H(M),q+H(M)]\), the set \(A\cup\{q\}\) is the unique product-minimal partition of \(s+q\). Indeed, every finite set \(B\) of distinct primes satisfying
\[
\sum_{p\in B}p=s+q,\qquad \prod_{p\in B}p\le qM
\]
necessarily equals \(A\cup\{q\}\).

The isolation radius \(H(M)\) is quasi-linear in \(M\):
\[
H(M)=(1+o(1))\,M\frac{\log M}{\log\log M}\quad(M\to\infty).
\]
Here and below the asymptotic is a property of the integer function \(H\), not a uniform bound for the size of the isolated prime \(q\).

## Assumptions and scope
All products of finite sets use the convention that the empty product is \(1\); the empty sum is \(0\). Competing prime sets \(B\) have pairwise distinct elements, as in the motivating distinct-prime partition problem. The criterion is sufficient, not necessary; it imposes a symmetric prime-free interval around \(q\). The quantity \(\Lambda(M)\) is finite because \(P_{k-1}/k\to\infty\), and is at least \(2\) for \(M\ge2\). Thus \(H(M)\ge2M\ge s\), ensuring \(q\notin A\).

## Proof
Fix \(A,M,s,q\) as stated. Let \(B\) be a finite distinct-prime set with sum \(q+s\) and product at most \(qM\); the set \(A\cup\{q\}\) itself is one candidate. Put \(k=|B|\ge1\), \(b=\max B\), \(U=B\setminus\{b\}\), \(u=\sum_{p\in U}p\), and \(R=\prod_{p\in U}p\). Since \(b\) is the greatest of the \(k\) positive summands,
\[
b\ge\frac{q+s}{k}>\frac qk,\qquad R=\frac{\prod_{p\in B}p}{b}\le\frac{qM}{b}<kM.
\]
The \(k-1\) primes in \(U\) are distinct, so their product is at least the product of the first \(k-1\) primes: \(R\ge P_{k-1}\). Hence
\[
P_{k-1}\le R<kM,
\]
and the definition of \(\Lambda(M)\) gives \(k\le\Lambda(M)\). Consequently
\[
R<kM\le M\Lambda(M)=H(M).
\]
For a set of integers greater than one, its sum does not exceed its product if it is nonempty. In particular, \(0\le u\le R<H(M)\), with the inequality also holding for \(U=\varnothing\). Moreover \(0<s\le M<H(M)\). From the equal-sum condition \(b+u=q+s\),
\[
|b-q|=|s-u|<H(M).
\]
Since \(b\) and \(q\) are primes and \(q\) is the only prime in \([q-H(M),q+H(M)]\), it follows that \(b=q\). We therefore have \(\sum_{p\in U}p=s\) and \(R\le M\). The product-minimality of \(A\) yields \(R\ge M\), so \(R=M\). Unique prime factorization forces \(U=A\). Thus \(B=A\cup\{q\}\), proving both assertions.

For the growth assertion, the prime number theorem gives \(\log P_{k-1}=(1+o(1))k\log k\) as \(k\to\infty\). The criterion \(P_{k-1}<kM\) therefore has terminal index \(\Lambda(M)=(1+o(1))\log M/\log\log M\). Multiplying by \(M\) proves the displayed asymptotic. No unproved prime-gap estimate is used: existence of arbitrarily large eligible \(q\) for each fixed \(H(M)\) follows from the classical isolated-prime theorem cited below.

## Verification
The standalone integer-arithmetic script `verify.py` computes \(\Lambda(M)\), enumerates isolated primes for several product-minimal base sets, and exhaustively compares the minimum product among all distinct-prime subsets at the resulting sums, through the stated finite cutoff. Run `python3 verify.py`. It prints `VERIFY_OK` on success. These tests corroborate the theorem only on a finite domain; the preceding proof establishes all parameters.

For \(A=\{3,5,19\}\), whose product-minimality at sum \(27\) is noted in the motivating paper, \(M=285\) and \(\Lambda(M)=5\), so the sufficient isolation radius is \(1425\), compared with the paper's \(4M^2=324900\). At \(A=\{2\}\), the new radius is \(4\) rather than \(16\).

## Relationship to prior work
Campbell's 2026 paper establishes the prime-extension lemma using the sufficient symmetric isolation radius \(4M^2\) (Lemma 2), by bounding the number of competing parts via a square-root estimate. The present theorem strengthens precisely this sufficient radius to \(M\Lambda(M)\), by using the primorial bound forced by *distinctness* of the competing primes. This changes quadratic dependence on \(M\) to quasi-linear dependence, a quantitative refinement of the paper's inductive construction. The paper's separate prime-gap condition for the maximum-product complement construction (Lemma 6) is not changed or claimed as a consequence.

## Limitations
The criterion need not be necessary, and does not bound the least eligible prime \(q\) or the minimal odd integer whose product-minimal partition has a specified size. It does not improve the classical theorem on the frequency or sizes of gaps around isolated primes. The possibility of an equivalent criterion implicit in broader prime-partition literature remains; independent mathematical validation has not been performed.

## References
- J. M. Campbell, *On a problem on partitions into distinct primes*, arXiv:2610.19534v1 (publicly submitted 2026-10-14), especially Lemmas 1--3 and their proofs, https://arxiv.org/html/2610.19534v1.
- W. Sierpiński, 1948 isolated-prime theorem, as quoted and attributed in Campbell's Lemma 1.
- Prime number theorem, used only for the optional asymptotic evaluation of \(\Lambda(M)\).
