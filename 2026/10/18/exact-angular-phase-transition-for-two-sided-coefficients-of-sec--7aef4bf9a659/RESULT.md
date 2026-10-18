# Exact angular phase transition for two-sided coefficients of sector-valued harmonic Hardy functions

## Finding
Let \(0\le\beta\le\pi/2\), let \(n\ge1\) be an integer, and define the closed convex sector
\[\mathcal C_\beta=\{0\}\cup\{re^{i\phi}:r>0,\ |\phi|\le\beta\}.\]
For every nonzero complex harmonic map \(f=h+\overline{k}\) on \(\mathbb D\) with \(k(0)=0\), values in \(\mathcal C_\beta\), and finite harmonic Hardy norm \(\|f\|_{h^2}\), write \(h(z)=\sum_{j\ge0}a_jz^j\) and \(k(z)=\sum_{j\ge1}b_jz^j\). Then the exact sharp constant is
\[
\sup_{f\ne0}\frac{|a_n|+|b_n|}{\|f\|_{h^2}}
=\begin{cases}1,&0\le\beta\le\pi/4,\\\sqrt2\sin\beta,&\pi/4\le\beta\le\pi/2.\end{cases}
\]
The equality traces undergo a sharp geometry change at \(\beta=\pi/4\): below the threshold every extremal boundary trace occupies a single positive cosine half-wave; above it every extremal trace occupies both half-waves with opposite edge phases. At the threshold a continuous one-parameter family of distinct optimizer geometries connects these types. The constant and classification are independent of \(n\).

## Assumptions and scope
The normalized angular measure is \(dm(t)=dt/(2\pi)\); \(\|f\|_{h^2}^2=\sup_{0<r<1}\int_0^{2\pi}|f(re^{it})|^2dm(t)\). All values of the map, not merely a finite set of its values, lie in the closed sector. Since \(\mathcal C_\beta\) is convex and closed, its boundary trace \(g=f^*\in L^2(\mathbb T)\) lies in \(\mathcal C_\beta\) almost everywhere; conversely any such \(g\) yields an admissible harmonic Poisson extension with \(\|f\|_{h^2}=\|g\|_2\). The Fourier formulas are \(a_n=\int g(t)e^{-int}\,dm(t)\) and \(\overline{b_n}=\int g(t)e^{int}\,dm(t)\).

Let \(P_\beta:\mathbb C\to\mathcal C_\beta\) be the Euclidean metric projection. The *complete equality classification* is as follows: a nonzero map is extremal if and only if its boundary trace, up to equality almost everywhere, is
\[
 g(t)=cP_\beta\!\left(2e^{-i\tau}\cos(nt+\delta)\right),\qquad c>0,\quad\delta\in\mathbb R,
\]
where, modulo the simultaneous replacement \((\tau,\delta)\mapsto(\tau+\pi,\delta+\pi)\), the permitted \(\tau\in[-\pi/2,\pi/2]\) are
\[
\begin{cases}
|\tau|\le\beta,&0\le\beta<\pi/4,\\
|\tau|\le\pi/2,&\beta=\pi/4,\\
|\tau|=\pi/2,&\pi/4<\beta\le\pi/2.
\end{cases}
\]
For \(\beta<\pi/4\), this is equivalently \(g(t)=c'e^{i\sigma}(\cos(nt+\delta))_+\), with \(c'>0\) and \(|\sigma|\le\beta\). For \(\beta>\pi/4\), it is equivalently
\[g(t)=c'\left[e^{-i\beta}(\cos(nt+\delta))_++e^{i\beta}(-\cos(nt+\delta))_+\right],\qquad c'>0.\]
Here \((u)_+=\max(u,0)\). All these traces are bounded, and hence define genuine harmonic functions of the indicated class.

## Proof
**Step 1: exact coefficient duality.** Let \(g\) be the boundary trace and \(Q_n(g)=|a_n|+|b_n|\). Choosing phases independently for the two complex Fourier coefficients gives
\[
Q_n(g)=\max_{\tau,\delta\in\mathbb R}\operatorname{Re}\int_0^{2\pi}2e^{i\tau}\cos(nt+\delta)\,g(t)\,dm(t).
\]
The phase pairs in the two coefficient dualizations parametrize all \((\tau,\delta)\) because a sum of two unit complex exponentials with frequencies \(\pm n\) equals \(2e^{i\tau}\cos(nt+\delta)\) after reparametrization.

**Step 2: sector projection is the exact dual.** Put \(K_{\tau,\delta}(t)=2e^{-i\tau}\cos(nt+\delta)\). For any \(g(t)\in\mathcal C_\beta\), the orthogonal-projection characterization of a closed convex cone gives
\[
\operatorname{Re}\left(\overline{K_{\tau,\delta}(t)}g(t)\right)
\le\operatorname{Re}\left(\overline{P_\beta(K_{\tau,\delta}(t))}g(t)\right).
\]
Integration and Cauchy--Schwarz yield \(Q_n(g)\le\|g\|_2\max_\tau\|P_\beta(K_{\tau,\delta})\|_2\). Equality for a fixed maximizing \(\tau,\delta\) is attained by \(g=cP_\beta(K_{\tau,\delta})\), since \(\operatorname{Re}\big(\overline{K-P_\beta(K)}P_\beta(K)\big)=0\) pointwise. Cauchy--Schwarz also proves these are the only equality traces.

**Step 3: the two cosine half-waves.** By reflection and the redundancy \((\tau,\delta)\sim(\tau+\pi,\delta+\pi)\), it suffices to take \(0\le\tau\le\pi/2\). Let \(u\) and \(v\) be the angular projection factors on the positive and negative cosine half-waves. Elementary nearest-angle geometry gives
\[
u_\beta(\tau)=\begin{cases}1,&\tau\le\beta,\\\cos(\tau-\beta),&\tau\ge\beta,\end{cases}
\qquad
v_\beta(\tau)=\begin{cases}0,&\tau+\beta\le\pi/2,\\-\cos(\tau+\beta),&\tau+\beta\ge\pi/2.\end{cases}
\]
The positive and negative cosine half-waves each carry exactly one quarter of the normalized \(L^2\) cosine-square mass, for every integer \(n\). Hence
\[\|P_\beta(K_{\tau,\delta})\|_2^2=u_\beta(\tau)^2+v_\beta(\tau)^2,\]
independent of \(\delta\) and \(n\).

**Step 4: exact phase maximum.** Where both projection factors are nontrivial, the identity
\[
\cos^2(\tau-\beta)+\cos^2(\tau+\beta)
=1+\cos(2\tau)\cos(2\beta)
\]
shows the change at \(\beta=\pi/4\). For \(\beta<\pi/4\), \(u^2+v^2\le1\), with equality exactly for \(0\le\tau\le\beta\). For \(\beta>\pi/4\), \(u^2+v^2\le2\sin^2\beta\), with equality only at \(\tau=\pi/2\); this also follows directly on the intervening interval where \(u=1\) and \(v>0\) by comparing \(1+\cos^2(2\beta)\le1-\cos(2\beta)\). At \(\beta=\pi/4\), the squared projection norm equals one at every \(0\le\tau\le\pi/2\), and nowhere larger. Restoring the negative phases proves the exact constants and permitted phase sets.

**Step 5: equality and admissibility.** Strict equality conditions in the Hilbert-space Cauchy--Schwarz step force \(g\) to be a positive real multiple of the projected dual kernel. The preceding maximizer classification is exhaustive. Every resulting \(g\) belongs to \(L^2(\mathbb T)\cap L^\infty(\mathbb T)\) and takes its values in \(\mathcal C_\beta\); its Poisson extension stays in the closed convex sector. Thus every listed equality case is realized, including the critical continuous family and both endpoints.

## Verification
The standalone standard-library program `verify_sector.py` evaluates finite Fourier sums of explicit equality traces for \(n=1,3,7\) at sector angles below, at, and above \(\pi/4\). It additionally checks randomly generated cone-valued traces and the trigonometric identity. These are finite numerical consistency checks, not substitutes for Steps 1--5. All normalization constants, especially the half-wave mass \(1/4\), have been checked independently from \(\int_0^{2\pi}\cos^2(nt+\delta)\,dm=1/2\).

## Relationship to prior work
Chen, Huang, Jin and Li establish the unrestricted sharp harmonic Hardy coefficient constant for \(p\ge1\). Their \(p=2\) formula gives \(\sqrt2\); the present theorem asks a different, sector-constrained question and determines exactly when the sector already permits that unrestricted value. It adds a complete sector-dependent equality classification and the critical \(45^\circ\) optimizer bifurcation. Earlier equality classifications for unrestricted harmonic Hardy coefficients concern no sector constraint and therefore do not imply the sharp angular profile merely by specializing their hypotheses. Cone projection and elementary Fourier duality are classical; neither is claimed as new in isolation.

## Limitations
Only the Hilbert exponent \(p=2\), one two-sided coefficient pair at a time, and sector half-angles \(0\le\beta\le\pi/2\) are covered. A numerical trace test is not a proof of the universal coefficient bound. The result does not imply that the same sharp profile holds in non-Hilbert harmonic Hardy spaces or for simultaneous coefficient constraints. Historical originality has not been independently audited.

## References
1. S. Chen, M. Huang, L. Jin and Q. Li, *Sharp constant problems for harmonic mappings*, arXiv:2609.33159v1, first publicly posted September 27, 2026, Theorem 1.3 and proof, pp. 4--5 and 9--14. The author's classification is Primary MSC2020 31A05.
2. Classical Hilbert-space metric projection onto closed convex cones, Cauchy--Schwarz inequality, and Fourier--Poisson representation for harmonic \(h^2\) functions. These standard ingredients are proved or specialized above as needed.
