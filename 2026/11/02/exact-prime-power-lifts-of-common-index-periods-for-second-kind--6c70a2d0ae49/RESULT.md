# Exact prime-power lifts of common index periods for second-kind Dickson functions

## Finding

For an odd prime \(p\), positive integer \(k\), and unit \(a\pmod p\), let \(E_n(X,a)\) be the second-kind Dickson polynomial given by
\[
E_0(X,a)=1,\qquad E_1(X,a)=X,\qquad
E_{n+2}(X,a)=X E_{n+1}(X,a)-aE_n(X,a).
\]
The *common index period* \(T_{p,k}(a)\) is the least positive \(T\) such that
\[
E_{n+T}(x,a)\equiv E_n(x,a)\pmod{p^k}
\quad\text{for every }n\ge0\text{ and every }x\in\mathbb Z/p^k\mathbb Z.
\]
Then
\[
\boxed{T_{p,k}(a)=
\begin{cases}
p^{k-1}(p^2-1),&\displaystyle\left(\frac{a}{p}\right)=-1,\\[3pt]
\dfrac{p^k(p^2-1)}2,&\displaystyle\left(\frac{a}{p}\right)=1.
\end{cases}}
\]
Every stated period is least, including at the first prime-power level and all higher levels. For odd \(M=\prod_{i=1}^s p_i^{k_i}\) coprime to \(a\), the common index period modulo \(M\) is \(\operatorname{lcm}_{i}T_{p_i,k_i}(a)\), by the Chinese remainder theorem.

## Assumptions and scope

All polynomial coefficients are integral. The parameter \(a\) is a unit modulo the odd prime \(p\). The symbol \(\left(\frac{a}{p}\right)\) is the Legendre symbol. This is equality of **polynomial functions evaluated at every residue**, not equality of polynomial coefficients, an individual recurrence orbit, or the period of a permutation property. For \(p\nmid a\), every fixed-\(x\) companion matrix is invertible; hence the index sequences are purely periodic from index zero. The genuinely new part of the classification is the sharp prime-power lift \(k\ge2\), beyond the finite-field problem.

## Proof

**1. A companion-matrix equivalence.** Work over \(R=\mathbb Z/p^k\mathbb Z\) and put
\[
C_x=\begin{pmatrix}x&-a\\1&0\end{pmatrix},\qquad \det C_x=a\in R^\times.
\]
For \(v_x=(x,1)^{\mathsf T}\), the first and second coordinates of \(C_x^n v_x\) are \(E_{n+1}(x,a)\) and \(E_n(x,a)\). The two columns \(v_x,C_xv_x\) form a basis of \(R^2\), since their determinant is \(a\). Therefore \(E_{n+T}(x,a)=E_n(x,a)\) for all \(n\ge0\) if and only if \(C_x^T=I\): the forward implication says that \(C_x^T\) fixes \(v_x\), and commutation makes it fix \(C_xv_x\); the reverse implication is immediate. Thus \(T_{p,k}(a)\) is the least common multiple of the orders of all \(C_x\) over \(x\in R\).

**2. Exact prime-field exponent.** Over \(\mathbb F_p\), the eigenvalues \(u,v\) satisfy \(uv=a\) and \(u+v=x\). The collection of all possible eigenvalues as \(x\) varies is exactly
\[
\mathbb F_p^\times\ \cup\
\{u\in\mathbb F_{p^2}^\times:u^{p+1}=a\}.
\]
Indeed, a root in \(\mathbb F_p^\times\) has its other root \(a/u\) in that field. A root outside \(\mathbb F_p\) has Frobenius conjugate \(u^p=a/u\), and conversely this equality makes the trace \(u+a/u\) lie in \(\mathbb F_p\).

Let \(d=\operatorname{ord}_{\mathbb F_p^\times}(a)\). A primitive generator \(g\) of \(\mathbb F_{p^2}^\times\) writes \(a=g^{(p+1)e}\); the norm-\(a\) fiber has exponents \(e+(p-1)t\). Its generated subgroup has order \((p+1)d\). Hence the least common multiple of all eigenvalue orders is
\[
h=\operatorname{lcm}(p-1,(p+1)d)
=\frac{p^2-1}{\gcd(p+1,(p-1)/d)}.
\]
Because \(\gcd(p+1,p-1)=2\), this denominator is one exactly when \(a\) is a nonsquare, and two exactly when \(a\) is a square. In the nonsquare case all characteristic polynomials have distinct roots (their discriminants cannot vanish); therefore \(C_x^h=I\) at every field point, and \(h=p^2-1\) is least.

In the square case there are points \(x=\pm2\rho\) with \(\rho^2=a\) over \(\mathbb F_p\). There the matrix has a nontrivial repeated-root Jordan block, whose order introduces exactly one factor of \(p\). The least common field period is consequently \(p h=p(p^2-1)/2\). In both cases the prime-to-\(p\) part \(h\) is forced by eigenvalues that really occur among these matrices.

**3. Universal lifting upper bounds.** If a matrix \(B\) over \(\mathbb Z/p^k\mathbb Z\) is the identity modulo \(p\), then \(B^{p^{k-1}}\equiv I\pmod{p^k}\), by repeated binomial expansion (\(p\) odd). Applying this to the common field period of each \(C_x\) gives
\[
T_{p,k}(a)\mid
\begin{cases}
p^{k-1}(p^2-1),&a\text{ nonsquare},\\
p^k(p^2-1)/2,&a\text{ square}.
\end{cases}
\]

**4. Sharpness in the square case.** The square root \(\rho\) of \(a\) lifts to a unit modulo every \(p^k\) by Hensel's lemma, because \(p\) is odd. At \(x=2\rho\), the companion matrix is \(C_x=\rho I+N\) with \(N^2=0\) and \(N_{21}=1\). Therefore
\[
(C_x^T)_{21}=T\rho^{T-1}.
\]
Every common period is divisible by \(p^k\). It is also divisible by the prime-to-\(p\) eigenvalue exponent \(h=(p^2-1)/2\) from Step 2. Since \(p\nmid h\), their product \(p^k h\) divides every period and equals the upper bound.

**5. Sharpness in the nonsquare case.** Here \(h=p^2-1\), so \(p\nmid h\). For each \(x_0\in\mathbb F_p\), let \(\Delta=x_0^2-4a\ne0\). In a splitting field the roots \(u,v\) of \(z^2-xz+a\) are distinct, and the standard Binet identity gives
\[
E_{h-1}(x,a)=\frac{u^h-v^h}{u-v}.
\]
At \(x=x_0\), both \(u^h\) and \(v^h\) equal one. Implicit differentiation, using \(u'=u/(u-v)\) and \(v'=v/(v-u)\), yields the exact nonzero derivative in \(\mathbb F_p\):
\[
E_{h-1}'(x_0,a)=\frac{2h}{x_0^2-4a}\ne0.
\]
Choose any integer lift \(y\) of \(x_0\). Taylor expansion modulo \(p^2\) gives
\[
E_{h-1}(y+p,a)-E_{h-1}(y,a)
\equiv p E_{h-1}'(x_0,a)\not\equiv0\pmod{p^2}.
\]
Consequently at least one of these two lifts has \(E_{h-1}(x,a)\not\equiv0\pmod{p^2}\), hence \(C_x^h\not\equiv I\pmod{p^2}\) (the lower-left entry of \(C_x^h\) is \(E_{h-1}(x,a)\)). For such a lift, \(C_x^h=I+pD\) with \(D\not\equiv0\pmod p\). For odd \(p\), successive raising to the \(p\)-th power shows that its exact order modulo \(p^k\) is \(p^{k-1}\): the first nonzero layer of \((I+pD)^{p^j}-I\) is \(p^{j+1}D\), modulo \(p^{j+2}\). The prime-field eigenvalue calculation separately forces \(h\), coprime to \(p\). Thus the common period is divisible by \(p^{k-1}h\), matching the upper bound. For \(k=1\), Step 2 already establishes sharpness. This completes both cases.

## Verification

The accompanying `verify.py` uses integer modular matrix multiplication and fast exponentiation. It checks all units \(a\) and all residues \(x\) in the tested rings \(\mathbb Z/p^k\mathbb Z\), verifies the displayed period, and excludes every proper prime-divisor quotient of that period by an explicit witness. It also directly checks the scalar polynomial recurrence on several fields and the nonzero derivative certificate at every field residue for the tested primes. All computations are finite corroboration, not an argument for the unrestricted theorem. Run `python3 verify.py` with Python 3 standard library.

## Relationship to prior work

Qu and Ding (2014) establish the recurrence and investigate *permutation indices* of \(E_n(X,a)\) over prime-power integer residue rings; permutation criteria are not the least periods of the entire function-valued index sequence. Gültekin and Taşyurdu (2013) prove periodicity of Fibonacci polynomials in a distinct coefficient-and-exponent reduction and give a companion-matrix perspective; they do not state the present precise least pointwise period. Wang (2025), Lemma 6, explicitly studies common index periods of second-kind Dickson polynomial *functions over finite fields*. Therefore the prime-field periodicity problem, and the use of eigenvalues to solve it, are **prior art**, not claimed as new. The distinction established here is the exact all-parameter integer prime-power lift \(k\ge2\), including uniform sharpness. Henderson (1997) provides earlier finite-field second-kind Dickson theory. The possibility of an equivalent prime-power statement elsewhere in the literature remains a priority risk.

## Limitations

The modulus is an odd prime power, the parameter must be a unit, and periods are pointwise functional index periods (not coefficientwise periods). The characteristic-two, nonunit-parameter and arbitrary coefficientwise-period problems are not covered. Independent mathematical validation has not been performed. Literature search and accessible-source inspection cannot guarantee historical uniqueness; in particular, a general earlier matrix-period theorem might imply this result without naming Dickson polynomials.

## References

- L. Qu and C. Ding, *Dickson Polynomials of the Second Kind That Permute \(\mathbb Z_m\)*, SIAM Journal on Discrete Mathematics 28 (2014), 722–735, DOI `10.1137/130942589`, electronically published 2014-05-01.
- İ. Gültekin and Y. Taşyurdu, *On Period of the Sequence of Fibonacci Polynomials Modulo \(m\)*, Discrete Dynamics in Nature and Society (2013), article 731482, DOI `10.1155/2013/731482`.
- Z. Wang, *First and Second Moment Analysis of Dickson Polynomials of the Second Kind*, Journal of Mathematics (2025), 5569145, DOI `10.1155/jom/5569145`, particularly Lemma 6.
- M. Henderson, *A note on permutation behaviour of Dickson polynomials of the second kind*, Bulletin of the Australian Mathematical Society (1997), DOI `10.1017/S0004972700031300`.
