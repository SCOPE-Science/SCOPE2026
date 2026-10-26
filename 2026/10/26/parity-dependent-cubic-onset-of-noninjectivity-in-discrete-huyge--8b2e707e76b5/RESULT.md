# Parity-dependent cubic onset of noninjectivity in discrete Huygens rings

## Finding

For every integer \(n\ge3\), let \(K\) denote the combinatorial Laplacian of the unweighted cycle \(C_n\), and consider the phase-difference map
\[
 F_h(z)=z+hK\sin z\pmod{2\pi},\quad z\in\mathcal Z_n:=\{z\in(\mathbb R/2\pi\mathbb Z)^n:\sum_i z_i=0\pmod{2\pi}\}.
\]
Write \(\Lambda_n=4\) for even \(n\) and \(\Lambda_n=2+2\cos(\pi/n)\) for odd \(n\). The known diffeomorphism interval \(0<h<1/\Lambda_n\) is sharp **for every cycle length, including odd lengths**: at \(h_*=1/\Lambda_n\), the exact singular locus of the derivative on the tangent hyperplane comprises one point if \(n\) is even, namely \((\pi,\ldots,\pi)\), and comprises \(n\) points if \(n\) is odd, namely the cyclic placements of one zero among \(n-1\) entries equal to \(\pi\). Every such singularity has nullity exactly one.

For each of these points \(z_*\), put \(\mu=h\Lambda_n-1\). There exists \(\epsilon_n>0\) such that whenever \(0<\mu<\epsilon_n\), the target \(z_*\) has at least three distinct preimages under \(F_h\), all tending to \(z_*\) as \(\mu\downarrow0\). With an explicitly normalized critical unit eigenvector \(w\) and Euclidean scalar coordinate \(t=\langle z-z_*,w\rangle\), the two nontrivial preimages have
\[
 t_\pm=\begin{cases}\pm\sqrt{6n\mu}+O_n(\mu^{3/2}),&n\text{ even},\\ \pm\sqrt{4n\mu}+O_n(\mu^{3/2}),&n\text{ odd}.\end{cases}
\]
In particular, immediately above \(h_*\), the map is not injective. The statement concerns the reduced edge-difference torus and does not assert noninjectivity for every arbitrarily large \(h\).

## Assumptions and scope

Indices belong to \(\mathbb Z/n\mathbb Z\); the cycle has unit weights and exactly two distinct neighbors at each vertex, with \(n\ge3\). Set \(E=\{u\in\mathbb R^n:\sum_i u_i=0\}\), \(K_{ii}=2\), and \(K_{i,i\pm1}=-1\), adding entries in the case \(n=3\) (whose two neighbors are still distinct). The map has natural local lifts to \(E\) around each \(z_*\), because \(\sum_iK_{ij}=0\). All differentiability and nullity claims concern its \((n-1)\)-dimensional tangent space \(E\).

Normalize \(w_i=(-1)^i/\sqrt n\) when \(n\) is even. When \(n\) is odd and the zero occurs at position \(j\), set \(k=(n-1)/2\) and
\[
 w_i=\sqrt{2/n}\sin\bigl(2\pi k(i-j)/n\bigr).
\]
These real vectors have norm one, sum zero and obey \(Kw=\Lambda_n w\). Their signs can be reversed without changing the claim.

## Proof

**1. Classification of the first singular set.** Let \(K_0=K|_E\), which is symmetric positive definite. At a configuration \(z\), write \(D(z)=\operatorname{diag}(\cos z_i)\). The derivative on \(E\) is
\[
 J_h(z)=I_E+hK D(z)|_E.
\]
The operator \(-KD(z)|_E\) is similar, using the positive square root of \(K_0\), to the symmetric operator \(-K_0^{1/2}D(z)K_0^{1/2}|_E\). Since \(-D(z)\preceq I\), for each \(u\in E\),
\[
 \langle u,-K_0^{1/2}D(z)K_0^{1/2}u\rangle\le\langle u,K_0u\rangle\le\Lambda_n\|u\|^2.
\]
Equality for a nonzero \(u\) forces both \(u\) to belong to the top eigenspace of \(K_0\) and \(v=K_0^{1/2}u\) to have \(v_i=0\) at every position where \(\cos z_i>-1\). Consequently, \(J_{h_*}(z)\) can be singular only if a nonzero highest-frequency eigenvector of \(K\) is supported on coordinates where \(z_i=\pi\pmod{2\pi}\); conversely this condition produces a null vector.

When \(n\) is even, the top eigenspace is spanned by the alternating vector with no zero coordinates, so \(z_i=\pi\) for all \(i\). Since \(n\pi\equiv0\pmod{2\pi}\), this configuration belongs to \(\mathcal Z_n\) and has a one-dimensional kernel.

When \(n\) is odd, the top eigenspace is the real span of the sine and cosine waves at frequency \(k=(n-1)/2\). Any nonzero vector in this plane has at most one zero coordinate: zeros at distinct positions \(i,j\) would require \(\sin(2\pi k(i-j)/n)=0\), hence \(2k(i-j)\equiv0\pmod n\), impossible since \(\gcd(2k,n)=1\). Thus at most one coordinate of \(z\) can differ from \(\pi\). With no exception the phase sum is \(\pi\pmod{2\pi}\) and violates closure; with one exception, closure forces that entry to equal zero. For each of the \(n\) placements, the displayed normalized sine vector vanishes at exactly that exceptional coordinate, yielding a kernel. Requiring vanishing at this coordinate cuts the two-dimensional top eigenspace to dimension one. Hence the list is complete and every nullity is exactly one.

**2. Odd analytic reduction.** At any listed \(z_*\), write \(D_*=\operatorname{diag}(\cos (z_*)_i)\), so \(\sin z_*=0\), \(D_*w=-w\), and \(Kw=\Lambda_n w\). The map's local displacement from the target is
\[
 f_h(u)=F_h(z_*+u)-z_*=u+hKD_*\sin u,
\]
where the equality uses a sufficiently small consistent local lift and componentwise sine. It is odd real analytic. Moreover its linearization \(J_h=I+hKD_*\) satisfies \(J_hw=J_h^\top w=(1-h\Lambda_n)w\). Thus the splitting \(E=\mathbb Rw\oplus W\), \(W=E\cap w^\perp\), is invariant under \(J_h\). The restriction \(J_{h_*}|_W\) is invertible because the full nullity is one.

Let \(Q:E\to W\) be the orthogonal projection. By the analytic implicit-function theorem, for \(h\) near \(h_*\), all solutions of the transverse equation \(Q f_h(tw+y)=0\) near zero are given by a unique analytic odd function \(y=y(t,h)\in W\). The vanishing transverse linear forcing and oddness imply \(y(t,h)=O_n(t^3)\), uniformly for nearby \(h\).

**3. Cubic scalar equation and branches.** The remaining scalar equation is \(g_h(t)=\langle w,f_h(tw+y(t,h))\rangle=0\). Taylor expansion of sine and the left-eigenvector identity give
\[
 g_h(t)=(1-h\Lambda_n)t+\frac{h\Lambda_n}{6}\left(\sum_iw_i^4\right)t^3+O_n(t^5).
\]
Terms linear in \(y\) cancel because \(w^\top J_h|_W=0\), and \(y=O_n(t^3)\) contributes only to order five and higher. The fourth-power sum is \(1/n\) in the even case. In the odd case, since \(\gcd(k,n)=1\) and \(n\ge3\) is odd, summing the identity \(\sin^4 x=(3-4\cos2x+\cos4x)/8\) over the residues gives \(\sum_iw_i^4=3/(2n)\).

With \(\mu=h\Lambda_n-1\), obtain
\[
 g_h(t)=t\left[-\mu+(1+\mu)c_n t^2+O_n(t^4)\right],\quad
 c_n=\begin{cases}1/(6n),&n\text{ even},\\1/(4n),&n\text{ odd}.\end{cases}
\]
Because \(g_h\) is odd analytic, its bracket is analytic in \(\rho=t^2\) and \(\mu\). At \((\rho,\mu)=(0,0)\), its derivative with respect to \(\rho\) equals \(c_n>0\), so the implicit-function theorem gives \(\rho(\mu)=\mu/c_n+O_n(\mu^2)>0\) for \(\mu>0\) sufficiently small. The three roots \(t=0\) and \(t=\pm\sqrt{\rho(\mu)}\) give three distinct solutions \(u=tw+y(t,h)\) to \(f_h(u)=0\). Since \(\|y\|=O_n(t^3)\), the nontrivial branch amplitudes have the asserted square-root laws, and all three preimages converge to \(z_*\). This proves the first local onset of noninjectivity for both parities. \(\square\)

## Verification

The standalone code `checks/verify.py` computes the cycle matrices, verifies the proposed critical eigenvectors and nullities, and numerically solves the **full** transverse implicit equations for \(n=3,\ldots,15\) at \(\mu=0.005\) and \(\mu=0.015\). Its final output is `VERIFY_OK`. The computation checks 26 supercritical parameters across thirteen cycle sizes, but the all-\(n\) theorem follows from the analytic proof, not this finite test. To run: install the listed NumPy/SciPy requirements, then execute `python checks/verify.py`.

## Relationship to prior work

Buescu and Oliveira's 2026 ring paper establishes the map, cycle spectrum, and global diffeomorphism for \(0<h<1/\Lambda_n\), and explicitly notes sharpness of both spectral thresholds for **even** cycles. It does not identify the exact singular configurations for odd cycles or establish the cubic supercritical inverse branches. Buescu, D'Aniello and Oliveira's 2026 network paper proves a more general sufficient invertibility interval and optimality for sinusoidal **trees**, whose edge phases lack the odd-cycle closure obstruction. The present result pinpoints the first singular locus for all rings and resolves the odd parity sharpness with a concrete branch-count mechanism. Classical local cubic singularity theory explains the analytic normal-form shape abstractly; the substantive content here is its exact occurrence, number, normalization, and arithmetic parity dependence for these closed-loop maps.

## Limitations

There is no assertion that these are the only singularities at later interaction strengths; none that the map ceases to be injective at the exact boundary \(h=h_*\); and none that exactly three global preimages exist for the displayed target. The theorem concerns the quotient system, unweighted sine coupling and \(n\ge3\); the parity classification need not survive edge-weight perturbations. Bibliographic priority for specialized cycle-oscillator inverse-map singularities remains subject to independent historical review. The self-review is not an independent audit.

## References

1. J. Buescu and H. M. Oliveira, *Almost-global convergence to twisted states in discrete Huygens rings*, arXiv:2610.19953v1 (first publicly posted 2026-10-14), Sections 2 and 4, in particular Theorem 2.1 and the even-cycle sharpness statement.
2. J. Buescu, E. D'Aniello and H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1 (2026), Theorem 3.2 and Corollary 5.3 (tree optimality).
