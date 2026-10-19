# Sharp reshuffling reversal threshold for two-component stochastic extragradient

## Finding

The comparison of random reshuffling (RR, sampling without replacement) against independently sampled indices (WR, sampling with replacement) is not uniformly favorable to RR, even on a two-component strongly convex quadratic where each individual stochastic extragradient (SEG) step is a nonexpansion. For a symmetric family of two rank-one gradient components, we determine the **exact worst-initial-vector, two-step expected squared-error comparison**, the unique threshold at which its direction reverses, and an explicit rational witness on an objective of condition number two.

Let \(0<t<1\), \(0<k<2\), \(a=\sqrt{(1+t)/2}\), and \(b=\sqrt{(1-t)/2}\). Set \(u=(a,b)^\mathsf T\), \(v=(a,-b)^\mathsf T\), and \(F_1(z)=uu^\mathsf Tz\), \(F_2(z)=vv^\mathsf Tz\). Use same-sample SEG with extrapolation step \(\gamma_2=1/2\) and update step \(\gamma_1=2k\). A selected component then gives exactly
\[
 z^+=z-\gamma_1F_i(z-\gamma_2F_i(z))=(I-kP_i)z,\qquad P_1=uu^\mathsf T,\quad P_2=vv^\mathsf T.
\]
After **two** component updates, let \(\mathcal R\) be the expectation of the squared-error matrix over either uniform ordering \((1,2)\) or \((2,1)\), and let \(\mathcal W\) be the expectation for two independent uniform component indices. Define \(R=\lambda_{\max}(\mathcal R)\), \(W=\lambda_{\max}(\mathcal W)\), the sharp worst-start expected squared-norm factors. With
\[
 A=1-\frac{k(1+t)}2,\quad D=1-\frac{k(1-t)}2,\quad h^2=\frac{k^2(1-t^2)}4,
\quad p=A^2-h^2,\quad r=D^2-h^2,\quad q^2=h^2(D-A)^2,
\]
the matrices are diagonal in the displayed coordinate system with entries
\[
 R_+=p^2+q^2,\quad R_-=r^2+q^2,\qquad
 W_\pm=\frac{R_\pm+1-[1-(1-k)^4](1\pm t)/2}{2}.
\]
In particular, \(W=W_-\), \(R=\max\{R_+,R_-\}\), and, for the polynomial
\[
 P(k,t)=3k^2t^3+k^2t^2+k^2t-k^2-2kt^2-8kt+2k+8t,
\]
**the exact sampling-order comparison is**
\[
 \boxed{R>W\ \Longleftrightarrow\ P(k,t)<0},\qquad
 \boxed{R=W\ \Longleftrightarrow\ P(k,t)=0}.
\]
For \(P(k,t)>0\), RR instead has strictly smaller worst-case expected squared error than WR. In all cases \(0<R,W<1\).

There is a unique **global critical effective step** \(k_*\in(3/2,2)\) such that RR is never worse at any angle for \(0<k\le k_*\), whereas for every \(k_*<k<2\), a nonempty open interval of angles makes RR strictly worse. The threshold is the unique root in \((3/2,2)\) of
\[
 19k^6-116k^5+356k^4-848k^3+1344k^2-1104k+368=0,
\]
namely \(k_*=1.64548714630887\ldots\). Equality at the threshold occurs at the unique positive minimizer \(t_*=0.34232387947618\ldots\) of \(P(k_*,t)\); below the threshold equality does not occur at any interior angle.

An entirely rational strict witness is \(k=5/3\), \(t=1/3\), for which
\[
 R_+=\frac{1217}{2187},\quad R_-=\frac{802}{2187},\qquad
 W_+=\frac{1117}{2187},\quad W_-=\frac{1202}{2187},
\]
so \(R-W=5/729>0\), while both methods still contract in mean square. The averaged objective \(f(z)=\tfrac14[(u^\mathsf Tz)^2+(v^\mathsf Tz)^2]\) has Hessian \(\tfrac12(P_1+P_2)=\operatorname{diag}((1+t)/2,(1-t)/2)\) and condition number exactly \(2\) in this witness.

## Assumptions and scope

The domain is \(\mathbb R^2\). Both rank-one component operators are monotone and one-Lipschitz, and their average is strongly monotone with constant \((1-t)/2\). The two sampling schemes each use two component updates (and equal numbers of operator calls). Each SEG update uses **the same sampled component in both substeps** and employs the same positive deterministic step pair. RR selects uniformly from the two permutations; WR selects both indices independently. Expectations concern squared Euclidean error from the common solution zero, and the supremum over deterministic, nonzero initial errors is taken **outside** expectation. All claims concern exact arithmetic. \(t=0\) and \(t=1\), and \(k=0\) and \(k=2\), are excluded from the strict-threshold statements.

## Proof

**1. Reduction to a pair of noncommuting symmetric contractions.** Because \(P_i^2=P_i\), the SEG composition is exactly \(B_i=I-kP_i\). Its eigenvalues are \(1\) and \(1-k\), so \(\|B_i\|_2=1\) throughout \(0<k<2\). In the bisector basis,
\[
 B_1=\begin{pmatrix}A&-g\\-g&D\end{pmatrix},\qquad
 B_2=\begin{pmatrix}A&g\\g&D\end{pmatrix},\qquad g=kab>0.
\]
Thus \(B_2B_1=\begin{psmallmatrix}p&q\\-q&r\end{psmallmatrix}\) and \(B_1B_2=\begin{psmallmatrix}p&-q\\q&r\end{psmallmatrix}\), where \(q=g(D-A)\). Averaging their squared matrices \((B_jB_i)^\mathsf T(B_jB_i)\) cancels off-diagonal terms and yields \(\mathcal R=\operatorname{diag}(p^2+q^2,r^2+q^2)\).

**2. Independent sampling and the sign reduction.** Each repeated-index word contributes \(B_i^4=I-[1-(1-k)^4]P_i\). Since the four words have probability \(1/4\), \(\mathcal W=\frac12\mathcal R+\frac14(B_1^4+B_2^4)\), proving the displayed expressions. Direct polynomial expansion yields the three exact identities
\[
 W_+-W_-=\frac{kt(k-2)}2[k^2t^2+(k-2)^2]<0,
\]
\[
 R_--W_-=-\frac{k^2(2-k)(1-t^2)(2-k+kt)}4<0,
\]
\[
 R_+-W_-=-\frac{k(2-k)}4P(k,t).
\]
As \(W=W_-\) and \(R_-<W_-\), comparison of the two *maximal eigenvalues* reduces exactly to the sign of \(P\). Strict contraction follows without relying on the formulas: every RR word uses both distinct nonparallel projectors and strictly diminishes every nonzero vector's norm at some step; for WR, the all-first-index and all-second-index words each have positive probability, and no nonzero vector lies in both fixed spaces. Compactness of the unit circle makes the maximum expected squared factor strictly below one.

**3. Existence and uniqueness of the global step frontier.** Put
\[
 C(t)=3t^3-t^2+t+1>0,\qquad E(t)=3t^3+t^2+t-1.
\]
For \(k=1+h\), direct collection gives
\[
 P(1+h,t)=C(t)-6t(1-t^2)h+E(t)h^2.
\]
For \(0<k\le1\), substitute \(h=k-1\in(-1,0]\): since \(C(t)>1\) for \(0<t<1\) and \(E(t)\ge-1\), one gets \(P>1-h^2>0\). For \(t\ge1/\sqrt3\) and \(0< h<1\), rewrite
\[
 P(1+h,t)=(1-h)[C(t)-E(t)h]+4ht(3t^2-1)>0.
\]
Here \(C(t)-E(t)=2(1-t^2)>0\), so the first bracket is strictly positive.

In the remaining interval \(0<t<1/\sqrt3\), the derivative
\[
 \partial_hP(1+h,t)=-6t(1-t^2)+2E(t)h
\]
is strictly negative for \(0\le h\le1\). This is immediate if \(E\le0\), while if \(E>0\), the stronger inequality \(E<3t(1-t^2)\) follows from \(6t^3+t^2-2t-1<0\), using \(t^2<1/3\). Now \(P(1,t)=C(t)>0\), but \(P(2,t)=4t(3t^2-1)<0\). Each such \(t\) consequently has one unique zero in \(k\in(1,2)\), and these zeroes approach \(k=2\) at either angular endpoint. Furthermore,
\[
 P(3/2,t)=\frac{27t^3-3t^2-7t+3}{4}\ge\frac13,
\]
with equality at \(t=1/3\); and \(P(2,1/3)=-8/9<0\). The continuous minimum of \(P(k,t)\) over \(0\le t\le1/\sqrt3\) decreases strictly through zero exactly once as \(k\) grows from \(3/2\) to \(2\). Thus \(k_*\) exists and is unique. At every \(3/2\le k<2\), \(\partial_tP\) is an upward-opening quadratic with negative constant term, hence exactly one positive critical point. At the first zero this critical point is the unique tangency point \(t_*\).

**4. Algebraic identification of the frontier.** Eliminating \(t\) from \(P(k,t)=0\) and \(\partial_tP(k,t)=0\) gives the exact resultant
\[
 \operatorname{Res}_t(P,\partial_tP)=48k^4 Q(k),
\quad Q(k)=19k^6-116k^5+356k^4-848k^3+1344k^2-1104k+368.
\]
The rational Sturm sequence of \(Q\) has sign patterns \((+,-,-,+,+,-,+)\) at \(k=3/2\) and \((-,-,+,-,-,-,+)\) at \(k=2\), giving respectively four and three sign changes, hence exactly one root in that interval. The existence/uniqueness argument already proves which root is relevant; the Sturm computation makes its stated algebraic characterization unconditional. Solving the resultant root and the positive critical-point equation gives the displayed approximations, which are not used as proof.

**5. Rational witness.** Substituting \(k=5/3\) and \(t=1/3\) into the exact diagonal formulas gives \(P=-4/81\), \(R_+=1217/2187\), \(R_-=802/2187\), \(W_+=1117/2187\) and \(W_-=1202/2187\). Their maxima differ by \(15/2187=5/729\), proving the announced reversal on a strongly convex problem of condition number two.

## Verification

The standalone script `verify.py` (Python 3 plus SymPy 1.14) symbolically checks all three factorized diagonal-comparison identities, the elimination resultant, the rational Sturm sign patterns and the rational witness. It also checks the four sampling-word matrices against the derived scalar formulas for 1,000 independently generated nondegenerate parameters and tests the sign law on a 19,701-point parameter grid. Its reproducible recorded run reports 28,701 checks. These finite tests independently stress the computations; the inequalities over the full parameter domain and the unique threshold are proved above, not inferred from a grid. Run `python verify.py` from a directory containing the script.

## Relationship to prior work

Emmanouilidis, Vidal and Loizou (2024) give the same-sample and reshuffled SEG definitions, establish convergence for strongly monotone variational inequalities under explicit small-step restrictions, and motivate the RR-versus-WR comparison. Their rate bounds do not imply a sharp all-angle comparison of the **one-epoch worst-start expected squared Euclidean error** for the larger step family studied here. Yun, Sra and Jadbabaie (2021), especially Appendix B, analyze noncommutative arithmetic-geometric-mean comparisons of without-replacement and with-replacement matrix products under **positive-semidefinite factor** assumptions. For \(k>1\), the present step factors have one strictly negative eigenvalue even though they are nonexpansive, so those PSD product comparisons do not apply. Work on shuffled SGD, including Gürbüzbalaban–Ozdaglar–Parrilo (2015/2021), Safran–Shamir (2021), and Liu (2026), establishes regimes of faster RR convergence or other performance bounds; such statements do not provide the exact finite-horizon, sharp Euclidean worst-start phase computed here, and their stepsize assumptions and performance criteria differ.

The rank-one components satisfy \(F_i^2=F_i\), making same-sample SEG algebraically identical here to **overrelaxed component gradient descent** with effective step \(k\). This is a shared interpretation, not a claim of a uniquely extragradient phenomenon. The novel claimed contribution is the precise phase boundary and finite-horizon comparison for this natural common setting, not the classical scalar algebra of orthogonal projectors.

## Limitations

The result concerns only two rank-one components in two real dimensions, symmetric equal-strength directions, positive fixed SEG parameters with effective \(0<k<2\), a single two-step epoch, and Euclidean worst-start mean-square error. It neither claims RR is asymptotically inferior after many epochs nor contradicts small-step acceleration theorems, and it does not cover general nonnormal operators, observation noise, unequal sampling weights, momentum, or different second-step samples. The exact universal threshold within this family is not a universal threshold across all finite sums. A historically equivalent theorem under the language of two noncommuting overrelaxed projections or two-sample SGD remains a priority risk despite the source comparisons.

## References

1. K. Emmanouilidis, R. Vidal, N. Loizou, *Stochastic Extragradient with Random Reshuffling: Improved Convergence for Variational Inequalities* (first submitted 11 March 2024), arXiv:2403.07148, https://arxiv.org/abs/2403.07148 .
2. C. Yun, S. Sra, A. Jadbabaie, *Can Single-Shuffle SGD be Better than Reshuffling SGD and GD?* (2021), arXiv:2103.07079, https://arxiv.org/abs/2103.07079 .
3. M. Gürbüzbalaban, A. Ozdaglar, P. A. Parrilo, *Why Random Reshuffling Beats Stochastic Gradient Descent* (preprint 2015; journal 2021), arXiv:1510.08560, https://arxiv.org/abs/1510.08560 .
4. I. Safran, O. Shamir, *Random Shuffling Beats SGD Only After Many Epochs on Ill-Conditioned Problems* (2021), arXiv:2106.06880, https://arxiv.org/abs/2106.06880 .
5. Z. Liu, *Random Reshuffling Dominates Stochastic Gradient Descent* (2026), arXiv:2606.32005, https://arxiv.org/abs/2606.32005 .
