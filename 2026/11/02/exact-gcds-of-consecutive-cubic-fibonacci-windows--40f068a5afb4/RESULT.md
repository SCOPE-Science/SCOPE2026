# Exact GCDs of consecutive cubic Fibonacci windows

## Finding

Let \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\); let \(L_0=2\), \(L_1=1\), and \(L_{n+2}=L_{n+1}+L_n\). For every integer \(k\ge1\), put
\[
S_k(n)=\sum_{j=0}^{k-1}F_{n+j}^{3},\qquad
G_3(k)=\gcd\{S_k(n):n\ge0\}.
\]
Define the positive integer
\[
H(k)=\begin{cases}
2,& k\equiv3\pmod6,\\
1,& k\equiv1,5\pmod6,\\
L_{k/2},& k\equiv2\pmod4,\\
F_{k/2},& 4\mid k.
\end{cases}
\]
Then the exact cubic-window GCD for every positive integer \(k\) is
\[
\boxed{G_3(k)=\frac{3^{\mathbf 1_{8\mid k}}}{2^{\mathbf 1_{6\mid k}}}\,H(k).}
\]
The denominator is integral because \(H(k)\) is even whenever \(6\mid k\). Equivalently, the even-length cases are \(L_{k/2}\), \(F_{k/2}\), or \(3F_{k/2}\), depending on \(k\bmod 8\), and each is halved precisely when \(6\mid k\). The result gives the exact values \(G_3(6)=2\), \(G_3(8)=9\), and \(G_3(24)=216\), with no finite bound on \(k\).

## Assumptions and scope

All indices are nonnegative integers and all GCDs are nonnegative greatest common divisors of integers. The theorem concerns the ordinary Fibonacci sequence and third powers; it does not assert a general formula for arbitrary initial conditions, Lucas cubes, or higher powers. The definition beginning at \(n=0\) is equivalent to that beginning at \(n=1\): the cubic Fibonacci sequence, and hence its finite window sums, satisfies a monic order-four integer recurrence whose constant term is a unit, allowing each zero-index term to be expressed integrally from later terms.

## Proof

**1. Reducing the infinite GCD to four differences.** The Binet roots of \(F_n^3\) are \(\alpha^3,\beta^3,-\alpha,-\beta\), where \(\alpha=(1+\sqrt5)/2\), \(\beta=(1-\sqrt5)/2\). Consequently \(F_n^3\) satisfies the integral recurrence with characteristic polynomial
\[
(t^2-4t-1)(t^2+t-1)=t^4-3t^3-6t^2+3t+1.
\]
For fixed \(k\), let \(\Delta_n=F_{n+k}^3-F_n^3\). Each \(\Delta_n\) satisfies the same recurrence, so \(D_k=\gcd_{n\ge0}\Delta_n=\gcd(\Delta_0,\Delta_1,\Delta_2,\Delta_3)\). Since \(S_k(n+1)-S_k(n)=\Delta_n\), a telescoping GCD identity gives
\[
G_3(k)=\gcd(S_k(0),D_k).
\]
Set \(x=F_k\), \(y=F_{k+1}\). We have \(\gcd(x,y)=1\), and the four differences are \(x^3\), \(y^3-1\), \((x+y)^3-1\), and \((x+2y)^3-8\). Subtracting the first two contributions from the last two yields
\[
D_k=\gcd\bigl(x^3,y^3-1,3xy(x+y),6xy(x+2y)\bigr).
\]
Using \(\gcd(x,y)=1\), the GCD of the final two displayed entries equals \(3xy\gcd(x+y,2)\). Hence, with \(\varepsilon=\gcd(x+y,2)\),
\[
\boxed{D_k=\gcd(x^3,y^3-1,3x\varepsilon).}\tag{1}
\]

**2. Evaluating the ordinary period factor.** Cassini's identity gives
\[
y^2-xy-x^2=(-1)^k.
\]
Therefore \(y^3-1\equiv(-1)^k y-1\pmod x\), and thus
\[
\gcd(x,y^3-1)=\gcd\bigl(x,y-(-1)^k\bigr)=:H_k.
\]
If \(k\) is odd, reducing Cassini modulo \(H_k=\gcd(F_k,F_{k+1}+1)\) gives \(1\equiv-1\pmod{H_k}\), so \(H_k\mid2\). Fibonacci parity has period three: \(F_k\) is even exactly when \(3\mid k\). This proves \(H_k=2\) for odd multiples of three and \(H_k=1\) for all other odd \(k\).

If \(k=2h\), standard addition and Cassini identities give
\[
F_{2h}=F_hL_h,\qquad
F_{2h+1}-1=\begin{cases}
F_hL_{h+1},&h\text{ even},\\
L_hF_{h+1},&h\text{ odd}.
\end{cases}
\]
Consecutive Fibonacci numbers, and consecutive Lucas numbers, are coprime. It follows that \(H_k=F_h\) when \(h\) is even and \(H_k=L_h\) when \(h\) is odd. Together, these give precisely \(H_k=H(k)\).

**3. The exceptional factor three in the difference GCD.** For primes \(p\ne2,3\), (1) gives \(v_p(D_k)=\min(v_p(x),v_p(y^3-1))=v_p(H_k)\). For \(p=2\), if \(x\) is odd neither GCD has a factor two. If \(x\) is even, then \(3\mid k\), \(\varepsilon=1\), and \(y\) is odd. The factor \(y^2+y+1\) is odd, so for even \(k\), equation (1) gives \(v_2(D_k)=\min(v_2(x),v_2(y-1))=v_2(H_k)\). For odd \(k\), the Fibonacci sequence modulo four shows \(v_2(x)=1\), and the same equality follows from (1) and \(H_k=2\).

Modulo three, Fibonacci numbers have period eight; thus \(3\mid x\) exactly when \(4\mid k\). When \(k\equiv4\pmod8\), we have \(y\equiv-1\pmod3\), so neither \(D_k\) nor \(H_k\) has a factor three. When \(8\mid k\), put \(h=k/2\), so \(4\mid h\). The Lucas sequence modulo three shows that both \(L_h\) and \(L_{h+1}\) are prime to three. The displayed addition identities give
\[
v_3(x)=v_3(y-1)=v_3(F_h)=:e\ge1.
\]
The lifting-the-exponent identity yields \(v_3(y^3-1)=e+1\). Equation (1) then gives \(v_3(D_k)=e+1\), while \(v_3(H_k)=e\). In all remaining cases \(3\nmid x\). We conclude that
\[
\boxed{D_k=3^{\mathbf1_{8\mid k}}H(k).}\tag{2}
\]

**4. Taking the GCD with the initial window.** Define the cubic polynomial \(P(X,Y)=-3X^3+3XY^2-Y^3\). Direct expansion gives
\[
P(Y,X+Y)-P(X,Y)=2X^3.
\]
Telescoping over the Fibonacci pairs yields
\[
\boxed{2S_k(0)=1-y^3+3xy^2-3x^3.}\tag{3}
\]
Equation (1) implies \(D_k\mid3x\): if \(\varepsilon=1\) directly, and if \(\varepsilon=2\), then \(x\) and \(D_k\) are odd. Using (1) and (3) therefore gives \(D_k\mid2S_k(0)\). When \(D_k\) is odd, \(G_3(k)=D_k\).

The even values of \(D_k\) occur precisely when \(3\mid k\). If \(k\) is odd, (2) gives \(D_k=2\). Every block of three consecutive Fibonacci numbers contributes an even number of odd terms, so \(S_k(0)\) is even, whence \(G_3(k)=D_k\).

If \(k\) is even and \(3\mid k\), write \(k=2h\) and \(e=v_2(D_k)=v_2(H_k)\). The factorization in Step 2, together with Fibonacci and Lucas parity, shows that \(x\) is divisible by \(2^{e+1}\), whereas \(y-1\) has exact valuation \(e\): for odd \(h\), the extra factor is the even \(F_h\) and \(F_{h+1}\) is odd; for even \(h\), the extra factor is the even \(L_h\) and \(L_{h+1}\) is odd. Since \(y\) is odd, \(y^2+y+1\) is odd. Formula (3) now shows that \(v_2(2S_k(0))=e\), hence \(v_2(S_k(0))=e-1\). All odd prime powers in \(D_k\) divide \(S_k(0)\), so \(G_3(k)=D_k/2\). Combining with (2) proves the theorem. \(\square\)

## Verification

Run `python3 verify_cubic_windows.py` using Python 3. The standalone script checks all lengths \(1\le k\le300\), computes window GCDs independently from 14 starts beginning at zero and 14 starts beginning at one, verifies all four-difference reductions and the compact formula for \(D_k\), checks the cubic telescoper, and checks the integral recurrence. It reports 8,400 finite window-sum comparisons. These calculations are independent sanity checks, not a replacement for the infinite proof above.

## Relationship to prior work

Guyer and Mbirika (2021, arXiv:2104.12262) proved exact window GCDs for first powers. Mbirika and Spilker (2022, arXiv:2204.12626), Section 6.1, explicitly raise extension to powers at least three and print conjectural cubic relations for even window lengths; their proved theorems concern squares. This theorem establishes a closed Fibonacci/Lucas formula for **all** positive lengths, including odd lengths and the exceptional powers of two and three. The case distinction in the cubic conjecture as printed in its 2023 arXiv revision does not reproduce the elementary values at \(k=2\) and \(k=6\); the present statement uses independently proved factors. Adegoke (2017, arXiv:1706.08469) supplies factored sums of cubic Fibonacci/Lucas subsequences, but does not claim the infinite shifted-window GCD classification.

## Limitations

The proof addresses only ordinary Fibonacci cubes. No assertion of analogous formulas for arbitrary Gibonacci initial conditions or Lucas cubes is made. Bibliographic searching and examination of the closest primary sources did not locate a prior proof of this complete statement, but unpublished or unindexed equivalent results remain possible. Finite checks do not independently certify the general proof. Independent expert audit has not been performed.

## References

1. D. Guyer and aBa Mbirika, *GCD of sums of \(k\) consecutive Fibonacci, Lucas, and generalized Fibonacci numbers*, Journal of Integer Sequences 24 (2021), Article 21.9.8; arXiv:2104.12262, first submitted 2021-04-25.
2. aBa Mbirika and J. Spilker, *GCD of sums of \(k\) consecutive squares of generalized Fibonacci numbers*, Fibonacci Quarterly 60 (2022), no. 5, 255–269; arXiv:2204.12626, first submitted 2022-04-26, especially Question 6.1.
3. K. Adegoke, *Factored closed-form expressions for the sums of cubes of Fibonacci and Lucas numbers*, arXiv:1706.08469, first submitted 2017-06-12.
