# Exact least periods of three-term LCM quotients for an Eisenstein cubic family

## Finding
For each positive odd integer \(m\), put \(f_m(n)=n^3+2m\), \(U_m=108m^2+1\), and \(V_m=27m^2+16\). For every integer \(n\ge0\), set
\[
Q_m(n)=\frac{f_m(n)f_m(n+1)f_m(n+2)}{\operatorname{lcm}(f_m(n),f_m(n+1),f_m(n+2))}.
\]
Then
\[
\boxed{Q_m(n)=2^{\mathbf1_{2\mid n}}
\gcd(2n+6m+1,U_m)\gcd(2n+6m+3,U_m)
\gcd(4n+4+3m,V_m).}
\]
Its **least positive period** is
\[
\boxed{P_m=2\operatorname{lcm}(U_m,V_m).}
\]
Moreover,
\[
\gcd(U_m,V_m)=\begin{cases}
7,&m\equiv\pm3\pmod7,\\1,&\text{otherwise}.
\end{cases}
\]
In the shared-prime case, the smaller of the two 7-adic exponents is exactly one, but the larger exponent can exceed one (for example, \(m=11\) has \(\nu_7(V_m)=2\), and \(m=17\) has \(\nu_7(U_m)=4\)). The period formula includes these higher powers.

## Assumptions and scope
The parameter \(m\) is an arbitrary positive odd integer and \(n\ge0\). All gcds and lcms refer to positive integers. As \(2\mid 2m\) and \(4\nmid2m\), \(t^3+2m\) is Eisenstein at 2, hence irreducible over the rationals. This theorem treats exactly three consecutive values and asserts no formula for even \(m\), other polynomials, or longer windows.

## Proof

**1. Triple gcd and prime-wise decomposition.** Set \(a=f_m(n)\), \(b=f_m(n+1)\), \(c=f_m(n+2)\). Their adjacent differences are
\[
b-a=3n^2+3n+1,\qquad c-b=3(n+1)^2+3(n+1)+1.
\]
Both differences are odd and congruent to 1 modulo 3. If an odd prime \(p\ne3\) divides both, then \(p\mid6(n+1)\), so \(n\equiv-1\pmod p\), which contradicts \(3n^2+3n+1\equiv1\pmod p\). No prime divides \(a,b,c\) simultaneously. Thus \(\gcd(a,b,c)=1\). Comparing prime exponents for three integers with triple gcd one gives
\[
\frac{abc}{\operatorname{lcm}(a,b,c)}
=\gcd(a,b)\gcd(b,c)\gcd(a,c).
\]

**2. Adjacent pairs.** Put \(R=3n^2+3n+1\), \(L=2n+6m+1\), and \(U=108m^2+1\). The exact polynomial identities
\[
3a-(n-1)R=L,\qquad 4R=3L^2-36mL+U
\]
show that for every odd prime \(p\ne3\) and \(j\ge1\), \(p^j\) divides both \(a,R\) exactly when it divides both \(L,U\). Here 3 and 4 are units modulo \(p^j\). Neither pairwise gcd admits a factor 2 or 3: \(R\) is odd and congruent to 1 modulo 3, and \(U\) is odd and congruent to 1 modulo 3. Hence
\[
\gcd(a,b)=\gcd(a,R)=\gcd(L,U).
\]
Replacing \(n\) by \(n+1\) gives \(\gcd(b,c)=\gcd(2n+6m+3,U)\).

**3. Distance-two pair.** Put \(u=n+1\), \(R_2=3u^2+1\), \(L_2=8u+6m\), and \(V=27m^2+16\). Then
\[
c-a=2R_2,\quad
3a-(u-3)R_2=L_2,\quad
64R_2=3L_2^2-36mL_2+4V.
\]
For every odd prime \(p\ne3\), these identities establish equality of the \(p\)-parts of \(\gcd(a,c)\) and \(\gcd(L_2,V)\); neither has a factor 3. Since \(V\) is odd, \(\gcd(L_2,V)=\gcd(4n+4+3m,V)\), by division of the first argument by 2 modulo \(V\). If \(n\) is even, both \(a\) and \(c\) have 2-adic valuation one (\(m\) odd); if \(n\) is odd, both are odd. Therefore
\[
\gcd(a,c)=2^{\mathbf1_{2\mid n}}\gcd(4n+4+3m,V).
\]
Multiplying the three pairwise formulas proves the displayed expression for \(Q_m\).

**4. Overlap of odd moduli.** Because \(U-4V=-63\) and \(U\equiv V\equiv1\pmod3\), the gcd divides 7. Modulo 7 we have \(U\equiv3m^2+1\), which vanishes precisely for \(m\equiv\pm3\pmod7\); this also makes \(V\) divisible by 7. Hence \(\gcd(U,V)\) is as claimed. In particular, **at least one** of \(\nu_7(U),\nu_7(V)\) equals one if both are positive, but it is not generally true that both equal one. The examples \(m=11\) and \(m=17\) above explicitly refute the latter assertion.

**5. Sharp least period, including all powers of 7.** The formula in the finding makes \(T=2\operatorname{lcm}(U,V)\) a period. Conversely, every period \(H\) of the integer-valued function preserves the valuation \(\nu_p(Q_m(n))\) for every prime. At \(p=2\), this valuation alternates between one and zero, forcing \(2\mid H\). For an odd prime \(p\mid UV\), note that \(p\ne3\).

If \(p^e\Vert U\) but \(p\nmid V\), the valuation at \(p\) equals
\[
A(n)=\min(e,\nu_p(2n+6m+1))+
\min(e,\nu_p(2n+6m+3)).
\]
The linear arguments differ by 2, so at odd \(p\) exactly two distinct residues modulo \(p^e\) attain the maximum \(e\). For \(e=1\) this nonempty proper set is not translation-invariant modulo \(p\). For \(e\ge2\), translation by \(p^{e-1}\) cannot preserve the two root residues (whose difference in the \(n\) variable is 1), since \(p^{e-1}\not\equiv\pm1\pmod{p^e}\). Hence the least \(p\)-power period is \(p^e\). If \(p^e\Vert V\) but \(p\nmid U\), the valuation reaches maximum \(e\) at one residue modulo \(p^e\), again forcing least local period \(p^e\).

It remains to treat a shared prime, necessarily \(p=7\). Write \(e=\nu_7(U)\), \(d=\nu_7(V)\). By step 4, \(\min(e,d)=1\). The roots modulo 7 of the two \(U\)-linear factors and the \(V\)-linear factor are **pairwise distinct**: overlap would make two of \(\gcd(a,b),\gcd(b,c),\gcd(a,c)\) divisible by 7 and hence force \(7\mid\gcd(a,b,c)\), contrary to step 1. If \(e=d=1\), the 7-adic valuation is one on exactly three of the seven residue classes and zero on the other four, so its local least period is 7.

If \(e\ge2\) (and therefore \(d=1\)), the valuation has maximum \(e\) exactly at the two residues modulo \(7^e\) where the respective \(U\)-linear argument vanishes modulo \(7^e\). At those roots the other two factors are prime to 7. Every other residue has valuation at most \(e-1\), except that the separate \(V\)-root class has valuation one. Since the two maximum residues differ by one in \(n\), translation by \(7^{e-1}\) cannot preserve their set. Thus the local least period is \(7^e\). If \(d\ge2\) (and \(e=1\)), the unique residue modulo \(7^d\) where the \(V\)-linear factor vanishes modulo \(7^d\) has maximal valuation \(d\), while all remaining residues have valuation at most \(d-1\), and the \(U\)-roots contribute only one. This forces local least period \(7^d\).

For any prime \(p\mid UV\), the valuation function just studied depends only on \(n\pmod{p^{\max(\nu_p(U),\nu_p(V))}}\) and has that prime power as its exact least period. Any global period \(H\) is also a period of each valuation sequence and therefore is divisible by that prime power; combine these independent conditions and the evenness requirement to deduce \(T\mid H\). Since \(T\) itself is a period, it is the least positive period, as claimed.

## Verification
An independent exact-integer cross-check compared the original three-cubic product divided by their lcm with the displayed gcd formula at 700 consecutive indices for each \(m\in\{1,3,5,11,17,81,87\}\): 4,900 comparisons. Crucially, the high-7-power cases \(m=11,17,81,87\) were tested separately and their predicted maximal 7-power local periods (49, 2401, 49, 49) were all confirmed by exact residue enumeration. These finite checks corroborate the proof but do not establish its infinite quantifiers. The accompanying `verify.py` independently reproduces these regression cases as well as its existing small-parameter comparisons.

## Relationship to prior work
Bodin and Drouin, *Around the gcd of the values of two polynomials* (arXiv:2409.01224), supply general resultant-based methods and periodicity phenomena for pairwise polynomial gcds. Dubickas, *On the least common multiple of several consecutive values of a polynomial* (Algebra i Analiz 34 (2022)), proves broader periodicity bounds using reduced resultants. Hong and Qian analyze consecutive **quadratic** progressions. These general results do not, as stated, supply this family-specific exact gcd decomposition or the sharp least period including the shared-7 valuation cases. Historical priority over less accessible or unindexed special-case results remains qualified.

## Limitations
The theorem covers precisely positive odd \(m\) and three consecutive values, not even \(m\), arbitrary cubic polynomials, or longer windows. It does not claim general polynomial-gcd periodicity as new. Finite computations support the arithmetic only; the valuation argument establishes the all-parameter theorem. No universal historical-priority certification is claimed.

## References
1. Arnaud Bodin and Christian Drouin, *Around the gcd of the values of two polynomials*, arXiv:2409.01224, https://arxiv.org/abs/2409.01224.
2. Arturas Dubickas, *On the least common multiple of several consecutive values of a polynomial*, Algebra i Analiz 34 (2022), 231–239; St. Petersburg Math. J. 34 (2023), 305–311, https://www.mathnet.ru/eng/aa1806.
3. S. Hong and G. Qian, *The least common multiple of consecutive quadratic progression terms*, arXiv:1208.5119, https://arxiv.org/abs/1208.5119.
