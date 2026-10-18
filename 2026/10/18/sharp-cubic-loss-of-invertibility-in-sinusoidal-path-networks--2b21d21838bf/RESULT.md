# Sharp cubic loss of invertibility in sinusoidal path networks

## Finding

For every integer \(N\ge 2\), let \(K_N\) be the real symmetric tridiagonal matrix of size \(N\) with diagonal entries \(2\), adjacent off-diagonal entries \(-1\), and every other entry zero. On \(\mathbb T^N=(\mathbb R/2\pi\mathbb Z)^N\), define the sinusoidal path map
\[
G_h(z)=z+hK_N\sin z\pmod{2\pi},\qquad h>0,
\]
with coordinatewise sine. Put
\[
\lambda_N=2+2\cos\!\left(\frac{\pi}{N+1}\right),\qquad h_c=\lambda_N^{-1},\qquad p=(\pi,\ldots,\pi).
\]

**The sharp first loss of invertibility has three distinct stages.**

1. At \(h=h_c\), the map \(G_{h_c}\) is a *global homeomorphism*, although its derivative is singular exactly at \(p\). Its inverse is locally Hölder continuous with exponent \(1/3\) at \(p\), and no larger Hölder exponent is possible there.
2. For each fixed \(N\) there is \(\delta_N>0\) such that, for every \(h_c<h<h_c+\delta_N\), the target \(p\) has **exactly three** distinct preimages: \(p\) and two nontrivial points \(z^+(h),z^-(h)\). Writing \(\varepsilon=h\lambda_N-1\), their coordinates, using representatives near \(p\), satisfy
\[
z_i^\pm(h)=\pi\pm 2\sqrt{2\varepsilon}\,(-1)^{i-1}\sin\!\left(\frac{i\pi}{N+1}\right)+O_N(\varepsilon^{3/2}),\qquad 1\le i\le N.
\]
3. Throughout that short interval above \(h_c\), \(p\) remains a linearly attracting fixed point. In particular, the exact three-to-one fiber appears *before* the attraction multiplier reaches \(-1\), at the distinct threshold \(h=2/\lambda_N\).

The subcritical interval \(0<h<h_c\) is already known to consist of Morse–Smale diffeomorphisms [1]; the endpoint topology, optimal inverse regularity, and emergent three-point fiber are the new assertions.

## Assumptions and scope

Here \(N\) is finite and at least two; the path edges all have unit weight; \(h\) is a positive real step. The topology, dimension, preimage count, and modulus-of-continuity claims concern the quotient torus, not unrestricted non-periodic lifts. We use the Euclidean norm on a sufficiently small lift neighborhood of \(p\); on a compact torus all smooth local norms are equivalent. The constants implicit in \(O_N\) may depend on fixed \(N\), and \(\delta_N\) is an existence bound rather than a uniform-in-\(N\) constant.

The eigenvalues of \(K_N\) are \(2-2\cos(k\pi/(N+1))\), for integers \(1\le k\le N\). A real unit top eigenvector, with entries nonzero, is
\[
v_i=(-1)^{i-1}\sqrt{\frac{2}{N+1}}\sin\!\left(\frac{i\pi}{N+1}\right).
\]

## Proof

**1. Unique endpoint singularity.** Write \(K=K_N\), \(\lambda=\lambda_N\), \(h_c=1/\lambda\), and let \(\widetilde G_h\) be the standard lift. Its Jacobian is \(I+hK\operatorname{diag}(\cos z_i)\). Multiplication on the left by \(K^{-1}\) yields the symmetric matrix
\[
K^{-1}D\widetilde G_{h_c}(z)=\underbrace{(K^{-1}-h_c I)}_{\succeq0}+h_c\operatorname{diag}(1+\cos z_i).
\]
The first summand is positive semidefinite and has kernel precisely \(\mathbb Rv\), because the maximal eigenvalue is simple. Every coordinate of \(v\) is nonzero. Since the second summand is diagonal positive semidefinite, their sum can have a kernel only when all \(\cos z_i=-1\). At that point it has one-dimensional kernel \(\mathbb Rv\). Thus \(p\) is the only singular point modulo \(2\pi\), with corank one.

**2. The critical map remains globally one-to-one and onto.** For different lifts \(x,y\in\mathbb R^N\), set \(d=x-y\). Integration along the segment gives
\[
d^TK^{-1}\bigl(\widetilde G_{h_c}(x)-\widetilde G_{h_c}(y)\bigr)
=d^T(K^{-1}-h_cI)d+h_c\sum_{i=1}^Nd_i^2\int_0^1\bigl(1+\cos(y_i+td_i)\bigr)\,dt>0.
\]
The strict inequality holds since \(d\ne0\): for at least one \(d_i\ne0\), the integrand is nonnegative and cannot vanish throughout its nondegenerate segment. Therefore the lift is injective. Equivariance \(\widetilde G_h(x+2\pi k)=\widetilde G_h(x)+2\pi k\) for integer vectors \(k\) implies injectivity of the quotient map as well: any equality of torus images reduces to equality of two appropriately translated lifts. The quotient is homotopic to the identity, hence has degree one and is surjective. Being a continuous bijection of a compact Hausdorff space, it is a homeomorphism. It is a smooth local diffeomorphism away from \(p\).

**3. The optimal cubic inverse Hölder exponent.** Put \(z=p+u\); near \(p\) the displacement from the fixed image is \(F(u)=u-h_cK\sin u\). For \(u,w\) in a sufficiently small coordinate cube and \(d=u-w\), the identity from part 2 becomes
\[
d^TK^{-1}(F(u)-F(w))=d^T(K^{-1}-h_cI)d+h_c\sum_i d_i^2\int_0^1[1-\cos(w_i+td_i)]\,dt.
\]
On \(|s|\le1\), \(1-\cos s\ge s^2/4\). For arbitrary real \(a,b\), \(\int_0^1(a+tb)^2dt\ge b^2/12\). Therefore
\[
d^TK^{-1}(F(u)-F(w))\ge\frac{h_c}{48}\sum_i d_i^4\ge\frac{h_c}{48N}\|d\|_2^4.
\]
By Cauchy–Schwarz, the left side is at most \(\|K^{-1}\|_2\|d\|_2\|F(u)-F(w)\|_2\). Canceling \(\|d\|_2\) proves
\[
\|u-w\|_2\le\left(\frac{48N\|K^{-1}\|_2}{h_c}\right)^{1/3}\|F(u)-F(w)\|_2^{1/3}.
\]
This is the claimed local inverse Hölder estimate. Conversely, along \(u=tv\), the linear term vanishes and
\[
F(tv)=\frac{h_c}{6}K(v_1^3,\ldots,v_N^3)^Tt^3+O_N(t^5).
\]
Its cubic coefficient is nonzero because \(K\) is invertible and \(v\ne0\). Consequently, any inverse estimate of exponent strictly above \(1/3\), compared with the input separation \(|t|\), fails for \(t\to0\).

**4. Exactly three critical-target inverse points immediately past the threshold.** Set \(h=(1+\varepsilon)/\lambda\). The local preimage equation for the fixed target \(p\) is
\[
F_h(u)=u-hK\sin u=0.
\]
Decompose \(u=tv+w\) with \(w\perp v\), and let \(Q=I-vv^T\). At \((t,w,\varepsilon)=(0,0,0)\), the derivative of \(QF_h\) with respect to \(w\) is \(Q(I-h_cK)|_{v^\perp}\), which is invertible because all other eigenvalues of \(K\) are strictly smaller than \(\lambda\). The analytic implicit-function theorem provides a unique local \(w=w(t,\varepsilon)\); it is odd in \(t\) and satisfies \(w=O_N(t^3)\), uniformly for small \(\varepsilon\).

The remaining scalar equation is
\[
\varphi(t,\varepsilon)=\langle v,F_h(tv+w(t,\varepsilon))\rangle
=-\varepsilon t+(1+\varepsilon)\beta_Nt^3+O_N(t^5),
\]
where
\[
\beta_N=\frac16\sum_i v_i^4=\frac1{4(N+1)}>0.
\]
(The quartic sum follows from elementary finite trigonometric sums, valid for all \(N\ge2\).) Oddness and analyticity make \(\varphi/t\) an analytic function of \(y=t^2\) and \(\varepsilon\), with value \(-\varepsilon\) at \(y=0\), and positive \(y\)-derivative \(\beta_N\) at \((0,0)\). The scalar implicit-function theorem gives a unique small positive root \(y(\varepsilon)=\varepsilon/\beta_N+O_N(\varepsilon^2)\) for every small positive \(\varepsilon\). Thus the local solutions are exactly \(t=0\) and \(t=\pm\sqrt{\varepsilon/\beta_N}+O_N(\varepsilon^{3/2})\). Inserting the displayed coordinates of \(v\) gives the two formulae in the statement.

There are no additional *global* preimages. Otherwise, a sequence \(h_j\downarrow h_c\) would admit inverse images of \(p\) staying outside a fixed neighborhood of \(p\); compactness would yield a limit that is a second inverse image of \(p\) under the already-proved homeomorphism \(G_{h_c}\), a contradiction. Shrinking \(\delta_N\) ensures all preimages lie in the implicit-function neighborhood. Finally \(DG_h(p)=I-hK\) has all multipliers in \((-1,1)\) whenever \(0<h<2/\lambda\); hence the noninvertible three-fiber regime begins while \(p\) is a hyperbolic sink. This completes the proof.

## Verification

The accompanying standalone file `verify.py` independently evaluates the exact path eigenvalues, the normalized top eigenvector, the quartic coefficient, the cubic critical displacement, and the predicted nonzero inverse branches. Run `python verify.py` with NumPy and SciPy. Representative finite sizes \(N=2,3,4,5,7,10,15\) and several positive excess-step values were tested. The program reports 66 finite diagnostics passed; those tests are *not* substitutes for the uniform analytical proof, the compactness argument, or the theorem for every finite \(N\).

## Relationship to prior work

Buescu, D’Aniello, and Oliveira [1], Theorem 4.1 and its optimality proof, establish the exact strict diffeomorphism interval \(0<h<1/\lambda_N\) for this map and show a derivative singularity for \(h\ge1/\lambda_N\). Their Corollary 5.4 gives the path spectrum and synchronizing sink, and their discussion treats the subcritical Morse–Smale regime. **Derivative singularity does not imply failure of global injectivity.** Parts 2–4 here establish that the singular endpoint retains invertibility as a *homeomorphism*, quantify its sharp cubic inverse regularity, and identify the three-to-one fixed-target fiber after crossing; these conclusions are not stated by the cited threshold and local-diffeomorphism argument. Earlier three-clock Lyapunov papers [2,3] address low-step synchronisation and stable basins rather than this exact singular-endpoint inverse-fiber transition; their complete implications have not been independently ruled out here.

## Limitations

This is a finite-dimensional, unit-weight *path* statement; no uniform large-\(N\) bifurcation radius or extension to other graphs is proved. The inverse Hölder estimate is local, not a global uniform bound. The exact preimage count is for the single natural target \(p\) and steps just above threshold, not every torus target or all supercritical steps. The theorem does not assert a global attractor classification after loss of invertibility. A broader theorem from classical monotone-map or singularity theory could imply some individual conclusions; bibliographic originality requires independent assessment.

## References

[1] J. Buescu, E. D’Aniello, H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1, first public 2026-10-07, Sections 3–5, Theorem 4.1, Corollary 5.4. https://arxiv.org/html/2610.10993v1

[2] J. Buescu, E. D’Aniello, H. M. Oliveira, *A Lyapunov function for a Synchronisation diffeomorphism of three clocks*, arXiv:2502.15371 (2025). https://arxiv.org/abs/2502.15371

[3] J. Buescu, H. M. Oliveira, *Lyapunov functions for Morse–Smale synchronisation diffeomorphisms*, arXiv:2503.13230 (2025). https://arxiv.org/abs/2503.13230
