# Sharp spectral-radius inflation for polar means of periodic weighted shifts

## Finding
Let \(n\ge 2\), \(K\ge1\), and \(0\le\lambda\le1\). A positive \(n\)-periodic weighted shift \(T\) acts on a cyclic Hilbert space \(\mathbb C^n\), or on \(\ell^2(\mathbb N_0)\), or on \(\ell^2(\mathbb Z)\), by \(Te_j=w_j e_{j+1}\), where \(w_j>0\) and \(w_{j+n}=w_j\). In the cyclic case, subscripts are reduced modulo \(n\). Let \(T=U|T|\) be its polar decomposition and
\[
M_\lambda(T)=\lambda U|T|+(1-\lambda)|T|U.
\]
If \(\max_j w_j/\min_j w_j\le K\), then the sharp universal spectral-radius comparison is
\[
\boxed{1\le \frac{r(M_\lambda(T))}{r(T)}\le
\left(1+\frac{\lambda(1-\lambda)(K-1)^2}{K}\right)^{\lfloor n/2\rfloor/n}.}
\]
For \(K>1\) and \(0<\lambda<1\), equality on the right occurs precisely when every weight belongs to \(\{a,Ka\}\) for some \(a>0\) and the number of changes between adjacent weights around the period equals \(2\lfloor n/2\rfloor\). Thus even periods require perfect alternation, whereas odd periods have exactly one equal neighboring pair. Equality on the left occurs precisely when all weights are equal. For fixed \(K>1\), optimization over \(\lambda\in[0,1]\) uniquely selects \(\lambda=1/2\), with sharp amplification
\[
\boxed{\left(\frac{K+1}{2\sqrt K}\right)^{2\lfloor n/2\rfloor/n}.}
\]
If \(K=1\), or if \(\lambda=0\) or \(1\), the ratio is identically \(1\).

## Assumptions and scope
The statements apply to the spectral radius \(r\), not operator norm or numerical radius. Positivity and periodicity are essential hypotheses of this result. The bound \(K\) is on the ratio of the largest and smallest weights in one period; the scale \(a\) is immaterial. On \(\ell^2(\mathbb N_0)\) the polar factor is the unilateral isometry, while on the bilateral or finite cyclic space it is unitary. There are no invertibility assumptions on the unilateral shift. No assertion is made for nonperiodic or sign-changing weights.

## Proof
**Step 1: reduction to geometric means.** Since \(|T|e_j=w_je_j\) and \(Ue_j=e_{j+1}\), the mean has weights \(m_j=\lambda w_j+(1-\lambda)w_{j+1}\). The \(n\)-th powers of \(T\) and \(M_\lambda(T)\) are respectively \((\prod_{j=0}^{n-1}w_j)U^n\) and \((\prod_{j=0}^{n-1}m_j)U^n\). In all three spaces \(r(U)=1\); by spectral-radius multiplicativity for powers,
\[
\frac{r(M_\lambda(T))^n}{r(T)^n}=
\prod_{j=0}^{n-1}\frac{\lambda w_j+(1-\lambda)w_{j+1}}{w_j}.
\]
Weighted arithmetic–geometric means imply \(m_j\ge w_j^\lambda w_{j+1}^{1-\lambda}\), and taking products gives the lower bound. For \(0<\lambda<1\), equality forces equality at each edge, hence a constant period.

**Step 2: strict coordinate convexity.** Normalize weights by their minimum and write \(x_j=\log w_j\) after scaling, so \(x_j\in[0,L]\), where \(L=\log K\). The logarithm of the right-hand product in Step 1 is
\[
F(x_0,\dots,x_{n-1})=\sum_{j=0}^{n-1}
\log(\lambda e^{x_j}+(1-\lambda)e^{x_{j+1}})
-\sum_{j=0}^{n-1}x_j.
\]
For \(0<\lambda<1\), with all other variables held fixed, the dependence on \(x_j\) is strictly convex: the second derivative is a sum of two strictly positive log-sum-exp second derivatives. Specifically, each term \(\log(ce^y+d)\) with \(c,d>0\) has second derivative \(cde^y/(ce^y+d)^2>0\); the analogous statement holds for \(\log(c+de^y)\). This remains true at \(n=2\). Consequently every maximizer on \([0,L]^n\) is a vertex, and therefore has \(w_j\in\{a,Ka\}\). Strict coordinate convexity also rules out any other maximizer when \(L>0\).

**Step 3: exact vertex enumeration without enumerating configurations.** On a binary periodic sequence, the number of transitions from \(a\) to \(Ka\) equals the number of reverse transitions, say \(k\). Since transitions alternate, \(0\le k\le\lfloor n/2\rfloor\). Constant edges contribute factor one to the product in Step 1. A forward and reverse transition contribute
\[
\frac{[\lambda K+(1-\lambda)]\,[\lambda+(1-\lambda)K]}{K}
=1+\frac{\lambda(1-\lambda)(K-1)^2}{K}=:\Theta.
\]
The product is exactly \(\Theta^k\). Because \(\Theta>1\) when \(K>1\) and \(0<\lambda<1\), its maximum is obtained only at \(k=\lfloor n/2\rfloor\); such binary cycles exist for every \(n\). Taking the \(n\)-th root proves the sharp upper bound and all its equality cases.

**Step 4: parameter optimization.** For \(K>1\), \(\Theta\) is strictly increasing with \(\lambda(1-\lambda)\), whose unique maximum on \([0,1]\) is at \(\lambda=1/2\). There \(\Theta=(K+1)^2/(4K)\). This proves the claimed sharp double maximum and its uniqueness in \(\lambda\). The excluded degenerate cases \(K=1\) and \(\lambda\in\{0,1\}\) give ratio one directly.

## Verification
The included `verify.py` independently checks the transition identity with exact rational arithmetic, exhaustively evaluates all binary patterns for periods \(2\le n\le 9\) at multiple positive contrast and interpolation parameters, verifies the predicted maximum and every binary maximizing pattern, and tests representative nonbinary periods. These finite checks are auxiliary: Steps 1–4 prove the theorem for every period and every real parameter in scope.

## Relationship to prior work
Lee, Lee, and Yoon established the mean transform and its weighted-shift coefficient formula (2014). Chabbabi, Curto, and Mbekhta established general spectral-radius monotonicity for mean transforms of unilateral weighted shifts and included a two-period calculation with spectral-radius increase (2018 preprint/2019 publication). Consequently neither the mere existence of inflation nor the lower inequality for the ordinary mean is claimed as new. Das, Biswas, and Nahak (first publicly posted August 15, 2026) address inequalities for the interpolating mean transform and the failure of unrestricted spectral-radius decrease. The present result instead solves the contrast-constrained *maximum inflation* problem exactly, for all periods and interpolation parameters, and classifies all extremizing weight patterns including the odd-cycle parity defect.

## Limitations
The statement is restricted to positive periodic weights and spectral radius. The full 2026 Das–Biswas–Nahak manuscript could not be inspected; its accessible public abstract does not report the sharp contrast theorem, but an equivalent statement in inaccessible material cannot be excluded. The assertion of originality is consequently subject to this specified literature-access risk. Independent mathematical audit has not been performed.

## References
- S. H. Lee, W. Y. Lee, J. Yoon, *The mean transform of bounded linear operators*, Journal of Mathematical Analysis and Applications **410** (2014); author-hosted manuscript: https://www.math.snu.ac.kr/~wylee/14JMAA.pdf.
- F. Chabbabi, R. E. Curto, M. Mbekhta, *The mean transform and the mean limit of an operator*, Proc. Amer. Math. Soc. **147** (2019), 1119–1133; https://arxiv.org/abs/1812.03499.
- B. Das, G. Biswas, C. Nahak, *Operator Inequalities and Several Characterizations of the \(\lambda\)-Mean Transform*, first arXiv posting August 15, 2026; https://arxiv.org/abs/2608.15180.
