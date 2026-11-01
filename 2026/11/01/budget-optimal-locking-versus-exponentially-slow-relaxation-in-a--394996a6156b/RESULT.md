# Budget-optimal locking versus exponentially slow relaxation in a detuned Kuramoto triad

## Finding

For three continuous-time Kuramoto oscillators with natural frequencies \((-\omega,0,\omega)\), \(\omega>0\), distribute a positive total directed-edge budget \(K\) by the frequency-distance power rule \(K_{ij}\propto |\Omega_i-\Omega_j|^p\), \(p\geq0\), with zero self-links and normalization \(\frac13\sum_{i,j}K_{ij}=K\). The following conclusions hold for every finite exponent \(p\geq0\), modulo common phase translation.

1. There is precisely one **locally exponentially attracting phase-locked configuration** if \(K>K_{\mathrm{lock}}(p)\), and none if \(K\leq K_{\mathrm{lock}}(p)\). Write
   \[
   q=2^p,\qquad c_q=\frac{\sqrt{1+32q^2}-1}{8q},\qquad
   K_{\mathrm{lock}}(p)=\frac{2\omega(2+q)}{3\sqrt{1-c_q^2}(1+2q c_q)}.
   \]
   This is an exact sharp threshold over **all** phase-locked configurations, not merely over a preselected symmetric ansatz.
2. The threshold is strictly decreasing in \(p\), with
   \[
   K_{\mathrm{lock}}(0)=1.1362522106646809\ldots\,\omega,
   \qquad
   K_{\mathrm{lock}}(p)=\frac{2\omega}{3}\left[1+\left(2-\frac1{\sqrt2}\right)2^{-p}+O(2^{-2p})\right].
   \]
   In particular the infimum \(2\omega/3\) is not attained by any finite exponent.
3. Fix a budget \(K>2\omega/3\) and let \(p\to\infty\). Along the unique attracting lock, its spectral relaxation gap \(g_p\) on the two-dimensional phase-difference space obeys
   \[
   g_p=\frac{9K}{2^{p+1}}\cos\phi_\infty+O(2^{-2p}),\qquad
   \phi_\infty=\frac12\arcsin\left(\frac{2\omega}{3K}\right)\in(0,\pi/4).
   \]
   Thus reallocating budget increasingly toward the most detuned pair reduces the locking threshold but ultimately makes the attracting configuration exponentially slow to relax as a function of the allocation exponent.
4. For each \(2\omega/3<K<K_{\mathrm{lock}}(0)\) there is a unique finite exponent \(p_c(K)>0\) below which no attracting lock exists. Above it the relaxation gap is strictly positive, tends to zero as \(p\downarrow p_c(K)\) and as \(p\to\infty\), and therefore attains a strictly positive global maximum at at least one **finite interior** exponent. Uniqueness of the maximizing exponent is not asserted.

## Assumptions and scope

The governing equations are
\[
\dot\theta_i=\Omega_i+\sum_{j=1}^{3}K_{ij}\sin(\theta_j-\theta_i),\qquad
(\Omega_1,\Omega_2,\Omega_3)=(-\omega,0,\omega).
\]
For \(i\ne j\), use \(K_{ij}=K|\Omega_i-\Omega_j|^p/C_p\), where \(C_p=\frac13\sum_{i\ne j}|\Omega_i-\Omega_j|^p\), and define \(K_{ii}=0\) even at \(p=0\). This off-diagonal convention avoids assigning any budget to dynamically inert self-links. Specifically, setting
\[
 a=K_{12}=K_{23}=\frac{3K}{2(2+q)},\quad b=K_{13}=q a,\quad q=2^p,
\]
ensures \(\frac13\sum_{i,j}K_{ij}=\frac23(2a+b)=K\). The model includes no phase lag, inertia, stochastic forcing, or time-varying weights. Phase locking means that all oscillator velocities equal a common constant; since \(\sum_i\dot\theta_i=0\), this constant is necessarily zero. Exponential attraction is understood **modulo the neutral common-phase rotation**; it is not attraction to a single point in unreduced three-dimensional phase space.

## Proof

**1. Exhausting all locked configurations.** Let \(u=\theta_2-\theta_1\) and \(v=\theta_3-\theta_2\) modulo \(2\pi\). Direct subtraction yields
\[
\begin{aligned}
\dot u&=\omega-2a\sin u+a\sin v-b\sin(u+v),\\
\dot v&=\omega+a\sin u-2a\sin v-b\sin(u+v).
\end{aligned}
\]
At a lock, \(\sin u=\sin v\). All possibilities are therefore either \(v\equiv u\pmod{2\pi}\) or \(v\equiv\pi-u\pmod{2\pi}\). On the second branch, \(u+v\equiv\pi\), the two nearest-neighbor linearized edge conductances are opposite and the distant-edge conductance is \(-b\). The weighted Laplacian has trace \(-2b<0\), so at least one nonneutral linearized direction of the dynamical Jacobian \(-L\) is unstable. This branch cannot be exponentially attracting, including at intersections with the first branch.

On the first branch write \((\theta_1,\theta_2,\theta_3)=(-\phi,0,\phi)\), up to a common shift. The locked equation and the two nonzero eigenvalues of the **negative** Jacobian (the positive decay rates) are exactly
\[
 \omega=a(\sin\phi+q\sin2\phi),\quad
 \lambda_1=3a\cos\phi,\quad
 \lambda_2=a(\cos\phi+2q\cos2\phi).
\]
One can verify the eigenvectors as \((1,-2,1)\) and \((-1,0,1)\). An attracting lock requires both rates positive. Since \(\lambda_1>0\) implies \(\cos\phi>0\), the equilibrium equation with \(\omega>0\) then forces \(\phi\in(0,\pi/2)\) modulo \(2\pi\).

**2. Exact fold and unique attracting branch.** On \((0,\pi/2)\), define \(h_q(\phi)=\sin\phi+q\sin2\phi\). Its derivative is \(h'_q(\phi)=\cos\phi+2q\cos2\phi\), while \(h''_q(\phi)=-\sin\phi-4q\sin2\phi<0\). Consequently \(h'_q\) has exactly one zero \(\phi_*(q)\), and \(h_q\) increases strictly from zero to its strict maximum at \(\phi_*\). For \(\phi\in(0,\phi_*)\), both positive decay rates hold; the remainder of \((0,\pi/2)\) has \(\lambda_2<0\). At \(\phi_*\), \(\lambda_2=0\), excluding exponential attraction. Solving \(h'_q(\phi_*)=0\) with \(c_q=\cos\phi_*\) gives
\[
 4q c_q^2+c_q-2q=0,\qquad
 c_q=\frac{\sqrt{1+32q^2}-1}{8q},
\]
which yields the displayed exact threshold after substituting \(a=3K/[2(2+q)]\). This proves the global exhaustive and unique stable-lock assertion.

**3. Strict budget improvement and endpoint.** Because \(h'_q(\pi/3)=1/2-q<0\) for \(q\geq1\), the maximizing phase satisfies \(\phi_*<\pi/3\) and hence \(c_q>1/2\). The envelope derivative is
\[
\frac{\mathrm d}{\mathrm dq}\left(\frac{h_q(\phi_*(q))}{q+2}\right)
=\frac{\sin\phi_*(q)(4\cos\phi_*(q)-1)}{(q+2)^2}>0.
\]
Thus \(K_{\mathrm{lock}}\) decreases strictly with \(q=2^p\). As \(q\to\infty\), the maximizing phase converges to \(\pi/4\). A direct expansion of \(\max_{\phi} [q\sin2\phi+\sin\phi]\) about \(\pi/4\) yields \(q+1/\sqrt2+O(q^{-1})\), proving the two-term threshold formula. In particular the finite-\(p\) threshold always exceeds \(2\omega/3\).

**4. Spectral edge and the finite optimal exponent.** For fixed \(K>2\omega/3\), the unique stable phase solves
\[
 \omega=\frac{3K}{2(q+2)}\,[\sin\phi_q+q\sin2\phi_q].
\]
The stable solution converges to \(\phi_\infty=\frac12\arcsin(2\omega/(3K))\in(0,\pi/4)\). Its decay rates satisfy
\[
\lambda_1=\frac{9K\cos\phi_\infty}{2q}+O(q^{-2}),\qquad
\lambda_2=3K\cos2\phi_\infty+O(q^{-1}).
\]
Since the second limit is strictly positive, \(g_p=\min(\lambda_1,\lambda_2)=\lambda_1\) for sufficiently large \(p\), giving the claimed edge rate. For \(2\omega/3<K<K_{\mathrm{lock}}(0)\), strict continuity and monotonicity of the threshold give a unique \(p_c\). As \(p\downarrow p_c\), the attracting phase tends to the fold and \(\lambda_2\downarrow0\). As \(p\to\infty\), \(\lambda_1\downarrow0\). The strictly positive, continuous gap must therefore achieve a global positive maximum at a finite interior point, by compactness after excluding its two vanishing ends.

## Verification

Execute `python verify.py` with Python 3, NumPy, SymPy and SciPy installed. The script checks the exact Laplacian eigenvectors, the negative trace of the alternate locked branch, finite-grid folded equations, direct vector-field stationarity and direct three-by-three Jacobian spectra for 400 positive cases, sample threshold monotonicity, and the large-exponent asymptotic. The script passed in the working environment. These finite checks do not replace the proof above and do not certify global uniqueness by enumeration.

For the natural budget \(K=\omega\), the zero-exponent edge-allocation limit \(p=0\) has no attracting locked configuration because \(K_{\mathrm{lock}}(0)>\omega\); at \(p=1\), \(K_{\mathrm{lock}}(1)=0.9747247402447522\ldots\,\omega<\omega\), so an attracting locked configuration exists. Its positive transverse decay rates are approximately \(0.830350969\) and \(0.411113093\). At still larger \(p\), the slower rate decreases to zero despite continued attraction.

## Relationship to prior work

Pando, Bernstein and collaborators (arXiv:2603.29648, first version March 31, 2026) introduced frequency-distance-proportional Kuramoto coupling under a fixed budget and numerically found non-monotone synchronization behavior in large random-frequency ensembles, with an intermediate favorable exponent. Their full accessible HTML including the analytical and supplementary sections was examined. It does **not** state the present exact finite three-frequency locking threshold, exhaustive stable-lock classification, strict exponent monotonicity for onset, or the exponentially vanishing relaxation gap.

Zhao and Zhou (arXiv:2407.11314, Sections 1–3) classify equilibria of a three-oscillator isosceles network with **zero intrinsic frequency mismatch** and attractive or repulsive couplings; the equations there have no detuning term and no exponent-dependent coupling budget. The model is structurally related, but its autonomous zero-detuning equilibrium classification does not imply the forced fold law here. Xin, Kikkawa and Liu (ACC 2016, DOI:10.1109/ACC.2016.7525284) address standard **uniform-coupling** three- and four-oscillator equilibrium equations; the specific power-weighted budget optimization here lies outside that assumption. General gradient-flow and weighted-Laplacian facts are used as established tools, not claimed as novel. Historical priority may be affected by specialized small-network optimization work not recovered in the searches.

## Limitations

Only a symmetric **three-site** detuning pattern and positive reciprocal sine couplings are treated. The result is local and modulo global phase: it does not establish attraction from almost every phase initialization, exclude other non-attracting states or periodic solutions, or extend the monotonic threshold to Gaussian or other large-network frequency distributions. The coupling convention excludes wasted self-links at \(p=0\). The infinite-exponent limit is a **disconnected** network; it is not an admissible finite exponent with exponential attraction of the relative phases. No uniqueness of the gap-maximizing finite exponent is proved, and no independent validation or historical-priority certification is claimed.

## References

1. A. Pando et al., *Enhanced synchronization with proportional coupling in Kuramoto oscillator networks under a fixed coupling budget*, arXiv:2603.29648v1 (March 31, 2026), revised as v2 October 21, 2026, https://arxiv.org/html/2603.29648v2 .
2. X. Zhao and X. Zhou, *Critical Points, Stability, and Basins of Attraction of Three Kuramoto Oscillators with Isosceles Triangle Network*, arXiv:2407.11314v2 (2024), https://arxiv.org/pdf/2407.11314 .
3. X. Xin, T. Kikkawa and Y. Liu, *Analytical solutions of equilibrium points of the standard Kuramoto model: 3 and 4 oscillators*, American Control Conference (2016), DOI:10.1109/ACC.2016.7525284 .
