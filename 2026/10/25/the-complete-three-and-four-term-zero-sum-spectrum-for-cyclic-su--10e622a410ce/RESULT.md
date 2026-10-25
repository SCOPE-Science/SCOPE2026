# The complete three- and four-term zero-sum spectrum for cyclic subgroups of order eleven

## Finding
For a prime \(p\) and an integer \(q\) satisfying \(\operatorname{ord}_p(q)=11\), let \(m(q,p)\) be the smallest positive integer \(t\) for which some nonnegative integers \(a_1,\ldots,a_t\), allowing repetition, satisfy
\[
q^{a_1}+\cdots+q^{a_t}\equiv0\pmod p.
\]
Then the following are exact, uniform in the choice of the order-eleven generator \(q\):
\[
\begin{aligned}
m(q,p)=3&\iff p\in\{23,683\},\\
m(q,p)=4&\iff p\in\{67,89,419,661,991\},\\
m(q,p)\ge5&\iff p\notin\{23,67,89,419,661,683,991\}.
\end{aligned}
\]
The third equivalence is relative to the standing hypothesis \(\operatorname{ord}_p(q)=11\). In particular, the theorem classifies **all** order-eleven subgroups containing an additive zero of length at most four; it does not assert the exact minimum at other primes.

## Assumptions and scope
Every prime under consideration satisfies \(p\equiv1\pmod{11}\). The base \(q\) can be any integer whose reduction has multiplicative order exactly eleven, so \(q\) need not be a primitive generator of the entire nonzero field. Repeated summands are allowed. Exponents can be reduced modulo eleven. The minimum depends only on the order-eleven subgroup, since all its generators have the same set of powers.

## Proof
Write \(\Phi_{11}(X)=1+X+\cdots+X^{10}\), and for a multiset of exponents \(J=(j_1,\ldots,j_t)\), with \(0\le j_1\le\cdots\le j_t\le10\), put \(f_J(X)=\sum_{s=1}^{t}X^{j_s}\). Define the positive integral absolute norm
\[
N(J)=\left|\operatorname{Res}_X(\Phi_{11}(X),f_J(X))\right|.
\]
We first prove the **norm criterion**: for each prime \(p\equiv1\pmod{11}\) and each \(t\), the order-eleven subgroup has a vanishing \(t\)-term sum if and only if \(p\mid N(J)\) for some \(t\)-element multiset \(J\). Indeed, \(\Phi_{11}\) splits over \(\mathbb F_p\) as the product of the eleven-th roots other than one, all simple. Reduction of the integral resultant vanishes precisely if \(f_J\) vanishes at one such root. Each such root is a power of any given \(q\) of order eleven, so replacing each exponent by an appropriate multiple gives a sum of powers of that particular \(q\). Conversely any vanishing sum yields a common root and a vanishing resultant modulo \(p\).

Two multisets \(J,J'\) are *affine equivalent* if the exponent multisets are related by \(j\mapsto aj+b\pmod{11}\) for some \(a\in\{1,\ldots,10\}\) and \(b\in\{0,\ldots,10\}\). Then \(N(J')=N(J)\): translation multiplies each cyclotomic conjugate by a root of unity of absolute norm one, while dilation merely permutes the ten conjugates. Hence it is enough to compute one norm for each affine orbit.

There are \(\binom{13}{3}=286\) multisets of size three and \(\binom{14}{4}=1001\) of size four. The complete orbit enumeration has exactly four and twelve orbits, respectively. Every orbit representative is the lexicographically smallest sorted tuple under the affine group. The following tables list **every** representative and its exact absolute cyclotomic norm:

| Three-term representative | \(N(J)\) |
|---|---:|
| \((0,0,0)\) | \(59049=3^{10}\) |
| \((0,0,1)\) | \(683\) |
| \((0,1,2)\) | \(1\) |
| \((0,1,3)\) | \(23\) |

| Four-term representative | \(N(J)\) |
|---|---:|
| \((0,0,0,0)\) | \(1048576=2^{20}\) |
| \((0,0,0,1)\) | \(44287=67\cdot661\) |
| \((0,0,1,1)\) | \(1024=2^{10}\) |
| \((0,0,1,2)\) | \(529=23^2\) |
| \((0,0,1,3)\) | \(991\) |
| \((0,0,1,5)\) | \(1541=23\cdot67\) |
| \((0,0,1,7)\) | \(419\) |
| \((0,0,1,10)\) | \(1\) |
| \((0,1,2,3)\) | \(1\) |
| \((0,1,2,4)\) | \(23\) |
| \((0,1,2,5)\) | \(89\) |
| \((0,1,3,4)\) | \(1\) |

These are exact integer certificates: in the ring \(\mathbb Z[X]/(\Phi_{11})\), multiplication by \(f_J\) is a ten-by-ten integer matrix. Form its columns by reducing \(X^{j_s+k}\) using \(X^{11}=1\) and \(X^{10}=-(1+\cdots+X^9)\). Its determinant has absolute value \(N(J)\). The accompanying standalone program calculates these determinants using exact division and independently enumerates every affine orbit. Thus each entry, its integrality, and the exhaustiveness of the sixteen rows are directly reproducible without heuristic search or floating-point arithmetic.

Every admissible prime \(p\) is \(1\pmod{11}\). In the three-term table the only such prime divisors are \(23\) and \(683\). In the four-term table the complete corresponding set is \(\{23,67,89,419,661,991\}\). By the norm criterion, these are respectively exactly the primes permitting three and four summands. One summand cannot vanish modulo \(p\), and two cannot, because \(q^{a-b}=-1\) would give an element of order two in an odd-order subgroup. Removing the primes already admitting three summands gives exactly the asserted minimum-four set. This completes the proof.

## Verification
The bundled `verify_eleven.py` uses only Python's standard library. Running `python verify_eleven.py` rebuilds all \(1287\) exponent multisets, normalizes them under all \(110\) affine transformations, checks the complete sixteen-row norm table through exact integer determinants, trial-factors those sixteen norms, and checks direct modular zero-sum witnesses for each exceptional prime. All checks passed. For example, the order-eleven elements \(q=4\) modulo \(683\) satisfy \(1+1+4^6\equiv0\pmod{683}\), and \(q=9\) modulo \(661\) satisfy \(1+1+1+9^6\equiv0\pmod{661}\). The finite enumeration here is an **exhaustive symbolic certificate** of the sixteen orbit classes, not an extrapolation from tested primes; the norm criterion extends it to every prime.

## Relationship to prior work
Jacob and Külshammer (2022) introduce the invariant, prove a general bound, and derive finite-exception principles. Their Proposition 15 gives a complete order-seven classification, whereas Example 16(i) for order eleven **already reports** the length-three instance at \(p=23\), and the length-four instances at \(p=67\) and \(p=89\), together with some longer-length examples. This work does not claim those three instances as new: its additional content is the complete if-and-only-if order-eleven classification, including \(p=683\), \(p=419\), \(p=661\), and \(p=991\), using exact cyclotomic-norm certificates.

The earlier Breuer–Héthelyi–Horváth–Külshammer work develops the invariant and tabulates individual cases; general algorithms for determining one fixed \(m(q,p)\) do not by themselves state this uniform exceptional-prime spectrum. Work on vanishing sums of roots of unity supplies related cyclotomic methods, but cancellation in characteristic zero is distinct from reduction modulo an exceptional prime.

## Limitations
The theorem classifies precisely the cases \(m(q,p)\le4\) at multiplicative order eleven; it does **not** give the precise value \(m(q,p)\) when the minimum is at least five, nor does it classify prime-power moduli \(p^k\) with \(k>1\) or other multiplicative orders. Exhaustiveness refers to the sixteen exact integer-norm orbit classes, not to testing every prime. Originality outside the inspected available primary literature remains subject to unindexed and inaccessible antecedents.

## References
1. L. Jacob and B. Külshammer, *Congruences for sums of powers of an integer*, arXiv:2204.09403v1 (first public 2022-04-20), https://arxiv.org/pdf/2204.09403 (especially Proposition 11, Proposition 15, and Example 16(i)).
2. T. Breuer, L. Héthelyi, E. Horváth and B. Külshammer, *The Loewy structure of certain fixpoint algebras, Part II*, International Electronic Journal of Algebra **30** (2021), 16–65.
3. T. Y. Lam and K. H. Leung, *On vanishing sums of roots of unity*, Journal of Algebra **224** (2000), 91–109, arXiv:math/9511209.
4. T. Y. Lam and K. H. Leung, *Vanishing sums of mth roots of unity in finite fields*, Finite Fields and Their Applications (1996), DOI:10.1006/ffta.1996.0025 (abstract consulted; full text not inspected).
5. R. Dvornicich and U. Zannier, *Sums of roots of unity vanishing modulo a prime* (2002), DOI:10.1007/s00013-002-8291-4 (metadata consulted; full text not inspected).
