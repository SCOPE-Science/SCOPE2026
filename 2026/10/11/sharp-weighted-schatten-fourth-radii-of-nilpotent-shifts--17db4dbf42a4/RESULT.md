# Sharp weighted Schatten-fourth radii of nilpotent shifts

## Finding
For each integer \(n\ge2\), put \(T e_j=a_j e_{j+1}\) on \(\mathbb C^n\) for \(0\le j\le n-2\), and \(T e_{n-1}=0\), where the complex weights \(a_j\) may vanish. For \(0\le t\le1\), define the weighted Schatten-fourth numerical radius
\[
\mathcal W_{t,4}(T)=\sup_{\theta\in\mathbb R}\left\|t e^{i\theta}T+(1-t)e^{-i\theta}T^*\right\|_4,
\qquad \|A\|_4^4=\operatorname{tr}\bigl((A^*A)^2\bigr).
\]
Then, with \(b_j=|a_j|^2\), the exact identity is
\[
\boxed{\mathcal W_{t,4}(T)^4=
\bigl(t^4+(1-t)^4\bigr)\sum_{j=0}^{n-2}b_j^2
+4t^2(1-t)^2\sum_{j=0}^{n-3}b_jb_{j+1}.}
\tag{1}
\]
(The second sum is empty when \(n=2\).) Consequently the optimal, dimension-dependent constant over all such shifts is
\[
\boxed{\mathcal W_{t,4}(T)^4\le
\bigl(t^4+(1-t)^4+4t^2(1-t)^2\cos(\pi/n)\bigr)\|T\|_4^4.}
\tag{2}
\]
For \(0<t<1\) and \(T\ne0\), equality in (2) holds if and only if there is a \(c>0\) such that
\[
\boxed{|a_j|^2=c\sin\bigl((j+1)\pi/n\bigr)\quad(0\le j\le n-2).}
\tag{3}
\]
The phases of the \(a_j\) are unrestricted. At \(t=0,1\), every shift realizes equality.

For \(n\ge3\), define the Euclidean unit vector \(v\in\mathbb R^{n-1}\) by
\[
v_j=\sqrt{2/n}\sin\bigl((j+1)\pi/n\bigr).
\]
For \(0<t<1\) the sharp quantitative rigidity estimate is
\[
\boxed{
\left(t^4+(1-t)^4+4t^2(1-t)^2\cos(\pi/n)\right)\|T\|_4^4
-\mathcal W_{t,4}(T)^4
\ge4t^2(1-t)^2\left(\cos(\pi/n)-\cos(2\pi/n)\right)
\left(\|b\|_2^2-|\langle b,v\rangle|^2\right).}
\tag{4}
\]
The factor \(\cos(\pi/n)-\cos(2\pi/n)\) cannot be increased, even while all weights are strictly positive.

For every unilateral weighted shift \(T\in\mathcal S_4(\ell_2(\mathbb N_0))\), identity (1) remains valid with both sums infinite and absolutely convergent. Its optimal dimension-free constant is
\[
\sup_{T\ne0}\frac{\mathcal W_{t,4}(T)^4}{\|T\|_4^4}
=t^4+(1-t)^4+4t^2(1-t)^2.
\tag{5}
\]
For \(0<t<1\), the supremum (5) is **not attained** by any nonzero infinite shift; for \(t=0,1\), it is attained by every nonzero such shift.

## Assumptions and scope
The finite-dimensional assertion concerns all nilpotent one-step unilateral weighted shifts on the standard complex Euclidean space, not arbitrary nilpotent matrices. The Schatten-fourth norm is unnormalized (no division of the trace by dimension). The parameter \(t\) lies in the closed interval \([0,1]\). In (4), \(b\) denotes the real vector of squared weight moduli, \(b=(b_0,\ldots,b_{n-2})\), and the Euclidean inner product is the ordinary sum. Infinite shifts are defined on the standard complex \(\ell_2\) basis and assumed Schatten-fourth, equivalently \(\sum_{j\ge0}|a_j|^4<\infty\). All claims are uniform over arbitrary complex phases and zero weights unless a nonzero equality case is expressly stated.

## Proof
**Phase reduction.** Let \(D_\theta e_j=e^{ij\theta}e_j\). Then \(D_\theta TD_\theta^*=e^{i\theta}T\) and \(D_\theta T^*D_\theta^*=e^{-i\theta}T^*\). Thus the Schatten norm in the definition is independent of \(\theta\), including in the infinite setting. A further diagonal unitary removes individual nonzero weight phases, but the trace calculation below already handles their moduli.

**Exact fourth moment.** Set \(s=1-t\) and \(B=tT+sT^*\). Put \(b_{-1}=b_{n-1}=0\). The diagonal entries of \(B^*B\) are \(d_j=t^2b_j+s^2b_{j-1}\), and its only possible off-diagonal entries are at separation two, with squared moduli \(t^2s^2b_jb_{j+1}\). Consequently
\[
\operatorname{tr}((B^*B)^2)
=\sum_{j=0}^{n-1}d_j^2+2t^2s^2\sum_{j=0}^{n-3}b_jb_{j+1}
=(t^4+s^4)\sum_{j=0}^{n-2}b_j^2+4t^2s^2\sum_{j=0}^{n-3}b_jb_{j+1}.
\]
This proves (1), including \(n=2\) and \(t=0,1\). Since \(T^*T\) is diagonal with entries \(b_j\) (and a final zero), \(\|T\|_4^4=\sum_jb_j^2\).

**Sharp finite constant and complete equality.** On \(\mathbb R^{n-1}\), let \(J\) be the symmetric tridiagonal matrix with nearest-neighbor off-diagonal entries \(1/2\) and zeros otherwise. Then \(\langle b,Jb\rangle=\sum b_jb_{j+1}\). The discrete Dirichlet recurrence with endpoints \(u_{-1}=u_{n-1}=0\) yields the complete orthogonal eigenbasis
\[
u_j^{(k)}=\sin\bigl((j+1)k\pi/n\bigr),\quad
Ju^{(k)}=\cos(k\pi/n)u^{(k)},\quad 1\le k\le n-1.
\]
For \(n=2\) this consists of the single eigenvalue zero. In all dimensions the largest eigenvalue is \(\cos(\pi/n)\), simple, with a strictly positive eigenvector \(u^{(1)}\). The Rayleigh principle gives (2), and the strict top-eigenvalue gap gives the exact positive equality class (3) for \(0<t<1\). Arbitrary phases do not affect (1).

**Sharp rigidity.** For \(n\ge3\), the second largest eigenvalue of \(J\) is \(\cos(2\pi/n)\). Decompose \(b=\langle b,v\rangle v+z\) with \(z\perp v\). The spectral theorem gives
\[
\cos(\pi/n)\|b\|_2^2-\langle b,Jb\rangle
\ge\bigl(\cos(\pi/n)-\cos(2\pi/n)\bigr)\|z\|_2^2.
\]
Combining with (1) proves (4). To verify optimality **inside the admissible nonnegative cone**, let \(u^{(2)}\) be the second sine eigenvector and choose \(b=v+\varepsilon u^{(2)}\) with \(0<|\varepsilon|\) sufficiently small that every coordinate of \(b\) is positive. Equality holds in the displayed gap estimate and hence in (4). Choose weights with moduli \(\sqrt{b_j}\); all are nonzero. This proves sharpness without relying on inadmissible sign-changing weight squares.

**Infinite shifts and nonattainment.** In \(\ell_2(\mathbb N_0)\), Schatten-fourth membership is exactly \(b=(|a_j|^2)\in\ell_2\). Finite truncations converge in Schatten-fourth norm, and the trace is continuous for fourth moments; alternatively, the trace expansion above is absolutely convergent by Cauchy–Schwarz. Hence (1) holds with sums over all \(j\ge0\). The identity
\[
\sum_{j\ge0}b_j^2-\sum_{j\ge0}b_jb_{j+1}
=\frac12b_0^2+\frac12\sum_{j\ge0}(b_j-b_{j+1})^2
\tag{6}
\]
holds for all real \(b\in\ell_2\), because \(b_j\to0\) and the sums converge. If its right side vanishes, then \(b_0=0\) and all successive coordinates agree, so \(b=0\). Thus for nonzero \(T\), the ratio in (5) is strictly less than its stated supremum when \(0<t<1\). The finite-dimensional sine extremizers, extended by zero to \(\ell_2\), have ratio \(t^4+s^4+4t^2s^2\cos(\pi/n)\), tending to the right side of (5). For endpoint \(t\), (1) makes every nonzero operator an extremizer. This completes the proof.

## Verification
The accompanying standalone standard-library verifier `verify_shift_s4.py` independently forms finite matrices over exact rational arithmetic and checks (1) for sizes \(2\le n\le10\), five parameter values, and three explicit coefficient patterns per size. It also checks the sine eigenvector quotients and equality of both sides of the sharp spectral-gap estimate for \(3\le n\le33\). Independently, complex-phase matrices were checked numerically against (1) in several dimensions and at three angles, with agreement to floating-point tolerance. These **finite checks do not establish** the all-dimensional or infinite-dimensional assertions; the preceding proof does.

To replay without third-party packages, run `python verify_shift_s4.py` in the directory containing that embedded file. Expected successful output: `SCHATTEN_FOURTH_SHIFT_EXACT_MATRIX_AND_PATH_CHECK_OK`.

## Relationship to prior work
S. Sahoo, *Further bounds on \(p\)-numerical radii of operators via generalized Aluthge transform*, arXiv:2504.04693v1 (first publicly posted April 7, 2025), develops general Schatten-\(p\) numerical-radius inequalities. Its inspected Theorems 2.1–2.3 and related remarks bound operator radii via Aluthge transforms and blocks; they do **not** furnish the exact quartic profile, the dimension-sharp sine-law weights, or infinite-shift nonattainment established here. Ghosh–Birbonshi–Ojha, arXiv:2608.17486v1 (August 18, 2026), studies the *ordinary operator-norm numerical radius* for a specific infinite family of geometrically patterned weighted shifts; its spectral/root constructions likewise do not imply the present Schatten-fourth norm theorem.

The earlier Alrimawi–Kawariq–Abushaheen work introduces weighted Schatten radius inequalities for \(2\times2\) blocks and estimates, not this all-dimensional extremal classification. A later paper by Pal–Chandok, arXiv:2610.11336v1 (October 8, 2026), was checked for potentially covering results: its inspected main results are generalized-Aluthge bounds and illustrative small matrices, not an exact path-graph spectral optimization. The sharpness mechanism here is an explicit Rayleigh quotient for squared shift weights, not a specialization of a cited dimension-uniform inequality.

## Limitations
The formula is for the Schatten exponent four and **one-step unilateral shifts** only. It does not establish a comparable sharp profile for arbitrary nilpotent operators, other Schatten exponents, or general weighted graphs. The rigidity estimate quantifies the squared moduli vector, not phase stability (phases are genuinely unconstrained). The infinite-dimensional assertion concerns Schatten-fourth shifts, not all bounded weighted shifts. The novelty assessment is relative to the specifically inspected and searched literature; it is not an independent literature certification. The full Gao–Hou–Zhao July 2026 article was not accessible through the attempted lawful routes, so implicit coverage there remains a residual originality risk.

## References
1. S. Sahoo, *Further bounds on p-numerical radii of operators via generalized Aluthge transform*, arXiv:2504.04693v1 (2025), https://arxiv.org/pdf/2504.04693.
2. A. Ghosh, R. Birbonshi, and S. Ojha, *On the numerical radius of a class of weighted shift operators*, arXiv:2608.17486v1 (2026), https://arxiv.org/html/2608.17486v1.
3. F. Alrimawi, H. Kawariq, and F. A. Abushaheen, *Generalized-weighted numerical radius inequalities for Schatten p-norms*, International Journal of Mathematics and Computer Science 17 (2022), 1463–1473, https://future-in-tech.net/17.3/R-Alrimawi.pdf.
4. F. Gao, M. Hou, and J. Zhao, *On p-numerical radius inequalities for Hilbert space operators*, Mathematische Nachrichten 299 (2026), 2191–2207; first online July 6, 2026, https://doi.org/10.1002/mana.70187.
5. K. Pal and S. Chandok, *On weighted Schatten p-numerical radii via generalized Aluthge transformation*, arXiv:2610.11336v1 (2026), https://arxiv.org/html/2610.11336v1. (October 8, 2026).
