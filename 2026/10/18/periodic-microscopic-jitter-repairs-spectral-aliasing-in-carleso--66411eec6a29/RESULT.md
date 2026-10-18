# Periodic microscopic jitter repairs spectral aliasing in Carleson orbit frames

## Finding

Let \(\mathcal Z=\{z_j:j\geq0\}\) be a sequence of distinct nonzero points of the open unit disk, avoiding the principal-logarithm branch cut, contained in a Stolz region at \(1\), and satisfying the Carleson interpolation condition. In particular, \(z_j\to1\). On \(\ell^2(\mathbb N_0)\), define \(De_j=z_je_j\) and the canonical generating vector \(g=(\sqrt{1-|z_j|^2})_{j\ge0}\). For real \(t\ge0\), powers are \(D^te_j=\exp(t\operatorname{Log}z_j)e_j\).

Fix **any** \(r>0\). For an integer \(p\ge2\) and offsets \(0\le\tau_a<r\) indexed by \(0\le a<p\), sample at
\[
t_{pk+a}=r(pk+a)+\tau_a\qquad (k\ge0,\ 0\le a<p).
\]
Set \(\xi_j=z_j^{rp}\) and \(G_\xi=\{j:\xi_j=\xi\}\). Each \(G_\xi\) is finite, and only finitely many have more than one element. **Exact criterion:** \(\{D^{t_n}g\}_{n\ge0}\) is a frame if and only if, for every distinct \(\xi\), the finite matrix
\[
M_\xi=\bigl(z_j^{ra+\tau_a}\bigr)_{0\le a<p,\,j\in G_\xi}
\]
has full column rank. In particular, no choice of offsets with period \(p\) can overcome a fiber with more than \(p\) points.

**Minimal-period test:** For every fixed integer \(p\ge2\), the particular microscopic offsets \(\tau_a=a\varepsilon\) give a frame for all sufficiently small \(\varepsilon>0\) **if and only if**
\[
\max_{\xi}\#\{j:z_j^{rp}=\xi\}\le p.
\]
Thus the least permitted repair period is exactly the least integer \(p\ge2\) satisfying this alias-multiplicity inequality; such an integer always exists.

**Arbitrary-density repair:** There exist \(p\ge2\) and \(\varepsilon_0>0\), depending on \(\mathcal Z\) and \(r\), such that for **every** \(0<\varepsilon<\varepsilon_0\) the strictly increasing sequence
\[
t_n=rn+(n\bmod p)\varepsilon
\]
generates a frame. Thus an arbitrarily small positive periodic perturbation restores a frame at every prescribed average spacing \(r\), even if the unperturbed powers are incomplete.

Let
\[
m_r=\max_{w}\#\{j:z_j^r=w\}.
\]
This is a finite positive integer. For the above choice of \(p\), denote the **optimal** lower and upper frame bounds by \(A_\varepsilon\) and \(B_\varepsilon\). Their sharp orders as \(\varepsilon\downarrow0\) are
\[
A_\varepsilon\asymp\varepsilon^{2(m_r-1)},
\qquad
0<\inf_{0<\varepsilon<\varepsilon_0}B_\varepsilon
\leq\sup_{0<\varepsilon<\varepsilon_0}B_\varepsilon<\infty.
\]
Here \(X_\varepsilon\asymp Y_\varepsilon\) means two-sided positive constant bounds for sufficiently small \(\varepsilon\). In particular, when \(m_r>1\), the sampled frame condition number grows with exact order \(\varepsilon^{-2(m_r-1)}\); when \(m_r=1\), the unperturbed sample family is already a frame.

## Assumptions and scope

A Carleson interpolating sequence means
\[
\inf_j\prod_{k\ne j}\left|\frac{z_j-z_k}{1-\overline{z_k}z_j}\right|>0.
\]
A Stolz region at \(1\) means \(\{|1-z|\le\alpha(1-|z|)\}\) for some finite \(\alpha\ge1\). The nonzero, off-cut assumption fixes the principal logarithm. The theorem concerns a **fixed** such sequence and permits sampling offsets to depend on that sequence and on \(r\); it is not a uniform choice of offsets for all Carleson spectra. The space may be complex; no radial or real-spectrum hypothesis is made.

## Proof

**Step 1: Powered distinct nodes remain interpolating.** For fixed \(q=rp>0\), the holomorphic map \(F(z)=\exp(q\operatorname{Log}z)\) fixes \(1\) and has nonzero derivative \(q\) there. In a sufficiently small neighborhood of \(1\), its inverse is holomorphic and both \(|F(z)-F(w)|/|z-w|\) and \((1-|F(z)|)/(1-|z|)\) are bounded above and away from zero for the spectral points. Hence a separated Stolz tail remains pseudohyperbolically separated and contained in a Stolz region. Pairwise pseudohyperbolic separation in a Stolz region implies the Carleson interpolation condition (the standard Carleson-frame criterion). Only finitely many points lie outside that tail. Consequently the **distinct** values \(\Xi=\{\xi_j:j\ge0\}\), with repeats removed, form an interpolating Carleson sequence: any finite number of new distinct nodes preserves interpolation. This also proves that only finitely many fibers \(G_\xi\) are nonsingleton.

**Step 2: Exact fiberwise reduction.** Let \(u_\xi=(\sqrt{1-|\xi|^2}\,\xi^k)_{k\ge0}\). The Carleson interpolation theorem for normalized Hardy kernels gives constants \(0<c_q\le C_q<\infty\) such that for all square-summable scalar families \((b_\xi)\),
\[
c_q\sum_{\xi\in\Xi}|b_\xi|^2
\le\left\|\sum_{\xi\in\Xi}b_\xi u_\xi\right\|_{\ell^2(k)}^2
\le C_q\sum_{\xi\in\Xi}|b_\xi|^2.
\]
For each residue \(a\) and vector \(x=(x_j)\), the time-sampling coefficient (up to harmless complex conjugation) is
\[
\sum_j\overline{x_j}\sqrt{1-|z_j|^2}\,
 z_j^{ra+\tau_a}\,\xi_j^k
 =\sum_{\xi\in\Xi}\sqrt{1-|\xi|^2}\,\xi^k\,
 q_\xi\sum_{j\in G_\xi}\overline{x_j}z_j^{ra+\tau_a},
\]
where
\[
q_\xi=\sqrt{\frac{1-|z_j|^2}{1-|\xi|^2}}
=\sqrt{\frac{1-|z_j|^2}{1-|z_j|^{2rp}}}
\qquad(j\in G_\xi).
\]
Equality of \(\xi_j\) forces equality of \(|z_j|\), so \(q_\xi\) is well defined. As a function of \(|z_j|\in(0,1)\), its value extends continuously with positive limits \(1\) at zero and \((rp)^{-1/2}\) at one. Thus \(q_\xi\) is uniformly positive and finite. Applying the displayed Hardy-kernel inequalities separately for the \(p\) residue classes gives the two-sided comparison
\[
c\sum_{\xi\in\Xi}\|M_\xi\overline{x}|_{G_\xi}\|_2^2
\le\sum_{n\ge0}|\langle x,D^{t_n}g\rangle|^2
\le C\sum_{\xi\in\Xi}\|M_\xi\overline{x}|_{G_\xi}\|_2^2.
\]
Only finitely many matrices have multiple columns. For singleton fibers, the first matrix row has modulus \(|z_j|^{\tau_0}\), bounded away from zero because \(z_j\to1\) and all points are nonzero. The matrix entries are uniformly bounded because all exponents are nonnegative. Therefore the family is Bessel, and the lower frame inequality holds exactly when all nonsingleton fiber matrices have full column rank. This proves the criterion and its necessity, including the rank obstruction for \(|G_\xi|>p\).

**Step 3: Choose a finite period.** Because \(z_j\to1\), choose \(0<\rho<1\) so that every spectral point of modulus exceeding \(\rho\) has principal argument in \((-\pi/(2r),\pi/(2r))\), and only finitely many points have modulus at most \(\rho\). Let \(N\) be the number of these latter points and choose \(p\ge\max\{3,N\}\). Within any fiber of \(z\mapsto z^{rp}\), all points have the same modulus. If that modulus is at most \(\rho\), the fiber has at most \(N\le p\) members. Otherwise, equality of powers forces angular differences to be integral multiples of \(2\pi/(rp)\). Since all admissible arguments lie in an interval of length \(\pi/r\), the fiber has at most \(\lfloor p/2\rfloor+1\le p\) members. Thus every fiber has size at most \(p\).

Take \(\tau_a=a\varepsilon\) for \(0\le a<p\), with \((p-1)\varepsilon<r\). Then \(M_\xi\) is the first \(p\) rows of a Vandermonde matrix on the nodes \(w_j(\varepsilon)=z_j^{r+\varepsilon}\), \(j\in G_\xi\). There are only finitely many nonsingleton fibers. For distinct points \(z_i,z_j\) within a fiber, the analytic function \(z_i^{r+\varepsilon}-z_j^{r+\varepsilon}\) is either nonzero at \(\varepsilon=0\) or has a **simple** zero there: in the second case the derivative is \(z_i^r(\operatorname{Log}z_i-\operatorname{Log}z_j)\ne0\). Thus, for some \(\varepsilon_0>0\), all nodes within every such fiber remain pairwise distinct for every \(0<\varepsilon<\varepsilon_0\), and \((p-1)\varepsilon_0<r\). Each Vandermonde has full column rank; Step 2 proves the frame assertion. For any other fixed period, the same reasoning proves the sufficient direction of the minimal-period test if its largest powered fiber has at most \(p\) points. If a powered fiber has more than \(p\) points, Step 2 rules out a frame for every possible periodic offset, proving necessity. The sample times are strictly increasing because their consecutive gaps are either \(r+\varepsilon\) or \(r-(p-1)\varepsilon\).

**Step 4: Sharp small-jitter order.** Partition any nonsingleton fiber into subclusters on which \(s_j=z_j^r\) is constant. If a subcluster has size \(m\), then its nodes satisfy \(w_j(\varepsilon)=s_j\exp(\varepsilon\operatorname{Log}z_j)\); their pairwise differences have exact first order \(\Theta(\varepsilon)\). Differences between nodes in distinct subclusters stay bounded away from zero. For a fiber of size \(h\le p\), invert its square \(h\)-row Vandermonde block using Lagrange interpolation. The denominators \(\prod_{i\ne j}(w_j-w_i)\) have magnitude bounded below by a constant times \(\varepsilon^{m_j-1}\), where \(m_j\le m_r\) is the size of the subcluster containing \(j\); all numerator coefficients remain bounded. Hence every such matrix has smallest singular value bounded below by \(c\varepsilon^{m_r-1}\), uniformly across the finitely many nonsingleton fibers. Singleton matrices have a uniform positive lower bound. Step 2 gives \(A_\varepsilon\gtrsim\varepsilon^{2(m_r-1)}\).

For the reverse inequality when \(m_r=m\ge2\), choose a subcluster of exactly \(m\) points with identical \(s_j=s\). Their logarithms \(L_j=\operatorname{Log}z_j\) are distinct. Linear algebra supplies nonzero coefficients \((a_j)\) with \(\sum_j a_j L_j^h=0\) for all \(0\le h<m-1\). Restrict a unit vector to that subcluster with conjugated coefficients \((a_j)\). The sampled residue coefficients are, for the fixed finite set \(0\le a<p\),
\[
s^a\sum_j a_j\exp(a\varepsilon L_j)=O(\varepsilon^{m-1}),
\]
by Taylor expansion, uniformly in \(a\). Step 2's upper inequality therefore gives \(A_\varepsilon\lesssim\varepsilon^{2(m-1)}\). If \(m_r=1\), all matrices are already full column rank at zero and the same comparison gives \(A_0>0\). The uniform upper-frame-bound assertion follows from Step 2 and bounded matrix entries. A fixed nonzero coordinate vector gives a uniform positive lower bound for the optimal upper frame bound. This completes the proof.

## Verification

The bundled `CHECKER.py` implements supplementary finite-fiber calculations. It verifies the exact residue-class decomposition for two and three colliding spectral points, checks Vandermonde ranks under positive jitter, and numerically confirms singular-value exponents \(1\) and \(2\), corresponding to squared lower-frame exponents \(2\) and \(4\). These finite tests are diagnostics only; the infinite frame theorem follows from the analytic Carleson kernel and fiber-rank argument above.

A concrete infinite-spectrum example is \(z_0=0.7i\), \(z_1=-0.7i\), and \(z_{j+2}=1-2^{-(j+3)}\) for \(j\ge0\). This is an interpolating Stolz sequence with nonzero points away from the branch cut. With \(r=2\), the first two points have the same square, so unperturbed sampling is incomplete. But with \(p=2\), \(t_{2k}=4k\) and \(t_{2k+1}=4k+2+\varepsilon\) is a frame for each sufficiently small positive \(\varepsilon\), and the optimal lower frame bound has order \(\varepsilon^2\).

## Relationship to prior work

Krishtal, Mashreghi, and Miller (2026), *Frames from Functional Calculus*, Theorem 1.3 establishes a frame for all bounded offsets when \(r<\pi/c\) under an angular spectral restriction. Remark 2.13 demonstrates a collision counterexample for uniform power sampling at or beyond that threshold; Remark 2.5 observes that the unperturbed frame persists when the powered spectral nodes remain distinct. Neither statement yields recovery of **collided** spectral fibers by microscopic periodic offsets, the exact multi-fiber rank criterion, or the sharp conditioning exponent proved here. Krishtal and Miller's *Demystifying Carleson Frames* addresses arbitrary offsets for positive spectra, where power collisions cannot occur; their *Block Diagonal Carleson Frames* addresses Jordan-block orbit structures and positive-spectrum density phenomena. Krishtal and Miller's *Kadec-type theorems for sampled group orbits* assumes an initial frame under an isometric group and guarantees preservation under sufficiently small perturbations; it does not recover a contractive orbit that is incomplete before jitter. Standard Hardy-kernel interpolation is an input, not a claimed innovation.

## Limitations

The chosen period and jitter scale depend on the given spectral sequence and the prescribed step size. The result does not give a universal period valid for all spectra, uniform numerical constants in the lower frame bound, or a theorem for arbitrary Carleson sequences without the Stolz accumulation hypothesis. The asymptotic frame-bound exponent is exact; its leading numerical constant is not computed. Prioritization against results using different terminology remains subject to independent assessment.

## References

1. I. Krishtal, J. Mashreghi, and B. Miller, *Frames from Functional Calculus*, arXiv:2607.20798v1 (first public July 22, 2026), https://arxiv.org/abs/2607.20798 .
2. I. Krishtal and B. Miller, *Demystifying Carleson Frames*, arXiv:2505.04859v1 (May 7, 2025), https://arxiv.org/abs/2505.04859 .
3. I. Krishtal and B. Miller, *Block Diagonal Carleson Frames*, arXiv:2607.18491v1 (July 20, 2026), https://arxiv.org/abs/2607.18491 .
4. I. Krishtal and B. Miller, *Kadec-type theorems for sampled group orbits*, arXiv:2407.15827v1 (July 22, 2024), https://arxiv.org/abs/2407.15827 .
5. Classical Hardy-space Carleson interpolation theorem for normalized Szegő kernels, as used in the references above.
