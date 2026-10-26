# Fixed-width random rotation intervals with vanishing topological entropy

## Finding
For every integer \(m\ge 2\), there is an iid two-symbol random degree-one circle endomorphism with random lift \(F^{[m]}\) for which, almost surely,
\[
\operatorname{Rot}(F^{[m]})=[0,1],\qquad
\mathbb E\sup_{x\in\mathbb R}|F^{[m]}_{\omega}(x)-x|=1,
\]
yet its random topological entropy obeys
\[
0<h_{\mathrm{top}}^{(r)}(F^{[m]})\leq\frac{\log(2m+1)}m\longrightarrow0.
\]
More precisely, writing \(f_m\) for the nonidentity deterministic circle map below,
\[
h_{\mathrm{top}}^{(r)}(F^{[m]})=\frac{h_{\mathrm{top}}(f_m)}m.
\]
Consequently, **neither the length of the random rotation interval alone nor that length jointly with a fixed expected uniform lift-displacement budget admits any strictly positive universal entropy lower bound** over integrable random degree-one circle endomorphisms. The individual entropy in each system remains strictly positive.

## Assumptions and scope
Let \(\mathbb T=\mathbb R/\mathbb Z\) with its geodesic metric. For \(m\ge2\), define the continuous degree-one lift \(B_m:\mathbb R\to\mathbb R\) by its restriction to \([0,1]\):
\[
B_m(x)=\begin{cases}(2m+1)x,&0\le x\le1/2,\\
(1-2m)x+2m,&1/2\le x\le1,\end{cases}
\qquad B_m(x+j)=B_m(x)+j\ (j\in\mathbb Z).
\]
Equivalently \(B_m(x)-x=m(1-|2\{x\}-1|)\), with \(\{x\}\in[0,1)\) the fractional part. Set \(f_m=B_m\bmod1\). Let \(\Omega=\{0,1\}^{\mathbb N_0}\), equipped with the iid Bernoulli law satisfying \(\mathbb P(\omega_0=1)=1/m\) and the left shift. The fibre lift is \(F^{[m]}_\omega=\operatorname{Id}\) if \(\omega_0=0\) and \(F^{[m]}_\omega=B_m\) if \(\omega_0=1\). The circle quotient has fibre maps \(\operatorname{Id}_{\mathbb T}\) and \(f_m\).

The random rotation set is the closed set of upper asymptotic lift displacements of the fibre cocycle in the convention of Li–Lloyd–Romaña, arXiv:2606.16498v1, Definition 2.1. Random topological entropy uses their sample Bowen separated sets (Section 4.1). All asymptotic statements are for almost every Bernoulli sequence; the integer \(m\) is fixed before the limit in time.

## Proof
**1. Lift geometry and integrability.** Both affine formulas agree at \(1/2\), where \(B_m(1/2)=1/2+m\); the endpoint values are \(B_m(0)=0\) and \(B_m(1)=1\). Therefore the periodic extension is continuous and degree one. Moreover,
\[
0\le B_m(x)-x\le m\quad(x\in\mathbb R),
\qquad B_m(0)=0,\quad B_m(1/2)=1/2+m.
\]
Hence \(\sup_x|F^{[m]}_\omega(x)-x|\) equals \(0\) on zero symbols and \(m\) on unit symbols. Its expectation is exactly \(m/m=1\), uniformly in \(m\). All hypotheses of the integrable-lift random rotation theorem in the cited paper are satisfied.

**2. Exact random rotation interval.** Put \(N_n(\omega)=\sum_{j=0}^{n-1}\omega_j\). Since the identity commutes with \(B_m\), for every \(x\in\mathbb R\) and every \(n\ge0\),
\[
F^{[m],(n)}_\omega(x)=B_m^{N_n(\omega)}(x).
\]
Every active iterate changes its lifted coordinate by a number in \([0,m]\), and inactive iterates do nothing. Thus
\[
0\le\frac{F^{[m],(n)}_\omega(x)-x}{n}\le\frac{mN_n(\omega)}n.
\]
The Bernoulli strong law gives \(N_n/n\to1/m\). Both endpoints occur as genuine ordinary limits for the fixed points \(x=0\) and \(x=1/2\) modulo the circle: the first has zero lift displacement and, by degree-one equivariance, \(B_m^k(1/2)=1/2+km\). Hence their rotation limits are \(0\) and \(1\), respectively. Li–Lloyd–Romaña Theorem 2.1 independently establishes that the full random rotation set is a compact interval on a common full-measure set. Its containment in \([0,1]\) and the two attained endpoints force equality, with the ordinary rotation values filling the interval.

**3. Exact Bernoulli time-thinning law for entropy.** Write \(d_k^{(m)}(x,y)=\max_{0\le j<k}d_{\mathbb T}(f_m^j(x),f_m^j(y))\) and \(d_{n,\omega}(x,y)=\max_{0\le j<n}d_{\mathbb T}(f^{[m],(j)}_\omega(x),f^{[m],(j)}_\omega(y))\). The nondecreasing sequence of activation counts \(N_j\), for \(0\le j<n\), visits **every integer** from \(0\) through \(N_{n-1}\). Consequently the two Bowen metrics satisfy the exact identity
\[
d_{n,\omega}=d_{N_{n-1}(\omega)+1}^{(m)}.
\]
Therefore at every separation scale \(\varepsilon>0\), the maximal separated-set cardinalities satisfy \(s(n,\varepsilon,\omega)=s_{f_m}(N_{n-1}+1,\varepsilon)\). Along almost every Bernoulli sequence \(N_{n-1}/n\to1/m\), and \(N_{n-1}\) takes all sufficiently large integer values. Passing to the limsup growth rates gives the exact equality of scale entropies
\[
\limsup_{n\to\infty}\frac1n\log s(n,\varepsilon,\omega)
=\frac1m\limsup_{k\to\infty}\frac1k\log s_{f_m}(k,\varepsilon).
\]
Letting \(\varepsilon\downarrow0\) proves \(h_{\mathrm{top}}^{(r)}(F^{[m]})=h_{\mathrm{top}}(f_m)/m\). The equality holds almost surely, not just in expectation.

**4. Uniformly vanishing upper bound and positive members.** The lift \(B_m\) is globally Lipschitz on \(\mathbb R\) with constant \(L_m=2m+1\), so the quotient map \(f_m\) is \(L_m\)-Lipschitz on \(\mathbb T\). For a deterministic \((k,\varepsilon)\)-separated set, partitioning the circle into at most \(1+2L_m^{k-1}/\varepsilon\) arcs of diameter smaller than \(\varepsilon/L_m^{k-1}\) shows
\[
h_{\mathrm{top}}(f_m)\le\log(2m+1).
\]
Since the random rotation interval is nondegenerate, Theorem 2.3 of Li–Lloyd–Romaña implies \(h_{\mathrm{top}}^{(r)}(F^{[m]})>0\) for every fixed \(m\). Combining with the time-thinning identity yields the asserted estimate. Finally \(\log(2m+1)/m\to0\), whereas both the interval width and expected displacement budget are exactly \(1\) throughout. Any purported positive lower bound determined solely by either of those fixed data is contradicted by this sequence of examples.

## Verification
The standalone `verify.py` script uses exact rational arithmetic to check the piecewise lift, integer equivariance, endpoint drift, and collapse of every finite Bernoulli word's orbit record to its activation-count record for \(2\le m\le6\). It also checks the strict decay of the explicit numerical upper bound for \(2\le m\le50\), which is not itself used for the limiting proof. Execute `python verify.py`; successful execution prints `FINITE_IDENTITIES_OK` and the count of finite instances. The strong law, random rotation interval, and infinite-time entropy identity are established analytically; finite experiments do not certify those limiting statements.

## Relationship to prior work
Li, Lloyd and Romaña (arXiv:2606.16498v1, 15 June 2026) prove that any nondegenerate random rotation interval gives **positive** entropy (Theorem 2.3), and Section 5 expressly distinguishes this from finding quantitative bounds in terms of recurrence of full-cover blocks. Their Example 4.1 has entropy \(\log3\) for a different, uniformly expanding two-map family. The present construction identifies an exact obstruction to a quantitative strengthening based only on rotation-interval width, **even with fixed expected lift-displacement norm**: high-displacement maps activated at reciprocal frequency preserve width while their per-step entropy vanishes. The result does not contradict positivity in each fixed system.

Alsedà–Llibre–Mañosas–Misiurewicz (1988) develop deterministic lower entropy bounds in terms of the rotation interval, which apply to the individual active map \(f_m\), not directly to its Bernoulli identity-interspersed cocycle. A published note on Bernoulli rotation singleton graphs treats simultaneous zero-entropy invariant sections, not the global relative entropy/interval-width comparison used here. The exact cocycle time-thinning identity is an elementary feature of identity insertion; the claimed contribution is the combined fixed-width and fixed-integrability counterexample, not the time-change identity by itself.

## Limitations
The counterexample is within iid two-map measurable random circle dynamics. Its nonidentity Lipschitz constant and peak one-step lift displacement both increase with \(m\); the theorem **does not** exclude an entropy lower bound under a uniform almost-sure Lipschitz or displacement bound, nor under a positive uniform recurrence constraint. The quantitative entropy estimate is an upper bound, not an exact closed form for \(h_{\mathrm{top}}(f_m)\). Strict positivity uses a published theorem, whereas the counterexample's vanishing upper bound is self-contained. No independent validation or universal literature-priority certification is asserted.

## References
1. Z. Li, S. Lloyd and S. Romaña, *Rotation Sets and Topological Entropy for Random Circle Endomorphisms*, arXiv:2606.16498v1 (15 June 2026), Theorems 2.1 and 2.3, Section 4.1 and Section 5. https://arxiv.org/abs/2606.16498
2. L. Alsedà, J. Llibre, F. Mañosas and M. Misiurewicz, *Lower bounds of the topological entropy for continuous maps of the circle of degree one*, Nonlinearity 1 (1988), 463–479. DOI: 10.1088/0951-7715/1/3/004.
