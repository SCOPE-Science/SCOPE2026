# An exact spectral census and square-root law for adaptive-threshold equilibria on complete bipartite graphs

## Finding
For all integers \(a,b\ge1\), consider the extended, evolving-threshold graph dynamical systems of Chang, Cochran, Mortveit, Raval and Schroeder on the labelled complete bipartite graph \(K_{a,b}\). Each vertex of degree \(d\) has a binary state and an individual integer threshold in \(\{1,\ldots,d+1\}\); the update compares its **closed-neighborhood** count of active vertices with its threshold. The increasing, decreasing and mixed threshold schemes, under parallel updates or any fixed permutation of sequential updates, have a common number \(F(a,b)\) of **extended-state fixed points**. Write \((u)_{\underline{k}}=u(u-1)\cdots(u-k+1)\) and \((u)_{\underline0}=1\). Then

\[
F(a,b)=(b+2)^a(a+2)^b\sum_{k=0}^{\min(a,b)}
\frac{(a)_{\underline{k}}(b)_{\underline{k}}}
{((a+2)(b+2))^k}.
\]

For \(h=ab/(a+b)\), as \(\min(a,b)\to\infty\), **without any balance assumption**, this obeys the sharp asymptotic law

\[
F(a,b)\sim (b+2)^a(a+2)^b\sqrt{\frac{\pi ab}{2(a+b)}}.
\]

For the balanced graphs \(K_{n,n}\), the fraction of all extended states that are fixed therefore satisfies

\[
\frac{F(n,n)}{[2(n+1)]^{2n}}
\sim \frac{e^2\sqrt\pi}{2}\,\frac{\sqrt n}{4^n}.
\]

The exact formula is the trace of a two-stage binomial kernel. Its full spectrum is the finite sequence of positive factors in the sum, with additional zero eigenvalues precisely when the second part is larger than the first (\(b>a\)). This kernel is an **enumeration device**, not the original adaptive-threshold dynamical map.

## Assumptions and scope
Let the disjoint vertex parts \(A,B\) have sizes \(a,b\ge1\), with every cross-part edge present and no within-part edges. The binary state at vertex \(v\) is \(x_v\in\{0,1\}\); its threshold \(k_v\) lies in \(\{1,\dots,d(v)+1\}\). Under a local update, its new binary state is \(1\) precisely when \(\sum_{w\in N[v]}x_w\ge k_v\), where \(N[v]\) includes \(v\). In the increasing scheme a threshold rises by one only upon a \(0\to1\) switch; in the decreasing scheme it falls by one only upon a \(1\to0\) switch; the mixed scheme performs both. Because each threshold changes only when its own bit changes, the extended state is locally fixed exactly when its bit is unchanged. For sequential updates in a permutation, each vertex updates once; hence a globally fixed extended state requires every vertex to remain unchanged at its individual update, so the same local condition characterizes fixed states in all six schemes.

The count distinguishes **labelled vertices and threshold assignments**. It does not count fixed binary configurations alone, basins of attraction, two-cycles, or orbit periods. The asymptotic requires both part sizes to grow, not merely their sum.

## Proof
**1. Exact local count.** Fix a binary configuration with \(i\) active vertices in \(A\) and \(j\) in \(B\). An active vertex in \(A\) sees \(j+1\) active sites in its closed neighborhood, so its threshold has exactly \(j+1\) allowed values. An inactive vertex in \(A\) sees \(j\) active sites and needs a threshold greater than \(j\), leaving exactly \(b+1-j\) values. The corresponding numbers on the other side are \(i+1\) for active vertices and \(a+1-i\) for inactive vertices. Choosing the active sites and multiplying independent threshold choices yields

\[
F(a,b)=\sum_{i=0}^{a}\sum_{j=0}^{b}
\binom ai\binom bj (j+1)^i(b+1-j)^{a-i}
(i+1)^j(a+1-i)^{b-j}.

\]

**2. Convert the double sum into a trace.** Define a conditional binomial law \(U_j(i)\) for \(0\le i\le a\), given \(0\le j\le b\), by

\[
U_j(i)=\binom ai\left(\frac{j+1}{b+2}\right)^i
\left(\frac{b+1-j}{b+2}\right)^{a-i},
\]

and a second law \(V_i(j)\), for \(0\le j\le b\), by

\[
V_i(j)=\binom bj\left(\frac{i+1}{a+2}\right)^j
\left(\frac{a+1-i}{a+2}\right)^{b-j}.
\]

Their parameters lie strictly between zero and one and each distribution sums to one. The two-step Markov operator on functions of \(j\in\{0,\ldots,b\}\) is

\[
(Qf)(j)=\sum_{i=0}^a U_j(i)\sum_{j'=0}^b V_i(j')f(j').
\]

Its matrix diagonal satisfies \(Q_{jj}=\sum_i U_j(i)V_i(j)\). Consequently equation (1) gives

\[
\frac{F(a,b)}{(b+2)^a(a+2)^b}=\operatorname{tr}Q.

\]

**3. Triangularize on the polynomial basis.** Every function on the \(b+1\) distinct integers \(0,\ldots,b\) has a unique interpolating polynomial of degree at most \(b\). For a binomial variable \(Y\sim\operatorname{Bin}(m,p)\) and every nonnegative integer \(r\), the factorial-moment identity \(\mathbb E[(Y)_{\underline r}]=(m)_{\underline r}p^r\), together with the monomial-to-falling-factorial expansion, shows that \(\mathbb E[Y^k]\) is a polynomial in \(p\) of degree \(\min(k,m)\) and, when \(k\le m\), its leading coefficient is \((m)_{\underline k}\).

Apply this first to \(J'\mid I=i\sim\operatorname{Bin}(b,(i+1)/(a+2))\). For \(0\le k\le b\), the polynomial \(\mathbb E[(J')^k\mid I=i]\) has leading \(i^k\)-coefficient \((b)_{\underline k}/(a+2)^k\). Then average over \(I\mid J=j\sim\operatorname{Bin}(a,(j+1)/(b+2))\). If \(k\le a\), the leading \(j^k\)-coefficient of \((Qj^k)(j)\) is

\[
\lambda_k=\frac{(a)_{\underline k}(b)_{\underline k}}
{((a+2)(b+2))^k}.
\]

If \(k>a\), the first binomial average has degree at most \(a<k\), so the diagonal coefficient is zero, consistent with \((a)_{\underline k}=0\). Hence the matrix of \(Q\) in the ordered monomial basis \(1,j,\ldots,j^b\) is triangular with diagonal \(\lambda_k\) for \(0\le k\le b\), where every \(\lambda_k\) with \(k>\min(a,b)\) vanishes. The trace identity (2) proves the exact formula for all positive \(a,b\).

**4. Sharp asymptotic for arbitrary growing parts.** Put \(h=ab/(a+b)\). For \(0\le k\le\min(a,b)\), the nonzero diagonal terms can be written

\[
\lambda_k=\prod_{r=0}^{k-1}
\frac{(a-r)(b-r)}{(a+2)(b+2)}.

\]

Fix \(t\ge0\) and put \(k=\lfloor t\sqrt h\rfloor\). When \(\min(a,b)\to\infty\), also \(h\to\infty\), and \(k\ll\min(a,b)\). Taking logarithms in (3) and expanding \(\log(1-u)\) at zero gives

\[
\log\lambda_k
=-\frac{k(k-1)}2\left(\frac1a+\frac1b\right)
+O\!\left(k\left(\frac1a+\frac1b\right)
+k^3\left(\frac1{a^2}+\frac1{b^2}\right)\right)
\longrightarrow -\frac{t^2}{2}.
\]

For an integrable uniform majorant, use \(\log(1-u)\le-u\) in (3). For \(a,b\ge2\),

\[
\lambda_k\le
\exp\!\left[-\left(\frac1{a+2}+\frac1{b+2}\right)
\frac{k(k+3)}2\right]
\le \exp\!\left(-\frac{k^2}{4h}\right).

\]

(The second inequality uses \(1/(a+2)+1/(b+2)\ge1/(2h)\).) The Gaussian majorant and pointwise convergence imply, by dominated Riemann-sum convergence,

\[
\frac1{\sqrt h}\sum_{k=0}^{\min(a,b)}\lambda_k
\longrightarrow \int_0^\infty e^{-t^2/2}\,dt
=\sqrt{\frac\pi2}.
\]

This establishes the general asymptotic. Finally, on \(K_{n,n}\) the full extended state space has exactly \([2(n+1)]^{2n}\) elements. Dividing the derived asymptotic by this total and using \(((n+2)/(n+1))^{2n}\to e^2\) establishes the claimed balanced fixed-state fraction.

## Verification
The standalone Python 3 program `checks.py` uses only standard-library modules. It independently brute-forces complete binary/threshold assignments for \((a,b)=(1,1),(1,2),(2,2),(2,3)\), then checks the integer double sum against the rational spectral sum for every \(1\le a,b\le7\). The brute-force counts are respectively \(10,42,324,2128\). In particular, \(K_{1,1}\) is the two-vertex path and \(K_{2,2}\) is the four-cycle, agreeing with the base counts \(10\) and \(324\) in the primary source. The script prints finite-size ratios approaching the asserted asymptotic constant for larger balanced instances; **these finite computations are not a proof of the limit**, which is established in Step 4.

Run with `python3 checks.py` in the directory containing this file.

## Relationship to prior work
Chang, Cochran, Mortveit, Raval and Schroeder introduced the evolving-threshold rules and proved common fixed-point conditions, with exact enumerations for paths and cycles and a procedure for trees. Their Section 4 does not state a complete-bipartite fixed-point count, a binomial-trace spectral identity, or the dense-graph square-root correction. Those are the present result's additions. The earlier Kuhlman–Mortveit–Murrugarra–Kumar work concerns **bi-threshold rules with fixed thresholds**, rather than thresholds included as changing state variables. Polynomial triangularization is related to classical Bernstein-operator spectral methods, notably Cooper and Waldron, but the auxiliary kernel here composes two dimension-changing biased binomial laws; the fixed-point enumeration identity and asymptotic are not asserted in the inspected sources.

## Limitations
This is an exact enumeration for complete bipartite graphs, not general graphs, and makes no claim concerning the sizes of basins, unstable fixed points, two-cycle counts, or distribution of convergence times. The matrix \(Q\) is a counting construction, not the original deterministic system's transition matrix. The leading asymptotic requires \(\min(a,b)\to\infty\); it is not claimed for a fixed part size. The originality assessment is bounded by indexed comparisons and accessible text; the full text of Cooper and Waldron's operator paper was not accessible in this check, so an unindexed equivalent application remains a residual risk.

## References
1. L. Chang, J. Cochran, H. S. Mortveit, S. Raval, M. Schroeder, *Adaptive Complex Contagions and Threshold Dynamical Systems*, first public arXiv version, 20 May 2013, https://arxiv.org/abs/1305.4599, especially Definitions 2.1–2.2, Theorem 3.1, and Section 4.
2. C. J. Kuhlman, H. S. Mortveit, D. Murrugarra, V. S. A. Kumar, *Bifurcations in Boolean Networks*, DMTCS, Automata proceedings, 2012, https://dmtcs.episciences.org/2975/pdf, especially Sections 2–4.
3. S. Cooper and S. Waldron, *The Eigenstructure of the Bernstein Operator*, *Journal of Approximation Theory* 105 (2000), 133–165, https://doi.org/10.1006/jath.2000.3464 (bibliographic abstract inspected; full text not accessed).
