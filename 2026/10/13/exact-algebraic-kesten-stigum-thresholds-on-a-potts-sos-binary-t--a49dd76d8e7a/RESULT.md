# Exact algebraic Kesten–Stigum thresholds on a Potts–SOS binary-tree branch
## Finding
For the three-state Potts–SOS model on the Cayley tree of order \(2\), consider the translation-invariant branch used by Rahmatullaev and Rasulova under the specialization \(r=\theta^2\). Their boundary-law equations reduce to \(x=1\) and
\[
F(\theta,y):=y^3-\theta y^2+2\theta y-2=0,
\qquad y>0.
\]
On this same branch the two nontrivial eigenvalues of the tree-indexed transition matrix are exactly
\[
0,
\qquad
\rho(\theta,y)=\frac{y(\theta-y)}{2\theta+y^2}.
\]
Hence the binary-tree Kesten–Stigum equality is \(2\rho(\theta,y)^2=1\). Eliminating \(y\) from this equality and \(F(\theta,y)=0\) gives
\[
P(\theta)=\theta^8-10\theta^7-\theta^6+40\theta^5-18\theta^4-70\theta^3-24\theta^2+1.
\]
The polynomial \(P\) has exactly two positive roots:
\[
\theta_-=0.16669933109403204097423640683729208055\ldots,
\]
\[
\theta_+=9.70630162779232446848704777772942539669\ldots.
\]
They are the exact algebraic values behind the source's two computer-reported Kesten–Stigum thresholds \(0.1666993311\) and \(9.706301628\), respectively.

Over \(\mathbb{Q}(\sqrt2)\), the octic splits as \(P=Q_-Q_+\), with
\[
Q_-(\theta)=\theta^4+5(\sqrt2-1)\theta^3+(12-8\sqrt2)\theta^2-17+12\sqrt2,
\]
\[
Q_+(\theta)=\theta^4-5(1+\sqrt2)\theta^3+(12+8\sqrt2)\theta^2-17-12\sqrt2.
\]
The first root is a \(\rho=-1/\sqrt2\) crossing on the unique branch. The second is a \(\rho=+1/\sqrt2\) crossing on the middle of the three positive branches present at large \(\theta\).

## Assumptions and scope
The local spin space is \(\{0,1,2\}\), the tree has order \(2\), and only the source specialization \(r=\theta^2\) is considered. The boundary-law normalization is the source normalization \(x=1\). The finding concerns the Kesten–Stigum sufficient condition for non-extremality, whose equality on a binary tree is \(2\lambda_{\max}^2=1\). It does not claim that this equality is the exact extremality/non-extremality boundary of the Gibbs measures.

## Proof
The source gives the boundary-law cubic \(F(\theta,y)=0\) and the quadratic equation for the two nontrivial transition-matrix eigenvalues. Under \(x=1\) and \(r=\theta^2\), the constant term of that eigenvalue equation is
\[
(2\theta^4-\theta^4r-2\theta^2r+r^3)xy=0.
\]
Also \(Z=\theta^2+\theta y^2+r=\theta(2\theta+y^2)\). The remaining nonzero root is therefore
\[
\rho=\frac{(2+y)\theta^2-Z}{Z}
     =\frac{y(\theta-y)}{2\theta+y^2}.
\]
Thus \(2\rho^2=1\) is equivalent, because \(2\theta+y^2>0\), to
\[
K(\theta,y):=2y^2(\theta-y)^2-(2\theta+y^2)^2=0.
\]
A direct Sylvester determinant gives
\[
\operatorname{Res}_y(F,K)=16P(\theta).
\]
An exact Sturm sequence shows that \(P\) has exactly two positive roots, one in \((0.1666993,0.1666994)\) and one in \((9.706301,9.706302)\).

For branch identification, factor
\[
P=Q_-Q_+
\]
over \(\mathbb{Q}(\sqrt2)\). The equality \(\rho=-1/\sqrt2\) is equivalent to
\[
(1-\sqrt2)y^2+\sqrt2\,\theta y+2\theta=0,
\]
and its resultant with \(F\) is a nonzero constant multiple of \(Q_-\). The equality \(\rho=+1/\sqrt2\) is equivalent to
\[
(1+\sqrt2)y^2-\sqrt2\,\theta y+2\theta=0,
\]
and its resultant with \(F\) is a nonzero constant multiple of \(Q_+\). Exact reduction modulo these quartics gives common-root representatives
\[
y_-(\theta)=-\frac{\sqrt2}{3}+\left(\frac{10}{3}+\frac{5\sqrt2}{3}\right)\theta+(12+9\sqrt2)\theta^2+\left(\frac{20}{3}+\frac{14\sqrt2}{3}\right)\theta^3,
\]
\[
y_+(\theta)=\frac{\sqrt2}{3}+\left(\frac{10}{3}-\frac{5\sqrt2}{3}\right)\theta+(12-9\sqrt2)\theta^2+\left(\frac{20}{3}-\frac{14\sqrt2}{3}\right)\theta^3.
\]
At \(\theta_-\), the cubic has only one real root, so \(y_-(\theta_-)\) is the unique positive branch. At \(\theta_+\), exact interval evaluation gives \(2<y_+(\theta_+)<3\). Since \(F(1)>0\), \(F(3)<0\), \(F(6)<0\), and \(F(8)>0\) throughout the isolating interval for \(\theta_+\), the three positive roots lie in \((0,1)\), \((2,3)\), and \((6,8)\); hence the common root is the middle branch.

## Verification
The accompanying verifier reconstructs the Sylvester determinant over the integer polynomial ring and checks that it is exactly \(16P\). It also builds a rational Sturm sequence for \(P\), certifies exactly two positive roots and one root in each stated rational interval, checks the factorization \(P=Q_-Q_+\) in \(\mathbb{Q}(\sqrt2)\), and numerically evaluates the two isolated roots at high precision only as a secondary readability check. The symbolic identities, not the decimal approximations, carry the proof.

## Relationship to prior work
Rahmatullaev and Rasulova derive the same boundary-law cubic and transition-matrix eigenvalue equation and apply the Kesten–Stigum condition. They state that a Maple computation yields thresholds approximately \(0.1666993311\) and \(9.706301628\), with no exact algebraic equation for either threshold. The present calculation identifies both numbers as the only positive roots of one octic and explains them as opposite-sign \(1/\sqrt2\) spectral crossings.

The earlier finite-state SOS analysis of Külske and Rozikov concerns the pure SOS interaction rather than the Potts–SOS interaction. A later general \(\lambda\)-model paper contains the Potts–SOS model as a special case but was not found to state this octic or these exact threshold values. Targeted searches for the octic, the high-precision roots, and the paired decimal thresholds produced no covering published statement.

## Limitations
Kesten–Stigum is used here exactly as in the source: as a sufficient non-extremality criterion. The result does not close any gap between sufficient non-extremality and sufficient extremality tests. The calculation is confined to \(r=\theta^2\) and \(x=1\). A weakly indexed equivalent derivation could still exist; in particular, a later general \(\lambda\)-model article is a residual comparison risk because only limited accessible material was available for direct statement-level comparison.

## References
1. M. M. Rahmatullaev and M. A. Rasulova, “Extremality of translation-invariant Gibbs measures for the Potts-SOS model on the Cayley tree,” arXiv:2104.00973v1, first public 2021-04-02; Journal of Statistical Mechanics: Theory and Experiment 2021, 073201, DOI: 10.1088/1742-5468/ac08ff.
2. C. Külske and U. A. Rozikov, “Extremality of Translation-Invariant Phases for a Three-State SOS-Model on the Binary Tree,” Journal of Statistical Physics 160 (2015), 659–680, DOI: 10.1007/s10955-015-1279-9.
3. F. M. Mukhamedov, M. M. Rahmatullaev, and M. A. Rasulova, “Extremality of translation-invariant Gibbs measures for the \(\lambda\)-model on the binary Cayley tree,” Theoretical and Mathematical Physics 210 (2022), 411–424, DOI: 10.1134/S0040577922030114.
