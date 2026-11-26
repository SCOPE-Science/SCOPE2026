# A dimension-free sharp-exponent concentration modulus for complex quadratic polynomials on c-zero

## Finding

The optimal uniform power of the finite-coordinate norm deficit is **one half**, and the obstruction already uses two retained and one discarded coordinate. Let \(P:c_0(\mathbb N;\mathbb C)\to\mathbb C\) be a continuous two-homogeneous polynomial of norm one, let \(F\) be a finite nonempty coordinate set, and let \(P_F=P\circ\pi_F\), where \(\pi_F\) keeps the coordinates in \(F\) and zeros the others. Write \(\delta=1-\|P_F\|\), with all norms taken on the supremum-norm unit ball. The argument of Dantas and Rodríguez gives the uniform bound \(\|P-P_F\|\le 8\sqrt\delta+\delta\) by direct specialization to \(c_0\). No dimension-free bound \(C\delta^p\) with \(p>1/2\) holds, even if \(P\) depends on only three coordinates and \(|F|=2\). In contrast, when \(|F|=1\) the uniform linear estimate \(\|P-P_F\|\le 3\delta\) holds even with arbitrarily many discarded coordinates. The leading constant in a square-root bound is not determined.

## Proof

**Background upper bound (specialization of prior work).** On disjoint supports write
\[
P(u+v)=A(u)+L_v(u)+C(v),\qquad L_v(u)=2B(u,v),
\]
where \(B\) is the symmetric bilinear form of \(P\). For \(\|u\|_\infty,\|v\|_\infty\le1\), taking the average at \(u+tv\) and \(u-tv\) for \(|t|=1\) and optimizing the phase yields \(|A(u)|+|C(v)|\le1\). Pick a maximizer \(x\) on the finite polytorus and multiply \(P\) by a unimodular scalar so that \(A(x)=1-\delta\); then \(\|C\|\le\delta\).

Use the tangential signs of Dantas and Rodríguez (Theorem 3.4, proof before taking the limit). For each \(v\) in the discarded unit ball, write \(L_v(u)=\sum l_j u_j\) and pick \(w_j=i\epsilon_j x_j\) with \(\epsilon_j\in\{-1,1\}\) so that \(|L_v(w)|\ge \tfrac12\sum |l_j|\). Indeed, the best signs applied to either the real or the imaginary parts of \(il_jx_j\) attain at least half the sum of their moduli. For \(s>0\), both vectors \(x\pm(s w+\mu v)\) have norm \(\sqrt{1+s^2}\) when \(|\mu|=1\). Choose \(\mu L_v(w)=|L_v(w)|\). Averaging the two evaluations, taking real parts and using \(|P(w)|\le1\), \(|P(\mu v)|\le\delta\) gives
\[
1+s^2\;\ge\; (1-\delta)-s^2+s|L_v(w)|-\delta .
\]
Thus \(s\|L_v\|\le4\delta+4s^2\). Take \(s=\sqrt\delta\) for positive deficit, or let \(s\downarrow0\) when \(\delta=0\). Adding the pure discarded bound proves the claimed upper estimate. This quantitative consequence is included to give context for the lower obstruction, not claimed as a new upper estimate.

**Three-coordinate obstruction.** For \(b>0\) put
\[
R_b(z)=\tfrac12 z_1(z_1+z_2)+b(z_1-z_2)z_3,\quad D_b=\sqrt{1+4b^2},\quad P_b=R_b/D_b,\quad F=\{1,2\}.
\]
On the distinguished boundary of the tridisk, choose the phase of \(z_3\) to add the two terms in modulus. As the relative phase of \(z_1,z_2\) varies, the resulting objective is \(\cos\theta+2b\sin\theta\) for \(0\le\theta\le\pi/2\). Its maximum, attained at \(\tan\theta=2b\), is \(D_b\); by the maximum-modulus principle this is the full norm. Consequently \(\|P_b\|=1\), \(\|(P_b)_F\|=1/D_b\), and \(\|P_b-(P_b)_F\|=2b/D_b\). For \(\delta_b=1-1/D_b\), the exact identity is
\[
\frac{\|P_b-(P_b)_F\|^2}{\delta_b}=1+\frac1{D_b}\longrightarrow 2\qquad (b\downarrow0).
\]
Thus a larger power of the deficit is impossible because \(\delta_b\downarrow0\) and the ratio to \(\sqrt{\delta_b}\) tends to \(\sqrt2\).

**One retained coordinate.** For \(|F|=1\), take a unit vector \(x\) supported in \(F\). Then \(|A(x)|=1-\delta\) and \(\|L_v\|=|L_v(x)|\) for every \(v\). Schwarz–Pick at the origin for the disk map \(t\mapsto P(x+tv)\) gives \(|L_v(x)|\le 1-(1-\delta)^2\) (the boundary-value case is constant). Adding \(\|C\|\le\delta\) yields \(3\delta-\delta^2\le3\delta\). Thus two retained coordinates are necessary for the square-root obstruction; one discarded coordinate is necessary for a nonzero error.

## Prior work and scope

Dantas and Rodríguez, [*Concentration theorems for 2-homogeneous polynomials and bilinear forms with applications to the Kadec–Klee properties*](https://arxiv.org/abs/2608.00780), Theorem 3.4 and proof on pp. 9–12, state qualitative uniform concentration on a broader class of complex sequence lattices. Their pre-limit tangential argument on \(c_0\) already yields the above rate bound by optimizing \(s\). Their §6 optimality statements concern scalar field, degree and lattice assumptions, not the deficit exponent. Dantas, Jung, Mazzitelli and Rodríguez, [arXiv:2209.01767](https://arxiv.org/abs/2209.01767), Proposition 4.6, establish point-dependent qualitative localization in a related Hilbert-valued setting. The contribution here is the exact three-coordinate obstruction to any higher exponent and the contrast with retaining a single coordinate, not the previously obtainable upper rate. Historical priority is limited to the literature inspected.

The proof is for complex scalar-valued quadratic polynomials. It does not give the optimal prefactor or assert the same result for other scalar fields, degrees or target spaces. The check in `checker.py` illustrates the exact obstruction on rational Pythagorean data; the proof establishes the full range and the universal bounds.
