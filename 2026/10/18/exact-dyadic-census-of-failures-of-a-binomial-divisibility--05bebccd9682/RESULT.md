# Exact dyadic census of failures of a binomial divisibility

## Finding

For each integer \(L\geq0\), define
\[
F_L=\#\left\{n\in\mathbb Z:1\leq n<2^L,\quad (3n+1)\nmid\binom{5n}{2n}\right\}.
\]
The complete dyadic enumeration of the nondivisibility instances is
\[
\boxed{\sum_{L\geq0}F_Lz^L=\frac{z(1+z)}{1-z-z^2+z^3-z^4}}.
\]
In particular, \(F_0=0\), \(F_1=1\), \(F_2=2\), \(F_3=3\), \(F_4=4\), and, for every \(L\geq5\),
\[
\boxed{F_L=F_{L-1}+F_{L-2}-F_{L-3}+F_{L-4}}.
\]
The initial counts are \(0,1,2,3,4,6,9,14,21,32,48,73,110,167,252,382\). If \(\lambda\) is the largest positive root of
\[
\lambda^4-\lambda^3-\lambda^2+\lambda-1=0,
\]
then \(\lambda\approx1.51287639686409\) and
\[
F_L\sim c\lambda^L,\qquad
c=-\frac{1+\rho}{Q'(\rho)}>0,\quad
\rho=\lambda^{-1},\quad Q(z)=1-z-z^2+z^3-z^4.
\]
The exponent \(\log_2\lambda\approx0.5972941231\) quantifies the sparse but infinite family of failures. In particular, these exceptional integers have natural density zero.

## Assumptions and scope

All quantities are over ordinary nonnegative integers. The fixed binomial ray is \(\binom{5n}{2n}\), with the divisibility test \(3n+1\). The level \(L\) counts \(n\) below \(2^L\), not the integers of exactly \(L\) binary digits. The case \(L=0\) is empty. We write \(\nu_2(m)\) for the exponent of \(2\) in a positive integer \(m\). The variable \(z\) is formal for the rational generating-function identity. Only this fixed pair of slopes is enumerated; no conclusion is asserted for arbitrary pairs.

## Proof

**1. Only a single factor of two can obstruct divisibility.** For \(n\geq1\), put \(T=5n+1\) and \(A=2n\). Counting all \(A\)-element subsets of a cyclic set of \(T\) positions by rotation, any orbit has size \(T/d\), where its stabilizer order \(d\) divides \(\gcd(T,A)=\gcd(n+1,2)\). Thus
\[
\frac{T}{\gcd(n+1,2)}\ \bigg|\ \binom{T}{A}.
\]
The identity
\[
\frac1T\binom{T}{A}=\frac{1}{3n+1}\binom{5n}{2n}
\]
shows that every even \(n\) passes the divisibility test, whereas for odd \(n\) the quotient on the right is an integer or a half-integer. Accordingly, for odd \(n\), failure is **equivalent** to
\[
\nu_2\binom{5n}{2n}=\nu_2(3n+1)-1.\tag{1}
\]
This also reproves the relevant case of Sun's divisibility bound, without assuming it.

**2. The binary carry condition.** By Kummer's theorem, the valuation on the left of (1) is precisely the number of carries when adding \(2n\) and \(3n\) in base two. For odd \(n\), put \(h=\nu_2(3n+1)\). The base-two digits of \(3n\) are \(1\) in positions \(0,\ldots,h-1\) and \(0\) in position \(h\). Bit zero of \(2n\) is \(0\), so it makes no carry. Bit one of \(2n\) is \(1\); therefore at each position \(1,\ldots,h-1\) a carry is forced. The minimum possible total is \(h-1\). Equality in (1) occurs precisely if **all** later carry-outs, from position \(h\) onward, vanish.

**3. A seven-state exact finite automaton.** Read the base-two digits of odd \(n\) from least significant to most significant, including sufficiently many leading zero digits. The compulsory first bit is \(1\), after which the state is \(A=(1,0,0,0)\). A state \((p,a,b,q)\) stores the preceding input bit \(p\), the carry \(a\) in forming \(3n=n+2n\), the carry \(b\) in forming \(5n=3n+2n\), and a phase \(q\): phase zero means all bits of \(3n\) observed so far are ones; phase one means its first zero has occurred. For a new input digit \(u\in\{0,1\}\), set
\[
s=u+p+a,\quad v=s\bmod2,\quad a'=\lfloor s/2\rfloor,\quad
b'=\lfloor(v+p+b)/2\rfloor.
\]
In phase zero a transition is permitted only if \(b'=1\) when \(v=1\), or \(b'=0\) when \(v=0\); the latter switches to phase one. In phase one a transition is permitted only when \(b'=0\). The new state is \((u,a',b',q\lor(v=0))\). These conditions count precisely the carries forced by the trailing ones and forbid all subsequent carries. The forced bit \(n_0=1\) has no carry, so it needs no special transition.

The reachable states \(A,B,C,D,E,F,G\), their two transitions for digit \(0\) or \(1\), and acceptance after adding infinitely many terminal zero bits are as follows. A dash means a forbidden transition:

| State | \((p,a,b,q)\) | input 0 | input 1 | zero-tail accepted |
|---|---|---|---|---|
| A | \((1,0,0,0)\) | B | C | yes |
| B | \((0,0,1,0)\) | D | E | yes |
| C | \((1,1,0,1)\) | F | — | yes |
| D | \((0,0,0,1)\) | D | G | yes |
| E | \((1,0,1,0)\) | B | — | yes |
| F | \((0,1,0,1)\) | D | C | yes |
| G | \((1,0,0,1)\) | — | C | no |

All seven states are reachable. Terminal acceptance has been checked under the actual infinite zero tail, not by discarding possible high carries. Let \(G_A(z),\ldots,G_G(z)\) be the generating functions for accepted continuations in each state, with one power of \(z\) per additional digit. The table gives the **exact** formal equations
\[
\begin{aligned}
G_A&=1+z(G_B+G_C),&G_B&=1+z(G_D+G_E),\\
G_C&=1+zG_F,&G_D&=1+z(G_D+G_G),\\
G_E&=1+zG_B,&G_F&=1+z(G_D+G_C),\\
G_G&=zG_C.
\end{aligned}
\]
Put \(Q(z)=1-z-z^2+z^3-z^4\). Direct substitution verifies that these seven equations have the unique formal-power-series solution \(G_i=H_i/Q\), with numerator vector
\[
(H_A,H_B,H_C,H_D,H_E,H_F,H_G)
=(1+z,\ 1+z-z^2+z^3,\ 1,\ 1+z^3,\ 1,\ 1+z-z^2+z^3,\ z).
\]
The uniqueness follows from the constant term \(1\) in the coefficient matrix \(I-zM\). Every odd \(n<2^L\) has exactly \(L-1\) free digits after its first bit, hence contributes to \(F_L=[z^{L-1}]G_A\) for \(L\geq1\). Since \(G_A=(1+z)/Q\) and \(F_0=0\), the claimed rational generating function follows. Coefficient extraction proves the recurrence and all boundary values.

**4. Growth and sparsity.** The nonnegative transition matrix has a strongly connected class on states \(C,D,F,G\), with a self-loop at \(D\), so this class is primitive. Its characteristic polynomial is \(\lambda^4-\lambda^3-\lambda^2+\lambda-1\). The other recurrent component \(B,E\) has spectral radius \(1\), while \(A\) is transient. Perron--Frobenius gives a unique simple dominant positive eigenvalue \(\lambda>1\). Equivalently, \(Q\) has a unique simple pole \(\rho=1/\lambda\) of smallest modulus. The numerator \(z(1+z)\) does not vanish there. The simple-pole coefficient formula yields the stated positive \(c\) and asymptotic. If \(2^{L-1}\leq X<2^L\), the count of failures up to \(X\) is at most \(F_L=O(\lambda^L)=O(X^{\log_2\lambda})=o(X)\), proving natural density zero. The asymptotic also proves infinitely many failures.

## Verification

Run `python verify.py` using Python 3's standard library. The verifier checks all seven numerator-polynomial identities as **exact integer polynomial equalities**, verifies the transition rule directly from digit arithmetic, compares exact binomial divisibility for every integer \(1\leq n<600\), and tests the carry/valuation characterization for all \(1\leq n<16384\). It independently matches nineteen finite-state counts against the scalar recurrence and prints `VERIFY_OK`. These finite checks corroborate, but do not replace, the formal proof for all levels.

## Relationship to prior work

Sun's 2010 Theorem 1.4 gives the general gcd-based divisor and raises the qualitative question of exception behavior. Guo and Krattenthaler's 2013 Theorem 2.1 proves existence of infinitely many exceptions for the relevant slopes, but does not enumerate the dyadic exceptions. A prior finite-state result for the same binomial ray determined the **marginal** distribution of \(\nu_2\binom{5n}{2n}\) across all \(n<2^L\). Marginal valuation counts alone do not decide whether that valuation equals the index-dependent target \(\nu_2(3n+1)-1\). The present census instead counts the **joint carry-trailing-ones event** and gives its exact rational series and growth exponent. The overlap with the prior carry approach is methodological and the denominator polynomial is shared; the asserted arithmetical enumeration is distinct. These comparisons are under accessible-source scope, not a certified uniqueness claim.

## Limitations

The argument treats only the fixed parameters \((2,3)\); it neither characterizes exception densities for arbitrary slopes nor provides individual primality information. The leading asymptotic is along dyadic cutoff levels; the natural-density conclusion holds for all cutoffs, but no uniform non-dyadic second-order asymptotic is asserted. Broader unlocated automatic-sequence or binomial-divisibility results could imply the enumeration. Independent mathematical and bibliographic assessments remain outstanding.

## References

1. Zhi-Wei Sun, *On divisibility concerning binomial coefficients*, arXiv:1005.1054 (first submitted May 6, 2010), Theorem 1.4 and Section 1. https://arxiv.org/abs/1005.1054
2. Victor J. W. Guo and C. Krattenthaler, *Some divisibility properties of binomial and q-binomial coefficients*, arXiv:1301.7651 (first submitted January 31, 2013), Theorems 1.1 and 2.1. https://arxiv.org/abs/1301.7651
3. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen*, J. Reine Angew. Math. 44 (1852), 93–146 (base-prime carry theorem).
