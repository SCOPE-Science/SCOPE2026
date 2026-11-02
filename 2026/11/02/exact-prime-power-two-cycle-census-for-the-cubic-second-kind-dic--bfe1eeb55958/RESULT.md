# Exact prime-power two-cycle census for the cubic second-kind Dickson map

## Finding
Let \(p\) be any prime, \(k\ge1\), and let \(F\) act on \(\mathbb Z/p^k\mathbb Z\) by
\[
F(x)=x^3-2x=E_3(x,1).
\]
A point has **least period two** if \(F(F(x))=x\) and \(F(x)\ne x\) modulo \(p^k\). The following is an exact classification, for all primes and every level.

For odd \(p\), write \(h=\lceil k/3\rceil\). The complete set is
\[
\{x:x\equiv1\pmod{p^h}\}\;\mathbin{\dot\cup}\;\{x:x\equiv-1\pmod{p^h}\},
\]
and it has precisely \(2p^{k-h}\) points, or \(p^{k-h}\) distinct two-cycles.

For \(p=2\), no point has least period two at \(k=1\). At \(2\le k\le10\), **every odd class** has least period two: the point count is \(2^{k-1}\), and the cycle count is \(2^{k-2}\). At \(k\ge11\), put \(r=\lceil(k-1)/3\rceil\). The complete set is
\[
\{x:x\equiv1\pmod{2^{r-1}}\}\;\mathbin{\dot\cup}\;\{x:x\equiv-1\pmod{2^{r-1}}\},
\]
with \(2^{k-r+2}\) points and \(2^{k-r+1}\) two-cycles. In particular, the first nontrivial restriction on the odd residue classes occurs **exactly at exponent eleven**.

## Assumptions and scope
All congruences are in the integer residue ring \(\mathbb Z/p^k\mathbb Z\), not in a finite field unless \(k=1\). The polynomial is the degree-three Dickson polynomial of the second kind with parameter one. Point counts distinguish elements; cycle counts identify each unordered pair \(\{x,F(x)\}\). No permutation hypothesis is needed. For nonzero integers \(m\), \(\nu_p(m)\) is the usual \(p\)-adic valuation; setting \(\nu_p(0)=+\infty\) makes the divisibility statements below uniform.

## Proof
Over the integers, direct composition and factorization give
\[
F(F(X))-X=X(X^2-3)(X^2-1)^3,
\qquad F(X)-X=X(X^2-3).
\tag{1}
\]
These are polynomial identities, so they remain valid modulo any integer.

**Odd primes.** If \(x^2-1\) is a unit modulo \(p\), equation (1) says that \(F(F(x))-x\) and \(F(x)-x\) differ by a unit. Thus any point whose second iterate is itself is already fixed, so it has no least period two. Conversely, suppose \(x\equiv\epsilon\pmod p\), where \(\epsilon\in\{1,-1\}\). The factor \(x(x^2-3)\) is a unit, since it is \(\epsilon(1-3)=-2\epsilon\) modulo odd \(p\). Thus \(F(x)\not\equiv x\pmod p\), while equation (1) gives
\[
\nu_p(F(F(x))-x)=3\nu_p(x^2-1)=3\nu_p(x-\epsilon).
\]
The last equality follows because \(x+\epsilon\equiv2\epsilon\) is a unit. Hence the second-iterate congruence holds exactly when \(x\equiv\epsilon\pmod{p^{\lceil k/3\rceil}}\). The two residue balls are disjoint, each contains \(p^{k-\lceil k/3\rceil}\) points, and all these points have least period two. This argument includes \(p=3\).

**The prime two.** At \(k=1\), \(F(x)\equiv x\pmod2\) for both residue classes, so no least-two point exists. Let \(k\ge2\). For even \(x\), \(x^2-1\) is odd and the first case of (1) again forces every second-iterate fixed point to be fixed. For odd \(x\), one has \(\nu_2(x)=0\), \(\nu_2(x^2-3)=1\), and therefore
\[
\nu_2(F(x)-x)=1,\qquad
\nu_2(F(F(x))-x)=1+3\nu_2(x^2-1).
\]
Thus an odd class is never fixed modulo \(2^k\) for \(k\ge2\), and it has least period two precisely if
\[
\nu_2(x^2-1)\ge r:=\lceil(k-1)/3\rceil.\tag{2}
\]
Every odd square is one modulo eight, so (2) holds for all odd classes exactly when \(r\le3\), equivalently \(2\le k\le10\). This gives \(2^{k-1}\) points. For \(k\ge11\), \(r\ge4\). Exactly one of \(x-1,x+1\) has \(2\)-valuation one, and the other has valuation at least two. Therefore \(\nu_2(x^2-1)\ge r\) is equivalent to \(x\equiv\pm1\pmod{2^{r-1}}\). These classes are disjoint when \(r\ge4\), each has \(2^{k-(r-1)}\) lifts, giving the claimed total. Every least-two orbit has two distinct points, so dividing point counts by two gives every cycle count. \(\square\)

## Verification
Run `python3 verify.py` with Python 3. It uses only the standard library, proves the displayed polynomial identity by exact symbolic coefficient arithmetic, then for a documented finite collection of prime powers independently enumerates all residue classes, computes two modular iterates directly, and checks **both** the exact point set and the count. All machine checks are finite and are not substitutes for the preceding universal proof.

## Relationship to prior work
Diene and Salim (2013) determine fixed-point statistics for Dickson polynomials of the second kind over finite fields, noting that their broader cycle structure was not classified there. A period-two point is a fixed point of the **second iterate** but not of the polynomial; this is not the same as their single-map fixed-point problem, especially over rings \(\mathbb Z/p^k\mathbb Z\). Qu and Ding (2014) classify substantial families of second-kind Dickson **permutation polynomials** over prime-power rings, rather than the point and cycle counts of this particular nonpermutation map. General polynomial valuation methods of Medina, Moll and Rowland (2015) address valuations, while Hutz and Patel (2017) study different maps over prime fields; neither inspected result states this classification. A 2025 paper by Wang computes Dickson-polynomial moments over finite fields, also a different quantity. The elementary factorization (1) and valuation principles are not claimed as new. The proposed contribution is their complete, sharp period-two census for this particular map over every prime-power residue ring, including the two-adic threshold.

## Limitations
The theorem concerns only least period two for \(E_3(X,1)\) on integer prime-power residue rings. It does not classify cycles of higher period, Dickson polynomials of other degrees or parameters, or finite-field extensions. Equivalent coverage in unlocated historical dynamics literature remains a risk.

## References
- A. Diene and M. A. Salim, *Fixed Points of the Dickson Polynomials of the Second Kind*, Journal of Applied Mathematics (2013), article 472350, https://doi.org/10.1155/2013/472350 (public 8 April 2013).
- L. Qu and C. Ding, *Dickson Polynomials of the Second Kind that Permute \(\mathbb Z_m\)*, SIAM Journal on Discrete Mathematics 28 (2014), 722–735, https://doi.org/10.1137/130942589 (published online 1 May 2014).
- L. A. Medina, V. H. Moll and E. S. Rowland, *Periodicity in the p-adic valuation of a polynomial*, https://arxiv.org/abs/1505.02302 (2015).
- B. Hutz and T. Patel, *Periodic points and tail lengths of split polynomial maps modulo primes*, https://arxiv.org/abs/1710.07821 (2017).
- Z. Wang, *First and Second Moment Analysis of Dickson Polynomials of the Second Kind*, Journal of Mathematics (2025), https://doi.org/10.1155/jom/5569145.
