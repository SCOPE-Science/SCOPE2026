# A sharp Gaussian stability window for top concepts of Bernoulli formal contexts

## Finding

Consider a rectangular random formal context with \(m\) objects and \(N_m\) attributes, in which every incidence is independently present with the same probability \(p\in(0,1)\). Let \(\sigma_m\) be the *intensional stability* of its top concept: the proportion of object subsets with the same common attributes as the full object set. Write \(\beta=-\log p>0\) and let \(\Phi\) be the standard normal distribution function.

**Theorem (exact mean, quenched critical window, and exponential decay).** For every positive integer \(m\) and \(N_m\),
\[
\mathbb E\sigma_m=2^{-m}\sum_{t=0}^{m}\binom mt(1-p^t+p^m)^{N_m}.
\]
If \(b\in\mathbb R\) is fixed and
\[
\log N_m=\frac{\beta m}{2}+b\sqrt m+o(\sqrt m),
\]
then
\[
\boxed{\sigma_m\longrightarrow\Phi\!\left(-\frac{2b}{\beta}\right)\quad\text{almost surely and in }L^1.}
\]
The almost-sure statement holds under **every** coupling across sizes \(m\), provided each individual rectangular array has the stipulated independent Bernoulli incidences.

More generally, suppose \(\log N_m/m\to c\in[0,\infty]\), allowing \(c=+\infty\). If \(c<\beta/2\), then \(\sigma_m\to1\) almost surely; if \(c>\beta/2\), then \(\sigma_m\to0\) almost surely. For finite \(c>\beta/2\), the exact exponential rate of the mean is
\[
\lim_{m\to\infty}\frac{1}{m}\log\mathbb E\sigma_m=-D\!\left(\min\left\{\frac c\beta,1\right\}\middle\|\frac12\right),
\]
where \(D(s\|1/2)=s\log(2s)+(1-s)\log(2(1-s))\), interpreted continuously at \(s=1\). When \(c=+\infty\), the rate equals \(-\log2\). The theorem does not assign a zero-one limit from the single condition \(c=\beta/2\); the finer square-root window resolves that boundary.

## Assumptions and scope

For each \(m\ge1\), put \(G_m=\{1,\ldots,m\}\) and \(M_m=\{1,\ldots,N_m\}\), with \(N_m\) a positive integer. Let \(I_m\subseteq G_m\times M_m\) be random, with independently distributed incidence indicators of common probability \(p\) strictly between zero and one. For \(T\subseteq G_m\), its derivation is \(T'=\{a\in M_m:\text{every }g\in T\text{ is incident with }a\}\), with the empty-set derivation equal to all attributes. The top concept is \((G_m,G_m')\). Define
\[
\sigma_m=2^{-m}\big|\{T\subseteq G_m:T'=G_m'\}\big|.
\]
These are random *context-wise* stability values, not the probability that a particular fixed concept exists. The coupling in the almost-sure assertion is arbitrary: no independence is presumed between arrays with different \(m\). All logarithms are natural. The upper and lower limits refer to increasing object counts; attribute counts may increase exponentially.

## Proof

**1. Exact expectation.** Fix \(T\subseteq G_m\) with \(|T|=t\). An attribute belongs to \(T'\setminus G_m'\) exactly when all \(t\) incidences on \(T\) are present but at least one of the remaining \(m-t\) incidences is absent. Since the entries are independent, the probability of this event for a given attribute is \(p^t-p^m\). Independence between attributes gives
\[
\Pr(T'=G_m')=(1-p^t+p^m)^{N_m}.
\]
The equality follows because \(G_m'\subseteq T'\) always. Summing over all \(2^m\) choices of \(T\) proves the exact mean formula, including \(T=\varnothing\) and \(T=G_m\).

**2. Uniform threshold sandwich.** Set \(r_m=(\log N_m)/\beta\) and \(w_m=m^{1/4}\). Suppose first that \(r_m/m\to1/2\), as in the square-root window. For large \(m\), every \(T\) with \(|T|\ge r_m+w_m\) satisfies, by a union bound,
\[
\Pr(T'\ne G_m')\le N_mp^{|T|}\le e^{-\beta w_m}.
\]
On the other hand, for \(|T|\le r_m-w_m\), we have \(m-|T|\ge m/3\) eventually. Hence \(1-p^{m-|T|}\ge1/2\), and
\[
\Pr(T'=G_m')=\big(1-p^{|T|}(1-p^{m-|T|})\big)^{N_m}
\le\exp\big(-\tfrac12N_mp^{|T|}\big)
\le\exp\big(-\tfrac12e^{\beta w_m}\big).
\]
Let \(X_m\sim\operatorname{Bin}(m,1/2)\), not necessarily coupled to the random context. Define \(A_m=\Pr(X_m>r_m)\). Since the maximum binomial point mass is \(O(m^{-1/2})\), the proportion of subsets with \(||T|-r_m|\le w_m\) is \(O(m^{-1/4})\). If \(Z_m\) is the fraction of subsets *outside* that band whose indicators \(\mathbf1_{\{T'=G_m'\}}\) disagree with the threshold indicator \(\mathbf1_{\{|T|>r_m\}}\), then
\[
\mathbb E Z_m\le\delta_m:=e^{-\beta m^{1/4}}+\exp\!\left(-\tfrac12e^{\beta m^{1/4}}\right).
\]
For every realization, \(|\sigma_m-A_m|\le Z_m+O(m^{-1/4})\), with a deterministic implied constant. The bound on \(\delta_m\) is summable even after taking square roots: \(\sum_m\sqrt{\delta_m}<\infty\). Markov's inequality gives \(\Pr(Z_m>\sqrt{\delta_m})\le\sqrt{\delta_m}\); the first Borel–Cantelli lemma therefore gives \(Z_m\to0\) almost surely, without any cross-\(m\) independence. Boundedness also proves \(L^1\) convergence to the same threshold asymptotic.

**3. Gaussian profile.** The assumed critical-window scaling gives
\[
\frac{r_m-m/2}{\sqrt m/2}\longrightarrow\frac{2b}{\beta}.
\]
The de Moivre–Laplace central limit theorem for \(X_m\) implies \(A_m\to1-\Phi(2b/\beta)=\Phi(-2b/\beta)\). Combining with Step 2 proves the almost-sure and \(L^1\) statements.

**4. Zero-one regions.** Suppose \(\log N_m/m\to c<\beta/2\). Choose \(a\) strictly between \(c/\beta\) and \(1/2\). For every \(|T|\ge am\), the union bound from Step 2 gives \(\Pr(T'\ne G_m')\le N_mp^{am}=e^{-\Omega(m)}\); and \(\Pr(X_m<am)=e^{-\Omega(m)}\) by binomial large deviations. Therefore \(\sum_m\mathbb E(1-\sigma_m)<\infty\), so \(\sigma_m\to1\) almost surely by Markov and Borel–Cantelli. When \(c>\beta/2\), choose \(a\) strictly between \(1/2\) and \(\min(c/\beta,1)\). For \(|T|\le am\), we have \(m-|T|\ge(1-a)m\), so the lower-threshold inequality yields \(\Pr(T'=G_m')\le\exp(-e^{\Omega(m)}/2)\). The remaining fraction of subsets is at most \(\Pr(X_m>am)=e^{-\Omega(m)}\). Thus \(\sum_m\mathbb E\sigma_m<\infty\), which implies \(\sigma_m\to0\) almost surely. The same argument works when \(c=+\infty\).

**5. Exponential mean rate.** Let \(\beta/2<c<\beta\) and put \(s=c/\beta\in(1/2,1)\). For any sufficiently small \(\varepsilon>0\), the preceding estimates with constant-width fractions give
\[
(1-o(1))\Pr(X_m\ge(s+\varepsilon)m)
\le\mathbb E\sigma_m
\le\Pr(X_m\ge(s-\varepsilon)m)+\exp(-e^{\Omega(m)}).
\]
The binomial large-deviation formula \(m^{-1}\log\Pr(X_m\ge am)\to-D(a\|1/2)\) for \(a\in(1/2,1)\), followed by \(\varepsilon\downarrow0\), proves the stated rate. If \(c\ge\beta\) is finite or infinite, the deterministic inclusion \(T=G_m\) gives \(\sigma_m\ge2^{-m}\); for every \(a\in(1/2,1)\), the upper bound \(\mathbb E\sigma_m\le\Pr(X_m\ge am)+\exp(-e^{\Omega(m)})\) holds. Letting \(a\uparrow1\) yields the matching rate \(-\log2\). This completes the proof.

## Verification

The standard-library program `verify.py` reconstructs the top concept directly from each incidence matrix and computes \(\sigma_m\) by enumerating every object subset. It exhaustively sums over all binary incidence matrices in 29 small parameter cases with rational entry probabilities \(1/2\), \(1/3\), and \(2/3\), comparing the exact probability-weighted mean with the closed formula using rational arithmetic. It examines 10,238 complete matrices and reports `VERIFY_OK`. A separate floating-point evaluation of the exact expectation at critical sizes illustrates convergence toward \(1/2\); it is not evidence of the infinite limit. The asymptotic claims are proved by the threshold sandwich, summable bounds, the central limit theorem, and binomial large deviations, not by finite tests.

Run `python3 verify.py` from the directory containing this file and the verifier. No external packages or data are required.

## Relationship to prior work

Intensional stability of a formal concept is an established measure of its invariance under removal of objects; Zhi (2014) gives minimal-generator and inclusion–exclusion calculations for a fixed context. Mouakher and Ko (2022) develop efficient assessment procedures. Sakurai (2021) treats random formal contexts and obtains exact expected **total concept counts** and superpolynomial growth; its article specifies the Bernoulli random-incidence model but does not compute the stability of the top concept or derive the quenched Gaussian window established here. These are different quantities: a concept count is not a probability of preserving one concept's intent after deletion of random objects. Classical binomial central-limit and large-deviation estimates are used as known tools, not claimed as original.

## Limitations

This theorem concerns only the top concept, a fixed incidence probability strictly between zero and one, and independent Bernoulli entries **within** each finite context. It says nothing about the joint stability of other concepts, heterogeneous incidence probabilities, dependent columns, or a general concept-stability distribution. It does not provide a nontrivial sample-path fluctuation law at the critical window beyond the deterministic limit. An earlier implicit reduction of concept stability to the Bernoulli coverage threshold may exist. The full text of Mouakher and Ko (2022) could not be obtained through accessible lawful channels; that comparison rests on its bibliographic abstract and is an originality risk. Independent external mathematical audit has not been performed.

## References

1. T. Sakurai, *On formal concepts of random formal contexts*, arXiv:2101.11023 (first public version 26 January 2021), https://arxiv.org/pdf/2101.11023. Full primary text inspected.
2. A. Mouakher and A. Ko, *Efficient assessment of formal concept stability in the Galois lattice*, 2022, DOI:10.1080/03081079.2022.2084728. Bibliographic abstract inspected; full text not accessible.
3. H.-l. Zhi, *On the Calculation of Formal Concept Stability*, Journal of Applied Mathematics (2014), DOI:10.1155/2014/917639. Full publicly accessible article inspected.
4. R. Emilion and G. Levy, *Size of random Galois lattices and number of closed frequent itemsets*, Discrete Applied Mathematics (2009), DOI:10.1016/j.dam.2009.02.025. Abstract compared; full text not inspected.
