# A monotone radial law excludes recurrent chaos in the Yang–Liu cubic flow
## Finding
Consider the four-dimensional autonomous system
\[
\dot x=yzw,\qquad
\dot y=ay-xzw,\qquad
\dot z=-bz+xyw,\qquad
\dot w=-cw+xyz.
\]
Assume \(a\ne0\), \(b>0\), and \(c>0\). Define
\[
R=x^2+y^2.
\]
Then
\[
\dot R=2x\dot x+2y\dot y=2ay^2.
\]
Thus \(R\) is monotone along every orbit, with the sign determined by \(a\), and is constant only when \(y=0\).

Every recurrent point is therefore an equilibrium point on
\[
\mathcal E=\{(x,0,0,0):x\in\mathbb R\}.
\]
Moreover, every compactly supported invariant probability measure is supported on \(\mathcal E\). Hence this vector field has no non-equilibrium compact recurrent statistical state for \(a\ne0\), \(b>0\), \(c>0\). In particular, a compact chaotic or hyperchaotic attractor in the usual invariant-measure sense is impossible in the positive-parameter regimes reported for this system.

## Assumptions and scope
The result concerns the printed Yang–Liu cubic vector field, reproduced explicitly in the later same-system study by Rech. The assumptions are \(a\ne0\), \(b>0\), and \(c>0\). They include the positive parameter values used in the reported numerical studies. No claim is made for the degenerate plane \(a=0\), where \(R\) is a first integral, or for sign changes in \(b\) or \(c\).

“Recurrent point” means a point returning arbitrarily close to itself under positive time. “Compactly supported invariant probability measure” means a Borel probability measure invariant under the flow whose support is compact. The conclusion excludes non-equilibrium compact recurrent dynamics; it does not exclude long complicated transients or unbounded trajectories.

## Proof
For any classical solution,
\[
\frac{d}{dt}(x^2+y^2)
=2x(yzw)+2y(ay-xzw)
=2ay^2.
\]
If \(a>0\), \(R\) is nondecreasing; if \(a<0\), it is nonincreasing. Let \(p\) be recurrent. There are times \(t_n\to\infty\) with \(\phi_{t_n}(p)\to p\). Continuity gives \(R(\phi_{t_n}(p))\to R(p)\). A monotone function of time that returns along a sequence to its initial value must be constant, so \(y(t)=0\) for all \(t\ge0\) on the recurrent orbit.

On such an orbit,
\[
\dot z=-bz,\qquad \dot w=-cw.
\]
Because \(b,c>0\), recurrence forces \(z=w=0\). The remaining equations give \(\dot x=\dot y=0\), so the recurrent point lies on \(\mathcal E\).

Now let \(\mu\) be any compactly supported invariant probability measure. Invariance and the generator identity give
\[
0=\int \dot R\,d\mu=2a\int y^2\,d\mu.
\]
Since \(a\ne0\), one has \(y=0\) on the support of \(\mu\). Applying invariance to \(z^2\) and \(w^2\) on that support yields
\[
0=-2b\int z^2\,d\mu,\qquad
0=-2c\int w^2\,d\mu,
\]
so \(z=w=0\) on the support. Therefore \(\operatorname{supp}\mu\subset\mathcal E\).

A compact chaotic or hyperchaotic attractor in the standard statistical sense supports a non-equilibrium invariant probability measure with recurrent typical points. The support theorem above rules this out for the stated parameter domain.

## Verification
A standalone exact polynomial checker is supplied as `verify.py`. It represents the vector field and \(R\) as multivariate polynomials over the rationals and verifies symbolically that the Lie derivative is exactly \(2ay^2\). Running it prints `VERIFY_OK`.

The measure-theoretic step uses only invariance of a compactly supported probability measure and the elementary identity \(\int Lf\,d\mu=0\) for smooth observables \(f\) on a compact invariant support. The recurrence step uses monotonicity plus the definition of recurrence.

## Relationship to prior work
Yang and Liu introduced the four-dimensional cubic system and reported hyperchaotic attractors and coexisting dynamics. A later same-system paper by Rech reproduces the vector field explicitly and summarizes the earlier parameter sweeps and routes to chaos. The inspected same-system literature discusses divergence, equilibria, Lyapunov spectra, bifurcation diagrams, and multistability, but the exact monotone identity above and its recurrence/invariant-measure consequence were not found.

Semantic searches of the published-finding corpus corpus for the system equations, title, monotone radial identities, and no-hyperchaos implications returned related structural results for other flows but no result implying this statement for the Yang–Liu system. The closest analogues involve conserved spheres, stable slaving directions, or distinct balance laws and therefore do not cover the present monotone radial obstruction.

## Limitations
The full eighteen-page Yang–Liu article was not available in the inspected lawful public material; a publisher preview and bibliographic records were available, while Rech's later paper reproduces the exact system and attributes it to Yang and Liu. This access limitation leaves a residual literature risk, although any prior theorem establishing the present monotonicity obstruction would be difficult to reconcile with the source's own compact-hyperchaos interpretation.

The theorem does not say that finite numerical traces must look simple. It allows long transients, numerical artifacts, and unbounded behavior. It also does not classify the degenerate case \(a=0\).

## References
1. J. Yang and Z. Liu, “A Novel Simple Hyperchaotic System with Two Coexisting Attractors,” *International Journal of Bifurcation and Chaos* 29 (2019), 1950203. DOI: 10.1142/S0218127419502031.
2. P. C. Rech, “Dynamics of a Four-Dimensional System with Cubic Nonlinearities,” *International Journal of Bifurcation and Chaos* 31 (2021), 2150012. DOI: 10.1142/S0218127421500127.
3. MaRDI/zbMATH bibliographic record for the Yang–Liu article, recording MSC classifications headed by 34A34.
