# Exact stabilization phase diagram for scalar linearized ADMM
## Finding
Consider
\[
\min_{x,w\in\mathbb R} \frac{m}{2}x^2+\frac{m}{2}w^2
\quad\text{subject to}\quad w-x=0,
\qquad m>0.
\]
Use the linearized ADMM update in Ouyang--Chen--Lan--Pasiliao with penalty \(\rho=rm\) and proximal stabilization \(\eta=hm\), where \(r>0\) and \(h\ge0\). The boundary value \(h=0\) is included because the augmented quadratic still makes the scalar \(x\)-subproblem strongly convex.

Let \(\varrho(r,h)\) denote the spectral radius of the exact post-transient linear recurrence. With
\[
\phi=\frac{1+\sqrt 5}{2},
\]
the minimizers of \(\varrho(r,h)\) over \(h\ge0\) are
\[
h_*(r)=
\begin{cases}
\dfrac{-r^2+r+3-2\sqrt{2(1-r^2)}}{r},&0<r<1,\\[1.2ex]
[1/3,3],&r=1,\\[0.8ex]
\dfrac{1+r-r^2}{r+2},&1<r<\phi,\\[1.2ex]
0,&r\ge\phi.
\end{cases}
\]
For \(0<r<1\) the minimizer is unique and is a repeated-root critical-damping point. For \(1<r<\phi\) the minimizer is unique and makes the trace vanish, so the two real eigenvalues have equal magnitude and opposite signs. At \(r=1\) the entire interval \([1/3,3]\) is optimal with spectral radius \(1/2\). For \(r\ge\phi\), the unique optimum is the no-extra-stabilization boundary \(h=0\); at \(r=\phi\) this is also the trace-zero point.

The optimal radius is
\[
\varrho_*(r)=
\begin{cases}
\sqrt{\dfrac{h_*(r)-1}{(h_*(r)+r)(r+1)}},&0<r<1,\\[1.2ex]
\dfrac12,&r=1,\\[0.8ex]
\sqrt{\dfrac{r^2+1}{(r+1)(3r+1)}},&1<r<\phi,\\[1.2ex]
\dfrac{r^2-r-1+\sqrt{r^4-2r^3+3r^2+6r+1}}{2r(r+1)},&r\ge\phi.
\end{cases}
\]
By contrast, the universal L-ADMM choice \(\eta=L_G=m\), i.e. \(h=1\), has
\[
\varrho(r,1)=\frac{r^2+1}{(r+1)^2},
\]
and is asymptotically rate-optimal only when \(r=1\).

## Assumptions and scope
The claim concerns the exact scalar symmetric quadratic above and the L-ADMM update obtained from equation (1.12) of Ouyang et al., with the ordinary exact \(w\)-subproblem and multiplier update. It optimizes only the asymptotic spectral radius over a constant scalar stabilization \(\eta\) for a fixed penalty \(\rho\). It does not claim a finite-horizon optimum, a matrix-valued optimum, or a worst-case optimum over general convex problems.

The source paper's general AECCO convergence theorem uses \(\eta\ge L_G\) for L-ADMM. The branch \(h<1\) above is therefore an instance-specific extension beyond that sufficient majorization condition, justified here directly by the exact scalar recurrence. At a repeated eigenvalue the matrix can be defective, so the statement is about asymptotic spectral radius; a polynomial prefactor can occur in finite-time norms.

## Proof
For the source sign convention, the scalar updates are
\[
x_{k+1}=\frac{\rho w_k+(\eta-m)x_k-y_k}{\rho+\eta},\qquad
w_{k+1}=\frac{y_k+\rho x_{k+1}}{m+\rho},
\]
\[
y_{k+1}=y_k-\rho(w_{k+1}-x_{k+1}).
\]
The \(w\)-optimality equation gives \((m+\rho)w_{k+1}=y_k+\rho x_{k+1}\). Substituting this into the multiplier update yields the exact one-step identity
\[
y_{k+1}=m w_{k+1}.
\]
Hence, after one completed update, \(y_k=mw_k\) permanently. With \(r=\rho/m\) and \(h=\eta/m\), the state \((x_k,w_k)\) therefore obeys
\[
\begin{pmatrix}x_{k+1}\\w_{k+1}\end{pmatrix}
=M(r,h)
\begin{pmatrix}x_k\\w_k\end{pmatrix},
\]
where
\[
M(r,h)=
\begin{pmatrix}
\dfrac{h-1}{r+h}&\dfrac{r-1}{r+h}\\[1.2ex]
\dfrac{r(h-1)}{(1+r)(r+h)}&
\dfrac{r(r-1)}{(1+r)(r+h)}+\dfrac1{1+r}
\end{pmatrix}.
\]
Its characteristic polynomial is \(p(\lambda)=\lambda^2-T\lambda+D\), with
\[
T=\frac{hr+2h+r^2-r-1}{(h+r)(r+1)},\qquad
D=\frac{h-1}{(h+r)(r+1)}.
\]
The discriminant numerator is
\[
N_\Delta=h^2r^2+2hr^3-2hr^2-6hr+r^4-2r^3+3r^2+6r+1,
\]
and its discriminant as a quadratic in \(h\) is
\[
-32r^2(r-1)(r+1).
\]
Thus for \(0<r<1\) there are two real discriminant zeros
\[
h_\pm=\frac{-r^2+r+3\pm2\sqrt{2(1-r^2)}}{r},
\]
with \(h_->1\). For \(r>1\) the characteristic roots are distinct and real for every \(h\ge0\).

The monotonicity argument is elementary. Differentiate:
\[
T'=\frac{3r+1}{(h+r)^2(r+1)}>0,
\qquad
D'=\frac1{(h+r)^2}>0.
\]
Set
\[
c=\frac{D'}{T'}=\frac{r+1}{3r+1}.
\]
For any simple real root \(\lambda\), implicit differentiation of \(p(\lambda)=0\) gives
\[
\lambda'=\frac{T'(\lambda-c)}{2\lambda-T}.
\]
A direct substitution gives the \(h\)-independent identity
\[
p(c)=-\frac{2r^2(r-1)}{(r+1)(3r+1)^2}.
\]

If \(0<r<1\), then \(p(c)>0\). For \(h<1\), the roots have opposite signs and both root magnitudes decrease as \(h\) increases. From \(h=1\) to \(h=h_-\), both roots are nonnegative, \(c\) lies to the right of the larger root, and that larger root continues to decrease. On \((h_-,h_+)\) the roots are conjugate and their common modulus is \(\sqrt D\), which strictly increases because \(D'>0\). Beyond \(h_+\), continuity together with \(p(c)>0\) and the limit of the larger root toward \(1\) places \(c\) to its left, so the larger root increases. Hence the unique minimum is \(h_-\).

If \(r>1\), then \(p(c)<0\). Whenever the roots have opposite signs, the positive root increases with \(h\) while the magnitude of the negative root decreases. Since \(T\) is strictly increasing, the two magnitudes are equal exactly when \(T=0\), namely at
\[
h_0=\frac{1+r-r^2}{r+2}.
\]
This point belongs to \((0,1)\) exactly for \(1<r<\phi\), and is then the unique minimizer. For \(r\ge\phi\), \(T\ge0\) already at \(h=0\), so the positive root dominates and increases immediately; the unique minimizer is \(h=0\). For \(h\ge1\), both roots are nonnegative and \(p(c)<0\) places \(c\) between them, so the larger root continues to increase.

Finally, at \(r=1\) the characteristic polynomial factors with eigenvalues
\[
\frac12,
\qquad
\frac{h-1}{h+1}.
\]
Therefore the radius is \(1/2\) exactly for \(h\in[1/3,3]\), proving the remaining case and the complete phase diagram.

## Verification
The included `verify.py` independently reconstructs the recurrence from the scalar update, checks the trace and determinant identities in exact rational arithmetic at multiple rational parameter pairs, checks the special factorization at \(r=1\), evaluates the closed-form minimizers, and compares them against deterministic dense scans and two-sided perturbations. Running

`python3 verify.py`

prints `VERIFY_OK`.

The finite scan is only a regression check. The minimization itself is proved by the sign analysis above, not by enumeration.

## Relationship to prior work
Ouyang, Chen, Lan, and Pasiliao define L-ADMM in equation (1.12), explicitly note prior work on tuning its parameter \(\eta_t\), and give general convergence choices including \(\eta\ge L_G\) for the unaccelerated method. Their paper does not give the scalar spectral-radius phase diagram above. Their primary MSC listing begins with 90C25.

Chen, Hager, Yashtini, Ye, and Zhang develop BOSVS, a variable-stepsize Bregman/operator-splitting method closely related to linearized ADMM. Its full text uses a Barzilai--Borwein curvature estimate followed by line search; it does not state the constant-parameter scalar spectral minimizer above.

Ghadimi, Teixeira, Shames, and Johansson derive optimal parameters for ordinary and over-relaxed ADMM on quadratic problems. Their full-text recurrence and optimized parameters concern the ADMM penalty and relaxation parameter, not the additional L-ADMM stabilization \(\eta\). The present claim is therefore not a special case of their stated parameter rule.

The exact scalar result is useful as a modal benchmark: it isolates three qualitatively different mechanisms for the best stabilization--critical damping, equal-magnitude sign alternation, and a zero-stabilization boundary--and shows exactly when the general majorization value \(\eta=L_G\) is conservative for this quadratic mode.

## Limitations
This is a one-dimensional symmetric quadratic calculation. It does not prove that the same \(h_*(r)\) is optimal for nonsymmetric block curvatures, multiple spectral modes, nonquadratic objectives, or adaptive/accelerated variants. A matrix problem generally requires balancing several modes at once.

The originality comparison cannot exclude an unindexed thesis, implementation note, or later preconditioned-ADMM analysis that contains an equivalent scalar reduction. Two application papers cited by Ouyang et al. as stepsize-tuning precedents were identified bibliographically but were not available here as fully inspected primary text; this remains a residual literature risk rather than evidence of coverage.

## References
1. Y. Ouyang, Y. Chen, G. Lan, and E. Pasiliao Jr., *An Accelerated Linearized Alternating Direction Method of Multipliers*, arXiv:1401.6607; SIAM Journal on Imaging Sciences 8 (2015), 644--681, DOI 10.1137/14095697X.
2. Y. Chen, W. W. Hager, M. Yashtini, X. Ye, and H. Zhang, *Bregman operator splitting with variable stepsize for total variation image reconstruction*, Computational Optimization and Applications 54 (2013), 317--342, DOI 10.1007/s10589-012-9519-2.
3. E. Ghadimi, A. Teixeira, I. Shames, and M. Johansson, *Optimal parameter selection for the alternating direction method of multipliers (ADMM): quadratic problems*, arXiv:1306.2454; IEEE Transactions on Automatic Control 60 (2015), 644--658, DOI 10.1109/TAC.2014.2354892.
