# Complete zero-forcing and minimal-fort distributions for matched pairs of cliques

## Finding

Let \(H_n=K_n\square K_2\), for every integer \(n\ge2\). Label its two complete-graph layers \(A=\{A_1,\ldots,A_n\}\) and \(B=\{B_1,\ldots,B_n\}\); the only cross-layer edges are \(A_iB_i\). A *standard zero-forcing set* is an initially blue vertex subset from which repeated applications of the rule "a blue vertex with exactly one white neighbor colors that neighbor blue" eventually color the whole graph. A *fort* is a nonempty set \(F\) for which every vertex outside \(F\) has either zero or at least two neighbors in \(F\). A fort is *inclusion-minimal* when no proper subset is a fort.

For a blue set \(S\), write \(W_A=\{i:A_i\notin S\}\), \(W_B=\{i:B_i\notin S\}\), \(a=|W_A|\), and \(b=|W_B|\). Then \(S\) is zero forcing **if and only if** at least one of the following holds:

1. \(a=0\) or \(b=0\).
2. \(W_A=\{j\}\) and some \(i\ne j\) is outside \(W_B\).
3. \(W_B=\{j\}\) and some \(i\ne j\) is outside \(W_A\).

Put \(\mathcal Z_n(z)=\sum_{S\text{ zero forcing}}z^{|S|}\). The complete polynomials are
\[
\mathcal Z_2(z)=4z^2+4z^3+z^4,
\]
and, for all \(n\ge3\),
\[
\boxed{\mathcal Z_n(z)=2z^n(1+z)^n-z^{2n}+n^2z^{2n-2}
+2n\sum_{b=2}^{n-2}\binom nb z^{2n-b-1}
+2n(n-1)z^n.}
\]
Empty sums are zero. In particular, every coefficient, not merely the minimum cardinality, is given.

The inclusion-minimal forts have an exact complete classification. For \(n\ge4\), they are precisely:

- every four-set with two vertices from \(A\) and two from \(B\), with the choices independent; and
- for every \(j\in[n]\), the two \(n\)-sets \(\{A_j\}\cup\{B_i:i\ne j\}\) and \(\{B_j\}\cup\{A_i:i\ne j\}\).

For \(n=3\), retain those six three-vertex sets and add the three four-sets \(\{A_i,B_i:i\ne j\}\) indexed by \(j\in[3]\). For \(n=2\), the only minimal forts are \(\{A_1,B_2\}\) and \(\{A_2,B_1\}\). Thus, putting \(\mathcal M_n(z)=\sum_{F\text{ minimal fort}}z^{|F|}\),
\[
\boxed{\mathcal M_n(z)=
\begin{cases}
2z^2,&n=2,\\
6z^3+3z^4,&n=3,\\
\binom n2^2z^4+2nz^n,&n\ge4.
\end{cases}}
\]
In the last line the two monomials have the same degree when \(n=4\), and their coefficients add.

For every \(n\ge3\), the number of zero-forcing sets, including all cardinalities, is exactly
\[
\boxed{\mathcal Z_n(1)=(n+1)2^{n+1}-n^2-6n-1,}
\]
and the number of minimum zero-forcing sets is \(2n(n-1)+2\), all of cardinality \(n\). At \(n=2\), the corresponding values are \(9\) and \(4\).

If every vertex is independently blue with probability \(p_n=1-\lambda/n\), with fixed \(\lambda\ge0\) and sufficiently large \(n\), the exact polynomial yields the critical-window limit
\[
\boxed{\lim_{n\to\infty}\Pr(\text{all vertices are eventually blue})
=1-\bigl(1-(1+\lambda)e^{-\lambda}\bigr)^2.}
\]
If \(n(1-p_n)\to0\), this success probability tends to \(1\); if \(n(1-p_n)\to\infty\), it tends to \(0\). Thus the robustness threshold for uniformly random initially white vertices lies at density of order \(1/n\).

## Assumptions and scope

Every graph is finite, simple, and undirected. The two cliques have equal size \(n\ge2\), with a fixed perfect matching between corresponding vertices. Vertices are labeled; no automorphism quotient is taken. Only standard blue-vertex forcing is considered; skew and positive-semidefinite variants are not covered. The probabilistic statement concerns independent, identically distributed initial vertex colors and does not treat correlated failures.

## Proof

**Step 1: Exact success criterion.** A blue vertex \(A_i\) has precisely \(a+\mathbf1_{\{i\in W_B\}}\) white neighbors, and a blue vertex \(B_i\) has precisely \(b+\mathbf1_{\{i\in W_A\}}\) white neighbors. If \(a,b\ge2\), every blue vertex has at least two white neighbors, so no first force is possible. If \(a=0\), each white vertex \(B_i\) has a blue counterpart \(A_i\) with exactly one white neighbor; all white vertices can be forced. The case \(b=0\) is symmetric. The only remaining possibility for success has \(a=1\) or \(b=1\). When \(W_A=\{j\}\), a blue vertex \(A_i\) with \(i\ne j\) can force \(A_j\) if and only if \(i\notin W_B\); this reduces to \(a=0\) and completes forcing. If no such \(i\) exists, then \([n]\setminus\{j\}\subseteq W_B\). In that case all blue \(A_i\) have two white neighbors and the only possible blue vertex in \(B\), namely \(B_j\), has at least two white neighbors (the cases \(n=2\) and \(n\ge3\) both satisfy this). Hence the process stalls. Interchange the cliques to obtain the third condition. This proves the criterion in both directions.

**Step 2: Count all success sets.** It is convenient to count by the number of *white* vertices, writing \(F_n(y)=\sum_{S\text{ zero forcing}}y^{2n-|S|}\). Cases with \(a=0\) or \(b=0\) contribute \(2(1+y)^n-1\). For \(n\ge3\), the other successful cases are disjoint: (i) \(a=b=1\), contributing \(n^2y^2\); (ii) one white in a specified layer and \(2\le b\le n-2\) white in the other, contributing \(2n\sum_{b=2}^{n-2}\binom nb y^{b+1}\); and (iii) one white in the first layer and \(n-1\) in the other, where the other layer's sole blue index is different from the first layer's white index, contributing \(2n(n-1)y^n\). There is no overlap between (i)--(iii) for \(n\ge3\). Thus
\[
F_n(y)=2(1+y)^n-1+n^2y^2+2n\sum_{b=2}^{n-2}\binom nb y^{b+1}+2n(n-1)y^n.
\]
When \(n=2\), the only additional successful configurations beyond \(a=0\) or \(b=0\) are the two with \(W_A=\{j\}\) and \(W_B=\{j\}\), giving \(F_2(y)=1+4y+4y^2\). The substitutions \(\mathcal Z_n(z)=z^{2n}F_n(1/z)\) give the claimed polynomials. For \(n\ge3\), the highest-degree term of \(F_n\) is \((2+2n(n-1))y^n\), giving minimum blue cardinality \(n\) and the corresponding count. Summing coefficients at \(y=1\) and using \(\sum_{b=2}^{n-2}\binom nb=2^n-2-2n\) gives the stated total.

**Step 3: Classify all minimal forts.** Write \(F_A=\{i:A_i\in F\}\), \(F_B=\{i:B_i\in F\}\), and \(a=|F_A|\), \(b=|F_B|\). If \(a=0<b\), a blue \(A_i\) corresponding to any \(i\in F_B\) has exactly one neighbor in \(F\), impossible for a fort. Symmetrically, \(b=0<a\) is impossible. If \(a=1\), say \(F_A=\{j\}\), then every unselected \(A_i\) with \(i\ne j\) already sees \(A_j\), so it must also see \(B_i\), giving \([n]\setminus\{j\}\subseteq F_B\). Conversely every such set is a fort, since vertices outside the other layer see at least \(n-1\) members there (for \(n=2\), the matched omitted counterpart also supplies one additional neighbor). Inclusion-minimality forces \(F_B=[n]\setminus\{j\}\), and this set has no smaller fort. The symmetric case is identical. Finally, if \(a,b\ge2\), the set is automatically a fort and contains a fort with exactly two vertices per layer. For \(n\ge4\), such four-sets cannot contain a fort of the preceding one-versus-\((n-1)\) type, and all are inclusion-minimal. For \(n=3\), a two-per-layer fort contains a three-set of that type unless its unique missing index in each layer is the same; exactly three four-sets survive. For \(n=2\), the only minimal one-versus-one forts have opposite indices. This proves necessity, sufficiency, and all enumerations.

**Step 4: Random robustness limit.** Let \(X_A,X_B\) be the independent counts of initially white vertices in the two layers. Under \(p_n=1-\lambda/n\) they converge jointly to independent Poisson variables of mean \(\lambda\). By Step 1, success is equivalent to \(\min(X_A,X_B)\le1\), apart from configurations where one white count is exactly one and the other layer is white at all but at most one index; the probability of this exceptional event tends to zero. The displayed limit is consequently \(1-[\Pr(\mathrm{Poi}(\lambda)\ge2)]^2\). For the two threshold regimes, if \(n(1-p_n)\to0\), both white counts are zero with probability tending to one. If \(n(1-p_n)\to\infty\), both counts are at least two with probability tending to one, which forces immediate failure by Step 1. No asymptotic independence beyond the stated model is assumed.

## Verification

A standalone standard-library Python checker constructs the graph adjacency from the definition and simulates actual zero-forcing rounds, independently of the success predicate. It enumerates every initial blue set for \(2\le n\le8\) and compares the entire coefficient dictionary, every subset against the necessary-and-sufficient criterion, and exact total/minimum counts. For \(2\le n\le7\), it also enumerates every fort and determines inclusion-minimality by checking **all proper fort subsets**, not merely one-vertex deletions; it then compares the exact list of forts against the structural classification. The execution completed with `VERIFY_OK direct_subsets=87376 complete_polynomial_orders=7 exact_minimal_fort_orders=6`. Details and the implementation are in `VERIFICATION.md` and `verify.py`. The finite checks corroborate, but do not replace, the all-order proof above.

## Relationship to prior work

Boyer, Brimkov, English, Ferrero, Keller, Kirsch, Phillips and Reinhart (arXiv:1801.08910v1, January 26, 2018) introduced the zero-forcing polynomial and gave general extremal-coefficient results and specific other families. Their full 2018 preprint does not give the matched-clique Cartesian-product enumeration. Abara and Pelayo (arXiv:2202.04997v1, February 10, 2022) studied maximal failed zero forcing sets of graph products, including the known maximum-failed cardinality for products of complete graphs; those scalar conclusions do not determine the present complete polynomial. Cameron, Hogben, Kenter, Mojallal and Schuerger (arXiv:2310.17904, first posted October 27, 2023) introduced the minimal-fort hypergraph as a systematic tool, and proved general and special-family Cartesian-product inequalities and scalar results; no complete fort hypergraph for the matched-clique family appears in its inspected current preprint. Jacob (arXiv:2309.06234v1, September 12, 2023) developed zero-forcing span, which sees only whether certain coefficients are interior, not their counts. The known scalar zero-forcing number \(Z(K_n\square K_2)=n\) and failed-zero-forcing extrema are not claimed as new. The new contribution is the full labeled polynomial together with every inclusion-minimal fort and the independent-failure critical window.

## Limitations

The theorem concerns the two-layer Cartesian product \(K_n\square K_2\), not arbitrary \(K_m\square K_n\) or ordinary cycle prisms \(C_n\square K_2\). It does not address leaky, skew, or positive-semidefinite forcing. The probability limit requires independent initial colors and does not assert universality under correlations. Exact originality is assessed against the inspected accessible literature and related research records, not independently certified; an unindexed equivalent result or inaccessible later revision remains possible. Exhaustive tests terminate at \(n=8\) for the zero-forcing polynomial and \(n=7\) for minimal forts and do not themselves prove infinite statements.

## References

1. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips and C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910v1 (first posted 2018-01-26), https://arxiv.org/abs/1801.08910 .
2. M. N. M. Abara and P. A. B. Pelayo, *Maximal failed zero forcing sets for products of two graphs*, arXiv:2202.04997v1 (first posted 2022-02-10), https://arxiv.org/abs/2202.04997 .
3. T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal and H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904 (first posted 2023-10-27), https://arxiv.org/abs/2310.17904 .
4. B. Jacob, *The zero forcing span of a graph*, arXiv:2309.06234v1 (first posted 2023-09-12), https://arxiv.org/abs/2309.06234 .
