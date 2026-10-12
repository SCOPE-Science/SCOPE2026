# The complete first multiplicity layer of four-layered numbers
## Finding
Let \(\Omega(n)\) count prime factors with multiplicity. An integer \(n\ge2\) is *four-layered* if its positive divisors admit a partition into four disjoint sets of equal integer sum. Then
\[
\boxed{\Omega(n)\ge8\quad\text{for every four-layered }n,}
\]
and the complete equality fiber is
\[
\boxed{\{n:\ n\text{ is four-layered},\ \Omega(n)=8\}
=\{27720,32760,120120,180180,235620\}.}
\]
More strongly, the same five integers are **all** integers \(n\ge2\) with \(\Omega(n)\le8\) and \(\sigma(n)\ge4n\), where \(\sigma(n)=\sum_{d\mid n}d\). Thus the necessary four-abundancy condition is sufficient throughout this first multiplicity layer.

## Assumptions and scope
All divisors and primes are positive. In a factorization \(n=\prod_{i=1}^r p_i^{a_i}\) with \(p_1<\cdots<p_r\) and \(a_i\ge1\), \(\Omega(n)=\sum_i a_i\), and
\[
I(n):=\frac{\sigma(n)}n
=\prod_{i=1}^r\left(1+\frac1{p_i}+\cdots+\frac1{p_i^{a_i}}\right).
\]
Four-layeredness implies \(\sigma(n)\ge4n\), since one of the four equally weighted divisor parts contains \(n\). The stronger exact four-abundant enumeration below concerns \(I(n)\ge4\), **not** the narrower equation \(I(n)=4\).

## Proof
**1. An unbounded-prime pruning lemma.** For a prime \(p\) and exponent \(a\ge1\), put
\[
A_a(p)=\sum_{j=0}^a p^{-j}=\frac{p^{a+1}-1}{p^a(p-1)}<\frac p{p-1}.
\]
Let \(q_1<\cdots<q_m\) be the first \(m\) primes strictly larger than a specified prime \(P\), and set
\[
E(P,m)=\prod_{j=1}^m\frac{q_j}{q_j-1},\qquad E(P,0)=1.
\]
For any prime-factorization prefix consisting of primes at most \(P\), with current abundancy \(R\) and \(m\) **remaining prime factors counted with multiplicity**, every completion has abundancy at most \(R E(P,m)\). Indeed, it uses at most \(m\) new distinct primes; writing them in increasing order, its \(j\)-th prime is at least \(q_j\), and every local factor is strictly smaller than the corresponding Euler factor. Consequently, a prefix with \(R E(P,m)<4\) cannot extend to a four-abundant number.

If the next chosen prime is \(p>P\) and \(m\ge1\), a uniform bound for every exponent of that prime and every subsequent extension is
\[
R\frac p{p-1}E(p,m-1).
\]
This bound is strictly decreasing as \(p\) increases, so once it falls below \(4\), **all larger** choices of the next prime are excluded. The genuine local ratio after choosing exponent \(a\) is \(R A_a(p)\); recurse only if \(R A_a(p)E(p,m-a)\ge4\).

**2. A finite exhaustive search without any numerical cutoff on the primes.** Enumerate multiplicities \(m=1,2,\ldots,8\) in order. Start each search with \(P=1\), \(R=1\), and \(m\) slots. Choose primes strictly increasingly and exponents \(1\le a\le m\), using exactly the pruning inequalities from Step 1; on exhausting the slots, retain exactly those products with \(R\ge4\). This visits every canonical factorization once unless it is excluded by a mathematically valid strict upper bound. The search loops terminate: when searching total multiplicity \(m\), every proper prime-factorization prefix has multiplicity less than \(m\) and, by the already completed smaller-multiplicity searches, abundancy below \(4\). Hence the next-prime bound tends to that prefix abundancy, strictly below \(4\), as the candidate prime tends to infinity.

The complete exact-rational enumeration gives no four-abundant numbers for multiplicities \(1\) through \(7\). For multiplicity \(8\), there are \(33\) visited recursion nodes and \(58\) candidate-prime tests (the largest tested prime is \(19\)), and exactly five survivors:
\[
\begin{array}{r|l|c}
n&\text{prime factorization}&I(n)\\\hline
27720&2^3\cdot3^2\cdot5\cdot7\cdot11&312/77\\
32760&2^3\cdot3^2\cdot5\cdot7\cdot13&4\\
120120&2^3\cdot3\cdot5\cdot7\cdot11\cdot13&576/143\\
180180&2^2\cdot3^2\cdot5\cdot7\cdot11\cdot13&224/55\\
235620&2^2\cdot3^2\cdot5\cdot7\cdot11\cdot17&3744/935
\end{array}
\]
This exact search is independently re-executable via `python3 verify.py`, using Python's integer arithmetic and `fractions.Fraction`. The bound proves global exhaustion; the largest tested prime \(19\) is an *output* of pruning, not an unproved input cutoff.

**3. Four-partition certificates.** The accompanying `partitions.json` gives four disjoint integer lists for each survivor. The standard-library verifier independently reconstructs the full divisor set from the prime factorization, compares its sorted elements with the union of the four lists, and checks that each list sums to \(\sigma(n)/4\). The five respective common sums are
\[
28080,\quad32760,\quad120960,\quad183456,\quad235872.
\]
Thus **each** of the five four-abundant survivors is four-layered. Combined with the necessary condition and the exhaustive classification in Step 2, this proves both boxed statements.

## Verification
Extract `verify.py` and `partitions.json` into the same directory and run `python3 verify.py` with Python 3. The script uses only the standard library and prints a `PARTITION_OK` line for each of the five integers and a final `EXHAUSTIVE_SEARCH_OK` line. The exact output of the executed version is in `verification_output.txt`. The certificate lists are explicit integers, checked against the divisor multiset and equal sums; their original discovery method is not needed for verification. A separately implemented finite sieve through \(300000\) reproduced the same five integers, but the global proof depends on the exact pruning bounds, not on that bounded regression.

## Relationship to prior work
Mahanta, Saikia, and Yaqubi introduce systematic characterizations of \(k\)-layered numbers, including low prime-support exclusions. Jokar explicitly finds \(27720\) as the smallest **numerical** four-layered integer and classifies a restricted family with four distinct prime supports; neither assertion classifies the smallest **total prime-factor multiplicity** or its full fiber. OEIS A204831 lists the first \(31\) four-layered integers and includes four of the five integers above but ends below \(235620\). OEIS A023198 lists four-abundant integers, and A392936 lists primitive four-abundant integers including \(235620\); neither is an unbounded classification by \(\Omega\).

A separately published exact boundary theorem for **quadriperfect** numbers \(\sigma(n)=4n\) identifies \(32760\) as the unique example with \(\Omega(n)=8\). The present theorem covers \(\sigma(n)\ge4n\) and certifies four additional strict-inequality examples; the previous equality theorem and its accompanying verifier filter explicitly for \(I(n)=4\), so do not imply this statement or its divisor-partition certificates. The strict-inequality distinction matters.

## Limitations
No classification is claimed for \(\Omega(n)\ge9\), for general four-abundant numbers, or for arbitrary \(k\)-layered numbers. The inference from the exact rational recursion requires the pruning lemma and its induction-based termination argument; the short program output alone would not establish an infinite search result. Published sequence lists may contain the displayed examples without proving global exhaustion. Earlier or unindexed treatments of the same multiplicity boundary remain a residual literature risk. This is a mathematical claim with a reproducible finite certificate, not an independent external audit.

## References
1. P. J. Mahanta, M. P. Saikia, D. Yaqubi, "Some properties of Zumkeller numbers and \(k\)-layered numbers," arXiv:2008.11096v1, publicly submitted 2020-08-07, DOI 10.1016/j.jnt.2020.05.003; primary MSC 11A25.
2. F. Jokar, "On \(k\)-layered numbers," arXiv:2207.09053v1, publicly submitted 2022-07-19; primary MSC 11A25.
3. OEIS Foundation, A204831, "Numbers whose divisors can be partitioned into four disjoint sets of equal sum"; A023198, "4-abundant numbers"; A392936, "Primitive 4-abundant numbers".
4. "The first multiplicity layer of quadriperfect numbers," published mathematical research record ending `4f417ab1f93c` (exact equation \(\sigma(n)=4n\)).
