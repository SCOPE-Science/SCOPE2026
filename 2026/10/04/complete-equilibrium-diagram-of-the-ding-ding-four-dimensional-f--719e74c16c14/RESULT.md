# Complete equilibrium diagram of the Ding–Ding four-dimensional flow
## Finding
Consider the autonomous system
\[
\dot x=a(y-x),\qquad
\dot y=bx-y-xz+w,\qquad
\dot z=x^2-cz,\qquad
\dot w=w-dx^3,
\]
with \(a,b,c,d>0\). Its real equilibria admit a complete parameter classification. When \(dc\ne1\), define
\[
R=\frac{c(1-b)}{dc-1}.
\]
If \(R>0\), there are exactly three equilibria,
\[
O=(0,0,0,0),\qquad
E_\pm=(\pm\sqrt R,\pm\sqrt R,R/c,\pm dR^{3/2}).
\]
If \(R\le0\), the origin is the only distinct equilibrium. When \(dc=1\), the origin is the only equilibrium if \(b\ne1\); if also \(b=1\), every point
\[
(x,x,x^2/c,x^3/c),\qquad x\in\mathbb R,
\]
is an equilibrium.

For the parameters emphasized in the introducing paper, \((a,b,c,d)=(24,25,3,1/2)\), one has \(R=-144\). Hence the origin is the only equilibrium, although the paper labels the entire curve \((x,x,x^2/3,x^3/2)\) as an equilibrium curve. The origin is always linearly unstable because its Jacobian has the exact eigenvalue \(1\).

## Assumptions and scope
The classification concerns the differential equations exactly as printed in Ding and Ding (2020), with positive real parameters \(a,b,c,d\). It is a statement about equilibria and their linearization, not about the existence of numerically observed hyperchaotic trajectories, the quality of numerical Lyapunov estimates, or the cryptographic performance of the later image-encryption construction.

The primary mathematical classification is MSC2020 37C10, dynamics induced by flows and semiflows.

## Proof
At an equilibrium, the first equation and \(a>0\) give \(y=x\). The third equation and \(c>0\) give \(z=x^2/c\), while the fourth gives \(w=dx^3\). Substituting these three identities into the second equation yields
\[
0=bx-x-x\frac{x^2}c+dx^3
 =x\left[(b-1)+\left(d-\frac1c\right)x^2\right].
\]
Thus either \(x=0\), giving the origin, or
\[
(dc-1)x^2=c(1-b).
\]
If \(dc\ne1\), this is exactly \(x^2=R\). A positive \(R\) gives the two real signs shown above; \(R<0\) gives no nonzero real solution; and \(R=0\) yields only \(x=0\), so no additional distinct equilibrium exists.

If \(dc=1\), the reduced second equation becomes \(x(b-1)=0\). Therefore \(b\ne1\) again forces \(x=0\), while \(b=1\) leaves \(x\) arbitrary and produces exactly the stated one-dimensional equilibrium curve.

At the origin the Jacobian is
\[
J(O)=\begin{pmatrix}
-a&a&0&0\\
b&-1&0&1\\
0&0&-c&0\\
0&0&0&1
\end{pmatrix}.
\]
Consequently
\[
\det(\lambda I-J(O))
=(\lambda+c)(\lambda-1)
\left(\lambda^2+(a+1)\lambda+a(1-b)\right),
\]
so \(1\) is always an eigenvalue. The origin is therefore linearly unstable for every allowed parameter choice.

For \((a,b,c,d)=(24,25,3,1/2)\), direct substitution gives \(R=-144\), proving that only the origin is an equilibrium at the paper's showcased parameter set. For example, the paper's displayed curve point corresponding to \(x=1\) has a nonzero second component of the vector field, so it is not an equilibrium.

## Verification
The accompanying `verify.py` uses exact rational arithmetic to replay the showcased-parameter calculation, verify a positive-\(R\) example, verify the degenerate equilibrium-curve case, and check directly that the fourth row of \(J(O)-I\) vanishes. Running it from the packaged path prints `VERIFY_OK`.

The proof itself is algebraic and does not infer an infinite classification from finite experimentation; the script is only a replay aid.

## Relationship to prior work
The introducing paper explicitly asserts that an equilibrium curve exists for the system, plots that curve at \((a,b,c,d)=(24,25,3,1/2)\), and then performs a Routh–Hurwitz calculation at an arbitrary point taken from such a curve. It also separately gives a sign condition involving \(c(1-b)/(dc-1)\), but its printed nonzero equilibrium coordinates omit the square roots required by \(x^2=R\).

The exact substitution above reconciles these statements: a genuine continuum of equilibria occurs only on the codimension-two parameter locus \(b=1\) and \(dc=1\). Away from that locus, the equilibria are isolated and are completely classified by the sign of \(R\). Targeted searches of the source DOI, the reduced equilibrium equation, and close published dynamical-system records did not locate a prior source stating this complete correction.

## Limitations
This finding corrects the equilibrium geometry and the applicability of the paper's local-stability calculation. It does not establish that the numerically plotted attractor is absent, does not recompute its Lyapunov spectrum, and does not evaluate the image-encryption experiments. A correction or discussion could exist in literature not captured by the searched indexes.

## References
1. L. Ding and Q. Ding, “The Establishment and Dynamic Properties of a New 4D Hyperchaotic System with Its Application and Statistical Tests in Gray Images,” *Entropy* 22 (2020), 310. DOI: 10.3390/e22030310. PMCID: PMC7516767.
2. OpenAlex record W3012474806, publication date 2020-03-10; PMID 33286085.
3. Mathematics Subject Classification 2020, 37C10, “Dynamics induced by flows and semiflows.”
