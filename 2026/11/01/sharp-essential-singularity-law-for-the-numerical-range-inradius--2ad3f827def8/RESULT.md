# Sharp essential-singularity law for the numerical-range inradius of Dirichlet-series translations

## Finding
For every fixed \(\sigma>0\), let \(T_{\sigma,t}f(s)=f(s+\sigma+it)\) act on the Hardy Hilbert space \(\mathcal H^2\) of ordinary Dirichlet series with square-summable coefficients. Define \(r_{\sigma,t}\) as the largest radius of a Euclidean closed disk centered at zero and contained in \(\overline{W(T_{\sigma,t})}\). Then \(r_{\sigma,0}=0\); for every nonzero real \(t\), one has \(r_{\sigma,t}>0\); and
\[
\boxed{\lim_{t\to0}\frac{\sigma}{|t|}\exp\left(\frac{\pi\sigma}{|t|}\right)r_{\sigma,t}=e^{-1}.}
\]
The coefficient is a genuine sharp limit, not merely a logarithmic exponential rate. It quantifies the collapse of numerical-range disk inclusion as a nonreal translation approaches a positive real one.

## Assumptions and scope
The Hilbert space \(\mathcal H^2\) consists of series \(f(s)=\sum_{n\ge1}a_n n^{-s}\) with \(\|f\|^2=\sum_{n\ge1}|a_n|^2\). The functions \(e_n(s)=n^{-s}\) form its orthonormal basis. The parameters satisfy \(\sigma>0\) fixed and \(t\in\mathbb R\). Numerical range means \(W(T)=\{\langle Tf,f\rangle:\|f\|=1\}\), and the closure in the definition of the inradius is essential for clarity, although this operator has closed numerical range when \(t\ne0\). The elementary proof below does not require any global finite-vertex description of that numerical range.

## Proof
**1. Spectral convexity and symmetry.** On the basis above,
\[
T_{\sigma,t}e_n=n^{-\sigma-it}e_n.
\]
Thus this is a bounded diagonal normal operator and
\[
K_{\sigma,t}:=\overline{W(T_{\sigma,t})}
=\overline{\operatorname{co}}\{n^{-\sigma-it}:n\ge1\}.
\]
The zero limit point is included automatically. Conjugation gives \(K_{\sigma,-t}=\overline{K_{\sigma,t}}\), so it suffices to take \(t>0\). At \(t=0\), all eigenvalues are positive real and \(K_{\sigma,0}=[0,1]\), hence the centered disk radius is zero.

**2. Upper bound by the continuous logarithmic spiral.** Set \(a=\sigma/t\), \(u=t\log n\) and \(z_a(u)=e^{-au}e^{-iu}\). All eigenvalues lie on this spiral at \(u\ge0\). Its positive imaginary coordinate is \(-e^{-au}\sin u\). In the first positive-imaginary half-turn \(\pi<u<2\pi\), the maximum occurs at
\[
v_a=\arctan(1/a),\quad U_a=\pi+v_a,\quad m_a=\frac{e^{-a(\pi+v_a)}}{\sqrt{1+a^2}}.
\]
The positive-imaginary maxima on subsequent half-turns decay by the factor \(e^{-2\pi a}\), so \(\operatorname{Im}z_a(u)\le m_a\) for all \(u\ge0\). A centered disk of radius \(r\) contains \(ir\); since every point of \(K_{\sigma,t}\) has imaginary part at most \(m_a\),
\[
r_{\sigma,t}\le m_a.\tag{1}
\]

**3. Three eigenvalues supply an asymptotically matching inscribed disk.** Put \(V=\pi/2\), \(B_a=e^{-aV}\), and \(A_a=e^{-aU_a}\cos v_a\). At \(u=U_a\), the spiral is \(-A_a+im_a\), with the exact identity \(A_a/m_a=a\). Take the integers
\[
N_Q=\left\lceil e^{V/t}\right\rceil,\qquad N_R=\left\lceil e^{U_a/t}\right\rceil.
\]
Let \(Q=N_Q^{-\sigma-it}\) and \(R=N_R^{-\sigma-it}\), and set \(P=1\). For fixed \(\sigma>0\) and \(t\downarrow0\), the ceiling estimate implies
\[
0\le t\log N_Q-V\le t e^{-V/t},\qquad 0\le t\log N_R-U_a\le t e^{-U_a/t}.
\]
(The inequalities hold once the exponents are sufficiently large; they follow from \(0\le\lceil x\rceil-x<1\) and \(\log(1+h)\le h\).) Since \(a t=\sigma\) is fixed, exponentiation and the trigonometric expansions give
\[
\operatorname{Im}Q=-B_a(1+o(1)),\quad \operatorname{Re}Q\le0,\quad
|\operatorname{Re}Q|/B_a=o(1),
\]
\[
\operatorname{Re}R=-A_a(1+o(1)),\qquad \operatorname{Im}R=m_a(1+o(1)).\tag{2}
\]
For small positive \(t\), the real part of \(Q\) is nonpositive and that of \(R\) is strictly negative, while the imaginary parts have opposite signs. Thus zero is in the interior of the triangle \(\Delta=\operatorname{co}\{P,Q,R\}\), which lies inside \(K_{\sigma,t}\).

We estimate the distances from zero to the three lines supporting the triangle sides. Since
\[
\frac{A_a}{B_a}=e^{-a(U_a-V)}\cos v_a\longrightarrow0,\quad
\frac{m_a}{B_a}\longrightarrow0,\quad
\frac{A_a}{m_a}=a\longrightarrow\infty,
\]
the side \(PR\) has distance \(m_a(1+o(1))\), while \(PQ\) has distance \(B_a(1+o(1))\gg m_a\). For \(QR\), write \(Q=-b-iB\), \(R=-A+ iM\), with \(b\ge0\), \(B=B_a(1+o(1))\), \(A=A_a(1+o(1))\), \(M=m_a(1+o(1))\). The line distance is
\[
\frac{bM+AB}{|Q-R|}\ge A(1+o(1)),
\]
because \(|Q-R|=B_a(1+o(1))\). Hence this third distance also exceeds \(m_a(1-o(1))\). The inradius of a triangle measured **from a fixed interior center**, here zero, is the minimum of its three side-line distances. Consequently
\[
r_{\sigma,t}\ge m_a(1-o(1)).\tag{3}
\]
Combining (1) and (3) yields \(r_{\sigma,t}\sim m_a\).

**4. Evaluation of the coefficient.** As \(a\to\infty\), \(a\arctan(1/a)\to1\) and \(a/\sqrt{1+a^2}\to1\). Therefore
\[
\lim_{a\to\infty}a e^{\pi a}m_a
=\lim_{a\to\infty}\frac{a}{\sqrt{1+a^2}}e^{-a\arctan(1/a)}=e^{-1}.
\]
As \(a=\sigma/t\), this proves the sharp asymptotic for positive \(t\), and complex conjugation proves the formula with \(|t|\).

**5. Interior inclusion for every nonreal shift.** For fixed \(t>0\), the mesh \(t\log(n+1)-t\log n\to0\). Modulo \(2\pi\), points \(t\log n\) therefore approach arbitrarily large prescribed phases, for instance \(2\pi/3\) and \(4\pi/3\). Two corresponding nonzero eigenvalues have negative real parts and imaginary parts of opposite signs. Together with \(1\), they form a triangle containing zero in its interior. Hence \(r_{\sigma,t}>0\) for any \(t>0\), and similarly for \(t<0\). The theorem is proved.

## Verification
The accompanying `verify.py` independently evaluates the two spiral landmark eigenvalues, the triangle side distances and their asymptotic comparison with the exact continuous upper bound for several positive shifts. It checks signs, geometric placement and the relevant finite inequalities; these finite tests do not replace the uniform limiting estimates established above. Reproduce with `python3 verify.py` using only the Python standard library. The analytical proof is self-contained.

## Relationship to prior work
Finet and Queffélec (2004) studied numerical ranges of composition operators on this same Dirichlet-series Hilbert space, including normal translations. Their known polygonal description is **prior input** and is not claimed as novel. Lahiri–Ojha–Halder–Birbonshi (2026), Proposition 2.8(c), explicitly reproduces the qualitative closed-polygon property for a nonreal constant shift, but neither that proposition nor its disk-inclusion section states the sharp centered inradius at the boundary \(t\to0\). The new statement extracts an exponential boundary-layer scale and its exact \(e^{-1}\) constant from the arithmetic density of the spectral spiral sample. A related published numerical-range inradius result for contracting dilations on *weighted Dirichlet Hilbert spaces* has a geometric spectral sampling sequence and a fractional-phase oscillation, not the Dirichlet-series eigenvalue sequence \(n^{-\sigma-it}\). These are distinct operator objects; the present limit has a nonoscillating coefficient. A possible older indirect derivation from the normal-case polygon characterization remains a publication-priority risk.

## Limitations
The formula is a fixed-\(\sigma>0\), small-imaginary-shift asymptotic. It does not give the exact inradius at arbitrary nonzero \(t\), uniformity as \(\sigma\) varies, or results for nonconstant weights or nonlinear composition symbols. The 2004 primary text was not available in full through the accessible sources, so possible previously published sharper formulas there could not be excluded independently. This is a mathematical proof subjected to self-review, not independent certification.

## References
1. S. Lahiri, S. Ojha, S. Halder and R. Birbonshi, *Numerical range and invariant subspaces of weighted composition operators on the Hardy space of Dirichlet series*, arXiv:2608.29294v1 (first publicly posted 2026-08-29), https://arxiv.org/abs/2608.29294. Especially Proposition 2.8 and Section 3.
2. C. Finet and H. Queffélec, *Numerical range of composition operators on a Hilbert space of Dirichlet series*, Linear Algebra Appl. 377 (2004), 1–10, DOI: 10.1016/j.laa.2003.05.003. Full text not accessed.
3. C. Finet, H. Queffélec and A. Volberg, *Image numérique et compacité d'opérateurs de composition sur un espace de Hilbert de séries de Dirichlet*, C. R. Math. 335 (2002), 325–328, DOI: 10.1016/S1631-073X(02)02483-4.
