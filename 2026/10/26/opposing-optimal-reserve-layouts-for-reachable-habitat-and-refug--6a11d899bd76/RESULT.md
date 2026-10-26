# Opposing optimal reserve layouts for reachable habitat and refuge connectivity on a cyclic landscape

## Finding

**Theorem (distributional reserve-spacing tradeoff).** Fix integers \(n\ge3\), \(2\le k\le n\), and \(0<p<1\). On the cycle \(C_n\), choose \(k\) protected habitat patches that always remain functional; each of the other \(n-k\) patches independently remains functional with probability \(p\). Adjacency means consecutive patches on the original cycle. Let \(R\) be the number of functional patches in components that contain at least one protected patch, and let \(J\) indicate that all protected patches belong to the same functional component.

Write \(S=n-k\), and denote the successive numbers of unprotected patches between protected patches by the cyclic gap vector \(L=(L_1,\ldots,L_k)\), where \(L_i\ge0\) and \(\sum_i L_i=S\). For every threshold \(r\), the following simultaneous bounds hold:

\[
\Pr(R_{\mathrm{clustered}}\ge r)\le\Pr(R_L\ge r)\le\Pr(R_{\mathrm{balanced}}\ge r).
\]

Here the clustered vector is any permutation of \((S,0,\ldots,0)\); in a balanced vector the gaps differ by at most one. Thus balanced placement maximizes *every* upper tail of rescued habitat, whereas clustering minimizes every upper tail. The inequality may be an equality for distinct layouts: replacing two gaps \((2,0)\) by \((1,1)\) leaves the entire law of \(R\) unchanged.

By contrast, the probability that all protected patches are mutually connected obeys

\[
\Pr(J_{\mathrm{balanced}}=1)\le \Pr(J_L=1)\le\Pr(J_{\mathrm{clustered}}=1)=1.
\]

Every nontrivial two-gap balancing operation strictly decreases this connectivity probability. Moreover, the information-theoretic ceiling \(R\preceq k+\mathrm{Binomial}(S,p)\) is attained in distribution by some layout *if and only if* \(S\le2k\), equivalently \(n\le3k\); for a given layout the ceiling is attained exactly when each gap has length at most two. These are finite-sample, all-parameter claims for the stated static model, not assertions of population persistence in a dynamic metapopulation.

## Assumptions and scope

A protected patch is always functional and serves as a possible connection source; every unprotected patch independently survives with identical probability \(p\). The functional network is the vertex-induced subgraph on surviving patches. A surviving unprotected patch contributes to \(R\) if a path made entirely of functional patches leads to *at least one* protected patch. Multiple protected patches need not be mutually connected for their separate reachable components to count. The connectivity indicator \(J\) instead requires *all* \(k\) protected patches to lie in one connected component. No passage through a failed patch, long-distance transport, recolonization process, environmental dependence, or temporal dynamics is assumed. Vertex count includes protected patches, so \(k\le R\le n\).

All placements on a cycle have a nonnegative integer cyclic gap vector summing to \(S\), and every such vector is realized by a placement, up to cyclic rotation. Statements concerning strict changes refer to a single pair of gaps \(a\ge b+2\) replaced by \(a-1,b+1\), all other gaps unchanged. The coverage law is unchanged only for the elementary pair \((a,b)=(2,0)\), although this pair always strictly changes the protected-connectivity probability when \(p\in(0,1)\).

## Proof

**1. Exact one-gap distribution and independence.** Let \(X_\ell\) be the number of functional unprotected patches in a gap of length \(\ell\) that can reach at least one of its protected endpoints. For \(\ell=0\), \(X_0=0\). For \(\ell\ge1\), if the gap contains at least two failed patches, the reached vertices are precisely a run of functional vertices at the left endpoint and a run at the right endpoint, with two endpoint-run failures separating them. The number of placements of these two runs with total length \(j\le\ell-2\) is \(j+1\). If exactly one site fails, precisely \(\ell-1\) sites are reached; if none fails, all \(\ell\) are reached. Thus, setting \(q=1-p\),

\[
\Pr(X_\ell=j)=
\begin{cases}
(j+1)q^2p^j,&0\le j\le \ell-2,\\
\ell q p^{\ell-1},&j=\ell-1,\\
p^\ell,&j=\ell.
\end{cases}
\]

Let \(Q_0(z)=1\) and, for \(\ell\ge1\),

\[
Q_\ell(z)=q^2\sum_{j=0}^{\ell-2}(j+1)(pz)^j+\ell q(pz)^{\ell-1}+(pz)^\ell.
\]

The gaps have independent survival states, so \(R=k+\sum_iX_{L_i}\) and \(\mathbb E[z^{R-k}]=\prod_iQ_{L_i}(z)\). This fully determines the distribution for every layout.

**2. Pair balancing improves all tails.** We show coefficientwise, for all integers \(a\ge b+2\ge2\),

\[
Q_a(z)Q_b(z)-Q_{a-1}(z)Q_{b+1}(z)=(1-z)E_{a,b}(z),
\]

where every coefficient of \(E_{a,b}\) is nonnegative, and some coefficient is positive unless \((a,b)=(2,0)\). For \(b=0\), direct subtraction using \(Q_1= q+pz\) gives

\[
E_{a,0}(z)=p q^2\sum_{j=0}^{a-3}(j+1)(pz)^j,
\]

with the empty sum understood as zero. For \(b\ge1\), let \(h=a-1\), \(d=h-b\ge1\), and write \(t=pz\). From the displayed distribution one checks

\[
Q_{\ell+1}(z)-Q_\ell(z)=p(z-1)(pz)^{\ell-1}(pz+\ell q),\qquad\ell\ge1.
\]

Hence

\[
E_{a,b}(z)=p\,t^{b-1}H_{h,b}(t),\qquad
H_{h,b}(t)=(t+bq)Q_h(t/p)-t^d(t+hq)Q_b(t/p).
\]

The coefficients \(c_j=[t^j]H_{h,b}(t)\) are exactly

\[
 c_j=\begin{cases}
 bq^3,&j=0,\\
 q^2\bigl(j+bq(j+1)\bigr),&1\le j\le d-1,\\
 dq^2\bigl(1+q(h-j-1)\bigr),&d\le j\le h-2,\\
 dq^2,&j=h-1,\\
 0,&j\ge h,
 \end{cases}
\]

where ranges with lower bound above upper bound are empty. This follows by multiplying the explicit three-term expressions for \(Q_h\) and \(Q_b\), then canceling the coefficients for powers at least \(h\). As \(b,d\ge1\) and \(q>0\), each displayed nonzero coefficient is strictly positive. The two polynomials on the left have total mass one. For any two probability generating functions \(A(z),B(z)\), the coefficient of \(z^j\) in \((A-B)/(1-z)\) is the difference of their cumulative masses through \(j\), equivalently \(\Pr(B\text{-variable}\ge j+1)-\Pr(A\text{-variable}\ge j+1)\). Thus the coefficientwise positivity proves that the balanced pair stochastically dominates the unbalanced pair. Multiplication by every other gap's nonnegative-coefficient PGF preserves that order and preserves strictness if a positive coefficient exists. Repeated balancing reaches a vector whose entries differ by at most one. Reversing majorization transfers reaches the clustered vector, proving both global distributional bounds.

**3. Mutual connectivity reverses the order.** All \(k\) protected vertices are connected on a cycle if and only if at most one of its \(k\) gaps contains any failed vertex. The gap-completion indicators are independent, with \(\Pr(\text{gap }i\text{ complete})=p^{L_i}\). Therefore, including zero-length gaps,

\[
\Pr(J=1)=\prod_i p^{L_i}+\sum_i(1-p^{L_i})\prod_{j\ne i}p^{L_j}
=p^S\left(\sum_i p^{-L_i}-(k-1)\right).
\]

For a balancing step \(a\ge b+2\), strict convexity of \(x\mapsto p^{-x}\) gives \(p^{-a}+p^{-b}>p^{-(a-1)}+p^{-(b+1)}\). The connectivity probability therefore strictly *decreases* at every balancing step. The extreme layouts follow. A clustered placement has all protected patches consecutive, so they are connected with probability one.

**4. Sharp coverage ceiling and threshold.** For any placement, \(R\) is at most the number \(k+Y\) of all functional sites, where \(Y\sim\mathrm{Binomial}(S,p)\); this is a pointwise coupling and hence implies stochastic dominance. If every gap length is at most two, each surviving unprotected patch neighbors a protected patch, so \(R=k+Y\) pointwise. Conversely, if any gap has length at least three, the positive-probability local pattern 'failed, functional, failed' traps a surviving patch away from both protected endpoints. On that event \(R<k+Y\), and equality in distribution is impossible because these variables are bounded and differ in expectation under the coupling. A vector of \(k\) gaps with total \(S\) and maximum two exists precisely when \(S\le2k\). This proves the threshold.

**5. An exact illustrative comparison.** On eight patches with two protected patches, take \(p=1/2\). For clustered gaps \((6,0)\), \(\mathbb E R=31/8\) and \(\Pr(J=1)=1\). For balanced gaps \((3,3)\), \(\mathbb E R=19/4\) and \(\Pr(J=1)=15/64\). The larger reachable habitat from spreading refuges comes with much lower probability that those refuges are mutually connected.

## Verification

The standalone `verify.py` reconstructs the gap laws and connectivity formula, directly enumerates independent functional/failed states for small cycles, and verifies the balancing inequalities and all-parameter symbolic coefficient pattern on finite rational instances. Running `python3 verify.py` produces the embedded `certificate.json`; the exact arithmetic uses Python's `fractions.Fraction` and has no external dependencies. The certificate counts 742 direct state enumerations, 2,523 pair-balancing checks, 351 exact rational coefficient tests, 924 global coverage extrema, 924 connectivity extrema, 150 exact coverage-ceiling cases, and 48 gap-law checks. This finite corroboration is not the proof for arbitrary \(n,k,p\); the proof is the coefficient identity, repeated balancing, and exact connectivity formula above.

## Relationship to prior work

Wagner, Ross, and Possingham (2003) provide an explicit ecological motivation for competing reserve objectives arising from proximity, colonization and correlated catastrophes. Their two-reserve dynamic Markov model maximizes quasi-stationary survival, not the static distribution of habitat reachable from multiple guaranteed surviving sites on a Bernoulli-damaged cycle. Hof and Flather (1996) study connected habitat placement with environmental correlation, but in a different spatial optimization model. Blowes and Connolly (2012) investigate risk spreading and connectivity of reserves; the abstract and metadata studied do not provide an identifiable implication yielding the present two-order theorem, though complete-text comparison remains a residual risk. Frasca, Garin, Gerencsér, and Hendrickx (2014) investigate unreliable sensors and expected maximum one-dimensional geographic distance to an active sensor, where sensors rather than interstitial habitat fail; their objective, failure mechanism and expected-value statement do not imply the simultaneous tail inequalities and reversed terminal-connectivity extremum here. Standard graph reliability and percolation could contain an equivalent result under a different terminology; novelty is not certified by unsuccessful searches.

## Limitations

The protected sites never fail. All other sites have independent, identical survival; failures are site removals, not edge removals or spatially correlated catastrophes. The cycle topology and the static reachability definition are essential. The finding does not assert extinction risk, colonization rates, species persistence, or similar conclusions for real ecological communities. Strict stochastic ordering does not distinguish the \((2,0)\) and \((1,1)\) elementary placements; equality can occur despite distinct reserve layouts. The comparisons do not establish a unique best layout without additional conditions. Primary-source coverage and independent validation remain incomplete.

## References

1. L. Wagner, J. Ross, and H. Possingham, *Catastrophe Management and Inter-Reserve Distance for Marine Reserve Networks*, arXiv:math/0309255 (first publicly posted 2003-09-16), https://arxiv.org/abs/math/0309255.
2. P. Frasca, F. Garin, B. Gerencsér, and J. M. Hendrickx, *Optimal One-Dimensional Coverage by Unreliable Sensors*, arXiv:1404.7711 (first publicly posted 2014-04-30), https://arxiv.org/abs/1404.7711.
3. S. A. Blowes and S. R. Connolly, *Risk spreading, connectivity, and optimal reserve spacing*, *Ecological Applications* (2012), https://doi.org/10.1890/11-0952.1.
4. J. Hof and C. Flather, *Accounting for Connectivity and Spatial Correlation in Optimal Placement of Wildlife Habitat*, *Ecological Modelling* 89 (1996), 143–155.
