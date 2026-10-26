# Sharp oscillation of digit-rotation coprimality densities

## Finding
Fix an integer base \(b\ge2\). For each integer \(m\ge1\), let \(F_b(m)\) count the positive integers \(N\) with exactly \(m\) base-\(b\) digits for which the greatest common divisor of all \(m\) cyclic rotations of the digit string is \(1\). A rotation is evaluated as an integer even if it begins with zero. Put \(M_m=b^m-1\) and \(L_m=(b-1)b^{m-1}\). Then, for every \(b\ge2\) and \(m\ge1\),

\[
\left|F_b(m)-L_m\frac{\varphi(M_m)}{M_m}\right|\le 2\sqrt{M_m}+\pi(b-1)\left\lceil\frac b2\right\rceil^m,
\]

where \(\varphi\) is Euler's totient function and \(\pi(x)\) counts primes at most \(x\). In particular, with \(P_b(m)=F_b(m)/L_m\),

\[
P_b(m)=\frac{\varphi(b^m-1)}{b^m-1}
+O_b\left(b^{-m/2}+\left(\frac{\lceil b/2\rceil}{b}\right)^m\right).
\]

Every fixed positive integer \(d\) yields a subsequential limit:

\[
\lim_{\substack{\ell\to\infty\\ \ell\ \mathrm{prime}}} P_b(d\ell)
=\frac{\varphi(b^d-1)}{b^d-1}.
\]

Consequently, the sequence of digit-length proportions has infinitely many distinct accumulation values and

\[
\boxed{\liminf_{m\to\infty}P_b(m)=0,
\qquad\limsup_{m\to\infty}P_b(m)=\frac{\varphi(b-1)}{b-1}.}
\]

For decimal integers, the sharp upper and lower limits are \(2/3\) and \(0\). For binary integers they are \(1\) and \(0\).

## Assumptions and scope
All digit strings use the ordinary positional representation with one nonzero leading digit and \(m-1\) subsequent digits in \(\{0,1,\ldots,b-1\}\). Their rotations are positional \(m\)-place strings; any resulting leading zeros are retained as positions but do not change the represented integer. The common gcd includes the original integer. The base \(b\) is fixed when taking any limit. No claim is made about *pairwise* coprimality of the rotations, which is a different, stronger requirement.

## Proof
**1. Exact rotation-gcd identity.** Write the digits of \(N\) as \(a_0,a_1,\ldots,a_{m-1}\) in left-to-right order, and let \(N_j\) be the integer represented by the rotation through \(j\) positions to the left, where \(N_0=N\) and indices of \(a_j\) are taken modulo \(m\). Set

\[
D=\gcd(a_0,\ldots,a_{m-1})\ge1,
\qquad G=\gcd(N_0,\ldots,N_{m-1}),\qquad M=b^m-1.
\]

The elementary rotation relation is \(N_{j+1}=bN_j-Ma_j\) for all \(j\), with \(N_m=N_0\). Since \(G\) divides both consecutive rotations, it divides every \(Ma_j\), hence \(MD\), and also \(N\). Therefore \(G\mid\gcd(N,MD)\). Conversely, \(g=\gcd(N,MD)\) divides \(N_0\) and every \(Ma_j\), because \(D\mid a_j\). Induction through the rotation relation shows \(g\mid N_j\) for every \(j\). Thus

\[
\boxed{G=\gcd(N,(b^m-1)D).}
\]

Also \(D\mid N\), since it divides every digit. It follows that \(G=1\) holds exactly when \(D=1\) and \(\gcd(N,M)=1\).

**2. Uniform count.** Let \(A_b(m)\) count the integers in \([b^{m-1},b^m)\) coprime to \(M\). Möbius inversion gives the exact identity

\[
A_b(m)=\sum_{d\mid M}\mu(d)
\left(\left\lfloor\frac{b^m-1}{d}\right\rfloor
-\left\lfloor\frac{b^{m-1}-1}{d}\right\rfloor\right).
\]

Each parenthesis differs from \(L_m/d\) by less than \(1\). Using \(\sum_{d\mid M}\mu(d)/d=\varphi(M)/M\),

\[
\left|A_b(m)-L_m\frac{\varphi(M)}{M}\right|
\le2^{\omega(M)}\le\tau(M)\le2\sqrt M.
\]

The condition \(D>1\) implies that some prime \(q\le b-1\) divides all digits. For each such prime, there are at most \(\lceil b/q\rceil^m\) possible positional strings, because only the multiples of \(q\) are allowed in each position. Hence the number of such exceptional strings is at most

\[
\sum_{q\le b-1\atop q\text{ prime}}\left\lceil\frac bq\right\rceil^m
\le\pi(b-1)\left\lceil\frac b2\right\rceil^m.
\]

Since \(F_b(m)\) is obtained from \(A_b(m)\) by removing precisely the coprime-to-\(M\) strings with \(D>1\), the stated explicit error bound follows. Division by \(L_m\) establishes the exponentially small proportion error for each fixed \(b\).

**3. Prime-multiple subsequences.** Fix \(d\ge1\) and write \(B=b^d\). Let \(\ell\) run through primes larger than \(B-1\), and factor

\[
b^{d\ell}-1=(B-1)S_\ell,
\qquad S_\ell=1+B+\cdots+B^{\ell-1}.
\]

Since \(S_\ell\equiv\ell\pmod{B-1}\), the factors on the right are coprime. If a prime \(q\mid S_\ell\), then \(q\nmid B-1\) and the multiplicative order of \(B\) modulo \(q\) is exactly \(\ell\); therefore \(q\equiv1\pmod\ell\) and \(q\ge\ell+1\). As \(\omega(S_\ell)\log(\ell+1)\le\log S_\ell<\ell\log B\),

\[
0\le\sum_{q\mid S_\ell}\frac1q
\le\frac{\ell\log B}{(\ell+1)\log(\ell+1)}\longrightarrow0.
\]

Using \(1-\sum t_i\le\prod(1-t_i)\le1\) for \(0\le t_i\le1\), the totient product formula gives

\[
\frac{\varphi(b^{d\ell}-1)}{b^{d\ell}-1}
=\frac{\varphi(B-1)}{B-1}
\prod_{q\mid S_\ell}\left(1-\frac1q\right)
\longrightarrow\frac{\varphi(B-1)}{B-1}.
\]

The proportion error from step 2 tends to zero along \(m=d\ell\); hence the claimed subsequential limit holds. With \(d=1\), this gives the lower bound for the limit superior. The upper bound follows from \(b-1\mid b^m-1\), since \(\varphi(N)/N\) decreases or stays constant when additional distinct prime factors are introduced.

**4. Lower limit and infinitely many accumulation values.** For every prime \(q\nmid b\), let \(o_q\) denote the positive multiplicative order of \(b\) modulo \(q\). For a threshold \(Y\), choose any integer \(m_Y\ge Y\) divisible by all \(o_q\) with \(q\le Y\) prime and \(q\nmid b\). Then every such \(q\) divides \(b^{m_Y}-1\), so

\[
0\le\frac{\varphi(b^{m_Y}-1)}{b^{m_Y}-1}
\le\prod_{q\le Y\atop q\nmid b}\left(1-\frac1q\right)
\longrightarrow0
\]

by divergence of the sum of reciprocals of the primes. The proportion error again tends to zero, giving the limit inferior \(0\). Taking \(d=m_Y\) in step 3 shows that the positive ratios \(\varphi(b^d-1)/(b^d-1)\) form an infinite collection of distinct accumulation values: a collection of positive values approaching zero cannot be finite. This completes the proof.

## Verification
The standalone file `check.py` constructs each positional digit rotation directly, compares its exact gcd with the formula from step 1, checks the coprimality decomposition, and tests the resulting proportions. Executing `python check.py` gave `VERIFY_OK: 235455 direct rotation gcd tests across 49 base/length blocks`, covering bases \(2\) through \(11\) with every tested length satisfying \(b^m\le150000\). Among the decimal counts were \(F_{10}(2)=41\), \(F_{10}(3)=511\), \(F_{10}(4)=5125\), and \(F_{10}(5)=56675\). The familiar example \(148,481,814\) has gcd \(37\), also checked. Finite tests support the identities but do not establish the infinite asymptotic claims, which are proved above.

## Relationship to prior work
OEIS A084433, introduced by Amarnath Murthy on June 2, 2003, lists decimal integers whose digit rotations have common gcd greater than one and gives examples of divisibility mechanisms. OEIS A387356 explicitly lists the complementary gcd-one integers, while OEIS A287513 concerns the strictly stronger pairwise-coprime condition. None of the inspected entries gives the present length-dependent totient approximation or its complete extremal limits. The MathPages article *Cyclic and Reverse Divisibility* shows that \(\gcd(N,b^m-1)\) divides every rotation; this is a necessary input but does not determine the full rotation gcd (for example, \(N=22\) has full rotation gcd \(22\), whereas \(\gcd(22,99)=11\)). The classical description of transposable integers likewise includes the rotation congruence without the quantitative count. Basta's 2026 preprint concerns rotations of prime-denominator repetends, not the distribution over all digit strings.

## Limitations
The theorem treats the gcd of the entire rotation set, not pairwise gcds, primality, or exact factorization of general repetends. The asymptotic error is uniform in digit length for a fixed base; its implicit constant may depend on the base. The accumulation values proved above are guaranteed members of the accumulation set but are not asserted to exhaust that set. No independent mathematical audit or exhaustive historical priority certification has been performed.

## References
- Amarnath Murthy, OEIS A084433, *Numbers whose cyclic permutations have GCD > 1*, introduced June 2, 2003, https://oeis.org/A084433 .
- Paolo Xausa, OEIS A387356, *Numbers whose set of cyclic permutations has GCD = 1*, August 27, 2025, https://oeis.org/A387356 .
- Rémy Sigrist, OEIS A287513, *Numbers whose cyclic permutations are pairwise coprime*, May 26, 2017, https://oeis.org/A287513 .
- *Cyclic and Reverse Divisibility*, MathPages, https://www.mathpages.com/home/kmath081/kmath081.htm .
- *Transposable integer*, section “General,” https://en.wikipedia.org/wiki/Transposable_integer .
- Oussama Basta, *Analytical Generalization of Cyclic Digit Rotation and Phase-Space Prime Location Theory*, preprint dated October 11, 2026, DOI 10.13140/RG.2.2.27277.70888; accessible text at https://www.researchgate.net/publication/415560874_Analytical_Generalization_of_Cyclic_Digit_Rotation_and_Phase-Space_Prime_Location_Theory .
