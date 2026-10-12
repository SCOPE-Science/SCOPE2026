# Complete monotonicity of coalescent age–frequency covariance

## Finding

The covariance of Kingman genealogy age with the total branch length at derived-allele frequency \(r\) has a strictly completely monotone dependence on the *entire* frequency index. In addition, all frequency classes, including macroscopic frequencies proportional to sample size, share a universal \(1/n\) covariance scale with a nonconstant profile whose endpoint values are \(4\) and \(2\).

Write \(c_{n,r}=\operatorname{Cov}(H_n,L_{n,r})\). With a binomial coefficient taken as zero whenever its lower argument is outside \(0,\ldots,\) its upper argument, the exact finite-sample law is
\[
c_{n,r}=4\sum_{k=2}^{n-r+1}\frac{k\binom{n-r-1}{k-2}}{\binom{n-1}{k-1}k^2(k-1)^2},\qquad 1\le r<n.
\]
For all \(j\ge0\) and \(1\le r\le n-1-j\), defining \(\Delta_r c_{n,r}=c_{n,r+1}-c_{n,r}\),
\[
(-1)^j\Delta_r^j c_{n,r}=4\sum_{k=j+2}^{n-r+1}\frac{k\binom{n-r-j-1}{k-j-2}}{\binom{n-1}{k-1}k^2(k-1)^2}>0.
\]
The inequality is strict wherever the indicated difference exists, including at the highest possible difference order. In particular \(c_{n,1}=4/n\) and \(c_{n,n-1}=2/(n-1)\).

For any sequence \(1\le r_n\le n-1\) with \(r_n/n\to\alpha\in[0,1]\),
\[
\lim_{n\to\infty}n c_{n,r_n}=g(\alpha):=4\sum_{k=2}^{\infty}\frac{(1-\alpha)^{k-2}}{k(k-1)}.
\]
The continuous endpoint values are \(g(0)=4\), \(g(1)=2\), and the interior expression is
\[
g(\alpha)=\frac{4[(1-\alpha)+\alpha\log\alpha]}{(1-\alpha)^2},\qquad 0<\alpha<1.
\]
Its positive-power series shows that \(g\) is strictly decreasing, strictly convex, and has alternating derivative signs of every order on \((0,1)\).

## Assumptions and scope

Start with \(n\ge2\) labeled leaves. While \(k\) ancestral lineages remain, every unordered pair coalesces at rate \(1\); the holding time \(T_k\) is exponential with rate \(\binom{k}{2}\), independent of all holding times and of the sequence of uniformly sampled merger pairs. Set
\[
H_n=\sum_{k=2}^{n}T_k,\qquad L_{n,r}=\sum_{k=2}^{n}W_{k,r}T_k,
\]
where \(W_{k,r}\) is the number of extant lineages ancestral to exactly \(r\) original leaves at level \(k\). The root branch after the last merger is not included. The label \(r\) is an *exact descendant count*, not a proportion; all rates are in standard coalescent units. No variable population size or multiple-merger mechanism is assumed.

## Proof

**Step 1: lineage-count expectation.** The standard lineage-size identity [1, Section 2, Lemma 1] is, for \(2\le k\le n\) and \(1\le r<n\),
\[
\mathbb E W_{k,r}=k\frac{\binom{n-r-1}{k-2}}{\binom{n-1}{k-1}},
\]
where the numerator is zero if \(k>n-r+1\). This is exactly the product expression given by Dahmer and Kersting: explicitly
\[
\mathbb E W_{k,r}=\frac{k(k-1)}{n-r}\prod_{h=0}^{r-2}\frac{n-k-h}{n-1-h}.
\]
The empty product for \(r=1\) equals \(1\). That cited identity is a known input, not claimed as new.

**Step 2: covariance.** Independence of the holding times from the entire merger-history chain implies
\[
\operatorname{Cov}\Big(\sum_{k=2}^{n}T_k,\sum_{k=2}^{n}W_{k,r}T_k\Big)
=\sum_{k=2}^{n}\mathbb E W_{k,r}\,\operatorname{Var}(T_k).
\]
All off-diagonal contributions cancel; for each diagonal the covariance of \(T_k\) with \(W_{k,r}T_k\) equals \(\mathbb E W_{k,r}\operatorname{Var}(T_k)\). Since \(\operatorname{Var}(T_k)=4/[k^2(k-1)^2]\), substitution yields the exact finite-sample sum.

**Step 3: all-order finite differences.** Repeated use of Pascal's identity gives, with the zero convention,
\[
(-1)^j\Delta_r^j\binom{n-r-1}{k-2}
=\binom{n-r-j-1}{k-j-2}
\]
for each \(j\ge0\) with \(r+j\le n-1\). Apply the identity termwise, keeping the other nonnegative factors fixed. The term \(k=j+2\) has numerator \(\binom{n-r-j-1}{0}=1\), so the resulting sum is strictly positive. This proves strict complete monotonicity on the finite index set. At \(r=1\), the first-step identity simplifies the covariance to
\[
\frac4{n-1}\sum_{k=2}^{n}\frac1{k(k-1)}=\frac4n.
\]
At \(r=n-1\), only \(k=2\) remains and gives \(2/(n-1)\).

**Step 4: macroscopic frequency scaling.** For fixed \(k\ge2\) and any \(r_n/n\to\alpha\in[0,1]\), the product in Step 1 yields
\[
n\mathbb E W_{k,r_n}\longrightarrow k(k-1)(1-\alpha)^{k-2},
\]
with \(0^0=1\) for the \(k=2\) term at \(\alpha=1\). Moreover, for all allowed indices and \(n\ge2\), every factor in the product in Step 1 is in \([0,1]\), so
\[
0\le n\mathbb E W_{k,r}\le\frac{n}{n-1}k(k-1)\le2k(k-1).
\]
After multiplication by \(4/[k^2(k-1)^2]\), this supplies the summable majorant \(8/[k(k-1)]\), independent of \(n\) and \(r\). Dominated convergence for counting measure on \(k\ge2\) proves the asserted infinite series, including both endpoints. Summation of the series via geometric integration yields its logarithmic expression. On \(0<\alpha<1\), termwise derivatives are justified locally uniformly, and each nonzero derivative has the required alternating sign; the \(k=3\) term makes the first derivative strict, and \(k\ge j+2\) terms make all derivatives of order \(j\) strict. Continuity at \(\alpha=0,1\) follows from dominated convergence.

Two independent consistency identities follow directly from the deterministic tree relations \(\sum_{r=1}^{n-1}rL_{n,r}=nH_n\) and \(\sum_{r=1}^{n-1}L_{n,r}=\sum_{k=2}^{n}kT_k\):
\[
\sum_{r=1}^{n-1}r c_{n,r}=n\operatorname{Var}(H_n),\quad
\sum_{r=1}^{n-1}c_{n,r}=4\sum_{k=2}^{n}\frac1{k(k-1)^2}.
\]
These identities are verification checks, not a separate novelty claim.

## Verification

Run the standalone `verify_coalescent.py` with Python 3. It independently propagates each exact merger configuration as a rational-valued Markov chain for \(2\le n\le8\), recomputes the stagewise lineage-count expectations, and checks covariance formulas, strict finite differences, both endpoints and both global consistency identities. It reports `EXACT_OK` and 140 exact checks. It also evaluates \(n c_{n,r}\) for several fixed fractions and sample sizes up to 2,000 to check finite-size convergence. The finite enumerations and numerical calculations do not certify the infinite claim; Steps 1–4 are the proof.

## Relationship to prior work

Dahmer and Kersting [1] establish the general lineage-count expectation used in Step 1 and derive fixed-order branch-length moment limits. Their known formula and \(\mathbb E L_{n,r}=2/r\) are not asserted novel. Alimpiev and Rosenberg [2] calculate many covariances of aggregate coalescent-tree features, including the \(r=1\) height–external-length endpoint. Hobolth et al. [3] explain a general phase-type/reward method able to calculate finite branch-length covariances, and Sendrowski and Hobolth [4] implement more general arbitrary-reward moments. Those frameworks cover generic numerical finite moment *computation*; the contribution assessed here is specifically the exact strict **all-order inequality** across every descendant-frequency index together with its explicit macroscopic \(r/n\) continuum profile. A historical or implementation-based derivation not located in the inspected sources remains possible; exhaustive priority is not asserted.

## Limitations

Only a single-locus, constant-size, binary-merger Kingman genealogy is covered. No variable demography, multiple-merger coalescents, inference-optimality, joint limit theorem or correlation coefficient is established. The magnitude of the covariance depends on the stipulated time normalization. The finite covariance sum uses a previously published branch-count expectation. Publicly indexed accounts of the broader phase-type methods do not settle all possible implicit consequences of those methods, and independent scientific assessment has not occurred.

## References

[1] I. Dahmer and G. Kersting, *The internal branch lengths of the Kingman coalescent*, arXiv:1303.4562, first public version 2013-03-19; *Annals of Applied Probability* 25 (2015), 1325–1348. https://arxiv.org/abs/1303.4562

[2] E. Alimpiev and N. A. Rosenberg, *A compendium of covariances and correlation coefficients of coalescent tree properties*, arXiv:2103.13467 (2021). https://arxiv.org/abs/2103.13467

[3] A. Hobolth, I. Rivas-González, M. Bladt, A. Futschik, *Phase-type distributions in mathematical population genetics: An emerging framework*, *Theoretical Population Biology* 157 (2024), 14–32. https://doi.org/10.1016/j.tpb.2024.03.001

[4] J. Sendrowski and A. Hobolth, *PhaseGen: exact solutions for time-inhomogeneous multivariate coalescent distributions under diverse demographies*, *Genetics* 232 (2026), iyaf135; first online 2025-07-22. https://doi.org/10.1093/genetics/iyaf135
