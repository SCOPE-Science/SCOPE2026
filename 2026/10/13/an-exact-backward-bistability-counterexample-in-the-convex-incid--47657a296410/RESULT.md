# An exact backward-bistability counterexample in the convex-incidence SIR model

## Finding

The printed system is
\[
\dot S=B-\eta S-MIS(1+\gamma I)+\alpha R,
\]
\[
\dot I=MIS(1+\gamma I)-(\mu+\eta)I,
\]
\[
\dot R=\mu I-(\alpha+\eta)R.
\]

Its disease-free equilibrium is
\[
E_0=\left(\frac{B}{\eta},0,0\right).
\]
Direct linearization of the infected equation gives
\[
\lambda_I=\frac{MB}{\eta}-(\mu+\eta),
\]
so the actual invasion threshold is
\[
\mathcal R=\frac{MB}{\eta(\mu+\eta)}.
\]
This differs in general from the source's equation (2.4),
\[
\mathcal R_0^{\mathrm{print}}=\frac{MB}{\mu(B+\mu)}.
\]

Even after using the correct threshold, the source's claim that no positive equilibrium exists below threshold is false. Define
\[
k=\frac{\eta(\mu+\alpha+\eta)}{\alpha+\eta}.
\]
For \(0<\mathcal R<1\), there are two distinct positive endemic equilibria exactly when
\[
\gamma>
\frac{k}{B}
\frac{\left(1+\sqrt{1-\mathcal R}\right)^2}{\mathcal R}.
\]

The exact parameter choice
\[
B=\eta=\mu=\alpha=M=1,\qquad \gamma=10
\]
has
\[
\mathcal R=\mathcal R_0^{\mathrm{print}}=\frac12,
\]
yet has two endemic equilibria,
\[
E_-=\left(\frac34,\frac16,\frac1{12}\right),\qquad
E_+=\left(\frac25,\frac25,\frac15\right).
\]
Here the disease-free equilibrium and \(E_+\) are locally asymptotically stable, while \(E_-\) is a saddle. The model therefore has exact backward bistability at a subthreshold parameter set.

## Assumptions and scope

All six model parameters are positive.

The claim treats the ordinary differential equation system exactly as printed. It separates two issues: the displayed reproduction number is not the linear invasion threshold, and the convex incidence can produce subthreshold endemic multiplicity even after the correct threshold is used.

The exact witness was chosen so that the printed and correct threshold quantities both equal \(1/2\). Therefore its contradiction to the no-endemic-equilibrium and global-attraction claims does not depend on the reproduction-number formula mismatch.

The result does not classify every possible phase portrait of the model.

## Proof

At the disease-free equilibrium,
\[
I=R=0,\qquad S=\frac{B}{\eta}.
\]
The infected linearization is
\[
\dot I=
\left(\frac{MB}{\eta}-(\mu+\eta)\right)I+O(I^2),
\]
which yields
\[
\mathcal R=\frac{MB}{\eta(\mu+\eta)}.
\]

At a positive equilibrium, the infected and recovered equations give
\[
S=\frac{\mu+\eta}{M(1+\gamma I)},\qquad
R=\frac{\mu}{\alpha+\eta}I.
\]
Substitution into the susceptible equation gives
\[
B-\frac{\eta(\mu+\eta)}{M(1+\gamma I)}
-\frac{\eta(\mu+\alpha+\eta)}{\alpha+\eta}I=0.
\]
With
\[
k=\frac{\eta(\mu+\alpha+\eta)}{\alpha+\eta},
\]
this is equivalent to
\[
k\gamma I^2+(k-B\gamma)I+B\left(\frac1{\mathcal R}-1\right)=0.
\]

Assume
\[
0<\mathcal R<1.
\]
The leading and constant coefficients are positive. Two distinct positive roots occur exactly when the sum of roots is positive and the discriminant is positive:
\[
B\gamma>k
\]
and
\[
(B\gamma-k)^2>
4k\gamma B\left(\frac1{\mathcal R}-1\right).
\]
Putting
\[
z=\frac{B\gamma}{k}
\]
reduces the discriminant boundary to
\[
(z-1)^2=4z\frac{1-\mathcal R}{\mathcal R}.
\]
The boundary root with \(z>1\) is
\[
z_+=\frac{\left(1+\sqrt{1-\mathcal R}\right)^2}{\mathcal R},
\]
giving the stated condition.

For
\[
B=\eta=\mu=\alpha=M=1,\qquad \gamma=10,
\]
one has
\[
\mathcal R=\frac12,\qquad k=\frac32.
\]
The endemic equation becomes
\[
30I^2-17I+2=0,
\]
with roots
\[
I_-=\frac16,\qquad I_+=\frac25.
\]
Back-substitution gives the two stated equilibria.

The Jacobian is
\[
J=
\begin{pmatrix}
-\eta-MI(1+\gamma I) & -MS(1+2\gamma I)&\alpha\\
MI(1+\gamma I)&MS(1+2\gamma I)-(\mu+\eta)&0\\
0&\mu&-(\alpha+\eta)
\end{pmatrix}.
\]
At the disease-free equilibrium its characteristic polynomial is
\[
(\lambda+1)^2(\lambda+2).
\]
At \(E_-\) it is
\[
\frac{(\lambda+1)(36\lambda^2+43\lambda-42)}{36}.
\]
The quadratic factor has negative constant term, hence one positive root. At \(E_+\) it is
\[
\frac{(\lambda+1)(5\lambda^2+12\lambda+14)}5.
\]
Its quadratic discriminant is
\[
-136<0
\]
and its real part is negative. This proves the stated stability types.

## Verification

The bundled `verify.py` uses exact symbolic arithmetic to reconstruct the disease-free eigenvalue, the endemic-equilibrium quadratic, the saddle-node boundary, the exact witness, and all three characteristic polynomials.

It verifies the exact infected roots
\[
\frac16,\qquad \frac25
\]
and the complete equilibrium coordinates. No numerical integration, parameter grid, or floating-point stability test is used.

## Relationship to prior work

The motivating article introduces the convex incidence
\[
MIS(1+\gamma I)
\]
and states that its equation (2.4) is the basic reproduction number. It then states that a subthreshold value excludes positive equilibria and later claims global attraction of the disease-free equilibrium.

Nonlinear-incidence epidemic models are already known to exhibit saddle-node and richer bifurcations. Ruan and Wang analyze a different nonlinear-incidence model with saddle-node, Hopf, and homoclinic bifurcations. That general phenomenon is not claimed as new here.

The source-specific contribution is the correct invasion threshold of this printed model, the exact endemic-equilibrium quadratic, the sharp subthreshold two-root condition, and an exact stable–saddle–stable witness at threshold value \(1/2\).

Targeted source, formula, equilibrium-count, backward-bifurcation, correction, and erratum searches did not locate a published correction of these claims.

## Limitations

The result does not classify all parameter regimes or determine the global basin boundary of the exact bistable witness.

The broader possibility of backward bifurcation under nonlinear incidence is established prior theory. Originality is restricted to the exact printed model and its source-specific formulas.

## References

1. R. ud Din, K. Shah, M. A. Alqudah, T. Abdeljawad, F. Jarad, “Mathematical study of SIR epidemic model under convex incidence rate,” AIMS Mathematics 5 (2020), 7548–7561. DOI: 10.3934/math.2020483.
2. S. Ruan, W. Wang, “Dynamical behavior of an epidemic model with a nonlinear incidence rate,” Journal of Differential Equations 188 (2003), 135–163. DOI: 10.1016/S0022-0396(02)00089-X.
