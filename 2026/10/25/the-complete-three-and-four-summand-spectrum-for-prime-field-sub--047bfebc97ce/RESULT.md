# The complete three- and four-summand spectrum for prime-field subgroups of order thirteen

## Finding
Let \(p\) be prime, and let \(q\) be an integer whose residue has multiplicative order exactly \(13\) modulo \(p\). Write \(m(q,p)\) for the least positive integer \(t\) for which some \(t\) (not necessarily distinct) nonnegative powers of \(q\) have sum divisible by \(p\). Then
\[
 m(q,p)=
 \begin{cases}
 3,&p\in\{53,2731\},\\
 4,&p\in\{79,131,157,1327,2003,7229,398581\},\\
 \ge5,&\text{otherwise}.
 \end{cases}
\]
The trichotomy is independent of which generator of the unique order-\(13\) subgroup is chosen. In particular, it is a complete classification over *all* admissible primes, not a prime-range census.

## Assumptions and scope
The integers \(p\) and \(q\) are universally quantified as above. Necessarily \(p\equiv1\pmod{13}\), because the order of the multiplicative group of \(\mathbb F_p\) is \(p-1\). Conversely, every prime with this congruence has an order-\(13\) subgroup. Exponents in the definition of \(m\) are nonnegative integers and repetitions are permitted. The claim concerns prime moduli, not general composite moduli or higher prime powers.

## Proof
An order-\(13\) subgroup contains no element of order \(2\). A sum of one nonzero group element cannot vanish, and a zero sum of two would require their quotient to be \(-1\). Hence \(m(q,p)\ge3\).

Identify the exponents with \(\mathbb Z/13\mathbb Z\). For an exponent multiset \(E\) of cardinality \(t\), let \(P_E(X)=\sum_{e\in E}X^e\) with multiplicities. Each affine transformation \(e\mapsto ue+v\), with \(u\in(\mathbb Z/13\mathbb Z)^\times\) and \(v\in\mathbb Z/13\mathbb Z\), preserves **existence of a vanishing sum at some primitive thirteenth root**: translation by \(v\) multiplies the evaluated sum by a nonzero root-power, and rescaling by \(u\) permutes the primitive roots when the evaluation root is replaced by its \(u^{-1}\)-th power. This is an existential statement, not the generally false assertion that every multiplicative group automorphism preserves a fixed additive relation. It therefore suffices to consider one representative of each affine orbit of multisets.

Let \(\Phi_{13}(X)=1+X+\cdots+X^{12}\), and put
\[
 N_E=\left|\operatorname{Res}_X\bigl(\Phi_{13}(X),P_E(X)\bigr)\right|.
\]
For an admissible prime, \(\Phi_{13}\) splits into \(12\) distinct linear factors over \(\mathbb F_p\), whose roots are precisely the elements of order \(13\). Hence \(p\mid N_E\) if and only if \(P_E\) vanishes at one of those roots; after a change of exponent generator this is equivalent to a vanishing \(t\)-summand sum in the given subgroup.

Here is the **complete finite calculation**. Representatives are shown as sorted exponent multisets; the next columns give the size of their affine orbit and the absolute integral resultant. Repetition in a representative means repeated summands.

| \(t\) | Exponents | Orbit size | \(N_E\) |
|---:|:---|---:|---:|
|3|\((0,0,0)\)|13|\(3^{12}\)|
|3|\((0,0,1)\)|156|\(2731\)|
|3|\((0,1,2)\)|78|\(1\)|
|3|\((0,1,3)\)|156|\(53\)|
|3|\((0,1,4)\)|52|\(3^3\)|
|4|\((0,0,0,0)\)|13|\(2^{24}\)|
|4|\((0,0,0,1)\)|156|\(398581\)|
|4|\((0,0,1,1)\)|78|\(2^{12}\)|
|4|\((0,0,1,2)\)|156|\(2003\)|
|4|\((0,0,1,3)\)|156|\(53\cdot79\)|
|4|\((0,0,1,4)\)|156|\(1327\)|
|4|\((0,0,1,5)\)|156|\(3^3\cdot131\)|
|4|\((0,0,1,6)\)|156|\(7229\)|
|4|\((0,0,1,12)\)|78|\(1\)|
|4|\((0,1,2,3)\)|78|\(1\)|
|4|\((0,1,2,4)\)|156|\(79\)|
|4|\((0,1,2,5)\)|156|\(157\)|
|4|\((0,1,2,6)\)|156|\(53\)|
|4|\((0,1,3,4)\)|78|\(1\)|
|4|\((0,1,3,9)\)|52|\(3^6\)|
|4|\((0,1,3,11)\)|39|\(1\)|

This table is an exhaustive certificate rather than a sample: the orbit sizes sum to \(455=\binom{15}{3}\) for \(t=3\) and to \(1820=\binom{16}{4}\) for \(t=4\), exactly the numbers of three- and four-element multisets from thirteen residues. The accompanying stand-alone verifier constructs all multisets, generates each affine orbit, verifies disjoint coverage and the stated orbit sizes, computes every resultant as the exact determinant of multiplication by \(P_E\) in the rank-\(12\) ring \(\mathbb Z[X]/(\Phi_{13})\), and performs integral factorization. A separate symbolic resultant computation agreed on all \(21\) representatives.

The prime divisors congruent to \(1\pmod{13}\) in the \(t=3\) rows are exactly \(53,2731\). Those in the \(t=4\) rows are exactly \(53,79,131,157,1327,2003,7229,398581\). Every listed integer is prime, as can be verified by trial division to its integer square root. All these primes admit the stated vanishing sums, by the splitting-and-resultant equivalence proved above. Excluding the \(m=3\) primes from the four-summand list, and recalling \(m\ge3\), gives the asserted classification. \(\square\)

## Verification
Run `python3 verify_order13.py` with Python \(\ge3.8\) and no third-party packages. It constructs all \(455\) three-element and \(1820\) four-element exponent multisets and checks all affine orbits; computes \(21\) exact \(12\times12\) integer determinants by fraction-free Bareiss elimination; factors all determinants by exact integer trial division; and independently enumerates finite-field witnesses for the nine exceptional primes. A separately performed symbolic-resultant calculation agreed on all \(21\) norms. The script prints `PASS` only after all assertions succeed. The finite enumeration is exhaustive by the stated multiset counts; it does not extrapolate from a bounded set of primes.

## Relationship to prior work
Jacob and Külshammer, *Congruences for sums of powers of an integer* (arXiv:2204.09403, first posted 20 April 2022), define the same invariant, prove broad bounds and finiteness reductions, and in Example 16(ii) provide **examples** for order \(13\): \(p=53\) with \(m=3\), and \(p=79,131,157\) with \(m=4\). They do not there give the exhaustive short-sum prime spectrum. The new calculation proves completeness and exhibits the additional exceptional primes \(2731,1327,2003,7229,398581\). The antecedent work of Breuer, Héthelyi, Horváth and Külshammer (*The Loewy Structure of Certain Fixpoint Algebras, Part II*, arXiv:1912.03065, first posted 6 December 2019) supplies general finiteness and computation methods and tables for smaller instances; those methods motivate, but do not explicitly state, this list. This classification is not a result for general multiplicative orders or prime-power moduli.

## Limitations
The proof uses a fully specified finite integer certificate for the orbit and norm table, supported by an executable checker. It is not a by-hand derivation of every determinant. The result establishes exact values only when the minimum is at most four; the remaining primes are known only to have minimum at least five. Searches and inspections described in the accompanying review found no equivalent published classification, but implicit/unindexed antecedents and publication-priority uncertainty remain possible. Independent mathematical validation has not been performed.

## References
1. L. Jacob and B. Külshammer, *Congruences for sums of powers of an integer*, arXiv:2204.09403 (20 April 2022), particularly Introduction, Proposition 11, Corollary 13, and Example 16(ii). https://arxiv.org/abs/2204.09403
2. T. Breuer, L. Héthelyi, E. Horváth and B. Külshammer, *The Loewy Structure of Certain Fixpoint Algebras, Part II*, arXiv:1912.03065 (6 December 2019), Section 2, Example 2.21, and Tables 1–3. https://arxiv.org/abs/1912.03065
