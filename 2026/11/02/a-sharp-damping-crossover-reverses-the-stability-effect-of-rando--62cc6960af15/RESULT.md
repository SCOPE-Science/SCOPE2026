# A sharp damping crossover reverses the stability effect of randomized Lie–Trotter order

## Finding

Consider the planar linear initial-value problem \(\dot y=(A+B)y\), with
\[
A=-aI+K\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
B=-aI-K\begin{pmatrix}0&0\\1&0\end{pmatrix},
\]
where \(a,K,h>0\) and \(h\) is the step length. The true flow has the exact norm \(\|y(t)\|_2=e^{-2at}\|y(0)\|_2\), so its continuous dynamics is exponentially stable for all these parameters.

At each step independently select either Lie–Trotter order, \(e^{hA}e^{hB}\) or \(e^{hB}e^{hA}\), with probability \(1/2\). Write \(s=Kh\) and \(Y_n\) for the randomized iterate starting from any deterministic \(Y_0\in\mathbb R^2\). Then, **for every integer \(n\ge0\)**,
\[
\mathbb E\|Y_n\|_2^2=\left[e^{-4ah}\left(1+\frac{s^4}{2}\right)\right]^n\|Y_0\|_2^2.
\]
Therefore the randomized method is asymptotically mean-square stable for every nonzero initial state exactly when
\[
a>a_{\rm rand}(s,h):=\frac{\log(1+s^4/2)}{4h}.
\]
At equality, the expected squared norm is constant and nonzero; below it the expected squared norm diverges exponentially.

For either *fixed* order, let
\[
R(s)=\begin{cases}
1,&0<s\le2,\\
\displaystyle\frac{s^2-2+s\sqrt{s^2-4}}{2},&s>2.
\end{cases}
\]
Every trajectory of a fixed-order scheme tends to zero exactly when
\[
a>a_{\rm fixed}(s,h):=\frac{\log R(s)}{2h}.
\]
At the fixed threshold at least one nonzero initial state does not decay; below it at least one state grows without bound.

There is **one and only one** positive dimensionless shear \(s_*>2\) at which the two stability thresholds meet. It is the square root of the unique real root \(x_*>4\) of
\[
x_*^3-8x_*^2+4x_*-16=0,
\qquad x_*=7.750259588325559\ldots,
\quad s_*=2.783928804464216\ldots.
\]
For \(0<s<s_*\), \(a_{\rm fixed}<a_{\rm rand}\). Thus one can have **both fixed orders asymptotically stable but independent fair order selection mean-square unstable**. For \(s>s_*\), the strict inequalities reverse, and one can have **independent fair order selection mean-square stable although both fixed orders are unstable**. At \(s=s_*\), the sharp thresholds are equal.

The two reversals have simple exact witnesses. At \(h=K=s=1\) and \(e^{-2ah}=9/10\), each fixed order has spectral radius \(9/10\), but the randomized squared-norm multiplier is \(243/200>1\). At \(h=1\), \(K=s=3\), and \(e^{-2ah}=1/\sqrt{44}\), the randomized multiplier is \(83/88<1\), but each fixed order has spectral radius \((7+3\sqrt5)/(2\sqrt{44})>1\).

## Assumptions and scope

The parameters \(a,K,h\) are strictly positive. Operators \(A\) and \(B\) are the exact, time-independent \(2\times2\) real matrices displayed above. Both subflows are integrated exactly, for the same positive step length \(h\). In the randomized scheme, a *fresh independent fair* order selection is made at **every** step, independently of the current iterate. Initial states are deterministic, including the zero state for which all quantities vanish. All stability statements refer to convergence to zero as the number of steps tends to infinity at fixed \(h\). Randomized stability is in the **mean-square** sense, not a claim about almost-sure Lyapunov exponents. Fixed-order stability refers to decay of every initial state, equivalently Schur stability of its step matrix.

## Proof

**1. Exact flow and split matrices.** Since
\[
A+B=-2aI+K\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\]
and the second summand is skew-symmetric, \(e^{t(A+B)}=e^{-2at}\) times a rotation. Both off-diagonal nilpotents square to zero, so with \(q=e^{-2ah}\),
\[
e^{hA}=e^{-ah}\begin{pmatrix}1&s\\0&1\end{pmatrix},\qquad
e^{hB}=e^{-ah}\begin{pmatrix}1&0\\-s&1\end{pmatrix}.
\]
The two full step matrices are
\[
M_+=qF_s,\quad M_-=qG_s,\qquad
F_s=\begin{pmatrix}1-s^2&s\\-s&1\end{pmatrix},\quad
G_s=\begin{pmatrix}1&s\\-s&1-s^2\end{pmatrix}.
\]

**2. Exact all-step second moments.** Direct multiplication gives
\[
F_s^{\mathsf T}F_s=\begin{pmatrix}1-s^2+s^4&-s^3\\-s^3&1+s^2\end{pmatrix},\quad
G_s^{\mathsf T}G_s=\begin{pmatrix}1+s^2&s^3\\s^3&1-s^2+s^4\end{pmatrix},
\]
and therefore the exact, direction-independent identity
\[
\frac{M_+^{\mathsf T}M_++M_-^{\mathsf T}M_-}{2}
=q^2\left(1+\frac{s^4}{2}\right)I.
\]
Conditioning on \(Y_n\), using independence of the next fair order choice, yields
\[
\mathbb E[\|Y_{n+1}\|_2^2\mid Y_n]
=q^2(1+s^4/2)\|Y_n\|_2^2.
\]
Induction proves the all-\(n\) identity, including the equality boundary and the sharp mean-square threshold. No approximation or assumption about the distribution of the state direction is used.

**3. Fixed-order spectral radius.** The matrices \(F_s\) and \(G_s\) have the common determinant \(1\) and trace \(2-s^2\). Their characteristic polynomial is \(\lambda^2-(2-s^2)\lambda+1\). For \(0<s<2\), both eigenvalues lie on the unit circle; at \(s=2\), each has a nontrivial double eigenvalue \(-1\), and its Jordan power grows only polynomially. In all cases \(s\le2\), multiplication by \(q<1\) makes every fixed-order trajectory decay. If \(s>2\), the two real eigenvalues have magnitudes \(R(s)\) and \(R(s)^{-1}\), where \(R(s)>1\) has the stated formula. Consequently the damped spectral radius is \(qR(s)\); the claimed strict fixed-order stability criterion and boundary behavior follow immediately. Both orders share this entire spectral analysis.

**4. Unique and sharp crossover.** Set \(x=s^2\), and let \(c(x)=1+x^2/2\). The randomized and fixed thresholds compare \(c(x)\) and \(R(s)^2\), respectively. If \(0<s\le2\), then \(R(s)^2=1<c(x)\), so randomization requires strictly greater damping. For \(s>2\), use the reciprocal eigenvalue pair to obtain
\[
R(s)^2+R(s)^{-2}=x^2-4x+2,
\]
whence exact rational simplification yields
\[
\big(R(s)^2+R(s)^{-2}\big)-\big(c(x)+c(x)^{-1}\big)
=\frac{x\big(x^3-8x^2+4x-16\big)}{2(x^2+2)}.
\]
Because \(u+u^{-1}\) is strictly increasing for \(u>1\), the sign of \(R(s)^2-c(x)\) for \(x>4\) equals the sign of \(f(x)=x^3-8x^2+4x-16\). Now \(f(4)=-64\), \(f(8)=16\), \(f'(4)=-12\), and \(f''(x)=6x-16>0\) on \([4,\infty)\). Thus \(f'\) increases strictly from a negative value, making \(f\) first decrease and then strictly increase to infinity. It follows that \(f\) has exactly one root above \(4\), lying in \((4,8)\), and the sign switches exactly once. The stated ordering of damping thresholds follows on taking logarithms and dividing by \(4h\). Since both threshold intervals are strict and nonempty on their respective sides, choosing a damping coefficient strictly between them realizes both claimed reversals.

**5. Exact rational witnesses.** At \(s=1\), all undamped eigenvalues have modulus one; \(q=9/10\) makes either fixed matrix stable, while \(q^2(1+s^4/2)=(81/100)(3/2)=243/200>1\). At \(s=3\), \(R(3)=(7+3\sqrt5)/2\), so \(R(3)^2=(47+21\sqrt5)/2>44\); with \(q^2=1/44\) the fixed spectral radius exceeds one. Yet \(q^2(1+3^4/2)=83/88<1\). Both chosen \(q\) correspond to a strictly positive \(a\) at \(h=1\), and the true ODE remains exponentially decaying. This completes the proof.

## Verification

Run `python3 verify.py` with the Python standard library. The checker uses exact rational arithmetic for both split matrices, their determinants and traces, the fair-averaged Gram identity, and exhaustive enumeration of \(2^n\) order histories for \(0\le n\le8\) across multiple nonzero rational shears and initial vectors. It separately verifies both rational witnesses, checks the cubic's endpoint and derivative data, and numerically brackets the unique crossover and the sign reversal at additional parameter values. The numerical root is a reported approximation; **the proof of uniqueness and of all infinitely many parameter claims is analytic**, not based on the finite enumeration or floating-point bisection.

## Relationship to prior work

Agazzi, Mattingly and Melikechi (2022) investigate random splitting with random *subflow durations* and prove ergodicity and finite-time convergence in fluid models; their randomization mechanism and conclusions are not the iid fair order selection or exact mean-square stability boundary here. Childs, Ostrander and Su (2018) randomize product formula order in quantum simulation, where factors are unitary; unitarity precludes the present norm-amplification mechanism. Sturman and Thiffeault (2019; preprint 2017) derive bounds on generalized Lyapunov exponents for random products of individual shear matrices; their random word law is not one complete pair in a randomly reversed order per step. Eisenmann and Stillfjord (2022) study randomized *subsets* of split operators for evolutionary problems. Wei, Guenter and Spiteri (2025) specifically note that reversing an ordinary two-factor Lie–Trotter order leaves classical linear stability unchanged; here the new observation is that **randomly interleaving the two isospectral orders** can either destroy or restore second-moment stability. General spectral-radius and second-moment criteria for independent random matrix products give a framework but do not by themselves specify this explicit two-way crossover without the displayed algebra. The two-sided sharp comparison is the claim of this note, not the generic observation that switching can destabilize systems.

## Limitations

The result is for a specific two-dimensional damped skew-plus-nilpotent splitting, independent fair orders, and **mean-square** stability. It does not claim almost-sure instability in the first witness, almost-sure stability in the second, optimal randomized probabilities, extension to nonnormal systems in general, or any all-step finite-horizon accuracy advantage. Both subflow generators need not be individually Euclidean dissipative; only the full generator is. Exact stable continuous dynamics need not yield a stable large-step split scheme. An earlier specialized result on reversed shear-pair random products may still imply the formula; publication-priority novelty is subject to independent literature review.

## References

1. A. Agazzi, J. C. Mattingly and O. Melikechi, *Random Splitting of Fluid Models: Ergodicity and Convergence*, initial arXiv posting 2022-01-17, https://arxiv.org/abs/2201.06643.
2. M. Eisenmann and T. Stillfjord, *A randomized operator splitting scheme inspired by stochastic optimization methods*, initial arXiv posting 2022-10-11, https://arxiv.org/abs/2210.05375.
3. R. Sturman and J.-L. Thiffeault, *Lyapunov Exponents for the Random Product of Two Shears*, arXiv:1706.03398 (2017), *Journal of Nonlinear Science* 29 (2019), 593–620; https://link.springer.com/article/10.1007/s00332-018-9497-3.
4. A. M. Childs, A. Ostrander and Y. Su, *Faster quantum simulation by randomization*, arXiv:1805.08385 (2018), https://arxiv.org/abs/1805.08385.
5. S. Wei, V. Guenter and R. J. Spiteri, *Improving the stability and efficiency of high-order operator-splitting methods*, arXiv:2501.02310 (2025), https://arxiv.org/abs/2501.02310.
6. P. Monmarché and E. Strickler, *Asymptotic expansion of invariant measure for Markov-modulated ODEs at high frequency*, arXiv:2309.16464 (2023), https://arxiv.org/abs/2309.16464.
