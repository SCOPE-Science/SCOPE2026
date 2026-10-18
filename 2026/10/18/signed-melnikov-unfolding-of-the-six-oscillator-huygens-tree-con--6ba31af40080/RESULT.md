# Signed Melnikov unfolding of the six-oscillator Huygens tree connection

## Finding

Fix any interaction strength \(0<h<2/(5+\sqrt{17})\). Consider the six-vertex double-star tree with the central edge weighted by \(\alpha>0\) and the four leaf edges weighted by one. Restrict the exact edge-phase discrete Huygens map to its invariant leaf-symmetric two-torus. In coordinates \((u,v)\in(\mathbb R/2\pi\mathbb Z)^2\), its lift is

\[
F_{h,\alpha}(u,v)=\bigl(u+h(2\alpha\sin u+4\sin v),\ v+h(\alpha\sin u+3\sin v)\bigr).
\]

The fixed points \(p=(\pi,0)\), \(q=(0,\pi)\) are saddles for all \(\alpha\) sufficiently close to \(1\). At \(\alpha=1\), their one-dimensional unstable and stable branches agree along the heteroclinic arc \(u=v+\pi\), \(0<v<\pi\). This coincident arc was identified in the motivating source. Our assertion quantifies its response to a *single central-edge detuning*.

For a fixed \(v_0\in(0,\pi)\), let \(v_j\), \(j\in\mathbb Z\), be the unique bi-infinite orbit satisfying

\[
v_0=v_0,\qquad v_{j+1}=v_j+2h\sin v_j,\qquad 0<v_j<\pi.
\]

Set \(a_j=1-h\cos v_j\). Define the **signed splitting coefficient**

\[
M_h(v_0)=h\sum_{j=-\infty}^{-1}\sin v_j\prod_{k=j+1}^{-1}a_k
+h\sum_{j=0}^{\infty}\frac{\sin v_j}{\prod_{k=0}^{j}a_k}.
\]

Empty products equal one. Both series converge absolutely and \(M_h(v_0)>0\). If \(u^{\mathrm u}_{h,\alpha}(v_0)\) and \(u^{\mathrm s}_{h,\alpha}(v_0)\) are the lifted intersection coordinates of the respective unstable branch of \(p\) and stable branch of \(q\) with the vertical section \(v=v_0\), chosen continuously near \(u=v_0+\pi\), then

\[
\boxed{u^{\mathrm s}_{h,\alpha}(v_0)-u^{\mathrm u}_{h,\alpha}(v_0)
=(\alpha-1)M_h(v_0)+O_{h,v_0}((\alpha-1)^2).}
\]

In particular, the stable intersection lies strictly above the unstable intersection for small \(\alpha>1\), and strictly below it for small \(\alpha<1\). This gives a **strict, signed, first-order unfolding** of the symmetric heteroclinic arc, not a numerical suggestion of splitting.

## Assumptions and scope

The six-vertex tree has oriented edges \((1,2),(1,3),(1,4),(5,2),(6,2)\), exactly as in Proposition 5.12 of Buescu–D’Aniello–Oliveira, and all edges use the repulsive sine interaction. Only the first edge has weight \(\alpha\); the others have weight one. The full quotient phase map is \(z\mapsto z+hK_*\operatorname{diag}(\alpha,1,1,1,1)\sin z\), where

\[
K_*=\begin{pmatrix}2&1&1&1&1\\1&2&1&0&0\\1&1&2&0&0\\1&0&0&2&1\\1&0&0&1&2\end{pmatrix}.
\]

The subtorus \(z=(u,v,v,v,v)\) remains invariant for every \(\alpha>0\); substitution yields the two-coordinate map above. The parameter \(h\) is fixed, not taken to zero. For \(\alpha\) near one, the full map and its restricted map remain diffeomorphisms by continuity of the spectral invertibility bound. All splitting statements are **inside this invariant two-torus** and apply to fixed compact interior sections. The fixed-point existence, hyperbolicity, and local branch labels persist for \(\alpha\) near one.

## Proof

**1. Reduction and the unperturbed connection.** Subtracting the second lifted coordinate from the first, define \(w=u-v-\pi\). Then the exact map reads

\[
\begin{aligned}
w^+&=w+h[\sin v-\alpha\sin(v+w)],\\
v^+&=v+h[3\sin v-\alpha\sin(v+w)].
\end{aligned}
\]

At \(\alpha=1\) and \(w=0\), the first component is zero and the second reduces to \(f_h(v)=v+2h\sin v\). Since \(h<1/2\), this is an increasing diffeomorphism of \([0,\pi]\) fixing its endpoints, with \(f_h(v)>v\) in the interior. Its unique two-sided orbit through \(v_0\) consequently tends to zero in backward time and to \(\pi\) in forward time. The endpoint derivatives are \(1+2h>1\) and \(1-2h\in(0,1)\). Thus \(v_j\) decays geometrically as \(j\to-\infty\) and \(\pi-v_j\) decays geometrically as \(j\to+\infty\).

At \(p\) the two tangent multipliers of \(F_{h,1}\) are \(1+2h\), \(1-h\); at \(q\) they are \(1-2h\), \(1+h\). All lie away from the unit circle. Consequently the unstable one-manifold of \(p\) and stable one-manifold of \(q\) agree along \(w=0\), and persist smoothly for \(\alpha\) near one. Their transverse intersections with a section \(v=v_0\) depend at least twice continuously differentiably on \(\alpha\), by the smooth parameter-dependent stable-manifold theorem plus a finite number of smooth forward or backward iterates. The common unperturbed branch has tangent \((du,dv)=(1,1)\), transverse to the vertical section.

**2. Variational forcing.** Put \(\delta=\alpha-1\) and differentiate the **exact** \(w\)-recurrence at \(\delta=0\) along either invariant-manifold branch. Crucially, \(\partial_v(\sin v-\sin(v+w))|_{w=0}=0\), so the first-order motion in \(v\) does not enter the transverse recurrence. Writing \(W_j=\partial_\delta w_j|_{\delta=0}\), one obtains

\[
W_{j+1}=(1-h\cos v_j)W_j-h\sin v_j=a_jW_j-h\sin v_j.
\]

For the unstable branch, its orbit converges to the parameter-independent fixed point \(p\) in backward time; the bounded particular solution with \(W_j\to0\) as \(j\to-\infty\) is

\[
W^{\mathrm u}_0=-h\sum_{j=-\infty}^{-1}\sin v_j\prod_{k=j+1}^{-1}a_k<0.
\]

For the stable branch, the orbit converges to the parameter-independent fixed point \(q\) in forward time; the unique particular solution with \(W_j\to0\) as \(j\to+\infty\) is

\[
W^{\mathrm s}_0=h\sum_{j=0}^\infty\frac{\sin v_j}{\prod_{k=0}^{j}a_k}>0.
\]

The endpoint decay condition here describes the **parameter derivative of each invariant-manifold graph** at a fixed section; it does not require the same parameterized orbit to pass through the unperturbed iterates when \(\delta\ne0\). Their longitudinal first-order shifts cancel out of the displayed normal recurrence because the unperturbed normal vector field is identically zero along the invariant arc.

**3. Absolute convergence and positivity.** Since \(0<h<1/2\), every \(a_j\) lies in \((1-h,1+h)\). The backward product contains \(-j-1\) factors tending to \(1-h<1\) as \(j\to-\infty\), and the forward denominator contains \(j+1\) factors tending to \(1+h>1\) as \(j\to\infty\). Hence the products are bounded by corresponding geometric sequences after a finite number of factors. Combined with bounded \(\sin v_j\), both series converge absolutely. In fact all their terms are positive, and so \(W_0^{\mathrm u}<0<W_0^{\mathrm s}\).

**4. Section displacement.** The transverse variable is \(w=u-v-\pi\). At fixed \(v=v_0\), \(\partial_\alpha u=\partial_\alpha w\). Taylor expansion of the two smooth manifold-section functions around \(\alpha=1\) gives their difference with coefficient \(W^{\mathrm s}_0-W^{\mathrm u}_0=M_h(v_0)>0\), as claimed. For every chosen \(h,v_0\), strict positivity dominates the quadratic remainder for sufficiently small nonzero \(\alpha-1\). The sign reverses with the sign of \(\alpha-1\), proving local splitting and its orientation.

## Verification

A standalone executable `verify.py` checks the matrix reduction algebra, endpoint hyperbolicity, forward/inverse scalar monotonicity, convergence of the truncated bilateral Melnikov sums, and the sign of the predicted branch displacement. It computes, for example, \(M_{0.1}(\pi/2)\approx1.20038789815\), with separate stable and unstable contributions both strictly positive. These are finite diagnostics. Absolute convergence, the infinite identity and strict signs follow from the proof above, not from finite truncation.

## Relationship to prior work

Buescu, D’Aniello and Oliveira (2026), Propositions 5.11–5.12 and their Figure 3, establish the exactly coincident heteroclinic arc and the nontransverse tangent spaces at **unit weights**; their weighted results elsewhere concern Morse–Smale sufficient conditions, not the central-edge splitting of this double-star connection. The present statement is a first-order, sign-definite unfolding of **that same identified obstruction**, not a new claim that the obstruction exists at unit weight. Melnikov-type separatrix displacement is a standard method: Lomelí and Ramírez-Ros (2008) study discrete Melnikov splitting for a different, three-dimensional volume-preserving setting. The signed coefficient here and its noncancellation for every permitted \(h\) come from this specific gradient network and do not follow merely from naming the general method.

## Limitations

The theorem does not claim the full five-dimensional stable and unstable manifolds become transverse, nor the absence of other heteroclinic connections elsewhere. Its scope is local on the leaf-symmetric invariant two-torus near fixed interior points of one branch. There is no explicit uniform width in the detuning parameter, and no assertion of global Morse–Smale dynamics. Priority against all unindexed literature has not been independently established. The proof uses standard parameter-dependent stable-manifold smoothness for hyperbolic diffeomorphisms and does not supply an alternative constructive proof of that classical theorem.

## References

- J. Buescu, E. D’Aniello, H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks* (2026), arXiv:2610.10993v1, §§2, 3, 5.4, especially Propositions 5.11–5.12. Publicly available 2026-10-07. https://arxiv.org/pdf/2610.10993
- H. E. Lomelí and R. Ramírez-Ros, *Separatrix Splitting in 3D Volume-Preserving Maps*, SIAM Journal on Applied Dynamical Systems (2008), DOI:10.1137/080713173. General method comparison only; different setting. https://doi.org/10.1137/080713173
