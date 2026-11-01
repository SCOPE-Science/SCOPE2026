# Sharp imaginary-strip width and boundary-layer law for Hardy monomial composition Berezin ranges

## Finding
Let \(m\ge2\) be an integer, \(a\in\mathbb C\) with \(0<q=|a|\le1\), and let \(C_{a z^m}\) be the composition operator on classical complex \(H^2(\mathbb D)\). Define the sharp vertical half-width of its Berezin range by
\[
H_m(q)=\sup_{w\in\mathbb D}|\operatorname{Im}\langle C_{a z^m}\widehat k_w,\widehat k_w\rangle|.
\]
The value depends on \(a\) only through \(q\). Put \(\alpha=(m+1)/2\). For \(0<q<1\), set \(\eta=-\log q\); there is a **unique** \(u_q\in(0,\log(1+1/\alpha))\) satisfying
\[
\tanh(\eta+\alpha u_q)=\alpha(e^{u_q}-1).
\]
The exact, attained half-width is
\[
\boxed{H_m(q)=\frac{1-e^{-u_q}}{2\sinh(\eta+\alpha u_q)}}.
\]
For \(q=1\), the sharp half-width is \(H_m(1)=1/(m+1)=1/(2\alpha)\), **not attained** by any interior normalized reproducing kernel. The imaginary projection of the Berezin range is precisely \([-H_m(q),H_m(q)]\) for \(0<q<1\), and \((-H_m(1),H_m(1))\) for \(q=1\). For \(q=0\), the Berezin range is real and its imaginary projection is \(\{0\}\). For fixed \(m\), the half-width is strictly increasing on \(0\le q\le1\), so this geometric invariant recovers \(|a|\) uniquely; for each fixed \(q>0\) it is strictly decreasing with integer degree \(m\ge2\). By contrast, the ordinary Berezin number is exactly \(1\) for every such symbol, including \(a=0\).

For \(0<q<1\), exactly \(m-1\) distinct kernel parameters attain the positive endpoint and exactly \(m-1\) attain the negative endpoint. All have modulus \(e^{-u_q/2}\). With \(d_q=e^{-(\eta+\alpha u_q)}\), they are the solutions of
\[
\frac{a}{|a|}\left(\frac{w}{|w|}\right)^{m-1}
=\frac{2d_q\pm i(1-d_q^2)}{1+d_q^2},
\qquad |w|=e^{-u_q/2}.
\]
The plus sign corresponds to the positive endpoint.

The complete endpoint asymptotics are
\[
H_m(q)\sim q\frac{\alpha^\alpha}{(\alpha+1)^{\alpha+1}}
\quad(q\downarrow0),
\]
and, with \(\eta=-\log q\downarrow0\),
\[
u_q=\sqrt{\frac{2\eta}{\alpha}}+O(\eta),\qquad
H_m(1)-H_m(q)=\frac{\sqrt\eta}{\sqrt2\,\alpha^{3/2}}+O(\eta).
\]
Consequently the exact critical exponent for the strip-width deficit at the compact-to-isometric symbol boundary is one half.

At \(q=1\), write \(u=-\log|w|^2\) and take \(\psi\in(-\pi,\pi]\) to represent \(\arg a+(m-1)\arg w\) modulo \(2\pi\). A sequence \(w_j\) satisfies \(\operatorname{Im}\langle C_{a z^m}\widehat k_{w_j},\widehat k_{w_j}\rangle\to\pm H_m(1)\) **if and only if**
\[
u_j\to0,\qquad \psi_j/u_j\to\pm\alpha.
\]
Thus all extremizing kernels escape to the circle at one of the \(m-1\) roots \((w/|w|)^{m-1}=\overline a\), with a sharp angular-to-radial approach ratio.

## Assumptions and scope
Here \(H^2(\mathbb D)\) has norm \(\|\sum_{n\ge0}c_nz^n\|^2=\sum_{n\ge0}|c_n|^2\). Its reproducing kernel is \(k_w(z)=(1-\overline w z)^{-1}\), and \(\widehat k_w=(1-|w|^2)^{1/2}k_w\). The inner product is linear in its first input. The Berezin transform is \(\widetilde C(w)=\langle C\widehat k_w,\widehat k_w\rangle\). The word *width* refers to the least closed horizontal strip symmetric about the real axis containing the Berezin range; it is not the usual Berezin number. No assertion about the entire planar boundary, convexity, or the ordinary numerical range is made.

## Proof
**Kernel calculation and circular fibers.** Reproducing gives
\[
\widetilde C(w)=\frac{1-|w|^2}{1-\overline w\,a w^m}.
\]
For \(w=\sqrt t\,e^{i\vartheta}\), set \(\alpha=(m+1)/2\), \(d=qt^\alpha\), and \(\gamma=\arg a+(m-1)\vartheta\). Since \(m\ge2\), \(\gamma\) runs through all angles. Thus for each \(t\in(0,1)\), the Berezin values are the circle
\[
\left|z-\frac{1-t}{1-d^2}\right|=\frac{(1-t)d}{1-d^2}.
\]
In particular, their maximum absolute imaginary part is the radius \((1-t)d/(1-d^2)\). Its two extremal points on the circle occur at the precisely displayed phase values in the Finding: indeed, for \(z=(1-t)(1\pm id)/(1-d^2)\), solving \(z=(1-t)/(1-de^{i\gamma})\) gives \(e^{i\gamma}=(2d\pm i(1-d^2))/(1+d^2)\). There are exactly \(m-1\) preimages of each phase, none coincident.

**One-variable uniqueness.** Substitute \(t=e^{-u}\), \(\eta=-\log q\); the circle radius becomes
\[
R_{\eta}(u)=\frac{1-e^{-u}}{2\sinh(\eta+\alpha u)}\quad(u>0).
\]
For \(\eta>0\), the radius tends to zero at both endpoints of \((0,\infty)\), and
\[
\frac{R'_{\eta}(u)}{R_{\eta}(u)}=
\frac1{e^u-1}-\alpha\coth(\eta+\alpha u).
\]
A zero is equivalent to \(\tanh(\eta+\alpha u)=\alpha(e^u-1)\) and requires \(0<u<U=\log(1+1/\alpha)\). Define
\[
F(u)=\operatorname{arctanh}[\alpha(e^u-1)]-\alpha u\quad(0<u<U).
\]
Then \(F(0+)=0\), \(F(U-)=\infty\), and
\[
F'(u)=\alpha\left(\frac{e^u}{1-\alpha^2(e^u-1)^2}-1\right)>0.
\]
Consequently \(F(u)=\eta\) has one solution. The derivative of \(R_\eta\) is positive before and negative after it, so this solution gives the unique maximum. For \(\eta=0\), \(F(u)>0\) for every \(0<u<U\), hence \(R'_0(u)<0\) there; the derivative is also negative for \(u\ge U\) directly. Therefore \(R_0(u)\) decreases strictly from \(1/(2\alpha)\) to zero. No interior kernel attains the supremum at \(q=1\).

**Imaginary projections.** The open disk is path-connected and its Berezin transform is continuous, so the imaginary projection is an interval. Conjugate symmetry follows by replacing \(\gamma\) with \(-\gamma\). The preceding attainment analysis gives exactly the stated closed or open interval endpoints.

**Strict monotonicity and invariant separation.** For every fixed \(t\in(0,1)\), the fiber radius \((1-t)d/(1-d^2)\) is strictly increasing in \(d\in(0,1)\). Here \(d=qt^\alpha\) increases strictly in \(q>0\) and decreases strictly in \(\alpha\) at fixed positive \(q\). Evaluation at the interior maximizing parameter for the smaller half-width proves both strict inequalities whenever \(q<1\); for \(q=1\), use \(H_m(1)=1/(2\alpha)\) and the strict smaller bound at any \(q<1\). Finally \(d\le t\) implies \( |\widetilde C(w)|\le(1-t)/(1-d)\le1\), with equality at \(w=0\); hence the standard Berezin number is identically one and does not encode these distinctions.

**Small coefficient.** Directly in \(t\),
\[
\frac{R_q(t)}q=\frac{(1-t)t^\alpha}{1-q^2t^{2\alpha}}.
\]
As \(q\downarrow0\), this converges uniformly on \([0,1]\) to \((1-t)t^\alpha\), which has its unique global maximum at \(t=\alpha/(\alpha+1)\) with value \(\alpha^\alpha/(\alpha+1)^{\alpha+1}\). This proves the first asymptotic.

**Critical boundary layer.** Taylor expansion of the strictly increasing root map gives
\[
F(u)=\frac\alpha2u^2+O(u^3)\quad(u\downarrow0).
\]
Hence \(u_q=\sqrt{2\eta/\alpha}+O(\eta)\). Since \(\eta=O(u_q^2)\), uniformly along these roots,
\[
R_\eta(u_q)=\frac1{2\alpha}\left(1-\frac{u_q}2-\frac\eta{\alpha u_q}+O(u_q^2)\right)
=\frac1{2\alpha}\left(1-u_q+O(\eta)\right).
\]
This yields the stated sharp square-root coefficient. As \(\eta\downarrow0\), the maximizing radii \(e^{-u_q/2}\) tend to one. Indeed \(C_{az^m}z^n=a^n z^{mn}\), so the nonzero singular values of this composition operator are \(q^n\) for \(n\ge0\); it is compact at \(q<1\) and is an isometry at \(q=1\). This identifies the geometric transition as a compact-to-isometric boundary layer.

**Every limiting extremizer at \(q=1\).** If the imaginary parts converge to either sharp endpoint, the strict finite-\(u\) inequality forces \(u_j\to0\). Since the numerator of \(\widetilde C(w_j)\) is \(O(u_j)\) and its imaginary part has nonzero limit, the denominator must be \(O(u_j)\); thus the principal phase \(\psi_j=O(u_j)\). Uniformly for such phases,
\[
\widetilde C(w_j)=\frac{u_j+O(u_j^2)}{\alpha u_j-i\psi_j+O(u_j^2)}.
\]
Any subsequential limit of \(\psi_j/u_j\) therefore has imaginary part \(\beta/(\alpha^2+\beta^2)\) in its limiting Berezin value. This scalar function attains \(\pm1/(2\alpha)\) only at \(\beta=\pm\alpha\), respectively. All subsequences consequently have the same ratio limit. Conversely, that ratio limit in the displayed expansion gives the claimed limiting imaginary value. This proves the if-and-only-if statement.

## Verification
The accompanying `verify.py` checks the circular-fiber maxima, unique scalar optimizers against independent one-dimensional optimization, imaginary strip bounds over finite sampling grids, complex symbol-phase invariance, and both endpoint asymptotics for several integers \(m\). It reports 45,527 passed supplementary assertions with SciPy. Reproduce with `python3 verify.py` in an environment with SciPy installed. Finite sampling is not used as proof of the universal statements.

## Relationship to prior work
Cowen and Felder (2021) introduced and studied convexity of Hardy Berezin ranges, including elliptic automorphism and Blaschke-factor composition symbols, and posed geometric questions. Augustine, Garayev and Shankar (2023) studied Hardy composition with linear symbols and Bergman analogues. Bourdon, Le and Thompson (arXiv:2610.17634, publicly submitted 2026-10-13) investigate Hardy composition Berezin-range shape, symmetry and convexity, including a linear-symbol classification. The present statement concerns the exact least horizontal strip, all of its attaining kernels, and the compact-to-isometric square-root transition for nonlinear monomial symbols, rather than those qualitative convexity results. The full 2026 preprint was not accessible during this examination, so unrecognized implicit earlier coverage remains a scientific priority risk.

## Limitations
This is a theorem about the imaginary projection of the Berezin range, not a classification of the full two-dimensional set, numerical range, or norm. Its novelty assessment is based on inspected accessible literature and mathematical-record searches, not an exhaustive index of all publications; an inaccessible plausible 2026 source is explicitly retained as a priority risk. No independent audit has been performed.

## References
1. C. C. Cowen and C. Felder, *Convexity of the Berezin Range* (2021), arXiv:2109.12095; https://www.researchgate.net/publication/354857566_Convexity_of_the_Berezin_Range .
2. A. Augustine, M. Garayev and P. Shankar, *Composition Operators, Convexity of Their Berezin Range and Related Questions*, Complex Analysis and Operator Theory 17 (2023), https://doi.org/10.1007/s11785-023-01432-x .
3. P. Bourdon, T. Le and D. Thompson, *Berezin Ranges of Composition Operators on \(H^2\)* (first public 2026-10-13), arXiv:2610.17634; https://borowiecki.dev/abs/2610.17634 .
