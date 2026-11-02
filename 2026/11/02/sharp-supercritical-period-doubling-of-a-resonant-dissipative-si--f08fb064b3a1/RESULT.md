# Sharp supercritical period doubling of a resonant dissipative sine twist map

## Finding

For every fixed \(0<\lambda<1\), consider the analytic map of the cylinder \(\mathbb T\times\mathbb R\), with \(\mathbb T=\mathbb R/\mathbb Z\),
\[
F_{\lambda,t}(x,y)=\left(x+\frac12+y',y'\right),\qquad y'=\lambda y+\frac{t}{2\pi}\sin(2\pi x),\quad t>0.
\]
Its Jacobian determinant is \(\lambda\), so it is conformally symplectic. The orbit \((0,0)\leftrightarrow(1/2,0)\) has prime period two for every \(t\). It is exponentially attracting precisely for
\[
0<t<t_c(\lambda),\qquad t_c(\lambda)=\sqrt{2(1+\lambda^2)}.
\]
At \(t=t_c\), its two-step multipliers are \(-1\) and \(-\lambda^2\). For each fixed \(\lambda\) and sufficiently small \(\mu=t-t_c>0\), a unique nearby prime-period-four orbit bifurcates and is exponentially attracting. No such nearby orbit is present for sufficiently small \(\mu<0\).

Put \(a=1+\lambda\), \(b=1-\lambda\), and \(k=2\pi\). The new orbit, in chronological order, is
\[
(u,u+v),\quad (1/2+v,v-u),\quad (-u,-u-v),\quad (1/2-v,u-v),
\]
with angular coordinates modulo one, where \(u,v>0\) are the unique small positive solution of
\[
\frac{t}{k}\sin(ku)=-au+bv,\qquad
\frac{t}{k}\sin(kv)=bu+av.
\]
The leading amplitude and nontrivial four-step multiplier are explicit:
\[
\begin{pmatrix}u\\v\end{pmatrix}=
\sqrt{\frac{6\mu}{k^2(t_c^2+a^2)(t_c+a)}}
\begin{pmatrix}b\\t_c+a\end{pmatrix}
+O_\lambda(\mu^{3/2}),
\]
\[
\nu_{\mathrm{critical}}=1-\frac{8t_c}{1-\lambda^2}\mu+O_\lambda(\mu^2).
\]
The other four-step multiplier is \(\lambda^4+O_\lambda(\mu)\). All asymptotic statements hold with \(\lambda\) fixed strictly between zero and one; no uniformity as \(\lambda\uparrow1\) is asserted.

## Assumptions and scope

The angular coordinate is considered modulo one and the momentum coordinate lies in \(\mathbb R\). The map is invertible for \(\lambda>0\). Only the exact half-turn orbit and its sufficiently small local bifurcation are classified. "Unique nearby" refers to one geometric orbit (four distinct points), not to one distinguished cyclic starting point. Stability refers to the full two-dimensional derivative, not to an artificially imposed symmetry subspace.

## Proof

**Exact two-cycle spectrum.** At the first and second points the Jacobians are respectively
\[
J_+=\begin{pmatrix}1+t&\lambda\\t&\lambda\end{pmatrix},\qquad
J_-=\begin{pmatrix}1-t&\lambda\\-t&\lambda\end{pmatrix}.
\]
Their product \(A=J_-J_+\) has \(\det A=\lambda^2\) and \(\operatorname{tr}A=1+\lambda^2-t^2\). For \(0<\lambda<1\), the two-dimensional strict Schur inequalities are \(1-\operatorname{tr}A+\det A=t^2>0\) and \(1+\operatorname{tr}A+\det A=2(1+\lambda^2)-t^2>0\); \(1-\det A>0\) is automatic. This gives the sharp threshold and at equality the roots \(-1,-\lambda^2\). The critical root crosses outwards because its derivative with respect to \(t\) at \(t_c\) is \(-2t_c/(1-\lambda^2)<0\).

**Exact orbit equations and their symmetry.** The map satisfies \(F(-x,-y)=-F(x,y)\) on the cylinder after interpreting the angular half-turn modulo one. Starting from \((u,u+v)\), requiring its first image to be \((1/2+v,v-u)\) gives the first sine equation; requiring its next image to be \((-u,-u-v)\) gives the second. Odd symmetry supplies the final two steps. Conversely, a small solution of these two equations generates the stated orbit. In particular, \(u,v\ne0\) implies four distinct points for sufficiently small amplitudes.

**Nondegenerate bifurcating branch.** Define
\[
E(u,v;t)=\left(\frac tk\sin(ku)+au-bv,\ \frac tk\sin(kv)-bu-av\right).
\]
At the origin its symmetric Jacobian is
\[
M(t)=\begin{pmatrix}t+a&-b\\-b&t-a\end{pmatrix},\quad
\det M(t)=t^2-t_c^2.
\]
At \(t_c\), the kernel is spanned by \(w=(b,t_c+a)\); the complementary eigenvalue is \(2t_c>0\). Write \(z=s w+z_\perp\) and use the analytic implicit function theorem on the complementary equation, obtaining \(z_\perp=O(s^3+|\mu s|)\). Projection of \(E=0\) onto \(w\) gives
\[
0=\mu s\|w\|^2-\frac{t_c k^2}{6}s^3(w_1^4+w_2^4)
+O(|\mu|^2|s|+|\mu||s|^3+|s|^5).
\]
The exact identities \(\|w\|^2=2t_c(t_c+a)\) and \(w_1^4+w_2^4=2(t_c^2+a^2)(t_c+a)^2\) show that the nontrivial roots are \(s=\pm\sqrt{6\mu/[k^2(t_c^2+a^2)(t_c+a)]}+O(\mu^{3/2})\) for \(\mu>0\), and no small nonzero roots for \(\mu<0\). The two roots correspond to the same four-point orbit, shifted by two steps. The simple multiplier \(-1\), its transverse crossing, and this nonzero cubic term are the standard nondegeneracy conditions for the local flip of \(F^2\); the local period-doubling theorem excludes other nearby prime-period-four branches.

**Full-space attraction and sharp response.** At the two consecutive points of the new four-cycle the two-step derivative has factors \(J_+(t\cos ku)\) and \(J_-(t\cos kv)\), where \(J_+(r)=[[1+r,\lambda],[r,\lambda]]\) and \(J_-(r)=[[1-r,\lambda],[-r,\lambda]]\). Its determinant is \(\lambda^2\), while its trace is
\[
1+\lambda^2-t^2\cos(ku)\cos(kv)
+a t[\cos(ku)-\cos(kv)].
\]
Inserting the amplitude formula and using the kernel identities gives
\[
\operatorname{tr}D(F^2)=-(1+\lambda^2)+4t_c\mu+O_\lambda(\mu^2).
\]
For fixed \(\lambda<1\), the root near \(-1\) is therefore \(-1+[4t_c/(1-\lambda^2)]\mu+O_\lambda(\mu^2)\), while the other is near \(-\lambda^2\). The second half of the four-orbit has the same two-step derivative by odd symmetry; hence the four-step return derivative is the square of the two-step derivative and has the stated multipliers. Both are strictly inside the unit disk when \(\mu>0\) is sufficiently small.

## Verification

The file `verify.py` uses only the Python standard library. Run `python3 verify.py` to reproduce Newton solutions of the two exact sine equations, exact one-step orbit identities, the analytical two-cycle threshold, the nonzero four-cycle, the Jacobian determinant, and asymptotic amplitude/trace estimates at multiple damping parameters. These finite checks corroborate the proof; the quantified statements for all \(\lambda\in(0,1)\) are derived analytically above.

## Relationship to prior work

Arnaud's 2026 treatment establishes the conformally symplectic setting and discusses attractors and invariant manifolds, but does not derive this half-turn branch's threshold or the explicit period-four amplitude. The broader standard-map period-doubling literature (Murakami et al., 2001) studies conservative accelerator-mode and fixed-orbit scaling rather than the present uniformly dissipative return spectrum. General smooth-map flip theory (Glendinning and Simpson, 2023) guarantees qualitative branches under nondegeneracy but does not imply the parameter-dependent threshold, exact sine orbit equations, or coefficients without new calculation. Work on periodic trajectories of dissipative standard maps (Wenzel, Biham, and Jayaprakash, 1991; Celletti and Di Ruzza, 2011) is especially relevant historical prior work; their complete articles were not available for a decisive priority comparison. Novelty is therefore conditional on the inspected literature and not a claim of independently established historical priority.

## Limitations

This is local in parameter \(t-t_c\), except for the global-in-\(t\) stability classification of the distinguished two-cycle. It does not classify all periodic points, all attractors, or global basins. It does not give a uniform neighborhood as \(\lambda\to0\) or \(\lambda\to1\), and it does not assert anything about the conservative endpoint \(\lambda=1\). The inaccessible historical primary studies remain a specific originality risk.

## References

- M.-C. Arnaud, *Conformally symplectic Dynamics* (first public 2026-02-28), arXiv:2603.00758, https://arxiv.org/abs/2603.00758.
- C. Murakami, W. Murakami, K.-I. Hirose, Y. H. Ichikawa, *Global Period-Doubling Bifurcation in the Standard Map*, Prog. Theor. Phys. 106 (2001), 909–915, https://doi.org/10.1143/PTP.106.909.
- P. A. Glendinning and D. J. W. Simpson, *Normal Forms, Differentiable Conjugacies, and Elementary Bifurcations of Maps*, SIAM J. Appl. Math. 83 (2023), 816–836, https://doi.org/10.1137/22M1503701.
- W. Wenzel, O. Biham, J. Jayaprakash, *Periodic Orbits in the Dissipative Standard Map*, Phys. Rev. A 43 (1991), 6550–6567.
- A. Celletti and S. Di Ruzza, *Periodic and quasi-periodic orbits of a dissipative twist map*, DCDS-B 16 (2011), 151–167, https://doi.org/10.3934/dcdsb.2011.16.151.
