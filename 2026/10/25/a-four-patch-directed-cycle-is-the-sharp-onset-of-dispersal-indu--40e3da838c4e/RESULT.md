# A four-patch directed cycle is the sharp onset of dispersal-induced rotating instability

## Finding

**Theorem (first delay instability in lossy cyclic logistic patches).** Let \(n\in\{2,3,4\}\), \(d>0\), \(\eta>0\), \(r>\eta d\) and \(\tau\ge0\). In the directed cyclic delayed population model defined below, the strictly positive spatially uniform equilibrium is unique. Put \(K=r-\eta d\), \(q=d/K\), and \(\tau_{\mathrm{syn}}=\pi/(2K)\).

For two or three patches the equilibrium is exponentially linearly stable for \(0\le\tau<\tau_{\mathrm{syn}}\) and linearly unstable for \(\tau>\tau_{\mathrm{syn}}\). Its first critical eigenspace is spatially uniform.

For four patches, let \(t_*\) be the unique solution in \((0,\pi/2)\) of
\[
\frac\pi2(\sin t+\cos t-1)=t,
\qquad q_*:=\sin t_*=0.5814567017105\ldots.
\]
If \(0<q<q_*\), the first critical delay is **strictly below** the uniform one and is exactly
\[
\tau_{\mathrm{rot}}(q)=\frac{\arccos(-q)}{K(q+\sqrt{1-q^2})}<\frac\pi{2K}.
\]
The critical eigenvectors have successive patch phases separated by one quarter-turn. If \(q>q_*\), the first critical delay is \(\tau_{\mathrm{syn}}\), with a spatially uniform critical eigenspace. At \(q=q_*\), the rotating and synchronous imaginary eigenvalue pairs occur simultaneously at \(\tau_{\mathrm{syn}}\). In every case the equilibrium is exponentially linearly stable for all delays strictly below the specified first threshold and linearly unstable for all delays strictly above it. No assertion of nonlinear stability is made at a critical delay.

Equivalently, for a fixed mortality fraction \(\eta\) and growth \(r\), four-patch rotating instability precedes uniform instability precisely when
\[
0<d<\frac{r q_*}{1+\eta q_*}.
\]
In particular, with \(d=\eta=1/2\), \(r=5/4\) one has \(K=1\), \(q=1/2\), and
\[
\tau_{\mathrm{rot}}=\frac{4\pi}{3(1+\sqrt3)}=1.533203626075\ldots
<\tau_{\mathrm{syn}}=\frac\pi2=1.570796326795\ldots.
\]
Thus some delays admit decay of all synchronous linear perturbations while a transverse quarter-phase mode grows.

## Assumptions and scope

The state is a vector of nonnegative population densities with patch labels \(j\in\mathbb Z/n\mathbb Z\). Patches communicate one way around a directed ring. For each \(j\), define
\[
\dot u_j(t)=d\bigl(u_{j-1}(t)-(1+\eta)u_j(t)\bigr)
+u_j(t)\bigl(r-u_j(t-\tau)\bigr).
\tag{1}
\]
Here \(d\) is the dispersal rate, \(\eta d\) the per-patch migration-associated net loss rate, \(r\) the growth parameter, and \(\tau\) the maturation/competition delay. The dispersal matrix \(P-(1+\eta)I\) is irreducible, has nonnegative off-diagonal entries, and its column sums are \(-\eta<0\). This is a homogeneous logistic specialization of the lossy dispersal model of Huang and Chen [1]. For the spectral results it suffices to use the linearized retarded functional differential equation in the usual continuous-history phase space.

The equilibrium \(u_j=K=r-\eta d\) exists by substitution. At any strictly positive equilibrium, a patch achieving maximum \(M\) has \(0\le M(K-M)\), hence \(M\le K\); a patch achieving minimum \(m\) has \(0\ge m(K-m)\), hence \(m\ge K\). Thus \(m=M=K\). This proves uniqueness among strictly positive equilibria. The zero equilibrium and possible boundary histories are not the subject of the theorem.

## Proof

**1. Modal reduction and stability at zero delay.** Write \(u_j=K+v_j\). Since the derivative of \(u_j(r-u_j(t-\tau))\) at equilibrium is \((r-K)v_j-Kv_j(t-\tau)=\eta d v_j-Kv_j(t-\tau)\), the exact linearization simplifies to
\[
\dot v_j(t)=d(v_{j-1}(t)-v_j(t))-Kv_j(t-\tau).
\tag{2}
\]
The cyclic shift has distinct roots of unity \(\zeta\) for \(n=2,3,4\). Each Fourier component satisfies
\[
\lambda=d(\zeta-1)-Ke^{-\lambda\tau}.
\tag{3}
\]
With \(z=\lambda/K\), \(s=K\tau\), and \(q=d/K\), write \(q(\zeta-1)=-A+iB\) with \(A\ge0\). Complex conjugation allows \(B\ge0\) for counting first positive delays. The scalar factors are
\[
z=-A+iB-e^{-zs}.
\tag{4}
\]
At \(s=0\), every root is \(z=-1-A+iB\), hence has negative real part. If \(\Re z\ge0\) then \(|z+A-iB|=e^{-s\Re z}\le1\), so roots cannot enter the closed right half-plane from infinity as finite \(s\) varies. Therefore first loss of exponential stability must occur at a nonzero imaginary root of (4), whose crossing can be checked directly.

**2. First imaginary crossings.** Substituting \(z=i\omega\) gives
\[
 e^{-i\omega s}=-A+i(B-\omega),
 \qquad (B-\omega)^2=1-A^2.
\tag{5}
\]
If \(A>1\), there is no imaginary root. For \(0\le A<1\), set \(R=\sqrt{1-A^2}\) and \(\Theta=\arccos(-A)\in[\pi/2,\pi)\). The branch \(\omega_+=B+R>0\) has its earliest positive delay at
\[
 s_+(A,B)=\frac\Theta{B+R}.
\tag{6}
\]
The other branch \(\omega_-=B-R\) cannot yield a smaller positive delay: if \(0<\omega_-\), its first positive delay is \((2\pi-\Theta)/\omega_-\); if \(\omega_-<0\), its first positive delay is \(\Theta/|\omega_-|\). The delay is strictly larger than (6) whenever \(B>0\), using \(\Theta<\pi\), \(B+R>|B-R|\), and \(2\pi-\Theta>\Theta\). If \(B=0\), both branches have the same first delay, as required by conjugate scalar roots. A zero frequency cannot solve (4), because substituting \(z=0\) gives \(0=-A+iB-1\), impossible with \(A\ge0\). At \(A=1,B>0\) the two frequency branches coincide at \(\omega=B\), with first possible delay \(s=\pi/B\). For real modes with \(B=0,A=1\), no imaginary root exists at any finite delay.

At a positive-frequency crossing of (6) with \(0\le A<1\), implicit differentiation of (4) gives
\[
 \frac{dz}{ds}=\frac{ze^{-zs}}{1-se^{-zs}},\quad
 \Re\frac{dz}{ds}=
 \frac{(B+R)R}{(1+sA)^2+s^2R^2}>0.
\tag{7}
\]
Thus these crossings strictly destabilize. For the negative-frequency branch when \(B<R\), its crossings also go to the right (the same calculation gives positive real derivative because both its frequency and its sine factor are negative).

**3. Two patches.** The nonuniform mode has \(\zeta=-1\), so \((A,B)=(2q,0)\). If \(2q\ge1\), it never has a finite imaginary-axis crossing. Otherwise (6) gives \(s_+=\arccos(-2q)/\sqrt{1-4q^2}>\pi/2\). The uniform mode \(\zeta=1\) first crosses at \(s=\pi/2\).

**4. Three patches.** The nonuniform complex mode has \((A,B)=(3q/2,\sqrt3q/2)\). If \(q>2/3\), there is no imaginary crossing; at \(q=2/3\) its crossing is later than \(\pi/2\). For \(0<q\le2/3\), put \(t=\arcsin(3q/2)\). Formula (6) yields
\[
s_3(t)=\frac{\pi/2+t}{\cos t+(\sin t)/\sqrt3}.
\tag{8}
\]
The inequality \(s_3(t)>\pi/2\) is equivalent to \(G(t)>0\), where
\[
G(t)=\pi/2+t-(\pi/2)(\cos t+\sin t/\sqrt3).
\]
Here \(G(0)=0\), \(G'(0)=1-\pi/(2\sqrt3)>0\), and \(G''(t)=(\pi/2)(\cos t+\sin t/\sqrt3)>0\) on \((0,\pi/2)\). Hence no three-patch transverse mode precedes synchronization.

**5. Four patches.** The two nonuniform types are \(\zeta=-1\), already excluded before \(\pi/2\) by the two-patch comparison, and \(\zeta=\pm i\), for which \((A,B)=(q,q)\). For \(0<q\le1\), formula (6) gives
\[
s_{\rm rot}(q)=\frac{\arccos(-q)}{q+\sqrt{1-q^2}}.
\tag{9}
\]
For \(q>1\) no rotating imaginary root exists. Put \(q=\sin t\) for \(0<t<\pi/2\). Then \(s_{\rm rot}(q)<\pi/2\) is equivalent to
\[
F(t)=(\pi/2)(\sin t+\cos t-1)-t>0.
\tag{10}
\]
We have \(F(0)=0\), \(F'(0)=\pi/2-1>0\), \(F(\pi/2)=-\pi/2<0\), and \(F''(t)=-(\pi/2)(\sin t+\cos t)<0\). Strict concavity gives exactly one root \(t_*\) in the open interval; its sign is positive before and negative afterward. The exact smallest critical delay therefore follows from (9) and the uniform \(\pi/2\) crossing.

Finally, for \(q<q_*<1/\sqrt2\), the rotating mode satisfies \(B=q<R\), so every positive-delay rotating imaginary crossing is strictly from left to right, including its negative-frequency branch by step 2; once its first crossing occurs a right-half-plane characteristic root persists for all later delays. For \(q\ge q_*\), the synchronizing scalar factor \(z=-e^{-zs}\) has only rightward crossings, all at \(s=(\pi/2+2\pi k)\) for positive frequency and the conjugates; its unstable spectrum persists after \(s=\pi/2\). At equality \(q=q_*\) both nonzero and uniform Fourier modes cross; they have different frequencies \(K(q_*+\sqrt{1-q_*^2})\) and \(K\). Equation (7) gives the strict transverse crossing because \(q_*<1\). This proves linear stability below and instability above the stated first threshold. The explicit witness follows from \(\arccos(-1/2)=2\pi/3\).

## Verification

Run `python verify.py` with Python 3 standard library. The code independently computes the strict transition bracket, checks modal imaginary characteristic residuals for the \(2\)-, \(3\)- and \(4\)-patch cases over several parameter values, verifies the crossing derivative formula and sign, and tests exact witness numerics. It is a reproducibility check only: all-parameter uniqueness of the threshold, all-delays stability and absence of earlier roots rely on the preceding analytic argument, not numerical sampling.

## Relationship to prior work

Huang and Chen [1] introduce and analyze the general lossy dispersal patch equation (their equation (2)); they investigate delay-induced Hopf phenomena at small dispersal and near a critical dispersal value, discuss topology-dependent onset, and specifically identify the intermediate-dispersal regime as challenging. The present fixed homogeneous directed-cycle specialization solves the *entire positive-equilibrium dispersal range* for first linear instability and separates spatially synchronized from rotating loss mechanisms. Their general existence and perturbative theorems do not state this sharp four-patch mode-switching threshold.

Chen, Shen and Wei [2] and Huang, Chen and Zou [3] study Hopf bifurcations for broader patch and nonlocal interactions, including limiting dispersal regimes, but do not provide the explicit all-rate first-crossing classification here. Liu, Shen and Chen [4] analyze a distinct finite **open-chain** advective network with downstream loss; its topology and onset mechanism are different. Ring-coupled Wilson–Cowan oscillators have related mode competition [5], but neural feedback and location of delays differ from local logistic maturation feedback. These connections motivate the comparison without establishing the present parameter threshold as previously known.

## Limitations

The stability assertions are **linear local** statements for the strictly positive equilibrium, not global nonlinear attractivity, extinction, periodic-orbit existence/stability, or bifurcation normal-form classification. Critical delays carry imaginary spectrum; no nonlinear stability assertion is made at equality. The sharp minimality claim refers only to the directed homogeneous cyclic family of sizes \(2\), \(3\), and \(4\), not all graphs of size below four. The novelty comparison is conditional on inspected literature and searchable records; an equivalent result may exist under another parametrization. Computed decimal values are corroborative, not certified interval endpoints.

## References

1. D. Huang and S. Chen, *Dynamics of a delayed population patch model with the dispersion matrix incorporating population loss*, arXiv:2302.01814 (first posted 2023-02-03), https://arxiv.org/abs/2302.01814.
2. S. Chen, Z. Shen, and J. Wei, *Hopf bifurcation in a delayed single population model with patch structure*, arXiv:1912.11780, https://arxiv.org/abs/1912.11780.
3. D. Huang, S. Chen, and X.-Q. Zou, *Hopf bifurcation in a delayed population model over patches with general dispersion matrix and nonlocal interactions*, Journal of Dynamics and Differential Equations, open manuscript https://www.uwo.ca/apmaths/faculty/zou/repr/jdde21.pdf.
4. W. Liu, Z. Shen, and S. Chen, *Hopf bifurcations for a delayed discrete single population patch model in advective environments*, European Journal of Applied Mathematics, https://doi.org/10.1017/S0956792524000342.
5. I. Pinder, M. R. Nelson, and J. J. Crofts, *Bifurcations and synchrony in a ring of delayed Wilson–Cowan oscillators*, Proc. R. Soc. A 479 (2023), https://doi.org/10.1098/rspa.2023.0313.
