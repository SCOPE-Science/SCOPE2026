# A universal host-to-tree threshold for isolate–motif covariance in fixed-edge random graphs

## Finding

For a uniform simple graph \(G(n,m)\), a growing tree motif exhibits a **host-size covariance sign threshold that is independent of the tree's shape and of the prescribed edge count**. Let \(H_s\) be any tree on \(s\ge3\) vertices, and let \(X_{H_s}\) count non-induced copies; let \(U\) count isolated vertices. Put \(N=\binom n2\) and \(B=\binom{n-1}2\). Whenever \(n\ge s\) and \(s-1\le m\le B\),

\[\operatorname{Cov}(U,X_{H_s})=\mathbb E U\,\mathbb E X_{H_s}\left[\frac{n-s}{n}\frac{(N)_{s-1}}{(B)_{s-1}}-1\right].\]

Here \((a)_j=a(a-1)\cdots(a-j+1)\), and the falling factorial is \(1\) for \(j=0\). For \(m<s-1\) or \(m>B\), covariance is zero because one of the two statistics is identically zero. When a sequence of trees satisfies \(s\to\infty\) and \(n/s\to\alpha>1\), the covariance is eventually negative for \(1<\alpha<\alpha_*\) and positive for \(\alpha>\alpha_*\), where

\[\alpha_*=1.25500097491598\ldots,\qquad(1-\alpha_*^{-1})e^{2/\alpha_*}=1.\]

For comparison, in \(G(n,p)\) the covariance is strictly negative for every \(0<p<1\) and every nonempty tree with at least two vertices. The exact identity also holds for arbitrary fixed non-induced motifs with no isolated vertices, replacing the number of tree edges by the actual edge count.

## Assumptions and scope

The host vertex set is labeled; the graph is uniform among graphs with exactly \(m\) distinct, unoriented edges. A copy of \(H\) is an injection of the vertices of a simple undirected motif \(H\) into the host, modulo automorphisms of \(H\); extra host edges among the selected vertices are permitted. The motif has \(s\ge2\) vertices, \(e\ge1\) edges and **no isolated motif vertices**, and \(n\ge s\). The general finite identity applies for \(e\le m\le B\), necessarily with \(e\le B\). At all other \(m\), the covariance is zero. No results are asserted for induced copies or for motifs containing isolated motif vertices.

## Proof

Write \(X=X_H\) and \(q=\binom Bm/\binom Nm\), so \(\mathbb E U=nq\) if \(0\le m\le B\). Let \(M_H=(n)_s/|\operatorname{Aut}(H)|\) be the number of possible labeled placements of \(H\), each with \(e\) prescribed edges. For \(m\ge e\),

\[\mathbb E X=M_H\frac{(m)_e}{(N)_e}>0.\]

Fix one placement and one vertex \(v\). If \(v\) belongs to the motif placement, the event that \(v\) is isolated is disjoint from the event that the copy is present, because every motif vertex has positive degree. If \(v\) is outside, then all \(e\) prescribed motif edges are among the \(B\) edges not incident with \(v\). Conditioning on \(v\) being isolated, those \(m\) edges form a uniformly chosen subset of the \(B\) allowed edges; consequently

\[\mathbb P(\text{copy present}\mid v\text{ isolated})=\frac{(m)_e}{(B)_e}.\]

There are exactly \(n-s\) allowable exterior vertices for each motif placement. By summing indicator products and dividing by the original copy probability,

\[\mathbb E[UX]=(n-s)M_Hq\frac{(m)_e}{(B)_e}
=\mathbb E U\,\mathbb E X\,\frac{n-s}{n}\frac{(N)_e}{(B)_e}.\]

Subtracting \(\mathbb E U\mathbb E X\) proves the general exact formula. When \(m<e\) there is no copy; when \(m>B\) there is no isolated vertex. If \(e\le m\le B\), both expectations are positive, so the sign depends **only** on the factor in brackets, never on \(m\) or the motif's internal topology beyond \((s,e)\).

For trees, \(e=s-1\). If \(n/s\to\alpha>1\), then \(N=\Theta(s^2)\), \(B=N-(n-1)\), and uniformly for \(0\le j\le s-2\),

\[\log\frac{N-j}{B-j}=\frac2n+O_\alpha(s^{-2}).\]

Adding \(s-1\) terms gives

\[\frac{(N)_{s-1}}{(B)_{s-1}}\longrightarrow e^{2/\alpha},\qquad
\frac{n-s}{n}\longrightarrow1-\frac1\alpha.\]

Writing \(x=1/\alpha\), the sign of the limit is the sign of \(h(x)=\log(1-x)+2x\). Here \(h(0)=0\), \(h'(x)=(1-2x)/(1-x)\) is positive until \(x=1/2\), negative afterwards, and \(h(x)\to-\infty\) as \(x\uparrow1\). Hence exactly one root \(x_*\in(1/2,1)\) exists, giving \(\alpha_*=1/x_*\), with positive sign for \(\alpha>\alpha_*\). Because the limit is nonzero strictly off this threshold and both expectations are positive, the eventual sign follows. Nothing is claimed at the critical ratio itself.

Finally, under independent-edge sampling \(G(n,p)\), an exterior vertex's isolation is independent of the copy edges while an interior vertex cannot be isolated. Consequently

\[\operatorname{Cov}_{G(n,p)}(U,X_H)=-s\,\mathbb E X_H(1-p)^{n-1}<0\qquad(0<p<1).\]

## Verification

Run the enclosed self-contained \(\texttt{verify.py}\) with Python 3. It exhaustively enumerates graph distributions over several host sizes and motif shapes, computes exact rational moments, and compares them to the formula in every edge-count stratum, including empty ranges. It performs 113 exact strata checks plus six sign comparisons across growing-tree examples. Exact arithmetic is used for all finite covariance comparisons. These computations are checks, not substitutes for the all-size proof above.

## Relationship to prior work

Motif-count expectations in random-network ensembles were investigated by Itzkovitz and collaborators (2003). Ellis and Ferry (2010) obtain variance formulas for connected subgraph counts in the independent-edge Erdős–Rényi model. Sah (2022) proves local limit and anticoncentration theorems for subgraph statistics in both \(G(n,p)\) and \(G(n,m)\), principally for fixed motifs. Janson (1994) developed general orthogonal-decomposition methods for random graph statistics. These works provide strong background and general tools; no inspected statement gives the **growing-tree, host-to-motif-size critical ratio** for covariance with isolated vertices. General joint-moment results may implicitly recover the finite formula, and no exclusive priority is claimed for that elementary step.

## Limitations

The result concerns non-induced motif copies; changing the definition to induced copies changes the calculation. The simultaneous scaling requires a growing motif, not a single fixed tree. The eventual sign statement excludes sequences with \(n/s\to\alpha_*\), where a finer boundary analysis would be needed. The absolute covariance may become small because the expected number of motifs or isolated vertices becomes small. Historical coverage of the growing-motif sign phase has not been exhaustively excluded; no independent audit has been performed.

## References

1. S. Itzkovitz, R. Milo, N. Kashtan, G. Ziv, U. Alon, *Subgraphs in random networks*, arXiv:cond-mat/0302375 (first publicly posted 2003-02-19); Phys. Rev. E 68 (2003), 026127. https://arxiv.org/abs/cond-mat/0302375
2. R. B. Ellis and J. P. Ferry, *Variance of the subgraph count for sparse Erdős–Rényi graphs*, Discrete Applied Mathematics 158 (2010), 649–658. https://doi.org/10.1016/j.dam.2009.11.012
3. A. Sah, *Local limit theorems for subgraph counts*, Journal of the London Mathematical Society (2022). https://doi.org/10.1112/jlms.12523
4. S. Janson, *Orthogonal Decompositions and Functional Limit Theorems for Random Graph Statistics*, Memoirs of the American Mathematical Society 534 (1994).
