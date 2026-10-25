# A unique sketch-angle threshold for condition-number reversal in three-state Nyström preconditioning

## Finding
Consider the rank-two Nyström preconditioner of Frangella, Tropp, and Udell for the regularized linear system \((A+\mu I)x=b\), formed from a full-column-rank sketch \(\Omega\):
\[
H=A\Omega(\Omega^{\mathsf T}A\Omega)^{-1}\Omega^{\mathsf T}A
 =U\operatorname{diag}(\lambda_1,\lambda_2)U^{\mathsf T},\qquad
P=\frac{U\operatorname{diag}(\lambda_1+\mu,\lambda_2+\mu)U^{\mathsf T}}{\lambda_2+\mu}+I-UU^{\mathsf T}.
\]
For every \(k>1\) and \(m>0\), take \(A=\operatorname{diag}(k,1,1)\) and \(\mu=m\). For an arbitrary rank-two sketch, the positive eigenvalues of \(H\) are \(\lambda\) and \(1\), with \(1\le\lambda\le k\). If \(1<\lambda<k\), set
\[
t=\frac{\lambda-1}{k-\lambda},\quad
\begin{aligned}
a_0&=(m+1)(k+2m+1),\\
a_1&=k^2+3km+k+3m^2+3m+1,\\
a_2&=k(k-1)(k+2m)(m+1),\\
a_3&=k^2(k+m)(m+1).
\end{aligned}
\]
There is exactly one positive root \(t_*\) of
\[
a_3t^3+a_2t^2-a_1t-a_0=0.
\]
Let \(\kappa_0=(k+m)/(1+m)\) and let \(\kappa_{\rm Nys}\) be the spectral condition number of \(P^{-1/2}(A+mI)P^{-1/2}\). The **exact comparison** is
\[
\boxed{\ \kappa_{\rm Nys}>\kappa_0\ \Longleftrightarrow\ 0<t<t_*,\qquad
\kappa_{\rm Nys}=\kappa_0\ \Longleftrightarrow\ t=t_*,\qquad
\kappa_{\rm Nys}<\kappa_0\ \Longleftrightarrow\ t>t_* .\ }
\]
At the endpoint \(\lambda=1\), the preconditioner is the identity and the condition numbers agree. At \(\lambda=k\), it is ideal and \(\kappa_{\rm Nys}=1\). Thus every nontrivial spike \(k>1\), at every positive regularization \(m\), has **a nonempty open set of Gaussian sketches with worse condition number than no preconditioning** and another nonempty open set with improvement. Dimension three is the smallest in which this can occur for the stated Nyström construction.

For example, let
\[
A=\operatorname{diag}(4,1,1),\quad m=1,\quad
\Omega=\begin{pmatrix}1&0\\4&0\\0&1\end{pmatrix}.
\]
The preconditioner is
\[
P=\begin{pmatrix}23/20&3/20&0\\3/20&23/20&0\\0&0&1\end{pmatrix},
\]
and its generalized eigenvalues relative to \(A+I\) are
\[
2,\quad \frac{161-3\sqrt{569}}{52},\quad \frac{161+3\sqrt{569}}{52}.
\]
Consequently,
\[
\boxed{\kappa_{\rm Nys}=\frac{161+3\sqrt{569}}{161-3\sqrt{569}}>\frac52=\kappa_0.}
\]
The strict inequality persists in an open neighborhood of this sketch, hence has positive probability under a full-support Gaussian sketch. Within the same three-state family, there are positive regularizations and sketches for which \(\kappa_{\rm Nys}/\kappa_0\to32/27\); this last number is an *attained asymptotic deterioration factor in this family*, not a claimed global bound.

## Assumptions and scope
All matrices are real, all computations in the theorem use exact arithmetic, and the two sketch columns are linearly independent. The regularization \(m\) is strictly positive. Gaussian sketches have independent standard normal entries; all such sketches have rank two almost surely. The comparison is of the **spectral condition numbers**, not of the actual conjugate-gradient iteration count for a fixed right-hand side. For a general sketch, the spike eigenspace has dimension one and the lower eigenspace has dimension two. Rotation inside the lower eigenspace changes neither the matrix nor the comparison.

## Proof
**1. Exact parametrization of every sketch.** Let \(\Pi\) be the orthogonal projector onto \(A^{1/2}\operatorname{ran}\Omega\). Since \(H=A^{1/2}\Pi A^{1/2}\) and \(\Pi\) has rank two, write \(I-\Pi=ww^{\mathsf T}\) for a unit vector \(w\). A rotation in the two-dimensional eigenspace of \(A\) with eigenvalue one puts \(w=(c,s,0)^{\mathsf T}\) with \(c^2+s^2=1\). Therefore
\[
H=A-A^{1/2}ww^{\mathsf T}A^{1/2}.
\]
Its third coordinate is an eigenvector with eigenvalue one. The leading \(2\times2\) block has rank one and trace
\[
\lambda=1+(k-1)s^2.
\]
For \(1<\lambda<k\), its positive eigenvector \(u\), chosen in the first two coordinates, satisfies
\[
u_1^2=\frac{k(\lambda-1)}{(k-1)\lambda},\qquad
u_2^2=\frac{k-\lambda}{(k-1)\lambda}.
\]
Every \(\lambda\in(1,k)\) is obtained by choosing \(s^2=(\lambda-1)/(k-1)\) and then any full-rank \(\Omega\) spanning \(A^{-1/2}w^\perp\). Formula (17) of the initiating paper reduces exactly to
\[
P=I+\frac{\lambda-1}{1+m}uu^{\mathsf T}.
\]

**2. The generalized eigenvalues.** Put \(\alpha=k+m\), \(\beta=1+m\). The direction orthogonal to \(u\) in the repeated unit-eigenspace gives the unchanged generalized eigenvalue \(\beta\). The two others \(z_-<z_+\) are the eigenvalues of the symmetric definite pencil \((\operatorname{diag}(\alpha,\beta), I_2+(\lambda-1)uu^{\mathsf T}/\beta)\). Applying the Sherman–Morrison identity and the determinant lemma gives
\[
\begin{split}
T=z_-+z_+&=\alpha+\beta-\frac{\lambda-1}{\lambda+m}
\left(\beta+\frac{k(\lambda-1)}{\lambda}\right),\\
D=z_-z_+&=\frac{\alpha\beta^2}{\lambda+m},\\
z_{\pm}&=\frac{T\pm\sqrt{T^2-4D}}2.
\end{split}
\]
Both \(u_1\) and \(u_2\) are nonzero; testing the two coordinate Rayleigh quotients gives \(z_-<\beta<z_+\). Hence \(\kappa_{\rm Nys}=z_+/z_-\), while \(\kappa_0=\alpha/\beta>1\).

**3. Exact comparison polynomial.** For a pair of positive roots with ratio \(r\ge1\), one has \(T^2/D=r+2+r^{-1}\), which is strictly increasing in \(r>1\). Thus the sign of \(\kappa_{\rm Nys}-\kappa_0\) is the sign of
\[
\frac{T^2}{D}-\frac{(\kappa_0+1)^2}{\kappa_0}
=-\frac{(\lambda-1)G(\lambda)}{\lambda^2(\lambda+m)(k+m)(m+1)^2},
\]
where the exact cubic numerator is
\[
\begin{split}
G(\lambda)={}&-m^2\lambda^3+
\big((k+1)^2+(k^2+2k+3)m+(2k+3)m^2\big)\lambda^2\\
&-k\big(3k+2+(2k+4)m+4m^2\big)\lambda+k^2.
\end{split}
\]
The substitution \(\lambda=(1+kt)/(1+t)\) yields the polynomial identity
\[
\frac{(1+t)^3}{k-1}G\!\left(\frac{1+kt}{1+t}\right)
=a_3t^3+a_2t^2-a_1t-a_0.
\]
All four coefficients \(a_i\) are strictly positive for \(k>1,m>0\). The cubic on the right is negative at zero, tends to positive infinity, and has strictly positive second derivative on the nonnegative half-line. Its first derivative starts negative and increases strictly, so the cubic decreases to one minimum and then increases through zero exactly once. Its sign is negative below that zero and positive above. The preceding comparison identity proves all three strict/equality cases. In particular, as \(\lambda\downarrow1\), the condition number is strictly *worse* for \(1<\lambda<\lambda_*\), where \(\lambda_*=(1+kt_*)/(1+t_*)\).

**4. Exact witness and probabilistic interpretation.** Direct multiplication of the displayed \(A\) and \(\Omega\) gives
\[
H=\begin{pmatrix}4/5&4/5&0\\4/5&4/5&0\\0&0&1\end{pmatrix},
\qquad (\lambda,1)=(8/5,1).
\]
The nontrivial generalized characteristic polynomial is \(26z^2-161z+200\). For this pencil,
\[
\frac{T^2}{D}-\frac{(\kappa_0+1)^2}{\kappa_0}=\frac{441}{5200}>0.
\]
Thus its condition number is strictly greater than \(5/2\), with no reliance on floating-point approximations. Continuity of the positive generalized eigenvalues with respect to full-rank \(\Omega\) gives an open neighborhood of worsening; Gaussian full support assigns it positive probability. A sketch with \(\lambda\) near \(k\) gives an open region of improvement.

**5. Minimal dimension and quantitative stiff-spike limit.** In dimension one there is no conditioning issue. In dimension two, a rank-one Nyström preconditioner is exactly \(I\), while a full-rank Nyström approximation is exactly \(A\) and yields condition number one. Hence three dimensions are minimal. Finally, choose \(\lambda=3/2\), \(m=1/k\), and take \(k\to\infty\). The formulas in step 2 give
\[
\frac{T}{k}\to\frac89,\qquad \frac{D}{k}\to\frac23,
\qquad\frac{\kappa_0}{k}\to1.
\]
Since \(z_+\sim T\) and \(z_-\sim D/T\), the relative condition-number inflation tends to
\[
\frac{\kappa_{\rm Nys}}{\kappa_0}
\longrightarrow\frac{(8/9)^2}{2/3}=\frac{32}{27}.
\]
This limit is achievable by full-rank sketches because \(3/2\in(1,k)\) for every \(k>3/2\).

## Verification
A standalone Python checker named `verify.py` uses SymPy to verify both polynomial identities, the endpoint identities, the exact rational witness, and the limiting factor. It independently reconstructs \(500\) Gaussian Nyström sketches and their generalized eigenvalues using NumPy/SciPy, checking against the derived formulas. The checker completed \(2008\) assertions successfully. Run `python verify.py` with Python 3 and NumPy, SciPy, and SymPy installed. Numerical trials illustrate algebraic statements but are not substituted for the universal proof.

## Relationship to prior work
Frangella–Tropp–Udell introduce precisely the normalized Nyström preconditioner studied here and prove an expected-condition-number bound at sufficiently large sketch rank, as well as an ideal spectral preconditioner using exact leading eigenspaces. Their statements do not provide a per-sketch guarantee of improvement over the unpreconditioned matrix, nor a complete condition-number comparison for the three-state spiked model. Daužickaitė–Lawless–Scott report that randomized spectral limited-memory preconditioners can displace small eigenvalues below one, but study a different preconditioner and do not imply this Nyström normalization's unique sketch-angle criterion. Dereziński–Musco–Yang analyze a distinct multilevel sketched preconditioner and average spectral complexity rather than this exact small-sketch comparison. The theorem here concerns specifically the normalized rank-two construction, not all Nyström-based preconditioners.

## Limitations
The result is an exact low-dimensional spectral-condition-number classification, not an iteration-count or runtime comparison, and does not assert that conditioning worsens with high probability. It does not make an overarching worst-case bound of \(32/27\) in arbitrary dimensions. The source work's large-rank expected condition-number guarantee is fully compatible with the positive-probability deterioration at rank two. Equivalent small-dimensional conditions may exist in specialized preconditioning literature; publication priority remains subject to independent assessment. Finite-precision stabilization shifts used in practical software are not analyzed.

## References
1. Z. Frangella, J. A. Tropp, and M. Udell, *Randomized Nyström Preconditioning*, arXiv:2110.02820v1 (first publicly submitted 2021-10-06); SIAM Journal on Matrix Analysis and Applications 44 (2023), 718–752, doi:10.1137/21M1466244. https://arxiv.org/abs/2110.02820 .
2. I. Daužickaitė, A. S. Lawless, and J. A. Scott, *Randomised preconditioning for the forcing formulation of weak-constraint 4D-Var*, Quarterly Journal of the Royal Meteorological Society 147 (2021), 3719–3734, doi:10.1002/qj.4151. https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.4151 .
3. M. Dereziński, C. Musco, and J. Yang, *Faster Linear Systems and Matrix Norm Approximation via Multi-level Sketched Preconditioning*, arXiv:2405.05865v1 (2024-05-09). https://arxiv.org/abs/2405.05865 .
