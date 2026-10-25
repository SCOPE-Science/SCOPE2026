# Exact angular-order crossings and triple resonances in single-degree spherical-cap localization

## Finding
Fix an integer \(\ell\ge1\). Let \(\mathcal H_\ell\) be the complex spherical harmonics of **exact degree** \(\ell\) on \(S^2\), normalized in \(L^2(S^2,d\omega)\), where \(d\omega\) is ordinary area measure. For \(0<c<1\), let \(C_c=\{\omega\in S^2:\omega_3\ge c\}\), and let \(T_{\ell,c}=\Pi_\ell\mathbf1_{C_c}\Pi_\ell\) on \(\mathcal H_\ell\). The eigenvalue associated with absolute azimuthal order \(m\in\{0,\ldots,\ell\}\) is \(\lambda_{\ell,m}(c)\), with multiplicity one at \(m=0\) and two at \(m>0\).

Write \(P_\ell\) for the ordinary Legendre polynomial with \(P_\ell(1)=1\), and use \(P_\ell^{(m)}\) to denote its **ordinary derivative of order** \(m\). For every \(0\le m<\ell\), the following identity holds exactly:

\[
\boxed{\lambda_{\ell,m}(c)-\lambda_{\ell,m+1}(c)
=\frac{2\ell+1}{2}\frac{(\ell-m-1)!}{(\ell+m+1)!}
(1-c^2)^{m+1}P_\ell^{(m)}(c)P_\ell^{(m+1)}(c).}
\]

Consequently, on \(0<c<1\), the two adjacent absolute-order eigenvalues have **exactly** \(\ell-m-1\) equality radii. All are simple sign-changing crossings: they are exactly the positive zeros of the two ordinary Legendre derivatives appearing above. Across all adjacent pairs there are \(\ell(\ell-1)/2\) *indexed* crossings, counting an equality of two different adjacent pairs at the same radius twice.

For \(1\le j\le\ell-1\), three consecutive absolute-order eigenvalues satisfy \(\lambda_{\ell,j-1}(c)=\lambda_{\ell,j}(c)=\lambda_{\ell,j+1}(c)\) **if and only if** \(P_\ell^{(j)}(c)=0\). There are exactly \(\lfloor(\ell-j)/2\rfloor\) such radii for that indexed triple, and \(\lfloor(\ell-1)^2/4\rfloor\) indexed triple resonances in total. **No four consecutive absolute orders** have equal eigenvalues at any \(0<c<1\). These are statements about *absolute-order levels*: a triple of levels may span five or six eigenvectors because of the \(\pm m\) multiplicities; nonconsecutive coincidences are not excluded.

There is a further sharp endpoint change of the leading absolute order: for each fixed \(\ell\ge2\), the largest eigenvalue occurs only at \(m=\ell-1\) for all sufficiently small positive \(c\), whereas it occurs only at \(m=0\) for \(c\) sufficiently close to one. Moreover \(\lambda_{\ell,\ell-1}(c)>\lambda_{\ell,\ell}(c)\) for **every** \(0<c<1\).

## Assumptions and scope
The exact-degree restriction is essential: unlike a standard low-pass Slepian problem, harmonics of different degrees are not mixed. The cap is centered at the north pole with opening angle \(\arccos c\in(0,\pi/2)\). All angular orders are integers and all functions are complex-valued. Rotation transfers the result to any cap center. At the excluded hemisphere \(c=0\), every absolute-order level is \(1/2\), and at the excluded zero-area cap \(c=1\), every level is zero; these boundary coincidences are not counted.

For \(0\le m\le\ell\), define
\[
q_{\ell,m}(t)=\sqrt{\frac{(\ell-m)!}{(\ell+m)!}}(1-t^2)^{m/2}P_\ell^{(m)}(t).
\]
Then \(\int_{-1}^1q_{\ell,m}(t)^2dt=2/(2\ell+1)\). The exact eigenvalue formula is
\[
\lambda_{\ell,m}(c)=\frac{2\ell+1}{2}\int_c^1 q_{\ell,m}(t)^2\,dt.
\]
The normalization holds equally for \(m=0\) and \(m>0\); complex spherical harmonics with orders \(m\) and \(-m\) share the same value.

## Proof
**1. Diagonalization.** The integral of \(Y_{\ell,m}\overline{Y_{\ell,n}}\) over the cap vanishes for \(m\ne n\) by longitudinal integration. The remaining diagonal integral is the stated \(\lambda_{\ell,|m|}(c)\).

**2. Boundary-factor identity.** Fix \(0\le m<\ell\), abbreviate \(q=q_{\ell,m}\), and set \(L=(\ell-m)(\ell+m+1)>0\). The associated Legendre equation and the normalized order-raising identity give
\[
-[(1-t^2)q'(t)]'+\frac{m^2}{1-t^2}q(t)=\ell(\ell+1)q(t),
\quad
q_{\ell,m+1}(t)=\frac{\sqrt{1-t^2}q'(t)+mtq(t)/\sqrt{1-t^2}}{\sqrt L}.
\]
Directly differentiating \(B(t)=(1-t^2)q(t)q'(t)+mtq(t)^2\) gives
\[
B'(t)=L\left(q_{\ell,m+1}(t)^2-q_{\ell,m}(t)^2\right).
\]
As \(t\uparrow1\), \(B(t)\to0\), including the case \(m=0\). Integration from \(c\) to one therefore yields
\[
\lambda_{\ell,m}(c)-\lambda_{\ell,m+1}(c)
=\frac{2\ell+1}{2L}B(c)
=\frac{2\ell+1}{2\sqrt L}\sqrt{1-c^2}\,q_{\ell,m}(c)q_{\ell,m+1}(c).
\]
Substitution of the factorial normalization produces the boxed polynomial factorization, with its strictly positive prefactor on \(0<c<1\).

**3. Counting adjacent crossings.** The polynomial \(P_\ell\) has \(\ell\) simple real roots strictly inside \((-1,1)\). By repeated Rolle's theorem and the degree bound, \(P_\ell^{(m)}\) has precisely \(\ell-m\) simple roots there; its parity is \((-1)^{\ell-m}\). Thus it has \(\lfloor(\ell-m)/2\rfloor\) positive roots. Consecutive derivatives have no common roots because those roots are simple. For the boxed product, the positive-root count is
\[
\left\lfloor\frac{\ell-m}{2}\right\rfloor+
\left\lfloor\frac{\ell-m-1}{2}\right\rfloor=\ell-m-1.
\]
Every zero is simple, so each equality is a strict sign-changing crossing. Summing over \(m\) gives \(\ell(\ell-1)/2\).

**4. Exactly the consecutive triples, and no consecutive quadruples.** At a positive zero of \(P_\ell^{(j)}\), both products for adjacent pairs \((j-1,j)\) and \((j,j+1)\) vanish. Conversely, simultaneous vanishing of these products with \(P_\ell^{(j)}(c)\ne0\) would require \(P_\ell^{(j-1)}(c)=P_\ell^{(j+1)}(c)=0\). Putting \(p=P_\ell^{(j-1)}\), differentiation of Legendre's differential equation gives
\[
(1-t^2)p''(t)-2jt p'(t)+[\ell(\ell+1)-(j-1)j]p(t)=0.
\]
At \(c>0\), the two putative zeros would imply \(p'(c)=0\), contradicting simplicity of the zeros of \(p\). The triple condition is therefore exact. Its positive-root count is \(\lfloor(\ell-j)/2\rfloor\), whose sum over \(j=1,\ldots,\ell-1\) is \(\lfloor(\ell-1)^2/4\rfloor\). For a fourth consecutive equality, a root of \(P_\ell^{(j)}\) would also have to be a root of \(P_\ell^{(j+1)}\) or \(P_\ell^{(j+2)}\). The first violates simplicity and the second violates the same differential equation argument with \(p=P_\ell^{(j)}\). Hence no four consecutive levels coincide.

**5. Leading order near the two endpoints.** Parity gives \(\lambda_{\ell,m}(0)=1/2\). Write \(d_m(c)=1/2-\lambda_{\ell,m}(c)\). If \(\ell-m\) is even, \(q_{\ell,m}(0)\ne0\), so \(d_m(c)\) has a strictly positive linear term in \(c\). If \(\ell-m\) is odd, then \(q_{\ell,m}(0)=0\) and
\[
d_m(c)=\frac{2\ell+1}{6}q_{\ell,m}'(0)^2c^3+O_\ell(c^5).
\]
The parity-odd indices are \(m=\ell-1,\ell-3,\ldots\). The ladder identity and the differential equation at zero imply, whenever both indices are in this sequence,
\[
\frac{q_{\ell,m+2}'(0)^2}{q_{\ell,m}'(0)^2}
=\frac{(\ell-m-1)(\ell+m+2)}{(\ell-m)(\ell+m+1)}<1.
\]
Thus the unique smallest positive cubic deficit is at \(m=\ell-1\), yielding the near-hemisphere top order. For \(c\uparrow1\), \(q_{\ell,0}(1)=1\), while \(q_{\ell,m}(t)=O_\ell((1-t)^{m/2})\) for every \(m\ge1\). Hence \(\lambda_{\ell,0}(c)\) is of order \(1-c\) and all other orders are \(O_\ell((1-c)^{m+1})\), proving strict pole-cap dominance of \(m=0\). Finally, the derivative polynomial \(P_\ell^{(\ell-1)}(c)\) is a positive multiple of \(c\) and \(P_\ell^{(\ell)}\) is positive, so the boxed factorization proves \(\lambda_{\ell,\ell-1}>\lambda_{\ell,\ell}\) throughout.

## Verification
Run `python check.py` with SymPy. It checks the normalized cap-integral expression against the boundary product by exact rational polynomial integration for degrees \(1\) through \(11\), root counts for every adjacent pair, the nonexistence of positive common roots two derivatives apart, and the near-equator cubic ordering. The recorded output is in `check-output.txt`. These finite tests **do not** establish the theorem for arbitrary \(\ell\); Steps 2–5 are its all-degree proof.

For a concrete illustration at \(\ell=3\), the positive zero \(c=1/\sqrt5\) of \(P_3'(c)\) gives \(\lambda_{3,0}=\lambda_{3,1}=\lambda_{3,2}\), whereas the adjacent pair \((0,1)\) also crosses at \(c=\sqrt{3/5}\). There is no four-order coincidence in either case. The full spherical-harmonic eigenspace multiplicity at the triple absolute-order resonance is at least five because the nonzero orders occur in pairs.

## Relationship to prior work
Michel–Plattner–Seibert (2021), Section 3, develops spherical-cap Slepian concentration matrices and commuting operators using spin-weighted spherical harmonics; the ordinary scalar, fixed-degree subspace is within the same setting. Simons–Dahlen–Wieczorek (2006), Section 4, develops fixed-order block diagonalization and the defining Legendre-integral kernels for low-pass spherical Slepian functions. Those results supply the **general concentration framework**. The theorem here concerns the *all-degree, within-one-multipole* boundary factorization, the **exact number** of positive-radius adjacent order crossings, and the complete classification of consecutive triple coincidences, rather than the general operator's eigenvalue formula or the hemisphere-only half-energy equality. Classical Legendre raising and zero-interlacing relations are used openly as inputs.

## Limitations
The theorem says nothing about equality between nonadjacent absolute orders, nor does it give a closed-form global optimizer for every cap radius or arbitrary low-pass degree combinations. A triple of distinct absolute-order labels does not mean an eigenspace of dimension three. The root-interlacing proof relies on integer-degree Legendre polynomials on \(S^2\); higher-dimensional Gegenbauer systems and spin-weighted analogues require separate analysis. Related older integral identities may exist, so independent bibliographic-priority verification remains necessary.

## References
1. V. Michel, A. Plattner, K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650, initially posted 2021-03-26; especially Sections 2–3. https://arxiv.org/abs/2103.14650
2. F. J. Simons, F. A. Dahlen, M. A. Wieczorek, *Spatiospectral concentration on a sphere*, SIAM Review 48 (2006), 504–536; and the related treatment of axisymmetric caps in *Spherical Slepian functions and the polar gap in geodesy*, Geophysical Journal International 166 (2006), 1039–1061, Section 4. https://academic.oup.com/gji/article/166/3/1039/2140074
3. NIST Digital Library of Mathematical Functions, Chapter 14, associated Legendre/Ferrers function equations and identities. https://dlmf.nist.gov/14
4. S. N. Samaddar, *Some Integrals Involving Associated Legendre Functions*, Mathematics of Computation 28 (1974), 257–263; identified as possible earlier integral-formula coverage, not fully inspected. DOI 10.2307/2005832.
