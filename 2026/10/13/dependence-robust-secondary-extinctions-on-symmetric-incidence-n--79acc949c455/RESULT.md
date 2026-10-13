# Dependence-robust secondary extinctions on symmetric incidence networks and odd-cycle frustration

## Finding

A common extinction probability for each pollinator does **not** determine expected plant loss unless the joint dependence of the pollinator failures is specified. In the all-neighbors-lost coextinction model, the least expected number of lost plants over *all* joint dependence structures is exactly computable for any vertex-transitive incidence hypergraph using the lower convex hull of its minimum induced-hyperedge profile. For every cyclic network with one plant per adjacent pair, this leads to a sharp parity-dependent phase diagram: an odd cycle retains a nonzero residual expected plant loss at the balanced marginal \(q=1/2\), although an even cycle can eliminate losses entirely.

## Assumptions and scope

Let \(H=(V,\mathcal E)\) be a finite nonempty hypergraph with \(|V|=n\ge3\), with nonempty hyperedges, and with an automorphism group acting transitively on the vertices. Vertices denote distinct pollinators and each hyperedge denotes one plant with precisely that set of pollinators. A plant dies exactly when *all* of its incident pollinators disappear; there are no additional cascades, dispersal effects, or compensatory adaptation. Hyperedges may be treated as a multiset provided the automorphisms preserve multiplicities.

For every \(q\in[0,1]\), let \(X=(X_v:v\in V)\) range over **every** joint distribution on \(\{0,1\}^V\) with \(\Pr(X_v=1)=q\) for each vertex. No pairwise or higher-order independence is assumed. Put

\[
Z(X)=\sum_{e\in\mathcal E}\prod_{v\in e}X_v,
\qquad
f_H(s)=\min_{\substack{S\subseteq V\\|S|=s}}\sum_{e\in\mathcal E}{\bf1}_{\{e\subseteq S\}},\quad 0\le s\le n.
\]

Let \(\ell_H:[0,n]\to\mathbb R\) be the greatest convex function satisfying \(\ell_H(s)\le f_H(s)\) at every integer \(s\). Then the complete sharp optimization theorem is

\[
\boxed{\min_{\substack{\mathcal L(X):\\ \Pr(X_v=1)=q\ \forall v}}\mathbb E Z=\ell_H(nq),}\qquad 0\le q\le1.
\]

For the cycle \(C_n\), take vertices \(0,\ldots,n-1\) modulo \(n\), with exactly one plant at each hyperedge \(\{i,i+1\}\). Define \(h_n(q)\) as the displayed minimum. If \(n=2k\ge4\),

\[
h_{2k}(q)=
\begin{cases}0,&0\le q\le\frac12,\\
2k(2q-1),&\frac12\le q\le1.
\end{cases}
\]

If \(n=2k+1\ge3\),

\[
h_{2k+1}(q)=
\begin{cases}
0,&0\le q\le\frac{k}{2k+1},\\
(2k+1)q-k,&\frac{k}{2k+1}\le q\le\frac{k+1}{2k+1},\\
(2k+1)(2q-1),&\frac{k+1}{2k+1}\le q\le1.
\end{cases}
\]

At the junctions, the adjacent formulas agree. In particular, \(h_{2k}(1/2)=0\) and \(h_{2k+1}(1/2)=1/2\). When the pollinator failures are independent, the expected number of lost cyclic plants instead equals \(nq^2\); the result concerns the best possible *arbitrary dependence* at fixed marginals, not the independent model.

## Proof

**Convex-hull lower bound.** For any realized extinction set \(S=\{v:X_v=1\}\), the number of dead plants is the number of hyperedges contained in \(S\), and therefore \(Z(X)\ge f_H(|S|)\ge\ell_H(|S|)\). Jensen's inequality and the equal marginals give

\[
\mathbb E Z\ge \mathbb E\ell_H(|S|)
\ge\ell_H(\mathbb E|S|)=\ell_H(nq).
\]

**Sharpness and attainability.** The lower convex hull at the abscissa \(nq\) lies on a face joining two (possibly equal) integer points \((s,f_H(s))\) and \((t,f_H(t))\). Choose extinction sets \(S_s,S_t\) attaining those two minima. First select cardinality \(s\) or \(t\) with mixing probabilities \(\theta\) and \(1-\theta\), where \(\theta s+(1-\theta)t=nq\). Then apply an independent, uniformly chosen automorphism of \(H\) to the chosen set. Since the automorphism group is transitive, each vertex belongs to the resulting set with conditional probabilities \(s/n\) and \(t/n\), hence unconditionally with probability \(q\). Automorphisms preserve the number of contained hyperedges, so \(\mathbb E Z=\theta f_H(s)+(1-\theta)f_H(t)=\ell_H(nq)\). The endpoint cases are included by taking one cardinality only. This proves the unrestricted hypergraph assertion without an enumeration.

**Exact cyclic profile.** For the cycle, if an extinction set has cardinality \(s\), the sum of its internal degrees is \(2s=2e(S)+|\partial S|\). Because the boundary has at most \(2\min(s,n-s)\) edges, its number of contained cycle edges satisfies

\[
e(S)\ge\max\{0,2s-n\}.
\]

Equality occurs for **every** integer \(0\le s\le n\). If \(s\le\lfloor n/2\rfloor\), choose an independent set of size \(s\); if \(s\ge\lceil n/2\rceil\), choose a set whose complement is independent of size \(n-s\). Such independent sets exist on a cycle for every size up to \(\lfloor n/2\rfloor\), and yield \(e(S)=0\) or \(e(S)=2s-n\), respectively. Therefore

\[
f_{C_n}(s)=\max\{0,2s-n\}\qquad(s=0,\ldots,n).
\]

When \(n=2k\), the discrete profile has zero slope until \(s=k\) and slope two thereafter, so its lower convex hull gives the stated two-branch formula. When \(n=2k+1\), the integer slopes are zero up through \(s=k\), then one between \(s=k\) and \(s=k+1\), and then two. They are nondecreasing, so the interpolating broken line is the lower convex hull; substitution \(s=nq\) gives all three branches.

**Structural obstruction relative to pairwise bounds.** The bivariate Fréchet inequality implies \(\Pr(X_i=X_{i+1}=1)\ge\max\{0,2q-1\}\) separately for each edge. The sum of these local bounds is \(n\max\{0,2q-1\}\). It is simultaneously sharp on an even cycle for every \(q\); on an odd cycle the exact excess is

\[
\Delta_n(q)=\max\left\{0,\frac12-n\left|q-\frac12\right|\right\},
\qquad(n\text{ odd}).
\]

Indeed, this is the difference between the explicit odd-cycle three-branch formula and the summed Fréchet lower bound. Its maximum is exactly \(1/2\) at \(q=1/2\), and it vanishes outside the interval between \(\lfloor n/2\rfloor/n\) and \(\lceil n/2\rceil/n\). The obstruction is global consistency around an odd loop; no stronger ecological or empirical claim is inferred.

## Verification

The bundled standalone file `verify_cycles.py` uses exact integer and rational arithmetic and only the Python standard library. From the extracted package, execute `python3 verify_cycles.py`. It enumerates the \(8{,}184\) deterministic extinction sets across cycle lengths \(3\) through \(12\), verifies the claimed profile at every cardinality, verifies cyclic rotation realizes equal marginals, and checks the closed-form convex envelope on a \(101\)-point rational grid for each cycle length. The returned status is `VERIFY_OK`. These finite checks are reproducibility aids; the preceding argument, not the enumeration, proves the result for every permitted hypergraph and all real \(q\in[0,1]\).

## Relationship to prior work

Memmott, Waser and Price introduced plant-pollinator knockout coextinction analysis with randomly or systematically ordered primary species losses. Bane, Pocock and James compare knockout model choices and ecological robustness measures. Neither inspected text optimizes over every joint dependence law with fixed primary-extinction marginals or supplies the cyclic parity phase diagram.

Huber and Marić characterize the admissible correlations of symmetric Bernoulli vectors through the cut polytope. Their case has the fixed marginal \(q=1/2\), and the balanced marginal/odd-cycle obstruction is compatible with it; that special point is not asserted to be new. Chaganty and Joe address admissible correlation matrices for general Bernoulli marginals, a broader feasibility framework from which a linear optimization can be posed. Their accessible abstract does not state an exact vertex-transitive coextinction convex-envelope result or an evaluated odd-cycle phase diagram. That full text was inaccessible at assessment, so prior implicit or explicit coverage remains a material residual risk. The present contribution is the **sharp all-marginal hypergraph reduction together with the evaluated all-length cyclic parity law**, not the basic Fréchet inequality, the coextinction rule, or the cut-polytope representation.

## Limitations

The optimization allows any dependence, including highly coordinated pollinator failures, and assumes exactly equal individual extinction marginals. It does not restrict dependence to a physically generated stochastic process and does not model temporal extinction sequences, demographic recovery, partial pollination, empirical frequencies, or additional cascades. The general hypergraph formula may require solving a hard combinatorial minimum contained-hyperedge problem for its numerical evaluation. The cycle formulas are complete, but their ecological prevalence and previously unindexed mathematical coverage have not been established. Independent validation has not been performed.

## References

- Memmott, J., Waser, N. M. & Price, M. V. (2004). *Tolerance of pollination networks to species extinctions*. Proceedings of the Royal Society B. https://doi.org/10.1098/rspb.2004.2909. First publicly online 6 December 2004.
- Bane, M. S., Pocock, M. J. O. & James, R. (2018). *Effects of model choice, network structure, and interaction strengths on knockout extinction models of ecological robustness*. Ecology and Evolution. https://doi.org/10.1002/ece3.4529.
- Huber, M. & Marić, N. (2019). *Admissible Bernoulli correlations*. Journal of Statistical Distributions and Applications. https://doi.org/10.1186/s40488-019-0091-5.
- Chaganty, N. R. & Joe, H. (2006). *Range of correlation matrices for dependent Bernoulli random variables*. Biometrika. https://doi.org/10.1093/biomet/93.1.197.
