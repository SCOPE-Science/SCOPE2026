# A sharp period-doubling branch and optimally damped transverse modes in even Huygens rings

## Finding

Consider an even ring of repulsively coupled discrete Huygens oscillators. As \(h\) increases through \(1/2\), phase opposition becomes unstable and a nonstationary alternating two-cycle is created. For every even \(n\ge4\), this two-cycle is locally asymptotically attracting modulo global phase exactly for \(1/2<h\le\pi/4\) among the parameters where it exists. It is hyperbolically attracting for \(1/2<h<\pi/4\) and nonhyperbolically attracting at \(h=\pi/4\). Its two-step Floquet spectrum and the unique minimizer of the linearized two-step spectral radius are explicit.

More precisely, put \(s_j=(-1)^j\), \(j=0,\ldots,n-1\). For every \(h>1/2\), exactly one \(a_h\in(0,\pi)\) solves
\[
 a_h=2h\sin a_h.
\]
The two edge configurations \(z^\pm=\pi\mathbf1\pm a_hs\) form a genuine two-cycle under the reduced map. Its two-step multipliers are
\[
 m_j(h)=\bigl(1-h\cos(a_h)[2-2\cos(2\pi j/n)]\bigr)^2,
 \qquad j=1,\ldots,n-1.
\]
All have modulus strictly less than one exactly for \(1/2<h<\pi/4\), are exactly one at \(h=\pi/4\), and exceed one for \(h>\pi/4\). These classifications concern the full \((n-1)\)-dimensional common-phase quotient, not merely the alternating invariant circle.

Write \(b_n=\sin^2(\pi/n)\). Within the attracting range (including its neutral endpoint), the minimum possible two-step transverse spectral radius is
\[
 \boxed{\rho_n^*=\left(\frac{1-b_n}{1+b_n}\right)^2.}
\]
It is attained at exactly one \(h_n^*\in(1/2,\pi/4)\), where
\[
 a_n^*\cot a_n^*=\frac1{1+b_n}, \qquad h_n^*=\frac{a_n^*}{2\sin a_n^*}.
\]
At the bifurcation the orbit is locally unique up to exchanging its two points, and its amplitude follows \(a_h=\sqrt{12(h-1/2)}[1+O(h-1/2)]\). For even \(n\to\infty\),
\[
 h_n^*=\frac12+\frac{\pi^2}{4n^2}+O(n^{-4}),\qquad
 \rho_n^*=1-\frac{4\pi^2}{n^2}+O(n^{-4}).
\]

## Assumptions and scope

Indices are modulo an even integer \(n\ge4\), and \(h>0\). The vertex phases lie in \(\mathbb T^n=(\mathbb R/2\pi\mathbb Z)^n\). The map is
\[
 F_h(\theta)_j=\theta_j+h\bigl[\sin(\theta_j-\theta_{j-1})+\sin(\theta_j-\theta_{j+1})\bigr]\pmod{2\pi}.
\]
It is equivariant under common-phase shifts. The actual hyperbolicity statement is on the quotient \(\mathbb T^n/\mathbb T\) by this symmetry; the full torus retains the unit common-phase multiplier. With \(B\) the incidence matrix of the simple cycle, the edge vector \(z=B^T\theta\) belongs to \(\mathcal Z=\{z\in\mathbb T^n:\sum_jz_j\equiv0\pmod{2\pi}\}\), and the reduced map is
\[
 \overline F_h(z)=z+hL\sin z\pmod{2\pi},\qquad
 (Lz)_j=2z_j-z_{j-1}-z_{j+1}.
\]
The tangent space \(E=\mathbf1^\perp\) has dimension \(n-1\). The alternating vector \(s\) is in \(E\). The statements about locally unique period-two configurations refer to a sufficiently small neighborhood of \(z=\pi\mathbf1\) in \(\mathcal Z\), with \(h\) sufficiently close to \(1/2\), and do not purport to classify all remote periodic orbits.

## Proof

**1. Exact alternating branch.** Because \(n\) is even, \(Ls=4s\) and \(s\in E\). For \(z=\pi\mathbf1+xs\), the componentwise identity \(\sin(\pi+xs_j)=-s_j\sin x\) gives
\[
 \overline F_h(\pi\mathbf1+xs)=\pi\mathbf1+[x-4h\sin x]s.
\]
Hence the alternating circle is invariant and carries the odd scalar map \(g_h(x)=x-4h\sin x\pmod{2\pi}\). A symmetric two-cycle \(a\leftrightarrow-a\) satisfies \(g_h(a)=-a\), equivalently \(a=2h\sin a\). The function \(H(a)=a/(2\sin a)\) increases strictly from \(1/2\) to infinity for \(a\in(0,\pi)\), since \(\sin a-a\cos a>0\) there. Thus each \(h>1/2\) determines exactly one \(a_h\in(0,\pi)\). The two phases are distinct modulo \(2\pi\). In vertex coordinates one may take the two states \(\theta_{2k}=0,\ \theta_{2k+1}=\pi+a_h\) and \(\theta'_{2k}=a_h,\ \theta'_{2k+1}=\pi\). A direct substitution shows that one is sent to the other and back, with no net common-phase displacement.

**2. Full quotient Floquet spectrum.** At either point of the cycle, \(\cos z_j=-\cos a_h\) independently of \(j\). Consequently
\[
 D\overline F_h\bigm|_{E}=I-h\cos a_h L\bigm|_E
\]
at both points. The two-step derivative is its square. The nonzero cycle-Laplacian eigenvalues are \(\lambda_j=2-2\cos(2\pi j/n)\), \(1\le j<n\), with smallest \(\lambda_{\min}=4\sin^2(\pi/n)>0\) and largest \(\lambda_{\max}=4\), the latter simple for even \(n\). These give the asserted exact multipliers. Define \(t=h\cos a_h=(a_h/2)\cot a_h\). As \(h\) moves from \(1/2\) to \(\pi/4\), \(a_h\) moves from zero to \(\pi/2\), and \(t\) moves strictly from \(1/2\) down to zero. Thus, in the open interval, \(0<t<1/2\), whence \(-1<1-t\lambda_j<1\) for every nonzero eigenvalue. At \(h=\pi/4\), \(a_h=\pi/2\) and \(t=0\), giving the identity derivative at each cycle point. For \(h>\pi/4\), \(a_h>\pi/2\), so \(t<0\) and every quotient multiplier \((1-t\lambda_j)^2\) exceeds one. This establishes the exact sink/nonhyperbolic/source trichotomy.

**Nonlinear attraction at the upper endpoint.** Set \(h=\pi/4\), and use mean-zero displacements \(u\in E\) centered at the successive cycle points. Write \(\odot\) for componentwise multiplication. The maps on displacements from \(z^+\) to \(z^-\) and back are respectively \(u\mapsto u+Q(u)\) and \(u\mapsto u-Q(u)\), where
\[
Q(u)=hL\bigl(s\odot(\mathbf1-\cos u)\bigr),\qquad
Q_2(u)=\frac h2 L(s\odot u\odot u).
\]
Here \(Q_2\) is the quadratic part of \(Q\). The return at \(z^+\) is \(T(u)=u+Q(u)-Q(u+Q(u))=u-DQ_2(u)Q_2(u)+O(\|u\|^4)\). The return at \(z^-\) has the same cubic part. With \(L_E^{-1}\) the inverse of \(L\) on \(E\), put \(W(u)=u^{\mathsf T}L_E^{-1}u/2\) and \(w=s\odot u\odot u\). Then
\[
W(T(u))-W(u)=-\frac{h^2}{2}\,w^{\mathsf T}Lw+O(\|u\|^5).
\]
Indeed \(DQ_2(u)v=hL(s\odot u\odot v)\), and \(u^{\mathsf T}L_E^{-1}L=u^{\mathsf T}\) for \(u\in E\). The kernel of \(L\) consists of the constants. A constant \(w\) must be zero since its entries have alternating weak signs; this forces \(u=0\). By homogeneity and compactness on the unit sphere of \(E\), \(w^{\mathsf T}Lw\ge c_n\|u\|^4\) for some \(c_n>0\). Thus a small sublevel set of \(W\) traps the return iterates and \(W\) decreases by at least a positive constant times \(\|u\|^4\) at each nonzero point. Summing this bound shows \(u\to0\). This proves local asymptotic attraction in the full quotient despite unit multipliers.

**3. Sharp spectral optimum.** The neutral endpoint has \(\rho_n=1\), so cannot minimize. In the hyperbolically attracting interval, \(\rho_n(t)=\max_{1\le j<n}(1-t\lambda_j)^2\). Because \(\lambda\mapsto|1-t\lambda|\) is convex on the interval \([\lambda_{\min},4]\) and both endpoints occur in the spectrum,
\[
 \rho_n(t)=\max\{(1-t\lambda_{\min})^2,(1-4t)^2\}.
\]
The unique minimizer over \(0<t<1/2\) equalizes the endpoint absolute multipliers, namely \(1-t\lambda_{\min}=4t-1\). Thus \(t_*=2/(\lambda_{\min}+4)=1/[2(1+b_n)]\) and \(\rho_n^*=[(4-\lambda_{\min})/(4+\lambda_{\min})]^2=[(1-b_n)/(1+b_n)]^2\). Uniqueness follows also from the strict monotonicity of \(t=(a/2)\cot a\) on \((0,\pi/2)\), because \(\sin a\cos a<a\). The equation for \(a_n^*\) and its unique \(h_n^*\) follow.

**4. Local exclusivity of the bifurcating two-cycle.** Work in the local tangent coordinates \(u\in E\) around \(z_0=\pi\mathbf1\). Write \(u=xs+w\), with \(w\perp s\) in \(E\). At \(h_0=1/2\), the linearization of \(\overline F_{h_0}\) has one eigenvalue \(-1\), on the line \(\mathbb Rs\), and every other eigenvalue strictly between \(-1\) and \(1\). Therefore the derivative with respect to \(w\) of the \(w\)-component of \(\overline F_h^2(z_0+xs+w)-(z_0+xs+w)\) is invertible at \((h_0,x,w)=(1/2,0,0)\). The analytic implicit-function theorem gives a unique small solution \(w=w(h,x)\) to that component. Since the line \(w=0\) is exactly invariant under the map, \(w=0\) already solves the projected equation for all small \((h,x)\), and uniqueness forces \(w(h,x)\equiv0\). Thus every local point of period dividing two lies on the alternating line. On it,
\[
 g_h(x)= (1-4h)x+\frac{2h}{3}x^3+O(x^5),
\]
and the even analytic quotient \([g_h(g_h(x))-x]/x\), written as a function of \(y=x^2\), has the expansion
\[
 \frac{g_h(g_h(x))-x}{x}=8(h-1/2)-\frac23 y+O((h-1/2)^2+|h-1/2|y+y^2).
\]
Another application of the implicit-function theorem gives exactly one small analytic squared-amplitude branch \(y=12(h-1/2)+O((h-1/2)^2)\). It is positive exactly for \(h>1/2\) sufficiently close to the threshold, and its two square roots form one prime two-cycle; for \(h<1/2\) there are none nearby. These roots coincide with the already explicit alternating branch, proving local uniqueness up to cyclic time shift.

**5. Large-ring and onset expansions.** Expanding \(H(a)=\tfrac12+a^2/12+O(a^4)\) gives \(a_h=\sqrt{12(h-1/2)}[1+O(h-1/2)]\). With \(b_n=\sin^2(\pi/n)=\pi^2/n^2+O(n^{-4})\), the identity \(a_n^*\cot a_n^*=1/(1+b_n)\) and \(a\cot a=1-a^2/3+O(a^4)\) give \((a_n^*)^2=3b_n+O(b_n^2)\). Therefore \(h_n^*=1/2+b_n/4+O(b_n^2)\) and \(\rho_n^*=1-4b_n+O(b_n^2)\), which are the asserted asymptotics.

## Verification

The accompanying standalone `checker.py` evaluates the alternating two-step return in the original vertex dynamics at four interaction strengths, for each of five even ring sizes. It computes the complete nontrivial Laplacian spectrum and compares the direct Floquet spectral radius to the closed optimum, including perturbations on either side of each optimum. Its output in `checker_output.txt` records the tested sizes, numerical optima, and the limitation that finite calculations do not establish an infinite-family theorem. The proof above supplies that theorem and the near-flip uniqueness argument.

## Relationship to prior work

Buescu and Oliveira [1] analyze exactly this unweighted repulsive discrete ring and prove almost-global convergence to attracting twisted fixed points for \(0<h<2/\Lambda_n\), where \(\Lambda_n=4\) on an even cycle. Their paper identifies the \(-1\) multiplier at \(h=1/2\) and expressly leaves larger-strength bifurcations untreated. The weighted bipartite analysis in [4] does cover the local birth, uniqueness and attraction just above the flip, as well as nonlinear relaxation at the fixed-point threshold. Its sign convention is conjugate to the repulsive one by shifting one color class by \(\pi\).

Buescu, D'Aniello, and Oliveira [2] prove a Morse–Smale theorem in a smaller, diffeomorphic interval. Zhai, Xiao, and Zheng [3] describe qualitative period doubling and synchronization loss in discrete circle-map networks. The balanced all-to-all two-cluster reduction in [5] has the same scalar branch equation after rescaling, but its transverse modes are different. The later biregular-network treatment [6] specializes exactly to the cycle's Floquet spectrum and minimax optimizer. It proves a parabolic return on the two-colour subsystem at the upper endpoint and leaves transverse nonlinear attraction unresolved. The additional endpoint conclusion here is attraction in **all** common-phase quotient directions, proved using the quartic Lyapunov decrease rather than the scalar return or unit Floquet multipliers. The remaining formulas give a self-contained ring calculation; no separate priority claim is made for overlapping results.

## Limitations

All attraction and repulsion assertions are **local in the full common-phase quotient**. The unreduced phase torus has a neutral common-phase direction. No claim is made about global basins, absence of distant periodic orbits, persistence under heterogeneous coupling, or the dynamics of odd rings. Local uniqueness of the prime two-cycle is proved only sufficiently near \(h=1/2\) and phase opposition. The reported spectral optimum optimizes the linearized two-step convergence rate for this specific orbit; it is not an optimizer of global convergence or physical transient time. Priority beyond the inspected literature is not fully resolved.

## References

[1] J. Buescu and H. M. Oliveira, *Almost-global convergence to twisted states in discrete Huygens rings*, arXiv:2610.19953v1, first publicly posted 14 October 2026. https://arxiv.org/html/2610.19953

[2] J. Buescu, E. D'Aniello and H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1, first publicly posted 7 October 2026. https://arxiv.org/pdf/2610.10993

[3] Y. Zhai, J. Xiao and Z. Zheng, *Synchronization–desynchronization transitions in networks of circle maps with sinusoidal coupling*, Chinese Physics B 32 (2023), 060505, doi:10.1088/1674-1056/acc062. https://www.cpsjournals.cn/en/article/doi/10.1088/1674-1056/acc062

[4] *Sharp two-cycle threshold and critical decay on weighted bipartite phase networks*. https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-sharp-two-cycle-threshold-and-critical-decay-on-weighted-biparti--690fe2013b5e

[5] *A sharp cluster-size threshold for alternating two-cycles of the discrete Kuramoto map*. https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-a-sharp-cluster-size-threshold-for-alternating-two-cycles-of-the--da59163e9d68

[6] *Universal stable window and optimal decay of alternating cycles in biregular Huygens networks*. https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-universal-stable-window-and-optimal-decay-of-alternating-cycles--bd570f026995
