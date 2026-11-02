# Complete prime-cube root-count law for random monic polynomials

## Finding

Let \(p\) be any prime, and let \(d\geq 3p\) be an integer. Choose a monic polynomial \(F(X)=X^d+\sum_{j=0}^{d-1}a_jX^j\) uniformly, with independent \(a_j\in\mathbb Z/p^3\mathbb Z\), and let \(R\) count the distinct residues \(x\pmod{p^3}\) satisfying \(F(x)=0\pmod{p^3}\).

Put
\[
U_p=p^6-(p-1)p^4-2p(p-1)-\frac{p(p-1)^2}{2}-1
\]
and define the polynomial
\[
L_p(z)=\frac{U_p+(p-1)p^4z+2p(p-1)z^p+\frac{p(p-1)^2}{2}z^{2p}+z^{p^2}}{p^6}.
\]
Then the **entire finite distribution**, including characteristic two, has the exact probability generating function
\[
\boxed{\mathbb E[z^R]=L_p(z)^p.}
\]
When \(p=2\), the equal exponents \(2p=p^2\) are combined, as specified by the polynomial expression. In particular, for all \(d\geq3p\), the law is independent of \(d\). Its moments satisfy
\[
\mathbb ER=1,\quad \operatorname{Var}(R)=3\left(1-\frac1p\right),\quad
\boxed{\mathbb ER^3=5p+5-\frac{17}{p}+\frac8{p^2}}.
\]
As \(p\) tends to infinity through primes, these laws converge weakly to the Poisson distribution with mean one, while \(\mathbb ER^2\to4\), \(\mathbb ER^3\sim5p\), and, for each fixed integer \(k\ge4\),
\[
\boxed{\mathbb ER^k\sim p^{2k-5}}.
\]
The first and second moments above agree with the previously known general prime-power mean and variance; the claimed contribution is the explicit prime-cube law and its higher-moment behavior.

## Assumptions and scope

The coefficient law is the uniform law on **monic degree-\(d\)** polynomials over the finite ring \(\mathbb Z/p^3\mathbb Z\). Roots are residues of that ring, not roots in the field of \(p\)-adic numbers, and a multiple root is counted as one residue. Every prime is included. The hypothesis \(d\ge3p\) is sufficient for the exact law, and no optimality of this degree cutoff is asserted.

## Proof

**Independent local jets.** Let \(S=\mathbb Z/p^3\mathbb Z\). For fixed representatives \(a=0,\ldots,p-1\), consider the monic polynomial \(W(X)=\prod_a(X-a)^3\). Its degree is \(3p\). Since the differences of distinct representatives are units in \(S\), the Chinese remainder theorem gives an isomorphism
\[
S[X]/(W)\ \cong\ \prod_{a=0}^{p-1}S[X]/((X-a)^3)\ \cong\ S^{3p}.
\]
Write the image in the \(a\)-th factor as \(A_a+B_a(X-a)+C_a(X-a)^2\). Each triple is the first three *Hasse* (integral Taylor) coefficients; no division by \(2\) occurs. The coefficients of degree less than \(3p\) in \(F\) are independent and uniform in \(S\). Reduction modulo the monic \(W\) maps those coefficients bijectively to the remainder space, while the other coefficients add a fixed shift. Thus all \(p\) local triples \((A_a,B_a,C_a)\) are independent and uniform in \(S^3\).

**One residue class.** Write a possible root in the class of \(a\) as \(x=a+pu+p^2v\), with \(u,v\in\{0,\ldots,p-1\}\). Hasse-Taylor expansion modulo \(p^3\) shows
\[
F(x)=A_a+(pu+p^2v)B_a+p^2u^2C_a\pmod{p^3}.
\]
If \(A_a\not\equiv0\pmod p\), the class contributes zero roots. If \(A_a\equiv0\pmod p\) and \(B_a\not\equiv0\pmod p\), Hensel's lemma supplies exactly one root modulo \(p^3\) in that class; this has probability \((p-1)/p^2\). If both \(A_a\) and \(B_a\) vanish modulo \(p\), the class has no roots unless \(A_a\equiv0\pmod{p^2}\). The latter event has probability \(p^{-3}\). Conditional on it, write \(A_a=p^2\alpha\), \(B_a=p\beta\) with \(\alpha,\beta\in\mathbb F_p\), and reduce \(C_a\) to \(\gamma\in\mathbb F_p\). These three coefficients are independent and uniform. The root condition is exactly
\[
\alpha+\beta u+\gamma u^2=0\quad\text{in }\mathbb F_p,
\]
with the free \(v\) contributing \(p\) distinct lifts for each solution \(u\).

**Quadratic census.** Among the \(p^3\) triples \((\alpha,\beta,\gamma)\), the counts of quadratics with zero, one, two, and all \(p\) field elements as roots can be encoded by
\[
N_0=\frac{p(p-1)^2}{2}+p-1,\quad N_1=2p(p-1),\quad N_2=\frac{p(p-1)^2}{2},\quad N_p=1.
\]
For odd \(p\) this follows by separating \(\gamma\ne0\) according to the quadratic discriminant, then counting linear and zero polynomials. When \(p=2\), there are \(2,4,2\) polynomials with respectively \(0,1,2\) roots; the same displayed four-term encoding gives \(N_0=2\), \(N_1=4\), and \(N_2+N_p=2\) because \(2=p\). Therefore the probabilities, per residue class, for contributions \(1,p,2p,p^2\) are respectively
\[
\frac{p-1}{p^2},\qquad\frac{2p(p-1)}{p^6},\qquad\frac{p(p-1)^2}{2p^6},\qquad\frac1{p^6},
\]
with coincident outcomes aggregated. The remaining probability corresponds to zero roots. On putting all probabilities over the common denominator \(p^6\), this gives exactly \(L_p(z)\). Independence across residue classes proves \(\mathbb E[z^R]=L_p(z)^p\).

**Moments.** Direct differentiation gives for one local count \(Y\):
\[
\mathbb EY=\frac1p,\qquad\mathbb EY^2=\frac{3p-2}{p^2},\qquad\mathbb EY^3=5-\frac5p+\frac1{p^2}.
\]
Since \(R\) is the sum of \(p\) independent copies of \(Y\), the multinomial identities yield \(\mathbb ER=1\), \(\mathbb ER^2=4-3/p\), and the asserted exact third moment \(5p+5-17/p+8/p^2\).

**Large-prime law and higher moments.** A fixed local class contributes one root with probability \(1/p+O(p^{-2})\); the probability that any of the \(p\) classes contributes at least \(p\) roots is \(O(p^{-2})\). Consequently, total variation distance from the binomial \(\mathrm{Bin}(p,(p-1)/p^2)\) tends to zero, and this binomial converges to \(\mathrm{Poisson}(1)\).

For any fixed \(k\ge4\), the only contribution on the scale \(p^{2k-5}\) comes from a class yielding \(p^2\) roots: each class has this event with probability \(p^{-6}\) for odd \(p\), so the probability of at least one such event is asymptotic to \(p^{-5}\); conditional on exactly one, the other classes contribute \(o(p^2)\) with probability tending to one. The remaining cases, including those with contributions \(p\) or \(2p\) but no \(p^2\), have \(k\)-th moment \(O_k(1+p^{k-2})\), which is lower order because \(k-2<2k-5\) for \(k\ge4\). More explicitly, the number of classes contributing \(p\) or \(2p\) has binomial-type bounded moments of scale \(O_k(p^{-2})\), while the count of simple-root classes has bounded moments. This proves \(\mathbb ER^k\sim p^{2k-5}\). The exact third moment above supplies the separate boundary behavior at \(k=3\).

## Verification

Run `python3 verify.py` (Python standard library only). Its independent coefficient enumeration checks all \(8^6\) monic degree-six polynomials modulo \(8\) and compares their entire root-count distribution with the formula. It also checks the stated local-law coefficients and independently evaluates sample monic polynomials modulo \(27\), \(125\), and \(343\). The exact full modulo-eight enumeration, rather than the samples, verifies the characteristic-two boundary exhaustively. Finite computations do not prove the all-prime theorem.

## Relationship to prior work

Simhi, *Squarefree values of random polynomials are Gaussian mixtures* (2026, arXiv:2610.29911v1), studies local root-count moments modulo **prime squares**, principally in an unrestricted-coefficient model. Earlier Monagan--Tuncer, *Some results on counting roots of polynomials and the Sylvester resultant* (2016, Theorem 1), proves the general mean and variance of root counts modulo any integer, including the formula \(\operatorname{Var}(R)=3(1-1/p)\) here; it explicitly does not supply a formula for the complete root-count distribution. Caruso, *Where are the zeroes of a random \(p\)-adic polynomial?* (2022), studies roots in \(p\)-adic fields and related moments, rather than finite residue counts modulo a cube. The prime-square monic and quadratic distributions previously established in related work do not determine the extra quadratic-singularity and free-lift branches at prime-cube level.

## Limitations

The degree condition \(d\ge3p\) has not been shown necessary. No extension to unrestricted leading coefficients, nonuniform coefficients, prime powers above the cube, or exact root counts over \(\mathbb Q_p\) is asserted. The literature review supports novelty of this explicit law relative to the inspected theorems, but an unindexed formula or implicit derivation in general random-polynomial literature could establish prior coverage. Independent mathematical review has not been performed.

## References

1. O. Simhi, *Squarefree values of random polynomials are Gaussian mixtures* (2026), arXiv:2610.29911v1, https://arxiv.org/abs/2610.29911.
2. M. Monagan and B. Tuncer, *Some results on counting roots of polynomials and the Sylvester resultant* (2016), DMTCS Proceedings, pp. 887--898, https://dmtcs.episciences.org/6371.
3. X. Caruso, *Where are the zeroes of a random p-adic polynomial?* (2022), Forum of Mathematics Sigma 10, e55, doi:10.1017/fms.2022.27.
