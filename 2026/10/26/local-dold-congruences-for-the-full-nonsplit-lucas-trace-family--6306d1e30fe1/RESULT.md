# Local Dold congruences for the full nonsplit Lucas trace family

## Finding
Let \(P\ge3\) be any integer, and define its companion Lucas sequence by
\[
V_0=2,\qquad V_1=P,\qquad V_{n+2}=PV_{n+1}+V_n.
\]
For every prime \(p\), set \(a_p(n)=p^{\nu_p(V_n)}\) for \(n\ge1\), and let \(T_p(n)=\sum_{d\mid n}\mu(n/d)a_p(d)\). The **local Dold property** means \(n\mid T_p(n)\) for every \(n\ge1\). Define the least repair factor \(K_p\) as the least positive integer such that \(n\mid K_pT_p(n)\) for every \(n\ge1\).

**Theorem.** For odd \(p\) put \(\Delta=P^2+4\) and let \(\chi_p=(\Delta/p)\), the quadratic Legendre symbol (zero when \(p\mid\Delta\)). Then the following are equivalent: (i) the local \(p\)-part fails the Dold property; (ii) \(\chi_p=-1\) and \(p\equiv3\pmod4\). If this happens, let \(\lambda_p=\min\{n\ge1:p\mid V_n\}\); then \(\lambda_p\) is even and \(K_p=\lambda_p\). At all other odd primes, \(K_p=1\). At \(p=2\), the least repair factor is \(3\) when \(P\) is odd, and \(1\) when \(P\) is even. Thus every local prime part is **almost Dold**, in the sense of a finite repair factor; the odd Dold primes have natural relative density \(3/4\) among all primes, for every fixed \(P\ge3\).

The complete signed transforms are explicit. For an odd prime with no zero of \(V_n\) modulo \(p\), \(T_p(1)=1\) and all later transforms vanish. Otherwise put \(\lambda=\lambda_p\) and \(e=\nu_p(V_\lambda)\). The transform has \(T_p(1)=p^e\) if \(\lambda=1\), and \(T_p(1)=1\) otherwise; its remaining possible nonzero values are
\[
\begin{aligned}
T_p(\lambda)&=p^e-1&& (\lambda>1),\\
T_p(2\lambda)&=1-p^e,\\
T_p(\lambda p^j)&=p^{e+j-1}(p-1)&& (j\ge1),\\
T_p(2\lambda p^j)&=-p^{e+j-1}(p-1)&& (j\ge1).
\end{aligned}
\]
All unspecified terms are zero. For \(p=2\): if \(P\) is even and \(s=\nu_2(P)\), the only nonzero terms are \(T_2(1)=2^s\) and \(T_2(2)=2-2^s\); if \(P\) is odd they are \(T_2(1)=1\), \(T_2(3)=3\), \(T_2(6)=-2\).

**Local realizability.** In the usual periodic-orbit sense, requiring every \(T_p(n)\ge0\) as well as \(n\mid T_p(n)\), the odd prime parts are realizable exactly when no \(V_n\) vanishes modulo \(p\); the \(2\)-part is realizable exactly when \(P\equiv2\pmod4\). This distinguishes signed congruence integrality from nonnegative orbit counts.

## Assumptions and scope
The integer parameter \(P\ge3\) is fixed. All \(V_n\) are positive integers; \(\nu_p\), \(\mu\), Legendre symbols, and Dold congruences have their standard meanings. The odd-prime formulas apply equally to the ramified primes dividing \(\Delta\) (which have no trace zeros). The natural prime density assertion ignores only the finitely many ramified primes. No uniform error term in \(P\) is asserted.

## Proof
**1. Rank of a trace zero.** Work in an algebraic closure of \(\mathbb F_p\), where \(p\) is odd. The roots \(\alpha,\beta\) of \(X^2-PX-1\) have product \(-1\), and \(V_n=\alpha^n+\beta^n\). If \(p\mid\Delta\), the roots coincide at a nonzero \(r\), so \(V_n=2r^n\ne0\pmod p\) for all \(n\). Otherwise set \(w=\alpha/\beta\), with finite multiplicative order \(z\). A trace zero occurs iff \(w^n=-1\). Therefore it occurs iff \(z\) is even; its least positive index is \(\lambda=z/2\), and precisely its odd multiples are zero. Since \(z\mid p^2-1\), \(p\nmid 2\lambda\).

**2. Exact lifting.** In the unramified quadratic extension of \(\mathbb Z_p\), both roots are units and their difference is a unit. For each odd integer \(k\), the polynomial LTE identity applied to \(\alpha^{\lambda k}+\beta^{\lambda k}\) yields
\[
\nu_p(V_{\lambda k})=\nu_p(V_\lambda)+\nu_p(k)=e+\nu_p(k).
\]
There are no other indices divisible by \(p\). One can also prove this in a splitting unramified extension, since unit roots and the odd-power factorization preserve valuation. Consequently \(a_p(n)\) is the constant function one off indices \(\lambda k\) for odd \(k\), and on those indices has value \(p^{e+\nu_p(k)}\). Its Möbius transform is the displayed signed rank tower: the base contribution \(p^e-1\) at \(\lambda\), the negative copy at \(2\lambda\), and successive differences \(p^{e+j}-p^{e+j-1}\) at \(\lambda p^j\), with negative copies at \(2\lambda p^j\). When \(\lambda=1\), the constant baseline and rank base merge at \(n=1\), producing \(p^e\). The displayed support and values follow without convergence assumptions.

**3. Sharp odd-prime repair.** Since \(p\nmid 2\lambda\), the nonzero tower term at \(n=2\lambda p\) has value \(-p^e(p-1)\). Consequently a repair multiplier must be divisible by
\[
K_p=\frac{2\lambda}{\gcd(2\lambda,p-1)}.
\]
Conversely, this multiplier repairs *all* transform terms: \(2\lambda\mid K_p(p-1)\) and hence \(2\lambda\mid K_p(p^e-1)\), so the base terms are repaired; the factor \(p^{e+j-1}\) in the level-\(j\) terms contains \(p^j\), so no additional factor is required. The case \(\lambda=1\) is included, and the positivity of \(e\) is essential. This proof remains valid for every multiplicity \(e\), including even \(e\).

For split primes, \(z=2\lambda\mid p-1\), so \(K_p=1\). For inert primes, Frobenius exchanges the roots and \(\alpha^{p+1}=\alpha\beta=-1\), whence
\[
w^{(p+1)/2}=(-1)^{(p+3)/2}.
\]
If \(p\equiv1\pmod4\), the exponent \((p+1)/2\) is odd and the right side is \(+1\); hence \(z\) is odd and no trace zero exists. If \(p\equiv3\pmod4\), the right side is \(-1\), implying \(z\) even and \(\lambda\) even; moreover \(z\mid p+1\) and \(\gcd(z,p-1)=2\), so \(K_p=z/2=\lambda\). Ramified primes are covered by step 1. This proves the full odd-prime criterion.

**4. The prime two.** Modulo \(2\), odd \(P\) gives the trace pattern \(0,1,1,0,1,1,\ldots\), whereas even \(P\) gives zero traces at odd indices and nonzero traces at even indices. For even \(P\), the doubling identity \(V_{2m}=V_m^2-2(-1)^m\) shows \(\nu_2(V_{2m})=1\), and recurrence or odd-power lifting gives \(\nu_2(V_{2m+1})=\nu_2(P)=s\). Thus \(a_2\) is \(2^s\) at odd indices and \(2\) at even indices, giving only \(T_2(1)=2^s\) and \(T_2(2)=2-2^s\). For odd \(P\), \(V_3=P(P^2+3)\) has \(\nu_2(V_3)=2\) (since \(P^2\equiv1\pmod8\)); its odd multiples retain valuation \(2\), while its even multiples have valuation \(1\) by the duplication identity. Hence \(a_2\) has values \(4\) on indices \(n\equiv3\pmod6\), \(2\) on indices divisible by \(6\), and \(1\) elsewhere, giving the three indicated transforms. Congruence failure at \(n=3\) requires and is repaired by factor \(3\). Nonnegative-transform conditions now follow directly.

**5. Prime density.** The integer \(\Delta=P^2+4\) is not a square for \(P\ge3\): two squares differing by \(4\) with positive difference \(P\ge3\) cannot occur. Its quadratic character is nontrivial, and, since \(\Delta>0\), is distinct from the nontrivial imaginary quadratic character \((-4/\cdot)\). Their product is nonprincipal. The indicator of the inert-and-\(3\)-mod-\(4\) class at unramified odd primes equals \((1-\chi_\Delta(p))(1-\chi_{-4}(p))/4\). Orthogonality of nonprincipal Dirichlet characters in primes, equivalently the prime number theorem in arithmetic progressions, gives density \(1/4\). The complement has density \(3/4\).

## Verification
The standalone script `verify.py` enumerates \(P=3,\ldots,20\), all \(26\) primes up to \(101\), and indices \(1\le n\le260\). It independently obtains exact recurrence values and Möbius transforms, compares all transform entries against the formulas and the predicted odd-prime Dold criterion, including ramified primes and binary cases. Run from the extracted package with `python3 verify.py`. The proof above, not this bounded computation, establishes every-index and density assertions.

## Relationship to prior work
Chuysurichay, Jaidee, Panraksa and Ward (2026) establish local Dold congruences for the classical Fibonacci and Lucas sequences and explicitly pose extension to general Lucas pairs. The present theorem treats all integer parameters \(P\ge3\) in the *companion/second-kind* recurrence \(V_n(P,-1)\), including both parities of \(P\) and nonsquare discriminants. Established first-kind Lucas valuations and the 2016 lifting theory supply related ingredients, but the claimed contribution is the signed companion transform, the sharp repair and realizability criteria, and the uniform prime-density dichotomy. Earlier published work on square-discriminant split companion sequences does not include nonsquare discriminant here; results about equality of recurrence periods do not supply Dold integrality. The parameter \(P=2\) has been treated separately in previous work and is excluded rather than reclaimed.

## Limitations
The parameter is fixed and \(P\ge3\), with recurrence constant term \(-1\); extension to arbitrary Lucas \((P,Q)\) is not asserted. The exact transforms determine local nonnegative-realizability but do not imply a global sequence realizing the full original trace. The density is a natural density among primes, not an effective error bound. Although targeted research searches revealed no theorem with the same full generality, a sufficiently broad published theorem about trace valuations or Dold congruences could imply portions of this result; independent priority validation remains necessary.

## References
1. S. Chuysurichay, S. Jaidee, C. Panraksa and T. Ward, *The local Dold congruence for Fibonacci and Lucas sequences*, arXiv:2609.24544v1 (21 September 2026), https://arxiv.org/abs/2609.24544.
2. C. Sanna, *On the \(p\)-adic valuation of Lucas sequences*, Fibonacci Quarterly 54 (2016); DOI:10.1080/00150517.2016.12427821.
3. J. Byszewski, G. Graff and T. Ward, *Dold sequences, periodic points, and dynamics*, Bull. London Math. Soc. 53 (2021), 1263–1298; DOI:10.1112/blms.12531.
