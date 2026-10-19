# Exact covariance and almost-sure Gaussian Peirce profiles of randomly decorated Grassmannian incidence algebras

## Finding

Let \(m\ge4\), choose an independent fair sign \(\varepsilon_B\in\{-1,+1\}\) for each triple \(B\in\binom{[m]}{3}\), and form the associated real signed Grassmannian incidence algebra as specified below. For every triple \(B\), let \(d_B\) be the multiplicity of the Peirce eigenvalue \(-1\) at its distinguished block idempotent; put \(n=m-3\), \(N=\binom m3\), and \(T_k=\#\{B:d_B=k\}\) for \(0\le k\le n\). Define

\[
p_k=2^{-n}\binom nk,\qquad
 a_k=2^{-(n-1)}\binom{n-1}{k},\qquad
 b_k=2^{-(n-1)}\binom{n-1}{k-1},
\]

where out-of-range binomial coefficients vanish. **The entire finite-dimensional spectral-profile covariance is exactly**

\[
\mathbb E T_k=Np_k,\qquad
\operatorname{Cov}(T_k,T_\ell)
=N\bigl(\mathbf1_{k=\ell}p_k-p_kp_\ell\bigr)
+\frac{3Nn}{4}(a_k-b_k)(a_\ell-b_\ell).
\]

Thus the covariance is a multinomial covariance plus an explicit rank-one correction. Moreover, the random empirical measure of standardized Peirce multiplicities,

\[
\mu_m=\frac1N\sum_{B\in\binom{[m]}3}
\delta_{(d_B-n/2)/(\sqrt n/2)},
\]

**converges almost surely weakly to the standard normal law as \(m\to\infty\)**. The assertion is valid under any coupling of the fair decorations at different values of \(m\); independence between dimensions is not assumed.

## Assumptions and scope

Take the real vector space with basis \(e_{ij}=e_{ji}\), one element for each unordered pair of distinct vertices. Set \(e_{ij}^2=0\), multiply basis elements associated with disjoint pairs to zero, and for three distinct indices define the commutative multiplication

\[
 e_{ij}e_{ik}=\varepsilon_{\{i,j,k\}}e_{jk}.
\]

For each block \(B=\{i,j,k\}\) the element

\[
 c_B=\tfrac12\varepsilon_B(e_{ij}+e_{ik}+e_{jk})
\]

is an idempotent. For each four-element set \(F\) define its Pasch sign \(\kappa_F=\prod_{B\in\binom F3}\varepsilon_B\); a Pasch configuration is negative when \(\kappa_F=-1\). All probabilities are over the \(\binom m3\) independent signs. The theorem concerns the block idempotents only, not all idempotents of the algebra. No classification of complete spectra at arbitrary idempotents is asserted.

## Proof

**1. Identify the spectral statistic from the algebra.** Let \(L_{c_B}\) denote multiplication by \(c_B\). The basis vectors from pairs entirely inside \(B\) form a three-dimensional invariant subspace with multiplication matrix having off-diagonal entries \(1/2\), hence eigenvalues \(1,-1/2,-1/2\). For each \(r\notin B\), the three basis vectors \(e_{ir},e_{jr},e_{kr}\) form a second invariant subspace whose symmetric multiplication matrix has off-diagonal entries \(\varepsilon_B\varepsilon_{\{i,j,r\}}/2\), \(\varepsilon_B\varepsilon_{\{i,k,r\}}/2\), and \(\varepsilon_B\varepsilon_{\{j,k,r\}}/2\). The product of their three signs is \(\kappa_{B\cup\{r\}}\). Its characteristic polynomial is \((z-\kappa_{B\cup\{r\}})(z+\kappa_{B\cup\{r\}}/2)^2\). The remaining \(\binom{m-3}{2}\) basis vectors contribute the zero eigenvalue. In particular

\[
 d_B=\sum_{r\notin B}\mathbf1\{\kappa_{B\cup\{r\}}=-1\}.
\]

This proves the Peirce/Pasch correspondence directly, independent of an external spectral lemma.

**2. Exact two-block dependence.** Fix \(B=\{i,j,k\}\). The signs \(\kappa_{B\cup\{r\}}\), for \(r\notin B\), are mutually independent fair signs: the independent input sign \(\varepsilon_{\{i,j,r\}}\) enters only the Pasch sign indexed by \(r\), and conditioning on all other input signs leaves these pivots independent and uniform. Thus \(d_B\) has the \(\operatorname{Binomial}(n,1/2)\) law.

Now take distinct blocks \(B,C\). If \(\lvert B\cap C\rvert\le1\), choose two vertices \(i,j\in B\setminus C\); the same pivot family \(\varepsilon_{\{i,j,r\}}\) does not appear in any Pasch sign of the star of \(C\) (each such Pasch sign uses only \(C\) and one external vertex). Conditional on all non-pivot signs, the entire star of \(B\) consists of independent fair signs, independently of the star of \(C\). Hence \(d_B\) and \(d_C\) are independent.

If \(\lvert B\cap C\rvert=2\), relabel \(B=\{1,2,3\}\) and \(C=\{1,2,4\}\). Their stars have exactly one common Pasch sign, \(\kappa_{\{1,2,3,4\}}\). All the other Pasch signs in these two stars are mutually independent fair signs and independent of the common one: for each outside vertex \(r\notin\{1,2,3,4\}\), use the distinct input pivots \(\varepsilon_{\{1,3,r\}}\) for the first star and \(\varepsilon_{\{1,4,r\}}\) for the second. The joint distribution is therefore

\[
(d_B,d_C)\stackrel d=(S+U,S+V),
\quad S\sim\operatorname{Bernoulli}(1/2),
\quad U,V\overset{\mathrm{iid}}\sim\operatorname{Binomial}(n-1,1/2),
\]

with \(S,U,V\) mutually independent. Consequently

\[
\operatorname{Cov}(\mathbf1\{d_B=k\},\mathbf1\{d_C=\ell\})
=\tfrac14(a_k-b_k)(a_\ell-b_\ell).
\]

Every block has precisely \(3n\) other blocks meeting it in exactly two vertices. Summing the diagonal contributions and these \(3nN\) ordered overlapping pairs yields the covariance formula in the Finding. This also proves that there are no unaccounted higher-order assumptions in the second-moment calculation.

**3. Concentration and almost-sure Gaussian law.** For any bounded real measurable \(f\) with \(\lVert f\rVert_\infty\le K\), set \(X_B=f((d_B-n/2)/(\sqrt n/2))\). The dependency analysis above, together with the Cauchy–Schwarz bound \(\lvert\operatorname{Cov}(X_B,X_C)\rvert\le K^2\), gives

\[
\operatorname{Var}\left(\frac1N\sum_BX_B\right)
\le \frac{K^2(1+3n)}{N}.
\]

For a fixed threshold \(t\in\mathbb R\), apply this with \(f=\mathbf1_{(-\infty,t]}\), obtaining the nonasymptotic probability bound

\[
\Pr\left(\left|\mu_m(( -\infty,t])-\Pr\{(Y_n-n/2)/(\sqrt n/2)\le t\}\right|>\eta\right)
\le\frac{1+3n}{N\eta^2},
\quad Y_n\sim\operatorname{Binomial}(n,1/2),\quad \eta>0.
\]

Since \((1+3n)/N=O(m^{-2})\), this bound is summable over \(m\). Borel–Cantelli yields almost-sure convergence of the empirical distribution function to its binomial expectation at each rational threshold. The ordinary binomial central limit theorem sends those expectations to \(\Phi(t)\). Intersecting the probability-one events for the countable set of rational thresholds and using monotonicity and continuity of \(\Phi\) proves weak almost-sure convergence to \(\mathcal N(0,1)\). The first Borel–Cantelli lemma requires no assumption on dependence across dimensions.

## Verification

The accompanying `verify.py` exhaustively enumerates all independent triple decorations for \(m=4\) (16 cases) and \(m=5\) (1,024 cases), using exact rational arithmetic to compare every profile mean and covariance entry with the theorem. It also constructs the actual multiplication matrices of block idempotents and checks their full characteristic polynomials over all 16 decorations for \(m=4\), and over seven fixed test decorations for \(m=5\). A seeded 10,000-sample check for \(m=6\) compares empirical means to exact expectations. Run `python verify.py` with Python and SymPy installed. Exhaustive finite checks are not substitutes for the general proof.

## Relationship to prior work

Fox and Tkachev [1] introduce these real decorated incidence algebras, identify block spectra through negative Pasch counts, and study the deterministic spectral profile including moment inversion and computational sampling. This paper's parameter \(d_B\) is therefore **not** new. The contribution here is the exact law of the whole profile's first two moments (including a rank-one covariance correction caused by two-block overlaps), an explicit concentration inequality, and a dimension-asymptotic almost-sure Gaussian law under independent fair decoration. The full accessible text of [1], including its spectral theorem and discussion of sampled profiles, was compared by implication; it does not state or imply an exact random covariance/strong limit law merely from its deterministic spectral characterization. Earlier Steiner-algebra work [2] develops a different underlying model and does not give this probability law.

## Limitations

The probability model requires independent fair signs attached to all triples, and the asymptotic keeps this model as the underlying vertex count grows. Deterministic decorations and constrained sign families need not have Gaussian empirical profiles. The theorem addresses only the \(-1\) eigenspace multiplicities at the canonical block idempotents, not the distribution of all algebra isomorphism classes, other idempotents, or complete profile probabilities. The proof establishes second moments and a weak almost-sure limit, not a central limit theorem for fluctuations of the entire vector \((T_k)_k\). A related manuscript cited within [1] but not available in the accessible source set presents a bibliographic risk for novelty claims; independent external review remains necessary.

## References

[1] Daniel J. F. Fox and Vladimir G. Tkachev, *On the Peirce spectral rigidity of decorated incidence algebras*, arXiv:2609.25353v1, first public version September 21, 2026. https://arxiv.org/abs/2609.25353

[2] Daniel J. F. Fox, *Killing metrized commutative nonassociative algebras associated with Steiner triple systems*, arXiv:2205.08838. https://arxiv.org/abs/2205.08838
