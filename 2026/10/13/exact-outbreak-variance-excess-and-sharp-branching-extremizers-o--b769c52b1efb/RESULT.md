# Exact outbreak-variance excess and sharp branching extremizers on rooted contact trees

## Finding

A finite rooted contact tree can have precisely the outbreak **mean** predicted by independent Bernoulli bond percolation, while having a strictly larger outbreak **variance**. For the conditional outward-transmissibility SIR model below, the discrepancy is exactly

\[
\operatorname{Var}(Z_T)-\operatorname{Var}(Z_T^{\mathrm{BP}})
=2vB_T(q),\qquad
B_T(q)=\sum_{\substack{\{u,w\}\subseteq V(T)\\u\parallel w}}
q^{d(u)+d(w)-d(\ell(u,w))-2}.
\]

Here \(u\parallel w\) means that neither vertex lies on the root-to-other path, and \(\ell\) is the lowest common ancestor. For \(n\ge3\), each rooted tree with at least one branch satisfies the sharp inequalities

\[
q^{n-3}\le B_T(q)\le\binom{n-1}{2}.
\]

The **unique** lower extremizer among branching rooted trees is a terminal binary broom: a path from the root ending in precisely two leaf children. The **unique** upper extremizer is the centered star. For \(n=3\) these shapes coincide. If there is no branch (the root is an endpoint of a path), \(B_T(q)=0\). These uniqueness assertions refer to \(B_T\) or, for \(v>0\), to the variance excess; if \(v=0\), the excess is zero for every rooted tree.

## Assumptions and scope

Let \(T=(V,E)\) be any finite simple undirected tree with \(n=|V|\) vertices, rooted at \(o\), with the **single initial infection** at \(o\) and no imported infections subsequently. At each vertex \(i\), independently sample \(Q_i\in[0,1]\) from a common distribution with

\[
q=\mathbb E Q_i\in(0,1),\qquad v=\operatorname{Var}(Q_i)\ge0.
\]

Conditional on the entire family \((Q_i)\), trial variables \(X_{i\to j}\) for oriented tree edges are independent, with \(\mathbb P(X_{i\to j}=1\mid Q)=Q_i\). Only the direction from each parent toward each child can contribute to transmission starting at the root. Infection is transmitted to a child if and only if all trials on its unique root-to-child path succeed. The total number of ever-infected vertices is \(Z_T\). For comparison, let \(Z_T^{\mathrm{BP}}\) be the size of the root component when the **undirected** edges are independently open with common probability \(q\).

This model includes independent identically distributed recovery times \(U_i\) with conditional contact-before-recovery probability \(Q_i=F(U_i)\), provided all edge-specific first-contact intervals are mutually independent and independent of the recovery times, with common distribution function \(F\). In particular, for rate-\(\beta\) Poisson contacts and rate-\(\gamma\) exponential recoveries,

\[
q=\frac{\beta}{\beta+\gamma},\qquad
v=\frac{\gamma\beta^2}{(\gamma+2\beta)(\gamma+\beta)^2}
=\frac{q^2(1-q)}{1+q}.
\]

No network cycles, multiple seeds, inter-host correlation in \(Q\), or imports are included in the conclusion.

## Proof

**Step 1: single-node probabilities and the mean.** For any vertex \(u\), denote by \(P(o,u)\) the set of oriented edges on the unique path from the root to \(u\), with the empty product equal to one for \(u=o\). The infection indicator is

\[
I_u=\prod_{(i\to j)\in P(o,u)} X_{i\to j}.
\]

Every edge along this simple path has a distinct *parent*, so its trial depends on a different independent \(Q_i\). Therefore

\[
\mathbb E I_u=q^{d(u)}.
\]

The same identity holds for the root-component indicator in independent bond percolation. Summation over all vertices proves the two means are equal and equal to \(\sum_u q^{d(u)}\).

**Step 2: exact pair-probability discrepancy.** Fix distinct vertices \(u,w\). If one is an ancestor of the other, the event that both are infected is exactly the event that the descendant is infected. Consequently its probability coincides in both models.

Otherwise the two root paths separate at their lowest common ancestor \(a=\ell(u,w)\). Their union has

\[
L=d(u)+d(w)-d(a)
\]

edges. Exactly two of these edges leave the same parent, namely \(a\), one into each branch. Every other edge in the union leaves a distinct parent. Independence across parent transmissibilities and conditional independence of trials thus give

\[
\mathbb E[I_uI_w]
=\mathbb E[Q_a^2]q^{L-2}
=(q^2+v)q^{L-2},
\]

whereas independent bond percolation has corresponding joint probability \(q^L\). Hence the difference is \(v q^{L-2}\). Because each individual indicator has the same marginal distribution in both models, expanding the variance of the sum \(Z_T=\sum_u I_u\) cancels all individual variance terms and every comparable-pair covariance. The remaining unordered pairs occur twice, proving

\[
\operatorname{Var}(Z_T)-\operatorname{Var}(Z_T^{\mathrm{BP}})
=2v\sum_{u\parallel w}q^{d(u)+d(w)-d(\ell(u,w))-2}.
\]

No limiting approximation or independence of infection indicators has been used.

**Step 3: zero excess for rooted paths.** If every vertex has at most one child, the rooted tree is a path whose root is an endpoint, and every pair of vertices is comparable. Thus \(B_T=0\). Conversely, if some vertex has at least two children, that child pair is incomparable and contributes a strictly positive term, because \(q\in(0,1)\). Therefore \(B_T=0\) precisely for endpoint-rooted paths.

**Step 4: upper bound and equality.** Every incomparable pair consists of two nonroot vertices. There are at most \(\binom{n-1}{2}\) such pairs; each term in \(B_T\) is at most one because its exponent is a nonnegative integer and \(q\in(0,1)\). Thus

\[
B_T(q)\le\binom{n-1}{2}.
\]

Equality requires every two nonroot vertices to be incomparable. If any nonroot vertex had a child, that pair would be comparable, yielding strict inequality. Hence equality forces all nonroot vertices to be children of the root, i.e. the centered star. In that star every pair of distinct leaves contributes \(q^0=1\), so the bound is attained.

**Step 5: lower bound and equality among branching trees.** Choose a branching vertex \(a\) at depth \(k\), and two of its children. The root-to-\(a\) path has \(k+1\) vertices, and adding the children accounts for \(k+3\) distinct vertices. Thus \(k\le n-3\). Those two children contribute exactly \(q^k\), which is at least \(q^{n-3}\). All other contributions to \(B_T\) are nonnegative, proving

\[
B_T(q)\ge q^{n-3}.
\]

If equality holds, strict decrease of \(q^k\) in \(k\) forces \(k=n-3\), so the root-to-\(a\) path and two children exhaust all \(n\) vertices. This gives exactly the terminal binary broom, with precisely one incomparable pair and contribution \(q^{n-3}\). Conversely, the broom attains equality. For \(n=3\), this broom is the centered star. Multiplication by \(2v\) yields the stated extremal excess-variance bounds; uniqueness requires \(v>0\).

**Step 6: continuous-time SIR specialization.** If \(U\) is exponential of rate \(\gamma>0\) and independent contact intervals have exponential rate \(\beta>0\), then \(Q=1-e^{-\beta U}\). Direct Laplace-transform evaluation yields

\[
\mathbb E Q=1-\frac{\gamma}{\gamma+\beta}=q,
\quad \mathbb E Q^2=1-\frac{2\gamma}{\gamma+\beta}+\frac{\gamma}{\gamma+2\beta}.
\]

Subtracting \(q^2\) proves the expression for \(v\) above.

## Verification

The standalone script `verify_tree_variance.py` uses exact rational arithmetic and no nonstandard dependencies. For each rooted increasing-parent encoding on up to seven vertices, it exhaustively enumerates all configurations of oriented forward-edge trials with an independently sampled two-point transmissibility distribution

\[
\mathbb P(Q_i=1/4)=\mathbb P(Q_i=3/4)=1/2,
\quad q=1/2,\quad v=1/16.
\]

It independently computes the exact distribution of outbreak size in correlated-outgoing SIR and in bond percolation, compares their first and second moments to the proposed weighted-pair formula, and checks the sharp lower and upper bounds for each size. Counts of topologically labeled rooted trees examined for \(n=1,2,3,4,5,6,7\) are respectively \(1,1,2,6,24,120,720\). It additionally verifies the Poisson/exponential special-case variance algebra with rational rates. Replay with `python3 verify_tree_variance.py` yields `VERIFY_OK`. The exhaustive calculation covers only the stated finite encodings and distribution; the preceding proof handles every finite rooted tree and admissible transmissibility law.

## Relationship to prior work

Hiraoka and Saramäki (2026, arXiv:2610.03573v1) prove that on trees the marginal infection probabilities, and hence the expected outbreak size, can match independent bond percolation despite dependence among outgoing transmissions (Section IV.3). Their Appendix A isolates common-recovery-induced covariance, and Section VI empirically observes excess variance of a largest-component statistic on large random graphs. Those facts are antecedents, not claimed as new here. The theorem above gives the **exact finite rooted-tree single-seed outbreak-size variance difference**, expressed as a weighted sum over precisely the incomparable pairs, together with **sharp extremizers at every finite vertex count**; those statements are not established in the inspected sections.

Kenah and Robins (2007, doi:10.1103/PhysRevE.76.036113) establish an exact semi-directed epidemic-percolation representation and show the bond-percolation distribution can be wrong. Their general representation can in principle compute moments but does not itself state the fixed-tree excess polynomial or its rooted-shape extremizers. Ramírez-Ramírez and Thompson (2013/2014, doi:10.1007/s11009-013-9325-z, Section 3.2 and equations 8–11) derive outbreak-variance expressions for **random network degree distributions**, including common infectious-period effects. Their calculations are an important overlapping framework; they do not provide a fixed finite rooted-tree LCA expansion or sharp star-versus-terminal-broom extrema. Wilkinson and Sharkey (2018, doi:10.1103/PhysRevE.97.052403) prove stochastic-order results for infection reachability as infectious-period variability changes, a distinct observable from this outbreak-size variance at fixed marginal transmissibility.

## Limitations

The theorem compares outbreak variances **on the same fixed rooted tree**; it does not claim that a centered star maximizes the raw outbreak variance across different shapes. No inequality is asserted for networks with cycles, heterogeneous transmissibility means, correlated latent transmissibilities between distinct vertices, or more than one initial seed. The conclusion is a finite-population exact identity, not a major-epidemic threshold or an asymptotic law. The exact variance formula presumes the single seed is known. General outbreak-variance frameworks predate this result; its distinct contribution is the finite-tree discrepancy polynomial with a complete sharp branching-shape classification. Further literature may contain equivalent formulas not captured by the inspected sources.

## References

1. Takayuki Hiraoka and Jari Saramäki, *Disentangling epidemics and percolation*, arXiv:2610.03573v1 (publicly submitted 2 October 2026), https://arxiv.org/html/2610.03573v1 .
2. Eben Kenah and James M. Robins, *Second look at the spread of epidemics on networks*, Physical Review E 76, 036113 (2007), doi:10.1103/PhysRevE.76.036113; full text https://pmc.ncbi.nlm.nih.gov/articles/PMC2215389/ .
3. Lilia L. Ramírez-Ramírez and Mary E. Thompson, *Applications of the Variance of Final Outbreak Size for Disease Spreading in Networks*, Methodology and Computing in Applied Probability 16, 839–862 (2014; first published online 2013), doi:10.1007/s11009-013-9325-z; full text https://smm.org.mx/eventos/covid19/files/pdfs/019_ApplicationsoftheVarianceofFinal.pdf .
4. Robert R. Wilkinson and Kieran J. Sharkey, *Impact of the infectious period on epidemics*, Physical Review E 97, 052403 (2018), doi:10.1103/PhysRevE.97.052403; full text https://pmc.ncbi.nlm.nih.gov/articles/PMC7217532/ .
5. K. J. Sharkey, I. Z. Kiss, R. R. Wilkinson, and P. L. Simon, *Exact Equations for SIR Epidemics on Tree Graphs*, Bulletin of Mathematical Biology 77 (2015), doi:10.1007/s11538-013-9923-5 (online 2013), https://link.springer.com/article/10.1007/s11538-013-9923-5 .
