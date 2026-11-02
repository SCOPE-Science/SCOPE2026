# Parity selection and universal quartic drift for short-interval Hermite concentration

## Finding
For every fixed integer \(N\ge3\), let \(h_j(x)=(2^j j!\sqrt\pi)^{-1/2}H_j(x)e^{-x^2/2}\) be the normalized physicists' Hermite functions, and set \(V_N=\operatorname{span}\{h_0,\ldots,h_{N-1}\}\). Define
\[
\Lambda_N(a,L)=\sup_{f\in V_N,\ \|f\|_{L^2(\mathbb R)}=1}\int_{a-L}^{a+L}|f(x)|^2\,dx,
\qquad a\in\mathbb R,\quad L>0.
\]
Let \(z_N\) be the smallest positive zero of \(H_N\) if \(N\) is even. For sufficiently small \(L>0\), the global maximizing center is **uniquely** \(a=0\) if \(N\) is odd. If \(N\) is even, the global maximizing centers are exactly \(\pm a_N(L)\), where
\[
a_N(L)=z_N\left(1-\frac{L^4}{90}\right)+O_N(L^6).
\]
More generally, every real zero \(z\) of \(H_N\) continues to a strict local maximum of \(a\mapsto\Lambda_N(a,L)\) with center
\[
a_z(L)=z\left(1-\frac{L^4}{90}\right)+O_{N,z}(L^6).
\]
In particular, the quadratic displacement vanishes **at every rank and every local peak**, while the quartic drift has the same coefficient \(1/90\). No claim is made about global maximizing centers at arbitrary positive interval widths or uniformity as \(N\to\infty\).

## Assumptions and scope
The integer \(N\) is fixed (not growing with \(L\)); \(H_j\) denotes the physicists' Hermite polynomial; all integrals use unweighted real Lebesgue measure. Set \(v(x)=(h_0(x),\ldots,h_{N-1}(x))^T\) and \(\rho(x)=v(x)^Tv(x)\). The exact finite-dimensional concentration matrix is \(G_N(a,L)=\int_{a-L}^{a+L}v(x)v(x)^T\,dx\), and \(\Lambda_N\) is its largest eigenvalue. The asymptotic is for \(L\downarrow0\) with \(N\) fixed; the constants implicit in the remainders depend on \(N\), and on the selected zero for the local statement.

## Proof
**1. Gaussian Hermite kernel peak ordering.** Standard normalized Hermite ladder identities are
\[
h_j'=\sqrt{j/2}\,h_{j-1}-\sqrt{(j+1)/2}\,h_{j+1},\qquad
xh_j=\sqrt{(j+1)/2}\,h_{j+1}+\sqrt{j/2}\,h_{j-1},
\]
with \(h_{-1}=0\), and \(h_j''=(x^2-2j-1)h_j\). Christoffel--Darboux gives
\[
\rho'(x)=-\sqrt{2N}\,h_N(x)h_{N-1}(x).
\]
The real zeros of \(H_N\) and \(H_{N-1}\) are simple and strictly interlace. Consequently the zeros of \(H_N\) are exactly the strict local maxima of \(\rho\); zeros of \(H_{N-1}\) are strict local minima. At a zero \(z\) of \(H_N\), ladder identities and Christoffel--Darboux give
\[
\rho(z)=N h_{N-1}(z)^2=\tfrac12 h_N'(z)^2,\quad
\rho'(z)=0,\quad\rho''(z)=-2\rho(z)<0.
\]
Define \(E_N(x)=h_N'(x)^2+(2N+1-x^2)h_N(x)^2\). The oscillator equation yields \(E_N'(x)=-2x h_N(x)^2\), strictly decreasing between distinct nonnegative zeros. At those zeros \(E_N(z)=2\rho(z)\), so the heights of positive local maxima strictly decrease away from the origin. Thus \(\rho\) has its unique global maximum at zero for odd \(N\), and exactly two global maxima at the first pair \(\pm z_N\) for even \(N\).

**2. Analytic spectral expansion.** Put \(\varepsilon=L^2\). Uniformly on a fixed compact interval of centers, midpoint Taylor expansion gives
\[
\frac{G_N(a,L)}{2L}=vv^T+\varepsilon B+\varepsilon^2 C+O_{N}(\varepsilon^3),\quad
B=\tfrac16(vv^T)'',\quad C=\tfrac1{120}(vv^T)^{(4)},
\]
with enough center derivatives for the implicit-function theorem. The top eigenvalue of the rank-one leading matrix is the simple eigenvalue \(\rho(a)>0\), so analytic symmetric-matrix perturbation yields
\[
\frac{\Lambda_N(a,L)}{2L}=\rho(a)+\varepsilon\mu_1(a)+\varepsilon^2\mu_2(a)+O_N(\varepsilon^3).
\]
For \(p=v^Tv'\), \(q=v^Tv''\), \(b=v^Tv'''\), \(c=v^Tv^{(4)}\), define
\[
w=v''+\frac{2p}{\rho}v'-\left(\frac q\rho+\frac{2p^2}{\rho^2}\right)v.
\]
The Rayleigh--Schrödinger calculation using the orthogonal complement of \(v\) is explicit:
\[
\mu_1=\frac13\left(q+\frac{p^2}{\rho}\right),\qquad
\mu_2=\frac c{60}+\frac{pb}{15\rho}+\frac{q^2}{20\rho}+\frac{\|w\|^2}{36}.
\]
The last term is precisely the second-order mixing with the zero eigenspace; dropping it gives an incorrect displacement coefficient.

**3. Exact cancellations at a Hermite zero.** Fix a real zero \(z\) of \(H_N\). Below all quantities are evaluated at \(x=z\), and \(R=\rho(z)>0\). The ladder relations imply
\[
p=0,\quad p'=-R,\quad v'\!\cdot v''=-zR,\quad
v\!\cdot v'''=zR,\quad v''\!\cdot v'''=0,
\quad v'\!\cdot v'+v\!\cdot v''=-R.
\]
For completeness, these weighted cancellations can be checked without assuming any limit or numerical identity. Let \(d_j=x^2-(2j+1)\), \(t_j=\sqrt{(j+1)/2}\,h_jh_{j+1}\). At a zero of \(h_N\), finite summation by parts gives, for arbitrary scalars \(s_j\),
\[
\sum_{j=0}^{N-1}s_jh_jh_j'
=\sum_{j=0}^{N-2}(s_{j+1}-s_j)t_j.
\]
The position recurrence yields \(\sum t_j=xR/2\) and \(\sum (j+1)t_j=x\sum(2j+1)h_j^2/4\). Taking \(s_j=d_j\) proves \(v'\cdot v''=-xR\); taking \(s_j=d_j^2\) and using \(v'''=2xv+(x^2I-D)v'\), where \(D=\operatorname{diag}(2j+1)\), proves \(v''\cdot v'''=0\). The two displayed identities for \(p'\) and \(v\cdot v'''\) follow from differentiation and the already established \(\rho''=-2R\) and \(\rho'''=-4xR\).

Therefore \(\mu_1'(z)=0\). For the second coefficient, write \(A=v\cdot v''\), \(V=v'\cdot v'\), \(U=v''\cdot v'''\). At \(z\), \(A+V=-R\), \(U=0\), and \(A'=0\). Differentiating \(v^{(4)}=2v+4xv'+(x^2I-D)v''\) gives \(v^{(5)}=6v'+6xv''+(x^2I-D)v'''\). These yield
\[
\frac{d}{dx}(v\cdot v^{(4)})\big|_z=4z(A+V)+2U=-4zR.
\]
Differentiating the formula for \(\mu_2\), and using \(w=v''-(A/R)v\) at \(z\), gives
\[
\mu_2'(z)=\frac{-4zR}{60}-\frac{zR}{15}+\frac{2zR}{18}
=-\frac{zR}{45}.
\]
These are exact identities for every \(N\ge1\), not numerical extrapolations.

**4. Center selection and universal drift.** Each Hermite zero \(z\) is a strict nondegenerate local maximum of \(\rho\), with \(\rho''(z)=-2R\). Analytic implicit-function theory applied to the derivative of the largest eigenvalue yields one local maximizing center \(a_z(L)=z+\alpha L^2+\beta L^4+O(L^6)\). The coefficient equations give
\[
\alpha=-\frac{\mu_1'(z)}{\rho''(z)}=0,\qquad
\beta=-\frac{\mu_2'(z)}{\rho''(z)}=-\frac z{90}.
\]
For fixed \(N\), all entries of \(G_N/(2L)-vv^T\) converge uniformly on the real line to zero, because Hermite products have bounded derivatives, and the limiting kernel \(\rho\) vanishes at infinity. The strict peak ordering from Step 1 therefore confines every global maximizer for small \(L\) to the neighborhoods of the leading Hermite zeros. Local uniqueness from the implicit-function theorem and evenness in \(a\) establish the asserted one-center/two-center classification. In odd rank the center branch at zero remains exactly zero by symmetry.

## Verification
The standalone `checker.py` evaluates Hermite-zero derivative identities for ranks \(1\) through \(12\), and compares high-precision Gram eigenvalues with the derived fourth-order expansion for ranks \(1\) through \(8\). It produced `PASS 195 deterministic assertions` at 55-decimal-digit precision. The code checks finite ranks only; Steps 1--4 are the proof for all fixed ranks. The earlier rank-two expansion is recovered as a consistency check, but that earlier case is not counted as a new contribution.

## Relationship to prior work
Christoffel--Darboux and Hermite ladder identities are classical (see the NIST DLMF orthogonal-polynomial chapter). Lee-Guzmán, Maximenko, Ramos-Vazquez and Sánchez-Nungaray (arXiv:2309.03410v1, September 7, 2023), Sections 7--9, establish a Hermite-function decomposition in polyanalytic Fock analysis; the article does not optimize finite-band interval placement. A previously recorded rank-two Hermite interval analysis gives the special \(N=2\) off-center formula and its quartic correction. The new all-rank claim consists of the parity classification for every fixed rank and the universal \(1/90\) quartic drift at every Hermite-root peak, neither of which is implied by the isolated rank-two example. Generic Christoffel--Darboux formulas alone determine the leading rank-one density, not the mixing coefficient in the finite-window top eigenvalue. No claim of absolute historical priority is made.

## Limitations
The result concerns consecutive initial Hermite bands, not arbitrary sparse masks, weighted windows, higher-dimensional tensor products, or non-small intervals. The expansion is pointwise in fixed rank; there is no rank-uniform remainder. The work is a self-review, without independent audit. Specialized historical literature on Hermite Christoffel maxima or finite-section localization may contain related observations not indexed by the searches used.

## References
1. E. Lee-Guzmán, E. A. Maximenko, G. Ramos-Vazquez, A. Sánchez-Nungaray, *Horizontal Fourier transform of the polyanalytic Fock kernel*, arXiv:2309.03410v1 (first publicly submitted 2023-09-07), Sections 7--9. https://arxiv.org/html/2309.03410v1
2. NIST Digital Library of Mathematical Functions, Section 18.2(v), Christoffel--Darboux identity and confluent formula. https://dlmf.nist.gov/18.2
3. Classical Hermite three-term recurrence, differentiation identities and oscillator equation, as covered in NIST DLMF Chapter 18. https://dlmf.nist.gov/18
