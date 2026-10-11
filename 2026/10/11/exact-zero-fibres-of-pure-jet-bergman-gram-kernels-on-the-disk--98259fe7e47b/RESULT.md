# Exact zero fibres of pure-jet Bergman Gram kernels on the disk

## Finding
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), equipped with unnormalized planar area measure. For every integer \(m\ge0\), let \(\xi^{(m)}=(\delta_{jm})_{j\ge0}\). The corresponding canonical positive-definite kernel \(B_m=B_{\xi^{(m)},\mathbb D}\), formed from the normalized jet functional \(f\mapsto f^{(m)}(z)/m!\), has the exact expression
\[
 B_m(z,w)=\frac{m+1}{\pi}\frac{P_m(z\overline w)}{(1-z\overline w)^{2m+2}},\qquad
 P_m(t)=\sum_{j=0}^{m}\binom mj\binom{m+1}j t^j.
\]
For \(m\ge1\), all \(m\) zeros of \(P_m\) are simple, real, strictly negative, and none equals \(-1\). Exactly \(\lceil m/2\rceil\) lie in \((-1,0)\), and exactly \(\lfloor m/2\rfloor\) lie in \((-\infty,-1)\). Hence the zero set of \(B_m\) in \(\mathbb D\times\mathbb D\) is the union of exactly \(\lceil m/2\rceil\) distinct level sets \(\{(z,w):z\overline w=\tau\}\), where \(\tau\in(-1,0)\) ranges over those interior roots. In particular, the disk is a \(\xi^{(m)}\)-Lu Qi-Keng domain if and only if \(m=0\), whereas every positive pure-jet order produces zeros. The count refers to distinct values of \(z\overline w\), not to the cardinality of the two-variable zero set.

## Assumptions and scope
The Bergman space is \(A^2(\mathbb D)\), norm \(\int_{\mathbb D}|f|^2\,dA\). Its reproducing kernel is \(K(z,w)=1/[\pi(1-z\overline w)^2]\). The differential functional uses the \(1/m!\) factor, in accordance with the sequence convention of Gehlawat, Jain and Sarkar. Every assertion is for integer \(m\ge0\) and \((z,w)\in\mathbb D^2\); all denominators stay nonzero on this domain. The polynomial \(P_m\) is not the Legendre polynomial: Legendre polynomials are denoted below by \(L_m\).

## Proof
The orthogonal monomial expansion of the ordinary Bergman kernel gives
\[
 K(z,w)=\frac1\pi\sum_{k\ge0}(k+1)(z\overline w)^k.
\]
The Riesz representative of \(f^{(m)}(w)/m!\) is the normalized conjugate derivative of \(K\) at \(w\). Therefore differentiating in both variables and dividing by \((m!)^2\) gives
\[
 B_m(z,w)=\frac1\pi\sum_{j\ge0}(j+m+1)\binom{j+m}{m}^{\!2}(z\overline w)^j
 =\frac{m+1}{\pi}{}_2F_1(m+1,m+2;1;z\overline w).
\]
Euler's terminating hypergeometric transformation gives
\[
 {}_2F_1(m+1,m+2;1;t)
 =(1-t)^{-2m-2}{}_2F_1(-m,-m-1;1;t),
\]
and the terminating series equals \(P_m(t)\), proving the displayed rational kernel formula. This identity can also be checked by equating the displayed convergent Taylor coefficients.

Set \(x=(1+t)/(1-t)\), with inverse \(t=(x-1)/(x+1)\). The hypergeometric representation of Jacobi polynomials yields the exact finite polynomial identity
\[
 P_m(t)=(1-t)^m P_m^{(0,1)}\!\left(\frac{1+t}{1-t}\right).
\]
All \(m\) zeros of \(P_m^{(0,1)}\) are simple and belong to \((-1,1)\) by orthogonality for the positive weight \(1+x\). Their inverse Cayley images are simple and belong to \((-\infty,0)\). The inverse transform sends \(x=0\) exactly to \(t=-1\), and sends \(x\in(0,1)\) to \(t\in(-1,0)\).

It remains to count positive Jacobi zeros. Write \(L_k=P_k^{(0,0)}\) for the Legendre polynomials. The finite identity
\[
 (1+x)P_m^{(0,1)}(x)=L_m(x)+L_{m+1}(x)
\]
follows from the standard Jacobi connection formulas (or coefficient comparison). At each zero \(r\) of \(L_{m+1}\), the right side equals \(L_m(r)\), which is nonzero and changes sign between successive zeros of \(L_{m+1}\) by strict Legendre interlacing. Thus the \(m\) zeros of \(P_m^{(0,1)}\) occur exactly one in each gap between the \(m+1\) successive zeros of \(L_{m+1}\); there are no others by the degree bound.

When \(m=2k\) is even, \(L_{m+1}\) is odd, has a simple zero at \(0\), and exactly \(k\) of its zero gaps lie entirely in \((0,1)\). Accordingly the Jacobi polynomial has exactly \(k\) positive zeros. When \(m=2k+1\) is odd, the even polynomial \(L_{m+1}\) has \(k\) positive gaps and one central gap straddling \(0\). The central Jacobi zero is positive: \(P_m^{(0,1)}(0)=L_{m+1}(0)\) has sign \((-1)^{k+1}\), whereas at the smallest positive zero \(r\) of \(L_{m+1}\), the identity gives \((1+r)P_m^{(0,1)}(r)=L_m(r)\), which has sign \((-1)^k\). The latter follows from \((1-r^2)L_{m+1}'(r)=(m+1)L_m(r)\) and the fact that \(L_{m+1}\) crosses its first positive zero from sign \((-1)^{k+1}\). Thus the central zero belongs to \((0,r)\), giving \(k+1\) positive Jacobi zeros. In both parities, \(P_m^{(0,1)}(0)=L_m(0)+L_{m+1}(0)\ne0\) because precisely one of the two consecutive Legendre values at \(0\) is zero and the even-degree value is nonzero. Therefore \(P_m(-1)\ne0\), and the stated numbers of roots on either side of \(-1\) follow.

Finally, for every \(\tau\in(-1,0)\), choose \(z=\sqrt{-\tau}\) and \(w=-\sqrt{-\tau}\). Then \(z,w\in\mathbb D\) and \(z\overline w=\tau\), giving a genuine kernel zero. Conversely \(|z\overline w|<1\) prevents roots in \((-\infty,-1)\) from contributing. The case \(m=0\) reduces to the usual zero-free Bergman kernel.

## Verification
The standalone file `check_jet_kernel.py` checks in exact arithmetic the Jacobi transformation, Legendre connection, denominator coefficient expansions, and the nonvanishing value at \(-1\) for \(0\le m\le12\). It also counts roots numerically from the standard Jacobi root routine for \(1\le m\le12\). The script was actually executed from its package path and printed `VERIFY_OK`. These finite computations corroborate, but do not replace, the preceding arbitrary-order algebraic and interlacing proof.

## Relationship to prior work
Gehlawat, Jain and Sarkar (arXiv:2608.13193v1, August 13, 2026) define the canonical Gram kernel, represent it by derivatives of the ordinary Bergman kernel, and prove upper-half-plane zero-free results, including for all single-coordinate sequences (Proposition 4.5 and Theorem 4.11). The present theorem treats a different domain: it explicitly classifies the roots and zero-fibre counts for *every* pure-jet order on the unit disk. Its nonvanishing conclusion sharply contrasts with the upper-half-plane case; conformal changes do not preserve a fixed order of ordinary jets without mixing lower derivatives. The Jacobi zero and Legendre-interlacing facts themselves are classical and are used, not claimed as new.

## Limitations
The theorem covers only the canonical Gram kernels for a single nonzero derivative coordinate on the unweighted disk. It does not classify mixed jet sequences, general weighted disks, other domains, or arbitrary derivatives under changes of coordinates. The existence of unindexed equivalent evaluations of the disk jet kernel cannot be excluded. The included finite checks do not certify the infinite family independently.

## References
1. Sahil Gehlawat, Aakanksha Jain and Amar Deep Sarkar, *A Canonical Positive Definite Kernel Associated with the ξ-Bergman Kernel*, arXiv:2608.13193v1 (first submitted August 13, 2026), especially §§2–4, Proposition 4.5 and Theorem 4.11. https://arxiv.org/abs/2608.13193
2. NIST Digital Library of Mathematical Functions, §18.16(ii)–(iii), *Zeros of Jacobi and Legendre polynomials*. https://dlmf.nist.gov/18.16
3. NIST Digital Library of Mathematical Functions, Chapter 18, *Classical Orthogonal Polynomials: hypergeometric representations and connection formulas*. https://dlmf.nist.gov/18
