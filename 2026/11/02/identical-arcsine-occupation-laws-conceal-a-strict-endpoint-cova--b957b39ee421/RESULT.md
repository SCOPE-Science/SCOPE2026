# Identical arcsine occupation laws conceal a strict endpoint-covariance gap

## Finding
Let a uniform permutation of \(\{1,\ldots,2n+1\}\) generate the walk \(S_0=0\), \(S_j-S_{j-1}=1\) for an ascent and \(-1\) for a descent. Write \(N_{2n}=\sum_{j=1}^{2n}\mathbf 1\{S_{j-1}\ge0,S_j\ge0\}\) for the number of edges lying nonnegatively above zero. For \(r\ge1\), let \(A(r,d)\) be the number of permutations of \(r\) elements having \(d\) descents.

For every integer \(n\ge1\), the exact occupation–endpoint covariance is
\[
C_n:=\operatorname{Cov}(N_{2n},S_{2n})=
\sum_{k=1}^{n}\frac{4k}{(2k+1)(2k)!}
\sum_{d=0}^{k-1}(2k-1-2d)A(2k,d)>0.
\]
For an independent simple symmetric random walk \(W\) of length \(2n\), let \(\widetilde N_{2n}\) count its nonnegative edges by the same convention. Then, despite the *identical exact discrete-arcsine marginal law* of \(N_{2n}\) and \(\widetilde N_{2n}\),
\[
0<C_n<\operatorname{Cov}(\widetilde N_{2n},W_{2n})
=\sum_{k=1}^{n}\frac{(2k-1)\binom{2k-2}{k-1}}{4^{k-1}}
\quad(n\ge1).
\]
The gap is not merely a small-sample anomaly:
\[
C_n\sim\frac{4}{3\sqrt{3\pi}}n^{3/2},\qquad
\operatorname{Cov}(\widetilde N_{2n},W_{2n})\sim\frac4{3\sqrt\pi}n^{3/2}.
\]
Nevertheless, normalizing each by its own endpoint standard deviation gives the common limit
\[
\operatorname{Corr}(N_{2n},S_{2n})\longrightarrow\frac4{3\sqrt\pi}.
\]
For example, at \(n=1\), the two covariances are \(2/3\) and \(1\); at \(n=2\), they are \(8/5\) and \(5/2\).

## Assumptions and scope
All permutations are chosen uniformly, with no ties. The increments are the consecutive ascent/descent indicators, not independent signs. The variable \(N_{2n}\) counts an edge when *both* its endpoints are nonnegative, so an edge incident to the origin on its nonnegative side is included. The classical comparator has independent equiprobable \(\pm1\) increments; each model uses its *unscaled* terminal displacement. The Eulerian numbers satisfy \(A(1,0)=1\), \(A(r,d)=0\) outside \(0\le d\le r-1\), and
\[A(r+1,d)=(d+1)A(r,d)+(r+1-d)A(r,d-1).\]

## Proof
**1. The paired-edge identity.** For every walk with increments in \(\{-1,1\}\), the odd-position height \(S_{2k-1}\) is nonzero. Both edges incident to this odd-position vertex lie nonnegatively above zero if and only if \(S_{2k-1}>0\). Consequently
\[N_{2n}=2\sum_{k=1}^{n}E_k,\quad E_k=\mathbf1\{S_{2k-1}>0\}.\]
Represent the permutation by the ranks of independent continuous uniform variables \(U_1,\dots,U_{2n+1}\). Put \(D_j=\sum_{i=1}^j\mathbf1\{U_i>U_{i+1}\}\). With \(r=2k\), the indicator \(E_k\) depends only on the first \(r\) uniforms and is \(\mathbf1\{D_{r-1}\le k-1\}\). The total endpoint is \(S_{2n}=2n-2D_{2n}\).

**2. The terminal-rank identity.** For a uniform permutation \(\pi\) on \(r\) elements, conditioned on \(D_{r-1}=d\), its expected terminal rank is \(r-d\). Here is a derivation. Let \(P_r(z)=\sum_{d=0}^{r-1}A(r,d)z^d\) and let \(M_r(z)=\sum_{\pi}\pi_r z^{\operatorname{des}(\pi)}\). Appending to \(\pi\) one new element of rank \(j\in\{1,\dots,r+1\}\) produces a final descent for exactly \(\pi_r\) values of \(j\), so
\[P_{r+1}(z)=(r+1)P_r(z)+(z-1)M_r(z).\]
The standard Eulerian insertion recurrence, obtained by inserting the largest element at each available position, gives
\[P_{r+1}(z)=(1+rz)P_r(z)+z(1-z)P'_r(z).\]
Subtracting gives \(M_r(z)=rP_r(z)-zP'_r(z)\), hence the claimed conditional terminal-rank mean by coefficients. Conditional on terminal rank \(j\), the last uniform observation \(U_r\) is the \(j\)-th order statistic of \(r\) independent uniforms, with mean \(j/(r+1)\). Thus
\[\mathbb E[U_r\mid D_{r-1}=d]=\frac{r-d}{r+1}.\]

**3. Exact covariance.** All descent indicators strictly after the comparison at position \(r\) are independent of \(E_k\), since their uniforms are disjoint from \(U_1,\ldots,U_r\). The comparison at position \(r\) has conditional expectation \(U_r\), so the rank identity implies
\[\operatorname{Cov}(E_k,D_{2n})=\frac r{r+1}\operatorname{Cov}(E_k,D_{r-1}).\]
The Eulerian distribution of \(D_{r-1}\) is symmetric about \((r-1)/2\). As \(r=2k\), \(E_k\) selects precisely its strict lower half. Therefore \(\mathbb P(E_k=1)=1/2\) and
\[\operatorname{Cov}(E_k,D_{r-1})=-\frac12\mathbb E\left|D_{r-1}-\frac{r-1}{2}\right|.\]
Using \(N_{2n}=2\sum E_k\) and \(S_{2n}=2n-2D_{2n}\), we obtain
\[C_n=\sum_{k=1}^{n}\frac{2r}{r+1}\mathbb E\left|D_{r-1}-\frac{r-1}{2}\right|,\qquad r=2k.\]
Expanding the symmetric Eulerian absolute moment gives the displayed finite sum. Every term is positive.

**4. Strict comparison with a simple walk.** For the independent-sign walk, the paired-edge identity and the martingale property imply
\[\operatorname{Cov}(\widetilde N_{2n},W_{2n})=\sum_{k=1}^{n}\mathbb E|W_{2k-1}|.\]
Elementary binomial counting yields \(t_k:=\mathbb E|W_{2k-1}|=(2k-1)\binom{2k-2}{k-1}/4^{k-1}\). Since \(t_1=1\) and \(t_{k+1}/t_k=(2k+1)/(2k)\), induction using \((2k+1)^2\ge4k(k+1)\) gives \(t_k\ge\sqrt k\). On the permutation side the variance of \(D_{r-1}\) is \((r+1)/12\) (the stationary descent indicators have variance \(1/4\), covariance \(-1/12\) for neighbours, and zero covariance at greater distances). Cauchy–Schwarz bounds its \(k\)-th covariance contribution by
\[\frac{2r}{r+1}\sqrt{\frac{r+1}{12}}=\frac{2k}{\sqrt{3(2k+1)}}<\sqrt k\le t_k.\]
This proves strict inequality term by term for every \(n\ge1\).

**5. Asymptotics and correlation.** The centered Eulerian descent count \(D_{r-1}\) is a sum of bounded stationary one-dependent variables. Its usual one-dependent central limit theorem gives \((D_{r-1}-(r-1)/2)/\sqrt r\Rightarrow N(0,1/12)\). Exact second moments make the normalized absolute values uniformly integrable. Hence
\[\mathbb E\left|D_{r-1}-\frac{r-1}{2}\right|\sim\sqrt{\frac r{6\pi}}.\]
Summing the contributions with \(r=2k\) proves the asymptotic for \(C_n\). The same elementary binomial expression gives \(t_k\sim2\sqrt{k/\pi}\) and its summed asymptotic. Finally the proved discrete-arcsine marginal law makes \(N_{2n}/2\) beta-binomial with parameters \((n,1/2,1/2)\), giving \(\operatorname{Var}(N_{2n})=n(n+1)/2\). The descent variance gives \(\operatorname{Var}(S_{2n})=(2n+2)/3\). Substitution yields the claimed limiting correlation.

## Verification
The attached standalone `checker.py` independently enumerates all \((2n+1)!\) permutations for \(n=1,2,3,4\), checks each exact covariance, the arcsine occupancy counts, and the exact two variances; it independently enumerates all \(2^{2n}\) simple-walk paths and checks the comparator. It checks the terminal-rank identity by direct enumeration for lengths \(2\) through \(8\), and compares the asymptotic coefficient with exact Eulerian sums at larger finite sizes. Run with `python checker.py`. The checker prints `PASS` when all asserted identities hold. Finite runs are *not* a proof of the all-size statements; those follow from Steps 1–5.

## Relationship to prior work
Fang et al. (first public January 24, 2020) introduced and studied the permutation-generated walk and its arcsine-type statistics, including the functional Brownian limit. They conjectured the *exact* discrete-arcsine marginal for nonnegative edges. Tang (September 20, 2026) proved that conjecture using an independent-symmetric-increment representation. The present result does **not** claim either of those existing results as new. Its contribution is the exact joint occupation–endpoint covariance, the strict finite-size comparison with the classical walk despite identical occupation marginals, and the explicit asymptotic gap. Although the two preceding sources imply the marginal and scaling-law ingredients, neither inspected proof provides this finite covariance formula or strict comparison. The standard Eulerian insertion identity itself is classical; the new deduction is its application to a rank-sensitive occupation–endpoint joint statistic.

## Limitations
The result concerns only uniform permutations, the particular nonnegative-edge convention, and classical symmetric walks for comparison. It does not give the entire bivariate joint law, a rate for the correlation limit, or extensions to biased Mallows parameters. The asymptotic correlation is obtainable from known invariance principles under suitable moment control and is not asserted as a separate priority claim. No claim of independence or external certification is made. Historical priority of the exact finite-covariance comparison is based on the inspected literature and searches, not an exhaustive theorem-database guarantee.

## References
1. X. Fang, H. L. Gan, S. Holmes, H. Huang, E. Peköz, A. Röllin, and W. Tang, *Arcsine laws for random walks generated from random permutations with applications to genomics*, arXiv:2001.08857 (first public January 24, 2020); *Journal of Applied Probability* 58 (2021), 851–867; DOI:10.1017/jpr.2021.14.
2. W. Tang, *The occupation time of a random walk generated by the uniform random permutation*, arXiv:2609.25102v1 (September 20, 2026), Theorem 0.1 and its proof.
3. Classical Eulerian-number recurrence and one-dependent descent central limit theorem; also discussed in Fang et al., Sections 2–3.
