# Optimal rainbow-diamond edge colourings of wheel graphs: a Poisson enumeration

## Finding

Let \(W_n=K_1\vee C_n\) be the wheel with \(n\ge5\) rim vertices. A \(D\)-colouring is a proper edge-colouring in which every subgraph isomorphic to a diamond (\(K_4\) with one edge deleted) is rainbow, where diamonds need not be induced. Write \(\chi'_D(W_n)\) for the minimum palette size. Then
\[
\chi'_D(W_n)=n\qquad(n\ge5).
\]
With a **fixed named palette** \(\{0,\ldots,n-1\}\), let \(N_n\) denote the number of \(D\)-colourings. The exact finite enumeration and limiting law are
\[
N_n=n!a_n,\quad
 a_n=\sum_{\substack{c_i\in \mathbb Z_n\setminus\{i-1,i,i+1,i+2\}\\i\in\mathbb Z_n}}
\ \prod_{i\in\mathbb Z_n}\mathbf1\{c_i\ne c_{i+1}\},
\qquad \lim_{n\to\infty}\frac{N_n}{n!(n-4)^n}=e^{-1}.
\]
All indices in this formula are interpreted modulo \(n\). In particular, \(a_5=1\) and \(a_6=2\). The limit is an asymptotic enumeration of every optimal-palette colouring, not just an existence statement.

## Assumptions and scope

The wheel has hub \(h\), rim vertices \(v_i\) (\(i\in\mathbb Z_n\)), spoke edges \(s_i=hv_i\), and rim edges \(r_i=v_iv_{i+1}\). An edge-colouring may reuse a colour on nonconflicting edges. A diamond is a five-edge subgraph on four vertices, not necessarily induced. A named-palette colouring is a function from the \(2n\) edges to \(\mathbb Z_n\); palettes differing by a permutation are counted separately. As all \(n\) spokes share the hub, each optimal colouring necessarily uses all \(n\) palette colours.

## Proof

**1. Complete conflict structure.** Every two spokes are incident. Each rim edge \(r_i\) must differ from the four spokes \(s_{i-1},s_i,s_{i+1},s_{i+2}\). The middle two are incident with \(r_i\); the outside two occur together with \(r_i\) in the diamonds on \(\{h,v_{i-1},v_i,v_{i+1}\}\) and \(\{h,v_i,v_{i+1},v_{i+2}\}\). There are no further spoke–rim conflicts. Indeed, every diamond on \(n\ge5\) wheel vertices consists of \(h\) and three consecutive rim vertices (it has their two rim edges and three spokes), since a rim-induced subgraph has no triangle. Two rim edges conflict precisely when they are consecutive: disjoint rim edges cannot lie in any diamond because every diamond has only two rim edges and these are consecutive. Thus the conflict graph has a clique on the spokes, a cycle on the rim edges, and exactly the four stated forbidden spoke–rim pairs at each rim edge.

**2. Exact minimum.** Any \(D\)-colouring needs \(n\) colours at the hub. Give spoke \(s_i\) colour \(i\) and rim edge \(r_i\) colour \(i+3\pmod n\). For \(n\ge5\), \(i+3\) is not among \(i-1,i,i+1,i+2\pmod n\), and consecutive rim colours are distinct. This is a valid \(n\)-colour \(D\)-colouring, proving \(\chi'_D(W_n)=n\).

**3. Enumeration.** Choose the spoke colours bijectively in \(n!\) ways. Relabel their colours so that \(s_i\) has colour \(i\); this fixes a bijection between rim colourings and sequences \((c_i)_{i\in\mathbb Z_n}\) with \(c_i\) in the list \(L_i=\mathbb Z_n\setminus\{i-1,i,i+1,i+2\}\) and \(c_i\ne c_{i+1}\). The lists have size \(n-4\). This proves the displayed exact sum. For \(n=5\), each list has one element, yielding \(a_5=1\). For \(n=6\), the only choices are \(c_i=i+3\) and \(c_i=i+4\). Consecutive equality occurs precisely at a transition from the second choice to the first. Any nonconstant cyclic binary word has such a transition, so \(a_6=2\).

**4. Poisson limit.** Independently choose uniform \(C_i\in L_i\), and define \(X_n=\sum_{i\in\mathbb Z_n}\mathbf1\{C_i=C_{i+1}\}\). Each adjacent pair of lists has intersection size \(n-5\), so for \(n\ge6\)
\[
p_n=\Pr(C_i=C_{i+1})=\frac{n-5}{(n-4)^2},\qquad np_n\longrightarrow1.
\]
Fix any positive integer \(k\). In the \(k\)-th falling factorial moment of \(X_n\), tuples of pairwise nonconsecutive event indices number \(n^k+O_k(n^{k-1})\), and their indicator events are independent, giving total contribution \((n^k+O_k(n^{k-1}))p_n^k\to1\). Every other tuple of \(k\) distinct indices comprises \(c\le k-1\) cyclic runs of consecutive indices; for fixed \(k\) and sufficiently large \(n\), there are \(O_k(n^c)\) such tuples. A run of \(\ell\) equality events forces \(\ell+1\) independent uniform list variables to be equal, a probability at most \((n-4)^{-\ell}\). Events in different runs use disjoint variables; hence the total probability for the tuple is at most \((n-4)^{-k}\). The contribution of every such type is therefore \(O_k(n^{-1})\). Thus \(\mathbb E(X_n)_k\to1\) for every fixed \(k\), the factorial moments of a Poisson random variable of mean one. By the factorial-moment characterization, \(X_n\) converges in law to \(\operatorname{Poisson}(1)\), whence \(\Pr(X_n=0)\to e^{-1}\). Finally, exactly \((n-4)^n\Pr(X_n=0)\) independent-list assignments have no adjacent equality, proving the asymptotic enumeration.

## Verification

The standalone `verify.py` constructs the wheel edge-conflict relation independently from vertex incidences and all five-edge diamond subgraphs; for each \(5\le n\le34\), it confirms the relation is precisely the one used above. It independently exhausts every list assignment for \(n=5,6,7\), checks the dynamic-programming counts for \(5\le n\le10\), and computes additional exact values through \(n=40\). The normalized counts for \(n=5,6,7,8,9,10\) are, respectively, \(1,2,367,11966,400376,13440226\). Run `python3 verify.py`. The asymptotic statement rests on the mathematical factorial-moment argument, not finite numerical evidence.

## Relationship to prior work

Runze Wang introduced rainbow-diamond \(D\)-colourings and studied general maximum-degree bounds in [1]. Harshit Verma established the sharp general planar bound of \(2\Delta-1\) for maximum degree at least six in [2]. The latter paper explicitly identifies the conflict graph of the four-rim wheel as \(K_4\vee C_4\), but neither examined source establishes the exact minimum-palette enumeration or the asymptotic \(e^{-1}\) factor for wheels of arbitrary rim length. The wheel family provides a parameter-sharp counterpoint to the worst-case planar bound: its palette size equals \(\Delta=n\), while the optimal-palette assignments display a nontrivial rare-event law.

## Limitations

The enumeration assumes \(n\ge5\), the ordinary wheel and exactly \(n\) named colours. It does not enumerate colourings with larger palettes or arbitrary planar graphs. General chromatic-polynomial and rare-pattern frameworks may contain equivalent specializations not identified in the literature comparison, so historical priority remains qualified. The probability limit does not supply an explicit uniform finite-size error estimate. No independent mathematical audit has been performed.

## References

[1] R. Wang, *Proper edge coloring with rainbow diamonds*, arXiv:2606.06831, first submitted 2026-06-05, especially Definition 1.2 and Section 4, https://arxiv.org/abs/2606.06831.

[2] H. Verma, *A proof of Wang’s planar D-coloring conjecture*, arXiv:2610.33322v1, first submitted 2026-10-23, especially Section 2.1 and Lemma 6.1, https://arxiv.org/html/2610.33322v1.
