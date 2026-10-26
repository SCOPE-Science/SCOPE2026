# Squarefree sparsity in equal-degree polynomial product collisions

## Finding

Fix a prime power \(q\). For each integer \(n\ge 1\), let \(E_q(n)\) count ordered quadruples of monic degree-\(n\) polynomials \((f_1,f_2,f_3,f_4)\) over \(\mathbb F_q[T]\) satisfying \(f_1f_2=f_3f_4\). Let \(S_q(n)\) count those quadruples for which **every** \(f_i\) is squarefree. For a monic irreducible \(P\), put \(|P|=q^{\deg P}\), and define
\[
C_q=\prod_{P\text{ monic irreducible}} (1-|P|^{-1})^4(1+4|P|^{-1}+|P|^{-2}).
\]
The product converges to a strictly positive constant and, as \(n\to\infty\) with \(q\) fixed,
\[
\boxed{S_q(n)=C_q(n+1)q^{2n}+O_q(q^{2n}).}
\]
The unrestricted energy is exactly
\[
E_q(n)=\bigl(n+1-n/q\bigr)q^{2n}.
\]
Consequently the limiting squarefree proportion among multiplicative collisions is
\[
\boxed{\rho_q:=\lim_{n\to\infty}\frac{S_q(n)}{E_q(n)}=\frac{C_q}{1-q^{-1}}.}
\]
For four independently sampled monic degree-\(n\) polynomials (\(n\ge2\)), the squarefree proportion is \((1-q^{-1})^4\). By contrast, for every prime power \(q\),
\[
\boxed{0<\rho_q<(1-q^{-1})^4.}
\]
Moreover, as prime powers \(q\to\infty\),
\[
\rho_q=1-\frac8q+O(q^{-2}),
\qquad (1-q^{-1})^4=1-\frac4q+O(q^{-2}).
\]
This quantifies the squarefree deficit imposed by the product-collision relation.

## Assumptions and scope

All polynomials are nonzero, monic, and belong to \(\mathbb F_q[T]\). The quadruple is ordered; each of its four members has **exact** degree \(n\). A polynomial is squarefree if no nonconstant irreducible divides it twice. The empty product is the monic unit polynomial. The parameter \(q\) is a fixed prime power for the degree-asymptotic estimate; the second expansion considers prime powers tending to infinity. No independence is assumed.

## Proof

**Canonical factorization.** Put \(A=\gcd(f_1,f_3)\), with monic gcd. Coprimality after division and the equality of products yield unique monic polynomials \(B,C,D\) with
\[
(f_1,f_2,f_3,f_4)=(AB,CD,AC,BD),\qquad \gcd(B,C)=1.
\]
Indeed, writing \(f_1=AB\), \(f_3=AC\) implies \(Bf_2=Cf_4\), and the coprimality of \(B,C\) gives \(f_2=CD\), \(f_4=BD\) uniquely. Exact equal degrees imply \(\deg A=\deg D=a\) and \(\deg B=\deg C=b=n-a\), with \(0\le a\le n\). Conversely all these data give one product collision.

All four products are squarefree exactly when every one of \(A,B,C,D\) is squarefree and all their pairs are coprime except that \(A\) and \(D\) are permitted to share irreducible factors. At any irreducible \(P\), the possible memberships among the four factors are: no membership, precisely one of \(A,B,C,D\), or simultaneous membership in \(A,D\). Thus the full four-variable generating series is
\[
F(u_A,u_B,u_C,u_D)=\prod_{P}\bigl(1+u_A^{\deg P}+u_B^{\deg P}+u_C^{\deg P}+u_D^{\deg P}+(u_Au_D)^{\deg P}\bigr).
\]
Writing \(T_q(a,b)=[u_A^a u_B^b u_C^b u_D^a]F\) yields the **exact**, not asymptotic, identity
\[
S_q(n)=\sum_{a=0}^{n}T_q(a,n-a).
\]

**Four-pole extraction.** Since the generating series of all monic polynomials is \(\prod_P(1-u^{\deg P})^{-1}=(1-qu)^{-1}\), write
\[
F(u_A,u_B,u_C,u_D)=\frac{H(u_A,u_B,u_C,u_D)}{(1-qu_A)(1-qu_B)(1-qu_C)(1-qu_D)},
\]
where
\[
H=\prod_P\Bigl[(1+u_A^{\deg P}+u_B^{\deg P}+u_C^{\deg P}+u_D^{\deg P}+(u_Au_D)^{\deg P})\prod_{j\in\{A,B,C,D\}}(1-u_j^{\deg P})\Bigr].
\]
Let \(R=q^{-3/4}\). The bracket at any irreducible of degree \(d\) is \(1+O(R^{2d})\), uniformly on the closed polydisc \(|u_j|\le R\); the linear terms cancel. The number of degree-\(d\) monic irreducibles is at most \(q^d/d\). Thus \(\sum_{d\ge1}(q^d/d)R^{2d}<\infty\), so \(H\) converges absolutely and uniformly on the closed polydisc. In particular \(H\) is holomorphic on a slightly larger open polydisc than \(|u_j|\le q^{-1}\), and its Taylor coefficients satisfy \(|h_{i_A,i_B,i_C,i_D}|\le M_q R^{-(i_A+i_B+i_C+i_D)}\) by the multivariate Cauchy estimate.

Expanding the four geometric series gives
\[
q^{-2(a+b)}T_q(a,b)=\sum_{\substack{0\le i_A,i_D\le a\\0\le i_B,i_C\le b}}h_{i_A,i_B,i_C,i_D}q^{-(i_A+i_B+i_C+i_D)}.
\]
Because \(qR=q^{1/4}>1\), comparison with the unrestricted absolutely convergent Taylor series at \(u_j=1/q\) shows
\[
q^{-2(a+b)}T_q(a,b)=H(q^{-1},q^{-1},q^{-1},q^{-1})+O_q(q^{-\min(a,b)/4}).
\]
The value on the right is \(C_q\), with the Euler factors shown in the finding. Summing over \(a+b=n\) and using \(\sum_{a=0}^{n}q^{-\min(a,n-a)/4}=O_q(1)\) proves the degree asymptotic. Each local Euler factor is positive and differs from \(1\) by \(O(|P|^{-2})\), proving \(C_q>0\).

**Unrestricted denominator.** For each \(a+b=n\), the choices for \(A,D\) number \(q^{2a}\). The number of ordered coprime monic \((B,C)\) of common degree \(b\) is \(1\) for \(b=0\), and \(q^{2b}-q^{2b-1}\) for \(b\ge1\): this follows by Möbius inversion and \(\sum_{\deg Q=j}\mu(Q)=0\) for \(j\ge2\), with first-degree sum \(-q\). Summing gives \(E_q(n)=q^{2n}[1+n(1-q^{-1})]\).

**Strict comparison with independence.** Put \(u=|P|^{-1}\), so \(0<u\le1/2\). Direct factorization gives
\[
(1-u^2)^5-(1-u)^4(1+4u+u^2)
=(1-u)^4u^2(u+2)(2-u-2u^2-u^3)>0,
\]
since \(u+2u^2+u^3\le9/8<2\) on this interval. The polynomial zeta identity \(\prod_P(1-|P|^{-2})=1-q^{-1}\) yields \(C_q<(1-q^{-1})^5\) by multiplying the strict local inequalities, and therefore \(\rho_q<(1-q^{-1})^4\). (The inequality is strict since every factor ratio is less than one and the products converge to positive limits.) Finally local expansion gives \((1-u)^4(1+4u+u^2)=1-9u^2+O(u^3)\). There are exactly \(q\) degree-one monic irreducibles, while the total contribution of irreducibles of degree at least two is \(O(q^{-2})\) to \(\log C_q\). Hence \(\log C_q=-9/q+O(q^{-2})\), which proves the large-field expansion after division by \(1-q^{-1}\).

## Verification

The accompanying standalone standard-library program `verify.py` computes squarefree monic polynomial product collisions by direct multiplicity counting, and separately by canonical coprime-factor counting for smaller cases. It checks \(q=2\) through \(n=6\), \(q=3\) through \(n=4\), and \(q=5\) through \(n=3\). Representative squarefree counts are \(S_2(4)=128\), \(S_3(4)=7170\), and \(S_5(3)=26020\). The numerical truncated Euler products check the strict comparison with the independent squarefree proportion. The program prints `VERIFY_OK` on success. These finite checks are corroboration; the proof above handles all prime powers and all positive degrees.

## Relationship to prior work

Afifurrahman, *Statistics of divisor functions over function fields* (arXiv:2610.11240v1, October 8, 2026), studies the unrestricted product-collision equation, and Theorem 2.2 covers its unrestricted fixed-degree enumeration. The gcd factorization and coprime monic polynomial counts used here are familiar from that framework. The inspected theorem statements and proofs do not impose squarefreeness on all four factors, compute the Euler-product density \(\rho_q\), or compare it with independent squarefreeness. The new object is the squarefree-conditioned collision count and its strict arithmetic bias. Generic squarefree-value and sieve methods may supply a different route to the leading product, so independent bibliographic review remains appropriate.

## Limitations

The error constant in \(O_q(q^{2n})\) depends on \(q\); no uniform error in simultaneous \(q,n\to\infty\) is claimed. The exact value of \(S_q(n)\) for arbitrary \(n\) is given by the multivariate coefficient formula, not a closed polynomial in \(n\). The result addresses squarefree monic inputs and exact equal degrees; it does not cover nonsquarefree patterns or shifted products. No independent audit or priority certification has been performed.

## References

- M. Afifurrahman, *Statistics of divisor functions over function fields*, arXiv:2610.11240v1 (first posted October 8, 2026), especially Theorem 2.2, Proposition 3.1, Proposition 3.2, and Section 5; https://arxiv.org/abs/2610.11240.
- B. Poonen, *Squarefree values of multivariable polynomials*, Duke Mathematical Journal **118** (2003), 353–373. General squarefree-sieve background; no claim that its hypotheses directly give the present degree-asymptotic or coefficient error.
