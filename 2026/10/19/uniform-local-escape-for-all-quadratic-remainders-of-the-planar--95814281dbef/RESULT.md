# Uniform local escape for all quadratic remainders of the planar nonsmooth-fold companion normal form

## Finding

**Theorem (uniform local escape under quadratic perturbations).** Fix real numbers \(\delta_L,\delta_R\) and \(\alpha>0\). Consider a continuous map \(F_\mu\), defined near the origin of the plane for \(\mu\ge0\), with branches
\[
F_\mu(x,y)=\begin{cases}
((1+\delta_L-\alpha)x+y+\mu+E^L_1(x,y,\mu),\;-\delta_Lx+E^L_2(x,y,\mu)),&x\le0,\\
((1+\delta_R+\alpha)x+y+\mu+E^R_1(x,y,\mu),\;-\delta_Rx+E^R_2(x,y,\mu)),&x\ge0.
\end{cases}
\]
Suppose the two remainder vectors agree on \(x=0\) and, for some finite \(C\ge0\), \(r_0>0\), obey
\[
|E^\sigma_i(x,y,\mu)|\le C(|x|+|y|+\mu)^2
\quad (i=1,2;\ \sigma=L,R;\ |x|+|y|+\mu\le r_0).
\]
There exist explicit \(\eta>0\), \(\mu_0>0\) such that for every \(0<\mu\le\mu_0\) and every \((x,y)\) in the closed Euclidean ball \(B_\eta\), the orbit leaves \(B_\eta\) in finite forward time. More precisely, defining \(\lambda=12C+2\), \(K=\sqrt2\eta+\lambda\eta^2\), one may choose \(\mu_0=\eta\) and achieve the uniform exit-time bound
\[
1\le m\le \left\lfloor\frac{4K}{\mu}\right\rfloor+1,
\qquad \|F_\mu^m(x,y)\|_2>\eta.
\]
In particular, no nonempty forward-invariant set is contained in \(B_\eta\). The result holds for *every* choice of the two real determinant parameters and all quadratically small continuous perturbations, including arbitrary compatible \(C^2\) remainders with zero constant and linear terms. It is a special-family result, not the general nonlinear nonsmooth-fold conjecture.

## Assumptions and scope

The switch is \(x=0\). The two formulae agree on it, so \(F_\mu\) is unambiguous. The norm in the conclusion is Euclidean. Only values of the perturbations at points inside \(B_\eta\) are needed; the map may be extended arbitrarily outside its neighborhood of definition. The parameters \(\delta_L,\delta_R\) need not have opposite signs. The smallness estimate is uniform in the branch and in \(\mu\) near zero. Every jointly piecewise-\(C^2\) perturbation vanishing to first order has such a bound locally by Taylor's theorem.

For the linear parts, \(\det(I-A_L)=\alpha>0\) and \(\det(I-A_R)=-\alpha<0\). Their virtual fixed points have first coordinates \(\mu/\alpha\) (left extension) and \(-\mu/\alpha\) (right extension) for \(\mu>0\); thus the result treats the nonsmooth-fold side where the two linear equilibria are inadmissible. No conclusion about globally bounded orbits outside \(B_\eta\) is asserted.

## Proof

Put \(D=\max(|\delta_L|,|\delta_R|)\), \(\lambda=12C+2\), \(A=6C+1\), and \(B=6C+1+2\lambda D^2\). Choose any positive \(\eta\) satisfying
\[
\eta\le\min\left\{\frac{r_0}{3},\frac12,\frac{\alpha}{2B},\frac1{2A}\right\},\qquad
54\lambda C^2\eta^2\le1.
\]
The last condition is automatic if \(C=0\). Let \(\mu_0=\eta\) and define
\[
\Phi(x,y)=x+y-\lambda y^2.
\]
For \(0<\mu\le\eta\), \(\|(x,y)\|_2\le\eta\), set \(s=|x|+|y|+\mu\), \(Q=x^2+y^2+\mu^2\). Then \(s\le3\eta\) and \(s^2\le3Q\). Write \(\delta=\delta_L\) or \(\delta_R\) according to the sign of \(x\), and \(E_i\) for the corresponding remainder. Summing the two coordinates of the update cancels the \(\delta x\) terms, yielding the exact identity
\[
\Phi(F_\mu(x,y))-\Phi(x,y)
=\mu+\alpha|x|+E_1+E_2+\lambda y^2-\lambda(-\delta x+E_2)^2.
\]
First, \(|E_1+E_2|\le2Cs^2\le6CQ\). Second, using \((u+v)^2\le2u^2+2v^2\),
\[
(-\delta x+E_2)^2\le2D^2x^2+2C^2s^4
\le2D^2x^2+54C^2\eta^2Q.
\]
The choice of \(\eta\) therefore proves the uniform drift inequality
\[
\begin{aligned}
\Phi(F_\mu(x,y))-\Phi(x,y)
&\ge \mu+\alpha|x|+(\lambda-6C-1)y^2-Bx^2-A\mu^2\\
&\ge \frac\mu2+\frac\alpha2|x|+A y^2
\ge\frac\mu2.
\end{aligned}
\]
Here \(\lambda-6C-1=A\), \(Bx^2\le B\eta|x|\le\alpha|x|/2\), and \(A\mu^2\le A\eta\mu\le\mu/2\). This holds on *both* closed half-planes, including their shared boundary.

On the ball \(B_\eta\), the function \(\Phi\) satisfies \(|\Phi|\le K=\sqrt2\eta+\lambda\eta^2\). If an orbit remained inside \(B_\eta\) for the first \(n\) updates, telescoping the drift would give \(n\mu/2\le\Phi(F_\mu^n(x,y))-\Phi(x,y)\le2K\). Therefore it must leave by the integer time \(\lfloor4K/\mu\rfloor+1\). The same argument rules out every nonempty forward-invariant subset of the ball. \(\square\)

## Verification

The standalone standard-library script `verify.py` checks the exact rational drift inequality on 5,968 states for four choices of \((\delta_L,\delta_R)\), including same-sign and reversed-sign cases, with nonzero quadratic remainders in both coordinates. Run `python verify.py`. Its output is an exact-fraction assertion result, not a proof of the universally quantified theorem; the algebraic inequalities above provide that proof.

## Relationship to prior work

Simpson's *Nonsmooth folds as tipping points* proves divergence for the truncated piecewise-linear normal form and formulates a conjecture for general higher-order perturbations (Conjecture 2). Its Appendix A, Proposition 6, handles the special quadratic perturbation \(E_1=0\), \(E_2=-y^2\) with \(\delta_L>0\), \(\delta_R<0\). The present theorem is a quantified uniform extension for *arbitrary* quadratically small remainder pairs and *all* \(\delta_L,\delta_R\in\mathbb R\), still within the specified companion-matrix family. The paper's general conjecture for all dimensions and all piecewise-\(C^1\) perturbations is not resolved.

## Limitations

The branch matrices are fixed to the companion form displayed in the theorem; this does not treat general piecewise-linear matrices or three-dimensional systems. Remainders merely satisfying \(o(\|(x,y,\mu)\|)\) without a quadratic bound are excluded. The local radius and exit-time prefactor may be small/large and are not claimed to be sharp. Nonempty invariant sets far from the collision need not disappear.

## References

D. J. W. Simpson, *Nonsmooth folds as tipping points*, arXiv:2406.04587 (first posted 2024-06-07), especially §§3–4 and Appendix A, Conjecture 2 and Proposition 6. DOI: 10.1063/5.0222291.

D. J. W. Simpson and P. A. Glendinning, *Inclusion of higher-order terms in the border-collision normal form: Persistence of chaos and applications to power converters*, *Physica D* **462** (2024), 134131, DOI: 10.1016/j.physd.2024.134131 (different, attractor-persistence regime).
