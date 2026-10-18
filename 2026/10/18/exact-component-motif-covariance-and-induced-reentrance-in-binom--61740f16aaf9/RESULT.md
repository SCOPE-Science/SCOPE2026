# Exact component–motif covariance and induced reentrance in binomial random graphs

## Finding

Fix two finite, simple, **connected** graphs \(H\) and \(F\), each with at least two vertices, and an integer \(n\ge\max\{|V(H)|,|V(F)|\}\). In \(G(n,p)\), \(0<p<1\), let \(N_H\) be the number of connected components isomorphic to \(H\). Let \(X_F^{\mathrm{ind}}\) count vertex subsets inducing \(F\), and let \(X_F^{\mathrm{sub}}\) count pairs consisting of a vertex subset and a spanning edge subset isomorphic to \(F\) (non-induced copies, counted once per distinct edge set).

Write \(h=|V(H)|\), \(f=|V(F)|\), \(e=|E(F)|\), \(q=\binom f2-e\), and \(c_F=f!/|\operatorname{Aut}(F)|\). Put
\[
B=c_F\left[\binom nf-\binom{n-h}{f}\right],\qquad
\psi_{\mathrm{ind}}(p)=p^e(1-p)^q,\qquad
\psi_{\mathrm{sub}}(p)=p^e,
\]
where binomial coefficients with an upper argument below \(f\) are zero. Let \(a_{\mathrm{ind}}(H,F)\) be the number of \(f\)-subsets of \(V(H)\) whose induced graph is \(F\), and let \(a_{\mathrm{sub}}(H,F)\) count the distinct spanning edge subsets isomorphic to \(F\) on all \(f\)-subsets of \(H\).

**Exact covariance and complete sign classification.** For either copy convention \(t\in\{\mathrm{ind},\mathrm{sub}\}\),
\[
\boxed{\operatorname{Cov}(N_H,X_F^t)
=\mathbb E[N_H]\big(a_t(H,F)-B\psi_t(p)\big).}
\]
In particular \(B>0\), \(\mathbb E[N_H]>0\), and the covariance's sign is determined by the displayed one-variable factor. If \(a_t=0\), the covariance is strictly negative for every \(0<p<1\). For non-induced copies, and for induced copies when \(F\) is complete, there is at most one interior zero, with sign changing only from positive to negative. For induced copies of noncomplete connected \(F\), put
\[
p_* = \frac e{e+q},\qquad M=\left(\frac e{e+q}\right)^e
\left(\frac q{e+q}\right)^q.
\]
If \(0<a_{\mathrm{ind}}/B<M\), there are exactly two interior zeroes \(p_-<p_*<p_+\), with signs \(+,-,+\). If \(a_{\mathrm{ind}}/B=M\), there is a unique tangential zero and the covariance is nonnegative elsewhere. If \(a_{\mathrm{ind}}/B>M\), the covariance is strictly positive throughout.

For \(H=F=P_3\), the three-vertex path, induced-copy reentrance occurs **for every \(n\ge4\)** and not for \(n=3\). More explicitly,
\[
\operatorname{Cov}(N_{P_3},X_{P_3}^{\mathrm{ind}})
=\mathbb E[N_{P_3}]\left(1-3\binom n3p^2(1-p)\right).
\]
For \(n=4\), this is \(12p^2(1-p)^4[1-12p^2(1-p)]\), giving two zeroes and covariance \(-3/32\) at \(p=1/2\). The two roots for general \(n\ge4\) satisfy
\[
3\binom n3p^2(1-p)=1,
\qquad p_-\sim \sqrt2\,n^{-3/2},\qquad 1-p_+\sim 2n^{-3}.
\]
For the same component statistic but *non-induced* path copies, the covariance factor becomes \(1-3\binom n3p^2\), so only a single positive-to-negative transition occurs.

## Assumptions and scope

The underlying probability space has one independent Bernoulli-\(p\) indicator for each of the \(\binom n2\) potential edges. Graph isomorphisms ignore vertex labels. Component counts count each maximal connected component once, not once per labeling. For induced copies each vertex subset contributes either zero or one. For non-induced copies an \(f\)-subset contributes the number of distinct \(F\)-edge patterns it contains. Both motifs are connected, which is essential to the exact decomposition. All identities hold **at finite \(n\)** and over the full open interval \(0<p<1\); no large-\(n\) approximation is used for the exact formula.

The mean needed above is explicitly
\[
\mathbb E[N_H]=\binom nh\frac{h!}{|\operatorname{Aut}(H)|}
 p^{|E(H)|}(1-p)^{\binom h2-|E(H)|+h(n-h)}.
\]

## Proof

Fix an \(h\)-element vertex set \(S\), and let \(A_S\) indicate that \(S\) induces a connected component isomorphic to \(H\). Conditional on \(A_S=1\), the graph on \(S\) is a uniformly labeled realization of \(H\), no edges join \(S\) and its complement, and the induced graph on the complement has the independent law \(G(n-h,p)\). Because \(F\) is connected, no copy of \(F\), under either counting convention, can meet both sides: a copy meeting both would contain an edge crossing the cut.

Consequently the conditional expected motif count is
\[
\mathbb E[X_F^t\mid A_S=1]
=a_t(H,F)+c_F\binom{n-h}{f}\psi_t(p),
\]
while unconditionally \(\mathbb E[X_F^t]=c_F\binom nf\psi_t(p)\). Therefore
\[
\operatorname{Cov}(A_S,X_F^t)=\Pr(A_S=1)
\big(a_t(H,F)-B\psi_t(p)\big).
\]
Sum over all \(h\)-sets \(S\). Since \(N_H=\sum_S A_S\), covariance linearity yields the displayed identity; summing the positive probabilities \(\Pr(A_S=1)\) gives the stated mean.

Since \(F\) is connected and has at least two vertices, \(e\ge1\). For non-induced copies, \(p^e\) is strictly increasing. The induced law has \(q=0\) exactly when \(F\) is complete; otherwise \(q\ge1\) and logarithmic differentiation gives \(\psi'_{\mathrm{ind}}/\psi_{\mathrm{ind}}=e/p-q/(1-p)\), positive before \(p_*\), negative afterward, and zero only at \(p_*\). Its values tend to zero at both endpoints. These observations prove all stated sign cases, including tangency.

For \(H=F=P_3\), there is one induced and one non-induced copy inside \(H\), and \(c_F=3\). Since \(h=f=3\), \(B=3\binom n3\). The maximum of \(p^2(1-p)\) is \(4/27\). For \(n=3\), \(B(4/27)=4/9<1\); for \(n\ge4\), \(B(4/27)\ge16/9>1\). This proves the minimal size and two-root characterization. Using \(B=n(n-1)(n-2)/2\), the lower root obeys \(p_-\to0\) and \(Bp_-^2(1-p_-)=1\), giving \(p_-\sim B^{-1/2}\sim\sqrt2n^{-3/2}\); the upper root obeys \(p_+\to1\), giving \(1-p_+\sim B^{-1}\sim2n^{-3}\). Substitution at \(n=4,p=1/2\) gives the claimed \(-3/32\).

## Verification

The companion `verify.py` uses exhaustive enumeration of all labeled simple graphs of sizes \(2\) through \(5\), exact rational edge probabilities \(1/4,1/3,1/2,3/4\), and six distinct connected motif types (edge, path, triangle, four-path, four-cycle, four-clique). It independently computes weighted mixed moments and the formula for both copy conventions. Running `python verify.py` gives **660 exact-rational covariance and phase assertions passed**. It also checks the size-four reentrant example. Exhaustive enumeration is finite evidence only; the general proof above establishes the all-size theorem.

## Relationship to prior work

Ráth, *A moment-generating formula for Erdős–Rényi component sizes* (arXiv:1707.05169, 2017), gives an exact change-of-measure relation for the size of the component of a distinguished vertex (Proposition 1.1 and Lemma 2.1). It motivates conditioning on component events, but does not identify mixed covariances between fixed component **types** and connected induced/non-induced motif counts or classify their \(p\)-dependent signs. The conditioning/decomposition technique itself is classical and is not presented as novel.

Sah and Sawhney, *Local limit theorems for subgraph counts* (arXiv:2006.11369, 2020; journal 2022), treat local limit laws and graph-factor decompositions for ordinary and induced subgraph counts. Their full open-access article examines marginal fluctuations, not the conditional component–motif covariance above. Ellis and Ferry, *Variance of the subgraph count for sparse Erdős–Rényi graphs* (2010), develop subgraph-overlay variance formulas, but do not in the accessible material state the mixed component–motif sign phase diagram.

The mathematical advance claimed here is the exact all-types **cross-covariance sign classification** and the qualitative induced/non-induced difference, not classical component probabilities or subgraph expectations.

## Limitations

The formula assumes independent edges and connected motif \(F\); disconnected motifs can straddle the component boundary. The endpoints \(p=0,1\) are excluded from sign claims because the component mean may vanish. A positive covariance is not an independence criterion. The graph-counting convention distinguishes induced vertex-set counts from non-induced edge-subgraph counts. The analysis does not identify all correlations or joint distributions. Earlier general mixed-moment or graph-overlay identities may implicitly contain this specialization; historical priority requires independent checking. There has been no independent audit.

## References

1. B. Ráth, *A moment-generating formula for Erdős–Rényi component sizes*, arXiv:1707.05169 (first posted 2017-07-17); Electronic Communications in Probability **23** (2018).
2. A. Sah and M. Sawhney, *Local limit theorems for subgraph counts*, arXiv:2006.11369 (first posted 2020-06-19); Journal of the London Mathematical Society **105** (2022), 950–1011, DOI:10.1112/jlms.12523.
3. R. B. Ellis and J. P. Ferry, *Variance of the subgraph count for sparse Erdős–Rényi graphs*, Discrete Applied Mathematics **158** (2010), 649–658, DOI:10.1016/j.dam.2009.11.012.
