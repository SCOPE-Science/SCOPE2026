# Two simultaneous periodic cylinders in a nilpotent-Jacobian polynomial flow

## Finding

For every real \(r>0\) and \(K\geq 3r/2\), the polynomial differential equation
\[
\begin{split}
\dot x&=(y+x^2)^2-K,\\
\dot y&=z-2x((y+x^2)^2-K),\\
\dot z&=((y+x^2)^2-K)^2-r^2
\end{split}\tag{1}
\]
on \(\mathbb R^3\) has **an everywhere-nilpotent Jacobian**, **no equilibrium**, and **at least two distinct, disjoint invariant cylinders**, each completely foliated by nonconstant periodic orbits of a common (cylinder-dependent) minimal period in the original physical time. The two cylinders lie on Hamiltonian-energy levels with strictly opposite signs. In particular a single nilpotent-Jacobian polynomial vector field can support two separate isochronous periodic surfaces, not merely two planar period annuli.

Let
\[
g(v)=v^2-K,\qquad U(v)=-\frac{v^5}{5}+\frac{2K}{3}v^3+(r^2-K^2)v,\qquad H(v,w)=\frac{w^2}{2}+U(v),
\]
and set \(a=\sqrt{K-r}\), \(b=\sqrt{K+r}\). There are two disjoint families of compact regular Hamiltonian ovals: \(\Gamma_L(E)\) surrounding \((-b,0)\) for \(U(-b)<E<U(-a)\), and \(\Gamma_R(E)\) surrounding \((a,0)\) for \(U(a)<E<U(b)\). Denote their original-time periods by \(T_L(E)\) and \(T_R(E)\), and write their axial one-period translations as
\[
D_j(E)=\int_0^{T_j(E)}g(v_j(t))\,dt,\qquad j\in\{L,R\}.
\]
Then \(D_L\) and \(D_R\) are continuous and have respective opposite-sign limiting *time averages*:
\[
\begin{array}{lll}
\displaystyle\lim_{E\downarrow U(-b)}D_L(E)/T_L(E)=r,&
\displaystyle\lim_{E\uparrow U(-a)}D_L(E)/T_L(E)=-r,\\[2mm]
\displaystyle\lim_{E\downarrow U(a)}D_R(E)/T_R(E)=-r,&
\displaystyle\lim_{E\uparrow U(b)}D_R(E)/T_R(E)=r.
\end{array}\tag{2}
\]
Therefore there are interior energies \(E_L^*>0>E_R^*\) with \(D_L(E_L^*)=D_R(E_R^*)=0\). The claimed cylinders are the inverse images, under the global polynomial change of coordinates below, of \(\mathbb R\times\Gamma_L(E_L^*)\) and \(\mathbb R\times\Gamma_R(E_R^*)\). No uniqueness or exact count of such cylinders is asserted.

## Assumptions and scope

The parameters satisfy exactly \(r>0\), \(K\ge3r/2\). There is no small-parameter restriction, genericity hypothesis, time reparametrization or bounded-domain truncation. A *periodic cylinder* means a smooth invariant surface diffeomorphic to \(\mathbb R\times S^1\) whose every orbit is periodic; *isochronous* here means all trajectories on an individual cylinder have the same minimal period. The two cylinders may have different periods. The asserted two-cylinder existence is not a classification of all compact invariant sets or of all possible cylinders. The parameter inequality is a sufficient range, not a claimed optimal threshold. Initial conditions lying on the two cylinders are complete for all real time; no global completeness claim is made for other initial conditions.

## Proof

**1. Polynomial integrability and nilpotence.** Put \(s=y+x^2\), \(g=s^2-K\), and introduce the global polynomial diffeomorphism
\[
(u,v,w)=(x,y+x^2,z),\qquad (x,y,z)=(u,v-u^2,w).
\]
Along (1), without altering time,
\[
\dot u=v^2-K,\qquad \dot v=w,\qquad \dot w=(v^2-K)^2-r^2.\tag{3}
\]
Consequently \(dH/dt=w\bigl(U'(v)+(v^2-K)^2-r^2\bigr)=0\), because \(U'(v)=r^2-(v^2-K)^2\).

For completeness, let \(g_s=2s\). Direct differentiation of the **original** vector field (1) gives
\[
J=\begin{pmatrix}
2xg_s &g_s&0\\
-2g-4x^2g_s&-2xg_s&1\\
4xgg_s&2gg_s&0
\end{pmatrix}.
\]
Its trace, trace of its square and determinant are identically zero. Its characteristic polynomial is therefore \(\lambda^3\), so Cayley–Hamilton gives \(J^3=0\) at every state. (The nonlinear conjugacy alone would not imply nilpotence, which is why it is checked in the original coordinates.) If \(\dot x=0\), then \(g=0\), but \(\dot z=-r^2<0\); hence the vector field has no equilibrium.

**2. Two disjoint projected centers and their annuli.** The planar subsystem of (3) is the one-degree-of-freedom Hamiltonian system \(\dot v=w\), \(\dot w=-U'(v)\), with
\[
U'(v)=r^2-(v^2-K)^2.
\]
Its four simple critical points, in increasing order, are \(-b,-a,a,b\). The points \(-b,a\) are strict local minima and hence centers; \(-a,b\) are strict local maxima and hence hyperbolic saddles. Evaluation gives
\[
U(b)=\frac4{15}(K+r)^{3/2}(3r-2K)\le0,
\qquad
U(-a)=\frac4{15}(K-r)^{3/2}(2K+3r)>0.
\]
Since \(U\) is odd, \(U(-b)=-U(b)\ge0\) and \(U(a)=-U(-a)<0\). Thus each center has its ordinary family of compact regular ovals below its adjacent saddle energy; all left-family energies are positive and all right-family energies are negative. Their oval families are disjoint even at \(K=3r/2\). The open energy intervals displayed in Finding are nonempty, because the critical points alternate strictly between minimum and maximum.

**3. Axial drift at a center.** For a fixed family of regular ovals, the period \(T_j(E)>0\) and displacement \(D_j(E)\) vary continuously with energy, by smooth dependence of planar trajectories and a transverse section. As an oval shrinks to its nondegenerate center \(v_c\), the position \(v(t)\) converges uniformly to \(v_c\); hence its average of the continuous observable \(g(v)\) tends to \(g(v_c)\). At the left center \(v_c=-b\), the value is \(r\), and at the right center \(v_c=a\), it is \(-r\).

**4. Axial drift at a separatrix.** At the outer boundary of the left annulus the oval approaches the homoclinic separatrix of the nondegenerate saddle \((-a,0)\); at the outer boundary of the right annulus it approaches that of \((b,0)\). For any small fixed neighborhood of the saddle on the separatrix, the period spent *outside* the neighborhood stays bounded as \(E\) approaches the saddle energy, whereas the time spent *inside* tends to infinity. This follows either from the standard hyperbolic saddle normal form, or directly from the period integral \(\sqrt2\int(dv)/\sqrt{E-U(v)}\) and the local expansion
\[
U(v)=U(v_s)-\tfrac12|U''(v_s)|(v-v_s)^2+O((v-v_s)^3).
\]
More explicitly, for each fixed neighborhood radius \(\varepsilon>0\), the period outside it is uniformly bounded, and the total period diverges logarithmically. Uniform continuity of \(g\) on the neighborhood then bounds the deviation of its full-time average from \(g(v_s)\) by \(\sup_{|v-v_s|<\varepsilon}|g(v)-g(v_s)|+o(1)\); let the energy approach the boundary and then \(\varepsilon\downarrow0\). This yields the saddle limits in (2): \(g(-a)=-r\), \(g(b)=r\).

**5. Periodic-surface conclusion.** The two drift averages are continuous and change sign on their respective annuli. Since periods are finite and positive at every interior energy, the intermediate-value theorem gives an interior zero of \(D_j(E)\) in each annulus. On \(\mathbb R_u\times\Gamma_j(E)\), a planar revolution changes \(u\) by exactly \(D_j(E)\), independent of the starting axial coordinate and orbital phase. At a zero-drift energy every lifted point returns after exactly one minimal planar period. A shorter lift period is impossible because its planar projection already has minimal period \(T_j(E)\). Both surfaces are smooth invariant cylinders foliated by original-time periodic trajectories; their disjointness follows from the strict sign separation of their conserved energies. Their polynomial inverse images under the displayed diffeomorphism prove the assertion for (1).

## Verification

The standalone `verify.py` and `requirements.txt` reproduce symbolic checks of \(J^3=0\), the polynomial conjugacy, conservation of \(H\), and the critical-energy formulas. They also compute two zero-drift energies numerically for each of three parameter pairs, always in distinct energy intervals. For the representative \(K=2\), \(r=1\), quadrature gives \(E_L^*\approx1.86179856938\) and \(E_R^*\approx-1.38578729983\), with respective periods approximately \(4.58899752409\) and \(6.15926848010\). Run `python verify.py` in the extracted directory after installing the dependencies. Root and quadrature numerics are **not** exhaustive and are not used to prove the existence for arbitrary parameters; Steps 1–5 constitute the proof.

## Relationship to prior work

Castañeda and Rebollo-Perdomo (arXiv:2209.06986v1, 2022), in their formula (9), obtain the general skew flow \(\dot u=P_1(v)\), \(\dot v=P_2(w)\), \(\dot w=a_{12}P_1(v)^2+A_3\) (for linear unit-leading \(P_2\)). The present family is the concrete subfamily \(P_1(v)=v^2-K\), \(P_2(w)=w\), \(a_{12}=1\), \(A_3=-r^2\). Their Proposition 1.3 establishes **one** periodic cylinder for the linear-\(P_1\) case. Their closing Section 5 exhibits a quadratic-\(P_1\) example with **two planar period annuli**, and explicitly asks how many *three-dimensional periodic surfaces* there can be. Merely having two planar annuli does not imply the two axial return translations vanish. The new assertion proves simultaneous zero drift on **both** wells in a full two-parameter region, producing two bona fide periodic cylinders, while preserving the nilpotent Jacobian in original coordinates.

A separately retrieved result, *Periodic cylinders and two-end algebraic period laws in even-kinetic skew flows*, studies a different higher-even-kinetic skew flow with just one projected annulus and explicitly no globally nilpotent Jacobian. It neither contains this two-well quadratic example nor implies the simultaneous nilpotent-flow existence. Standard Hamiltonian phase-portrait and hyperbolic-saddle time-average facts are used as proof ingredients, not claimed as original.

## Limitations

The proof guarantees at least two periodic cylinders, without excluding further zero-drift levels or establishing uniqueness within either annulus. The constraint \(K\ge3r/2\) ensures separate signed energy intervals and is not asserted to be necessary. The theorem does not assert stability, attraction, persistence under damping, or completeness of trajectories on noncompact planar-energy components. The 2022 arXiv full text was inspected and the original 2024 journal abstract identified; the later publisher full text was not read. Broader or unindexed results could imply simultaneous existence and therefore remain a priority risk. Independent external mathematical validation has not been performed.

## References

1. Álvaro Castañeda and Salomón Rebollo-Perdomo, *Discrete and continuous dynamics of real 3-dimensional nilpotent polynomial vector fields*, arXiv:2209.06986v1 (first posted 2022-09-15), especially formula (9), Proposition 1.3, and Section 5, https://arxiv.org/pdf/2209.06986 . Later journal version: *Archiv der Mathematik* 124 (2025), 415–434, DOI: 10.1007/s00013-024-02085-8 .
2. *Periodic cylinders and two-end algebraic period laws in even-kinetic skew flows*, retrieved mathematical result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-periodic-cylinders-and-two-end-algebraic-period-laws-in-even-kin--39357bc9e312 .
