# First off-center superspecial parameters in a classical \(D_6\) genus-three pencil

## Finding
For each odd prime \(5\leq p\leq31\), let \(k=\overline{\mathbf F}_p\). In the Fuertes–Streit family
\[
C_{p,t}:\quad y^2=x^7-tx^4+x,\qquad t\in k,\quad t^2\ne4,
\]
understood as the smooth projective model, the **complete superspecial parameter loci** are
\[
\begin{array}{c|c}
p&\{t\in k:\operatorname{Jac}(C_{p,t})\text{ is superspecial}\}\\\hline
5,13,17,29&\varnothing\\
7,11,19,23&\{0\}\\
31&\{0,12,-12\}\subset\mathbf F_{31}.
\end{array}
\]
Consequently \(31\) is the **first odd prime at least \(5\)** with a nonzero *marked parameter* on this fixed pencil whose smooth curve has a superspecial Jacobian. No assertion is made here about classifying geometric isomorphism classes across different parameters.

## Assumptions and scope
Everything is over the indicated algebraic closure of a prime field. The family has degree-seven squarefree right-hand side precisely when \(t^2\ne4\), for all primes considered; hence its smooth completion has genus three. The phrase *off-center* means \(t\ne0\) in the displayed coordinate, not a coordinate-free property of a moduli point. Characteristics \(2\) and \(3\) are not included in the threshold.

For \(p\ne2\), an abelian threefold is superspecial precisely when its \(a\)-number is three; for a Jacobian this occurs exactly when the Cartier operator on the three-dimensional space of regular differentials is zero. This is the test used below, not a test for mere supersingularity or \(p\)-rank zero.

## Proof
**1. Smoothness and genus.** Put \(P_t(u)=u^2-tu+1\) and \(f_t(x)=xP_t(x^3)\). The root at zero is simple. The remaining six roots are simple when the two roots of \(P_t\) are distinct, because \(p\ne3\) and neither root is zero. Their collision occurs exactly when \(t^2=4\). Therefore the odd-degree squarefree hyperelliptic model has genus \(3\) for the stated parameters.

**2. Cartier coefficients.** Set \(n=(p-1)/2\), and write \(f_t(x)^n=\sum_j c_j(t)x^j\). For the regular differential basis \(dx/y,x\,dx/y,x^2\,dx/y\), the Cartier matrix, up to entrywise inverse Frobenius, has entries \(c_{pi-j}(t)\) for \(1\le i,j\le3\). Indeed
\[
\frac{x^{j-1}\,dx}{y}=\frac{x^{j-1}f_t(x)^n\,dx}{y^p},
\]
and Cartier retains exactly the exponents \(pi-1\). Thus zeroing all the displayed coefficients is equivalent to the Cartier operator vanishing; the possible transpose/inverse-Frobenius convention does not affect zero entries.

Let \(m=(p-1)/6\) for \(p\equiv1\pmod6\), and \(m=(p-5)/6\) for \(p\equiv5\pmod6\). Define two polynomials in \(\mathbf F_p[t]\):
\[
A_p(t)=[u^m]P_t(u)^n,\qquad B_p(t)=[u^n]P_t(u)^n.
\]
Because \(f_t(x)^n=x^nP_t(x^3)^n\), and because \(P_t\) is reciprocal, the coefficient matrix has shape
\[
\begin{cases}
\operatorname{diag}(A_p,B_p,A_p),&p\equiv1\pmod6,\\[2pt]
\begin{pmatrix}0&0&A_p\\0&B_p&0\\A_p&0&0\end{pmatrix},&p\equiv5\pmod6.
\end{cases}
\]
In particular, the Jacobian is superspecial if and only if \(A_p(t)=B_p(t)=0\).

**3. Exact elimination and the first-prime cutoff.** All coefficient extractions are finite integer sums. More explicitly, for \(0\leq k\leq2n\),
\[
[u^k]P_t(u)^n=
\sum_{\substack{a,b,c\ge0\\a+b+c=n\\2a+b=k}}
\frac{n!}{a!b!c!}(-t)^b\pmod p.
\]
Computing the **monic** greatest common divisors in \(\mathbf F_p[t]\), one gets
\[
\begin{array}{c|ccccccccc}
p&5&7&11&13&17&19&23&29&31\\\hline
\gcd(A_p,B_p)&1&t&t&1&1&t&t&1&t(t^2-20).
\end{array}
\]
For clarity, the last polynomial is computed in \(\mathbf F_{31}[t]\). In particular,
\[
A_{31}(t)=4t(t^2-20)(t^2-12),
\]
\[
B_{31}(t)=11t+2t^3+16t^5+11t^7+30t^9+25t^{11}+7t^{13}+30t^{15}.
\]
The second polynomial is divisible by \(t(t^2-20)\); after division, its quotient reduces to the nonzero constant \(18\) modulo \(t^2-12\), so the displayed gcd has no extra factor. Since \(12^2\equiv20\pmod{31}\), the three common roots at the last prime are exactly \(0,12,-12\). At all three, \(t^2\ne4\). The earlier gcd entries similarly yield exactly the loci displayed in the finding. Because the listed primes exhaust all primes from \(5\) through \(31\), this proves the first-prime claim.

## Verification
The attached `verify.py` uses only exact integer binomial coefficients and modular polynomial division, with no external computer-algebra dependency. It recomputes \(A_p,B_p\), checks each gcd, and independently expands \(f_t(x)^n\) for *every* \(t\in\mathbf F_p\) at each of the nine primes to cross-check the matrix formula. The common-zero result over \(\overline{\mathbf F}_p\), including extension-field parameters, follows from the polynomial gcd rather than the finite-field sample. The script prints `VERIFY_OK` on success.

## Relationship to prior work
Kuribayashi–Komiya (1980), as cited by Fuertes–Streit, had already introduced this family. Fuertes–Streit (2006, §6, Eq. (6.1)) describe its hyperelliptic \(D_6\)-symmetry and moduli. The classical Cartier–Manin coefficient test for hyperelliptic curves (Yui, 1978) is used here, not claimed as new. Ohashi–Onuki–Kudo–Yoshizumi–Nuida (2025, §§4.1–4.2) give global counts and enumeration algorithms for superspecial genus-three hyperelliptic curves and identify the familiar \(t=0\) type in suitable characteristics. The claim here is the **explicit common-root classification on this particular marked pencil through the first exceptional nonzero prime**, not an algorithm to enumerate all genus-three curves, not a new Cartier formula, and not the previously known central example.

## Limitations
The cutoff is proved only for primes \(5\) through \(31\); no behavior for higher primes is asserted. The statement classifies marked parameters, not isomorphism classes. Historical computational tables or specialist dihedral-family literature could conceivably encode the same parameter list in another guise; these remain originality risks. The proof is an exact mathematical finite elimination, not a claim that unsuccessful search establishes uniqueness in the literature. Independent validation is not included.

## References
1. A. Kuribayashi and K. Komiya, *On the Structure of the Automorphism Group of a Compact Riemann Surface of Genus 3*, Bull. Fac. Sci. Eng. Chuo Univ. **23** (1980), 1–34 (cited in reference [10] of Fuertes–Streit).
2. Y. Fuertes and M. Streit, *Genus 3 normal coverings of the Riemann sphere branched over 4 points*, Rev. Mat. Iberoam. **22** (2006), 413–454, §6, DOI 10.4171/RMI/462, https://ems.press/content/serial-article-files/38161?nt=1.
3. N. Yui, *On the Jacobian varieties of hyperelliptic curves over fields of characteristic \(p>2\)*, J. Algebra **52** (1978), 378–410, DOI 10.1016/0021-8693(78)90247-8.
4. R. Ohashi, H. Onuki, M. Kudo, R. Yoshizumi and K. Nuida, *Listing superspecial curves of genus three using Richelot isogeny graphs*, Research in Number Theory **11** (2025), article 76, DOI 10.1007/s40993-025-00657-3.
