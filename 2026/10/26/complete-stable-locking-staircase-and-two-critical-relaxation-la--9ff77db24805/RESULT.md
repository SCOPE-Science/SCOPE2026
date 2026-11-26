# Exact critical relaxation laws for the alternating Kuramoto ring

## Finding
Fix an integer \(m\ge3\), detuning \(a>0\) and equal per-neighbor coupling \(K>0\) on the labelled \(2m\)-cycle:
\[
\dot\phi_j=(-1)^j a+K\big[\sin(\phi_{j+1}-\phi_j)+\sin(\phi_{j-1}-\phi_j)\big],\qquad j\in\mathbb Z/(2m\mathbb Z).
\]
Here a stable locked state is an equilibrium with one simple rotation eigenvalue zero and all other Jacobian eigenvalues negative. Its spectral relaxation gap \(\gamma_q(K)\) is the absolute value of the largest strictly negative eigenvalue. For each allowed winding \(q\) with \(2|q|<m\), the stable branch exists for \(K>K_q=a/[1+\cos(2\pi q/m)]\). With \(\varepsilon=K/K_q-1\downarrow0\), its full-space gap has the sharp laws
\[
\gamma_0(K)=\sqrt2\,a[1-\cos(\pi/m)]\sqrt{\varepsilon}+O(\varepsilon^{3/2}),
\]
\[
\gamma_q(K)=\frac{a[1-\cos(2\pi/m)]}{\sin(2\pi |q|/m)}\,\varepsilon+O(\varepsilon^2),\qquad 0<2|q|<m.
\]
These are paired critical slowing-down laws with different exponents in the same ring, depending on winding. At the central threshold both families of conductances vanish; at a noncentral threshold a positive dimer conductance survives and only the links between dimers vanish. The gap is the slowest transverse rate in the **full** phase space, not a relaxation eigenvalue of a symmetry-reduced branch equation.

For the exact finite-coupling formula put \(\vartheta=2\pi q/m\) and
\[
d=2\arcsin\!\left(\frac{a}{2K\cos(\vartheta/2)}\right),\qquad
\alpha=\frac{\vartheta+d}{2},\qquad \beta=\frac{\vartheta-d}{2},\qquad
u=K\cos\alpha,\quad v=K\cos\beta.
\]
The even edges have increment \(\beta\) and odd edges increment \(\alpha\), where edge \(j\) runs from \(j\) to \(j+1\). The full Jacobian spectrum, with multiplicities, is
\[
\lambda_r^\pm=-(u+v)\pm\sqrt{u^2+v^2+2uv\cos(2\pi r/m)},\qquad 0\le r<m.
\]
In particular, \(\gamma_q=u+v-\sqrt{u^2+v^2+2uv\cos(2\pi/m)}\). For context, the complete stable branch count is \(\sum_{q\in\mathbb Z:\,2|q|<m}{\bf1}\{K>K_q\}\), one class per winding and no others. It approaches \(m-1\) for even \(m\) and \(m\) for odd \(m\). The known general signed-cycle stability criterion, combined with the alternating sine flows, suffices to obtain the classification. The claimed contribution is the winding-dependent full relaxation calculation and paired sharp laws, not the criterion, winding construction, or threshold parameters in isolation.

## Assumptions and scope
The natural frequencies sum to zero, so a locked state has common frequency zero. Only simultaneous phase rotation is quotiented out; the vertices are labelled. Winding is the sum of the principal edge increments divided by \(2\pi\); it is used for stable states after every edge is shown acute. Threshold points with extra zero modes are not strictly linearly stable. The gap expansions are for fixed \(m,q,a\) and do not assert a uniform joint large-ring limit.

## Proof

**1. Which equilibria are stable?** With \(x_j=\phi_{j+1}-\phi_j\), equilibrium gives \(\sin x_j-\sin x_{j-1}=-(-1)^j a/K\). Thus the sines are constant on each parity, with the odd value exceeding the even value by \(a/K\). The Jacobian is minus the signed weighted cycle Laplacian with conductances \(w_j=K\cos x_j\). Strict stability is strict positivity of \(Q(y)=\sum_j w_j y_j^2\) on nonzero real edge differences satisfying \(\sum_j y_j=0\); this is the space of all vertex variations modulo rotation. If at least two conductances are negative, take differences \(+1,-1\) on two such edges and zero elsewhere to get \(Q<0\). One negative and one zero edge give the same conclusion. If there is exactly one negative conductance \(-c\) and every other conductance is positive, each of the other \(m-1\) edges of its parity has conductance \(+c\) because it shares its sine. Set the edge difference to 1 on the negative edge, to \(-1/(m-1)\) on those same-parity edges, and to zero on the others. This gives \(Q=-c+c/(m-1)<0\). Equivalently the prior reciprocal-sum criterion for a single negative edge fails: the same-parity edges alone give a sum \((m-2)/c>0\). If all conductances are nonnegative and one is zero, all edges of that parity have zero conductance, and the positive-edge graph is disconnected, with additional zero eigenvalues. All-positive conductances conversely give the required strict stability on the connected cycle.

**2. Acute branches and thresholds.** For positive conductances the sine fixes the acute increment uniquely. Write the odd increment as \(\alpha\) and even increment as \(\beta\), each in \((-\pi/2,\pi/2)\). Winding imposes \(m(\alpha+\beta)=2\pi q\), i.e. \(\alpha+\beta=\vartheta\) with \(2|q|<m\). Their difference \(d=\alpha-\beta\) lies in \((0,\pi-|\vartheta|)\), and
\[
\frac{a}{K}=\sin\alpha-\sin\beta=2\cos(\vartheta/2)\sin(d/2).
\]
The right side increases strictly in this interval from 0 to \(1+\cos\vartheta\), excluding its endpoints. This establishes the strict threshold \(K_q\), uniqueness for each winding, and the displayed increments. Closure allows them to be integrated to labelled phases uniquely up to rotation. At \(K=K_q\), the endpoint \(d=\pi-|\vartheta|\) makes at least one parity of conductances vanish; the criterion in Step 1 excludes strict stability there. The count follows by ranging over \(q\), with thresholds increasing in \(|q|\).

**3. Fourier spectrum and gap.** Use an \(m\)-cell Fourier decomposition of the weighted Jacobian with alternating conductances \(u,v>0\). At Fourier phase \(2\pi r/m\) the diagonal of its two-by-two block is \(-(u+v)\), with conjugate off-diagonal entries \(u+ve^{\pm2\pi ir/m}\) (the ordering of the two conductances can be interchanged). Its eigenvalues give the stated two bands. The only zero is \(\lambda_0^+\). The largest nonzero-\(r\) plus eigenvalue occurs at \(r=1,m-1\), and every minus mode is \(\le -(u+v)\). The plus eigenvalue at \(r=1\) is strictly above \(-(u+v)\) for \(m\ge3\) and positive \(u,v\). This identifies the full gap.

**4. Sharp gap asymptotics.** For \(q=0\) the two conductances coincide and equal \(\sqrt{K^2-a^2/4}\), so
\[
\gamma_0(K)=2\sqrt{K^2-a^2/4}[1-\cos(\pi/m)].
\]
Expanding at \(K=(a/2)(1+\varepsilon)\) gives the first law. For \(q\ne0\), put \(t=2\pi|q|/m\in(0,\pi)\) and \(d=\pi-t-\eta\). At the threshold one edge parity reaches \(|x_j|=\pi/2\) and the other retains conductance \(K_q\sin t>0\). Interchanging the two parities and negating the increments preserves the gap, so take \(q>0\) for the expansion. Then \(\alpha=\pi/2-\eta/2\) and \(\beta=t-\pi/2+\eta/2\). The sine equation becomes \(a/K=1+\cos t-(\sin t)\eta/2+O(\eta^2)\), so \(\eta=2(1+\cos t)\varepsilon/\sin t+O(\varepsilon^2)\). The vanishing conductance is \(K\sin(\eta/2)=a\varepsilon/\sin t+O(\varepsilon^2)\); the other is bounded away from zero. Taylor expansion of the full gap at a small conductance \(w\) with the other bounded away from zero gives \(w[1-\cos(2\pi/m)]+O(w^2)\). This proves the second law with its coefficient and remainder.

## Verification
The accompanying `verify.py` constructs the branch configurations, independently assembles the vector field and full numerical Jacobian, and compares with the two-band eigenvalues. The recorded run had 630 branch residual/spectrum cases for \(3\le m\le16\) and gap-scaling comparisons at six ring sizes. Its extra path-resistance samples illustrate the instability inequality but are not needed for the exact witness in Step 1. The finite tests do not establish the all-parameter classification or any asymptotic limit.

## Relationship to prior work
Ochab and Góra [1, §4] give a cycle winding method, and Roy and Lahiri [2, §§III–IV] treat the general signed ring Jacobian and mixed angle branches. Tilles, Cerdeira and Ferreira [3, §IV, Eqs. (32)–(47)] analyze the same alternating frequencies and give the central onset and, for ten oscillators with unit detuning, exchanges near \(0.764\) and \(5.236\), consistent with these thresholds. Their symmetry-reduced stability analysis is distinguished from stability in the full phase space. The specular condition in their §V is a different symmetry and is satisfied by strict adjacent alternation only when \(m\) is odd; their §V equations are not the all-size alternating-frequency reference. Tilles, Ferreira and Cerdeira [4] study general frequency choices and branch stability. Bronski, DeVille and Ferguson [5, Theorem 2.6 and Eq. (4.2)] give the general cycle stability criterion for nonzero conductances; they allow one negative conductance if the sum of reciprocals is negative. Equal within-parity magnitudes in the alternating problem exclude that case directly, so the stability exclusion and resulting count are included as context and not claimed as independent novelties. The period-two Fourier diagonalization is standard. The paired critical gap laws here evaluate the slowest rate among all transverse modes and identify its exact winding-dependent coefficient, not just the type of reduced branch crossing.

## Limitations
This result concerns strict linear stability and full transverse relaxation for exactly alternating detunings with homogeneous positive coupling. It does not classify unstable equilibria, basins, or nonlinear stability at the degenerate thresholds. No historical priority is asserted beyond bounded comparison with the cited literature.

## References
1. J. Ochab and P. F. Góra, *Synchronization of Coupled Oscillators in a Local One-Dimensional Kuramoto Model*, [arXiv:0909.0043](https://arxiv.org/abs/0909.0043), §4.
2. T. K. Roy and A. Lahiri, *Synchronized oscillations on a Kuramoto ring and their entrainment under periodic driving*, [arXiv:1103.4966](https://arxiv.org/abs/1103.4966), §§III–IV.
3. P. F. C. Tilles, H. A. Cerdeira and F. F. Ferreira, *Local attractors, degeneracy and analyticity: symmetry effects on the locally coupled Kuramoto model*, [arXiv:1108.3271](https://arxiv.org/abs/1108.3271), §§IV–V.
4. P. F. C. Tilles, F. F. Ferreira and H. A. Cerdeira, *Multistable behavior above synchronization in a locally coupled Kuramoto model*, [arXiv:1102.3890](https://arxiv.org/abs/1102.3890).
5. J. C. Bronski, L. DeVille and T. Ferguson, *Graph Homology and Stability of Coupled Oscillator Networks*, [arXiv:1508.01507](https://arxiv.org/abs/1508.01507), Theorem 2.6 and Eq. (4.2).
