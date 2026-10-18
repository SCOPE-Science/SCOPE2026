# Equal-width interval diffraction reduces exactly to finite point-set homometry

## Finding
Let \(w>0\), let \(m\geq1\) be an integer, and let \(A=\{a_1<\cdots<a_m\}\subset\mathbb R\) satisfy \(a_{j+1}>a_j+w\). Write \(E_A=\bigcup_{a\in A}[a,a+w]\), and use the Fourier transform \(\widehat h(\xi)=\int_{\mathbb R}h(t)e^{-2\pi i\xi t}\,dt\). For finite point sets define the *oriented difference measure*
\[
D_A=\sum_{a,a'\in A}\delta_{a-a'}.
\]

**Exact fiber theorem.** Among **all** nonempty finite unions \(G\subset\mathbb R\) of bounded intervals with positive length and mutually disjoint interiors (no restriction on the number or lengths of the competing intervals), the equality
\[
|\widehat{\mathbf1_G}(\xi)|=|\widehat{\mathbf1_{E_A}}(\xi)|\quad\text{for every }\xi\in\mathbb R
\]
holds **if and only if** there exists a finite point set \(B\subset\mathbb R\) with exactly \(m\) points, successive gaps strictly greater than \(w\), and \(D_B=D_A\), such that \(G=\bigcup_{b\in B}[b,b+w]\) up to null sets. In particular the data force every competing interval to have length \(w\), and force the interval count \(m\), without assuming either fact for the competitor.

**Three-interval consequence.** Every union of three equal-length, positively separated intervals is uniquely recovered up to translation and reflection among arbitrary finite interval unions, **regardless of how small the intervening gaps are**. Conversely the six-point homometric configurations \(A=\{0,1,4,10,12,17\}\) and \(B=\{0,1,8,11,13,17\}\) yield inequivalent six-interval unions with identical Fourier magnitudes for any \(0<w<1\). This explicit six-point example appears already in Xia and Xu (2026, Remark 6.3); it is not a new counterexample.

## Assumptions and scope
Intervals are interpreted as indicator functions up to sets of Lebesgue measure zero. Their endpoints may be arbitrary real numbers, with no rationality or commensurability hypothesis. In a competing union, merge any components that touch, so each listed component is a maximal positive-length interval and neighboring components have positive gaps. The target must consist of equal-width positive intervals with positive gaps, but there is **no** assumption that pairwise difference intervals are separated; the claim does not require collision-free point differences. Fourier modulus agreement is exact at all real frequencies.

## Proof
**1. Autocorrelation and the component count.** For a finite union \(H\) of \(r\) maximal closed intervals of positive lengths with positive gaps, let \(C_H(t)=\int\mathbf1_H(x)\mathbf1_H(x-t)\,dx\). For all sufficiently small \(t>0\), smaller than every component length and every positive intercomponent gap, its self-overlap has exactly \(r\) contributions, while distinct components cannot overlap after shifting by \(t\). Thus
\[
C_H(t)=|H|-rt.
\]
The transform of \(C_H\) is \(|\widehat{\mathbf1_H}|^2\), so equal Fourier magnitudes give equal autocorrelations and therefore the same number of maximal components. In particular any competitor has exactly \(m\) maximal components; also \(|G|=|E_A|=mw\) follows from the Fourier transform at zero.

**2. Arithmetic zeros force a finite integer deconvolution.** Put \(g=\mathbf1_G\), and take its distributional derivative, the finite signed endpoint measure \(\mu=Dg=\sum_{i}(\delta_{\ell_i}-\delta_{r_i})\). With \(h_w=\mathbf1_{[0,w]}\), the target factors as \(\mathbf1_{E_A}=h_w*\sum_{a\in A}\delta_a\); therefore its Fourier transform vanishes at every nonzero \(\xi=n/w\), \(n\in\mathbb Z\). The same is true for \(\widehat g\); hence \(\widehat\mu(n/w)=2\pi i(n/w)\widehat g(n/w)=0\) for all nonzero \(n\). At \(n=0\) this also holds because \(\mu(\mathbb R)=0\).

Push \(\mu\) forward to the circle \(\mathbb R/w\mathbb Z\). Every Fourier coefficient of this finite signed measure is zero, so uniqueness of Fourier coefficients of finite measures implies the pushforward is the zero measure. Equivalently, on **each** residue class \(r+w\mathbb Z\), the total signed endpoint mass is zero. Write the signed endpoint coefficients in that class as \(\mu_k\) at \(r+kw\), for \(k\in\mathbb Z\). The finite-support integer sequence
\[
c_k=\sum_{j\le k}\mu_j
\]
is well-defined and eventually zero at both ends, and satisfies \(\mu_k=c_k-c_{k-1}\). Combining the finitely many endpoint residue classes produces a finite integer atomic measure \(\nu=\sum_{t\in S}c_t\delta_t\), with distinct support points \(t\) and nonzero integers \(c_t\), such that
\[
\mu=(\delta_0-\delta_w)*\nu.
\]
As \(D(h_w*\nu)=(\delta_0-\delta_w)*\nu=Dg\) and both \(h_w*\nu\) and \(g\) are compactly supported, their difference has zero distributional derivative and must vanish: \(g=h_w*\nu\) almost everywhere. This step does **not** assume that the competing endpoint lengths are multiples of \(w\).

**3. Positivity upgrades integer atoms to point masses.** Since \(\widehat g=\widehat h_w\,\widehat\nu\) and \(\widehat{\mathbf1_{E_A}}=\widehat h_w\,\sum_{a\in A}e^{-2\pi ia\xi}\), cancellation wherever \(\widehat h_w\ne0\), followed by continuity across its isolated zeros, yields
\[
\left|\sum_{t\in S}c_te^{-2\pi it\xi}\right|=
\left|\sum_{a\in A}e^{-2\pi ia\xi}\right|\qquad(\xi\in\mathbb R).
\]
At frequency zero, positivity of the interval indicator gives \(\sum c_t=\widehat g(0)/w=m\). On the other hand, averaging the squares of these finite exponential polynomials over \([-R,R]\), dividing by \(2R\), and letting \(R\to\infty\) annihilates every cross term between distinct frequencies: their averages are bounded by \(1/(2\pi R|t-t'|)\). It follows that \(\sum c_t^2=m\). Therefore
\[
0=\sum_{t\in S}(c_t^2-c_t)=\sum_{t\in S}c_t(c_t-1).
\]
Each summand is a nonnegative integer, so \(c_t\in\{0,1\}\) for every \(t\). After removing zero coefficients, \(\nu=\sum_{b\in B}\delta_b\) for exactly \(m\) distinct points. Consequently \(g=\sum_{b\in B}\mathbf1_{[b,b+w]}\) almost everywhere. Because \(g\) is \(0\)-\(1\) valued, these windows cannot overlap in sets of positive measure. If two touched at endpoints, they would merge to a maximal component, reducing the number of maximal components below \(m\); Step 1 rules this out. Thus successive starts are separated strictly by more than \(w\).

**4. Exact homometry and converse.** Squaring the canceled exponential equality gives
\[
\sum_{b,b'\in B}e^{-2\pi i(b-b')\xi}=
\sum_{a,a'\in A}e^{-2\pi i(a-a')\xi}\quad(\xi\in\mathbb R).
\]
By uniqueness of the Fourier transform of a finite measure (equivalently, linear independence of distinct real-frequency exponentials), \(D_B=D_A\). Conversely, if \(B\) is any \(m\)-point set with pairwise separated \(w\)-windows and \(D_B=D_A\), then the last identity and the common factor \(\widehat h_w\) imply equal Fourier moduli of their interval unions. This proves the if-and-only-if statement.

**5. Three points and the six-point boundary.** For three ordered starts, translation makes them \(\{0,u,u+v\}\) with \(u,v>w\). Their positive pairwise difference multiset is \(\{u,v,u+v\}\): its largest member determines \(u+v\), and the two others determine the unordered pair \(\{u,v\}\). Interchanging \(u,v\) is exactly reflection plus translation. This gives universal three-interval uniqueness. The two displayed six-point sets have the same difference multiset (directly checked), and no translation or reflection identifies them, yielding the stated nonuniqueness. Their interval construction is credited to the motivating paper.

## Verification
The accompanying standalone Python checker uses exact integer endpoint autocorrelation coefficients (not floating-point FFTs). With interval endpoints constrained to integers in a finite search window, it compares all three-unit-window targets against every candidate finite interval union of total length three, allowing arbitrary positive integer component lengths. All equal-autocorrelation candidates have exactly three unit windows and differ from the target only by translation or reflection. It also verifies the published six-point homometric pair by exact oriented difference counts and signed endpoint autocorrelation. Run \(\texttt{python verify.py}\). The finite test is an independent consistency check; all unbounded real-parameter and arbitrary-interval conclusions are proved above.

## Relationship to prior work
Xia and Xu (2026, Theorems 1.2 and 1.7) prove global uniqueness for at most two unrestricted intervals and exhibit nonuniqueness for every interval count at least three. Their Theorem 6.2 instead imposes a strong **separation condition** on the difference intervals, excluding six intervals; their Remark 6.3 already contains the six-point equal-width ambiguity used here. The present result provides an **exact fiber characterization** for any number of equal-width target intervals **without their separation condition**, and without imposing equal width or component count on competing interval unions. In particular it proves unrestricted-competitor uniqueness for three equal-width intervals, despite unrestricted three-interval nonuniqueness.

Crimmins and Fienup (1983) treat functions confined to sufficiently separated support bands, with conclusions conditional on separation and, in important formulations, the allowed support of competitors. Those hypotheses do not supply this global equal-width rigidity for arbitrarily small gaps. The classical homometric/turnpike literature concerns reconstruction of finite point sets *once the point-distance measure is known*. The additional step here is proving that an arbitrary interval-indicator competitor **must** share the target's interval width and has an integer, then \(0\)-\(1\), point-measure quotient. This is not a general phase-retrieval theorem for arbitrary signals.

## Limitations
The result is exact, noiseless, and specific to nonnegative \(0\)-\(1\) indicators of finite unions of intervals. It does not assert stable recovery under noisy Fourier magnitudes or characterize homometric finite point sets of arbitrary cardinality. The six-point ambiguity is not new; no claim of historical priority over unindexed work is made. The argument relies on full continuous Fourier-magnitude data and cannot be inferred from a finite set of samples. Independent validation has not been performed.

## References
1. Yu Xia and Zhiqiang Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855v1 (first posted 2026-06-18), especially Theorems 1.2, 1.7, 6.2 and Remark 6.3. https://arxiv.org/abs/2606.19855
2. T. R. Crimmins and J. R. Fienup, *Uniqueness of phase retrieval for functions with sufficiently disconnected support*, Journal of the Optical Society of America 73 (1983), 218–221. https://doi.org/10.1364/JOSA.73.000218
3. A. Bekir and S. W. Golomb, *There Are No Further Counterexamples to S. Piccard's Theorem*, IEEE Transactions on Information Theory 53 (2007), 2864–2867. https://doi.org/10.1109/TIT.2007.899468
