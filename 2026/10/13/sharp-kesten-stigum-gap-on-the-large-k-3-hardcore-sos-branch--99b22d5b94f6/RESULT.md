# Sharp Kesten–Stigum gap on the large \(k=3\) hardcore-SOS branch
## Finding
For the three-state hinge-graph \(p=\infty\) hardcore-SOS model on the Cayley tree of order \(k=3\), let \(\mu_1(\theta)\) be the translation-invariant splitting Gibbs measure corresponding to \(x=1\) and the large root \(y_1>2^{1/4}\), for \(0<\theta<1\). If \(\lambda(\theta)\) is the second-largest transition-matrix eigenvalue in absolute value, then
\[
\lambda(\theta)\le \frac13,
\qquad
3\lambda(\theta)^2-1\le-\frac23.
\]
The bound is sharp: equality holds exactly at \(y_1=\sqrt2\), equivalently \(\theta=1/\sqrt2\). Hence the Kesten–Stigum sufficient non-extremality condition \(3\lambda(\theta)^2>1\) is never satisfied on this entire branch.

## Assumptions and scope
The local spin set is \(\{0,1,2\}\), admissible nearest-neighbor spin differences are \(0\) and \(1\), and the activity is the hinge-graph \(p=\infty\) activity of Jahnel and Rozikov. The tree has order \(k=3\). Only the symmetric boundary-law branch \(x=1\) and its unique large root \(y_1>2^{1/4}\) are considered. The coupling range is \(0<\theta<1\), which is the range in which the second-largest absolute eigenvalue can be identified from the published transition-eigenvalue formulas.

## Proof
For \(k=3\) and \(x=1\), the boundary-law equation is
\[
\theta y^4-y^3+y-2\theta=0,
\]
and on the large branch it can be written as
\[
\theta=\frac{y^3-y}{y^4-2},
\qquad y>2^{1/4}.
\]
Put \(r=y^2\), so \(r>\sqrt2\). Multiplying by \(y^3\) gives
\[
\theta y^3
 =\frac{r^2(r-1)}{r^2-2}
 =2+\frac{(r-2)^2(r+1)}{r^2-2}
 \ge 2.
\]
The denominator is positive on \(r>\sqrt2\), so equality occurs exactly at \(r=2\), i.e. \(y=\sqrt2\). Substitution into the boundary-law equation gives \(\theta=1/\sqrt2\).

For \(x=1\), the two nontrivial transition-matrix eigenvalues are
\[
\lambda_1=\frac{(1-2\theta^2)y^3}{\theta y^6+(2\theta^2+1)y^3+2\theta},
\qquad
\lambda_2=\frac1{\theta y^3+1}.
\]
Write \(t=y^3>0\) and \(D=\theta t^2+(2\theta^2+1)t+2\theta>0\). Direct common-denominator calculation gives
\[
(\lambda_2-\lambda_1)D(\theta t+1)=2\theta(\theta t+1)^2>0
\]
and
\[
(\lambda_2+\lambda_1)D(\theta t+1)=2(\theta t+1)\bigl(t(1-\theta^2)+\theta\bigr)>0
\]
for \(0<\theta<1\). Thus \(|\lambda_1|\le\lambda_2\), so \(\lambda=\lambda_2\). Since \(\theta y^3\ge2\),
\[
\lambda=\frac1{\theta y^3+1}\le\frac13,
\qquad
3\lambda^2-1\le-\frac23.
\]
At \(\theta=1/\sqrt2\), \(y=\sqrt2\), the value \(\theta y^3=2\) makes both bounds equalities.

## Verification
The accompanying `verify.py` checks the exact polynomial identity behind
\[
\frac{r^2(r-1)}{r^2-2}-2
 =\frac{(r-2)^2(r+1)}{r^2-2},
\]
checks the cleared-denominator identities used to compare the two nontrivial eigenvalues, and numerically evaluates several points on the large branch as a consistency check. The proof itself is symbolic and does not depend on finite sampling.

## Relationship to prior work
Jahnel and Rozikov derive the same boundary-law equation and the two transition eigenvalues. For the \(k=3\) large root they prove only that the Kesten–Stigum condition fails when
\[
\theta>\frac{\sqrt3-1}{8^{1/4}}\approx0.435,
\]
using the coarse inequality \(y_1>2^{1/4}\). Their discussion then notes that stronger extremality analysis is challenging. The present factorization uses the exact relation between \(\theta\) and \(y_1\) and closes the Kesten–Stigum question on the whole interval \(0<\theta<1\), with a sharp margin.

A later paper on extreme hard-core-SOS Gibbs measures studies the wand admissibility graph and explicitly distinguishes its equations from the hinge-graph model considered here; it therefore does not imply this hinge-branch bound. Earlier three-state SOS extremality work treats a different finite-coupling SOS model on the binary tree and likewise does not imply this \(k=3\), \(p=\infty\) statement.

## Limitations
Kesten–Stigum gives a sufficient condition for non-extremality, not a necessary one in this setting. Therefore the strict negative bound does not prove that \(\mu_1\) is extreme. The finding is restricted to \(0<\theta<1\), \(k=3\), the hinge admissibility graph, and the large \(x=1\) branch. No claim is made for the small roots, nonsymmetric branches, other tree orders, or the wand model.

## References
1. Benedikt Jahnel and Utkir Rozikov, “Gibbs measures for hardcore-SOS models on Cayley trees,” arXiv:2404.03297; WIAS Preprint 3100; DOI: 10.1088/1742-5468/ad5433.
2. R. M. Khakimov, M. T. Makhammadaliev, and U. A. Rozikov, “Extreme Gibbs measures for a Hard-Core-SOS model on Cayley trees,” arXiv:2412.05963.
3. Christof Külske and Utkir A. Rozikov, “Extremality of Translation-Invariant Phases for a Three-State SOS-Model on the Binary Tree,” Journal of Statistical Physics 160 (2015), 659–680.
