# Exact Steiner-hub transport on the positive cone of equilateral Lipschitz-free \(p\)-spaces

## Finding
Let \(0<p<1\), \(m\ge2\), and \(1/2\le t\le1\). Let \(N=\{b,a_1,\ldots,a_m\}\) have all distinct pairwise distances equal to one, with base point \(b\). Let \(M=N\cup\{h\}\) extend those distances by \(d(h,z)=t\) for each \(z\in N\). For arbitrary nonnegative \(c_1,\ldots,c_m\), set
\[
 u_c=\sum_{i=1}^m c_i\bigl(\delta(a_i)-\delta(b)\bigr).
\]
Then the real Lipschitz-free \(p\)-norms are exactly
\[
 \boxed{\|u_c\|_{\mathcal F_p(N)}^p=\sum_{i=1}^m c_i^p,}
\]
\[
 \boxed{\|u_c\|_{\mathcal F_p(M)}^p=
 \min_{S\subseteq\{1,\ldots,m\}}
 \left[\sum_{i\notin S}c_i^p+t^p\left(\sum_{i\in S}c_i^p+
 \left(\sum_{i\in S}c_i\right)^p\right)\right].}
\]
The minimum is attained by routing precisely the sources indexed by \(S\) through the new hub \(h\), and all others directly to \(b\).

For the equal-source molecule \(u_m=\sum_{i=1}^m(\delta(a_i)-\delta(b))\), the formula collapses to
\[
\boxed{\|u_m\|_{\mathcal F_p(M)}^p=\min\{m,t^p(m+m^p)\}.}
\]
For \(t<1\), the canonical inclusion strictly decreases this molecule's norm **if and only if**
\[
\boxed{m>(t^{-p}-1)^{-1/(1-p)}.}
\]
Its exact inverse distortion at this molecule is
\[
\boxed{\frac{\|u_m\|_{\mathcal F_p(N)}}{\|u_m\|_{\mathcal F_p(M)}}
=\max\left\{1,\frac1{t(1+m^{p-1})^{1/p}}\right\}.}
\]
For fixed \(t\in(1/2,1)\), the real-valued critical cardinality \(m_*(p,t)=(t^{-p}-1)^{-1/(1-p)}\) satisfies
\[
\boxed{m_*(p,t)\sim t^{-1/(1-t)}
\left(\frac{t}{1-t}\right)^{1/(1-p)}\quad(p\uparrow1),}
\]
and \(m_*(p,t)\sim [p\log(1/t)]^{-1}\) as \(p\downarrow0\). At \(t=1/2\), the first limit is instead \(m_*(p,1/2)\to4\). At \(t=1\), the inclusion is isometric on this positive cone.

The subset minimization is genuinely needed for nonuniform masses: at \(p=t=1/2\), for ten coefficients equal to one and an eleventh equal to \(10^4\), the unique minimizing routing pattern sends only the ten unit sources through the hub, leaving the large source direct.

## Assumptions and scope
All scalars are real. The free space uses its canonical \(p\)-norm; the relevant domain is the cone of molecules with one sink and nonnegative source coefficients, not the entire free space. The given distances define an ordinary metric and also a \(p\)-metric because \(2t^p\ge1\). The empty-subset terms have the usual value zero. The critical cardinality is a real boundary; actual source counts are positive integers.

## Proof
**Finite-tree norm reduction.** The finite spanning-tree formula for Lipschitz-free \(p\)-norms, proved by Cúth and Raunig [2, Theorem 2.2], expresses \(\|u_c\|^p\) as the minimum over spanning trees rooted at \(b\) of
\[
\sum_{v\ne b} d(v,\pi(v))^p
\left|\sum_{w\in\operatorname{desc}(v)}\mu(w)\right|^p,
\]
where \(\pi(v)\) is the parent of \(v\), \(\mu(a_i)=c_i\), \(\mu(h)=0\), and the coefficient of \(b\) is the balancing negative sum. For this positive-source molecule each subtree flow is its total source mass and is nonnegative. Edges carrying zero mass can be ignored.

**No source-to-source edge is optimal.** Suppose a source \(a_i\) has another source \(a_j\) as parent, whose own parent is \(w\). Detach the entire subtree at \(a_i\) and reattach it to \(w\). Since \(d(a_i,w)\le1=d(a_i,a_j)\), the moved subtree's edge cost does not increase. The flow on \(a_j\to w\) decreases strictly by the positive total mass of the detached subtree, leaving at least the positive mass \(c_j\) there. Hence its contribution strictly decreases. The move produces a tree because \(w\) is an ancestor. We may therefore assume every positive-mass source's parent belongs to \(\{b,h\}\).

**The hub points directly to the sink.** If the hub has positive subtree flow and has a source \(a_j\) as parent, then \(a_j\)'s parent must be \(b\), because source-to-source edges are excluded and an edge back to \(h\) would create a cycle. Reattach the hub subtree directly to \(b\): its edge length remains \(t\), while the positive flow on \(a_j\to b\) strictly decreases. Consequently the hub, when used, must have parent \(b\). It follows that each \(a_i\) either sends \(c_i\) directly to \(b\), at cost \(c_i^p\), or to \(h\), at cost \(t^pc_i^p\); the hub sends their sum to \(b\), at cost \(t^p(\sum_{i\in S}c_i)^p\). All such configurations are feasible spanning trees, so minimizing their exact costs proves the asserted formula when coefficients are positive. Coefficients equal to zero follow by continuity of the finite-dimensional \(p\)-norm.

**The smaller metric space.** In \(N\), the same shortcut argument eliminates all source-to-source edges, leaving the direct-star tree with cost \(\sum c_i^p\). This agrees with Cúth and Raunig's general positive-molecule criterion [2, Theorem 2.8].

**Equal masses, threshold and singular scales.** If precisely \(k\) of the \(m\) unit sources use the hub, the cost is \(m-k+t^p(k+k^p)\). This is strictly concave in real \(k\in[0,m]\), since \(0<p<1\). Therefore its minimum over integer \(k\) occurs at \(k=0\) or \(k=m\), giving the two-branch formula. The strict inequality \(t^p(1+m^{p-1})<1\) is equivalent to the displayed threshold for \(t<1\). Taking logarithms, expanding \(\log(t^{-p}-1)\) at \(p=1\), and using \(t^{-p}-1\sim p\log(1/t)\) at \(p=0\) establishes the asymptotics. In particular, for \(t>1/2\),
\[
\log m_*(p,t)=\frac{\log(t/(1-t))}{1-p}
 -\frac{\log t}{1-t}+O(1-p).
\]
For \(t=1/2\) the diverging coefficient vanishes, leaving limit four.

**A genuinely selective minimizer.** At \(p=t=1/2\), take \(c_1=\cdots=c_{10}=1\) and \(c_{11}=10^4\). For the routing subset containing \(k\) of the ten unit masses, with or without the large mass, the cost is concave in \(k\). Hence it suffices to compare four endpoint patterns: none, the ten small masses, the large mass alone, and all eleven masses. Their respective costs are
\[
110,\qquad 100+\frac{10+\sqrt{10}}{\sqrt2},\qquad
10+100\sqrt2,\qquad\frac{110+\sqrt{10010}}{\sqrt2}.
\]
The second is strictly smallest. This demonstrates that the general subset formula cannot be replaced by just the empty and full subsets.

## Verification
The standalone file `CHECKER.py` independently enumerates all labelled spanning trees by Prüfer sequences for three positive-mass patterns and for each \(p\in\{1/4,1/2,4/5\}\), \(t\in\{1/2,7/10,1\}\) in dimensions with two through four sources. It compares the spanning-tree minimum against the closed subset formula. All 27 finite comparisons pass, along with two checks of the threshold and selective-routing example, for 29 asserted comparisons. These checks are only finite corroboration. The proof above establishes the theorem for every permitted real parameter and integer dimension.

## Relationship to prior work
Albiac, Ansorena, Cúth and Doucha [1, Theorem 6.1] constructed an infinite equilateral set and an added hub to demonstrate that a canonical inclusion can fail to be isometric for \(p<1\). In their construction the hub is at short distance from the nonbase leaves but retains distance one from the base point; the present construction instead uses equal hub distance \(t\) to **every** old point, including the base. Their argument gives a sufficient upper estimate for particular finite-support vectors, not this exact positive-cone cost or a necessary and sufficient support-size threshold. Cúth and Raunig [2, Theorem 2.2] supplied the general finite spanning-tree minimization, used here as an established starting point, and [2, Theorem 2.8] characterized positive molecules with fully direct routing. Albiac and Ansorena [3, Theorem 3.5] proved uniform isomorphic embeddability for all pointed \(p\)-metric inclusions, without an exact norm formula for this star.

Related published results on universal one-point Lipschitz extension factors and universal three-point inclusion constants study suprema over all maps or molecules, rather than the exact norm of each positive one-sink molecule in the present equiradial family. Their titles and mathematical summaries were compared; full text of those records was not available for an exhaustive implication check.

## Limitations
No exact norm formula is asserted for signed or complex-valued source coefficients, multiple hubs, arbitrary finite metrics, or the full inverse operator norm of the inclusion. The strict support threshold applies only to the equal-source test molecule; other positive molecules can shrink at different cardinalities. Earlier equivalent formulations expressed through finite nonlinear transportation algorithms remain a publication-priority risk, and no independent audit has been carried out.

## References
[1] F. Albiac, J. L. Ansorena, M. Cúth, M. Doucha, “Lipschitz free \(p\)-spaces for \(0<p<1\),” *Israel Journal of Mathematics* 240 (2020), 65–98, arXiv:1811.01265v2, especially §6.

[2] M. Cúth, T. Raunig, “Canonical embedding of Lipschitz-free \(p\)-spaces,” *Banach Journal of Mathematical Analysis* 18 (2024), Paper 33, arXiv:2311.02920v1, especially Theorems 2.2 and 2.8.

[3] F. Albiac, J. L. Ansorena, “Lipschitz extensions into \(p\)-Banach spaces, and canonical embeddings of Lipschitz-free \(p\)-spaces for \(0<p<1\),” arXiv:2603.28193v1, first public March 30, 2026, especially Theorems 3.1 and 3.5.

[4] “Sharp leaf-count transitions in one-point \(p\)-Banach Lipschitz extensions,” published research record b03e5cc2b3f1; mathematical title and summary compared, full text not obtained.

[5] “Exact three-point Lipschitz-free \(p\)-inclusion constant,” published research record 2bd77d9d70; mathematical title and summary compared, full text not obtained.
