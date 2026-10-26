# Reciprocal cycles repel every longer directed cycle in fixed-outdegree digraphs

## Finding

For integers \(n\ge3\) and \(1\le k\le n-1\), independently at each vertex \(v\) of the labeled set \(\{1,\ldots,n\}\), choose uniformly a \(k\)-element subset of the other vertices and direct arcs from \(v\) to the chosen vertices. This produces a loop-free directed graph with distinct outgoing targets and exactly \(k\) outgoing arcs per vertex.

For \(2\le r\le n\), let \(C_r\) count the directed simple cycles of length \(r\), where two cyclically rotated vertex lists represent the same cycle, but reversing direction generally represents a different cycle. In particular, \(C_2\) counts reciprocal vertex pairs (directed two-cycles). Define \((n)_r=n(n-1)\cdots(n-r+1)\).

**Theorem.** For every integer \(3\le\ell\le n\),

\[
\operatorname{Cov}(C_2,C_\ell)
=-\frac{(n)_\ell k^\ell(n-k-1)^2(2n-\ell-1)}{2(n-1)^{\ell+2}(n-2)^2}.
\]

Thus the covariance is **strictly negative** whenever \(1\le k\le n-2\), and is zero when \(k=n-1\), in which case the graph is deterministic. This simultaneous finite-size assertion covers *every* longer simple directed-cycle length, including Hamiltonian cycles.

The sign is opposite in the independent-arc directed Erdős–Rényi graph, where every potential nonloop arc is included independently with probability \(p\in(0,1)\):

\[
\operatorname{Cov}_{D(n,p)}(C_2,C_\ell)
=(n)_\ell p^{\ell+1}(1-p)>0.
\]

Both models have the same expected outdegree when \(p=k/(n-1)\). For fixed positive integer \(k\) and fixed \(\ell\ge3\), as \(n\to\infty\), the first covariance is \(-k^\ell/n+O(n^{-2})\). For a fixed \(\ell\ge3\) and any sequence with \(k/(n-1)\to\rho\in(0,1)\),

\[
\frac{\operatorname{Cov}(C_2,C_\ell)}{n^{\ell-1}}\longrightarrow-\rho^\ell(1-\rho)^2.
\]

## Assumptions and scope

The choices made by distinct source vertices are independent. Within a source vertex, the \(k\) distinct targets are sampled **without replacement**. The graph is directed, arcs are retained with their orientations, loops and repeated outgoing targets are forbidden, and a cycle has pairwise distinct vertices. Neither strong-connectivity conditioning nor any constraint on indegrees is imposed. All expectations are taken over this exact finite probability space.

For comparison, \(D(n,p)\) has independent Bernoulli indicators for all ordered pairs of distinct vertices. In the fixed-outdegree model the cycle-count expectations are

\[
\mathbb E C_2=\binom n2\left(\frac{k}{n-1}\right)^2,
\qquad
\mathbb E C_\ell=\frac{(n)_\ell}{\ell}\left(\frac{k}{n-1}\right)^\ell.
\]

## Proof

Put \(p=k/(n-1)\) and \(q=k(k-1)/((n-1)(n-2))\). A specified outgoing arc from one source has probability \(p\); any two specified distinct arcs with the same source occur jointly with probability \(q\), including \(q=0\) when \(k=1\). Different sources are independent.

Fix one possible directed simple cycle \(\Gamma\) of length \(\ell\). For each unordered pair \(\{u,v\}\), let \(I_{uv}\) be the indicator that both arcs \(u\to v\) and \(v\to u\) are present. The product of the marginal probabilities of \(I_{uv}\) and the indicator \(I_\Gamma\) is always \(p^{\ell+2}\). The joint probability and the number of candidate pairs fall into four exhaustive cases:

1. Both vertices of the pair lie outside \(\Gamma\): the source choices are disjoint and the covariance contribution is zero.
2. Exactly one vertex of the pair lies on \(\Gamma\): there are \(\ell(n-\ell)\) such pairs, each with joint probability \(p^\ell q\).
3. Both vertices lie on \(\Gamma\) but are nonconsecutive on its underlying cycle: there are \(\ell(\ell-3)/2\) such pairs, each with joint probability \(p^{\ell-2}q^2\).
4. Both vertices are consecutive on \(\Gamma\): there are \(\ell\) such pairs, each with joint probability \(p^{\ell-1}q\). One of the two reciprocal arcs already belongs to \(\Gamma\), while its reverse is an additional required arc from the next source.

Consequently, with \(r=q/p^2=(k-1)(n-1)/(k(n-2))\),

\[
\begin{aligned}
\operatorname{Cov}(C_2,I_\Gamma)
&=\ell(n-\ell)p^\ell(q-p^2)
  +\frac{\ell(\ell-3)}2p^{\ell-2}(q^2-p^4)
  +\ell\bigl(p^{\ell-1}q-p^{\ell+2}\bigr)\\
&=\ell p^{\ell+2}\left[(n-\ell)(r-1)+\left(\frac rp-1\right)
    +\frac{\ell-3}2(r^2-1)\right]\\
&=-\ell p^{\ell+2}
 \frac{(n-k-1)^2(2n-\ell-1)}{2k^2(n-2)^2}.
\end{aligned}
\]

The last equality is an exact polynomial identity after multiplying by \(2k^2(n-2)^2\); an independent coefficient-level check is included in `verify.py`. There are exactly \((n)_\ell/\ell\) possible directed \(\ell\)-cycles. Summing the last identity over them and substituting \(p=k/(n-1)\) proves the theorem. Because \(2n-\ell-1\ge n-1>0\), the sign assertion holds throughout the stated domain; \(k=n-1\) makes every outgoing row complete, giving the zero boundary directly.

For the independent-arc model, each of the \((n)_\ell/\ell\) possible \(\ell\)-cycles has precisely \(\ell\) reciprocal dyads sharing one required arc. Every other reciprocal-dyad indicator uses distinct arc variables and hence has zero covariance with its cycle indicator. Each shared-arc pair contributes \(p^{\ell+1}(1-p)\), establishing the stated positive covariance. The fixed-\(k\) and dense-regime limits follow by dividing the exact rational expression by its leading powers of \(n\), with \(\ell\) held fixed.

## Verification

The self-contained Python 3 script `verify.py` checks the cleared-denominator polynomial identity by sparse polynomial coefficient arithmetic in \(n,k,\ell\). It independently recomputes joint probabilities by taking unions of required outgoing-arc sets for all reciprocal pairs and possible longer cycles when \(3\le n\le7\) and \(1\le k\le n-1\), giving 70 exact-rational parameter strata. It also enumerates every directed graph in the model for \(3\le n\le5\), giving 20 exact-rational parameter strata; both approaches reproduce the formula. The recorded command is `python verify.py`, with output `POLYNOMIAL_IDENTITY_PASS`, `EVENT_EXACT_PROBABILITY_PASS`, `EXHAUSTIVE_DIGRAPHS_PASS`, and `VERIFY_OK`.

The unrestricted theorem is proved analytically above. Finite enumeration is a diagnostic, not an infinite proof.

## Relationship to prior work

Sood and Yağan (2019) formulate the independently sampled distinct-neighbor random \(K\)-out construction, then discard arc orientations to study connectivity and giant components. Holm and collaborators (2019) investigate component-boundary edges and related sampling models for random \(k\)-out subgraphs. Cai and Devroye (2015) treat a random automaton model allowing loops/repeated outgoing targets and discuss its simple-digraph variant; their cycle theorems concern asymptotic structure outside the giant component. These results motivate the present fixed-row directed model but do not supply the exact mixed covariance of reciprocal cycles and all longer simple cycles. The comparison to independent-arc sampling is included because identical expected outdegree does not preserve the covariance sign.

## Limitations

The result does not treat random digraphs with **both** indegree and outdegree prescribed, directed cycles with repeated vertices, or sampling outgoing targets with replacement. It gives cross-covariances with \(C_2\), not the entire cycle-count covariance matrix or a general negative-association theorem. Historical priority of the exact identity has not been independently certified; more general enumerative formulae for fixed-row binary matrices could conceivably imply it.

## References

1. M. Sood and O. Yağan, *On the Strength of Connectivity of Inhomogeneous Random K-out Graphs*, arXiv:1911.05147 (first posted November 12, 2019), https://arxiv.org/abs/1911.05147.
2. J. Holm, V. King, M. Thorup, O. Zamir and U. Zwick, *Random k-out subgraph leaves only \(O(n/k)\) inter-component edges*, arXiv:1909.11147 (first posted September 24, 2019), https://arxiv.org/abs/1909.11147.
3. X. S. Cai and L. Devroye, *The graph structure of a deterministic automaton chosen at random: full version*, arXiv:1504.06238 (first posted April 23, 2015), https://arxiv.org/abs/1504.06238.
