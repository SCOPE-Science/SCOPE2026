# A square-root covariance transition among three-cycle-conditioned permutations

## Finding

Let \(\Pi_n\) be uniform over permutations of \(\{1,\ldots,n\}\) having **exactly three cycles**, and let \(C_{n,a}\) be its number of cycles of length \(a\). Fix an integer \(j\ge1\) and a real \(c>0\). For large \(n\), set \(r=\lfloor c\sqrt n\rfloor\) and \(k=n-j-r\). Write \(\gamma\) for the Euler--Mascheroni constant and \(c_*=e^{-\gamma/2}=0.749306\ldots\).

The covariance \(\operatorname{Cov}(C_{n,j},C_{n,k})\) is eventually **positive** if \(0<c<c_*\), and eventually **negative** if \(c\ge c_*\). The equality boundary belongs to the negative side. Specifically, if \(c\ne c_*\),
\[
\lim_{n\to\infty}\sqrt n(\log n)^3\operatorname{Cov}(C_{n,j},C_{n,k})=-\frac{4(\log c+\gamma/2)}{jc},
\]
while at \(c=c_*\),
\[
\lim_{n\to\infty}\sqrt n(\log n)^4\operatorname{Cov}(C_{n,j},C_{n,k})=-\frac{\pi^2}{3jc_*}.
\]

## Assumptions and scope

For each \(n\ge3\), the sample space is the uniform distribution on permutations with exactly three disjoint cycles (including fixed-point cycles). The two cycle lengths are distinct for all sufficiently large \(n\). Fix \(j\in\mathbb N\), \(c>0\) independently of \(n\). All limiting assertions are pointwise in \(j,c\), not uniform. The conditional covariance is computed within this three-cycle probability space. We use the harmonic numbers \(H_m=\sum_{t=1}^m 1/t\) and \(H_m^{(2)}=\sum_{t=1}^m 1/t^2\), with zero at \(m=0\), and unsigned Stirling numbers of the first kind \(\left[{m\atop a}\right]\).

## Proof

Define \(Z(m,a)=\left[{m\atop a}\right]/m!\) (zero for inadmissible indices). A uniformly random permutation has exactly \(a\) cycles with probability \(Z(m,a)\). Marking an ordered cycle of length \(j\), then a distinct ordered cycle of length \(k\), and requiring a total of three cycles gives, for distinct \(j,k\),
\[
\mathbb E C_{n,j}=\frac{Z(n-j,2)}{jZ(n,3)},\qquad
\mathbb E C_{n,k}=\frac{Z(n-k,2)}{kZ(n,3)},\qquad
\mathbb E(C_{n,j}C_{n,k})=\frac{Z(n-j-k,1)}{jkZ(n,3)}.
\]
These follow by choosing the labels of the marked cycles, cyclically ordering each, and freely partitioning the remaining labels into the indicated number of cycles. They give the **exact** identity
\[
\operatorname{Cov}(C_{n,j},C_{n,k})=
\frac{Z(n,3)Z(r,1)-Z(n-j,2)Z(n-k,2)}{jk\,Z(n,3)^2},
\qquad r=n-j-k.
\]
For \(r\ge1\), the coefficient identities \(Z(m,1)=1/m\), \(Z(m,2)=H_{m-1}/m\), and \(Z(m,3)=(H_{m-1}^2-H_{m-1}^{(2)})/(2m)\) are obtained by expanding \(\prod_{i=0}^{m-1}(z+i)/m!\) at small powers of \(z\). Consequently the covariance has precisely the sign of
\[
D_{n,j,r}=\frac{H_{n-1}^2-H_{n-1}^{(2)}}2
-\frac{nr}{(n-j)(j+r)}H_{n-j-1}H_{j+r-1}.
\]
Indeed, the exact covariance is \(D_{n,j,r}/(jk\,r\,Z(n,3)^2 n)\); every factor outside \(D\) is positive.

Now let \(L=\log n\). Since \(r=c\sqrt n+O(1)\) and \(j\) is fixed, standard harmonic expansions yield
\[
H_{n-1}=L+\gamma+O(n^{-1}),\quad
H_{n-j-1}=L+\gamma+O(n^{-1}),\quad
H_{j+r-1}=\tfrac12 L+\log c+\gamma+O(n^{-1/2}),
\]
\[
H_{n-1}^{(2)}=\frac{\pi^2}{6}+O(n^{-1}),\qquad
\frac{nr}{(n-j)(j+r)}=1+O(n^{-1/2}).
\]
The products of the errors with powers of \(L\) tend to zero. Substitution and collection of terms gives the critical expansion
\[
D_{n,j,r}=-(\log c+\gamma/2)L
-\gamma\log c-\gamma^2/2-\pi^2/12+o(1).
\]
If \(c<c_*\), the coefficient of \(L\) is positive. If \(c>c_*\), it is negative. If \(c=c_*\), that coefficient vanishes and \(D_{n,j,r}\to-\pi^2/12<0\). Thus every asserted strict eventual sign follows, including equality.

Finally, \(Z(n,3)\sim L^2/(2n)\), \(k\sim n\), and \(r\sim c\sqrt n\). Hence
\[
\operatorname{Cov}(C_{n,j},C_{n,k})=\frac{4D_{n,j,r}}{jc\sqrt n L^4}(1+o(1)),
\]
and the two stated normalizations follow from the corresponding terms of the expansion for \(D\). This proves the theorem.

## Verification

The standalone Python 3 program `verify.py` uses only the standard library. Running `python verify.py` exhaustively computes the conditional covariance from all three-cycle permutations through eight labels and compares it to the exact Stirling formula (55 comparisons). It performs 24,517 exact-rational harmonic/Stirling sign comparisons for parameters through 90 labels and four additional floating-point asymptotic sanity checks. The exhaustive and numerical checks do not substitute for the asymptotic proof.

## Relationship to prior work

The Ewens sampling formula, conditional cycle-count laws, and classical first-kind Stirling coefficients are established background; the exact conditional factorial-moment identity above is an application of those facts and is **not separately claimed to be novel**. The asserted contribution is the sharp square-root residual-label covariance transition, including the strict negative equality boundary and different logarithmic covariance scales. Tavaré's accessible exposition provides the conditioned Ewens law but does not state this transition in the material inspected. The accessible material in Lugo's permutation-profile paper and the abstract of Arratia--Barbour--Tavaré do not state it either. Published results on unconditioned cycle counts, other fixed-cycle statistics, and partitions were compared for implication overlap; they do not directly supply the asymptotic cancellation here.

## Limitations

The theorem concerns *exactly three* cycles, fixed \(j\), and fixed positive \(c\). No uniform convergence as \(j\) or \(c\) varies is established. No all-finite-\(n\) sign classification is asserted. The formulas are derived from established factorial moments; exhaustive priority over older conditional-permutation asymptotics has not been established. The inspected literature includes relevant full subsections and a scanned PDF, but an older plausible full text was inaccessible, so historical duplication remains a residual risk.

## References

- R. Arratia, A. D. Barbour, S. Tavaré (1992), *Poisson Process Approximations for the Ewens Sampling Formula*, Annals of Applied Probability 2, 519--535, DOI: 10.1214/aoap/1177005647 (first verified public date 1992-08-01).
- M. Lugo (2009), *Profiles of Permutations*, Electronic Journal of Combinatorics 16, R99, DOI: 10.37236/188 (public 2009).
- S. Tavaré (2021), *The Magical Ewens Sampling Formula*, Bulletin of the London Mathematical Society, DOI: 10.1112/blms.12537; particularly conditional cycle-count formula and related sections.
