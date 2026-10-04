# Fixed-prime-support asymptotics for refactorable numbers
## Finding
Let \(S=\{p_1,\ldots,p_m\}\) be a fixed nonempty finite set of primes, and let \(R_S(x)\) count positive integers \(n\le x\) whose set of prime divisors is exactly \(S\) and for which the divisor count \(\tau(n)\) divides \(n\). Then
\[
R_S(x)\sim
\frac{(\log\log x)^{m^2}}
{(m!)^m\prod_{j=1}^m(\log p_j)^m}
\qquad (x\to\infty).
\]

There is also an exact exponent criterion. Writing
\[
n=\prod_{i=1}^m p_i^{a_i},\qquad a_i\ge1,
\]
the number \(n\) is refactorable if and only if there are uniquely determined nonnegative integers \(e_{ij}\) such that
\[
a_i+1=\prod_{j=1}^m p_j^{e_{ij}}
\quad(1\le i\le m),
\]
and, for every \(j\),
\[
\sum_{i=1}^m e_{ij}\le a_j.
\]

## Assumptions and scope
The prime set \(S\) is fixed while \(x\to\infty\). Exact prime support means every prime in \(S\) occurs with a positive exponent and no prime outside \(S\) occurs. The function \(\tau\) is the ordinary positive-divisor counting function.

Colton's 1999 paper defines refactorable numbers by \(\tau(n)\mid n\), gives the standard prime-exponent formula for \(\tau(n)\), constructs infinite families, and counts refactorable numbers with a prescribed number of divisors. Spiro's earlier work gives a global counting estimate for all refactorable numbers. The result here instead resolves the asymptotic inside every fixed exact prime support.

## Proof
Put \(\lambda_j=\log p_j\). For
\[
n=\prod_{i=1}^m p_i^{a_i},
\]
we have
\[
\tau(n)=\prod_{i=1}^m(a_i+1).
\]
If \(\tau(n)\mid n\), every prime factor of every \(a_i+1\) belongs to \(S\). Thus there are unique \(e_{ij}\ge0\) with
\[
a_i+1=\prod_{j=1}^m p_j^{e_{ij}}.
\]
Moreover,
\[
\nu_{p_j}(\tau(n))=\sum_{i=1}^m e_{ij},
\]
so divisibility by \(n\) is equivalent to
\[
\sum_i e_{ij}\le a_j
\]
for every \(j\). This proves the exact criterion, including the converse.

Let \(H_S(y)\) be the number of \(S\)-smooth positive integers not exceeding \(y\). Such integers correspond to lattice points
\[
(r_1,\ldots,r_m)\in\mathbb Z_{\ge0}^m,
\qquad
\sum_{j=1}^m r_j\lambda_j\le\log y.
\]
The elementary simplex lattice-point estimate gives
\[
H_S(y)=C_S(\log y)^m+O((\log y)^{m-1}),
\qquad
C_S=\frac1{m!\prod_{j=1}^m\lambda_j}.
\]

Write \(L=\log x\) and \(T=\log L=\log\log x\). Set \(A_i=a_i+1\). If the column inequalities are temporarily ignored, the size condition is
\[
\sum_{i=1}^m (A_i-1)\lambda_i\le L,
\]
with each \(A_i\) an \(S\)-smooth integer at least \(2\). Call the number of these unrestricted tuples \(U_S(L)\).

For the upper bound, every admissible tuple has
\[
A_i\le 1+L/\lambda_i,
\]
so
\[
U_S(L)\le\prod_{i=1}^m H_S(1+L/\lambda_i)
=(C_S^m+o(1))T^{m^2}.
\]
For the lower bound, restrict independently to
\[
2\le A_i\le L/(m\lambda_i).
\]
Then \(\sum_i(A_i-1)\lambda_i<L\), and therefore
\[
U_S(L)\ge\prod_{i=1}^m\bigl(H_S(L/(m\lambda_i))-1\bigr)
=(C_S^m+o(1))T^{m^2}.
\]
Hence
\[
U_S(L)\sim C_S^mT^{m^2}.
\]

It remains to restore the column inequalities. In every tuple counted by \(U_S(L)\), each exponent \(e_{ij}\) is \(O(T)\), with constants depending only on \(S\). Thus there is a fixed \(K_S>0\) such that
\[
\sum_i e_{ij}\le K_ST
\]
for every column \(j\) once \(x\) is large. Consequently, any unrestricted tuple with
\[
A_j-1>K_ST\quad\text{for all }j
\]
automatically satisfies all divisibility inequalities.

The exceptional tuples have \(A_j\le K_ST+1\) for at least one \(j\). For a specified \(j\), the number of choices for that coordinate is
\[
H_S(K_ST+1)=O((\log T)^m),
\]
while each of the other \(m-1\) coordinates has \(O(T^m)\) choices. A union bound therefore gives
\[
O\!\left(T^{m(m-1)}(\log T)^m\right)=o(T^{m^2})
\]
exceptional tuples. Removing the finitely many choices with some \(A_i=1\) is also lower order. Thus
\[
R_S(x)\sim C_S^mT^{m^2},
\]
which is the stated formula.

## Verification
The included `verify.py` checks the exact exponent criterion against direct divisibility by \(\tau(n)\) for finite exponent boxes on several prime supports. It also enumerates the two-prime exponent lattice at increasing logarithmic scales and prints the ratio to the proved leading term as a numerical sanity check. These computations are not used to prove the asymptotic.

## Relationship to prior work
Colton's full article develops refactorable numbers, including the definition, the factorization formula for \(\tau(n)\), infinite constructions, membership restrictions, and a theorem counting refactorable numbers with a fixed value of \(\tau(n)\). Those results do not count refactorable numbers having a fixed set of prime divisors. Spiro's 1985 theorem concerns the global counting function over all prime supports and does not specialize to the fixed-support constant above.

Targeted searches for “refactorable”, “tau number”, “fixed prime support”, smooth exponent shifts, and the predicted \((\log\log x)^{m^2}\) scale found no same or stronger statement. The closest available database results concern fixed-support exponent lattices for weak Carmichael numbers, relative tau-divisibility by cyclotomic polynomials, and unrelated prime-index lattice asymptotics.

## Limitations
The support \(S\) must be fixed. No uniform estimate is claimed when either the number of supporting primes or the primes themselves vary with \(x\), and no effective error term is optimized. The originality search covered the principal refactorable-number sources located, the available indexed research corpus corpus, and targeted web searches, but cannot rule out an obscure equivalent historical formulation.

## References
1. S. Colton, “Refactorable Numbers - A Machine Invention,” *Journal of Integer Sequences* 2 (1999), Article 99.1.2.
2. C. Spiro, “How Often Is the Number of Divisors of \(n\) a Divisor of \(n\)?,” *Journal of Number Theory* 21 (1985), 81–100, doi:10.1016/0022-314X(85)90012-5.
3. R. E. Kennedy and C. N. Cooper, “Tau Numbers, Natural Density, and Hardy and Wright's Theorem 437,” *International Journal of Mathematics and Mathematical Sciences* 13 (1990), 383–386, doi:10.1155/S0161171290000576.
