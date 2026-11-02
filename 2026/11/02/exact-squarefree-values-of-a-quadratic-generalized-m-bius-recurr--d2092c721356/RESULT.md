# Exact squarefree values of a quadratic generalized Möbius recurrence

## Finding

Fix the **quadratic specialization** of the generalized Möbius recurrence introduced by Andrews, Kauffman and Sahoo: define the integer-valued arithmetic function \(a\) by \(a(1)=1\) and, for every integer \(n\ge 2\),
\[
a(n)=1-n-\sum_{d=2}^{n-1}a(d)\left\lfloor\frac nd\right\rfloor^2.
\]
Define the positive integer constants
\[
C_j=\sum_{\ell=1}^{\infty}\frac{\ell^j}{2^\ell}\quad(j\ge0),
\qquad C_0=1,\ C_1=2,\ C_2=6,\ C_3=26.
\]
**Theorem (one exact squarefree evaluation with its full-domain consequence).** For every squarefree integer \(n>1\), write \(P(n)\) for the set of its distinct prime divisors and \(k=|P(n)|\). Then
\[
\boxed{a(n)=(-1)^k\sum_{T\subsetneq P(n)}C_{|T|}\prod_{p\in T}(p-1).}
\]
The empty product equals \(1\). In addition, for **every** positive integer \(n\),
\[
\boxed{a(n)\equiv\mu(n)\pmod2.}
\]
Consequently, for every integer \(n\ge2\), \(a(n)=-1\) if and only if \(n\) is prime. In fact, if \(n\) is squarefree with at least two prime factors, then
\[
(-1)^k a(n)\ge 1+2\sum_{p\mid n}(p-1)>1;
\]
whereas for nonsquarefree \(n\), the integer \(a(n)\) is even. For example, \(a(pq)=2p+2q-3\) for distinct primes \(p,q\), while \(a(30)=-99\).

The sequence \((C_j)\) can be evaluated by finite integer arithmetic. For \(j\ge1\), with \(\left\{\begin{smallmatrix}j\\r\end{smallmatrix}\right\}\) denoting a Stirling number of the second kind,
\[
C_j=2\sum_{r=1}^j r!\left\{\begin{matrix}j\\r\end{matrix}\right\}.
\]
Thus the displayed formula is exact, not a limiting or numerical expression.

## Assumptions and scope

The arithmetic function \(a\) is integer-valued and uniquely specified for all \(n\ge1\) by the recurrence above. No primality, squarefreeness or analytic hypothesis is imposed on its definition. The closed prime-subset formula applies only to squarefree \(n>1\); the parity statement and its primality consequence apply to **all** positive integers. The primary subject is multiplicative and divisor-sum number theory (MSC2020 11A25). The motivating source was first made public on 2026-09-22.

## Proof

**1. Reduction to the divisor recurrence.** Subtract the defining recurrence at \(n-1\) from its equivalent cumulative form at \(n\). Equivalently, perform finite differencing on the floor terms. Since \(\lfloor n/d\rfloor\) changes between \(n-1\) and \(n\) exactly when \(d\mid n\), one obtains, for every \(n>1\),
\[
\boxed{a(n)=-1-\sum_{\substack{d\mid n\\1<d<n}}a(d)\left(2\frac nd-1\right).}\tag{1}
\]
This is the published generalized-divisor recurrence specialized to \(f(m)=m^2\); it also follows directly by elementary finite differences. At a prime, the sum in (1) is empty, giving \(a(p)=-1\).

**2. Parity on all inputs.** Each factor \(2n/d-1\) in (1) is odd. Suppose inductively \(a(d)\equiv\mu(d)\pmod2\) for proper divisors \(d\) of \(n\). As \(\sum_{d\mid n}\mu(d)=0\) when \(n>1\), (1) gives
\[
a(n)\equiv-1-\sum_{\substack{d\mid n\\1<d<n}}\mu(d)\equiv\mu(n)\pmod2.
\]
The base case \(a(1)=\mu(1)=1\) completes induction. In particular, if \(n\) is not squarefree, then \(a(n)\) is even and cannot equal \(-1\).

**3. Exact values on squarefree inputs.** Fix \(n=\prod_{i=1}^k p_i\), where the \(p_i\) are distinct primes and \(k\ge1\). Work in the finite, commutative nilpotent algebra
\[
R=\mathbb Q[z_1,\ldots,z_k]/(z_1^2,\ldots,z_k^2).
\]
For \(U\subseteq\{1,\ldots,k\}\), put \(z_U=\prod_{i\in U}z_i\) and \(n_U=\prod_{i\in U}p_i\) (empty products are \(1\)). Define
\[
A=\prod_i(1+z_i),\quad B=\prod_i(1+p_i z_i),\quad G=2B-A,
\quad S=\sum_U a(n_U)z_U.
\]
The coefficient of \(z_U\) in \(G\) is \(2n_U-1\). By (1), the coefficient of \(z_U\) in \(SG\) is \(2n_U-2\) for every nonempty \(U\), and equals \(1\) for the empty set. Therefore
\[
SG=2B-2A+1=G-(A-1),\qquad S=1-(A-1)G^{-1}.\tag{2}
\]
All inverses exist because their constant terms equal \(1\). In \(R\), \(A^{-1}=\prod_i(1-z_i)\), while
\[
\frac BA=\prod_i(1+(p_i-1)z_i)=\exp(w),\qquad
w=\sum_i(p_i-1)z_i.
\]
Consequently (2) becomes
\[
S=1-H(w)+A^{-1}H(w),\quad
H(w)=\frac1{2e^w-1}=\sum_{\ell\ge1}2^{-\ell}e^{-\ell w}.
\]
This last identity is a convergent power-series identity near \(w=0\), and may be evaluated in \(R\) because \(w\) is nilpotent. Its coefficient of \(w^j/j!\) is \((-1)^j C_j\). Hence for any \(T\subseteq\{1,\ldots,k\}\),
\[
[z_T]H(w)=(-1)^{|T|}C_{|T|}\prod_{i\in T}(p_i-1).
\]
Extracting the coefficient of \(z_1\cdots z_k\) from \(S\) gives
\[
\begin{aligned}
a(n)&=-(-1)^k C_k\prod_i(p_i-1)
+(-1)^k\sum_{T\subseteq\{1,\ldots,k\}}
 C_{|T|}\prod_{i\in T}(p_i-1)\\
&=(-1)^k\sum_{T\subsetneq\{1,\ldots,k\}}
 C_{|T|}\prod_{i\in T}(p_i-1),
\end{aligned}
\]
as required.

**4. Positivity and the prime criterion.** Every \(C_j\) is positive. For \(k=1\), the only proper subset is empty, so \(a(p)=-1\). For \(k\ge2\), the empty and all singleton subsets are proper. Their contributions give \((-1)^k a(n)\ge1+C_1\sum_{p\mid n}(p-1)>1\). Therefore no squarefree composite can give \(-1\). Step 2 excludes every nonsquarefree composite; primes attain \(-1\) by step 1. This proves the assertion for every integer \(n\ge2\).

**5. Integrality of the coefficients.** The exponential generating function \(H(w)\) yields the finite recurrence
\[
C_0=1,\qquad
C_j=-2\sum_{r=1}^j(-1)^r\binom jr C_{j-r}\quad(j\ge1).
\]
Alternatively the geometric distribution with mass \(2^{-\ell}\) at \(\ell\ge1\) has falling-factorial moments \(2r!\) for every \(r\ge1\). Expanding powers in the falling-factorial basis gives the stated Stirling formula. Both establish \(C_j\in\mathbb Z\).

## Verification

The standalone standard-library program `verify.py` independently computes the original floor recurrence on \(2\le n\le900\), computes the divisor recurrence on \(2\le n\le10000\), and checks both against the exact squarefree formula, Möbius parity and prime criterion using an integer factorization sieve. Its successful output is:

```text
VERIFY_OK n_max=10000 original_recurrence=900 squarefree_exact=6082 nonsquarefree_parity=3917 primes=1229 moment_values=[1, 2, 6, 26, 150, 1082] arithmetic=exact
```

These are finite consistency checks. The proof in the preceding section, not an extrapolation from the computation, establishes the infinite statements. Reproduce with `python3 verify.py` in the directory containing the script; no third-party packages or external data are required.

## Relationship to prior work

Andrews, Kauffman and Sahoo introduce the generalized recurrence, provide its equivalent divisor form, discuss power kernels and give exact values at prime squares and products of two distinct primes. Their Theorem 1 is worded as a primality equivalence for the family, but its proof's composite direction explicitly establishes only that the recurrence cannot give \(-1\) **identically across all admissible functions**. That symbolic statement does not yield a fixed-kernel criterion, and neither it nor the source's two-prime evaluation supplies the displayed formula for arbitrarily many squarefree prime factors.

An earlier result for **this same quadratic recurrence** establishes sharp dyadic vanishing, \(a(2^h m)=0\) for odd \(m\) and \(h\ge\Omega(m)+3\), with a positive value at the preceding layer. It also writes the recurrence as an implicit Dirichlet-convolution inverse. That theorem controls a high-dyadic-exponent boundary, not arbitrary squarefree values (in particular the odd squarefree slice), and it does not state the exact moment-polynomial or the all-input parity and fixed-kernel prime consequences. The recurrence and its formal inverse are used as starting identities, not claimed as newly discovered here.

The published observation that the constant choice \(f(m)=1\) returns \(-1\) at every \(n\ge2\) further illustrates why a kernel-specific proof is necessary. The present contribution is the complete squarefree value formula with its positive moment coefficients, coupled to an all-integer parity argument; the primality criterion is a consequence. Standard Möbius inversion alone supplies neither the nonlinear squarefree formula nor its sign/magnitude control.

## Limitations

The exact subset formula is proved for squarefree inputs only; nonsquarefree inputs are controlled here only modulo two, not by a full closed evaluation. The prime criterion is mathematical, not presented as an efficient alternative to factorization or sieving. No quantitative complexity bound, analytic asymptotic or claim of independent historical-priority certification is made. An undiscovered equivalent expression in earlier recurrence literature remains a genuine priority risk. The motivating paper's broader pointwise wording should not be used as a substitute for its displayed proof.

## References

1. G. E. Andrews, L. H. Kauffman, D. Sahoo, *A surprising generalization of the Möbius function*, arXiv:2609.25628v1 (first posted 2026-09-22), Section 1 and Proposition 1, https://arxiv.org/abs/2609.25628.
2. Classical Möbius divisor identity: \(\sum_{d\mid n}\mu(d)=0\) for every \(n>1\).
3. Classical Stirling expansion of ordinary powers into falling factorials, used to evaluate the geometric moments \(C_j\).
