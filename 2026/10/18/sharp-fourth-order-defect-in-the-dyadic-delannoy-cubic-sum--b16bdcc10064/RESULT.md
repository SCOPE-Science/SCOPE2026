# Sharp fourth-order defect in the dyadic Delannoy cubic sum

## Finding
Let \(D_m=\sum_{j=0}^{m}2^j\binom mj^2\) be the central Delannoy numbers and set
\[
S_n=\sum_{m=0}^{n-1}(-1)^m(2m+1)^3D_m.
\]
For every integer \(r\ge1\), with \(n=2^r\), the **exact** valuation is
\[
\boxed{\nu_2(S_n-2n^2)=4r-1.}
\]
Equivalently, the sharp residue is \(S_n\equiv 2n^2+2^{4r-1}\pmod{2^{4r}}\). A structural companion identity, also established here, is
\[
\boxed{\nu_2(D_{2^r}+D_{2^r-1})=3r+1}\qquad(r\ge1).
\]
The first statement is the single main finding; the second is the critical supporting lemma.

## Assumptions and scope
All indices are ordinary integers, \(r\ge1\). For any nonzero integer \(a\), \(\nu_2(a)\) denotes its largest power-of-two divisor exponent. Congruences are in the ordinary integers. We use the two-adic integers \(\mathbb Z_2\) solely to establish uniform divisibility, not as a numerical approximation. No statement is made for non-dyadic cutoffs.

## Proof
**1. An exact finite-sum endpoint identity.** The well-known Delannoy recurrence, valid for \(m\ge1\), is
\[
(m+1)D_{m+1}=3(2m+1)D_m-mD_{m-1},\quad D_0=1,\ D_1=3.
\]
Direct substitution of this recurrence and cancellation of the coefficients of \(D_m,D_{m-1}\) shows that
\[
T_n=\frac{(-1)^nn}{4}\big[(4n+1-4n^2)D_n+(1-4n-4n^2)D_{n-1}\big]
\]
satisfies \(T_1=1\) and \(T_{n+1}-T_n=(-1)^n(2n+1)^3D_n\). Consequently \(T_n=S_n\) for every \(n\ge1\). Put \(X_n=D_n+D_{n-1}\) and \(Y_n=D_n-D_{n-1}\). For even \(n\), the exact endpoint identity becomes
\[
S_n=\frac n4(1-4n^2)X_n+n^2Y_n. \tag{1}
\]

**2. Two-adic interpolation and reflection.** Define, for \(x\in\mathbb Z_2\),
\[
d(x)=\sum_{j\ge0}2^j\binom{x}{j}^{\!2}.
\]
The series converges uniformly because each generalized binomial coefficient is a two-adic integer. On nonnegative integers it equals \(D_x\). Continuity and density of nonnegative integers extend the Delannoy recurrence to all \(x\in\mathbb Z_2\):
\[
(x+1)d(x+1)=3(2x+1)d(x)-xd(x-1).
\]
Since \(d(-1)=\sum_{j\ge0}2^j=-1\) in \(\mathbb Z_2\), the recurrence inductively yields \(d(-n)=-D_{n-1}\) for all integers \(n\ge1\). Using \(\binom{x}{j}=x\binom{x-1}{j-1}/j\), we obtain
\[
d(x)=1+x^2\sum_{j\ge1}\frac{2^j}{j^2}\binom{x-1}{j-1}^{\!2}. \tag{2}
\]
All coefficients \(2^j/j^2\) belong to \(\mathbb Z_2\), since \(j-2\nu_2(j)\ge0\) for every \(j\ge1\); they tend two-adically to zero. In particular, for any positive integer \(n\),
\[
Y_n=d(n)+d(-n)\equiv2\pmod{n^2}\quad\text{when }n=2^r. \tag{3}
\]

**3. Exact adjacent-value valuation.** Fix \(n=2^r\) with \(r\ge2\). Set
\[
a_j=\frac{2^j}{j^2},\qquad A_j=\binom{n-1}{j-1},\qquad B_j=\binom{-n-1}{j-1}.
\]
Equations (2) and the reflection give
\[
X_n=d(n)-d(-n)=n^2\sum_{j\ge1}a_j(A_j^2-B_j^2). \tag{4}
\]
We prove the sum on the right is congruent to \(2n\) modulo \(4n\). For \(2\le j\le n\), both \(A_j\) and \(B_j=(-1)^{j-1}\binom{n+j-1}{j-1}\) are odd, by binary Lucas arithmetic: \(n-1\) has all lower \(r\) bits equal to one, and the lower \(r\) bits of \(n+j-1\) are exactly those of \(j-1\). Vandermonde's identity gives
\[
A_j-B_j=\sum_{t=1}^{j-1}\binom{2n}{t}\binom{-n-1}{j-1-t}.
\]
For \(1\le t<2n\), \(\nu_2\binom{2n}{t}=r+1-\nu_2(t)\). Hence
\[
\nu_2(A_j^2-B_j^2)\ge r+2-\lfloor\log_2(j-1)\rfloor,
\]
where the extra unit comes from the even factor \(A_j+B_j\). Apart from \(j=4\), the elementary inequality
\[
j-2\nu_2(j)-\lfloor\log_2(j-1)\rfloor\ge0
\]
holds for every \(j\ge2\). (At powers of two check \(2^s-3s+1\), and between consecutive powers use \(\nu_2(j)\le s-1\); the unique exception is \(j=4\).) Thus all \(2\le j\le n\) except \(j=4\) contribute multiples of \(4n\) to (4). The \(j=1\) contribution is zero.

For \(j>n\), \(A_j=0\). If \(r\ge3\), elementary splitting according to \(\nu_2(j)\) shows \(j-2\nu_2(j)\ge r+2\), so these terms also vanish modulo \(4n\). When \(r=2\), the same bound holds for all \(j>4\) except \(j=8\). At that exception, \(a_8=4\) and \(B_8=\binom{11}{7}=330\), so \(a_8B_8^2\) is divisible by \(16=4n\). This exhausts the infinite tail.

Finally, \(a_4=1\) and direct polynomial factorization yields
\[
A_4^2-B_4^2=-\frac{2n(n^2+1)(n^2+11)}{3}\equiv2n\pmod{4n},
\]
since \(4\mid n\). Therefore (4) gives
\[
X_n\equiv2n^3\pmod{4n^3},\qquad \nu_2(X_n)=3r+1. \tag{5}
\]
For \(r=1\), \(D_2+D_1=13+3=16\), so (5)'s valuation formula also holds.

**4. The sharp defect.** For even dyadic \(n\), subtract \(2n^2\) from (1):
\[
S_n-2n^2=\frac n4(1-4n^2)X_n+n^2(Y_n-2). \tag{6}
\]
By (5), the first term has valuation exactly \(r-2+(3r+1)=4r-1\). By (3), the second term is divisible by \(n^4=2^{4r}\). Distinct valuations cannot cancel; hence \(\nu_2(S_n-2n^2)=4r-1\) for all \(r\ge2\). For \(r=1\), \(S_2=1-27D_1=-80\) and \(S_2-2(2^2)=-88\), of valuation three. This completes the proof.

## Verification
The attached standard-library Python checker `verify.py` independently reconstructs Delannoy numbers using both the recurrence and their binomial formula; tests the exact endpoint identity and claimed valuations for dyadic indices up to \(2^{11}\); checks finite approximations to two-adic reflection modulo powers of two; and evaluates the exceptional \(j=4\) factorization and the local binomial bounds. These finite computations are supplementary; the proof above covers every integer \(r\ge1\).

## Relationship to prior work
Guo and Zeng (arXiv:1008.2894, first submitted 2010-08-17) formulated the underlying congruence \(S_n\equiv2n^2\pmod{n^3}\) for dyadic \(n\). Wang and Zhong (arXiv:2505.05728, first submitted 2025-05-09), Theorem 1.3 and equation (3.10), explicitly proved this congruence and a wider family modulo \(n^3\). The present result **does not claim to solve that already-solved conjecture**: it determines the *exact valuation of the error* and establishes an unbounded additional precision, up to the sharp modulus \(2^{4r}\). The adjacent-value valuation (5) is the decisive independent structural input. Neither cited paper's inspected theorem or proof states this sharp fourth-order result.

## Limitations
The exact law is restricted to dyadic cutoffs and cubic weights. No claim is made about arbitrary cutoff integers or higher odd powers. Previously unlocated literature could contain a stronger implication; an independent priority review has not occurred. Verification code checks finite examples but does not constitute an infinite certificate.

## References
Guo, V. J. W., and Zeng, J., *New congruences for sums involving Apéry numbers or central Delannoy numbers*, arXiv:1008.2894 (first public 2010-08-17), especially Conjecture 3.3.

Wang, R.-H., and Zhong, M. X. X., *Congruences for sums of Delannoy numbers and polynomials*, arXiv:2505.05728 (2025-05-09), especially Theorem 1.3, Theorem 3.1, equations (1.14) and (3.10).
