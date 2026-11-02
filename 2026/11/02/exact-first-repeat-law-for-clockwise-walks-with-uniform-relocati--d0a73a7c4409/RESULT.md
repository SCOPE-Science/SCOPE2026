# Exact first-repeat law for clockwise walks with uniform relocation

## Finding

Fix an integer \(n\ge2\). Let \(X_0=0\) and independently at each discrete step, with probability \(1-q\) move from \(x\) to \(x+1\pmod n\), or with probability \(q\) relocate to an independent uniform element of \(\mathbb Z/n\mathbb Z\). The relocation destination can equal a previously visited position, including the current one. Let
\[
T_n=\min\{t\ge1:X_t\in\{X_0,\ldots,X_{t-1}\}\}.
\]
Then for every \(q\in[0,1]\), every integer \(0\le t<n\), and \((a)^{\overline{k}}:=\prod_{j=0}^{k-1}(a+j)\), with the empty product equal to one,
\[
\boxed{\Pr(T_n>t)=\sum_{k=0}^{t}\binom tk q^k(1-q)^{t-k}\frac{(n-t)^{\overline{k}}}{n^k}.}
\]
Also \(\Pr(T_n>n)=0\), so the expression gives the whole finite law. For each fixed \(1\le t<n\), the survival probability is strictly decreasing in \(q\in[0,1]\).

The following are the two asymptotic regimes, with the relocation probability allowed to depend on \(n\).

**Critical finite-relocation window.** If \(nq_n\to\lambda\in[0,\infty)\), then \(T_n/n\) converges in distribution to a variable supported on \([0,1]\) whose survival probability for \(0\le x<1\) is \(e^{-\lambda x^2}\), and which has an atom of mass \(e^{-\lambda}\) at \(1\). For \(\lambda>0\) its continuous part has density \(2\lambda x e^{-\lambda x^2}\) on \((0,1)\). In particular,
\[
\lim_{n\to\infty}\frac{\mathbb E T_n}{n}=\int_0^1e^{-\lambda x^2}\,dx.
\]

**Many-relocation window.** If \(nq_n\to\infty\) and \(q_n\to q_\infty\in[0,1]\), put \(b_n=\sqrt{n/q_n}\). Then \(b_n=o(n)\) and for every \(x\ge0\),
\[
\boxed{\Pr(T_n/b_n>x)\longrightarrow\exp\bigl(-(1-q_\infty/2)x^2\bigr).}
\]
The coefficient continuously connects rare relocations (coefficient one) with the independent-uniform birthday process (coefficient one-half).

## Assumptions and scope

All transitions and relocation destinations are independent over time. The walk is on the directed clockwise cycle with a uniform relocation option, not an undirected nearest-neighbor walk or resetting to a fixed site. The first visit \(X_0\) counts in deciding whether a later position repeats. The finite formula includes the pure clockwise process \(q=0\) and pure independent-uniform sampling after the initial position \(q=1\). The two limit statements assume only the stated sequences of probabilities; the finite-window parameter \(\lambda\) may be zero, while the many-relocation scale is defined because \(q_n>0\) eventually.

## Proof

**Circular interval-packing identity.** Condition on which \(k\) of the first \(t\) transitions are relocations. The trajectory consists of \(k+1\) directed consecutive-site arcs of positive integer lengths \(\ell_0,\ldots,\ell_k\), with \(\sum_i\ell_i=t+1\). The first arc starts at zero; the later \(k\) arc starting sites are independent uniform positions. If \(t<n\), the visited positions are all distinct exactly when the arcs are pairwise disjoint as subsets of the cycle.

More generally, fix labeled arcs of positive integer lengths totaling \(L\le n\), with the first start anchored. A disjoint placement determines a clockwise permutation of the other \(k\) arc labels and \(k+1\) nonnegative gap lengths summing to \(n-L\). Conversely every such permutation and gap composition determines precisely one disjoint placement. Thus the number of choices of the other \(k\) starts is
\[
k!\binom{n-L+k}{k}=(n-L+1)^{\overline{k}}.
\]
Dividing by \(n^k\), and substituting \(L=t+1\), proves that the conditional no-repeat probability is \((n-t)^{\overline{k}}/n^k\), independently of the individual arc lengths or relocation times. The number of relocations is \(K\sim\operatorname{Bin}(t,q)\); averaging proves the finite formula. After \(n\) transitions there have been \(n+1\) visits to only \(n\) possible sites, so \(T_n\le n\) deterministically.

**Relocation monotonicity.** For fixed \(t<n\), the conditional survival factor \(f_t(k)=(n-t)^{\overline{k}}/n^k\) obeys
\[
\frac{f_t(k+1)}{f_t(k)}=\frac{n-t+k}{n}<1\qquad(0\le k<t).
\]
The binomial count \(K\) is strictly stochastically increasing in \(q\), giving strict decrease of the expectation of \(f_t(K)\) for every \(t\ge1\).

**Critical-window limit.** Fix \(0\le x<1\), and set \(t=\lfloor nx\rfloor\). If \(nq_n\to\lambda<\infty\), then \(K\sim\operatorname{Bin}(t,q_n)\) converges to \(\operatorname{Poisson}(\lambda x)\) and is tight. For each fixed \(k\),
\[
\frac{(n-t)^{\overline{k}}}{n^k}\longrightarrow(1-x)^k.
\]
Boundedness of these factors between zero and one gives
\[
\Pr(T_n>t)\longrightarrow\mathbb E(1-x)^{\operatorname{Poisson}(\lambda x)}=e^{-\lambda x^2}.
\]
For \(t=n-1\), the conditional factor is \(k!/n^k\): it tends to zero for each \(k\ge1\), whereas its value at zero is one. Poisson tightness implies \(\Pr(T_n=n)=\Pr(T_n>n-1)\to e^{-\lambda}\). Since \(0\le T_n/n\le1\), bounded convergence gives the claimed mean limit by integrating the survival function.

**Many-relocation limit.** Fix \(x>0\) and \(t=\lfloor xb_n\rfloor\), with \(b_n=\sqrt{n/q_n}\). The hypotheses imply \(t=o(n)\) and \(\mathbb EK=tq_n\sim x\sqrt{nq_n}\to\infty\). Binomial concentration yields \(K/(tq_n)\to1\) in probability. For all \(0\le K\le t\), Taylor expansion with a uniform remainder gives
\[
\log f_t(K)=-\frac{Kt}{n}+\frac{K(K-1)}{2n}
+O\!\left(\frac{Kt^2}{n^2}\right).
\]
The remainder is \(o_{\mathbb P}(1)\), since \(K=O_{\mathbb P}(tq_n)\) and \(q_nt^3/n^2=O((nq_n)^{-1/2})\). Meanwhile \(Kt/n\to x^2\) and \(K(K-1)/(2n)\to q_\infty x^2/2\) in probability. Thus \(f_t(K)\to e^{-(1-q_\infty/2)x^2}\) in probability, and boundedness allows taking expectations. At \(x=0\), survival converges to one. This establishes the stated weak limit.

## Verification

The accompanying `checker.py` uses only Python's standard library. Executing `python3 checker.py` runs independent exact-fraction transition-state recursions, enumerates relocation destinations for every relocation pattern on cycles of sizes \(2\) through \(7\), checks the gap-count formula, normalization, and strict finite-parameter monotonicity. The checker reports 438 exact comparisons. These finite checks detect normalization and indexing mistakes; the infinite-size conclusions follow from the analytic estimates above and do not depend on experimental extrapolation.

## Relationship to prior work

Villarroel, Montero and Vega study deterministic motion punctuated by resets to the original site, including escape and first-passage problems. Replacing a fixed reset destination by an independent uniform position on a finite directed cycle leads instead to a history-dependent first-repetition observable, which their escape-time formulas do not evaluate. Riascos and collaborators derive stationary and single-target first-passage quantities for walks with resets to fixed nodes on undirected networks, which likewise do not give the joint non-repetition event. Benjamini and Morris use birthday-type collisions for Markov-chain sampling complexity, rather than this finite exact first-repeat distribution. Random circular-arc placement is a classical enumerative ingredient; the gap enumeration here is not claimed as an independently novel circle-packing identity. The asserted contribution is its exact coupling to the finite walk and the complete scaling transition including its endpoint atom.

## Limitations

The uniform relocation distribution and a single deterministic clockwise successor are essential to the exact conditional packing count; arbitrary destination weights, steps in both directions, and other graph topologies are not covered. The many-relocation statement is a distributional limit, not a uniform error bound or a claim about expectations on that scale. Historical priority beyond the inspected sources remains subject to independent verification, particularly in older circular parking and regenerative scan literature.

## References

1. J. Villarroel, M. Montero and J. A. Vega, *A Semi-Deterministic Random Walk with Resetting*, preprint posted 7 June 2021, https://www.preprints.org/manuscript/202106.0151 ; journal version *Entropy* **23** (2021), 825, https://doi.org/10.3390/e23070825 .
2. A. P. Riascos, D. Boyer, P. Herringer and J. L. Mateos, *Random walks on networks with stochastic resetting*, arXiv:1910.13568, first posted 29 October 2019, https://arxiv.org/abs/1910.13568 .
3. I. Benjamini and B. Morris, *The birthday problem and Markov chain Monte Carlo*, arXiv:math/0701390, first posted 14 January 2007, https://arxiv.org/abs/math/0701390 .
4. A. F. Siegel and L. Holst, *Covering the Circle with Random Arcs of Random Sizes*, Stanford technical report, January 1981, https://statistics.stanford.edu/technical-reports/covering-circle-random-arcs-random-sizes .
