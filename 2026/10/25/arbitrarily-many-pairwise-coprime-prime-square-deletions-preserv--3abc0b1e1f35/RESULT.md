# Arbitrarily many pairwise-coprime prime-square deletions preserving sums of two squares

## Finding
Let \(\mathcal S=\{n^2:n\in\mathbb Z_{\ge0}\}\). There is an infinite strictly increasing sequence of primes \(p_1,p_2,\ldots\), with each \(p_i\equiv1\pmod4\), such that for every integer \(k\ge1\),
\[
\left(\mathcal S\setminus\{p_1^2,\ldots,p_k^2\}\right)+\mathcal S=\mathcal S+\mathcal S.
\]
Consequently the number of deletions from the first square summand can be arbitrarily large while their distinct prime square roots have no common prime factor.

## Assumptions and scope
All additive sums are sets of ordinary nonnegative integers; representations allow zero and repeated coordinates. The square-root primes are distinct positive primes \(1\pmod4\). This asserts the existence of infinite sequences, not that every choice of such primes works. No bound on the growth of the constructed primes is asserted.

## Proof
For an integer \(n\ge0\), let \(R(n)\) be the set of unordered pairs \(\{a,b\}\) of nonnegative integers with \(a^2+b^2=n\). If we delete a finite root set \(U\) from the first factor, a representation of \(n\) survives exactly when at least one pair in \(R(n)\) has an entry outside \(U\): choose that entry in the first factor. Thus a loss is possible only if every pair in \(R(n)\) is contained in \(U\).

First take \(p_1=5\). Inductively suppose distinct primes \(p_1<\cdots<p_{i-1}\), each \(1\pmod4\), have been selected. For every \(j<i\), choose *two new, mutually distinct auxiliary primes* \(\ell_{ij},m_{ij}\equiv1\pmod4\), different from all previously selected primes and from all other auxiliaries at the current stage. Since \(-1\) is a nonzero quadratic residue modulo each auxiliary prime, Hensel lifting yields units \(a_{ij}\), \(b_{ij}\) satisfying
\[
a_{ij}^2+p_j^2\equiv0\pmod{\ell_{ij}^2},\qquad
b_{ij}^2+p_j^2\equiv0\pmod{m_{ij}^2}.
\]
By the Chinese remainder theorem there is a residue class \(c\) modulo \(M=4\prod_{j<i}\ell_{ij}^2m_{ij}^2\) satisfying \(c\equiv1\pmod4\), \(c\equiv a_{ij}\pmod{\ell_{ij}^2}\), and \(c\equiv b_{ij}\pmod{m_{ij}^2}\). All its residues are units, so \(\gcd(c,M)=1\). Dirichlet's theorem supplies arbitrarily large primes \(p_i\equiv c\pmod M\); choose one with \(p_i^2>2p_{i-1}^2\). We have thereby ensured
\[
\ell_{ij}^2m_{ij}^2\mid p_i^2+p_j^2\qquad(j<i).
\]

These primes have **distinct unordered pair sums of squares**: for each fixed greatest index \(i\), the values \(p_i^2+p_j^2\), \(j\le i\), are distinct; each exceeds every pair sum from smaller greatest indices, because \(p_i^2>2p_{i-1}^2\). This property holds for every finite prefix \(U=\{p_1,\ldots,p_k\}\).

We now show each unordered pair \(\{p_i,p_j\}\) from \(U\) has at least one *other* nonnegative unordered two-square representation of its sum. For \(i\ne j\), the number \(n=p_i^2+p_j^2\) has two different prime factors \(\ell_{ij}\) and \(m_{ij}\), both \(1\pmod4\), each with valuation at least two. Jacobi's exact representation formula gives
\[
r_2(n)=4\prod_{q\mid n,\ q\equiv1\pmod4}(\nu_q(n)+1)\ge4\cdot3\cdot3=36,
\]
where \(r_2(n)\) counts all ordered, signed integer solutions. The prescribed unordered positive unequal pair accounts for only eight of these. Thus there is another unordered nonnegative pair.

For \(i=j\), \(n=2p_i^2\) has \(r_2(n)=4(2+1)=12\). The prescribed diagonal pair \(\{p_i,p_i\}\) accounts for only four signed ordered representations, so again another pair exists. Any such second pair cannot lie wholly inside \(U\), because the square sums of pairs of members of \(U\) are distinct. It therefore survives when the squares of members of \(U\) are removed from the first factor.

Every \(n\in\mathcal S+\mathcal S\) with a representation not using two roots from \(U\) survives automatically; those with a pair entirely inside \(U\) survive by the preceding argument. The reverse inclusion is trivial. Since Dirichlet gives infinitely many choices of \(p_i\) at every stage, there are infinitely many such increasing tuples for any given length \(k\), and an infinite sequence follows inductively. \(\square\)

## Verification
The accompanying standalone program `verify.py` exactly checks an explicit three-prime example \(U=\{5,37,89\}\): it independently computes all two-square representations up to the largest deleted-root pair sum and confirms preservation of the full sumset. For larger values the proof uses Dirichlet's theorem, quadratic Hensel lifting and Jacobi's formula, not finite experimentation.

## Relationship to prior work
Elsholtz and Stadlmann, Theorem 2(1), construct decompositions by deleting squares of roots all divisible by *one fixed prime* \(p\equiv1\pmod4\); their theorem therefore cannot supply a deleted set containing two different prime-square roots. Their Theorem 1 is an asymptotic restriction, not a simultaneous coprime-deletion existence result. A separate earlier exact two-hole classification covers only two individual deletions and does not imply unbounded prime-support size. The present construction makes the number of pairwise-coprime prime roots arbitrarily large. Its proof invokes classical Hensel/CRT/Dirichlet machinery and Jacobi's two-square formula.

## Limitations
No growth rate or effective upper bound is obtained for the prime sequence. The result does not classify all permissible finite root sets or prove that arbitrary finite prime sets are removable. The characterization may be implicit in general representation-theoretic literature not indexed under these terms. The theorem has received a self-review but no independent mathematical audit.

## References
- C. Elsholtz and J. Stadlmann, *The Large Sieve Inequality and Additive decompositions of sums of squares*, arXiv:2610.20554v1, first posted 2026-10-14, Sections 1.1 and 4.1, https://arxiv.org/html/2610.20554v1.
- Classical two-squares representation formula of Jacobi, \(r_2(n)=4(d_1(n)-d_3(n))\); see Hardy and Wright, *An Introduction to the Theory of Numbers*, treatment of sums of two squares.
- Dirichlet's theorem on primes in arithmetic progressions and Hensel's lemma (standard forms).
