# The exact conductor \(a(7)=19{,}027{,}139\) for seven-prime subset sums

## Finding

Let \(\mathcal P_7\) be the set of positive integers of the form \(p_1p_2\cdots p_7\), where \(p_1<\cdots<p_7\) are distinct rational primes. Define
\[
\mathcal R_7=\left\{\sum_{c\in E}c:E\subseteq\mathcal P_7\text{ is finite}\right\}.
\]
Each possible summand can be selected **at most once**. The exact largest nonrepresentable integer is
\[
\boxed{\max(\mathbb Z_{\geq0}\setminus\mathcal R_7)=19{,}027{,}139.}
\]
Equivalently, \(19{,}027{,}139\notin\mathcal R_7\) and every integer \(n\geq19{,}027{,}140\) belongs to \(\mathcal R_7\). This determines the seventh term in the sequence of exact conductors \(a(k)\) proposed by Butler, Erdős, and Graham.

## Assumptions and scope

Primes are positive rational primes, and products are **squarefree** with exactly seven distinct prime factors. The summands in a representation must be pairwise distinct; no repetitions are permitted. Empty sums represent zero. No hypothesis about prime gaps beyond Bertrand's postulate is used. This result is solely about integer subset sums, not representations by reciprocal denominators or products allowing repeated prime factors.

For the increasing enumeration \(c_1<c_2<\cdots\) of \(\mathcal P_7\), put
\[
\mathcal R_j=\left\{\sum_{i=1}^{j}\varepsilon_i c_i:\varepsilon_i\in\{0,1\}\right\}.
\]

## Proof

**Step 1: exact finite base.** Define \(B=40{,}000{,}000\) and use the first \(N=3100\) elements of \(\mathcal P_7\). Exact enumeration of squarefree integers with seven distinct prime factors yields
\[
 c_1=510{,}510,\quad
 c_{3100}=19{,}111{,}638,\quad
 c_{3101}=19{,}114{,}095.
\]
A deterministic, exhaustive zero-one subset-sum computation establishes
\[
19{,}027{,}139\notin\mathcal R_{3100},\qquad
[19{,}027{,}140,40{,}000{,}000]\cap\mathbb Z
\subseteq\mathcal R_{3100}.
\]
This is not an extrapolation from tested examples: the computation constructs the entire \(40{,}000{,}001\)-bit reachability vector. With \(T_0=\{0\}\) and \(T_j=T_{j-1}\cup(c_j+T_{j-1})\), its recurrence computes exactly all sums with each of the first \(j\) summands used zero or one times. The accompanying implementations enumerate the complete finite prime-product set by two different algorithms and evaluate this recurrence using independent bit representations. Their actual outputs are recorded in `certificate.json`.

Since \(c_{3100}>19{,}027{,}139\), every permitted summand outside the first 3100 is also larger than \(19{,}027{,}139\). The verified nonrepresentability therefore persists for the full infinite set \(\mathcal R_7\).

**Step 2: consecutive permitted products grow by less than a factor of two.** Let \(c_j=p_1\cdots p_7\) with \(p_1<\cdots<p_7\), and let \(q\) be the next prime after \(p_7\). Bertrand's postulate gives \(p_7<q<2p_7\), so
\[
c_j < \frac{q}{p_7}c_j <2c_j,
\]
and the middle integer is again a product of seven distinct primes. Consequently
\[
\boxed{c_{j+1}<2c_j\quad\text{for every }j\geq1.}
\]
This uses the defining ordered sequence, not a conjecture about gaps between seven-almost-primes.

**Step 3: propagation to infinity.** Put \(L=19{,}027{,}140\). The finite computation provides \([L,B]\cap\mathbb Z\subseteq\mathcal R_{3100}\). Its cardinality is
\[
B-L+1=20{,}972{,}861\ \geq\ c_{3101}=19{,}114{,}095.
\]
Suppose, for some \(j\geq3100\), that \([L,U]\cap\mathbb Z\subseteq\mathcal R_j\) and its length \(W=U-L+1\) is at least \(c_{j+1}\). In \(\mathcal R_{j+1}\), we have both intervals \([L,U]\) and \([L+c_{j+1},U+c_{j+1}]\). They overlap or are adjacent because \(c_{j+1}\leq W\). Thus
\[
[L,U+c_{j+1}]\cap\mathbb Z\subseteq\mathcal R_{j+1}.
\]
The enlarged length is \(W+c_{j+1}\geq2c_{j+1}>c_{j+2}\), by Step 2; hence the induction continues indefinitely. Since the right endpoints diverge, all integers \(n\geq L\) are representable. Together with the nonrepresentability in Step 1 this proves the claimed exact conductor.

## Verification

Two runnable, self-contained verification programs are included: `verify_exact.cpp` and `verify_alternate.py`. Both enumerate precisely the first 3101 or more seven-prime products and implement the complete finite subset-sum recurrence up to \(B\). The C++ version uses a sieve for prime-divisor counts and a packed 64-bit-vector subset-sum dynamic program. The Python version generates products recursively from ascending prime tuples and uses Python's arbitrary-precision bit integers for the dynamic program. The independent methods agree on the three critical products, the largest missing sum, and the continuous represented interval.

With a C++17 compiler and Python 3, run:

```sh
c++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_exact.cpp -o verify_exact
./verify_exact
python3 verify_alternate.py
```

Each prints `VERIFY_OK` on success and exits unsuccessfully if an asserted property fails. The finite certificate is exact; the mathematical propagation step supplies the infinite conclusion.

## Relationship to prior work

Butler, Erdős, and Graham explicitly define subset sums of products of distinct primes in Section 2 and, on page 8, ask to determine the largest omitted integer \(a(k)\) for each \(k\). They report the six values
\[
a(1)=6,\ a(2)=23,\ a(3)=299,\ a(4)=3439,\ a(5)=51637,\ a(6)=894211,
\]
but do not state the value at \(k=7\). The theorem here answers that next exact instance rather than reproving the paper's general Egyptian-fraction representation theorem. A later proof by Li that all positive integers admit Egyptian fractions with distinct semiprime denominators addresses a different representation problem and does not determine this integer subset-sum conductor. Searches for alternative statements and databases did not locate a previously published seventh value; absence from searched sources is not an absolute uniqueness certificate.

## Limitations

The theorem is specific to \(k=7\). It does not determine \(a(k)\) for all \(k\), nor does it provide a closed-form formula for the sequence of conductors. The finite input is certified computationally through two reproducible exhaustive algorithms; no short handwritten evaluation of all \(40{,}000{,}001\) subset-sum bits is claimed. An overlooked equivalent prior computation or unindexed source remains a possible originality risk. Independent audit has not been performed.

## References

1. S. Butler, P. Erdős, and R. Graham, *Egyptian Fractions with Each Denominator Having Three Distinct Prime Divisors*, Integers 15 (2015), A51, Sections 2–3 and page 8. Open author-hosted full text: https://mathweb.ucsd.edu/~ronspubs/15_04_egyptian.pdf .
2. S. Li, *Every Natural Number Is a Sum of Distinct Semiprime Unit Fractions*, 2026 preprint, arXiv:2606.15159. https://arxiv.org/abs/2606.15159 . Used for comparison of distinct-denominator Egyptian-fraction problems, not as an input to the proof.
3. Bertrand's postulate (Chebyshev's theorem): for each prime \(p\), its successor is strictly less than \(2p\). A standard classical theorem used only in Step 2.
