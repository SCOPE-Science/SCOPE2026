# A five-adic transfer law for cubic Lucas and Fibonacci window gcds

## Finding
Define Fibonacci numbers by \(F_0=0,F_1=1,F_{n+2}=F_{n+1}+F_n\), and Lucas numbers by \(L_0=2,L_1=1,L_{n+2}=L_{n+1}+L_n\). For every integer \(k\ge1\), write
\[
H_F(k)=\gcd_{n\ge0}\left(\sum_{j=0}^{k-1}F_{n+j}^{3}\right),\qquad
H_L(k)=\gcd_{n\ge0}\left(\sum_{j=0}^{k-1}L_{n+j}^{3}\right).
\]
Then the exact transfer law is
\[
\boxed{\ H_L(k)=\begin{cases}5H_F(k),&4\mid k,\\H_F(k),&4\nmid k.\end{cases}\ }
\]
The only prime at which the gcd changes is five, and it changes by exactly one power of five precisely for window lengths divisible by four. For example, the pairs \((H_F(k),H_L(k))\) at \(k=4,8,20\) are respectively \((1,5)\), \((9,45)\), and \((55,275)\).

## Assumptions and scope
All indices are nonnegative integers. The gcd of an infinite family is the positive generator of its additive ideal; the four consecutive initial windows suffice by an integral order-four recurrence with unit constant and leading coefficients. The claim holds for every \(k\ge1\), without an upper bound. It concerns cubes of the standard Fibonacci and Lucas sequences, not arbitrary initial conditions or other powers.

## Proof
**1. A transfer with determinant a power of five.** Put \(u_n=F_n^3\) and \(v_n=L_n^3\). Direct expansion of the second-order recurrence shows that both satisfy
\[
w_{n+4}-3w_{n+3}-6w_{n+2}+3w_{n+1}+w_n=0.\tag{1}
\]
The cubic-sequence identity
\[
L_n^3=-6F_n^3+24F_{n+1}^3+8F_{n+2}^3-3F_{n+3}^3\tag{2}
\]
holds for the four initial indices by direct substitution, and hence for all \(n\) by (1). Let \(E\) denote the shift, and let \(P(E)=-6+24E+8E^2-3E^3\). Equation (2) says \(v=P(E)u\). For each \(k\), taking \(k\)-term windows commutes with \(P(E)\). Relative to \(1,E,E^2,E^3\) in the ring \(\mathbb Z[E]/(E^4-3E^3-6E^2+3E+1)\), multiplication by \(P(E)\) has matrix
\[
M=\begin{pmatrix}-6&3&1&-3\\24&3&6&-8\\8&6&-3&24\\-3&-1&3&6\end{pmatrix},\qquad\det M=5^6.
\]
Because (1) is reversible over the integers, \(H_F(k)\) and \(H_L(k)\) are the gcds of their respective four initial window values. The corresponding transformation on the four-dimensional window vectors is \(P(C)\), with the same determinant \(5^6\) (the matrix \(M\) represents multiplication in the polynomial quotient). Since \(P(C)\) is invertible over \(\mathbb Z_p\) for every prime \(p\ne5\),
\[
\nu_p(H_F(k))=\nu_p(H_L(k))\qquad(p\ne5).\tag{3}
\]
Thus it remains to calculate the valuations at five.

**2. Detecting which window lengths are divisible by five.** Cubing is a permutation of \(\mathbb F_5\). If every \(k\)-term window sum of a sequence \(x_n^3\) vanishes modulo five, subtracting successive windows gives \(x_{n+k}^3=x_n^3\), hence \(x_{n+k}=x_n\pmod5\) for all \(n\). The Fibonacci sequence has least period \(20\) modulo five, while the Lucas sequence has least period \(4\). Conversely, direct summation over one respective period gives zero modulo five. It follows that
\[
5\mid H_F(k)\iff20\mid k,\qquad
5\mid H_L(k)\iff4\mid k.\tag{4}
\]
In particular, when \(4\nmid k\), both valuations are zero.

**3. The intermediate classes modulo twenty.** Lucas numbers have period \(20\) modulo \(25\), since \((L_{20},L_{21})\equiv(2,1)\pmod{25}\). Every Lucas-cube window of length \(20\) is divisible by \(25\). For lengths \(4,8,12,16\), the four initial window sums, reduced modulo \(25\), are respectively
\[
(0,10,15,20),\quad(20,10,10,0),\quad(10,0,10,15),\quad(20,5,15,15).
\]
Each quadruple is divisible by five but not by twenty-five. Reducing any window length \(k\equiv4,8,12,16\pmod{20}\) by full blocks of twenty, periodicity modulo twenty-five and divisibility of those full-block sums give \(\nu_5(H_L(k))=1\). By (4), \(\nu_5(H_F(k))=0\) in these classes.

**4. Exact lifting for lengths divisible by twenty.** Let \(C\) be the integral companion matrix for (1), acting on the four consecutive window values. Modulo five its characteristic polynomial is \((X-2)^4\). Since \(X^{20}-1=(X^4-1)^5\pmod5\) and \(X^4-1\) vanishes at \(X=2\), we have \(C^{20}\equiv I\pmod5\). Write \(C^{20}=I+5B\) for an integer matrix \(B\).

For either sequence, let \(V(20)\) be the column of its first four length-twenty sums. An exact evaluation gives the following residue certificates modulo \(125\):
\[
V_F(20)\equiv(30,30,65,120),\qquad V_L(20)\equiv(75,75,0,75)\pmod{125}.
\]
Thus the smallest entrywise five-adic valuation is exactly \(1\) for \(V_F(20)\) and exactly \(2\) for \(V_L(20)\).

For every \(t\ge1\), partitioning a window of length \(20t\) into \(t\) successive blocks yields
\[
V(20t)=\left(\sum_{j=0}^{t-1}C^{20j}\right)V(20)=tU_tV(20),
\]
where
\[
U_t=I+\sum_{r=1}^{t-1}\frac{5^r}{r+1}\binom{t-1}{r}B^r.
\]
Each nonconstant coefficient is a multiple of five in \(\mathbb Z_5\), since \(\nu_5(r+1)<r\) for every \(r\ge1\). Therefore \(U_t\equiv I\pmod5\) and is invertible over \(\mathbb Z_5\). Multiplication by it preserves the smallest five-adic valuation of vector entries. Consequently
\[
\nu_5(H_F(20t))=1+\nu_5(t),\qquad
\nu_5(H_L(20t))=2+\nu_5(t).\tag{5}
\]
Equations (3)–(5) settle every prime valuation, proving the claimed transfer law. \(\square\)

## Verification
The complete stand-alone script `verify.py` uses exact integer arithmetic and only Python's standard library. Execute `python3 verify.py` and compare against `verification_output.txt`. It verifies \(320\) lengths, \(2560\) directly evaluated window sums, \(640\) recurrence identities, \(320\) transfer identities, the determinant \(5^6\), and the finite modulo-\(25\)/\(125\) certificates. The proof above, not the finite range checked by software, establishes the result for every \(k\).

## Relationship to prior work
Mbirika and Spilker [1] prove gcd laws for sums of squares of Fibonacci and Lucas numbers and raise a corresponding question for cubes (Section 6, Question 6.1). Their even-square result has a factor of five for every even length, whereas the cubic transfer law has a sharper split at divisibility by four. The cubic expression printed in their question is conjectural, not a proof of this transfer theorem. Guyer and Mbirika [2] address first powers, not cube windows. No inspected primary result establishes equality of all non-five prime parts together with the exact five-adic phase in this theorem.

## Limitations
This theorem compares two standard cubic-window gcds; it does not itself determine higher-power analogues or all generalized Fibonacci initial conditions. The finite certificates only validate finite arithmetic instances, not an infinite search. Bibliographic uniqueness outside the inspected literature is not certified.

## References
[1] A. Mbirika and J. Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, arXiv:2204.12626 (first public version 26 April 2022), Sections 5–6, https://arxiv.org/abs/2204.12626.

[2] D. Guyer and A. Mbirika, *GCD of sums of k consecutive Fibonacci, Lucas, and generalized Fibonacci numbers*, arXiv:2104.12262 (2021), https://arxiv.org/abs/2104.12262.
