# The exact winner-index polymatroid under prescribed marginals and a prescribed maximum

## Finding

Let \(d\ge2\). Fix Borel probability measures \(\mu_i\) on \(\mathbb R\), with distribution functions \(F_i\), and another Borel probability measure \(\gamma\) with distribution function \(G\). Assume the **prescribed-maximum feasibility conditions**
\[
G(t)\le F_i(t)\quad(t\in\mathbb R,\ i=1,\ldots,d),
\qquad \gamma\le\sum_{i=1}^d\mu_i\quad\text{as measures}.
\]
Use the finite dominating measure \(\lambda=\gamma+\sum_i\mu_i\) and densities \(g=d\gamma/d\lambda\), \(f_i=d\mu_i/d\lambda\). For every set of indices \(S\subseteq[d]\), define
\[
r(S)=\int_{\mathbb R}\min\!\left\{g(x),\sum_{i\in S}f_i(x)\right\}\,\lambda(dx),\qquad r(\varnothing)=0.
\]
**Theorem.** Among all joint distributions of \((X_1,\ldots,X_d,J)\) with \(X_i\sim\mu_i\), \(M:=\max_iX_i\sim\gamma\), and \(J\in[d]\) satisfying \(X_J=M\) almost surely, the exact set of attainable winner-index probabilities \(p_i=\Pr(J=i)\) is
\[
\mathcal P=\left\{p\in\mathbb R^d:\ \sum_{i=1}^dp_i=1,\ \sum_{i\in S}p_i\le r(S)\quad\forall S\subseteq[d]\right\}.
\]
The nonnegative, increasing set function \(r\) is submodular and normalized by \(r([d])=1\). Thus \(\mathcal P\) is a nonempty polymatroid base. Its vertices are the (possibly repeated) vectors determined by permutations \(\sigma\) of \([d]\):
\[
p_{\sigma_j}^{\sigma}=r(S_j)-r(S_{j-1}),\qquad S_j=\{\sigma_1,\ldots,\sigma_j\},\quad S_0=\varnothing.
\]
Every such vertex has an explicit coupling realizing it, and mixtures of those couplings realize every point of \(\mathcal P\). The statement includes arbitrary atomic margins: \(J\) can choose a winner when there are ties.

**Unique-winner strengthening.** If all \(\mu_i\) and \(\gamma\) are atomless and each \(F_i(t)>G(t)\) for every \(t\) satisfying \(0<G(t)<1\), then **every** point of \(\mathcal P\) is realized by a coupling with \(X_J> X_i\) for each \(i\ne J\) almost surely. In this case \(J=\arg\max_iX_i\) is not randomized.

**Uniform-marginal example.** Take \(\mu_i=\operatorname{Uniform}[0,1]\) for all \(i\), and let \(G(t)=t^d\) on \([0,1]\), the distribution of the maximum of \(d\) independent uniforms. For \(|S|=k\) the rank is
\[
r_k= k-\frac{d-1}{d}\,k\left(\frac{k}{d}\right)^{1/(d-1)},\quad k=0,1,\ldots,d,
\]
interpreted as \(r_0=0\). The attainable winner distributions are exactly the vectors majorized by \(a=(r_1-r_0,\ldots,r_d-r_{d-1})\), where \(a\) is nonincreasing. In particular, for two variables the exact interval is
\[
\boxed{\Pr(X_1>X_2)\in[1/4,3/4]}
\]
while \(X_1,X_2\) remain individually uniform and \(\max(X_1,X_2)\) has CDF \(t^2\). Both endpoints admit couplings with no ties.

## Assumptions and scope

The inequality \(\gamma\le\sum_i\mu_i\) means domination on **every Borel set**, not only a comparison between cumulative distributions. The theorem concerns the finite vector of unconditional winner-label frequencies, not the full joint law of maximum and winner. Under ties the index \(J\) is part of the coupling, allowing randomized tie breaking; without the additional atomlessness and strict CDF inequalities, the theorem does **not** assert that any prescribed label vector is the distribution of a unique maximizer. All integrals and density identities hold modulo \(\lambda\)-null sets. The feasibility conditions are those characterized in Ansari (2026), not a new feasibility test.

## Proof

**1. Necessary subset bounds.** Set \(\nu_i(B)=\Pr(M\in B,J=i)\). Because \(J\) designates an actual maximizer, \(\sum_i\nu_i=\gamma\) and \(\nu_i\le\mu_i\). Thus for any \(S\subseteq[d]\), the measure \(\nu_S=\sum_{i\in S}\nu_i\) is dominated by both \(\gamma\) and \(\sum_{i\in S}\mu_i\). Taking Radon–Nikodym densities shows
\[
p(S):=\sum_{i\in S}\Pr(J=i)=\nu_S(\mathbb R)
\le\int\min\!\left(g,\sum_{i\in S}f_i\right)d\lambda=r(S).
\]
Also \(p([d])=1\).

**2. Submodularity and greedy allocations.** For fixed \(x\), the function \(S\mapsto\min(g(x),\sum_{i\in S}f_i(x))\) is nondecreasing and submodular: for \(S\subseteq T\) and \(i\notin T\), its marginal increase on adding \(i\) decreases as the partial sum increases, since \(z\mapsto\min(g(x),z)\) is concave and nondecreasing. Integration preserves these properties. The domination hypothesis gives \(g\le\sum_i f_i\) almost everywhere, so \(r([d])=\int g\,d\lambda=1\).

Choose a permutation \(\sigma\). Assign maximum-law density greedily: for \(j=1,\ldots,d\),
\[
v_{\sigma_j}(x)=\min\!\left\{f_{\sigma_j}(x),\left(g(x)-\sum_{h<j}f_{\sigma_h}(x)\right)_+\right\}.
\]
Then \(0\le v_i\le f_i\), \(\sum_i v_i=g\), and each prefix sum is \(\sum_{h\le j}v_{\sigma_h}=\min(g,\sum_{h\le j}f_{\sigma_h})\). The subprobability measures \(\nu_i(dx)=v_i(x)\lambda(dx)\) therefore satisfy \(\sum_i\nu_i=\gamma\), \(\nu_i\le\mu_i\), and \(\nu_{\sigma_j}(\mathbb R)=r(S_j)-r(S_{j-1})\). This proves attainability of the proposed greedy vectors once the coupling in Step 3 is constructed.

For completeness, these greedy vectors are precisely the vertices of the displayed base. Let \(c\in\mathbb R^d\), order its coordinates \(c_{\sigma_1}\ge\cdots\ge c_{\sigma_d}\), and write \(S_j=\{\sigma_1,\ldots,\sigma_j\}\). Every \(p\in\mathcal P\) obeys
\[
c\cdot p=c_{\sigma_d}+\sum_{j=1}^{d-1}(c_{\sigma_j}-c_{\sigma_{j+1}})p(S_j)
\le c_{\sigma_d}+\sum_{j=1}^{d-1}(c_{\sigma_j}-c_{\sigma_{j+1}})r(S_j),
\]
and the greedy vector for \(\sigma\) achieves equality. Thus every linear functional is maximized by a greedy vector; by separation for compact convex polytopes, \(\mathcal P\) is their convex hull, with no additional vertices. In particular \(\mathcal P\) consists of nonnegative vectors: \(p_i=1-p([d]\setminus\{i\})\ge1-r([d]\setminus\{i\})\ge0\).

**3. Realizing any feasible submeasure decomposition.** This step retains and adapts the quantile construction in Ansari (2026, Theorem 1). Suppose arbitrary measures \(\nu_i\) satisfy \(\sum_i\nu_i=\gamma\) and \(0\le\nu_i\le\mu_i\). First sample \((M,J)\) with \(\Pr(M\in B,J=i)=\nu_i(B)\). Write \(p_i=\nu_i(\mathbb R)\). When \(p_i<1\), define the probability measures
\[
\beta_i=\frac{\gamma-\nu_i}{1-p_i},\qquad
\eta_i=\frac{\mu_i-\nu_i}{1-p_i}
\]
with cumulative functions \(B_i,A_i\). The key exact identity is
\[
A_i(t)-B_i(t)=\frac{F_i(t)-G(t)}{1-p_i}\ge0.
\]
For each \(i\ne J\), take a conditional randomized distributional transform of \(M\sim\beta_i\) to obtain a uniform \(W_i\) such that \(B_i^{-1}(W_i)=M\) a.s. and set \(X_i=A_i^{-1}(W_i)\le M\). Set \(X_J=M\). Then \(X_i\) has marginal \(\nu_i+(1-p_i)\eta_i=\mu_i\); all coordinates do not exceed \(M\), and the designated one equals it. If \(p_i=1\), necessarily \(\nu_i=\mu_i=\gamma\), so set \(X_i=M\). A common auxiliary uniform variable is allowed, and no independence between coordinates is asserted. Hence **every** greedy vector and every convex mixture thereof is realized.

**4. Strict unique winner.** Under atomlessness of \(\mu_i,\gamma\), every \(\nu_i\le\mu_i,\gamma\) is also atomless; thus \(A_i,B_i\) are continuous. If \(p_i=1\), then \(F_i=G\), contradicting strict CDF dominance at any \(t\) with \(0<G(t)<1\). For each event \(\{J\ne i\}\), \(0<G(M)<1\) almost surely because \(M\) has an atomless law (and the conditional law \(\beta_i\) is dominated by \(\gamma\)). The identity in Step 3 implies \(A_i(M)>B_i(M)\). Since \(W_i=B_i(M)\) almost surely under continuous \(B_i\), continuity of \(A_i\) ensures there is a point \(z<M\) with \(A_i(z)>W_i\). Hence \(X_i=A_i^{-1}(W_i)\le z<M\). This holds simultaneously for all \(i\ne J\), giving a unique actual winner.

**5. Exact uniform profile.** For uniform marginals and \(G(t)=t^d\) on \([0,1]\), take Lebesgue domination on that interval: \(f_i(t)=1\) and \(g(t)=dt^{d-1}\). For \(|S|=k\),
\[
r_k=\int_0^1\min\{dt^{d-1},k\}\,dt.
\]
The two integrands meet at \(a=(k/d)^{1/(d-1)}\), so
\[
r_k=\int_0^a dt^{d-1}dt+\int_a^1 k\,dt
=a^d+k(1-a)=k-\frac{d-1}{d}ka.
\]
The notation \(\int_0^a dt^{d-1}dt\) means integration of \(d\cdot t^{d-1}\); explicitly its value is \(a^d\). By concavity of the cardinality-based rank, the increments \(a_j=r_j-r_{j-1}\) decrease. The subset inequalities are therefore precisely the majorization constraints on the sorted probabilities. When \(d=2\), \(r_1=3/4\), hence \(p_1\le3/4\) and \(p_2\le3/4\), or \(1/4\le p_1\le3/4\). Strict dominance \(t>t^d\) for \(0<t<1\) proves uniqueness of winners in the constructed endpoint and intermediate couplings. \(\square\)

## Verification

Run `python verify.py` with Python's standard library; `verify_output.txt` contains its recorded output. The program executed successfully with **894 exact-rational or deterministic assertions**. It checks finite discrete submodular ranks, greedily constructed measures, an exhaustive three-atom integer-allocation census against all subset inequalities, and the two-uniform-variable \(3/4\) rank on exact dyadic partitions. It also checks a numerical quadrature of the closed formula through seven dimensions. The program is independent supporting finite evidence, not a proof of the measure-theoretic theorem; Steps 1–5 give that proof.

## Relationship to prior work

Ansari, *Couplings with prescribed maxima: A short proof of the quasi-copula characterization* (arXiv:2610.30642v1, first public 2026-10-22), proves that the two feasibility conditions in this manuscript are necessary and sufficient, and constructs a coupling from one specified submeasure decomposition of the proposed maximum law. Those conditions and the underlying quantile construction are **not claimed as new**. The present theorem adds the complete vector of attainable **winner-label probabilities**, its exact submodular-rank description, greedy extremizers, and strict-unique-winner realization. In the symmetric uniform case it gives explicit sharp probabilities beyond existence of a maximum-law coupling.

Bartl, Kupper, Lux and Papapantoleon, *Marginal and dependence uncertainty: bounds, optimal transport, and sharpness* (arXiv:1709.00641v2; SIAM Journal on Control and Optimization 60 (2022), 410–434), develop general optimization duality for couplings under marginal and maximum constraints. That framework is broader at the level of generic cost optimization, but it does not directly provide the finite polymatroid of attainable winner-label frequencies. The polymatroid greedy principle itself is classical; its concrete rank function in this coupling problem is the assessed structural contribution. Historical-priority verification beyond the inspected works is incomplete.

## Limitations

For atomic marginals a designated index can share a tied maximum; its frequency is not necessarily the probability of a strictly unique argmax. The strict-uniqueness extension assumes atomlessness and strict stochastic CDF separation throughout the interior of the maximum distribution; neither condition is asserted necessary. The theorem does not classify the full conditional law of the winner given the maximum, does not optimize other joint statistics, and does not assert historical uniqueness beyond the literature comparisons described. Independent mathematical and priority review have not been performed.

## References

1. J. Ansari (2026), *Couplings with prescribed maxima: A short proof of the quasi-copula characterization*, arXiv:2610.30642v1, https://arxiv.org/html/2610.30642v1 (public 2026-10-22). In particular Theorem 1 and Section 6.
2. D. Bartl, M. Kupper, T. Lux and A. Papapantoleon (2022), *Marginal and dependence uncertainty: bounds, optimal transport, and sharpness*, SIAM Journal on Control and Optimization **60**, 410–434, preprint arXiv:1709.00641v2, https://arxiv.org/abs/1709.00641.
3. J. Edmonds (1970), *Submodular functions, matroids, and certain polyhedra*, in *Combinatorial Structures and Their Applications*, pp. 69–87. The greedy-polymatroid support-function argument is reproduced directly in the proof.
