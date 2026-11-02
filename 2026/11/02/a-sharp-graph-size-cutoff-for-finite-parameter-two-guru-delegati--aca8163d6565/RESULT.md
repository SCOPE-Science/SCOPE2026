# A sharp graph-size cutoff for finite-parameter two-guru delegation

## Finding

**Theorem (uniform cutoff and noncommuting voting-weight limits).** Let \(H=(V,E)\) be any finite connected simple undirected graph with \(N=|V|\geq 2\), and fix distinct vertices \(u,v\). Regard each edge as two directed delegation arcs, both of cost \(1\). Add exactly two arcs to absorbing casting voters, \(u\to A\) of cost \(2\) and \(v\to B\) of cost \(3\). For \(0<\varepsilon\leq1\), a delegating voter chooses each outgoing arc with probability proportional to \(\varepsilon^{\text{cost}}\). Write \(h_\varepsilon(x)\) for the eventual probability that a walk starting at \(x\) reaches \(A\). Let \(R_H(u,v)\) be the effective resistance between \(u\) and \(v\) when each undirected edge has unit resistance.

**(i) Exact quantitative regularization.** If \(g(v)=0\) and \(L_Hg=\mathbf 1_u-\mathbf 1_v\), then \(g(u)=R_H(u,v)\), \(0\leq g(x)\leq R_H(u,v)\), and

\[
h_\varepsilon(x)=\frac{1+\varepsilon^2g(x)}{1+\varepsilon+\varepsilon^2R_H(u,v)}.
\]

In particular, although the zero-parameter minimum-cost branching rule allocates every delegate to \(A\), the **sharp worst-case finite-parameter discrepancy** across all connected \(N\)-vertex graphs, all choices of the two exit vertices and all delegates is

\[
E_N(\varepsilon):=\max_{H,u,v,x}(1-h_\varepsilon(x))
=\frac{\varepsilon+\varepsilon^2(N-1)}{1+\varepsilon+\varepsilon^2(N-1)}.
\]

The maximum is attained by the two endpoints of an \(N\)-vertex path, with \(x=v\). Consequently, for any positive sequence \(\varepsilon_N\to0\), convergence to the zero-parameter allocation uniformly across **all** connected graphs of size \(N\) occurs if and only if \(N\varepsilon_N^2\to0\). If \(\sqrt N\varepsilon_N\to c\in[0,\infty]\), the maximal discrepancy tends to \(c^2/(1+c^2)\), interpreted as \(1\) at \(c=\infty\). Thus \(N^{-1/2}\) is the sharp graph-size crossover scale.

**(ii) Inversion of aggregate voting weight.** Take a path \(0,1,\ldots,L\), put \(u=0\) and \(v=L\), and attach \(K\) further leaves to \(v\), where \(L\geq1\), \(K\geq0\), and \(N=L+K+1\). Each caster retains one unit of its own weight. Their total fractional voting weights obey

\[
\Pi_A=1+\frac{N+\varepsilon^2L(L+1)/2}{1+\varepsilon+\varepsilon^2L},
\qquad \Pi_B=N+2-\Pi_A.
\]

The more costly caster \(B\) has strictly larger voting weight if and only if

\[
\varepsilon^2LK>N(1-\varepsilon).
\]

For example, \((L,K,\varepsilon)=(8,4,1/2)\) yields \((\Pi_A,\Pi_B)=(51/7,54/7)\). Even while \(\varepsilon\to0\), the disagreement can persist at a macroscopic level: for positive integers \(m\to\infty\), set \(\varepsilon=1/m\), \(L=K=4m^2\), and \(N=8m^2+1\). Then

\[
\frac{\Pi_A}{N+2}\longrightarrow\frac25,\qquad
\frac{\Pi_B}{N+2}\longrightarrow\frac35.
\]

For **each fixed** graph, in contrast, the zero-parameter rule gives caster \(A\) all \(N\) delegate units. The convergence in graph size and in the arc-weight parameter therefore does not commute.

## Assumptions and scope

Costs are positive integers, with ties allowed among the cost-one internal arcs. Each delegate has positive probability of eventually reaching a caster; connectivity and the two positive exit weights guarantee absorption with probability one. The finite-parameter process is the absorbing random walk used to regularize the ranked-cost delegation rule; the rule itself is defined by the \(\varepsilon\downarrow0\) limit. The result concerns **fractional voting weights**, not a particular election, preference aggregation, or pivotal-power index. The graph is undirected only at the level of the delegate-to-delegate connections; the model is directed once caster exits are included. No statement about arbitrary directed delegation networks or more than two casters is asserted.

## Proof

**1. Harmonic reduction.** Divide every outgoing arc weight by \(\varepsilon\). Each internal arc then has conductance \(1\), the exit at \(u\) has relative conductance \(\alpha=\varepsilon\), and the exit at \(v\) has relative conductance \(\beta=\varepsilon^2\). The first-step equations, including at the two exit vertices, are exactly

\[
L_Hh=\alpha(1-h(u))\mathbf1_u-\beta h(v)\mathbf1_v.
\]

Summing these equations over \(V\) gives \(\alpha(1-h(u))=\beta h(v)=j\). Since \(L_Hg=\mathbf1_u-\mathbf1_v\), connectedness implies that \(h(x)=h(v)+jg(x)\). Evaluating at \(v\) gives \(h(v)=j/\beta\), and evaluating at \(u\) gives \(h(u)=j/\beta+jR\), with \(R=g(u)\). Substitution into \(\alpha(1-h(u))=j\) yields \(j=\beta/(1+\beta/\alpha+\beta R)\). Hence \(h(v)=1/(1+\varepsilon+\varepsilon^2R)\) and the claimed exact formula follows. The electrical interpretation identifies \(R\) with the effective resistance for unit current from \(u\) to \(v\). The discrete maximum principle gives \(0=g(v)\leq g(x)\leq g(u)=R\).

**2. Sharp worst-case bound.** The pointwise error is

\[
1-h(x)=\frac{\varepsilon+\varepsilon^2(R-g(x))}{1+\varepsilon+\varepsilon^2R}.
\]

Its maximum over \(x\) is attained at \(v\), since \(g(v)=0\). For any connected graph, Rayleigh's variational principle (or a unit flow along a shortest \(u\)--\(v\) path) gives \(R\leq\operatorname{dist}_H(u,v)\leq N-1\). The function \(r\mapsto(\varepsilon+\varepsilon^2r)/(1+\varepsilon+\varepsilon^2r)\) is strictly increasing, and the endpoint-to-endpoint path has \(R=N-1\). This proves the exact maximum. The sequence statements follow by evaluating this rational expression, with \(\varepsilon_N\to0\). For any fixed \(N\), the minimum-cost directed branching must use the \(u\to A\) exit: the cheapest \(A\)-only spanning branching costs \(N+1\), whereas a \(B\)-only branching costs \(N+2\), and a branching using both exits costs \(N+3\). Thus all minimum-cost branchings lead to \(A\).

**3. Broom calculation.** A unit current along the unique \(u\)--\(v\) path has voltage \(g(i)=L-i\) on its \(L+1\) vertices and voltage \(0\) on each of the \(K\) leaves attached to \(v\). Hence \(R=L\) and \(\sum_{x\in V}g(x)=L(L+1)/2\). Summing the formula for \(h\) over delegates and adding caster \(A\)'s own vote proves \(\Pi_A\). Since each delegate's fractions sum to one, \(\Pi_B=N+2-\Pi_A\). Cross-multiplying positive denominators shows that \(\Pi_B>\Pi_A\) is equivalent to \(\varepsilon^2L(N-L-1)>N(1-\varepsilon)\), which is the stated inequality because \(K=N-L-1\). For \(L=K=4m^2\) and \(\varepsilon=1/m\), the denominator equals \(5+1/m\), while \(N+\varepsilon^2L(L+1)/2=16m^2+3\). Dividing by \(N+2=8m^2+3\) and sending \(m\to\infty\) gives \(2/5\) and \(3/5\), completing the proof.

## Verification

The included standalone `verify.py` independently solves the absorbing linear equations and the grounded unit-current Laplacian using exact rational Gaussian elimination. It compares the two descriptions on \(840\) graph/parameter instances generated reproducibly with a fixed seed, checks sharp endpoint paths through \(14\) vertices, tests the explicit \(L=8\), \(K=4\) broom, and checks the closed forms for eight members of the growing broom family. Run `python3 verify.py` using Python's standard library. These are finite consistency tests, **not** replacements for the preceding proof of the universal graph and asymptotic claims.

## Relationship to prior work

Utke and Schmidt-Kraepelin (2023) define ranked-cost random-walk delegations using arc weights \(\varepsilon^{c(e)}\) and analyze their zero-parameter fractional assignment via min-cost branchings. In their related-work discussion they explicitly credit Fita Sanmartín, Damrich and Hamprecht (2021) for equivalence between finite-temperature Gibbs forests and absorbing random walks. The earlier paper gives general Laplacian absorption formulas and, in Figure 1, an example where finite-temperature seed assignment differs from the minimum-cost forest. **Neither the electrical identity as a general technique nor the mere possibility of finite-temperature assignment reversal is claimed as new here.** The specific contributions assessed here are the attained sharp graph-size-uniform error envelope for the two-exit rank-cost family, its \(\varepsilon\sqrt N\) threshold, and the explicit macroscopic inversion of aggregate caster weights along a diverging-graph, vanishing-parameter sequence. No implication from the inspected general formulas to these sharp global and aggregate conclusions is stated in the cited sources; they do make the present derivation possible.

## Limitations

The result is for two prescribed asymmetric exit costs and common cost-one internal arcs on a connected undirected delegate graph. Ties among internal arc costs are allowed. The underlying electric-circuit calculations are classical; priority is asserted only for the combined sharp all-graph cutoff and macroscopic voting-weight construction within this restricted delegation model, subject to possible unidentified specialist precedence. The large-graph inversion is a fractional-vote statement, not a change in winning alternative or power index. For each fixed graph, the zero-parameter allocation remains perfectly concentrated on the cheaper caster. No independent external audit has been performed.

## References

1. M. Utke and U. Schmidt-Kraepelin, *Anonymous and Copy-Robust Delegations for Liquid Democracy*, arXiv:2307.01174, first public release 2023-07-03, https://arxiv.org/abs/2307.01174. In particular Sections 3 and 4–6 and the discussion of Directed Probabilistic Watershed.
2. E. Fita Sanmartín, S. Damrich and F. A. Hamprecht, *Directed Probabilistic Watershed*, Advances in Neural Information Processing Systems 34 (2021), https://papers.neurips.cc/paper_files/paper/2021/file/a73d9b34d6f7c322fa3e34c633b1297d-Paper.pdf. In particular Sections 2–5, Theorems 3.5 and 4.1, and Figure 1.
3. Classical unit-flow and effective-resistance principles, used here only through their elementary definitions and the one-path upper bound, as also discussed in the graph-based random-walker background of Reference 2.
