# Sharp stability-budget and transient-order transitions for two-periodic delayed gradient descent

## Finding

For deterministic one-iteration-stale gradient descent on a scalar strongly convex quadratic, positive learning rates alternating between two values admit a complete stability and rate-optimality phase diagram at a fixed two-update learning-rate sum. Alternation increases the maximal stable dimensionless sum from the constant-rate value \(2\) to the sharp supremum \(3\). When the sum exceeds \(1/2\), the fastest asymptotic allocation is critically damped and is generally unequal; its two possible orders have identical Floquet eigenvalues but unequal **exact Euclidean transient norms** at every positive two-step horizon, with the smaller rate first always better.

Let \(s>0\). The exact infimum of the two-step spectral radius over all strictly positive rate pairs with normalized sum \(s\) is
\[
\rho_*(s)=\begin{cases}
\dfrac{1-s+\sqrt{1-2s}}2,&0<s\le1/2,\\[2mm]
\dfrac{|1-s|}{2},&s\ge1/2.
\end{cases}
\]
For \(0<s\le1/2\) the only minimizing allocation is the equal pair. For \(s>1/2\), \(s\ne1\), the minimizing allocations, up to swapping, are
\[
(a_-,a_+)=\left(\frac{s-\sqrt{2s-1}}2,\frac{s+\sqrt{2s-1}}2\right).
\]
At \(s=1\), the infimum is zero but is not attained by any strictly positive pair.

## Assumptions and scope

Fix \(\lambda>0\), \(f(x)=\lambda x^2/2\), arbitrary real initial state \((x_0,x_{-1})\), and strictly positive learning rates \(\eta_0,\eta_1\), repeated periodically in the deterministic iteration
\[
x_{k+1}=x_k-\eta_{k\bmod2}\,f'(x_{k-1}).
\]
Set \(a=\lambda\eta_0\), \(b=\lambda\eta_1\), \(s=a+b\), and \(p=ab\). The two-update state map acts on \(u_k=(x_k,x_{k-1})^\mathsf T\). Strict stability means convergence of \(u_k\) to zero for **every** initial state, not merely a particular initialization. Rate optimization concerns the spectral radius per two updates, under the exact constraint \(a+b=s\); it does not optimize finite-horizon objective error or arbitrary history-dependent schedules.

## Proof

**Transfer and strict stability.** One step with normalized rate \(c>0\) maps the state by
\[
M(c)=\begin{pmatrix}1&-c\\1&0\end{pmatrix}.
\]
One period has matrix
\[
P=M(b)M(a)=\begin{pmatrix}1-b&-a\\1&-a\end{pmatrix},\qquad
\operatorname{tr}P=1-s,\quad\det P=p.
\]
Its characteristic polynomial is \(q(t)=t^2-(1-s)t+p\). The elementary second-degree Schur (Jury) conditions are \(1-p>0\), \(1-(1-s)+p>0\), and \(1+(1-s)+p>0\). Because \(a,b>0\), the middle condition \(s+p>0\) is automatic. Consequently, **for every pair of positive rates**, strict stability is equivalent to
\[
\boxed{\quad ab<1\quad\text{and}\quad a+b<2+ab.\quad}
\]
This is an exact if-and-only-if statement, including the exclusion of all boundary equalities.

**Optimal sum and spectral rate.** At fixed \(s\), positivity is equivalent to \(0<p\le s^2/4\), where equality occurs only when \(a=b\). Write \(T=|1-s|\). The two roots of \(q\) have maximal modulus
\[
R_s(p)=\begin{cases}
\dfrac{T+\sqrt{T^2-4p}}2,&0<p\le T^2/4,\\[2mm]
\sqrt p,&p\ge T^2/4.
\end{cases}
\]
The first branch strictly decreases with \(p\) (away from its endpoint), while the second strictly increases. For \(s<1/2\), \(T^2/4>s^2/4\), so the unique optimum is \(p=s^2/4\), the equal allocation. For \(s\ge1/2\), \(p_*=T^2/4\) is feasible unless \(s=1\), where it equals the excluded endpoint \(p=0\). For \(s>1/2\), \(s\ne1\), the quadratic equation \(t^2-st+p_*=0\) gives precisely the two orderings stated above, with two-step eigenvalue \(r=(1-s)/2\) repeated. When \(s=1\), \(R_1(p)=\sqrt p\) can approach but never reach zero. This proves the entire rate diagram.

There exists a strictly stable strictly positive allocation at a prescribed \(s\) **if and only if** \(0<s<3\), since its best attainable (or approachable) spectral radius is below one exactly there. Equivalently, if \(s\ge3\), \(p<1\) and \(s<2+p\) cannot both hold. By contrast, constant rates satisfy \(a=b=s/2\) and are strictly stable exactly for \(0<s<2\). Hence the alternating stability-budget supremum \(3\) is sharp and is exactly \(3/2\) times the constant-rate supremum \(2\).

**Exact transient-order law.** Fix \(s>1/2\), \(s\ne1\), and choose either spectral-rate-minimizing order. Put \(r=(1-s)/2\) and \(N=P-rI\). Because the characteristic polynomial is \((t-r)^2\), the Cayley–Hamilton theorem gives \(N^2=0\), while \(N\ne0\). Directly,
\[
N=\begin{pmatrix}d&-a\\1&-d\end{pmatrix},\qquad d=\frac{1+a-b}{2},\qquad d^2=a,
\]
so \(\|N\|_F=1+a\). Therefore, for every integer \(m\ge1\),
\[
P^m=r^m\left(I+\frac m r N\right).
\]
For any real \(2\times2\) traceless nilpotent \(N\), \(\det(I+tN)=1\), while \(\|I+tN\|_F^2=2+t^2\|N\|_F^2\). Its singular values are reciprocal, giving the exact norm formula
\[
\boxed{\quad
\|P^m\|_2=\frac{|r|^m}{2}
\left(\sqrt{4+\left(\frac{m(1+a)}{|r|}\right)^2}
+\frac{m(1+a)}{|r|}\right).\quad}
\]
Here \(a\) is the **first** normalized rate in each period. The right-hand side strictly increases with \(a\) for fixed \(s\) and \(m\). Thus the order \((a_-,a_+)\) uniquely minimizes \(\|P^m\|_2\) among the two spectrally optimal orders, simultaneously for every \(m\ge1\). The two orders have exactly the same eigenvalues but quantitatively different finite-horizon worst-case amplification.

**Exact witness.** At the sum \(s=5/2\), the optimal ordered pair is \((a,b)=(1/4,9/4)\). Its period has repeated eigenvalue \(-3/4\), hence it is strictly stable, while the equal-rate pair \((5/4,5/4)\) has determinant \(25/16>1\) and is unstable. Swapping the optimal rates preserves the eigenvalues but increases \(\|N\|_F\) from \(5/4\) to \(13/4\), strictly worsening every finite-horizon two-period operator norm.

## Verification

The accompanying Python program `verify.py` independently constructs the transfer matrix and characteristic polynomial in exact symbolic arithmetic, tests the Schur conditions on a parameter grid, checks exact repeated-root identities and powers over rational families, compares the exact norm formula against singular-value computations, and independently checks the sharp \(s=5/2\) example. Run `python verify.py` after installing dependencies from `requirements.txt`. Computational samples corroborate but do not establish the universal statements; their proof is given above.

## Relationship to prior work

Delayed quadratic-gradient convergence and its constant-learning-rate analysis were studied by Arjevani, Shamir and Srebro [1], and general delayed-gradient error estimates by Stich and Karimireddy [2]. Delay-adaptive schedules and sufficient convergence conditions for asynchronous optimization were developed by Wu and collaborators [3]. Cyclic steps and rate optimization for **current-gradient** heavy-ball updates were studied by Goujaud and collaborators [4]. Unlike those settings, the present exact two-period result concerns **stale-gradient** coefficients on the preceding iterate and includes a full fixed-sum spectral phase transition and the order-sensitive exact Euclidean transient law. Its Schur/Floquet reduction is classical, not presented as a novel principle. An earlier specialized formula may exist; independent priority checking is not performed.

## Limitations

This is a scalar quadratic, deterministic, one-iteration-delay theorem for strictly positive two-periodic rates. The rate is the spectral radius per two steps; at critical damping, finite-horizon amplification has a polynomial prefactor and may be large. The theorem makes no statement about arbitrary schedules, noisy gradients, nonquadratic global convergence, multidimensional robust parameter tuning, or optimization of transient loss. The \(s=1\) rate optimum is an unattained infimum under strict positivity. The sharp stability budget is not a recommendation to use aggressive alternating steps without safeguards.

## References

[1] Arjevani, Y.; Shamir, O.; Srebro, N. *A Tight Convergence Analysis for Stochastic Gradient Descent with Delayed Updates.* arXiv:1806.10188 (2018), https://arxiv.org/abs/1806.10188.

[2] Stich, S. U.; Karimireddy, S. P. *The Error-Feedback Framework: Better Rates for SGD with Delayed Gradients and Compressed Updates.* arXiv:1909.05350 (2019), https://arxiv.org/abs/1909.05350.

[3] Wu, X.; Magnusson, S.; Feyzmahdavian, H. R.; Johansson, M. *Delay-Adaptive Step-sizes for Asynchronous Learning.* arXiv:2202.08550 (2022), https://arxiv.org/abs/2202.08550.

[4] Goujaud, B.; Scieur, D.; Dieuleveut, A.; Taylor, A. B.; Pedregosa, F. *Super-Acceleration with Cyclical Step-sizes.* PMLR 151 (2022), https://proceedings.mlr.press/v151/goujaud22a.html.
