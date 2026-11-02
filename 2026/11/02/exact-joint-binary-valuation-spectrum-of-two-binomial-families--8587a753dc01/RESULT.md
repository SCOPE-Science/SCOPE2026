# Exact joint binary valuation spectrum of two binomial families

## Finding
For every positive integer \(n\), set
\[
A(n)=\nu_2\!\left(\binom{2n}{n}\right),\qquad
B(n)=\nu_2\!\left(\binom{3n}{n}\right).
\]
**Theorem.** For each integer \(k\ge 1\), the exact set of attained valuations in the fiber \(A(n)=k\) is
\[
\boxed{\{B(n):n\ge1,\ A(n)=k\}=\{0\}\cup\{2,3,\ldots,2k-2\}.}
\]
The second set is empty when \(k=1\). Every permitted pair \((k,b)\) occurs at infinitely many positive indices. In particular, valuation \(1\) never occurs in the family \(\binom{3n}{n}\), despite every integer valuation from \(2\) through the sharp fiberwise maximum \(2k-2\) being realized.

## Assumptions and scope
The symbol \(\nu_2\) is the exponent of \(2\) in a nonzero integer. All binomial coefficients have ordinary integer arguments. The function \(s_2(m)\) counts the ones in the standard binary expansion of a nonnegative integer \(m\). The index \(n\) is always a positive integer, the fiber parameter \(k\) is an integer at least one, and \(b\) denotes a nonnegative integer. No condition is placed on the length of the binary expansion of \(n\). The classification is for the ordered pair of two valuations, not an assertion about their distribution on finite intervals.

## Proof
**Step 1: digit-sum identities.** Legendre's factorial valuation formula yields, for every positive integer \(n\),
\[
A(n)=s_2(n),\qquad B(n)=2s_2(n)-s_2(3n).
\]
Indeed \(\nu_2(m!)=m-s_2(m)\) and \(s_2(2n)=s_2(n)\). Therefore \(A(n)=k\) implies \(B(n)=2k-s_2(3n)\). The integer \(3n\) is divisible by \(3\), so it cannot be a power of two; hence \(s_2(3n)\ge2\). As \(\binom{3n}{n}\) is integral, \(B(n)\ge0\). Consequently \(0\le B(n)\le2k-2\).

**Step 2: the missing valuation.** Count carries when adding \(n\) to \(2n\) in base two, as in Kummer's theorem. Write the binary digits of \(n\) as \(a_i\in\{0,1\}\), with \(a_{-1}=0\), and let \(c_i\in\{0,1\}\) be the carry into the \(i\)-th position, initially \(c_0=0\). The recurrence is
\[
c_{i+1}=\left\lfloor\frac{a_i+a_{i-1}+c_i}{2}\right\rfloor.
\]
If any carry occurs, choose the first outgoing carry \(c_{i+1}=1\). Because \(c_i=0\), necessarily \(a_i=a_{i-1}=1\). At the following position, the incoming carry equals \(1\) and the digit contributed by \(2n\) is \(a_i=1\). Thus \(c_{i+2}=1\) as well. Carries cannot occur exactly once. Since Kummer's theorem identifies their number with \(B(n)\), valuation \(1\) is excluded.

**Step 3: explicit witnesses at extremal weights.** For all \(k\ge1\), put
\[
z_k=\frac{4^k-1}{3}.
\]
Its binary expansion consists of \(k\) isolated ones, and \(3z_k=4^k-1\) has \(2k\) ones. Hence \(A(z_k)=k\) and \(B(z_k)=0\).

For \(j\ge2\), put
\[
e_j=\frac{2^{2j-1}+1}{3}.
\]
Its binary expansion is an alternating string ending in \(11\); it contains exactly \(j\) ones. Since \(3e_j=2^{2j-1}+1\) has two one-bits, \(A(e_j)=j\) and \(B(e_j)=2j-2\).

For \(j\ge3\), put
\[
o_j=\frac{2^{2j-2}+5}{3}.
\]
Its binary expansion is an alternating string ending in \(111\), with exactly \(j\) ones. Since \(3o_j=2^{2j-2}+5\) has exactly three one-bits, \(A(o_j)=j\) and \(B(o_j)=2j-3\). All three expressions are positive integers because their numerators are divisible by \(3\).

**Step 4: preserve a valuation while increasing the other.** Define \(P(n)=4n+1\). Binary concatenation gives
\[
s_2(P(n))=s_2(n)+1,\quad s_2(3P(n))=s_2(3n)+2,
\]
because \(3P(n)=4(3n)+3\). Therefore
\[
A(P(n))=A(n)+1,\qquad B(P(n))=B(n).
\]
Fix \(k\ge1\) and an allowed \(b\). If \(b=0\), choose \(n=z_k\). If \(b\ge2\) is even, set \(j=b/2+1\), so \(2\le j\le k\), and choose \(n=P^{\,k-j}(e_j)\). If \(b\ge3\) is odd, set \(j=(b+3)/2\), so \(3\le j\le k\), and choose \(n=P^{\,k-j}(o_j)\). Each choice has exactly \(A(n)=k\) and \(B(n)=b\). Finally, replacing any such \(n\) by \(2^h n\), for any integer \(h\ge0\), leaves both digit sums, hence both valuations, unchanged; these are distinct positive integers. All assertions follow. \(\square\)

## Verification
The standalone program `verify.py` independently compares \(A(n)\) and \(B(n)\) with exact integer-binomial computations for \(1\le n\le1200\), checks binary-carry counts for the same range, scans every \(1\le n<2^{17}\) for impossible values, and verifies every constructive \((k,b)\) pair for \(1\le k\le60\), including all resulting shifts by \(2^{13}\). In the scan it confirms the full predicted fibers for \(1\le k\le9\). Run with `python verify.py`; no third-party dependencies are required. These finite checks test the implementation and proof examples; the four-step argument proves the infinite assertions independently of their bounded extent.

## Relationship to prior work
Kummer's carry theorem and Legendre's formula are classical. Sun's 2010 analysis of central binomial divisibility includes both binomial families but addresses different global divisibility statements. Heuberger, Krenn and Kropf (2016) implement a binary multiplication-by-three transducer for different nonadjacent-form digit problems. Drmota and Krattenthaler (2018) establish joint *asymptotic* sum-of-digits results; such results do not determine exact support within each fixed \(A(n)\)-fiber. The classification here establishes the complete *joint valuation support* and explicit infinite witnesses, not an asymptotic count or a consequence of a marginal distribution. Earlier literature on binary-weight products may contain related restrictions, and absence of located equivalent wording is not a mathematical proof of novelty.

## Limitations
The theorem does not determine the number of indices realizing any particular pair in a finite interval, their limiting frequencies, or analogous joint spectra for other primes and other binomial multipliers. Generalizing the classification may require different carry-transition arguments. Novelty has not been independently certified, and unlocated specialist literature remains a residual risk.

## References
1. E. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen* (1852), classical theorem relating binomial valuations to carries.
2. Z.-W. Sun, *Products and sums divisible by central binomial coefficients*, arXiv:1004.4623 (first posted 2010-04-26), https://arxiv.org/abs/1004.4623.
3. C. Heuberger, D. Krenn and S. Kropf, *Automata in SageMath—Combinatorics meets Theoretical Computer Science*, arXiv:1404.7458, https://arxiv.org/abs/1404.7458.
4. M. Drmota and C. Krattenthaler, *A Joint Central Limit Theorem for the Sum-of-Digits Function, and Asymptotic Divisibility of Catalan-like Sequences*, arXiv:1803.02178, https://arxiv.org/abs/1803.02178.
5. H. Kaneko and T. Stoll, *Products of integers with few nonzero digits*, arXiv:2112.03077, https://arxiv.org/abs/2112.03077.
