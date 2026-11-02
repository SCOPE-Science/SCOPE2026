# A unique covariance transition between peaks and double ascents in Mallows permutations

## Finding

A Mallows permutation assigns to each permutation \(\pi\) of \([n]\) a probability proportional to \(q^{\operatorname{inv}(\pi)}\), for \(q>0\). Write \(P_n\) for its number of interior peaks and \(A_n\) for its number of interior double ascents. Their covariance has an **exactly one-crossing dependence transition** in the inversion-bias parameter at every order \(n\ge4\), and the critical parameters move strictly toward a universal algebraic limit.

Define
\[
\begin{aligned}
U(q)&=q^8-q^7-2q^6-2q^5-4q^4-3q^3-q^2-2q-2,\\
V(q)&=2q^5+3q^4+5q^3+5q^2+3q+1,\\
H(q)&=(q+1)^2(q^2+1)(q^2+q+1)^2(q^4+q^3+q^2+q+1).
\end{aligned}
\]
Then, for every integer \(n\ge4\) and every real \(q>0\),
\[
\boxed{\operatorname{Cov}(P_n,A_n)=\frac{q[(n-3)U(q)-V(q)]}{H(q)}.}
\]
There is a unique \(r_n>0\) satisfying \((n-3)U(r_n)=V(r_n)\); the covariance is negative below \(r_n\), zero at \(r_n\), and positive above it. Moreover, \(r_{n+1}<r_n\), and \(r_n\downarrow\rho=2.48765153547945\ldots\), the unique positive zero of \(U\). More precisely,
\[
r_n=\rho+\frac{V(\rho)}{(n-3)U'(\rho)}+O(n^{-2}).
\]
The first two critical parameters are \(r_4=2.76512368918815\ldots\) and \(r_5=2.64026650211909\ldots\). With only three permutation entries, the covariance is negative at every \(q>0\), so four is the first order admitting a sign change.

## Assumptions and scope

The sample space is the full symmetric group on \(n\ge3\) labels, with strictly positive inverse-temperature/fugacity parameter \(q\); no conditioning or restriction on permutations is assumed. Here \(\operatorname{inv}(\pi)\) counts pairs of positions \(i<j\) with \(\pi_i>\pi_j\). The random variables are
\[
P_n=\sum_{i=1}^{n-2}\mathbf1\{\pi_i<\pi_{i+1}>\pi_{i+2}\},\qquad
A_n=\sum_{i=1}^{n-2}\mathbf1\{\pi_i<\pi_{i+1}<\pi_{i+2}\}.
\]
In particular, they count only genuinely interior local triples and have no imposed endpoint sentinels. The two variables are not indicators of the same event; they are total counts. The case \(q=1\) is uniform permutations.

## Proof

**1. Local reduction.** If a contiguous window of length \(k\) is standardized by replacing its values with their ranks, its standardized order has Mallows \((k,q)\) distribution. To verify this, condition on the unordered labels appearing in that window: inversions crossing the window boundary depend on the selected label set but not their order inside the window, while inversions internal to the window supply exactly the factor \(q^{\operatorname{inv}}\). More generally, standardized orders in disjoint contiguous windows are independent: condition jointly on their unordered value sets and the order of the remaining positions, and observe that the weight factors into internal inversions within each window and a common external factor. This is the weak-dissociation/consecutive-homogeneity property discussed in [2].

Let \(I_i=\mathbf1\{\pi_i<\pi_{i+1}>\pi_{i+2}\}\) and \(J_i=\mathbf1\{\pi_i<\pi_{i+1}<\pi_{i+2}\}\). If \(|i-j|\ge3\), then \(\operatorname{Cov}(I_i,J_j)=0\). By stationarity across starting locations for standardized windows, \(c_t=\operatorname{Cov}(I_i,J_{i+t})\) depends only on \(t\) for \(-2\le t\le2\). Hence for \(n\ge4\),
\[
\operatorname{Cov}(P_n,A_n)=(n-4)(c_{-2}+c_2)+(n-3)(c_{-1}+c_1)+(n-2)c_0.
\]

**2. Five exact local covariances.** Write \(S_3=1+q+q^2\) and \(S_5=1+q+q^2+q^3+q^4\). The single-window probabilities are \(\Pr(I_i=1)=q/S_3\) and \(\Pr(J_i=1)=1/[(1+q)S_3]\). For each displacement \(t\), enumerate all standardized permutations of the union of the two windows (length three, four, or five), weighting by \(q^{\operatorname{inv}}\). This gives
\[
\begin{aligned}
c_{-2}&=-\frac{q^4}{S_3^2S_5},\\[2pt]
c_{-1}&=\frac{q^2(q^3+q^2+2q+1)}{(q+1)^2(q^2+1)S_3^2},\\[2pt]
c_0&=c_1=-\frac{q}{(q+1)S_3^2},\\[2pt]
c_2&=\frac{q^2(q^4+q^3+2q^2+2q+1)}{(q+1)^2(q^2+1)S_3^2S_5}.
\end{aligned}
\]
Substitution into the overlap sum and collection over the common positive denominator \(H(q)\) gives exactly \(q[(n-3)U(q)-V(q)]/H(q)\). The standalone checker independently enumerates the full Mallows permutation space through order eight and also verifies this polynomial identity over \(\mathbb Z[q]\), not merely at sampled numerical parameters.

**3. Sharp sign classification.** The polynomial \(U(q)\) has one positive leading coefficient and strictly negative coefficients in every lower degree. It is negative at zero and tends to positive infinity, so Descartes' rule of signs gives exactly one positive zero \(\rho\). Its value at one is negative, so \(\rho>1\). The polynomial \(V(q)\) is strictly positive for \(q>0\). For each \(n\ge4\), the polynomial \(B_n(q)=(n-3)U(q)-V(q)\) again has one positive leading coefficient and negative lower coefficients. Descartes' rule and endpoint signs therefore give precisely one positive root \(r_n\), and the sign changes from negative to positive at it. Since \(B_n(\rho)=-V(\rho)<0\), necessarily \(r_n>\rho\).

At \(q=r_n\) we have \(U(r_n)=V(r_n)/(n-3)>0\). Thus \(B_{n+1}(r_n)=U(r_n)>0\), forcing \(r_{n+1}<r_n\). The decreasing roots are bounded below by \(\rho\); if their limit exceeded \(\rho\), continuity would make \(U(r_n)\) bounded away from zero, contradicting \(U(r_n)=V(r_n)/(n-3)\). Therefore \(r_n\downarrow\rho\). Since \(U'(\rho)>0\) (indeed, writing \(U(q)=q^8-\sum_{j=0}^7a_jq^j\), at the root \(\rho U'(\rho)=\sum_{j=0}^7(8-j)a_j\rho^j>0\)), a Taylor expansion of that same root identity gives the displayed first-order asymptotic.

**4. The three-entry boundary.** When \(n=3\), the peak and double-ascent events are mutually exclusive, and their probabilities are positive. Their covariance is
\[
-\frac{q}{(q+1)(1+q+q^2)^2}<0.
\]

## Verification

Run `python3 CHECK.py` using Python's standard library. It checks the exact covariance by independent full-permutation weighted enumeration for \(n=3,4,5,6,7\) at five rational parameter values, and at \(n=8,q=3\); compares the overlap-count method for sixteen orders and nine rational parameters; checks rational sign tests; and verifies the **symbolic integer-polynomial identity** for the entire \(n\ge4\) family by testing its two affine-in-\(n\) coefficients. The packaged checker reports 285 exact assertions. These computations corroborate the algebra; the infinite-parameter sign classification rests on the proof above, not extrapolation from finite trials.

## Relationship to prior work

Crane, DeSalvo and Elizalde [2] establish the relevant local-window properties of the Mallows measure and a single-pattern overlap variance formula. He [1] investigates Mallows descent dependence and related limit laws. Pan and Zeng [3], as recapitulated in detail by Dong, Lin and Pan [4, Theorems 1.2–1.3], give inversion-refined multivariate generating functions tracking peaks and double ascents. **The latter generating functions already encode the full joint distribution; no new distributional generating function is asserted here.** The claimed addition is the explicit mixed covariance identity together with its sharp, unique, strictly moving positive dependence boundary and algebraic limiting threshold. The inspected text of [1], [2] and [4] does not state those threshold conclusions, but earlier implicit derivations remain a substantive priority risk.

## Limitations

The theorem is limited to Mallows permutations with homogeneous inversion weight and the specified interior three-position types. It does not characterize joint dependence for longer motifs, other ranking models, or conditional independence. The full 2019 text of [3] was not directly available; the related main theorem was checked as reproduced in the full 2024 preprint [4]. In particular, historical priority cannot be guaranteed simply from unsuccessful searches.

## References

[1] Jimmy He, *A central limit theorem for descents of a Mallows permutation and its inverse*, initial arXiv posting 2020-05-20, arXiv:2005.09802. https://arxiv.org/abs/2005.09802

[2] Harry Crane, Stephen DeSalvo and Sergi Elizalde, *The probability of avoiding consecutive patterns in the Mallows distribution*, initial arXiv posting 2016-09-06, arXiv:1609.01370. https://arxiv.org/abs/1609.01370

[3] Qiongqiong Pan and Jiang Zeng, *A q-analogue of generalized Eulerian polynomials with applications*, *Advances in Applied Mathematics* 104 (2019), 85–99. DOI:10.1016/j.aam.2018.12.002.

[4] Yao Dong, Zhicong Lin and Qiongqiong Pan, *A q-analog of the Stirling-Eulerian Polynomials*, initial arXiv posting 2024-04-15, arXiv:2404.09777. https://arxiv.org/abs/2404.09777
