# Exact least periods of three-term LCM quotients for an Eisenstein cubic family

## Finding
For every positive odd integer \(m\), set \(f_m(t)=t^3+2m\), \(U_m=108m^2+1\), and \(V_m=27m^2+16\). For each integer \(n\ge0\), define the integer
\[
Q_m(n)=\frac{f_m(n)f_m(n+1)f_m(n+2)}{\operatorname{lcm}(f_m(n),f_m(n+1),f_m(n+2))}.
\]
The exact formula is
\[
Q_m(n)=2^{\mathbf1_{2\mid n}}\gcd(2n+6m+1,U_m)\gcd(2n+6m+3,U_m)\gcd(4n+4+3m,V_m).
\]
Its **least** positive period is
\[
P_m=2\operatorname{lcm}(108m^2+1,27m^2+16).
\]
The two odd moduli intersect at the prime \(7\) exactly when \(m\equiv\pm3\pmod7\):
\[
\gcd(U_m,V_m)=\begin{cases}7,&m\equiv\pm3\pmod7,\\1,&\text{otherwise}.\end{cases}
\]

## Assumptions and scope
The parameter \(m\) ranges over **all positive odd integers**, and the index \(n\) over all nonnegative integers. All gcd and lcm operations use positive integers. The polynomial \(f_m\) is Eisenstein at \(2\), since its constant term has exactly one factor \(2\), so this is an infinite family of irreducible cubics. This is a three-value window only; no assertion is made for longer windows or even \(m\).

## Proof
**1. Reduction to pairwise gcds.** Write \(a=f_m(n)\), \(b=f_m(n+1)\), and \(c=f_m(n+2)\). For any positive integers with \(\gcd(a,b,c)=1\), comparison of prime valuations gives
\[
\frac{abc}{\operatorname{lcm}(a,b,c)}=\gcd(a,b)\gcd(b,c)\gcd(a,c).
\]
Here \(b-a=3n^2+3n+1\) and \(c-b=3(n+1)^2+3(n+1)+1\). Both differences are odd and congruent to \(1\) modulo \(3\). If an odd prime \(p\ne3\) divides both, their difference \(6(n+1)\) forces \(n\equiv-1\pmod p\), contradicting \(3n^2+3n+1\equiv1\pmod p\). Thus no prime divides all three terms and \(\gcd(a,b,c)=1\).

**2. Adjacent pairs.** Put \(R=3n^2+3n+1\) and \(L=2n+6m+1\). Direct polynomial identities give
\[
3a-(n-1)R=L,\qquad 4R=3L^2-36mL+(108m^2+1).
\]
Since \(\gcd(a,R)\) is odd and prime to \(3\) (as \(R\equiv1\pmod3\)), these identities, together with the converse implications modulo every odd prime power, establish
\[
\gcd(a,b)=\gcd(a,R)=\gcd(L,U_m).
\]
Indeed, modulo any odd prime power other than a power of \(3\), the first identity implies that simultaneous divisibility of \(a,R\) is equivalent to simultaneous divisibility of \(L,R\), and the second identity then gives equivalence to simultaneous divisibility of \(L,U_m\) (because \(4\) is invertible). Conversely, \(L\equiv U_m\equiv0\) implies \(R\equiv a\equiv0\) by the same identities. The integers \(U_m\equiv1\pmod3\) are also odd, so no excluded prime contributes. Replacing \(n\) by \(n+1\) gives
\[
\gcd(b,c)=\gcd(2n+6m+3,U_m).
\]

**3. Distance-two pair.** Put \(u=n+1\), \(R_2=3u^2+1\), and \(L_2=8u+6m\). Then \(c-a=2R_2\), and direct identities read
\[
3a-(u-3)R_2=L_2,\qquad 64R_2=3L_2^2-36mL_2+4(27m^2+16).
\]
For every odd prime \(p\ne3\), the same invertible-prime-power argument proves equality of the odd parts of \(\gcd(a,c)\) and \(\gcd(L_2,V_m)\). No factor \(3\) occurs, because \(R_2\equiv1\pmod3\). As \(V_m\) is odd, \(\gcd(L_2,V_m)=\gcd(4n+4+3m,V_m)\). Finally, \(m\) odd implies \(a,c\) have exactly one factor \(2\) when \(n\) is even (their cube terms are multiples of \(8\) and \(2m\) has valuation \(1\)); when \(n\) is odd both are odd. Thus
\[
\gcd(a,c)=2^{\mathbf1_{2\mid n}}\gcd(4n+4+3m,V_m).
\]
Multiplication of the three pairwise gcd formulas completes the exact formula for \(Q_m(n)\).

**4. Intersection of the two moduli.** Since \(U_m-4V_m=-63\), their gcd divides \(63\). Both are \(1\) modulo \(3\), so their gcd divides \(7\). Modulo \(7\), \(U_m\equiv3m^2+1\), which vanishes exactly for \(m\equiv\pm3\pmod7\). Thus the claimed intersection classification follows. In particular, if \(7\) divides both moduli, it appears to exponent exactly \(1\) in each.

**5. Sharpness of the period.** The explicit formula first shows that \(T=2\operatorname{lcm}(U_m,V_m)\) is a period. We prove that each prime-power factor of \(T\) is forced by the corresponding valuation pattern \(v_p(Q_m(n))\), which every period must preserve.

For \(p=2\), the valuation alternates exactly between \(1\) and \(0\), so every period is even. Now let \(p\) be an odd prime; neither modulus is divisible by \(3\). If \(p^e\Vert U_m\) and \(p\nmid V_m\), the valuation is
\[
\min(e,v_p(2n+6m+1))+\min(e,v_p(2n+6m+3)).
\]
Its maximum \(e\) occurs exactly on **two residues modulo \(p^e\)**, separated by \(1\). The residues are distinct because \(p\) is odd. A translation by \(p^{e-1}\) cannot preserve this two-element maximum set when \(e\ge2\): otherwise a translate of one root would be the other, requiring \(p^{e-1}\equiv\pm1\pmod{p^e}\), impossible for odd \(p\) and \(e\ge2\). For \(e=1\), there are exactly two of the \(p\) residues (and \(p\ge5\)), so this valuation is nonconstant. Since its period divides \(p^e\), its least period is exactly \(p^e\).

If \(p^e\Vert V_m\) and \(p\nmid U_m\), the valuation equals \(\min(e,v_p(4n+4+3m))\) and reaches its maximum at exactly one residue modulo \(p^e\); this forces least period \(p^e\). In the only overlapping case, \(p=7\), both exponents equal \(1\); the valuation is \(1\) at three **distinct** residue classes modulo \(7\), one arising from each gcd. If two of these classes coincided, the relevant two pairwise gcds would both be divisible by \(7\), forcing \(7\mid\gcd(a,b,c)\), which step 1 excludes. Hence the valuation is not constant modulo \(7\) and forces period \(7\).

All prime-power periods are therefore compulsory. Since they are coprime, every positive period is a multiple of \(2\operatorname{lcm}(U_m,V_m)\), proving minimality.

## Verification
The accompanying standalone Python program `verify.py` computes the original product/lcm quotient and the closed expression separately with exact integers for each odd \(1\le m\le99\) and \(0\le n<180\), totaling **9,000** comparisons. It additionally checks modulus intersection and local prime-power minimality patterns for \(m\in\{1,3,5,7,9\}\). It uses only the standard library and can be run as `python3 verify.py`. These finite tests check arithmetic and illustrative local structure; the unrestricted quantifiers are proved in the five steps above. The resulting least periods for \(m=1,3\) are \(9374\) and \(72002\), respectively.

## Relationship to prior work
Bodin and Drouin, *Around the gcd of the values of two polynomials* (first publicly posted 2024-09-02), establish resultant-based periodicity for pairwise polynomial gcds and study local valuation patterns. Dubickas, *On the least common multiple of several consecutive values of a polynomial* (2022), establishes general periodicity and a period expressed through reduced resultants. Hong and Qian analyze **quadratic** progressions in detail. These theorems motivate the object and supply broader periodicity, but their inspected statements do not give this Eisenstein cubic family's three-gcd decomposition, least period, or exact exceptional overlap at \(7\). The proof above establishes those sharper special-family statements directly.

## Limitations
Only positive odd \(m\) and exactly three consecutive arguments are covered. No claim is made about the least period for arbitrary cubic polynomials or for longer windows. Earlier general periodicity is not claimed as new. Mathematical originality is assessed against the cited, inspected sources and available indexed records, not against every possibly unindexed manuscript. No independent audit has been performed.

## References
1. A. Bodin and C. Drouin, *Around the gcd of the values of two polynomials*, arXiv:2409.01224 (first posted 2024-09-02), https://arxiv.org/abs/2409.01224.
2. A. Dubickas, *On the least common multiple of several consecutive values of a polynomial*, Algebra i Analiz 34 (2022), 231–239; St. Petersburg Math. J. 34 (2023), 305–311, https://www.mathnet.ru/eng/aa1806.
3. S. Hong and G. Qian, *The least common multiple of consecutive quadratic progression terms*, arXiv:1208.5119, https://arxiv.org/abs/1208.5119.
