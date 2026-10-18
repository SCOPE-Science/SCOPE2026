# Uniform part-frequency dominance from the fifth part

## Finding
For integers \(n\ge0\) and \(k\ge5\), let \(A_k(n)\) be the number of partitions of \(n\) into distinct positive parts that contain \(k\). Then
\[
A_k(n)\ge A_{k+1}(n).
\]
Consequently, for every modulus \(t\ge6\), residues \(5\le r<s\le t\), and \(n\ge0\), the total number \(D_{r,t}(n)\) of parts congruent to \(r\pmod t\) among all distinct-part partitions of \(n\) satisfies \(D_{r,t}(n)\ge D_{s,t}(n)\). This extends the range of the effective distinct-part part-frequency inequalities proved by Craig (2022), though only for residues at least five.

The proof also yields a positivity certificate: if neither \(k\) nor \(k+1\) is a power of two, then \(A_k(n)-A_{k+1}(n)\) exactly counts distinct-part partitions of \(n-k\) avoiding powers of two as well as \(k\) and \(k+1\). When one adjacent part is a power of two at least eight, a finite nonnegative polynomial certificate yields the remaining inequalities.

## Assumptions and scope
A partition is an unordered finite sum of positive integers; parts are pairwise distinct. The empty partition of zero is allowed, with coefficients at negative indices defined as zero. For \(1\le r\le t\), write \(D_{r,t}(n)=\sum_{j\ge0}A_{r+jt}(n)\). All series below are formal power series in \(q\), so no analytic convergence is assumed.

## Proof
Put \(Q(q)=\prod_{j\ge1}(1+q^j)\). Marking one part gives
\[
\sum_{n\ge0}\left(A_k(n)-A_{k+1}(n)\right)q^{n-k}
=(1-q)\prod_{\substack{j\ge1\\j\notin\{k,k+1\}}}(1+q^j).
\tag{1}
\]
The identity is interpreted as a series with no negative-degree terms; multiplying the right side by \(q^k\) gives the generating series of the difference. The uniqueness of binary expansion gives
\[
(1-q)\prod_{i\ge0}(1+q^{2^i})=1.
\]
Write \(\mathcal B\) for the positive integers that are not powers of two. If \(k,k+1\in\mathcal B\), equation (1) becomes
\[
\prod_{j\in\mathcal B\setminus\{k,k+1\}}(1+q^j),
\]
whose coefficients are nonnegative and have the claimed partition interpretation.

Otherwise, because \(k\ge5\), precisely one of the pair \(k,k+1\) is \(m=2^s\) for some \(s\ge3\). Denote the other by \(b=m-1\) or \(b=m+1\), and set \(h=m/8=2^{s-3}\). Equation (1) is now
\[
\frac{\prod_{j\in\mathcal B\setminus\{b\}}(1+q^j)}{1+q^m}.
\tag{2}
\]
The factor \(j=3m=24h\) occurs in the numerator and is neither a power of two nor equal to \(b\). Extract it and use the exact polynomial identity
\[
\frac{1+q^{3m}}{1+q^m}=1-q^m+q^{2m}.
\tag{3}
\]
If \(s\ge4\), select the five further distinct numerator factors indexed by \(j=ah\) for \(a\in T_+=(3,5,6,7,10)\). If \(s=3\) and \(b=9\), use the same set. If \(s=3\) and \(b=7\), instead take \(T_-=(3,5,6,10,14)\). Every selected index lies in \(\mathcal B\setminus\{b\}\) and differs from \(3m\): when \(h\ge2\), none of the selected multiples of \(h\) can equal the odd integer \(b\); for \(h=1\), the two displayed sets omit the forbidden value. Their elements all have an odd factor greater than one and thus are not powers of two.

Define the two explicitly checkable integral polynomials
\[
P_\pm(z)=(1-z^8+z^{16})\prod_{a\in T_\pm}(1+z^a).
\tag{4}
\]
Every coefficient of both polynomials is nonnegative. Indeed, multiplying five binomials and shifting their coefficients by \(0,8,16\) with signs \(+,-,+\) gives the exact finite coefficient arrays in the verification script `verify.py`; it asserts nonnegativity at every degree, and the complete coefficient arrays can be reproduced with elementary integer additions. The degrees are respectively \(47\) and \(54\). Substituting (3) into (2), factoring out the chosen five terms, and applying (4) expresses (2) as \(P_\pm(q^h)R(q)\), where \(R(q)\) is a formal product of terms \(1+q^j\) with nonnegative coefficients. Therefore every coefficient in (2) is nonnegative, completing the proof of \(A_k(n)\ge A_{k+1}(n)\) for all \(k\ge5\) and \(n\ge0\).

Finally, for \(5\le r<s\le t\), telescope each progression:
\[
D_{r,t}(n)-D_{s,t}(n)
=\sum_{j\ge0}\sum_{k=r+jt}^{s+jt-1}\bigl(A_k(n)-A_{k+1}(n)\bigr)\ge0.
\]
Only finitely many terms are nonzero for any fixed \(n\). This completes the claim.

## Verification
Run `python3 verify.py` using the bundled standard-library-only checker. It reconstructs both finite polynomial coefficient arrays by integer multiplication and verifies every coefficient is nonnegative (lengths 48 and 55, coefficient sum 32 each). Independently, it checks \(123255\) distinct part-frequency comparisons for \(5\le k<n\le500\), and verifies the exact restricted-partition identity for eligible \(5\le k\le50\), \(k\le n\le200\). These finite checks support the exact polynomial certificate and finite examples; the infinite inequalities follow from the factorization proof above.

## Relationship to prior work
Craig (2022, arXiv:2110.15835, Corollary 1.3) proves \(D_{r,t}(n)\ge D_{s,t}(n)\) for all \(n>8\) and \(2\le t\le10\), while giving eventual inequalities for any fixed modulus. The result here proves an all-\(n\), all-moduli statement for \(r\ge5\); it leaves residues \(r\le4\) unresolved by this argument. Euler's binary expansion and the distinct-part/no-powers-of-two partition identity recorded by Sellers, Sills, and Mullen (2004, citing Guy 1958) supply the classical positive factorization. The new step is the uniform treatment of the exceptional power-of-two adjacent pairs by two finite polynomial certificates, giving the universal cutoff at part size five.

## Limitations
The theorem makes no claim for adjacent part sizes \(1\le k\le4\), and it does not establish Craig's full conjectured range for \(1\le r<s\le t\) and \(n>8\). No optimality or strict positivity of the inequalities is claimed. The finite verifier is not an independent mathematical audit.

## References
- W. Craig, *On the Number of Parts in Congruence Classes for Partitions into Distinct Parts*, arXiv:2110.15835v5 (first posted October 29, 2021), especially Corollary 1.3 and its discussion of the unbounded-modulus gap.
- J. A. Sellers, A. V. Sills, and G. L. Mullen, *Bijections and Congruences for Generalizations of Partition Identities of Euler and Guy*, Electronic Journal of Combinatorics **11** (2004), #R43, doi:10.37236/1796 (classical binary-partition identity and generalizations).
