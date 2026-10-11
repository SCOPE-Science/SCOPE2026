# All exponential spectra of the cubic graph over prime-square cyclic rings

## Finding
For every prime \(p\ge5\), let \(R=\mathbb Z/p^2\mathbb Z\), \(G=R^2\), and let
\[
E_p=\{(t,t^3):t\in R\}\subset G.
\]
A **frequency spectrum** of \(E_p\) is an unordered \(p^2\)-point set \(\Lambda\subset G\) for which the characters \(e_\lambda(x)=\exp(2\pi i\langle\lambda,x\rangle/p^2)\), restricted to \(E_p\) and normalized by \(p^{-1}\), form an orthonormal basis of \(\ell^2(E_p)\). Distinct ambient character labels are counted separately.

Write \(\chi_p\) for the quadratic character of \(\mathbb F_p\), with \(\chi_p(0)=0\). Define the permitted slopes
\[
D_p=\{0\}\cup\{s\in\mathbb F_p^\times:\chi_p(-3s)=-1\};\qquad |D_p|=(p+1)/2.
\]
**Classification.** Every frequency spectrum, and only such spectra, is obtained as follows. Choose \(s\in D_p\) and \(b\in\mathbb F_p\). For each \(r\in\mathbb F_p\), choose the canonical integer residues \(r_0,t_r\in\{0,\dots,p-1\}\) of \(r,sr+b\). Then independently choose one of these \(p\)-point subsets of the residue fibre over \((r,sr+b)\):
\[
H_{r,c}=\{(r_0+p a,t_r+p c):a\in\mathbb F_p\},\qquad c\in\mathbb F_p;
\]
if \(p\equiv2\pmod3\), one may also choose
\[
V_{r,c}=\{(r_0+p c,t_r+p a):a\in\mathbb F_p\},\qquad c\in\mathbb F_p.
\]
The desired spectrum is \(\Lambda=\bigcup_{r\in\mathbb F_p}L_r\), where every \(L_r\) is one of the allowed fibre lines. The description is unique: its reduced affine line, every fibre orientation, and every fibre offset are recovered from \(\Lambda\).

Thus the exact number of unordered spectra is
\[
\boxed{\mathcal N_p=\frac{p(p+1)}2\,[p(1+\mathbf1_{p\equiv2\pmod3})]^p.}
\]
For instance \(\mathcal N_5=1{,}500{,}000\) and \(\mathcal N_7=23{,}059{,}204\). No other spectra exist.

## Assumptions and scope
The result concerns all primes \(p\ge5\), additive characters of \(R^2\), the indicated set of exactly \(p^2\) graph points, and *orthogonal* bases. It excludes \(p=2,3\), composite base moduli not of prime-square form, unequal point weights, and nonorthogonal Riesz bases. The statement counts frequency sets, not orderings or common-shift equivalence classes. No field structure on \(R\) is assumed.

## Proof
**Step 1: exact Fourier-zero criterion.** Write
\[
S_p(u,v)=\sum_{t\in R}\exp\!\bigl(2\pi i(ut+vt^3)/p^2\bigr).
\]
Two distinct characters are orthogonal on \(E_p\) precisely when \(S_p\) vanishes at their frequency difference. Denote reduction modulo \(p\) by a bar. If both coefficients are divisible by \(p\), say \((u,v)=(pU,pV)\), then
\[
S_p(pU,pV)=p\sum_{a\in\mathbb F_p}\exp\!\bigl(2\pi i(Ua+Va^3)/p\bigr).
\]
The prime-level sum vanishes if and only if the polynomial \(a\mapsto Ua+Va^3\) permutes \(\mathbb F_p\): by irreducibility of \(1+z+\cdots+z^{p-1}\), a sum of exactly \(p\) \(p\)-th roots vanishes precisely when all residues occur once. The only nonconstant permutation polynomials of this special shape are \(Ua\) with \(U\ne0,V=0\), and, when \(p\equiv2\pmod3\), \(Va^3\) with \(U=0,V\ne0\).

For completeness, if \(U,V\ne0\), rescale to \(f(a)=a^3+ca\) with \(c\ne0\). A permutation would require \(3(a+h/2)^2+c+h^2/4\ne0\) for every \(h\ne0\) and \(a\); hence \(\chi_p(h^2+4c)=-\chi_p(-1/3)\) for all \(h\ne0\). Its sum over those \(h\) would have absolute value \(p-1\). Yet, counting pairs \((y,h)\) satisfying \((y-h)(y+h)=4c\) gives \(\sum_{h\in\mathbb F_p}\chi_p(h^2+4c)=-1\), so the sum over nonzero \(h\) is \(-1-\chi_p(c)\) of absolute value at most \(2\). This contradicts \(p\ge5\). The cubic monomial is a permutation precisely when \(\gcd(3,p-1)=1\).

For primitive \((u,v)\), expand \(t=a+pz\) with \(a,z\in\{0,\dots,p-1\}\):
\[
S_p(u,v)=p\sum_{\substack{a\in\mathbb F_p\\\bar u+3\bar v a^2=0}}
\exp\!\bigl(2\pi i(ua+va^3)/p^2\bigr).
\]
There are at most two roots. A sum of one root of unity cannot vanish; two roots of unity of odd order \(p^2\) cannot cancel. Thus, for primitive frequencies, vanishing is *equivalent* to the derivative equation having no root. Explicitly this is exactly one of
\[
\bar v=0,\ \bar u\ne0,\qquad\text{or}\qquad
\bar u\bar v\ne0,\ \chi_p(-\bar u/(3\bar v))=-1.
\]
In particular a primitive difference with \(\bar u=0\), \(\bar v\ne0\) never gives orthogonality.

**Step 2: saturation of residue fibres.** Let \(\Lambda\) be a spectrum. Any two distinct residue pairs \((\bar u,\bar v)\in\mathbb F_p^2\) represented in \(\Lambda\) must have different first coordinates: otherwise their difference would be primitive and vertical, forbidden by Step 1. Thus at most \(p\) residue pairs occur. Inside any fixed residue fibre, Step 1 says allowable nonzero second-digit differences are horizontal only, or horizontal/vertical when \(p\equiv2\pmod3\). A set whose pairwise differences are horizontal/vertical lies entirely on one horizontal or vertical line: choose two distinct points, then any third compatible with both lies on their common line. Therefore each residue fibre contributes at most \(p\) frequencies. Since \(|\Lambda|=p^2\), exactly \(p\) residue fibres occur and each contains a full permitted line of \(p\) points. The reduced frequency set has the form
\[
A_f=\{(r,f(r)):r\in\mathbb F_p\}
\]
for a function \(f:\mathbb F_p\to\mathbb F_p\).

**Step 3: direction rigidity.** Every slope between two different points of \(A_f\) belongs to \(D_p\) by the primitive zero criterion: slope zero is allowed; nonzero slope \(s\) is allowed exactly when \(\chi_p(-3s)=-1\). Rédei–Megyesi's direction theorem says any noncollinear set of \(p\) points in \(\mathbb F_p^2\) determines at least \((p+3)/2\) directions. The source's theorem and its proof have been checked, including the prime-field hypothesis and the noncollinearity requirement; here only \((p+1)/2\) directions are available. Hence \(A_f\) is a line. The distinct-first-coordinate property makes it the graph of \(f(r)=sr+b\), and its unique slope satisfies \(s\in D_p\).

**Step 4: construction, uniqueness, count.** For any allowed reduced line, choose the full horizontal lift line in each of its \(p\) residue fibres; when \(p\equiv2\pmod3\), the full vertical lift line is an additional option. Pairs in the same fibre differ by an imprimitive allowed direction; pairs in different fibres differ by a primitive allowed direction. Thus all \(p^2\) restricted characters are pairwise orthogonal, hence form a basis. Conversely Steps 2–3 force precisely these choices. There are \(|D_p|=(p+1)/2\) slopes, \(p\) intercepts, and \(p\) or \(2p\) distinct choices independently in each fibre. This gives the claimed count without overcounting.

## Verification
The standalone `verify.py` uses exact integer arithmetic. It verifies the full prime-level zero classification for \(p=5,7,11,13\); computes every Fourier zero modulo \(p^2\) for those primes using coefficient divisibility by \(\Phi_{p^2}\), independently of the derivative formula; enumerates all reduced graph functions for \(p=5,7\) (only affine allowed-slope graphs survive); and explicitly checks orthogonality of 26 complete constructed spectra for \(p=5,7,11\). The finite tests do not establish the assertion for unbounded primes; the proof above does, relying on the cited Rédei–Megyesi theorem.

To reproduce: run `python3 verify.py` in a Python 3 environment without external dependencies. The resulting summary begins `VERIFY_OK`.

## Relationship to prior work
Cochrane and Zheng establish general prime-power stationary-phase formulas for polynomial exponential sums; the present derivative reduction is elementary and compatible with that theory, but their results do not classify all mutually orthogonal character bases of a particular prime-square polynomial graph or enumerate all fibre configurations. Rédei–Megyesi's established direction theorem (with a complete later proof by Somlai) supplies a vital geometry bound but does not determine which slopes are Fourier-orthogonal or how the fibres lift. Finite-field spectral-pair theory establishes existence and general graph criteria over prime fields; the ring \(\mathbb Z/p^2\mathbb Z\) and classification of *all* bases require additional arguments. The result is an explicit Fourier-geometry synthesis for this canonical curved graph, not a claim to new stationary-phase or direction theorems.

## Limitations
The classification is restricted to the prime-square cubic graph, and no claim is made for arbitrary polynomials, higher prime powers, other groups, or nonorthogonal bases. It uses the published Rédei–Megyesi direction theorem as a substantive input. A historical equivalent formulation in the literature on ring spectral sets or permutation polynomials cannot be categorically excluded; exhaustive priority certification and independent validation have not been performed. Computations are finite corroboration, never an infinite proof.

## References
1. T. Cochrane and Z. Zheng, *Pure and mixed exponential sums*, Acta Arithmetica **91** (1999), 249–278, DOI: 10.4064/aa-91-3-249-278, especially Theorem 2.1 (general stationary phase).
2. L. Rédei, *Lacunary Polynomials over Finite Fields* (1973 English translation), direction theorem; see G. Somlai, *A new proof of Rédei's theorem on the number of directions*, arXiv:2212.12823v1 (2022), DOI: 10.1007/s00013-024-01979-x, Theorem 1.1 and Section 3.
3. A. Iosevich, A. Mayeli and J. Pakianathan, *The Fuglede Conjecture holds in \(\mathbb Z_p\times\mathbb Z_p\)*, arXiv:1505.00883v1 (2015), Theorem 1.3.
4. C. Aten et al., *Tiling sets and spectral sets over finite fields*, arXiv:1509.01090v1 (2015), Section 6.
5. M. N. Kolountzakis and M. Matolcsi, *Complex Hadamard matrices and the spectral set conjecture*, arXiv:math/0411512v1 (2004), Section 2.
6. R. Shi, *Equi-distributed property and spectral set conjecture on \(\mathbb Z_{p^2}\times\mathbb Z_p\)*, J. London Math. Soc. **102** (2020), 1030–1046, DOI: 10.1112/jlms.12346 (neighboring ambient group; abstract consulted).
