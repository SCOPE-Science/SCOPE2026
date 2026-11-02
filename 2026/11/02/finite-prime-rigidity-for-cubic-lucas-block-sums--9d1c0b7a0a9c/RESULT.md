# Finite-prime rigidity for cubic Lucas block sums

## Finding

Define the classical Lucas sequence by \(L_0=2\), \(L_1=1\), and \(L_{n+2}=L_{n+1}+L_n\). For every **even integer** \(k\ge2\), define positive integers

\[
D_k=\gcd_{n\ge0}\left(\sum_{j=1}^k L_{n+j}^{3}\right),\qquad
E_k=\gcd\bigl(L_{k+1}^{3}-1,\ L_{k+2}^{3}-27\bigr).
\]

Then \(D_k\mid E_k\), and every prime divisor of \(E_k/D_k\) belongs to

\[
\boxed{\{2,3,7,13,73\}}.
\]

Equivalently, for every prime \(p\notin\{2,3,7,13,73\}\) and every \(e\ge1\),

\[
p^e\mid D_k\quad\Longleftrightarrow\quad p^e\mid E_k.
\]

The three odd potential obstructions are genuinely necessary, in infinite families:

\[
\begin{array}{c|c|c|c}
p & \text{even lengths }k & D_{k_0} & E_{k_0}\\\hline
7 & k\equiv6\pmod{16} & 2 & 28\\
13 & k\equiv24\pmod{28} & 1080 & 28080\\
73 & k\equiv34\pmod{148} & 3571 & 260683
\end{array}
\]

Here the displayed exact values are at the first lengths \(k_0=6,24,34\) respectively; the congruence classes assert divisibility by the corresponding excess prime, not constancy of the gcds.

## Assumptions and scope

All indices \(n\) are nonnegative and all sums have exactly \(k\) consecutive positive Lucas indices. The length \(k\) is even. The infinite gcd \(D_k\) is unambiguously the positive gcd of its summands; the first four windows suffice to compute it, as proved below. The endpoint comparison uses \(L_1^3=1\) and \(L_2^3=27\), not the square \(L_2^2=9\). No assertion is made about odd \(k\) or about equality at the excluded primes.

## Proof

**1. Divisibility in one direction.** Write \(S_{n,k}=\sum_{j=1}^k L_{n+j}^{3}\). Direct subtraction gives

\[
S_{n+1,k}-S_{n,k}=L_{n+k+1}^{3}-L_{n+1}^{3}.
\]

In particular, the differences at \(n=0\) and \(n=1\) are \(L_{k+1}^{3}-1\) and \(L_{k+2}^{3}-27\). Therefore \(D_k\mid E_k\), and the quotient is an integer.

**2. A fixed norm conic.** The recurrence yields the Cassini-type identity

\[
L_{r+1}^{2}-L_rL_{r+1}-L_r^2=5(-1)^{r+1}
\]

for every \(r\ge0\). Since \(k\) is even, \(x=L_{k+1}\), \(y=L_{k+2}\) obey

\[
y^2-xy-x^2=5.
\]

Let \(p\) be an odd prime outside \(\{3,7,13,73\}\), and suppose \(p\mid E_k\). Modulo \(p\), one then has \(x^3=1\), \(y^3=27\). We claim \(x=1\), \(y=3\) modulo \(p\).

If \(p\equiv2\pmod3\), cubing is bijective on \(\mathbb F_p\) and the claim is immediate. If \(p\equiv1\pmod3\), choose a primitive cube root \(\omega\) and write \(x=\omega^i\), \(y=3\omega^j\) with \(i,j\in\{0,1,2\}\). The conic equation becomes

\[
h_{ij}:=9\omega^{2j}-3\omega^{i+j}-\omega^{2i}-5=0
\]

in \(\mathbb F_p\). Treating \(h_{ij}\) first as an Eisenstein integer and using \(\omega^2+\omega+1=0\), its algebraic norm is explicitly

\[
\begin{array}{c|ccc}
N(h_{ij}) & j=0&j=1&j=2\\\hline
i=0&0&189&189\\
i=1&39&75&219\\
i=2&39&219&75
\end{array}.
\]

The nonzero entries factor as \(189=3^3\cdot7\), \(39=3\cdot13\), \(75=3\cdot5^2\), and \(219=3\cdot73\). The case \(p=5\) is already covered by the bijective-cubing argument, because \(5\equiv2\pmod3\). For our allowed primes, no nonzero table entry can vanish modulo \(p\). Thus \(i=j=0\) is forced, proving \(x\equiv1\), \(y\equiv3\pmod p\).

**3. Lifting both endpoints.** Suppose now that \(p^e\mid E_k\) for one such prime and an arbitrary integer \(e\ge1\). Since \(x\equiv1\) and \(y\equiv3\pmod p\), the exact factorizations

\[
x^3-1=(x-1)(x^2+x+1),\qquad
 y^3-27=(y-3)(y^2+3y+9)
\]

have second factors congruent to \(3\) and \(27\), respectively, modulo \(p\). Neither is divisible by \(p\). Hence

\[
L_{k+1}\equiv1,\qquad L_{k+2}\equiv3\pmod{p^e}.
\]

The recurrence gives \(L_k=L_{k+2}-L_{k+1}\equiv2\pmod{p^e}\). The recurrence matrix is invertible over \(\mathbb Z/p^e\mathbb Z\); therefore \(L_{n+k}\equiv L_n\pmod{p^e}\) for every \(n\ge0\).

**4. Cubic telescoping.** Put \(H(u,v)=u^3-3uv^2+v^3\). A direct algebraic identity is

\[
H(u,v)-H(v,u+v)=2v^3.
\]

Consequently,

\[
2S_{n,k}=H(L_n,L_{n+1})-H(L_{n+k},L_{n+k+1}).
\]

The congruence just proved makes the right side divisible by \(p^e\). Since \(p\) is odd, \(p^e\mid S_{n,k}\) for every \(n\). Thus \(p^e\mid D_k\). Combined with Step 1, the valuations of \(D_k\) and \(E_k\) coincide outside \(\{2,3,7,13,73\}\).

**5. Infinite obstruction families.** Exact integer recurrence computations at \(k_0=6,24,34\) give the three pairs \((D_{k_0},E_{k_0})\) in the finding table. The Lucas state \((L_T,L_{T+1})\) equals \((2,1)\) modulo \(p\) for \((p,T)=(7,16),(13,28),(73,148)\), respectively. Therefore shifting \(k_0\) by any multiple of \(T\) preserves the endpoint pair modulo \(p\), and keeps \(p\mid E_k\). The telescoping identity applied to a full period shows that the sum of its Lucas cubes is zero modulo any odd prime \(p\); hence \(S_{n,k_0+tT}\equiv S_{n,k_0}\pmod p\) for each \(n\) and integer \(t\ge0\). Since at least one window at \(k_0\) is nonzero modulo \(p\), \(p\nmid D_{k_0+tT}\). This proves all three infinite congruence families.

**6. Computing the finite witness gcds exactly.** The sequence of cubes \(L_n^3\) satisfies the monic order-four recurrence with characteristic polynomial

\[
(T^2-4T-1)(T^2+T-1)=T^4-3T^3-6T^2+3T+1.
\]

This follows by cubing the two-term Binet expression: the four characteristic roots are \(\alpha^3,\beta^3,-\alpha,-\beta\), with \(\alpha\beta=-1\). The same recurrence holds for \(S_{n,k}\) in the variable \(n\). Therefore \(D_k=\gcd(S_{0,k},S_{1,k},S_{2,k},S_{3,k})\) for every positive \(k\). The finite witness values and periods are thus exact, not extrapolated from a truncated infinite gcd.

## Verification

Run the standalone file `verify.py` using Python 3. It checks the nine Eisenstein-norm computations without symbolic packages; exhaustively tests the finite-field conic implication for ninety eligible primes below \(502\); verifies 300 even window lengths through \(600\), including the order-four recurrence, the exact four-window gcd, and prime support of \(E_k/D_k\); and checks the three exact witness values, periods, and several subsequent lengths in each obstruction family. It returns `VERIFY_OK`. These tests independently corroborate finite consequences; Steps 1–5 are the unrestricted proof.

## Relationship to prior work

Mbirika and Spilker (arXiv:2204.12626, first publicly posted 26 April 2022), particularly Section 6.1, study GCDs of consecutive powers of Fibonacci and Lucas terms and ask about cubed windows. Their proven general formulas concern squares, and their cubed-window discussion supplies proposed endpoint expressions rather than this prime-support rigidity theorem. The displayed Lucas proposal uses \(L_{k+2}^3-9\), whereas the genuine endpoint difference of cubes needed here is \(L_{k+2}^3-27\); the present theorem is deliberately stated only for the latter and does not assert the proposed expression is correct. Guyer and Mbirika (arXiv:2104.12262) prove endpoint GCD formulas for *first powers*. A separate exact result on cubic **Fibonacci** windows concerns a different initial sequence and does not imply the Lucas conic obstruction. The new arithmetic information here is a finite universal exceptional-prime support and three infinite, witnessed obstruction families.

## Limitations

No values of the two gcds at the excluded primes are classified uniformly, and the prime \(3\) is only retained as a possible obstruction, not shown necessary. The theorem is restricted to even block lengths and the classical Lucas sequence. It establishes equality of local prime-power divisibility outside the exceptional set, not a complete integer formula for either gcd. A prior general theorem indirectly implying the precise finite-prime classification would affect originality; no absolute priority claim is made. Independent scientific validation has not been performed.

## References

1. aBa Mbirika and Jürgen Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, arXiv:2204.12626, version 1 first posted 2022-04-26; especially Section 6.1 of version 2. https://arxiv.org/abs/2204.12626
2. Dan Guyer and aBa Mbirika, *GCD of sums of k consecutive Fibonacci, Lucas, and generalized Fibonacci numbers*, arXiv:2104.12262 (2021), Journal of Integer Sequences 24, Article 21.9.8. https://arxiv.org/abs/2104.12262
