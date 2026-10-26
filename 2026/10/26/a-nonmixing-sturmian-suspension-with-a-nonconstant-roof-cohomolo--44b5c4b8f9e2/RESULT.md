# A nonmixing Sturmian suspension with a nonconstant roof cohomology class

## Finding
Let \(Q_k=10^{k!}\) for integers \(k\ge1\), let \(\alpha=\sum_{k\ge1}Q_k^{-1}\), and let \(R_\alpha\) be rotation of the circle \(\mathbb T=\mathbb R/\mathbb Z\) by \(\alpha\). Define
\[
f(\theta)=\sum_{k\ge1}Q_k^{-2}\cos(2\pi Q_k\theta),\qquad \rho(\theta)=2+f(\theta).
\]
Let \((X_\alpha,\sigma)\) be the **two-sided Sturmian shift** obtained by coding \(R_\alpha\) with the partition \([0,1-\alpha)\), \([1-\alpha,1)\); write \(\pi:X_\alpha\to\mathbb T\) for its canonical rotation factor. The continuous positive roof \(r=\rho\circ\pi\) has all the following properties:

1. Its suspension flow is **not topologically mixing**.
2. The roof is **not continuously cohomologous to any constant**: there are no real \(c\) and continuous \(U:X_\alpha\to\mathbb R\) with \(r-c=U\circ\sigma-U\).
3. For every \(k\ge2\), its circle-factor Birkhoff sums satisfy the explicit uniform estimate
\[
\left\|\sum_{j=0}^{Q_k-1}\rho(\cdot+j\alpha)-2Q_k\right\|_\infty<\frac3{Q_k},
\qquad \|Q_k\alpha\|_{\mathbb R/\mathbb Z}<\frac{2Q_k}{Q_{k+1}}.
\]
In particular, the circle suspension factor has a sequence of near-identity return times \(2Q_k\to\infty\) even though the roof has nontrivial continuous cohomology class. This is a concrete negative answer to the minimal-shift cohomology question posed as Question 3.15 of Day (2025).

## Assumptions and scope
The symbolic alphabet is \(\{0,1\}\), and \(X_\alpha\) is the closure of the bi-infinite itineraries of points whose rotation orbits avoid the partition endpoints. The shift is minimal and the factor \(\pi\) is a continuous surjection intertwining \(\sigma\) with \(R_\alpha\). At most two symbolic points lie over a circle point, and a pair in a nontrivial fiber differs in only finitely many symbolic coordinates. These properties also follow directly from the rotation coding: all partition boundaries belong to one irrational rotation orbit.

The cohomology assertion concerns **continuous additive** transfers and constants, not measurable or \(L^2\) cohomology. The nonmixing assertion concerns the **topological** suspension flow, not merely measure-theoretic mixing. The roof is continuous on the symbolic shift and is the pullback of a \(C^1\) function on the circle. All asymptotic estimates concern the explicit subsequence \(Q_k\), not every iterate.

## Proof
**1. Arithmetic and regularity.** Write \(p_k/Q_k=\sum_{j=1}^k Q_j^{-1}\), with \(p_k\) integral, and put \(\delta_k=Q_k\alpha-p_k\). Since \(Q_{k+1}=Q_k^{k+1}\), the remaining positive tail satisfies
\[
\frac{Q_k}{Q_{k+1}}<\delta_k<\frac{2Q_k}{Q_{k+1}}<\frac12.
\]
The rapidly increasing rational denominators prove \(\alpha\) irrational: otherwise, for a fixed denominator \(b\), the nonzero rational approximation error would be at least \(1/(bQ_k)\), contradicting \(\alpha-p_k/Q_k<2/Q_{k+1}\) for large \(k\). Hence \(\|Q_k\alpha\|=\delta_k\). The series for \(f\) and its first derivative converge uniformly because \(\sum_k Q_k^{-2}\) and \(\sum_k Q_k^{-1}\) converge. Also \(\|f\|_\infty<1/50\), so \(r>0\).

**2. Explicit uniform Birkhoff rigidity.** For \(j<k\), the finite geometric-series identity, \(|1-e^{2\pi it}|\ge4\|t\|\), and \(\|Q_j\alpha\|=\delta_j\ge Q_j/Q_{j+1}\) yield
\[
\left|\sum_{\ell=0}^{Q_k-1}e^{2\pi iQ_j(\theta+\ell\alpha)}\right|
\le \frac{2\pi Q_j\delta_k}{4\delta_j}
\le\frac\pi2\,\delta_k Q_{j+1}.
\]
For \(j\ge k\) the same geometric sum has modulus at most \(Q_k\). Summing the Fourier coefficients and using \(Q_{j+1}\le Q_k\) for \(j<k\) gives
\[
\begin{aligned}
\left\|\sum_{\ell=0}^{Q_k-1}f(\cdot+\ell\alpha)\right\|_\infty
&\le\frac\pi2\,\delta_k\sum_{j<k}\frac{Q_{j+1}}{Q_j^2}
  +Q_k\sum_{j\ge k}\frac1{Q_j^2}\\
&<\frac{\pi}{50}\frac{Q_k^2}{Q_{k+1}}+\frac2{Q_k}
\le\frac{2+\pi/50}{Q_k}<\frac3{Q_k}\quad(k\ge2).
\end{aligned}
\]
Here the elementary series bounds are \(\sum_{j\ge1}Q_j^{-2}<1/50\) and \(\sum_{j\ge k}Q_j^{-2}<2Q_k^{-2}\); the penultimate inequality uses \(Q_{k+1}\ge Q_k^3\).

**3. Absence of a continuous circle transfer.** Suppose \(f=v\circ R_\alpha-v\) for continuous \(v:\mathbb T\to\mathbb R\). The Fourier coefficient of \(f\) at frequency \(Q_k\) is \(1/(2Q_k^2)\), so
\[
|\widehat v(Q_k)|
=\frac{1}{2Q_k^2|e^{2\pi iQ_k\alpha}-1|}
>\frac{Q_{k+1}}{8\pi Q_k^3}\longrightarrow\infty.
\]
This contradicts the boundedness of Fourier coefficients of a continuous function.

**4. Descent of every symbolic transfer.** Assume \(r-c=U\circ\sigma-U\) on \(X_\alpha\). Integrating against any invariant probability measure on \(X_\alpha\), whose image under \(\pi\) is Haar measure on the uniquely ergodic irrational rotation, gives \(c=2\). If \(x,y\) lie in one fiber of \(\pi\), the roof takes equal values along their entire orbits. It follows that \(U(\sigma^n x)-U(\sigma^n y)=U(x)-U(y)\) for all \(n\ge0\). The symbolic pair differs at finitely many coordinates; hence \(d(\sigma^n x,\sigma^n y)\to0\). By continuity, \(U(x)=U(y)\). Thus \(U\) is constant on all fibers and descends to a continuous \(v:\mathbb T\to\mathbb R\). The cohomology identity descends to \(f=v\circ R_\alpha-v\), contradicting Step 3.

**5. Topological nonmixing.** The Sturmian suspension with roof \(r\) factors continuously and surjectively onto the circle-rotation suspension with roof \(\rho\), by mapping \([x,s]\mapsto[\pi(x),s]\). Choose two disjoint circle arcs \(I,J\) with separated closures, and a small vertical interval about height \(1\). For all sufficiently large \(k\), Step 2 gives \(\|S_{Q_k}\rho-2Q_k\|_\infty<3/Q_k\) and \(Q_k\alpha\to0\). Thus at time \(2Q_k\), every point in the flow box over \(I\) at this height has made exactly \(Q_k\) complete roof crossings and lies over \(I+Q_k\alpha\), with height changed by at most \(3/Q_k\). This image misses the corresponding flow box over \(J\) for arbitrarily large times \(2Q_k\). The circle suspension is not topologically mixing. Topological mixing passes to continuous factors, so neither is the Sturmian suspension. This completes the proof.

## Verification
The accompanying `verify.py` checks the exact factorial-denominator relations and rational upper/lower tail inequalities for the first several return scales, together with explicit numerical coefficient-growth and rigidity-bound inequalities. Run `python verify.py` in the directory of the extracted documents. Its finite checks are supplementary; the displayed inequalities and factor/cohomology arguments constitute the infinite proof.

## Relationship to prior work
Day, *Topologically mixing suspension flows over shift spaces* (arXiv:2501.15323v1, §3.1, Question 3.15) asks whether every continuous roof over a minimal shift that yields a non-topologically-mixing suspension must be continuously cohomologous to a constant. The construction above answers this question negatively for a concrete minimal Sturmian shift. The same paper handles synchronizing shifts and finite-type cases, which have different hypotheses.

Katok's nonmixing theorem for bounded-variation special flows over interval exchanges and the rotation-flow cohomological analysis of Fayad and Windsor are classical predecessors. They concern suspension flows over rotations and, in Katok's theorem, measure-theoretic rather than topological mixing. The new claim here is the explicit continuous symbolic counterexample to Day's minimal-shift question and its uniform quantitative return estimate, using the nontrivial but elementary descent of continuous cohomology through Sturmian fibers. Existing work on the regularity of **already existing** Sturmian transfers does not assert their existence for this roof.

## Limitations
The example is a particular Liouville rotation and a continuous pullback roof; it does not characterize all roofs over minimal shifts. The quantitative rigidity holds along the prescribed factorial denominators, not for all times. The work does not claim measure-theoretic weak mixing or nonmixing of the symbolic suspension. Its cohomological nontriviality excludes continuous transfers only, and no assertion of independent validation is made. Historical priority outside the inspected materials remains a risk.

## References
[1] J. Day, *Topologically mixing suspension flows over shift spaces*, arXiv:2501.15323v1 (first public January 25, 2025), especially Question 3.15, https://arxiv.org/html/2501.15323v1.

[2] A. Katok, *Interval exchange transformations and some special flows are not mixing*, Israel Journal of Mathematics **35** (1980), 301–310, https://doi.org/10.1007/BF02760655.

[3] B. Fayad and A. Windsor, *A dichotomy between discrete and continuous spectrum for a class of special flows over rotations*, Journal of Modern Dynamics **1** (2007), 107–122; arXiv:math/0501203, https://arxiv.org/abs/math/0501203.

[4] W. Huang, O. Jenkinson, L. Xu and Y. Zhang, *Sturmian beta-shifts do not have typical periodic optimization*, arXiv:2610.03619v1 (2026), https://arxiv.org/html/2610.03619v1.
