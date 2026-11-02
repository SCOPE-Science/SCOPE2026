# A sharp slow-bath reversal of fourth-order temporal irreversibility under partial resetting

## Finding

In the two-coordinate viscoelastic tracer model of Santra and Das, resetting only the tracer can reverse the **long-lag sign** of a fourth-order, time-reversal-odd correlation. At reset rate one and for every bath parameter \(\gamma>0\), define
\[
H_\gamma(t)=\mathbb E_\pi[X_0X_t^3]-\mathbb E_\pi[X_0^3X_t],\qquad t\ge0,
\]
where \(\pi\) is the unique stationary law. This quantity would vanish identically in time for a reversible stationary scalar process.

Let \(z\in(0,1)\) be determined by
\[
\gamma=\frac{1-z}{z(2-z)},
\]
and define
\[
\begin{aligned}
P(z)={}&12z^{11}-26z^{10}-323z^9+1081z^8+623z^7-5918z^6\\
&+5548z^5+3765z^4-6534z^3-87z^2+2204z-309.
\end{aligned}
\]
There is a unique root \(z_*\in(0,1)\) of \(P\), with
\[
z_*=0.150082549621956\ldots,\qquad
\gamma_* = \frac{1-z_*}{z_*(2-z_*)}=3.06121757563033\ldots.
\]
The short-time slope is strictly positive for **every** bath parameter:
\[
H_\gamma(0)=0,\qquad H_\gamma'(0+)=\tfrac12\mathbb E_\pi[X^4]>0.
\]
On the other hand, the coefficient of the slowest temporal mode exists and equals
\[
\lim_{t\to\infty} e^{zt}H_\gamma(t)=L(z),
\]
where
\[
L(z)=-\frac{6zP(z)}{(z-1)(z^2-2z+2)(z^2+z-3)
(z^3-z^2-9z+12)(6z^6-z^5-30z^4+45z^2+34z-60)}.
\]
The denominator is strictly negative for \(0<z<1\), hence the sharp slow-mode sign classification is
\[
L(z)<0\iff\gamma>\gamma_*,\qquad
L(z)=0\iff\gamma=\gamma_*,\qquad
L(z)>0\iff0<\gamma<\gamma_*.
\]
**Consequently, when \(\gamma>\gamma_*\), the time-odd correlation is positive for all sufficiently short positive lags and negative for all sufficiently long lags.** It therefore crosses zero at least once. The theorem classifies the *leading long-time coefficient* for the other regimes; it does **not** exclude intermediate-lag negative values when \(\gamma\le\gamma_*\), nor determine the sign at the exact critical point after cancellation of the leading mode.

## Assumptions and scope

Let \(X,Q\in\mathbb R\). Between jumps, independent Brownian motions \(B,W\) drive
\[
 dX=(-X+Q)\,dt+\sqrt2\,dB,\qquad
 dQ=\gamma^{-1}(X-Q)\,dt+\sqrt{2/\gamma}\,dW.
\]
At the event times of an independent rate-one Poisson process, set \(X\mapsto0\), while leaving \(Q\) unchanged. All statements are for this precisely normalized stationary continuous-time process, \(\gamma>0\), \(t\ge0\). They concern the scalar tracer's fourth-order two-time statistic and not total entropy production, general resetting rates, or a nonstationary initialization.

The quadratic Lyapunov function \(V=X^2+\gamma Q^2\) obeys
\[
\mathcal LV=-3X^2+4XQ-2Q^2+4.
\]
The quadratic form is positive definite; analogous polynomial Lyapunov estimates yield finite moments of all required orders. Nondegenerate independent noises, irreducibility and the drift bound give a unique stationary law. Simultaneous sign reversal \((X,Q)\mapsto(-X,-Q)\) makes all stationary moments of odd total degree zero.

## Proof

**1. Stationary mixed moments.** Write \(M_{i,j}=\mathbb E_\pi[X^iQ^j]\). The exact Markov generator, including the jumps, acts on monomials as
\[
\begin{aligned}
\mathcal L(x^iq^j)={}&-\bigl(i+j/\gamma+\mathbf1_{i>0}\bigr)x^iq^j
+i x^{i-1}q^{j+1}+(j/\gamma)x^{i+1}q^{j-1}\\
&+i(i-1)x^{i-2}q^j +[j(j-1)/\gamma]x^iq^{j-2},
\end{aligned}
\]
where terms with negative powers are omitted. Setting its stationary expectation to zero gives, at degree two,
\[
\begin{aligned}
-3M_{2,0}+2M_{1,1}+2&=0,\\
-(2+\gamma^{-1})M_{1,1}+M_{0,2}+\gamma^{-1}M_{2,0}&=0,\\
-M_{0,2}+M_{1,1}+1&=0.
\end{aligned}
\]
At degree four, the full closed system is
\[
\begin{aligned}
-5M_{4,0}+4M_{3,1}+12M_{2,0}&=0,\\
\gamma^{-1}M_{4,0}-(4+\gamma^{-1})M_{3,1}+3M_{2,2}+6M_{1,1}&=0,\\
2\gamma^{-1}M_{3,1}-(3+2\gamma^{-1})M_{2,2}+2M_{1,3}+2M_{0,2}+2\gamma^{-1}M_{2,0}&=0,\\
3\gamma^{-1}M_{2,2}-(2+3\gamma^{-1})M_{1,3}+M_{0,4}+6\gamma^{-1}M_{1,1}&=0,\\
M_{1,3}-M_{0,4}+3M_{0,2}&=0.
\end{aligned}
\]
These nonsingular linear systems determine the required moments without approximation.

**2. Exact two-time evolution.** The generator preserves the six-dimensional space spanned by
\((x^3,x^2q,xq^2,q^3,x,q)\). In this ordered basis its matrix has block form
\[
B=\begin{pmatrix}C&F\\0&A\end{pmatrix},\qquad
A=\begin{pmatrix}-2&1\\\gamma^{-1}&-\gamma^{-1}\end{pmatrix},
\]
with
\[
C=\begin{pmatrix}
-4&3&0&0\\
\gamma^{-1}&-(3+\gamma^{-1})&2&0\\
0&2\gamma^{-1}&-(2+2\gamma^{-1})&1\\
0&0&3\gamma^{-1}&-3\gamma^{-1}
\end{pmatrix},\qquad
F=\begin{pmatrix}6&0\\0&2\\2\gamma^{-1}&0\\0&6\gamma^{-1}\end{pmatrix}.
\]
For \(m=(M_{4,0},M_{3,1},M_{2,2},M_{1,3},M_{2,0},M_{1,1})^{\mathsf T}\) and \(n=(M_{4,0},M_{3,1})^{\mathsf T}\), the Markov property gives the exact identity
\[
H_\gamma(t)=(e^{Bt}m)_1-(e^{At}n)_1.
\]
Differentiation at zero, together with the first degree-four balance equation, gives \(H_\gamma'(0)=M_{4,0}/2>0\).

**3. Identify the slowest mode.** The matrix \(A\) has its larger eigenvalue \(-z\), where \(\gamma=(1-z)/[z(2-z)]\). Right and left eigenvectors are
\[
w=(1,2-z)^{\mathsf T},\qquad v=(1,\gamma(2-z))^{\mathsf T}.
\]
The second eigenvalue is strictly to the left of \(-z\). The four eigenvalues of \(C\) are also strictly to the left of \(-z\); a fully symbolic Routh–Hurwitz certificate is below. Thus the coefficient of the leading exponential in the exact two-time difference is
\[
L(z)=\frac{-e_1^{\mathsf T}(C+zI)^{-1}Fw\,(v^{\mathsf T}(M_{2,0},M_{1,1})^{\mathsf T})
-v^{\mathsf T}n}{v^{\mathsf T}w}.
\]
Solving the stationary moment systems and simplifying this rational expression yields exactly the displayed \(L(z)\), with numerator \(-6zP(z)\).

**4. A global spectral certificate.** Let \(p(s)=\det(sI-(C+zI))=s^4+a_1s^3+a_2s^2+a_3s+a_4\). The quartic Routh–Hurwitz conditions are positivity of \(a_1,a_2,a_3,a_4\), \(a_1a_2-a_3\), and \(a_1a_2a_3-a_3^2-a_1^2a_4\). Introduce \(u=z/(1-z)>0\). On substituting \(z=u/(1+u)\), each of these six rational functions has a strictly positive denominator and a numerator with nonnegative coefficients and at least one positive coefficient. In the order just specified, the numerators, written as descending coefficient vectors with the positive normalization fixed by the accompanying verifier, are
\[
\begin{aligned}
&(6,17,9),\\
&(11,63,124,99,26),\\
&(6,52,185,341,334,154,24),\\
&(6,46,122,132,48,0),\\
&(60,453,1276,1652,969,210),\\
&(360,5838,42096,177649,486133,903188,1159251,1025169,610958,233634,51708,5040).
\end{aligned}
\]
Each is positive for \(u>0\). Therefore \(C+zI\) is Hurwitz for every \(z\in(0,1)\), and the long-time residue calculation is justified without an assumption of distinct cubic eigenvalues.

**5. Uniqueness and signs of the threshold.** Under the same positive change of variable,
\[
\begin{aligned}
(1+u)^{11}P\!\left(\frac{u}{1+u}\right)
={}&36u^{11}+702u^{10}+5864u^9+27411u^8+78556u^7\\
&+142219u^6+161725u^5+110871u^4+40878u^3\\
&+4958u^2-1195u-309.
\end{aligned}
\]
Its descending coefficient sequence has precisely one sign change. Descartes' rule of signs gives at most one positive root; the constant term is negative and the leading coefficient positive, so exactly one exists. Since \(\gamma=(1-z)/[z(2-z)]\) strictly decreases with \(z\), its sign ordering converts to the stated \(\gamma\)-threshold. The factors \(z-1\), \(z^2+z-3\), and \(6z^6-z^5-30z^4+45z^2+34z-60\) are strictly negative throughout \((0,1)\); the remaining factors are positive. These signs follow either from elementary estimates or from the all-same-sign coefficient transforms used in `verify.py`. Thus the denominator is strictly negative, making \(\operatorname{sgn}L(z)=\operatorname{sgn}P(z)\). The theorem follows by continuity and strictness of the asymptotic sign when \(L\ne0\).

## Verification

The complete standalone `verify.py` uses exact SymPy rational algebra to reconstruct every mixed-moment equation from the generator, both invariant polynomial generator blocks, the short-time slope, the long-time spectral projection and its factorization, Routh–Hurwitz positivity certificates, Descartes polynomial, denominator signs, and the numerical threshold. Run `python verify.py` with SymPy installed. It performs additional finite parameter spot checks of the residue sign; those checks are supportive and not substitutes for the all-parameter algebraic proof. For example, at \(\gamma=10\), the slow-mode coefficient is approximately \(-0.0164672138435\).

## Relationship to prior work

Santra and Das (2026, arXiv:2603.17027v1, sections II–III and Appendix A) introduce this probe-only resetting viscoelastic bath and derive its stationary and time-dependent single-time moments, stationary density and kurtosis. Those model and moment-recursion elements are prior work. The present claim concerns a specific *two-time*, time-antisymmetric fourth-order tracer observable and the exact algebraic boundary for the sign of its slowest mode, which are not given in those inspected sections. Biswas, Dubbeldam, Sandev and Pal (2024/2025) study a related renewal-reset generalized Langevin model and obtain variance and ordinary two-time correlation, but reset the bath memory as part of renewal; they do not supply the nonrenewal fourth-order sign boundary. General finite-dimensional Markov semigroup and Routh–Hurwitz methods are classical, while the model-specific phase boundary and its interpretation are the assessed contribution.

## Limitations

The reset rate is fixed to one and both noise temperatures have the normalization in the displayed SDE. The threshold is for the coefficient of the **slowest exponential contribution**. For \(\gamma<\gamma_*\), eventual positive sign does not preclude transient negative correlations. At \(\gamma=\gamma_*\) the leading coefficient is zero, and this theorem does not classify the next-slowest term. It does not establish a fluctuation-theorem entropy production rate or an experimental signal-to-noise ratio. Full priority against all possibly relevant general nonequilibrium correlation results has not been independently established; the explicit stated sources and algebraic checks support only qualified best-knowledge originality.

## References

- I. Santra and D. Das, *Resetting in a viscoelastic bath: the bath remembers*, arXiv:2603.17027v1, first posted 17 March 2026, https://arxiv.org/html/2603.17027v1 . See sections II, III.1, III.2, III.3 and Appendix A.
- A. Biswas, J. L. A. Dubbeldam, T. Sandev and A. Pal, *A resetting particle embedded in a viscoelastic bath*, arXiv:2412.09260, first posted 12 December 2024; *Chaos* **35** (2025), 031102, https://doi.org/10.1063/5.0253019 .
- I. M. Sokolov, *Linear Response and Fluctuation-Dissipation Relations for Brownian Motion under Resetting*, *Phys. Rev. Lett.* **130** (2023), 067101, https://doi.org/10.1103/PhysRevLett.130.067101 .
