# Nine prime-index cases of a cyclotomic Stern-polynomial divisibility conjecture

## Finding

For every \(p\in\{3,5,11,13,19,29,37,53,59\}\) and every positive integer \(n\), if the cyclotomic polynomial \(\Phi_p(X)\) or \(\Phi_p(-X)\) divides the Stern \((0,1)\)-polynomial \(A_n(X)\) over \(\mathbb Z[X]\), then \(2^{p-1}+1\mid n\). More precisely, in \(\mathbb F_2[X]\), \(\Phi_p(X)\mid \overline{A_n}(X)\) if and only if \(2^{p-1}+1\mid n\). Here \(A_0=0\), \(A_1=1\), \(A_{2j}(X)=A_j(X^2)\), and \(A_{2j+1}(X)=X A_j(X^2)+A_{j+1}(X^2)\).

The nine primes are exactly those \(p\le59\) for which \(2\) is a primitive root modulo \(p\). This settles, at these nine prime indices and for all positive Stern indices, the *necessity* direction of Conjecture 2 in Dilcher–Ericksen (2014). In particular, at \(p=59\), the required index divisor is \(288230376151711745\).

## Assumptions and scope

The polynomials \(A_n\in\mathbb Z[X]\) are the *Stern \((0,1)\)-polynomials* of Dilcher–Stolarsky, not the different family \(B_n\) of Klavžar–Milutinović–Petr. Define \(A_0=0\), \(A_1=1\), and for integers \(j\ge1\),
\[
A_{2j}(X)=A_j(X^2),\qquad A_{2j+1}(X)=X A_j(X^2)+A_{j+1}(X^2).
\]
Divisibility means exact divisibility over \(\mathbb Z[X]\); \(\Phi_p\) is the \(p\)-th cyclotomic polynomial. The claim is only for \(p\in\{3,5,11,13,19,29,37,53,59\}\) and every positive integer \(n\).

## Proof

Fix an indicated prime \(p\). The multiplicative order of \(2\) modulo \(p\) is \(p-1\), so \(\Phi_p(X)\) remains irreducible in \(\mathbb F_2[X]\). Put \(q=2^{p-1}\) and let \(\xi\) be any root. Its conjugates under squaring are all primitive \(p\)-th roots, whence
\[
\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}(\xi)=\sum_{j=1}^{p-1}\xi^j=1.
\]
Consequently \(T^2+T+\xi\) is irreducible over \(\mathbb F_q\). Its roots \(\alpha,\beta\) in \(\mathbb F_{q^2}\) satisfy \(\alpha+\beta=1\), \(\alpha\beta=\xi\ne0\) and \(\beta=\alpha^q\). Thus \(\rho=\alpha/\beta\) satisfies \(\rho^{q+1}=1\).

The sequence \(s_n=\alpha^n+\beta^n\) has \(s_0=0\), \(s_1=1\), and, by Frobenius squaring,
\[
s_{2j}=s_j^2,\qquad s_{2j+1}=\xi s_j^2+s_{j+1}^2.
\]
The last identity follows from \(\xi(\alpha^{2j}+\beta^{2j})+(\alpha^{2j+2}+\beta^{2j+2})=\alpha^{2j+1}+\beta^{2j+1}\), using \(\alpha+\beta=1\). These are precisely the defining Stern recurrences modulo two, so \(s_n=\overline{A_n}(\xi)\). Since \(\beta\ne0\),
\[
\overline{A_n}(\xi)=0\quad\Longleftrightarrow\quad \rho^n=1.
\]
It remains to show that \(\rho\) has the full order \(Q=q+1\), rather than a proper divisor.

The accompanying standalone verifier represents \(\mathbb F_q\) exactly as \(\mathbb F_2[X]/(\Phi_p(X))\). For each of the nine primes, it (i) verifies \(p\) and the primitive-root condition; (ii) gives and verifies a complete factorization of \(Q\) into primes by integer trial division; (iii) checks \(\overline{A_Q}(\xi)=0\); and (iv) checks \(\overline{A_{Q/r}}(\xi)\ne0\) for every distinct prime factor \(r\mid Q\). These finitely many nonzero certificates imply \(\operatorname{ord}(\rho)=Q\), because its order divides \(Q\). The verifier prints the nonzero residues in hexadecimal, so all required computations can be independently reproduced by integer/polynomial arithmetic.

The irreducibility of \(\Phi_p(X)\) modulo two now gives \(\Phi_p(X)\mid\overline{A_n}(X)\) if and only if \(Q\mid n\). Finally, \(\Phi_p(X)\) and \(\Phi_p(-X)\) have identical reduction modulo two, so either integer divisibility hypothesis forces \(Q\mid n\). This proves the theorem for every positive integer \(n\), not merely indices up to a computational limit.

## Verification

Run `python3 verify_stern.py` with Python 3 and no dependencies. It verifies 22 nonzero prime-factor test residues for the nine parameters, their complete integer factorizations, the nine primitive-root conditions, and nine zero tests. The expected terminal line is `VERIFY_OK primes= 9 nonzero_certificates= 22`. Finite arithmetic here is an exact *certificate for the nine fixed values of* \(p\); the preceding argument supplies the quantifier over all \(n\). The code uses exact GF(2) polynomial arithmetic, not floating-point approximations.

## Relationship to prior work

Dilcher–Ericksen (2014), Section 6, especially Proposition 8 and Proposition 15, prove sufficiency families of cyclotomic factors for multiples of \(2^{p-1}+1\). Their Section 8.2 explicitly poses the converse necessity as Conjecture 2, including both signs \(\Phi_p(\pm X)\). The present result proves that necessity at the first nine permitted primes using finite-field multiplicative-order certificates; it does **not** settle the conjecture for every permitted prime. Dilcher–Tomkins (2018) concerns the different Stern polynomial family \(B_n\) and is not a proof of this claim.

## Limitations

Only nine prime parameters are established; no assertion is made for larger admissible primes. Integer divisibility of \(A_n\) by \(\Phi_p(X)\) for *every* multiple of \(2^{p-1}+1\) is not claimed. The result is a proven finite-parameter slice of an infinite-parameter conjecture, not a complete resolution. Independent external validation has not been performed.

## References

1. K. Dilcher and L. Ericksen, *Reducibility and irreducibility of Stern (0,1)-polynomials*, Communications in Mathematics 22 (2014), 77–102, Section 6 and Conjecture 2 in Section 8.2. https://dml.cz/bitstream/handle/10338.dmlcz/143908/ActaOstrav_22-2014-1_7.pdf
2. K. Dilcher and H. Tomkins, *Square classes and divisibility properties of Stern polynomials*, Integers 18 (2018), #A29; the distinct \(B_n\) convention. https://math.colgate.edu/~integers/s29/s29.pdf
