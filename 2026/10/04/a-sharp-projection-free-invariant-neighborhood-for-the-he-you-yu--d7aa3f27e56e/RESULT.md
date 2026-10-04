# A sharp projection-free invariant neighborhood for the He--You--Yuan PDHG counterexample

## Finding
Consider the scalar linear program and its dual from He, You, and Yuan:
\[
\min_x x \quad\text{subject to}\quad x\ge 1,\;x\ge0,
\]
with dual
\[
\max_y y \quad\text{subject to}\quad y\le1,\;y\ge0.
\]
Its Lagrangian is \(L(x,y)=x-y(x-1)\), defined on \(\mathbb R_+\times\mathbb R_+\), and the unique saddle point is \((1,1)\). Write the primal and dual PDHG step sizes as \(\tau=1/r>0\) and \(\sigma=1/s>0\). The update is
\[
 x^+=\max\{x+\tau(y-1),0\},\qquad
 y^+=\max\{y-\sigma(x^+-1),0\}.
\]
Center at the saddle by \(u=x-1\), \(v=y-1\). For \(\tau\sigma<4\), define
\[
H_{\tau,\sigma}(u,v)=\sigma u^2+\tau\sigma uv+\tau v^2,
\qquad
c_*=\min\{\tau,\sigma\}\left(1-\frac{\tau\sigma}4\right).
\]
Then every initial state satisfying
\[
0<H_{\tau,\sigma}(u^0,v^0)<c_*
\]
remains strictly in \(x>0,y>0\), so neither projection ever activates. Along that orbit,
\[
\binom{u^{k+1}}{v^{k+1}}
=
M_{\tau,\sigma}
\binom{u^k}{v^k},
\qquad
M_{\tau,\sigma}
=
\begin{pmatrix}
1&\tau\\
-\sigma&1-\tau\sigma
\end{pmatrix},
\]
and \(H_{\tau,\sigma}\) is exactly conserved. Hence no nonzero state in this neighborhood can converge to the saddle.

The threshold is sharp in a geometric sense: \(c_*\) is the supremal value \(c\) for which the energy sublevel \(\{H_{\tau,\sigma}<c\}\) is wholly contained in \(u>-1,v>-1\), i.e. the strict positive orthant in the original variables.

There is also a complete resonant family. If
\[
\tau\sigma=4\sin^2\left(\frac{\pi}m\right),\qquad m\in\{3,4,5,\ldots\},
\]
then every nonzero orbit in the above projection-free neighborhood has exact period \(m\). In particular, the equal-step choice
\[
\tau=\sigma=2\sin\left(\frac{\pi}m\right)
\]
produces exact nonconvergent cycles whose step size tends to zero as \(m\to\infty\).

## Assumptions and scope
The result concerns the original two-block PDHG/Arrow--Hurwicz update analyzed in the 2014 source, not the extrapolated Chambolle--Pock variant used in many modern LP solvers. The theorem is local in initialization: it identifies an explicit open neighborhood around the saddle in which the nonnegativity projections never activate. It does not claim that every initial point is nonconvergent, nor that the source paper's particular start \((0,0)\) follows the same projection-free orbit for arbitrary step sizes.

The condition \(\tau\sigma<4\) is exactly the positive-definiteness range of the quadratic invariant used below. The periodic statement assumes the displayed resonance and \(m\ge3\).

## Proof
When the projections are inactive, the centered update is
\[
u^+=u+\tau v,\qquad v^+=v-\sigma u^+,
\]
so \(z^+=M_{\tau,\sigma}z\). Let
\[
Q=\begin{pmatrix}
\sigma&\tau\sigma/2\\
\tau\sigma/2&\tau
\end{pmatrix}.
\]
A direct multiplication gives
\[
M_{\tau,\sigma}^\top Q M_{\tau,\sigma}=Q.
\]
Thus \(H_{\tau,\sigma}(z)=z^\top Qz\) is conserved whenever the linear update applies. Moreover,
\[
\det Q=\tau\sigma\left(1-\frac{\tau\sigma}4\right)>0,
\]
so \(H_{\tau,\sigma}\) is positive definite when \(\tau\sigma<4\).

It remains to prove that the stated energy bound prevents either projection from activating. On the boundary \(u=-1\), complete the square:
\[
H_{\tau,\sigma}(-1,v)
=
\sigma\left(1-\frac{\tau\sigma}4\right)
+\tau\left(v-\frac{\sigma}{2}\right)^2.
\]
Hence the least energy on that boundary is \(\sigma(1-\tau\sigma/4)\). Likewise,
\[
H_{\tau,\sigma}(u,-1)
=
\tau\left(1-\frac{\tau\sigma}4\right)
+\sigma\left(u-\frac{\tau}{2}\right)^2,
\]
whose boundary minimum is \(\tau(1-\tau\sigma/4)\). Therefore every point with \(H<c_*\) lies strictly in \(u>-1,v>-1\). Conversely, at energy \(c_*\) one of these two boundaries is touched, proving sharpness of the sublevel threshold.

Now start with \(H(z^0)<c_*\). The linear candidate \(M z^0\) has the same energy, hence both of its coordinates are strictly larger than \(-1\). Therefore the raw primal and dual updates are positive and the projections do nothing. Induction gives projection-free motion and exact conservation for every iterate. Since \(H(z^0)>0\) and is conserved while \(H(0,0)=0\), the orbit cannot converge to the saddle.

Finally,
\[
\det M_{\tau,\sigma}=1,\qquad
\operatorname{tr}M_{\tau,\sigma}=2-\tau\sigma.
\]
If \(\tau\sigma=4\sin^2(\pi/m)\), then
\[
\operatorname{tr}M_{\tau,\sigma}
=2\cos\left(\frac{2\pi}m\right),
\]
so the two eigenvalues are the primitive roots \(e^{\pm 2\pi i/m}\). Consequently \(M^m=I\), while \(M^j-I\) is invertible for \(1\le j<m\). Every nonzero projection-free orbit therefore has exact period \(m\).

## Verification
The accompanying `check.py` symbolically verifies the matrix invariant, positive-definiteness determinant, the two completed-square boundary identities, determinant and trace of the iteration matrix, and representative resonant powers. It also numerically checks projection-free resonant orbits for several periods. The recorded output is `VERIFY_OK`.

## Relationship to prior work
He, You, and Yuan give this scalar LP as their illustrative nonconvergence example. They prove an exact six-cycle for \(r=s=1\), starting from \((0,0)\), and then report finite 1000-iteration tests for much larger \(r=s\) as evidence that tiny fixed steps need not cure nonconvergence. Their paper does not derive an invariant neighborhood, a sharp projection-free threshold, or exact arbitrarily-small-step periodic families.

Bailey, Gidel, and Piliouras later prove an exact conserved quadratic energy and recurrence for *unconstrained* alternating gradient descent--ascent in bilinear zero-sum games. The quadratic form above is the scalar specialization of that conserved energy after centering. That broader result explains the linear interior dynamics, so the invariant itself is not claimed as new. The additional statement here is the exact interaction with the nonnegativity projections: the boundary minimization yields the largest centered invariant-energy sublevel on which the constrained PDHG map is guaranteed to coincide forever with the unconstrained symplectic map. Combining that sharp threshold with the eigenangle calculation produces explicit exact \(m\)-cycles for arbitrarily small PDHG steps in the constrained LP.

Later analyses of PDHG for linear programming study convergent extrapolated/modern PDHG variants, active-set identification, and local rates under standard step restrictions. They do not supply the threshold or resonant family stated here for the original non-extrapolated Arrow--Hurwicz PDHG counterexample.

## Limitations
The result is a two-dimensional phase-space calculation for one scalar LP. It does not characterize the global piecewise-linear dynamics once a projection activates. It also does not imply that the original zero initialization is periodic for every small step. The originality comparison found no statement matching the sharp threshold or resonant constrained family, but an unindexed note could contain the same calculation. The result has received same-model review only; no independent audit has been performed.

## References
1. B. He, Y. You, and X. Yuan, *On the Convergence of Primal-Dual Hybrid Gradient Algorithm*, SIAM Journal on Imaging Sciences 7(4), 2526--2537 (2014), DOI: 10.1137/140963467.
2. J. P. Bailey, G. Gidel, and G. Piliouras, *Finite Regret and Cycles with Fixed Step-Size via Alternating Gradient Descent-Ascent*, arXiv:1907.04392 (2019), later COLT 2020.
3. H. Lu and J. Yang, *On the Geometry and Refined Rate of Primal-Dual Hybrid Gradient for Linear Programming*, arXiv:2307.03664; Mathematical Programming 212, 349--387 (2025).
