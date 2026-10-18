# Spatial Poisson limits for near-diametral chords and independent Gaussian crossings

## Finding
Let \(\mathcal M_n\) be a uniform random perfect matching of the cyclically ordered vertices \(\{0,1,\ldots,2n-1\}\), \(n\ge2\). For an unordered matched pair \(e\), define its shorter cyclic endpoint separation \(s(e)\in\{1,\ldots,n\}\) and its *diametral deficiency* \(j(e)=n-s(e)\).

For \(j\ge1\), the edge of deficiency \(j\) uniquely has the representation \(\{i,i+n-j\}\) modulo \(2n\); assign it location \(i/(2n)\pmod1\). For \(j=0\), each antipodal edge uniquely has the representation \(\{i,i+n\}\) with \(0\le i<n\); assign location \(i/n\pmod1\). Write \(\Xi_{n,j}\) for the associated finite counting measure on the unit circle \(\mathbb T=\mathbb R/\mathbb Z\).

**Theorem.** For each fixed integer \(J\ge0\), as \(n\to\infty\) through integers \(n>J\),
\[
\left(\Xi_{n,0},\ldots,\Xi_{n,J},\frac{C_n-n(n-1)/6}{n^{3/2}}\right)
\xrightarrow{\mathrm d}
(\Pi_0,\ldots,\Pi_J,G),
\]
where \(C_n\) counts unordered crossing chord pairs, \(\Pi_0\) is a homogeneous Poisson point process on \(\mathbb T\) with intensity \(\tfrac12\,dt\), \(\Pi_j\), for \(1\le j\le J\), are homogeneous Poisson processes with intensity \(dt\), and all processes and \(G\sim N(0,1/45)\) are mutually independent. Point-process convergence uses the weak topology on finite measures over the compact circle.

In particular, the integer-valued gap \(D_n=n-\max_{e\in\mathcal M_n}s(e)\) has a limit \(D\) independent of \(G\), with
\[
\Pr(D\ge k)=e^{-(k-1/2)}\qquad\text{for each integer }k\ge1.
\]
Thus the probability of an exactly antipodal chord tends to \(1-e^{-1/2}\), and for \(j\ge1\), \(\Pr(D=j)=e^{-(j-1/2)}(1-e^{-1})\).

## Assumptions and scope
All matchings have equal probability \(1/(2n-1)!!\). The value of \(J\) is fixed independently of \(n\); no uniformity in growing \(J\) is asserted. The position convention for exactly antipodal chords chooses the zero-based smaller label and therefore fixes an arbitrary origin, but the resulting limiting position law is uniform. For a random matching, the maximum is always defined, since there are exactly \(n\) chords. The theorem concerns *circular* shorter-arc length, not the linear endpoint distance or Euclidean random-chord lengths under independent continuous endpoint sampling.

## Proof
**1. Prescribed-edge probability and bounded conflicts.** If \(e_1,\ldots,e_t\) are distinct pairwise vertex-disjoint edges, then
\[
\Pr\{e_1,\ldots,e_t\subset\mathcal M_n\}
=\prod_{h=0}^{t-1}(2n-2h-1)^{-1}.
\]
For \(j=0\) there are exactly \(n\) potential antipodal edges; for each fixed \(j\ge1\) there are exactly \(2n\) candidate edges of deficiency \(j\). Each vertex touches at most \(1+2J\) candidates among deficiencies \(0,\ldots,J\). Consequently, for any fixed total number \(t\) of distinct candidate edges, only \(O_{J,t}(n^{t-1})\) of the \(O_{J,t}(n^t)\) ordered tuples contain an overlapping pair.

**2. Marked spatial factorial moments.** Fix finitely many arcs \(B_{j,h}\subset\mathbb T\) with Lebesgue-null boundaries and pairwise disjoint interiors for each mark \(j\). A color-zero class in an arc has \(n|B_{0,h}|+o(n)\) candidates; a color-\(j\) class for \(j\ge1\) has \(2n|B_{j,h}|+o(n)\). Multiplying the prescribed-edge probability from Step 1 by the count of admissible tuples gives, for every fixed collection of nonnegative integers \(r_{j,h}\),
\[
\mathbb E\prod_{j,h}\bigl(\Xi_{n,j}(B_{j,h})\bigr)_{r_{j,h}}
\longrightarrow\prod_{j,h}(\lambda_j |B_{j,h}|)^{r_{j,h}},
\qquad\lambda_0=\tfrac12,\quad\lambda_j=1\ (j\ge1),
\]
where \((u)_r\) is the falling factorial. These are the joint factorial moments of independent Poisson counts. They imply the asserted joint finite-dimensional Poisson convergence; uniform boundedness of expected total masses gives tightness of the point processes on the compact circle. Thus \((\Xi_{n,0},\ldots,\Xi_{n,J})\) converges to mutually independent homogeneous Poisson point processes.

**3. Gaussian marginal.** Flajolet and Noy proved for the crossing statistic \(C_n\) that
\[
\mathbb EC_n=\frac{n(n-1)}6,\qquad
\operatorname{Var}(C_n)=\frac{n(n-1)(n+3)}{45},\qquad
\frac{C_n-\mathbb EC_n}{n^{3/2}}\xrightarrow{\mathrm d}G\sim N(0,1/45).
\]
Only this established marginal theorem is invoked; its asymptotic normality is not a novelty claim.

**4. Uniform conditional stability.** Condition on any fixed \(t\) pairwise disjoint, specified candidate edges, where \(t\) does not grow with \(n\). The remaining matching on the other \(2(n-t)\) vertices is uniform. Relabeling these vertices in their inherited circular order preserves all crossings involving only remaining edges. Hence that residual crossing count \(C'\) has exactly the distribution of \(C_{n-t}\), independently of which edges were prescribed. At most \(t(n-t)+\binom t2\) crossings involve a prescribed chord, so
\[
|C_n-C'|\le t(n-t)+\binom t2,
\qquad |\mathbb EC_n-\mathbb EC_{n-t}|=O_t(n).
\]
After division by \(n^{3/2}\), the errors vanish uniformly over every choice of conditioned edges. Thus, for each bounded Lipschitz function \(f\), the conditional expectation of \(f((C_n-\mathbb EC_n)/n^{3/2})\), conditioned on *any* such edge set, converges uniformly to \(\mathbb Ef(G)\).

**5. Mixed convergence and independence.** Expand any product of finitely many falling factorial counts from Step 2 into a sum over specified edge tuples. Nondisjoint tuples contribute zero. On every admissible tuple, Step 4 factors the asymptotic conditional bounded-Lipschitz Gaussian test expectation, uniformly, from the tuple probability. Consequently,
\[
\mathbb E\!\left[f\!\left(\frac{C_n-\mathbb EC_n}{n^{3/2}}\right)
\prod_{j,h}(\Xi_{n,j}(B_{j,h}))_{r_{j,h}}\right]
\longrightarrow \mathbb Ef(G)\prod_{j,h}(\lambda_j|B_{j,h}|)^{r_{j,h}}.
\]
The same edge-count bounds give uniform integrability of all fixed factorial-count products (apply Step 2 with doubled exponents). Tightness and moment determinacy of the multivariate Poisson laws identify the joint limit and force independence of the Gaussian coordinate from the complete marked point-process vector.

**6. Extreme gap.** For each fixed integer \(k\ge1\), \(D_n\ge k\) holds precisely when no chord has deficiency \(0,\ldots,k-1\). By the joint Poisson limit,
\[
\Pr(D_n\ge k)\to\exp\!\left(-\tfrac12-(k-1)\right).
\]
These limiting tails vanish as \(k\to\infty\), giving tightness of \(D_n\); the same finite-dimensional joint convergence with the Gaussian coordinate yields the claimed independent joint limit \((D_n,Z_n)\Rightarrow(D,G)\).

**7. Finite identity, for calibration rather than novelty.** For an edge \(e\) of deficiency \(j\), its two complementary arcs contain \(a=n-j-1\) and \(b=n+j-1\) other vertices. Conditional on \(e\), exactly \(ab/(2n-3)\) other matched edges cross \(e\) on average. The crossings among the remaining \(n-1\) chords contribute \((n-1)(n-2)/6\) on average. Therefore, with \(N_{n,j}=\Xi_{n,j}(\mathbb T)\) and \(m_{n,0}=n\), \(m_{n,j}=2n\) for \(1\le j<n\),
\[
\operatorname{Cov}(N_{n,j},C_n)
=\frac{m_{n,j}}{2n-1}\,
\frac{n(n-1)-3j^2}{3(2n-3)}.
\]
For every fixed \(j\), this covariance is of order \(n\); nevertheless the rare-event/central-limit joint theorem establishes asymptotic independence at the \(n^{3/2}\) crossing scale.

## Verification
Run `python3 verify.py` using Python 3 standard library. The supplied script exhaustively enumerates all \(146598\) perfect matchings with \(2n\) vertices for \(2\le n\le7\) and performs \(75\) exact assertions checking class sizes, mean and variance of crossings, class-crossing covariance, and a third-order mixed factorial-moment identity. Successful output ends with `VERIFY_OK perfect_matchings 146598 assertions 75`. These are finite checks; the point-process and Gaussian independence statements follow from the six analytic steps above, not from enumeration.

## Relationship to prior work
Flajolet and Noy (INRIA RR-3914, March 2000, Theorem 3) prove the marginal Gaussian crossing law and its exact variance; these are used unchanged. Acan (arXiv:1501.01489v1, Theorem 4.2) proves independent Poisson limits for the counts of **fixed short-chord lengths** and analyzes the circular chord diagram's intersection graph. The fixed short-chord classes are not the moving near-diametral classes considered here; moreover, neither theorem gives their spatial Poisson processes or independence from global crossing fluctuations. Paguyo (arXiv:2104.01134, Sections 2–3) gives convergence rates for the individual crossing Gaussian and simple-chord Poisson laws, not their joint near-diametral marked process. Sullivan (arXiv:1611.02771, Theorem 2) enumerates matchings constrained by **linear minimum length**, not the distribution of circular maximum shorter-arc length. The present contribution is the combined marked spatial/extreme/global theorem and the conditional-stability proof, not rediscovery of these marginal facts.

## Limitations
The deficiency cutoff \(J\) is fixed; the result does not cover \(J\) growing with \(n\), rates for the point-process approximation, or a finite-sample exact law for the maximum. Historical priority of the *joint* statement remains subject to independent comparison with any unlocated general multivariate limit theorem for random matchings. The antipodal position convention breaks finite rotational equivariance and is used only to give one position to each antipodal edge. Verification has been performed through exact finite enumeration and self-review; no independent audit has been performed.

## References
1. P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA Research Report RR-3914 (March 2000), Theorem 3. Open-access original: https://algo.inria.fr/flajolet/Publications/FlNo00.pdf . DOI: 10.1007/978-3-662-04166-6_17.
2. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1 (first posted 2015-01-07), especially Section 4, Theorem 4.2. https://arxiv.org/pdf/1501.01489 .
3. J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134v1 (first posted 2021-04-02). https://arxiv.org/pdf/2104.01134 .
4. E. Sullivan, *Linear chord diagrams with long chords*, arXiv:1611.02771v1 (first posted 2016-11-08), Theorem 2. https://arxiv.org/pdf/1611.02771 .
