# Exact equilibrium indices and divergence correction for the Wang–Feng–Chen flow
## Finding
Consider the autonomous flow
\[
\dot x=a(y-x),\qquad \dot y=-by+xz+k,\qquad \dot z=d-e^{xy},\qquad \dot w=czw,
\]
with \(a,b,c,k>0\) and \(d>0\). Its equilibrium set is completely determined as follows. There is no equilibrium when \(d\le 1\). If \(d>1\), put \(s=\sqrt{\log d}\). Away from \(d_*=\exp((k/b)^2)\), there are exactly two equilibria
\[
E_\sigma=(\sigma s,\sigma s,b-\sigma k/s,0),\qquad \sigma\in\{+1,-1\}.
\]
At \(d=d_*\), the positive branch becomes the entire equilibrium line
\[
L=\{(k/b,k/b,0,w):w\in\mathbb R\},
\]
while \(E_-=(-k/b,-k/b,2b,0)\) remains isolated.

For the published parameter choice \(a=13/5\), \(b=1/5\), \(c=5\), \(d=17\), \(k=3\), both equilibria are hyperbolic and unstable. The positive equilibrium has unstable dimension two, and the negative equilibrium has unstable dimension three. Thus the published assertion that both equilibria are asymptotically stable is incompatible with the displayed vector field.

The exact divergence is
\[
\nabla\!\cdot F=-a-b+cz.
\]
At the source's point with \(z=1/10\) this equals \(-23/10=-2.3\), but it is positive whenever \(z>14/25\) at the published parameters. Therefore the single negative value reported in the source does not prove globally negative divergence or uniform phase-volume contraction.

## Assumptions and scope
The equilibrium classification assumes real state variables and \(a,b,c,k>0\), \(d>0\). The stability-index statement is only for the published parameters \(a=13/5\), \(b=1/5\), \(c=5\), \(d=17\), \(k=3\). The divergence statement is pointwise and does not assert that every long-time average of the divergence is positive or negative.

## Proof
At an equilibrium, \(a>0\) gives \(y=x\). The third equation then gives \(e^{x^2}=d\). Hence \(d<1\) is impossible. If \(d=1\), then \(x=y=0\), but the second equation equals \(k>0\), so no equilibrium exists. If \(d>1\), then \(x=y=\sigma s\), where \(s=\sqrt{\log d}>0\) and \(\sigma\in\{+1,-1\}\). The second equation gives \(z=b-\sigma k/s\). The fourth equation requires \(czw=0\). The negative branch has \(z=b+k/s>0\), so \(w=0\). The positive branch has \(z=b-k/s\), which vanishes exactly when \(s=k/b\), equivalently \(d=\exp((k/b)^2)\); only there is \(w\) arbitrary. This proves the equilibrium classification.

At any isolated equilibrium with \(w=0\), the Jacobian splits into a three-dimensional base block and the fiber eigenvalue \(cz\). With \(x=y=\sigma s\) and \(e^{xy}=d\), the base characteristic polynomial is
\[
q_\sigma(\lambda)=\lambda^3+(a+b)\lambda^2+\left(ab-a z_\sigma+d s^2\right)\lambda+2ad s^2.
\]
For the published parameters, write \(L=\log 17\), \(s=\sqrt L\). Then
\[
q_\sigma(\lambda)=\lambda^3+A\lambda^2+B_\sigma\lambda+C,
\]
where
\[
A=\frac{14}{5},\qquad B_\sigma=17L+\sigma\frac{39}{5s},\qquad C=\frac{442}{5}L.
\]
The exact certificate in `verify.py` proves \(2.83<L<2.84\), hence \(1.68<s<2\). It also proves \(B_->0\) and
\[
A B_\sigma-C<0\qquad(\sigma=\pm1).
\]
The Routh first column for each monic cubic therefore has signs \(+,+,-,+\), giving exactly two roots in the open right half-plane and one in the open left half-plane. No first-column entry vanishes, so there is no imaginary-axis root. The fiber eigenvalue is \(c(b-3/s)<0\) on the positive branch and \(c(b+3/s)>0\) on the negative branch. Thus the full unstable dimensions are respectively two and three, and both equilibria are hyperbolic.

Finally, differentiating the vector field componentwise gives \(\nabla\!\cdot F=-a-b+cz\). Substitution of the source's initial \(z=1/10\) gives \(-2.3\), while the sign changes at \(z=(a+b)/c=14/25\).

## Verification
Run `python3 verify.py`. It uses exact rational arithmetic and Taylor bounds for the exponential to certify \(2.83<\log 17<2.84\), then verifies the strict inequalities needed for the Routh count and the fiber-eigenvalue signs. The expected output is `VERIFY_OK`.

## Relationship to prior work
Wang, Feng, and Chen introduced this flow and reported the same parameter set, a divergence value of \(-2.3\) at one initial state, and two asymptotically stable equilibria. Direct reconstruction from their displayed equations instead gives the state-dependent divergence, the complete equilibrium set above, and unstable indices two and three at their baseline parameters. The correction is source-specific: standard Routh theory supplies the counting tool, but not these coefficients or conclusions.

The source uses equilibrium stability as part of its justification for calling the numerically observed attractor hidden. The present result removes that particular justification. It does not prove that the reported attractor is self-excited or hidden, because that distinction depends on basin geometry rather than solely on equilibrium eigenvalues.

## Limitations
No claim is made about global boundedness, the existence or uniqueness of the numerically plotted attractor, the correctness of the reported Lyapunov diagrams, or the basin intersection required by the formal hidden-attractor definition. Positive divergence on part of state space does not by itself disprove asymptotic volume contraction along a particular invariant set. The exceptional equilibrium line occurs at \(d=\exp((k/b)^2)\), far from the paper's baseline \(d=17\).

## References
1. Xuan Wang, Yiran Feng, and Yixin Chen, “A New Four-Dimensional Chaotic System and its Circuit Implementation,” *Frontiers in Physics* 10 (2022), article 906138, DOI 10.3389/fphy.2022.906138. Publicly published 27 April 2022.
2. MSC2020 37C10, “Dynamics induced by flows and semiflows.”
