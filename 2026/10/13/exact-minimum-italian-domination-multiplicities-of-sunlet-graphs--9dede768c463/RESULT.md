# Exact minimum Italian-domination multiplicities of sunlet graphs

## Finding

For each integer \(n\ge3\), let \(U_n=C_n\odot K_1\) be the sunlet graph: its core vertices \(u_0,\ldots,u_{n-1}\) form a cycle, and each \(u_i\) has its private leaf \(v_i\). Let \(D_I(U_n,z)=\sum_j d_I(U_n,j)z^j\) enumerate Italian dominating functions by weight. Define \(m_I(U_n)=d_I(U_n,\gamma_I(U_n))\), the number of optimum functions on labeled vertices. For all integers \(q\ge1\),

\[
\boxed{m_I(U_{3q})=3\cdot2^q,\quad m_I(U_{3q+1})=(3q+1)(q+3)2^q,\quad m_I(U_{3q+2})=(3q+2)2^{q+1}.}
\]

The minimum weight \(\gamma_I(U_n)=n+\lceil n/3\rceil\) itself is **previously known**, as a special case of the corona/Italian-domination theorem of Alizadeh et al. (2017) and Hernández-Ortiz et al. (2020). The result here is the exact multiplicity and the complete description of all optimum labelings.

## Assumptions and scope

An Italian dominating function (equivalently, a Roman \(\{2\}\)-dominating function) on a finite simple graph \(G\) is a map \(f:V(G)\to\{0,1,2\}\) such that every vertex \(w\) with \(f(w)=0\) satisfies \(\sum_{x\in N_G(w)}f(x)\ge2\). Its weight is \(\sum_{w\in V(G)}f(w)\), and \(\gamma_I(G)\) denotes the least weight. The graph is the ordinary simple sunlet with exactly one leaf on every cycle vertex; cycle indices are modulo \(n\). Distinct vertex-labeled functions are counted separately; no quotient by rotations, reflections, or color permutations is taken.

## Proof

**Step 1: sharp pair-weight lower bound.** Write \(a_i=f(u_i)\) and \(b_i=f(v_i)\). For every \(i\), \(a_i+b_i\ge1\), since \(b_i=0\) forces \(a_i=2\). Equality \(a_i+b_i=1\) is possible only for \((a_i,b_i)=(0,1)\). Put

\[
S=\{i:a_i+b_i\ge2\}.
\]

If \(i\notin S\), its pair is \((0,1)\), and the Italian condition at \(u_i\) gives \(a_{i-1}+a_{i+1}\ge1\). Therefore \(i\) is adjacent in the cycle to an index of \(S\). Thus \(S\) dominates \(C_n\), so

\[
\sum_i(a_i+b_i)\ge n+|S|\ge n+\gamma(C_n)=n+\lceil n/3\rceil.
\]

Conversely choose any dominating \(k\)-set \(S\) of the core cycle, with \(k=\lceil n/3\rceil\). Assign \((a_i,b_i)=(1,1)\) for \(i\in S\) and \((0,1)\) otherwise. Every zero cycle vertex is guarded by its leaf and at least one neighboring selected cycle vertex, giving an Italian function of weight \(n+k\). Thus the familiar scalar equality is recovered.

**Step 2: bijection for minimum functions.** Every function of weight \(n+k\) has \(|S|=k\), all pairs indexed by \(S\) have weight exactly two, and all others are \((0,1)\). The weight-two pairs are precisely

\[
(a_i,b_i)\in\{(0,2),(1,1),(2,0)\},\qquad i\in S.
\]

Call \(i\in S\) *active* if \(a_i>0\). Each active index has exactly two choices, \((1,1)\) or \((2,0)\); each inactive index has exactly one, \((0,2)\). Every chosen pair automatically satisfies its own Italian conditions. A vertex \(i\notin S\) requires that at least one of its two selected neighboring cycle vertices be active. Hence **minimum Italian functions correspond bijectively to a minimum dominating \(k\)-set \(S\) of \(C_n\) and an active subset \(A\subseteq S\) that dominates \(C_n\setminus S\), with multiplicity \(2^{|A|}\)**.

**Step 3: cyclic gaps.** List the \(k\) selected vertices in cyclic order. Their positive clockwise gaps \(g_1,\ldots,g_k\) have \(g_i\in\{1,2,3\}\) because \(S\) dominates the cycle; conversely any cyclic \(k\)-set with these gaps dominates it. Since \(\sum_i g_i=n\),

\[
\sum_{i=1}^k(3-g_i)=3k-n\in\{0,1,2\}.
\]

A gap of length three contains two unselected vertices, each adjacent to only one of the two selected endpoints; hence **both endpoints must be active**. A gap of length two contains one unselected vertex; hence **at least one endpoint must be active**. A gap of length one imposes no further condition. In counting gap patterns, choosing a distinguished start vertex gives \(n\) choices; every cyclic selected set is represented exactly \(k\) times over distinguished starts and ordered gap strings.

**Case \(n=3q\).** Here \(k=q\) and every gap is three. There are \(n/k=3\) minimum dominating sets, each with all \(k\) chosen indices active. Therefore \(m_I(U_n)=3\cdot2^q\). This also covers \(n=3\), when there is only one chosen vertex and its self-return gap is three.

**Case \(n=3q+2\).** Here \(k=q+1\); the gap string has exactly one gap of length two and \(k-1\) gaps of length three. There are \(nk/k=n\) selected sets, and every chosen vertex is an endpoint of a length-three gap, hence active. Thus \(m_I(U_n)=n2^k=n2^{q+1}\).

**Case \(n=3q+1\), with \(q\ge2\).** Here \(k=q+1\ge3\). The gap deficit of two permits either one gap of length one, or two gaps of length two. One length-one gap gives \(n\) selected sets, all chosen indices active, contributing \(n2^k\). Two length-two gaps that are cyclically adjacent give \(n\) selected sets. Their unique common endpoint may be inactive, while all other chosen indices are forced active; the contribution is \(n(2+1)2^{k-1}=3n2^{k-1}\). Finally, two nonadjacent length-two gaps give \(n(k-3)/2\) selected sets (there are \(k(k-3)/2\) unordered nonadjacent pairs of gap positions); all chosen indices are forced active, contributing \(n(k-3)2^{k-1}\). Summing yields

\[
 m_I(U_n)=n2^k+3n2^{k-1}+n(k-3)2^{k-1}=n(k+2)2^{k-1}=n(q+3)2^q.
\]

**Exceptional smallest order \(n=4\).** Here \(k=2\). Four minimum cycle dominating sets have gaps \((1,3)\), contributing \(4\cdot2^2=16\). The other two have gaps \((2,2)\). For each, at least one chosen index must be active: its two active labels contribute \(2^2=4\) if both active, and two possible single-active choices each contribute \(2\), totaling \(8\) per selected set. Hence \(m_I(U_4)=16+2\cdot8=32\), equal to \(4(1+3)2^1\). This completes the proof for every \(n\ge3\).

## Verification

The standalone program `checks/verify_sunlet.py` uses only Python standard-library tools. Run it from the package root with `python3 checks/verify_sunlet.py`. For each \(3\le n\le12\), it exhausts all \(3^n\) cycle-vertex labelings and independently computes the optimum admissible leaf labels and count. For each \(3\le n\le6\), a second unoptimized enumeration checks **all \(3^{2n}\) full vertex labelings** for Italian feasibility and optimum count. Its recorded output is `checks/verification_output.txt`; all checks passed. The exhaustive ranges test, but do not prove, the universal formulas, whose proof is above.

## Relationship to prior work

Shao and Zhao [1] introduced and studied Italian-domination counting polynomials, providing explicit and algorithmic results for trees and plain cycles. Their 31-page preprint does not supply the sunlet minimum-coefficient formula; its stated graph-family results and tables concern paths, trees, stars, and cycles. The *scalar* minimum weight for any ordinary corona with a leaf per base vertex was already established by the Roman \(\{2\}\)-domination theorem of Alizadeh et al. [2, Theorem 3.2] and the Italian rooted-product result of Hernández-Ortiz, Montejano and Rodríguez-Velázquez [3, Corollary 3.1]. Those references imply the weight but not an enumerative coefficient. The new contribution is the exact labeled multiplicity and the cyclic-gap classification of optimizers. The sunlet definition agrees with [4].

## Limitations

This is an exact count of **minimum-weight** functions on \(C_n\odot K_1\), not a formula for the complete Italian-domination polynomial, higher-weight coefficients, other corona factors, or arbitrary unicyclic graphs. The finite verifier cannot establish any claim for arbitrary \(n\), and literature searching cannot rule out all unindexed equivalent enumerations. The scientific review is same-model only; an independent external audit has not occurred.

## References

[1] P. Shao and C. Zhao, *Counting Weight-k Italian Dominating Sets on Trees and Cycles*, arXiv:2610.00108v1, first submitted 2026-09-09. https://arxiv.org/abs/2610.00108

[2] F. Alizadeh, H. R. Maimani, L. Parsaei Majd, and M. Rajabi Parsa, *Roman {2}-domination in graphs and graph products*, arXiv:1701.01416, Theorem 3.2. https://arxiv.org/abs/1701.01416

[3] R. Hernández-Ortiz, L. P. Montejano, and J. A. Rodríguez-Velázquez, *Italian domination in rooted product graphs*, arXiv:2006.02124, Corollary 3.1. https://arxiv.org/abs/2006.02124

[4] E. W. Weisstein, *Sunlet Graph*, MathWorld. https://mathworld.wolfram.com/SunletGraph.html
