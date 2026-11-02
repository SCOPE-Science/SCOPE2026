# One critical self-choice weight reverses the source–two-cycle covariance in random mappings

## Finding
Let \(n\ge3\) and \(w\ge0\). Independently for each vertex \(i\in\{1,\ldots,n\}\), select its image \(f(i)\) with probability \(w/(n-1+w)\) for \(f(i)=i\), and probability \(1/(n-1+w)\) for each \(f(i)\ne i\). Let \(Z\) denote the number of vertices of indegree zero in the resulting directed functional graph. For \(2\le r\le n\), let \(C_r\) count distinct directed cycles of length \(r\), identifying cyclic rotations.

Put \(a=n-1+w\) and \(q=\frac{n-1}{a}(\frac{a-1}{a})^{n-1}\). Then
\[
\operatorname{Cov}(Z,C_r)
=\frac{(n)_r}{r a^r}\,q\left[(n-r)\left(\frac a{a-1}\right)^r-n\right],
\]
where \((n)_r=n(n-1)\cdots(n-r+1)\).

For every \(3\le r\le n\), this covariance is **strictly negative** for every finite \(w\ge0\). For two-cycles there is exactly one critical weight
\[
w_n^*=\frac{\sqrt{n(n-2)}-(n-2)}{2}\in(0,1/2).
\]
The covariance \(\operatorname{Cov}(Z,C_2)\) is strictly positive when \(0\le w<w_n^*\), zero precisely at \(w=w_n^*\), and strictly negative when \(w>w_n^*\). In particular the loopless mapping model and the ordinary uniform mapping model are on opposite sides of this boundary.

For fixed \(w\ge0\) and fixed \(r\ge2\), as \(n\to\infty\),
\[
n\,\operatorname{Cov}(Z,C_r)\longrightarrow
 e^{-1}\left(\frac{3-r}{2}-w\right).
\]
The two-cycle boundary has the finer critical window \(w_n=\frac12+\frac tn\), with fixed \(t\in\mathbb R\) and \(n\) large enough that \(w_n\ge0\):
\[
n^2\operatorname{Cov}(Z,C_2)\longrightarrow
-\frac{t+1/4}{e}.
\]
Thus the finite-size critical value is \(w_n^*=1/2-1/(4n)+O(n^{-2})\).

## Assumptions and scope
Each of the \(n\) map images is independent, with one weight \(w\) on its own vertex and weight one on each other vertex. The distribution is *not* an independent identically distributed target law unless \(w=1\). A directed cycle of length \(r\ge2\) has \(r\) distinct vertices, so self-loops do not enter \(C_r\). Indegree counts all incoming arrows, including self-loops. All finite-size assertions hold simultaneously for every integer \(n\ge3\), every finite real \(w\ge0\), and every integer \(2\le r\le n\); the asymptotic assertions hold for each fixed positive length \(r\ge2\).

## Proof
**One-vertex avoidance probability.** Fix a vertex \(v\). Its own arrow avoids \(v\) with probability \((n-1)/a\); each of the other \(n-1\) arrows avoids \(v\) with probability \((a-1)/a\). Independence gives \(\Pr(\deg^-(v)=0)=q\), hence \(\mathbb EZ=nq\).

**Cycle and mixed expectations.** Fix an ordered cyclic word of \(r\) distinct vertices, up to rotation. Its \(r\) prescribed off-diagonal arrows occur with probability \(a^{-r}\). There are \((n)_r/r\) such cycles, so \(\mathbb EC_r=(n)_r/(r a^r)\). If \(v\) lies on the prescribed cycle, it receives an incoming arrow and cannot have indegree zero. If \(v\) lies outside it, the \(r\) prescribed source arrows are already known to point elsewhere than \(v\); the other source images remain independent. Therefore its conditional probability of indegree zero is \(q(a/(a-1))^r\). There are exactly \(n-r\) eligible vertices, giving
\[
\mathbb E(ZC_r)=\frac{(n)_r}{r a^r}(n-r)q\left(\frac a{a-1}\right)^r.
\]
Subtracting \(\mathbb EZ\mathbb EC_r\) proves the covariance formula.

**The strict sign classification.** Let \(B_r=(n-r)(a/(a-1))^r-n\). For \(2\le r<n\), the ratio of consecutive positive quantities \(F_r=(n-r)(a/(a-1))^r\) is
\[
\frac{F_{r+1}}{F_r}=\frac{n-r-1}{n-r}\frac a{a-1}<1,
\]
since the inequality is equivalent to \(a>n-r\), namely \(r-1+w>0\). At \(r=n\), \(F_n=0\). For each \(r\), \(F_r\) is nonincreasing as \(w\) increases, since \(a/(a-1)\) decreases with \(w\). At \(w=0\), direct cancellation gives
\[
B_3=-\frac{2n-3}{(n-2)^3}<0
\]
for \(n\ge3\), hence \(B_r<0\) for all \(r\ge3\) and \(w\ge0\). For \(r=2\), simplification yields
\[
B_2=-\frac{2w^2+2(n-2)w-(n-2)}{(n-2+w)^2}.
\]
The numerator is strictly increasing on \([0,\infty)\), starts negative and has the unique positive root \(w_n^*\) displayed above. Every multiplicative factor outside \(B_r\) in the covariance formula is strictly positive, completing all sign claims.

**Asymptotics.** For fixed \(r,w\), use \(a=n-1+w\), \(q=e^{-1}+O(n^{-1})\), and \((n)_r/a^r=1+O(n^{-1})\). The binomial expansion gives
\[
(n-r)\left(1+\frac1{n-2+w}\right)^r-n
=\frac r n\left(\frac{3-r}{2}-w\right)+O(n^{-2}).
\]
Multiplication establishes the fixed-weight first-order limit. For \(r=2\), substitute \(w=1/2+t/n\) into the exact displayed expression for \(B_2\): \(n^2 B_2\to-(2t+1/2)\); while \(\mathbb EC_2\to1/2\) and \(q\to e^{-1}\). This proves the critical-window limit. A second-order Taylor expansion of \(\sqrt{n(n-2)}\) gives \(w_n^*=1/2-1/(4n)+O(n^{-2})\).

## Verification
An independently written standard-library checker enumerates all \(n^n\) maps for each \(n\in\{3,4,5,6\}\) at the rational weights \(w\in\{0,1/4,1/2,1,2\}\). It compares exact weighted rational covariances to the closed formula at all lengths, and checks each sign against the formula. The same checker also verifies negativity of the analytic bracket for many larger finite parameter choices. Its executable is `verify_weighted_mapping.py`, run as `python verify_weighted_mapping.py`. The finite checks are corroboration, not a substitute for the unrestricted proof above.

## Relationship to prior work
Tavaré, *A note on the Screaming Toes game* (arXiv:2006.04805v1, 2020) studies the precisely loopless endpoint \(w=0\), and provides exact component and directed-cycle statistics. Classical uniform random mapping results address \(w=1\). The endpoint covariance signs in the loopless model have also been derived elsewhere. The contribution here is the **entire diagonal-weight interpolation**, its unique exact two-cycle sign boundary at \(w_n^*\), the strict absence of analogous reversals for longer cycles, and the microscopic crossover at weight \(1/2\). A previous endpoint-specific result does not by itself imply these interior-parameter statements. An undiscovered equivalent derivation in the larger random-mapping literature remains a historical-priority risk.

## Limitations
This concerns independent images and a common, nonnegative diagonal weight, not arbitrary source-dependent or correlated mappings. Cycles counted have length at least two; the number of one-cycles is not analyzed here. The covariance sign does not assert stochastic independence at its vanishing point. The asymptotic claims are for fixed cycle length and weight, apart from the stated two-cycle critical window. Finite enumeration cannot establish historical priority or replace the proof for unbounded \(n\).

## References
1. Simon Tavaré, *A note on the Screaming Toes game*, arXiv:2006.04805v1, submitted 8 June 2020, https://arxiv.org/abs/2006.04805 ; freely available full manuscript https://www.columbia.edu/cu/simontavare/STpapers-pdf/t20a.pdf .
2. P. Flajolet and A. M. Odlyzko, *Random mapping statistics*, in *Advances in Cryptology — EUROCRYPT '89*, Lecture Notes in Computer Science 434, Springer, 1990. (Background on the classical random-mapping model.)
