# Exact factorization and corrected first delay crossing in a four-neuron BAM benchmark
## Finding
For the four-neuron delayed BAM system studied by Cui et al., the linearized characteristic determinant has a hidden scalar-shift factorization. If
\[
F(z)=z^4+3z^2-z+1,
\]
then the determinant in their equation (3.2) is exactly
\[
F\!\left(\lambda+a e^{-\lambda\theta}\right).
\]
At the Example 5.1 value \(a=1/4\), the first imaginary-axis crossing is
\[
\omega_*=0.70557055798271148897\ldots,
\qquad
\theta_*=0.87624353377550209284\ldots.
\]
The crossing is transverse, with
\[
\operatorname{Re}\!\left(\frac{d\lambda}{d\theta}\right)
=0.14796571376147417604\ldots>0.
\]
Therefore the zero equilibrium is linearly asymptotically stable for every \(0\leq\theta<\theta_*\) and loses linear stability at \(\theta_*\). The paper reports instead \(\phi_0=2.0083\) and \(\theta_0\approx0.8\) in Example 5.1. The frequency \(2.0083\) cannot be an imaginary-axis crossing frequency of the printed characteristic equation at any delay when \(a=1/4\).

## Assumptions and scope
The claim concerns the integer-order common-delay model printed as equation (1.3) of Cui et al. and its linearization at \(E=(0,0,0,0)\). The exact determinant factorization is valid for arbitrary positive \(a\). The numerical stability threshold is specialized to \(a=1/4\), exactly as in Example 5.1. Stability here means linear asymptotic stability of the zero equilibrium. No statement is made about the first Lyapunov coefficient, nonlinear Hopf direction, orbital stability of a periodic branch, or the hybrid-controlled model of Section 4.

## Proof
Write
\[
z=\lambda+a e^{-\lambda\theta}.
\]
The matrix in equation (3.2) has the same scalar \(z\) in each diagonal entry. Direct expansion gives
\[
\det M(z)=z^4+3z^2-z+1=F(z).
\]
Equivalently, expanding \(F(\lambda+a e^{-\lambda\theta})\) gives exactly equation (3.3): the coefficients of the four delay powers are \(4a\lambda^3+6a\lambda-a\), \(6a^2\lambda^2+3a^2\), \(4a^3\lambda\), and \(a^4\), respectively.

For \(a=1/4\), first consider \(F\). It has no real zero: for \(x<0\) every term in \(x^4+3x^2-x+1\) is positive, while for \(x\geq0\), \(3x^2-x+1>0\). Its discriminant is \(697\), so all four zeros are simple. Let \(z=x+iy\) be a zero in the upper half-plane. The imaginary part of \(F(z)=0\) gives
\[
4x(x^2-y^2)+6x-1=0.
\]
Eliminating \(y^2\) from the real part yields
\[
64x^6+96x^4+20x^2-1=0.
\]
Thus \(q=x^2\) is the unique positive root of
\[
64q^3+96q^2+20q-1=0,
\]
because the left side is strictly increasing for \(q\geq0\). Since its value at \(q=1/16\) is \(41/64>0\), the corresponding \(r=\sqrt q\) satisfies \(0<r<1/4\). Numerically,
\[
r=0.20372326785245767562\ldots.
\]
The two upper-half-plane roots are
\[
z_1=r+i y_1,
\qquad
z_2=-r+i y_2,
\]
where
\[
y_1=0.56066772800511655533\ldots,
\qquad
y_2=1.66392849560987718280\ldots.
\]
Set
\[
s=\sqrt{(1/4)^2-r^2}=0.14490282997759493365\ldots,
\qquad
\alpha=\arccos(4r)=0.61825163905472391238\ldots.
\]
If \(\lambda=i\omega\), the scalar branch equation \(i\omega+(1/4)e^{-i\omega\theta}=x+iy\) is equivalent to
\[
\frac14\cos(\omega\theta)=x,
\qquad
\omega-\frac14\sin(\omega\theta)=y.
\]
Consequently the four positive crossing frequencies and their smallest compatible delays are
\[
\begin{array}{c|c}
\omega & \theta\\ \hline
 y_1+s & \alpha/(y_1+s)\\
 y_2+s & (\pi-\alpha)/(y_2+s)\\
 y_2-s & (\pi+\alpha)/(y_2-s)\\
 y_1-s & (2\pi-\alpha)/(y_1-s)
\end{array}
\]
which evaluate respectively to
\[
\begin{array}{c|c}
0.705570557982711\ldots & 0.876243533775502\ldots\\
1.808831325587472\ldots & 1.395011784039918\ldots\\
1.519025665632282\ldots & 2.475168377803223\ldots\\
0.415764898027522\ldots & 13.625329350795438\ldots
\end{array}.
\]
All later phase representatives add \(2\pi/\omega\) to the corresponding delay, so \(\theta_*\) is the first possible imaginary-axis crossing.

At \(\theta=0\), the characteristic polynomial is
\[
F(\lambda+1/4)
=\lambda^4+\lambda^3+\frac{27}{8}\lambda^2+\frac{9}{16}\lambda+\frac{241}{256}.
\]
Its first three Hurwitz determinants are \(1\), \(45/16\), and \(41/64\), and the fourth is \((241/256)(41/64)\); all are positive. Hence the zero-delay system is Hurwitz. Also \(F(1/4)=241/256\neq0\), so \(\lambda=0\) is never characteristic for any delay. If a characteristic root satisfies \(\operatorname{Re}\lambda\geq0\), then its scalar branch obeys \(|\lambda-z_j|=(1/4)e^{-\theta\operatorname{Re}\lambda}\leq1/4\); thus right-half-plane roots remain in four fixed compact disks and cannot arrive from infinity as \(\theta\) varies. Standard spectral continuity for retarded constant-coefficient systems, together with the exhaustive crossing calculation above, therefore gives stability on \([0,\theta_*)\).

Finally, on the first branch \((x,y)=(r,y_1)\), one has
\[
\frac14 e^{-i\omega_*\theta_*}=r-is.
\]
Differentiating \(\lambda+(1/4)e^{-\lambda\theta}=z_1\) gives
\[
\frac{d\lambda}{d\theta}
=
\frac{(1/4)\lambda e^{-\lambda\theta}}{1-(1/4)\theta e^{-\lambda\theta}}.
\]
Therefore, at the crossing,
\[
\operatorname{Re}\!\left(\frac{d\lambda}{d\theta}\right)
=
\frac{\omega_*s}{(1-r\theta_*)^2+(s\theta_*)^2}>0,
\]
so a simple conjugate pair crosses into the right half-plane. The numerical value is \(0.14796571376147417604\ldots\).

## Verification
The accompanying `verify.py` reconstructs the symbolic coefficient identity underlying \(F(\lambda+a e^{-\lambda\theta})\), checks the exact rational Hurwitz determinants at \(a=1/4\), recomputes all four positive crossing frequencies and their first phase-compatible delays, verifies the characteristic residual at \((i\omega_*,\theta_*)\), and checks transversality. It also evaluates the source's reported frequency \(2.0083\): the complete crossing list has maximum \(1.808831325587472\ldots\), so \(2.0083\) is excluded independently of any rounding of \(\theta_0\).

## Relationship to prior work
Cui et al. print the common-delay model in equation (1.3), its characteristic determinant in equation (3.2), and the expanded quasipolynomial in equation (3.3). Their Example 5.1 uses \(a=0.25\) and reports \(\phi_0=2.0083\), \(\theta_0\approx0.8\), with simulations at \(\theta=0.76\) and \(\theta=1.1\). The simulations on opposite sides remain compatible with the corrected threshold, but the reported crossing pair is not.

The closest structural predecessor located was Vaishwar and Yadav's 2022 four-dimensional minimal neural network. Its linearized characteristic matrix delays only the first two self-feedback terms, leaving the third and fourth diagonal terms instantaneous. Even in its equal-first-two-delay case, that matrix does not have a common scalar diagonal shift and therefore does not imply the factorization or threshold proved here.

Searches of published published-finding corpus records using the source DOI/title, the reported numerical pair, the quartic factor, and common-delay aliases did not locate this correction. Exact web searches for the quartic factor and the corrected numerical threshold likewise did not locate a prior statement. These negative searches are evidence of comparison, not a proof of uniqueness.

## Limitations
The result is a correction to the linear spectral calculation for the printed common-delay system at \(a=1/4\). It does not compute the nonlinear normal form or first Lyapunov coefficient, so it does not by itself determine whether the crossing produces a supercritical or subcritical Hopf branch. It does not reassess the controller model, and it does not claim that every later citing paper has been exhaustively inspected.

## References
1. Q. Cui, C. Xu, W. Ou, Y. Pang, Z. Liu, J. Shen, M. Farman, S. Ahmad, “Further study on Hopf bifurcation and hybrid control strategy in BAM neural networks concerning time delay,” *AIMS Mathematics* 9(5) (2024), 13265–13290. DOI: 10.3934/math.2024647.
2. A. Vaishwar, B. K. Yadav, “Stability and Hopf-bifurcation analysis of four dimensional minimal neural network model with multiple time delays,” *Chinese Journal of Physics* 77 (2022), 300–318. DOI: 10.1016/j.cjph.2022.02.011.
3. J. K. Hale, S. M. Verduyn Lunel, *Introduction to Functional Differential Equations*, Springer, 1993.
