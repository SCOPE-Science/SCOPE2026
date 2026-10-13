# Corrected exact phase threshold for the binary Cayley-tree Blum–Kapel model
## Finding
For the ferromagnetic Blum–Kapel model on the Cayley tree of order \(2\), let \(\lambda=e^{J/T}>1\). The translation-invariant boundary laws are the positive solutions of
\[
z_1=\left(\frac{\lambda z_1+\lambda^{-1}z_2+1}{z_1+z_2+1}\right)^2,
\qquad
z_2=\left(\frac{\lambda^{-1}z_1+\lambda z_2+1}{z_1+z_2+1}\right)^2.
\]
Define
\[
p(\lambda)=4\lambda^4+7\lambda^3-14\lambda^2-33\lambda-12.
\]
This polynomial has a unique positive root
\[
\lambda_c=2.10281584329153637453671705775749\ldots .
\]
The system has exactly one positive solution for \(1<\lambda\le\lambda_c\), and exactly three positive solutions for \(\lambda>\lambda_c\). The two noncentral solutions are exchanged by \(z_1\leftrightarrow z_2\). Consequently, the value \(\lambda_{cr}\approx2.1132163\) stated in Theorem 4.3 of Khatamov--Khakimov is not the actual bifurcation point. In the source convention, the corrected temperature is \(T_c=J/\log\lambda_c\).

## Assumptions and scope
The claim concerns the ferromagnetic parameter range \(J>0\), \(T>0\), hence \(\lambda=e^{J/T}>1\), and only the translation-invariant Gibbs measures encoded by the source's positive boundary-law equations. It does not classify non-translation-invariant Gibbs measures and does not address extremality of the three translation-invariant measures below the critical temperature.

## Proof
Put \(x=\sqrt{z_1}>0\), \(y=\sqrt{z_2}>0\),
\[
u=x+y,\qquad a=\lambda+\lambda^{-1},\qquad b=\lambda-\lambda^{-1}.
\]
Because the right sides of the boundary-law equations are positive, taking the positive square roots is reversible and gives
\[
x(x^2+y^2+1)=\lambda x^2+\lambda^{-1}y^2+1,
\]
\[
y(x^2+y^2+1)=\lambda^{-1}x^2+\lambda y^2+1.
\]
If \(x=y\), writing the common value as \(x\) gives
\[
a=2x+x^{-1}-x^{-2}.
\]
The derivative of the right side is
\[
\frac{2x^3-x+2}{x^3}>0
\]
for every \(x>0\): the numerator has its positive minimum at \(x=1/\sqrt6\), where it is \(2-2/(3\sqrt6)>0\). Thus for every \(a\ge2\), and hence every \(\lambda\ge1\), there is exactly one symmetric positive solution.

Now suppose \(x\ne y\). Subtracting and adding the square-root equations gives
\[
x^2+y^2+1=bu,
\qquad
u(x^2+y^2+1)=a(x^2+y^2)+2.
\]
Eliminating \(x^2+y^2\) shows that \(u\) must satisfy
\[
Q_\lambda(u):=u^2-au+\frac{\lambda-1}{\lambda+1}=0.
\]
For \(\lambda>1\), this quadratic has two distinct positive roots \(u_-<u_+\), because its product is positive and its discriminant is
\[
a^2-4\frac{\lambda-1}{\lambda+1}
=
\frac{\lambda^5+\lambda^4-2\lambda^3+6\lambda^2+\lambda+1}{\lambda^2(\lambda+1)}>0.
\]
Writing \(d=x-y\), the identity \(x^2+y^2=bu-1\) yields
\[
d^2=D_\lambda(u):=2bu-u^2-2.
\]
Conversely, if a positive root \(u\) of \(Q_\lambda\) has \(D_\lambda(u)>0\), then
\[
x=\frac{u+\sqrt{D_\lambda(u)}}2,
\qquad
y=\frac{u-\sqrt{D_\lambda(u)}}2
\]
are positive and reconstruct a nonsymmetric solution. Positivity follows exactly from
\[
u^2-bu+1=\frac{2(\lambda u+\lambda+u)}{\lambda(\lambda+1)}>0,
\]
which holds on \(Q_\lambda(u)=0\).

The lower root never produces a nonsymmetric solution. For \(\lambda\le\sqrt3\), reducing \(D_\lambda\) modulo \(Q_\lambda\) gives
\[
D_\lambda(u)=\frac{\lambda^2-3}{\lambda}u-\frac{\lambda+3}{\lambda+1}<0.
\]
For \(\lambda>\sqrt3\), one has \(Q_\lambda(1/b)<0\), so \(u_-<1/b\), and therefore
\[
D_\lambda(u_-)<2b(1/b)-2=0.
\]
Thus only \(u_+\) can bifurcate.

At a bifurcation, \(D_\lambda(u_+)=0\). On a root of \(Q_\lambda\), the reduced formula above implies
\[
u=\frac{\lambda(\lambda+3)}{(\lambda+1)(\lambda^2-3)}.
\]
Substitution into \(Q_\lambda(u)=0\) gives the exact identity
\[
Q_\lambda\!\left(\frac{\lambda(\lambda+3)}{(\lambda+1)(\lambda^2-3)}\right)
=
-\frac{\lambda\,p(\lambda)}{(\lambda+1)^2(\lambda^2-3)^2}.
\]
The coefficient signs of \(p\) have exactly one sign change, so Descartes' rule gives exactly one positive root. Since \(p(2)=-14\) and \(p(3)=276\), that root lies in \((2,3)\). Because \(D_\lambda(u_-)<0\), this common root is necessarily the unique zero of \(D_\lambda(u_+)\). Evaluation at \(\lambda=2\) and \(\lambda=3\) fixes the sign: \(D_\lambda(u_+)<0\) below \(\lambda_c\) and \(D_\lambda(u_+)>0\) above it. Hence there are no nonsymmetric positive solutions for \(1<\lambda\le\lambda_c\), while for \(\lambda>\lambda_c\) the upper root yields exactly the two swapped nonsymmetric solutions. Together with the unique symmetric solution, this proves the claimed one-versus-three classification.

A rational isolating interval is
\[
2.102815<\lambda_c<2.102816,
\]
because the exact values of \(p\) at those endpoints have opposite signs. Numerically,
\[
\lambda_c=2.10281584329153637453671705775749\ldots,
\qquad
\frac{T_c}{J}=\frac1{\log\lambda_c}=1.34539285309644707749\ldots .
\]

## Verification
The accompanying `verify.py` checks the polynomial identity used at the bifurcation, the exact rational sign change on \((2.102815,2.102816)\), the single Descartes sign change, and a high-precision numerical root. It also reconstructs nonsymmetric solutions at several couplings above \(\lambda_c\) and evaluates the original two boundary-law equations. These computations corroborate the analytic proof; the phase count itself does not rely on finite sampling.

## Relationship to prior work
Khatamov and Khakimov derive exactly the boundary-law system above, prove uniqueness of the symmetric branch, and in Theorem 4.3 state a critical value \(\lambda_{cr}\approx2.1132163\), with one translation-invariant Gibbs measure below it and three above it. Their displayed discriminant calculation is numerical and is followed by a statement that cumbersome calculations determine the branch behavior. The exact reduction above shows that the actual coalescence occurs earlier, at the unique positive root of \(p\). In particular, every \(\lambda\) in \((\lambda_c,2.1132163)\) already has the two nonsymmetric positive solutions.

A later paper on the Blume--Capel model with a “wand” constraint has a different interaction constraint and a different recursion; its exact critical value does not imply the threshold here. Searches by the source identifier, the reported decimal, the corrected decimal, the exact quartic, and translation-invariant/boundary-law aliases did not locate a published correction or an equivalent exact threshold formula.

## Limitations
The result corrects the translation-invariant boundary-law threshold only. It does not re-evaluate the source's later extremality bounds, does not classify all Gibbs measures, and does not claim that no equivalent correction exists in literature that is not indexed by the sources searched. The numerical digits are supplementary; the exact statement is the unique-positive-root characterization.

## References
1. N. Khatamov and R. Khakimov, “Translation-Invariant Gibbs Measures for the Blum--Kapel Model on a Cayley Tree,” Journal of Mathematical Physics, Analysis, Geometry 15 (2019), 239--255. DOI: 10.15407/mag15.02.239. Preprint: arXiv:1706.06130, first version 2017-06-15.
2. N. M. Khatamov, “Translation-Invariant Extreme Gibbs Measures for the Blume--Capel Model with a Wand on a Cayley Tree,” Ukrainian Mathematical Journal 72 (2020), 623--641. DOI: 10.1007/s11253-020-01804-y.
