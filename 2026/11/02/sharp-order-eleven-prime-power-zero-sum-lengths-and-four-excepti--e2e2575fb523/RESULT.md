# Sharp order-eleven prime-power zero-sum lengths and four exceptional primes

## Finding

For a positive integer \(e\) and a unit \(q\) modulo \(e\), define \(m(q,e)\) to be the least positive integer \(t\) for which there are nonnegative exponents \(a_1,\ldots,a_t\) satisfying
\[
q^{a_1}+\cdots+q^{a_t}\equiv0\pmod e.
\]
Let \(p\) be any prime with \(p\equiv1\pmod{11}\), let \(k\ge2\), and let \(q\) have multiplicative order **exactly eleven** modulo \(p^k\). Then the following is the complete classification:
\[
 m(q,p^k)=
 \begin{cases}
 5,&p=23,\ k=2,\\
 9,&p=23,\ k\in\{3,4\},\\
 8,&p=67,\ k=2,\\
 9,&p\in\{89,683\},\ k=2,\\
 11,&\text{in every other case}.
 \end{cases}
\]
Thus the only primes for which the order-eleven subgroup has a zero-sum of length less than eleven modulo the prime square are \(23,67,89,683\). The uniform stabilization depth \(k=5\) is **best possible**: every such subgroup has least zero-sum length eleven for \(k\ge5\), while \(p=23\) still has least length nine at \(k=4\).

## Assumptions and scope

The modulus is a prime power with prime \(p\equiv1\pmod{11}\), exponent \(k\ge2\), and \(q\) is any element of exact order eleven in the unit group. All repetitions of powers are allowed, so this is the minimal length of a zero-sum *multiset* drawn from the order-eleven subgroup; it is not the minimal size of a zero-sum subset with distinct elements. Every order-eleven generator gives the same answer because its eleven powers form the same subgroup. The classification says nothing about \(k=1\), orders different from eleven, or arbitrary non-prime-power moduli.

## Proof

### Step 1: Universal upper bound and generator invariance

The subgroup \(H\) of order eleven is unique in the cyclic group \((\mathbb Z/p^k\mathbb Z)^\times\). Thus all elements \(q\) of exact order eleven enumerate precisely its eleven elements \(1,q,\ldots,q^{10}\). Because \(q\not\equiv1\pmod p\), the factor \(q-1\) is invertible modulo \(p^k\). The geometric series therefore gives
\[
1+q+\cdots+q^{10}=\frac{q^{11}-1}{q-1}\equiv0\pmod{p^k},
\]
so \(m(q,p^k)\le11\). For each fixed \(p\), reduction of the unique order-eleven subgroup from level \(k+1\) to level \(k\) preserves the subgroup and implies that the minimum is nondecreasing with \(k\).

### Step 2: An unconditional finite cutoff

If there is a zero sum with \(1\le t\le10\), reduce each exponent modulo eleven and form
\[
g(X)=\sum_{j=0}^{10}c_jX^j\in\mathbb Z[X],\qquad c_j\ge0,\quad\sum_{j=0}^{10}c_j=t.
\]
Then \(g(q)\equiv0\pmod{p^k}\). Let \(\Phi_{11}(X)=1+X+\cdots+X^{10}\). This is irreducible over \(\mathbb Q\). Since \(\deg g\le10\), the condition \(\Phi_{11}\mid g\) would imply \(g=c\Phi_{11}\) with constant coefficient \(c\in\mathbb Z\), forcing \(t=11c\), impossible for \(1\le t\le10\). Thus the integer resultant \(R=\operatorname{Res}(\Phi_{11},g)\) is nonzero.

For a complex primitive eleventh root \(\zeta\), the standard product formula and triangle inequality give
\[
 1\le |R|=\left|\prod_{a=1}^{10}g(\zeta^a)\right|\le t^{10}\le10^{10}.
\]
The integral resultant Bézout identity provides \(A,B\in\mathbb Z[X]\) with
\[
 A(X)\Phi_{11}(X)+B(X)g(X)=R.
\]
Since \(q\) has order eleven modulo \(p^k\) and \(q-1\) is a unit, \(\Phi_{11}(q)\equiv0\pmod{p^k}\). Evaluating the identity at \(q\) yields \(p^k\mid R\). In particular \(p^2\le10^{10}\), hence \(p\le100000\). **No prime exceeding 100000 can support a shorter zero-sum at any level \(k\ge2\).** This step makes the subsequent finite computation an exhaustive proof, not an empirical cutoff.

### Step 3: Exact finite certificate at prime squares

The accompanying standalone C++17 source `verify.cpp` performs the following mathematically exhaustive operation. It sieves all primes through \(100000\), filters \(p\equiv1\pmod{11}\) (exactly \(945\) primes), constructs one nontrivial order-eleven root modulo each \(p\) by testing \(x^{11}\equiv1\pmod p\), and uniquely lifts that root to \(p^2\) using the simple-root Hensel correction for \(X^{11}-1\). It independently checks the root order and enumerates **every** nonzero weak eleven-composition of total mass at most ten:
\[
\#\{(c_0,\ldots,c_{10}):c_j\ge0,\ 1\le\textstyle\sum c_j\le10\}
=\binom{21}{11}-1=352715.
\]
Each vector is evaluated modulo \(p^2\) using exact integer arithmetic, and the minimum \(t\) of those producing zero is recorded (default eleven). The complete outcome is
\[
\begin{array}{c|ccccc}
 p &23&67&89&683&\text{every other eligible }p\le100000\\\hline
 m(q,p^2)&5&8&9&9&11
\end{array}.
\]
By Step 2 this table is exhaustive for **all** primes, not just the tested range. All operations use integer arithmetic, no statistical sampling and no floating-point tolerances.

For a checkable explicit example missing from the motivating paper, at \(p=683\) the integer \(q=383167\) has order eleven modulo \(683^2=466489\); the nine-term sum
\[
3q^4+4q^8+q^9+q^{10}\equiv0\pmod{466489}.
\]
The exhaustive certificate also proves that no shorter sum is possible.

### Step 4: Every higher prime-power level

For primes not in \(\{23,67,89,683\}\), Step 3 gives minimum eleven already modulo \(p^2\), so monotonicity and the upper bound give minimum eleven at all higher levels. For the three exceptional primes \(67,89,683\), the same exhaustive enumeration at \(p^3\) gives minimum eleven. For \(p=23\), the exhaustive values at \(p^3,p^4,p^5\) are respectively \(9,9,11\); a direct witness at \(p^4=279841\) is \(q=133034\) and
\[
4q^4+q^5+q^6+2q^9+q^{10}\equiv0\pmod{279841}.
\]
Each deeper modulus is examined over all \(352715\) coefficient vectors. Monotonicity then handles every untested higher exponent. This completes the classification and proves that five is the sharp uniform stabilization depth.

## Verification

Compile and execute the self-contained exact-arithmetic certificate in the same directory:

```sh
c++ -O2 -std=c++17 verify.cpp -o verify
./verify
```

The expected and observed output is:

```text
VERIFY_OK primes=945 vectors_per_prime=352715 exceptions=23,67,89,683 deeper_checks=6
```

The verifier directly checks all \(945\) eligible prime-square moduli and all \(6\) deeper cases (\(23\) at exponents \(3,4,5\); \(67,89,683\) at exponent \(3\)). Its coverage is exhaustive **because** the resultant proof first bounds every possible prime. The finite program by itself does not prove the resultant inequality or the unbounded exponent reduction; these are mathematical parts of the proof above.

## Relationship to prior work

Jacob and Külshammer, *Congruences for sums of powers of an integer*, arXiv:2204.09403v1 (20 April 2022), defines \(m(q,e)\), gives general finiteness and stabilization results (Proposition 10 and Corollary 13), and classifies the prime orders five and seven (Propositions 14–15). Its Example 16(i) reports selected order-eleven rows for primes \(23,67,89,199,353,397\), including the exceptional persistence at \(23\). It does **not** supply a complete order-eleven prime-power classification or name the additional prime \(683\), and it explicitly requests bounds on the stabilization depth. The older Breuer–Héthelyi–Horváth–Külshammer treatment gives foundational results on the same minimum-length invariant. The argument here specializes the general resultant finiteness idea to an explicit uniform cutoff and completes the finite order-eleven classification with a reproducible certificate.

## Limitations

The proof has an essential, but fully finite and exactly specified, exhaustive-computation component. Independent human verification and formal machine certification have not been performed. The stated upper bound \(100000\) is a proof cutoff, not an optimized analytic bound. Although searches found no earlier complete result, an unindexed or implicit earlier classification could affect publication priority. No claim is made for order eleven modulo primes \(p\not\equiv1\pmod{11}\), for arbitrary units without exact order eleven, or for other subgroup orders.

## References

1. L. Jacob and B. Külshammer, *Congruences for sums of powers of an integer*, arXiv:2204.09403v1, 20 April 2022, https://arxiv.org/abs/2204.09403.
2. T. Breuer, L. Héthelyi, E. Horváth and B. Külshammer, *The Loewy structure of certain fixpoint algebras, Part II*, preprint arXiv:1912.03065v1, 6 December 2019, https://arxiv.org/abs/1912.03065.
3. T. Y. Lam and K. H. Leung, *On vanishing sums of roots of unity*, Journal of Algebra 224 (2000), 91–109, background on nonvanishing short cyclotomic sums.
