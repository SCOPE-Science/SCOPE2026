# Sharp mass-only antipodal coalescence threshold for weighted Bergman boundary poles

## Finding
Fix an integer \(m\ge2\), an exponent \(\alpha>0\), a distinguished residue \(q>0\), and arbitrary light residues \(b_1,\ldots,b_m>0\). Put \(W=\sum_{j=1}^m b_j\). For boundary sites \(\zeta_j\in\mathbb T=\{z\in\mathbb C:|z|=1\}\), allow coincidences and form the rational function
\[
F_{\boldsymbol\zeta}(z)=\frac{q}{z-1}+\sum_{j=1}^m\frac{b_j}{z-\zeta_j},\qquad |z|<1.
\]
With the normalized weighted Bergman norm
\[
\|F\|_{\alpha}^{2}=\frac{\alpha+1}{\pi}\int_{|z|<1}|F(z)|^2(1-|z|^2)^\alpha\,dA(z),
\]
the configuration with *all light sites at the antipode* \(\zeta_1=\cdots=\zeta_m=-1\) is the **unique global minimizer** if and only if \(\alpha>2\) and
\[
q\ge q_*(\alpha,W)=\frac{W\alpha}{(\alpha-1)(\alpha-2)J_\alpha},\quad
J_\alpha=\int_0^1\frac{(1-t)^{\alpha+1}}{(1+t)^3}\,dt.
\]
For \(\alpha>2\) and \(q<q_*\), it has a strictly negative second variation. For \(0<\alpha\le2\), no global minimizing configuration has **any coincident positive-residue poles**, including collisions with the distinguished pole. Thus the coalescence threshold is controlled solely by the *total light residue* \(W\); the individual weights and number of light sites do not otherwise enter it.

For example, at \(\alpha=3\),
\[
\frac{q_*}{W}=\frac{6}{96\log2-66}\approx11.06746974646.
\]
The threshold diverges as \(\alpha\downarrow2\) and satisfies \(q_*/W\to1\) as \(\alpha\to\infty\).

## Assumptions and scope
All residues are strictly positive, \(m\ge2\), and the heavy pole is fixed at \(1\) by rotation. The unit disk area measure \(dA\) is ordinary Euclidean area; normalization makes the constant function have squared norm \(1\). Sites on the unit circle are free, and coincident sites represent added residues, not excluded configurations. Every such rational function belongs to the weighted space when \(\alpha>0\). The theorem optimizes the full Hilbert-space norm, not an unweighted area \(L^1\) electrostatic field or an operator commutator. Uniqueness is literal with the distinguished pole fixed and the positive light residues individually labeled (there is no nontrivial residual optimizer orbit).

## Proof
**1. Exact pair interaction.** Expanding \(1/(z-a)=-\sum_{k\ge1}a^{-k}z^{k-1}\) for \(|a|=1\), orthogonality of disk monomials gives
\[
\|F_{\boldsymbol\zeta}\|_\alpha^2
=\sum_{k\ge1}c_{\alpha,k}\left|q+\sum_j b_j\zeta_j^{-k}\right|^2,
\quad c_{\alpha,k}=(\alpha+1)\int_0^1t^{k-1}(1-t)^\alpha\,dt
=\frac{\Gamma(\alpha+2)\Gamma(k)}{\Gamma(k+\alpha+1)}.
\]
As \(c_{\alpha,k}=O(k^{-\alpha-1})\), all relevant Fourier sums converge absolutely and uniformly. Define the real pair potential, using the Chebyshev polynomial \(T_k(\cos\theta)=\cos(k\theta)\), by
\[
H_\alpha(u)=\sum_{k\ge1}c_{\alpha,k}T_k(u)
=(\alpha+1)\int_0^1\frac{(1-t)^\alpha(u-t)}{1-2tu+t^2}\,dt,\quad -1\le u\le1.
\]
The squared norm equals a configuration-independent self-energy plus \(2E\), where
\[
E=q\sum_j b_jH_\alpha(\operatorname{Re}\zeta_j)
+\sum_{i<j}b_ib_jH_\alpha(\operatorname{Re}(\zeta_i\overline{\zeta_j})).
\]
The integral representation follows by summing \(\sum_{k\ge1}t^{k-1}\cos(k\theta)=(\cos\theta-t)/(1-2t\cos\theta+t^2)\) before integration.

**2. Strict convexity and the regularity boundary.** Differentiating the integral for \(-1<u<1\) yields
\[
H_\alpha'(u)=(\alpha+1)\int_0^1
\frac{(1-t)^\alpha(1-t^2)}{(1-2tu+t^2)^2}\,dt>0,
\]
\[
H_\alpha''(u)=4(\alpha+1)\int_0^1
\frac{t(1-t)^\alpha(1-t^2)}{(1-2tu+t^2)^3}\,dt>0.
\]
These formulas establish strict convexity. The one-sided endpoint slopes are
\[
h_-:=H_\alpha'(-1)=(\alpha+1)J_\alpha>0,
\quad h_+:=H_\alpha'(1-)=
\begin{cases}
\dfrac{\alpha(\alpha+1)}{(\alpha-1)(\alpha-2)},&\alpha>2,\\
+\infty,&0<\alpha\le2.
\end{cases}
\]
The expression for \(h_+\) is obtained by integrating \((\alpha+1)(1+t)(1-t)^{\alpha-3}\). In particular, \(H_\alpha\) is continuous at both endpoints but has an infinite right-endpoint slope when \(\alpha\le2\).

**3. Global sufficiency when \(\alpha>2\).** Write \(E_0\) for the energy of \(\zeta_j=-1\). Strict convexity with finite endpoint slopes gives the valid supporting-tangent estimates
\[
H_\alpha(u)-H_\alpha(-1)\ge h_-(u+1),\quad
H_\alpha(v)-H_\alpha(1)\ge h_+(v-1).
\]
Their inequalities are strict whenever the respective arguments differ from the tangency endpoints. Set \(S=\sum_j b_j(1+\operatorname{Re}\zeta_j)\). The exact weighted chord-variance identity is
\[
\sum_{i<j}b_ib_j(1-\operatorname{Re}(\zeta_i\overline{\zeta_j}))
=WS-\tfrac12\left|\sum_jb_j(\zeta_j+1)\right|^2.
\]
Consequently
\[
\boxed{\quad E-E_0\ge(qh_--Wh_+)S
+\frac{h_+}{2}\left|\sum_jb_j(\zeta_j+1)\right|^2.\quad}
\]
If \(q\ge Wh_+/h_-\), both terms on the right are nonnegative. If any light site differs from \(-1\), the first tangency inequality is strict for that site, giving \(E>E_0\) even at equality in the mass threshold. This proves both global optimality and uniqueness.

**4. Necessity when \(\alpha>2\).** Because \(m\ge2\) and all \(b_j>0\), there are real numbers \(s_j\), not all zero, with \(\sum_j b_js_j=0\). Put \(\zeta_j(\varepsilon)=-e^{i\varepsilon s_j}\). The identities
\[
\operatorname{Re}\zeta_j=-1+\tfrac12\varepsilon^2s_j^2+O(\varepsilon^4),\quad
\operatorname{Re}(\zeta_i\overline{\zeta_j})=1-\tfrac12\varepsilon^2(s_i-s_j)^2+O(\varepsilon^4)
\]
and \(\sum_{i<j}b_ib_j(s_i-s_j)^2=W\sum_jb_js_j^2\) imply
\[
E(\varepsilon)-E_0=\tfrac12\varepsilon^2(qh_--Wh_+)\sum_jb_js_j^2+o(\varepsilon^2).
\]
This is strictly negative for sufficiently small nonzero \(\varepsilon\) whenever \(q<Wh_+/h_-\). Thus the stated condition is necessary.

**5. Collision exclusion for \(0<\alpha\le2\).** Since \(h_+=+\infty\), convexity and continuity imply
\[
\frac{H_\alpha(1)-H_\alpha(1-\delta)}{\delta}\longrightarrow+\infty
\quad(\delta\downarrow0).
\]
If at least two light poles coincide at \(\omega\), choose their infinitesimal angular velocities with weighted sum zero, leaving all other sites fixed. Every interaction with a pole outside this collision group has zero linear variation and an \(O(\varepsilon^2)\) remainder, since its inner product is strictly less than \(1\) and the kernel is smooth there. Inside the colliding group, some pair separates by angle comparable to \(|\varepsilon|\), decreasing the energy by an amount whose ratio to \(\varepsilon^2\) diverges. Hence the collision cannot minimize. If a light pole coincides with the fixed heavy pole at \(1\), move that light pole alone with the angular sign chosen so the linear contribution of external noncoincident poles is nonpositive; their remaining variation is \(O(\varepsilon^2)\). All interactions with remaining poles in the collision group can only decrease by the same cusp mechanism. Thus a heavy-light collision is also not minimal. Compactness of the configuration torus gives existence of global minimizers, so all of them are collision-free. In particular, an all-light antipodal collision can never be optimal when \(\alpha\le2\).

**6. Endpoint examples and limits.** Direct integration at \(\alpha=3\) yields \(h_+=6\) and \(h_-=96\log2-66\), giving the displayed threshold. As \(\alpha\downarrow2\), \(J_\alpha\to J_2=6\log2-4>0\), and
\[
\frac{q_*}{W}\sim \frac{2}{(6\log2-4)(\alpha-2)}.
\]
As \(\alpha\to\infty\), beta-integral concentration near \(t=0\) gives \((\alpha+1)J_\alpha\to1\), while \(h_+\to1\), hence \(q_*/W\to1\).

## Verification
A standalone Python checker `verify.py` reconstructs the \(\alpha=3\) endpoint integral symbolically, compares the pair-potential integral against an independent truncated Fourier representation, verifies the quantitative lower bound for diverse positive residue vectors and random sites in the regular regime, and confirms negative second variations just below threshold. It reports `VERIFY_OK 381 energy and Fourier comparisons; alpha3 critical mass ratio = 11.067469746461578` when executed with Python, NumPy, and SymPy. These calculations are supplementary; finite tests do not establish the universal claims, which follow from the analytic steps above.

## Relationship to prior work
Corbett's 2026 treatment of Chui's conjecture establishes equally spaced minimizers for equal positive boundary residues, including the relevant power weights for every \(\alpha>0\), and derives strict complete monotonicity of the pair potential [1]. Abakumov, Borichev, and Fedorovskiy developed the original weighted Bergman setting and its equal-residue minimization [2]. Doubtsov, Tselishchev, and Vasilyev treat arbitrary positive charges for a distinct \(L^1\) field lower-bound problem [3]. Bezrukov's recent generalized Chui preprint concerns broader radial \(L^p\) norms, but only its accessible abstract was reviewed [4]. None of the inspected substantive results gives the present residue-dependent antipodal coalescence criterion, its sharp global sufficiency, or its mass-only threshold. The convexity of the pair potential itself is a known input; the weighted chord-variance comparison and sharp collapse transition are the claimed contribution.

## Limitations
The coalescence criterion is specific to a single distinguished pole and an all-light antipodal cluster; it does not classify all minimizers below the threshold in the regular regime. All residues must be positive and the underlying norm must be quadratic. A plausible generalized preprint was accessible only by abstract, and a broader historical-priority gap remains possible; absence of a search hit is not proof of priority. No independent scientific audit has been performed.

## References
[1] Georgia Corbett, *Two new proofs of Chui's Conjecture in Weighted Bergman Spaces*, arXiv:2609.21121, first posted 2026-09-17. https://arxiv.org/abs/2609.21121

[2] E. Abakumov, A. Borichev, K. Fedorovskiy, *Chui's conjecture in Bergman spaces*, arXiv:2009.01898, first posted 2020-09-04. https://arxiv.org/abs/2009.01898

[3] E. Doubtsov, A. Tselishchev, A. Vasilyev, *Weighted Chui's conjecture*, arXiv:2603.05233, first posted 2026-03-05. https://arxiv.org/abs/2603.05233

[4] *Proof of the generalized Chui conjecture*, arXiv:2609.03134, first posted 2026-09-02. https://arxiv.org/abs/2609.03134
