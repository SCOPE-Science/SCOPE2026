# Exact even-window gcds of balancing and Lucas-balancing squares

## Finding
Define the balancing and Lucas-balancing sequences by
\[
B_0=0,\quad B_1=1,\quad B_{n+2}=6B_{n+1}-B_n,
\qquad C_0=1,\quad C_1=3,\quad C_{n+2}=6C_{n+1}-C_n.
\]
For every **positive even integer** \(k\), put \(g_k=\gcd(k,B_k)\). Then \(g_k\) is even and the following are exact equalities:
\[
\boxed{\gcd_{n\ge0}\Bigl(\sum_{j=1}^{k}C_{n+j}^{2}\Bigr)=g_k,\qquad
\gcd_{n\ge0}\Bigl(\sum_{j=1}^{k}B_{n+j}^{2}\Bigr)=\frac{g_k}{2}.}
\]
In particular, the ratio of the two consecutive-square GCDs is exactly \(2\) for every even window length, and both GCDs have formulas involving only the window length and one balancing number.

## Assumptions and scope
Here \(\gcd\) denotes the positive greatest common divisor of a nonempty collection of integers. The outer gcd is taken over **every** nonnegative integer \(n\), not just a finite experimental range. The evenness condition on \(k\) is essential to the formulation: no new odd-window statement is asserted. The result concerns the standard recurrence with coefficient \(6\), not an arbitrary generalized Lucas sequence.

For the proof, let the Pell and associated Pell sequences be \(P_0=0,P_1=1,P_{r+2}=2P_{r+1}+P_r\) and \(Q_0=1,Q_1=1,Q_{r+2}=2Q_{r+1}+Q_r\). The classical identities \(B_n=P_{2n}/2\) and \(C_n=Q_{2n}\) follow immediately from the recurrences and initial values.

## Proof
**1. Reducing the infinite gcd to the first window and its differences.** Put
\[
X_n=\sum_{j=1}^{k}C_{n+j}^{2},\qquad Y_n=\sum_{j=1}^{k}B_{n+j}^{2}.
\]
The Pell identities \(C_j^2=(Q_{4j}+1)/2\) and \(B_j^2=(Q_{4j}-1)/16\) give \(X_n=8Y_n+k\). Write \(\alpha=1+\sqrt2\) and \(\beta=1-\sqrt2\), so that \(P_m=(\alpha^m-\beta^m)/(2\sqrt2)\), \(Q_m=(\alpha^m+\beta^m)/2\), and \(\alpha\beta=-1\). Direct factorization gives, for all \(m\ge0\),
\[
Q_{m+4k}-Q_m=4P_{2k}P_{m+2k}.
\]
Consequently,
\[
X_{n+1}-X_n=2P_{2k}P_{2k+4n+4},\qquad
Y_{n+1}-Y_n=\frac{P_{2k}}4P_{2k+4n+4}.
\]
For even \(k\), the integer \(P_{2k}\) is divisible by \(4\). The strong-divisibility identity \(\gcd(P_a,P_b)=P_{\gcd(a,b)}\), obtained from the Pell addition formula and the Euclidean algorithm, gives
\[
\gcd_{n\ge0}P_{2k+4n+4}=P_{\gcd(2k+4,4)}=P_4=12.
\]
Thus, using \(B_k=P_{2k}/2\),
\[
\gcd_{n\ge0}(X_{n+1}-X_n)=48B_k,
\quad\gcd_{n\ge0}(Y_{n+1}-Y_n)=6B_k.
\]
Every window differs from the first by a sum of increments. Hence the desired GCDs are exactly \(\gcd(X_0,48B_k)\) and \(\gcd(Y_0,6B_k)\).

**2. Initial-window identities.** The identity \(P_{m+4}-P_m=4Q_{m+2}\) telescopes to \(\sum_{j=1}^{k}Q_{4j}=(P_{4k+2}-2)/4\), giving
\[
8X_0=P_{4k+2}-2+4k.
\]
Using \(P_{4k+2}=3P_{4k}+2Q_{4k}\), \(P_{4k}=2P_{2k}Q_{2k}\), and \(Q_{4k}=1+4P_{2k}^{2}\) gives
\[
2X_0=k+3B_k C_k+8B_k^2,
\qquad16Y_0=3B_k C_k+8B_k^2-k.
\]
In particular,
\[
2X_0\equiv k\pmod{B_k},\qquad16Y_0\equiv-k\pmod{B_k}.
\]
For every odd prime \(p\ne3\), these congruences already show that the \(p\)-part of each of \(\gcd(X_0,48B_k)\) and \(\gcd(Y_0,6B_k)\) equals the \(p\)-part of \(\gcd(k,B_k)\).

**3. The prime \(3\).** For even \(k=2m\), we claim
\[
\nu_3(B_k)=1+\nu_3(k).
\]
Indeed \(\alpha^4=17+12\sqrt2\) and \(\beta^4=17-12\sqrt2\) are units in the unramified \(3\)-adic quadratic integer ring; their difference \(24\sqrt2\) has valuation exactly \(1\). The elementary odd-prime lifting identity for two units congruent modulo \(3\), proved by factoring when the exponent is prime to \(3\) and then cubing, yields
\[
\nu_3(\alpha^{4m}-\beta^{4m})=1+\nu_3(m).
\]
As \(P_{4m}=(\alpha^{4m}-\beta^{4m})/(2\sqrt2)\), and \(2\sqrt2\) is a \(3\)-adic unit, the claim follows. The two congruences in Step 2 now imply \(\nu_3(X_0)=\nu_3(Y_0)=\nu_3(k)\), strictly below \(\nu_3(B_k)\). Thus the additional factor \(3\) in each increment gcd contributes no extra common divisor.

**4. The prime \(2\).** Write \(u=P_{2k}/(2k)\), viewed as a \(2\)-adic integer. From \(\alpha^2=3+2\sqrt2\), \(\beta^2=3-2\sqrt2\), binomial expansion yields the exact finite sums
\[
u=\sum_{r\ge0}\frac{8^r}{2r+1}\binom{k-1}{2r}3^{k-1-2r},
\qquad C_k=\sum_{r\ge0}8^r\binom{k}{2r}3^{k-2r},
\]
where binomial coefficients outside their range vanish. Terms with \(r\ge2\) vanish modulo \(16\). For \(k\ge4\) even, the surviving terms give
\[
u\equiv3^{k-1}+8\binom{k-1}{2}3^{k-3}\pmod{16},
\qquad C_k\equiv3^k+8\binom{k}{2}3^{k-2}\pmod{16}.
\]
If \(k\equiv0\pmod4\), the first right-hand side is \(11+8\equiv3\), and the second is \(1\). If \(k\equiv2\pmod4\), the first is \(3\) and the second is \(9+8\equiv1\). At the boundary \(k=2\), direct evaluation gives \(u=3\) and \(C_2=17\). Hence for every positive even \(k\),
\[
u\equiv3\pmod{16},\qquad C_k\equiv1\pmod{16}.
\]
In particular \(B_k=ku\) has \(\nu_2(B_k)=\nu_2(k)=:a\ge1\). Rewriting the identities of Step 2 gives
\[
\frac{X_0}{k}=\frac{1+3uC_k}{2}+4ku^2,\qquad
\frac{Y_0}{k}=\frac{3uC_k-1}{16}+\frac{ku^2}{2}.
\]
The first expression is congruent to \(5\pmod8\), so \(\nu_2(X_0)=a\). In the second expression, \(3uC_k-1\equiv8\pmod{16}\): its first summand has valuation \(-1\), while its second has valuation \(a-1\ge0\). Therefore \(\nu_2(Y_0)=a-1\).

Combining Steps 2--4 prime by prime with the exact increment gcds of Step 1 gives
\[
\gcd(X_0,48B_k)=\gcd(k,B_k),\qquad
\gcd(Y_0,6B_k)=\frac{\gcd(k,B_k)}{2}.
\]
This proves both assertions for every positive even \(k\). \(\square\)

## Verification
Run `python3 verify.py` using the accompanying exact-integer script. It independently constructs the Pell, balancing, and Lucas-balancing sequences by integer recurrences, evaluates windows for even lengths \(2,4,\ldots,250\) and starting indices \(1,\ldots,80\), and compares their actual gcds with the two formulas. It also checks the crucial quadratic identity, the \(2\)-adic unit congruences, and the \(3\)-adic valuation formula over those indices. The accompanying output is in `verification-output.txt`. These finite calculations are supplementary evidence and are not substituted for the unrestricted proof.

## Relationship to prior work
Mbirika, Schrader, and Spilker (2023), Section 6.1, Question 30, explicitly ask for formulas for the square-window gcds of the balancing and Lucas-balancing sequences and record the even-window factor-of-two relation as numerical evidence. The theorem here proves that relation in the even case and supplies both exact values, not merely a ratio. Their Section 6.2 concerns gcds of sequence terms with their indices but does not give the present even-window square formulas. Cerin and Gianella (2006) provide explicit finite sum-of-squares identities for Pell--Lucas numbers; such sum formulas do not state or evaluate the gcd over all translates. Mbirika and Spilker (2022) treat generalized Fibonacci recurrences with coefficient \(1\), whereas the balancing recurrence has coefficient \(6\). The previously established odd-window case is a separate domain and is not asserted here.

## Limitations
The formula concerns only positive even window lengths and only the displayed standard sequences; it makes no claim about the cobalancing and Lucas-cobalancing square-window gcds or arbitrary recurrences. The proof uses standard strong divisibility of Pell numbers and an explicit local lifting argument at \(3\). Literature comparisons reduce but cannot eliminate the possibility of an equivalent result in unindexed sources. No external independent audit has been conducted.

## References
1. aBa Mbirika, Janee Schrader, and Jürgen Spilker, *Pell and Associated Pell Braid Sequences as GCDs of Sums of k Consecutive Pell, Balancing, and Related Numbers*, Journal of Integer Sequences **26** (2023), Article 23.6.4, Section 6.1, Question 30. First public preprint: arXiv:2301.05758 (2023-01-13). https://arxiv.org/abs/2301.05758 ; https://cs.uwaterloo.ca/journals/JIS/VOL26/Mbirika/mbir5.pdf
2. Zvonko Čerin and Gian Mario Gianella, *On Sums of Squares of Pell-Lucas Numbers*, Integers **6** (2006), #A15. https://math.colgate.edu/~integers/g15/g15.pdf
3. aBa Mbirika and Jürgen Spilker, *GCD of Sums of k Consecutive Squares of Generalized Fibonacci Numbers*, Fibonacci Quarterly **60** (2022), 255–269. First public preprint: arXiv:2204.12626 (2022-04-26). https://arxiv.org/abs/2204.12626
