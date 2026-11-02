# Arbitrary point-to-continuous spectral thresholds for binary-branching tree shifts

## Finding
Fix any \(1<r<\sqrt2\) and either boundary choice \(\varepsilon\in\{0,1\}\). There exists a countable rooted, leafless, spherically homogeneous tree \(T\), with every vertex at level \(n\) having \(d_n\in\{1,2\}\) children, such that both symbols occur in arbitrarily long consecutive runs and the *unweighted backward shift* \(S\) on complex \(\ell^2(V(T))\) satisfies
\[
\sigma(S)=\{\lambda:|\lambda|\le\sqrt2\},\qquad
\sigma_{\mathrm p}(S)=\{\lambda:|\lambda|<r\}\cup
\begin{cases}
\{\lambda:|\lambda|=r\},&\varepsilon=1,\\
\varnothing,&\varepsilon=0.
\end{cases}
\]
Every remaining spectral point belongs to continuous spectrum and the residual spectrum is empty. Thus the point-to-continuous transition can occur at *any* interior radius, with its boundary circle independently included or excluded from point spectrum, even when the local branching bounds and the full spectral disk are held fixed.

More generally, for **every** rooted spherically homogeneous, bounded-branching, leafless tree with \(P_0=1\) and \(P_n=\prod_{j=0}^{n-1}d_j\), the corresponding bounded backward shift obeys the exact point-spectrum test
\[
\lambda\in\sigma_{\mathrm p}(S)
\quad\Longleftrightarrow\quad
\sum_{n=0}^{\infty}\frac{|\lambda|^{2n}}{P_n}<\infty.
\]
The construction proves the inverse spectral statement, not merely the formula for one prescribed tree.

## Assumptions and scope
The Hilbert space is complex \(\ell^2\) of the vertices of a countable rooted directed tree. All vertices at level \(n\) have exactly \(d_n\) children. The backward shift is defined on standard basis vectors by \(S e_{\rm root}=0\) and \(S e_v=e_{\operatorname{par}(v)}\) at every non-root vertex; equivalently \((Sx)_v=\sum_{u\in\operatorname{Chi}(v)}x_u\). For bounded branching \(S\) is bounded. The inverse-construction tree has \(d_n\in\{1,2\}\), so \(\|S\|=\sqrt2\). Point, continuous, and residual spectra use the usual operator-theoretic definitions, with continuous spectrum corresponding to injectivity and dense non-surjective range.

## Proof
**1. An exact summability criterion.** Put \(P_n=|\{v:|v|=n\}|\). For any complex \(\lambda\), the radial prescription \(x_v=\lambda^{|v|}/P_{|v|}\) satisfies \(Sx=\lambda x\) coordinatewise and has square norm \(\sum_n|\lambda|^{2n}/P_n\). Hence convergence produces a nonzero eigenvector. Conversely, if \(Sx=\lambda x\) and \(x_v\neq0\) for a vertex \(v\) of depth \(k\), then iterating the eigen-equation gives
\[
\lambda^m x_v=\sum_{u\in\operatorname{Chi}^{\langle m\rangle}(v)}x_u.
\]
Exactly \(P_{k+m}/P_k\) vertices occur in this descendant layer. Cauchy–Schwarz implies
\[
\sum_{u\in\operatorname{Chi}^{\langle m\rangle}(v)}|x_u|^2
\ge |x_v|^2|\lambda|^{2m}\frac{P_k}{P_{k+m}}.
\]
These layers are pairwise disjoint, so their right-hand sides are summable. For \(\lambda\neq0\), this is equivalent, up to a finite prefix and a positive constant, to the announced series criterion. For \(\lambda=0\), both the series and the eigencondition hold because \(Se_{\rm root}=0\).

**2. Selecting the threshold and its endpoint.** Write \(\theta=2\log_2 r\), so \(0<\theta<1\), and choose \(a=2\varepsilon\). For all sufficiently large integers \(n\) define
\[
B(n)=\left\lfloor\theta n+a\log_2(n+2)\right\rfloor.
\]
Choose a finite initial binary word whose number of ones equals \(B(n_0)\), where \(n_0\) is sufficiently large that \(0\le B(n_0)\le n_0\) and every subsequent increment \(B(n+1)-B(n)\) is \(0\) or \(1\). Beyond \(n_0\), use these increments as the initial binary branching word \(b_j\), with \(d_j=2^{b_j}\).

For every sufficiently large integer \(k\), choose disjoint windows starting at \(M_k=2^{k^4}\), each of length
\[
L_k=\left\lceil\frac{3k}{\min(\theta,1-\theta)}\right\rceil.
\]
For large \(k\), each such window contains at least \(k\) zeros and \(k\) ones because its unmodified count of ones is \(\theta L_k+O(1)\). Permute just its symbols to put \(k\) zeros followed by \(k\) ones; retain the remaining symbols in any order. The number of ones in each window is unchanged, and therefore the cumulative count \(N(n)=\sum_{j<n}b_j\) agrees with \(B(n)\) outside windows. Within the \(k\)-th window it differs by at most \(L_k=O(k)=O((\log(n+2))^{1/4})\). Consequently,
\[
N(n)=\theta n+a\log_2(n+2)+O((\log(n+2))^{1/4}),
\quad P_n=2^{N(n)},
\]
and both branching symbols have arbitrarily long uninterrupted blocks. In particular \(N(n)/n\to\theta\).

The exact point-spectrum series from step 1 converges for \(|\lambda|<r\), and its summands fail to tend to zero for \(|\lambda|>r\). On the critical circle \(|\lambda|=r\), its summands are exactly
\[
2^{\theta n-N(n)}=(n+2)^{-a+o(1)}.
\]
When \(a=0\), the series diverges (eventually its terms exceed \((n+2)^{-1/2}\)); when \(a=2\), it converges (eventually its terms are bounded by \((n+2)^{-3/2}\)). This gives the desired endpoint choice.

**3. The entire full spectral disk.** Since each branching number is at most two, \(\|S\|\le\sqrt2\), so no complex number of modulus greater than \(\sqrt2\) belongs to its spectrum. For each positive integer \(m\), select a block of \(m+1\) consecutive levels with branching number two. At the beginning of that block, choose two children \(u_1,u_2\) of the same parent and set \(h_0=(e_{u_1}-e_{u_2})/\sqrt2\). Thus \(Sh_0=0\). Propagate \(h_j=2^{-j/2}(S^*)^j h_0\) for \(0\le j\le m\). These vectors lie in different levels, are orthonormal, and satisfy \(Sh_j=\sqrt2h_{j-1}\) for \(1\le j\le m\). Therefore, for \(|\lambda|<\sqrt2\), the nonzero vector
\[
y_m=\sum_{j=0}^m(\lambda/\sqrt2)^j h_j
\]
satisfies \(\|y_m\|\ge1\) and
\[
(S-\lambda I)y_m=-\lambda(\lambda/\sqrt2)^m h_m\longrightarrow0.
\]
Thus every \(|\lambda|<\sqrt2\) lies in approximate point spectrum, hence spectrum. Closedness of the spectrum supplies the outer circle \(|\lambda|=\sqrt2\).

**4. No residual spectrum.** For the forward shift \(S^*\), the root coordinate of \(S^*x\) is zero, and the coordinate at a child \(u\) is \(x_{\operatorname{par}(u)}\). If \(S^*x=\zeta x\) with \(\zeta\neq0\), induction from the root forces \(x=0\); if \(\zeta=0\), leaflessness again gives \(x=0\). Thus \(S^*\) has no eigenvalues and \(\operatorname{ran}(S-\lambda I)\) is dense for every \(\lambda\). Non-eigenvalues in the spectral disk therefore have continuous, not residual, spectral type.

## Verification
The included `check_spherical_shift.py` is standalone Python standard-library code. Execute it with `python check_spherical_shift.py` to check, for every branching word of length at most eight, exact finite radial eigen-equations, layer mass identities, and all supported finite wavelet telescoping identities. It also tests local count-preserving window rearrangements for three numerical densities and both boundary choices. The script reports 4,620 passing finite test cases. The infinite series classification, sparse-window estimates, and spectral closure are established by the proof above; finite tests are not substituted for these arguments.

## Relationship to prior work
Mandal and Trivedi (2025, arXiv:2508.00763v1), the motivating recent work, classify unitary equivalence of balanced tree shifts using level weights and generation cardinalities. The present operators are balanced but the question here concerns their full point/continuous spectral partition under fixed two-valued branching. Budzyński, Dymek, and Ptak (2015, arXiv:1510.03828) give general point-spectrum inclusions and regular-tree examples; their Theorem 23 and Propositions 26–27 do not furnish this arbitrary intermediate threshold with independently switchable endpoint. Budzyński, Dymek, Płaneta, and Ptak (2017, arXiv:1702.00765) prove Wold-type decompositions for balanced shifts, which is consistent with but does not itself state the inverse spectral construction. No claim of novelty is made for the elementary radial summability principle considered in isolation; the claimed contribution is the complete two-symbol inverse spectral realization with the exact spectral-type partition. Earlier reformulations in general weighted-shift or bounded-point-evaluation language remain a priority risk.

## Limitations
The inverse realization is proved only for complex \(\ell^2\), unweighted backward shifts, spherically homogeneous leafless trees, and target radii strictly between \(1\) and \(\sqrt2\). It does not classify arbitrary inhomogeneous trees, perturbations of branching weights, or all possible eigenvector multiplicities. The construction is explicit but sparsely nonperiodic, not a stationary probabilistic model. Originality is a best-knowledge comparison, not a publication-priority certificate; independent mathematical audit is not performed.

## References
1. S. Mandal and S. Trivedi, *Unitary equivalence of balanced weighted shifts on rooted directed trees*, arXiv:2508.00763v1, first public 2025-08-01, https://arxiv.org/abs/2508.00763.
2. P. Budzyński, P. Dymek, M. Ptak, *Analytic structure of weighted shifts on directed trees*, arXiv:1510.03828, https://arxiv.org/abs/1510.03828.
3. P. Budzyński, P. Dymek, A. Płaneta, M. Ptak, *Weighted shifts on directed trees: Their multiplier algebras, reflexivity and decompositions*, arXiv:1702.00765, https://arxiv.org/abs/1702.00765.
