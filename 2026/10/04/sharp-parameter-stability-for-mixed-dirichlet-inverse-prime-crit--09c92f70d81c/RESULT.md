# Sharp parameter stability for mixed Dirichlet-inverse prime criteria
## Finding
For every integer \(k\ge 2\), every real parameter \(t>-2\), and every positive integer \(n\), put
\[
P_{k,t}(n)=\sigma_k^{(-1)}(n)+J_k(n)+2+t(\mu(n)+1),
\]
where \(\sigma_k(n)=\sum_{d\mid n}d^k\), \(\sigma_k^{(-1)}\) is its Dirichlet inverse, \(J_k\) is the \(k\)-th Jordan totient, and \(\mu\) is the Möbius function. Then
\[
P_{k,t}(n)=0\quad\Longleftrightarrow\quad n\text{ is prime}.
\]
Moreover, \(P_{k,-2}(1)=0\). Hence \((-2,\infty)\) is the maximal open interval containing \(t=0\) and \(t=1\) on which this prime-only zero-set statement holds simultaneously for every positive integer.

The endpoints \(t=0\) and \(t=1\) are exactly the two-function and three-function criteria appearing in Liu's recent paper for \(k\ge2\). The new ingredient is a strict sign lemma for the cube-free nonsquarefree case, which makes the entire parameter interval stable rather than merely the two isolated endpoint identities.

## Assumptions and scope
The variables satisfy \(k\in\mathbb Z\) with \(k\ge2\), \(t\in\mathbb R\) with \(t>-2\), and \(n\in\mathbb Z_{>0}\). Dirichlet inversion is with respect to convolution, not pointwise reciprocal. The result is a structural characterization and is not asserted to be an efficient primality test.

For \(n>1\), use the exhaustive factorization split from the source: squarefree; divisible by a prime cube; or cube-free and nonsquarefree. In the last case write uniquely
\[
n=ab^2,\qquad a,b\text{ squarefree},\qquad (a,b)=1,\qquad b>1.
\]
The source gives
\[
\sigma_k^{(-1)}(ab^2)=\mu(a)b^k\sigma_k(a),\qquad
J_k(ab^2)=b^kJ_k(a)J_k(b),
\]
and the prime-power values
\[
\sigma_k^{(-1)}(p)=-(p^k+1),\quad
\sigma_k^{(-1)}(p^2)=p^k,\quad
\sigma_k^{(-1)}(p^e)=0\ (e\ge3).
\]

## Proof
Write
\[
H_k(n)=\sigma_k^{(-1)}(n)+J_k(n)+2,
\qquad P_{k,t}(n)=H_k(n)+t(\mu(n)+1).
\]
At \(n=1\), \(H_k(1)=4\) and \(\mu(1)=1\), hence
\[
P_{k,t}(1)=4+2t>0
\]
for \(t>-2\). If \(n=p\) is prime, then \(H_k(p)=0\) and \(\mu(p)+1=0\), so \(P_{k,t}(p)=0\) for every real \(t\).

Now let \(n\) be composite.

If \(n\) is squarefree with \(r\ge2\) prime factors, write \(q_j=p_j^k\). When \(r\) is even, \(\mu(n)=1\) and
\[
H_k(n)=\prod_{j=1}^r(q_j+1)+\prod_{j=1}^r(q_j-1)+2\ge4.
\]
Therefore \(P_{k,t}(n)=H_k(n)+2t>0\) for \(t>-2\). When \(r\) is odd, necessarily \(r\ge3\) and \(\mu(n)=-1\), so the parameter term vanishes. The difference-of-products estimate
\[
\prod_{j=1}^r(q_j+1)-\prod_{j=1}^r(q_j-1)>2
\]
gives \(H_k(n)<0\), hence \(P_{k,t}(n)\ne0\).

If a prime cube divides \(n\), then \(\sigma_k^{(-1)}(n)=\mu(n)=0\) and \(J_k(n)\) is a positive integer. Thus
\[
P_{k,t}(n)=J_k(n)+2+t>1
\]
for \(t>-2\).

It remains to treat \(n=ab^2\), cube-free and nonsquarefree. Here \(\mu(n)=0\) and
\[
H_k(n)=b^kT+2,
\qquad
T=\mu(a)\sigma_k(a)+J_k(a)J_k(b).
\]
If \(\mu(a)=1\), then \(T>0\) immediately. If \(\mu(a)=-1\), then \(a>1\) is squarefree and
\[
\frac{\sigma_k(a)}{J_k(a)}
=\prod_{p\mid a}\frac{1+p^{-k}}{1-p^{-k}}
<\prod_p\frac{1+p^{-k}}{1-p^{-k}}
=\frac{\zeta(k)^2}{\zeta(2k)}.
\]
Every Euler factor decreases as \(k\) increases, so for integer \(k\ge2\),
\[
\frac{\zeta(k)^2}{\zeta(2k)}
\le \frac{\zeta(2)^2}{\zeta(4)}
=\frac52.
\]
On the other hand, because \(b>1\) is squarefree,
\[
J_k(b)=\prod_{p\mid b}(p^k-1)\ge2^k-1\ge3.
\]
Consequently \(J_k(b)>\sigma_k(a)/J_k(a)\), and therefore
\[
J_k(a)J_k(b)>\sigma_k(a).
\]
Thus \(T>0\) also when \(\mu(a)=-1\). Since \(T\) is an integer, \(T\ge1\); also \(b^k\ge4\). Hence
\[
H_k(n)=b^kT+2\ge6,
\qquad
P_{k,t}(n)=H_k(n)+t>4
\]
for \(t>-2\). This excludes every composite integer.

Finally, at \(t=-2\),
\[
P_{k,-2}(1)=4-4=0.
\]
Thus the prime-only characterization fails at the boundary. Since both \(t=0\) and \(t=1\) lie in \((-2,\infty)\), this proves the stated maximal-open-interval assertion. \(\square\)

## Verification
The proof is exact and infinite; the computation supplied in `verify.py` is only corroborative. It independently implements trial-division factorization, \(\mu\), \(J_k\), and the prime-power formula for \(\sigma_k^{(-1)}\). It checks the claimed zero set for \(2\le k\le6\), \(1\le n\le5000\), and several exact rational parameters on both sides of \(0\) but above \(-2\). It also checks that \(t=-2\) adds \(n=1\) as a zero and verifies positivity in every tested cube-free nonsquarefree case.

The critical infinite step is not inferred from enumeration: it is the exact Euler-product inequality
\[
\frac{\sigma_k(a)}{J_k(a)}<\frac{\zeta(k)^2}{\zeta(2k)}\le\frac52<3\le J_k(b).
\]

## Relationship to prior work
Liu, arXiv:2609.33278v2, proves separately that
\[
H_k(n)=0\Longleftrightarrow n\text{ is prime}
\]
for every \(k\ge1\), and that
\[
H_k(n)+\mu(n)+1=0\Longleftrightarrow n\text{ is prime}
\]
for \(k\ge2\). These are precisely \(t=0\) and \(t=1\) in the family above. The source's proof of the cube-free nonsquarefree case for \(k\ge2\) uses only integrality and divisibility to rule out one target value; it explicitly permits the bracketed factor to be negative in part of its case split. The strict positivity lemma proved here is stronger and is what allows a continuous real parameter interval.

General treatments by Haukkanen and Brown give formulas and background for Dirichlet inverses but do not, in the material inspected, state this mixed \(\sigma_k^{(-1)}\)-\(J_k\)-\(\mu\) parameter family. Targeted searches for equivalent parameterizations and stronger zero-set classifications found the Liu paper but no source covering the interval theorem.

## Limitations
The theorem is restricted to integer \(k\ge2\). The case \(k=1\) behaves differently because the \(t=1\) endpoint already has the exceptional composite zero \(n=18\). The result identifies the maximal open interval containing \(t=0\) and \(t=1\); it does not classify every disconnected real parameter value outside that interval. Direct evaluation generally requires factorization, so no computational speed claim is made. Priority is not claimed beyond the sources and databases actually inspected.

## References
1. Z. Liu, *Prime-Detecting Identities from Dirichlet Inversion and Jordan Totients*, arXiv:2609.33278v2, first publicly posted 2026-09-27.
2. P. Haukkanen, *Expressions for the Dirichlet inverse of arithmetical functions*, Notes on Number Theory and Discrete Mathematics 6 (2000), no. 4, 118–124.
3. P. G. Brown, *Some comments on inverse arithmetic functions*, Mathematical Gazette 89 (2005), no. 516, 403–408, DOI 10.1017/S0025557200178246.
4. OEIS Foundation, A046692, *Dirichlet inverse of sigma function*.
