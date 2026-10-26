# Two universal welfare thresholds for specialized public-goods equilibria on a path

## Finding

**Theorem (complete specialized-welfare phase diagram).** Consider the local public-goods game specified below on the path \(P_n\), \(n\ge2\). Among **specialized Nash equilibria** (not necessarily among all Nash equilibria), welfare-maximizing profiles are characterized solely by the path order and the scalar
\[
t=\frac{b(2e_*)-b(e_*)}{ce_*}\in(0,1).
\]
Write \(\ell=\lceil n/3\rceil\), \(u=\lfloor(n-1)/2\rfloor\), and \(M=\lceil n/2\rceil\). A specialized profile has a set \(I\) of specialists and let \(m=|I|\). Put \(a(I)\) equal to the number of nonspecialist vertices adjacent to exactly two specialists.

* For \(n\in\{2,4\}\), the maximizing specialist count is \(M\) for every \(t\in(0,1)\).
* For odd \(n\ge3\), the maximizing counts are \(\{\ell\}\) when \(t<1/3\), all integers in \([\ell,u]\) when \(t=1/3\), and \(\{u\}\) when \(t>1/3\). When \(\ell=u\), these formulas describe the same count.
* For even \(n\ge6\), the maximizing counts are \(\{\ell\}\) when \(t<1/3\), every integer in \([\ell,u]\) when \(t=1/3\), \(\{u\}\) when \(1/3<t<1/2\), \(\{u,M\}\) when \(t=1/2\), and \(\{M\}\) when \(t>1/2\). Again, coincident counts do not constitute separate regimes.

In each case an equilibrium with a specified optimizing count is welfare-maximizing **if and only if** it maximizes \(a(I)\) among maximal independent sets with that count: for \(\ell\le m\le u\), \(a(I)=3m-n\), while for \(m=M\), \(a(I)=M-1\). In particular, \(P_{12}\) is the smallest path exhibiting **three distinct strict-parameter specialist-count optima**: \(4,5,6\), respectively, as \(t\) traverses \((0,1/3)\), \((1/3,1/2)\), and \((1/2,1)\).

## Assumptions and scope

Vertices \(i=1,\dots,n\) choose effort \(x_i\ge0\) and receive payoff \(U_i=b(x_i+\sum_{j\sim i}x_j)-cx_i\). Assume \(c>0\), \(b:[0,\infty)\to\mathbb R\) differentiable, strictly increasing and strictly concave, and there exists \(e_*>0\) with \(b'(e_*)=c\). A *specialized Nash equilibrium* is one in which each effort is either \(0\) or \(e_*\). Equilibrium specialists form a maximal independent vertex set, and conversely every maximal independent set determines a specialized Nash equilibrium [1]. Indeed, a specialist has no contributing neighbor and uniquely optimizes at \(e_*\), while a zero-effort neighbor of a specialist optimizes at zero; the latter follows from strict concavity and \(b'(e_*)=c\).

All welfare comparisons below are **restricted to specialized Nash equilibria**. For such equilibria each vertex consumes either \(e_*\) or \(2e_*\). The number of vertices consuming \(2e_*\) is exactly \(a(I)\); those with two neighboring specialists are necessarily nonspecialists. Thus
\[
W(I)=\sum_i U_i=nb(e_*)+ce_*\bigl(t a(I)-m\bigr).
\]
Strict increase and strict concavity imply \(0<t<1\). No optimality assertion over non-specialized Nash equilibria or socially optimal off-equilibrium effort vectors is made.

## Proof

**Step 1: exact path encoding.** Encode specialists by ones in a binary string of length \(n\). Independence forbids consecutive ones, and domination forces at most two zeros between consecutive ones and at most one zero before the first or after the last one. Let \(e\in\{0,1,2\}\) count the zero endpoints. Among \(m-1\) interior gaps, let \(a\) contain one zero and the others two. Each singleton interior gap creates one vertex served by both adjacent specialists, so it contributes exactly one to \(a(I)\). Counting gives
\[
n=m+a+2(m-1-a)+e=3m-2-a+e,
\qquad a=3m-2+e-n.
\]
Every maximal independent set has \(\lceil n/3\rceil\le m\le\lceil n/2\rceil\). For each integer \(\ell\le m\le u\), placing zeros at both endpoints (\(e=2\)) and choosing exactly \(3m-n\) singleton interior gaps is feasible because \(0\le3m-n\le m-1\). This makes \(a=3m-n\), the maximum possible at that \(m\). For the remaining maximum count \(m=M\), all interior gaps are singletons, and \(a=M-1\). These constructions also cover path orders \(2,3,4\).

**Step 2: fixed-count dominance.** Since \(t>0\), only maximum \(a\) can maximize \(t a-m\) for fixed \(m\). Hence the best normalized score among specialized equilibria is the maximum of
\[
J_m=t(3m-n)-m=(3t-1)m-tn,\quad \ell\le m\le u,
\qquad J_M=t(M-1)-M.
\]
The first set is absent when \(n=2\) or \(4\). In that case \(M\) is the sole feasible specialist count.

**Step 3: the first threshold.** Where \(\ell\le u\), \(J_m\) is affine in \(m\) with slope \(3t-1\). Thus \(J_\ell\) dominates the regular candidates below \(t=1/3\), \(J_u\) above \(t=1/3\), and every regular count ties at equality.

**Step 4: the top alternating configuration.** If \(n=2k+1\) is odd, then \(u=k\), \(M=k+1\), and \(J_M-J_u=t-1<0\). Thus \(M\) never maximizes for odd \(n\). If \(n=2k\) is even with \(n\ge6\), then \(u=k-1\), \(M=k\), and \(J_M-J_u=2t-1\). For \(t\le1/3\), the regular winner \(J_\ell\ge J_u\) also beats \(J_M\). For \(1/3<t<1/2\), \(J_u\) strictly beats \(J_M\); equality occurs at \(t=1/2\); and for \(t>1/2\), \(J_M\) strictly beats \(J_u\), hence all regular counts. This proves the full set of maximizing counts and its tie cases.

**Step 5: sharp three-regime boundary.** Three distinct strict-regime optimal counts require an even order and \(\ell<u<M\). The first such even order is \(n=12\): for \(n=6,8,10\), \(\ell=u\), whereas \(n=12\) has \((\ell,u,M)=(4,5,6)\). The maximal-independent binary strings
\[
010010010010,\quad010101010010,\quad101010101010
\]
realize \((m,a)=(4,0),(5,3),(6,5)\), with normalized scores \(-4\), \(-5+3t\), and \(-6+5t\), giving both strict transitions. Every \(t\in(0,1)\) is achievable within the admissible benefit class: \(b_q(x)=ce^{qe_*}(1-e^{-qx})/q\), \(q>0\), has \(b_q'(e_*)=c\) and \(t=(1-e^{-qe_*})/(qe_*)\), a continuous strictly decreasing map from \((0,\infty)\) onto \((0,1)\).

## Verification

The included `verify.py` enumerates all independent binary strings of every path order \(2\) through \(23\), tests maximal domination directly, computes their \((m,a)\) profiles, and checks exact-rational welfare comparisons against the theorem at eight values of \(t\), including both threshold values. It checks the \(n=12\) witness strings separately. The packaged `verification_output.txt` records 2,508 enumerated maximal profiles and 248 exact-rational assertions. These tests are finite corroboration; Steps 1–5 supply the proof for arbitrary \(n\) and admissible \(b\).

## Relationship to prior work

Bramoullé and Kranton [1] introduced the local public-goods game and proved the specialized-equilibrium/maximal-independent-set correspondence, which is used as a premise. Their general welfare discussion and examples do not give this exact, all-length path classification for arbitrary admissible concave benefits. Pandit and Kulkarni [2] examine welfare and effort of specialized equilibria and asymptotic concavity limits, not the interior parameter transitions \(t=1/3\) and \(t=1/2\) with their equality classifications. Chadha and Kulkarni [3] obtain other aggregate-effort and welfare bounds on line networks but do not imply the exact specialized-welfare comparison here. The reduction to counting singly and doubly served nonspecialists is specific to the objective in [1], not a new assertion about the general graph-theoretic correspondence.

## Limitations

The assertion is for specialized equilibria, not all Nash equilibria. It assumes a simple path, homogeneous benefits and costs, a unique positive best-response effort, and exact welfare ranking. Replacing the benefit function with one outside these assumptions, changing the topology, or introducing heterogeneous strategic parameters may invalidate the thresholds. The novelty comparison is best-knowledge rather than an independently certified exhaustive bibliography; possible equivalent results in graph domination, maximum-weight independent-set optimization, or local public-goods followups are residual risks.

## References

[1] Y. Bramoullé and R. Kranton, “Public Goods in Networks,” *Journal of Economic Theory* **135** (2007), 478–494, doi:10.1016/j.jet.2006.06.006. First available online September 28, 2006. Open manuscript: https://sites.duke.edu/rachelkranton/files/2016/09/publicgoodsinnetworksbramoullekrantonjet2007.pdf.

[2] P. Pandit and A. A. Kulkarni, “Refinement of the Equilibrium of Public Goods Games over Networks: Efficiency and Effort of Specialized Equilibria,” arXiv:1607.02037 (first submitted July 7, 2016), https://arxiv.org/abs/1607.02037.

[3] J. Chadha and A. A. Kulkarni, “Aggregate Play and Welfare in Strategic Interaction on Networks,” arXiv:1906.07630 (2019), https://arxiv.org/abs/1906.07630.
