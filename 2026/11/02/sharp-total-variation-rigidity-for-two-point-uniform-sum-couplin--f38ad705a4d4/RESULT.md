# Sharp total-variation rigidity for two-point uniform-sum couplings

## Finding
Fix an integer \(k\ge1\), set \(h=1/(2k)\), and let \(X,Y\) each be uniform on \([0,1]\), without an independence assumption. Put \(\Pi=\mathcal L(X,Y)\) and
\[\varepsilon=\Pr\bigl(X+Y\notin\{1-h,1+h\}\bigr).\]
There is exactly one joint law \(\Pi_k\) for which \(\varepsilon=0\). For every \(\Pi\),
\[\boxed{d_{\rm TV}(\Pi,\Pi_k)\le k\varepsilon,\qquad d_{\rm TV}(P,Q)=\sup_A|P(A)-Q(A)|.}\]
The factor \(k\) is optimal. For \(k\ge2\), equality is attained for every \(0<\varepsilon\le1/(2k)\), and for \(k=1\), equality holds for every joint law. In particular, one may have \(\varepsilon=1/(2k)\to0\) while \(d_{\rm TV}(\Pi,\Pi_k)=1/2\) for all \(k\ge2\).

## Assumptions and scope
The two marginals are exactly continuous uniform on \([0,1]\), with arbitrary copula, and the event concerns the *exact* two symmetric sum values. No restriction is placed on the law outside the event, and all integers \(k\ge1\) are covered. The total variation convention has values in \([0,1]\). Define for Lebesgue-a.e. \(x\in[0,1]\)
\[j(x)=\lfloor 2kx\rfloor,\qquad T_k(x)=\begin{cases}x+h,&j(x)\text{ even},\\x-h,&j(x)\text{ odd}.\end{cases}\]
Every consecutive pair of length-\(h\) blocks is interchanged by \(T_k\). Thus \(T_k\) preserves uniform measure and the law of \((X,1-T_k(X))\), where \(X\) is uniform, is \(\Pi_k\). Its sum takes the values \(1-h\) and \(1+h\), each with probability \(1/2\).

## Proof
**1. Residue-chain decomposition.** Set \(V=1-Y\), so \(V\) is uniform and the success event is \(\{|X-V|=h\}\). Outside a null set, every coordinate has a unique representation \(r+jh\), with \(0<r<h\) and \(j\in\{0,1,\ldots,2k-1\}\). A successful pair must have the same residue \(r\) and adjacent indices: \(|i-j|=1\). The marginal measure at each index, when expressed in \(dr\), has density exactly one. Disintegrating the successful part of an arbitrary coupling therefore gives nonnegative edge densities with row and column totals at most one for almost every residue \(r\). The shortfall in any row is the density of the *failed* mass from that row. This argument does not assume that the failed mass preserves residues.

**2. Path bound.** The adjacent-index bipartite graph has two disjoint paths, each with \(k\) row vertices and \(k\) column vertices. In the path with even rows \(0,2,\ldots,2k-2\), let \(g_i\) denote the successful density from row \(2i\) to column \(2i+1\) (its canonical edge), \(a_i\) the successful density from row \(2i\) to column \(2i-1\) for \(1\le i<k\) (its noncanonical edge), and \(f_i\) its failure-row density. Set \(a_0=0\). Marginal constraints give
\[g_i+a_i+f_i=1,\qquad g_{i-1}+a_i\le1\quad(1\le i<k).\]
Consequently \(a_i\le a_{i-1}+f_{i-1}\), and hence
\[\sum_{i=1}^{k-1}a_i\le\sum_{j=0}^{k-2}(k-1-j)f_j\le(k-1)\sum_{j=0}^{k-1}f_j.\]
The path with odd rows and even columns satisfies the same inequality after reversing its index order. Integrate over \(r\) and add the paths. Let \(B\) be the probability of a successful but *noncanonical* edge, and \(F\) that of a failed edge. Then
\[B\le(k-1)F,\qquad F=\varepsilon.\]

**3. Total variation and uniqueness.** Let \(G_k\) be the graph of \(Y=1-T_k(X)\). The part of any joint law \(\Pi\) restricted to \(G_k\) is dominated by \(\Pi_k\): at each \(x\) it can use no more than the prescribed uniform first-marginal mass. As \(\Pi_k(G_k)=1\),
\[d_{\rm TV}(\Pi,\Pi_k)=\Pi(G_k^c)=F+B\le kF=k\varepsilon.\]
In particular, \(F=0\) implies \(\Pi=\Pi_k\), proving the unique-coupling assertion.

**4. Sharpness.** For \(k\ge2\), choose any Borel set \(E\subset(0,h)\) of Lebesgue measure \(\delta\in(0,h]\). For residues \(r\notin E\), use the canonical matching of indices \(j\mapsto j+1\) for even \(j\) and \(j\mapsto j-1\) for odd \(j\). For \(r\in E\), instead use the permutation
\[0\mapsto2k-1,\qquad 2i\mapsto2i-1\ (1\le i<k),\qquad 2i+1\mapsto2i\ (0\le i<k).\]
These are bijections of the index set, so the induced mapping \(X\mapsto V\) preserves Lebesgue measure on \([0,1]\). For each \(r\in E\), exactly one row (index zero) fails \(|X-V|=h\), and exactly \(k\) rows differ from the canonical mapping. Thus \(\varepsilon=\delta\) and \(d_{\rm TV}(\Pi,\Pi_k)=k\delta\). For \(k=1\), the adjacent-index success graph consists only of canonical edges, so \(B=0\) and equality holds for every coupling. Taking \(E=(0,h)\) gives \(\varepsilon=h=1/(2k)\) and total-variation distance \(kh=1/2\), proving failure of any \(k\)-uniform stability coefficient.

## Verification
The exact standalone file `verify_stability.py` enumerates all \((2k)!\) permutations for \(k=1,2,3,4\), checks the finite-path inequality \(B\le(k-1)F\), and checks the sharp finite permutation witness. All 82,138 exact integer assertions passed. This exhaustive finite test is supplementary: the proof above covers every integer \(k\) and every Borel joint law. The script and its recorded output are included with the result.

## Relationship to prior work
Chaudhary and Khandelwal (2026, arXiv:2610.24197v1, Section 2.3, Theorem 3 and Section 6, Corollary 34) characterize *which distributions of a sum* of two uniforms are attainable, including two-point and symmetric three-point laws. The present result does **not** claim that two-point sum feasibility is new. It instead asks a distinct inverse question: how much can the *entire copula* differ from the unique two-point realizing copula when the sum misses its two values with probability \(\varepsilon\)? The exact factor \(k\), its explicit equality construction, and the nonuniformity as \(k\to\infty\) are not supplied by those results. General transport-stability work for regularized costs and variable marginals does not imply this unregularized graph-support estimate.

## Limitations
The guarantee is about mass on two *exact* levels; it does not control observational tolerance bands around those levels, general nonuniform marginals, other level separations, Wasserstein perturbations, or noisy empirical reconstruction. Historical priority among older matching and optimal-transport stability results has not been independently established. Finite tests do not verify the infinite measure-theoretic statement, which is proved separately above.

## References
Chaudhary, P. and Khandelwal, K., *Sums of two dependent uniform random variables: a characterization by joint tail bounds*, arXiv:2610.24197v1 (first posted 2026-10-16), https://arxiv.org/html/2610.24197v1.

Eckstein, S. and Nutz, M., *Quantitative Stability of Regularized Optimal Transport and Convergence of Sinkhorn's Algorithm*, arXiv:2110.06798 (comparison of different stability setting), https://arxiv.org/abs/2110.06798.
