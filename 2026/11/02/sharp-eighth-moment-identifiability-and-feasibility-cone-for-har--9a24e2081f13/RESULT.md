# Sharp eighth-moment identifiability and feasibility cone for harmonically trapped switching diffusivity

## Finding

An observable position marginal can identify the two environmental diffusivities and the switching rate without observing the switching state or following individual trajectories. For the stationary model below, the **second, fourth, and eighth raw position moments** identify all three unknown positive parameters, while no collection of moments through degree seven can do so. Its attainable moment triples form the exact region
\[
u_2>0,\qquad A>0,\qquad \frac13<R<\frac1{1+2A},
\]
where
\[
A=\frac{u_4}{3u_2^2}-1,\quad B=\frac{u_8}{105u_2^4}-1-6A,\quad R=\frac{B}{3A^2}.
\]
The inverse is
\[
\gamma=a\frac{3R-1}{1-R},\qquad
c=\sqrt{\frac{2AR}{1-R}},\qquad
D_\pm=au_2(1\pm c).
\]
These inequalities are simultaneously necessary and sufficient; they are strict because the physical assumptions exclude zero contrast, instantaneous switching, and zero minimum diffusivity.

## Assumptions and scope

Fix a **known** trap relaxation rate \(a>0\). Let \(Z_t\) be an independent symmetric continuous-time Markov chain taking values \(+1,-1\) and switching from either state at rate \(\gamma>0\). Let \(B_t\) be independent standard Brownian motion. The process satisfies
\[
dX_t=-aX_t\,dt+\sqrt{2D_{Z_t}}\,dB_t,
\quad 0<D_-<D_+<\infty.
\]
We use the unique stationary law of the joint Markov process and write \(u_k=\mathbb E[X^k]\). The labels of the diffusivities are fixed by their ordering. The assertion concerns **population moments** from independent stationary snapshots, not finite-sample statistical consistency or uncertainty quantification. The relaxation rate \(a\) is known; joint recovery with unknown \(a\) is not claimed.

## Proof

**1. Stationary representation.** Couple the process to a two-sided stationary chain and Brownian motion. Exponential damping gives the stationary stochastic integral
\[
X_0=\int_{-\infty}^0 e^{as}\sqrt{2D_{Z_s}}\,dB_s.
\]
It is conditionally centered Gaussian, with conditional variance
\[
V=2\int_0^\infty e^{-2as}D_{Z_{-s}}\,ds
=u_2(1+cY),\qquad
u_2=\frac{D_++D_-}{2a},\qquad
c=\frac{D_+-D_-}{D_++D_-}\in(0,1),
\]
where \(Y=2a\int_0^\infty e^{-2as}Z_{-s}\,ds\). The joint Markov dynamics of the discounted environment have deterministic velocities \(2a(\pm1-Y)\) when the chain has state \(\pm1\). The stationary zero-flux equations give partial densities \(p_\pm(y)=(1\pm y)p(y)/2\) and
\[
\frac{d}{dy}\bigl((1-y^2)p(y)\bigr)=-\frac{\gamma}{a}y p(y).
\]
Consequently, for \(q=\gamma/(2a)>0\),
\[
p(y)=\frac{\Gamma(q+1/2)}{\sqrt\pi\,\Gamma(q)}(1-y^2)^{q-1},\qquad -1<y<1.
\]
This is the symmetric beta law transformed to \([-1,1]\). It also follows by stationarity of the telegraph input and is normalized for every \(q>0\). Exponential contraction in the initial position and irreducibility of the finite environment establish uniqueness of the joint stationary law and finiteness of all its moments.

**2. Moment identities.** For integer \(\ell\ge0\), symmetry and beta integration yield
\[
\mathbb E[Y^{2\ell}]=\frac{(1/2)_\ell}{(q+1/2)_\ell},
\qquad \mathbb E[Y^{2\ell+1}]=0.
\]
Here \((s)_\ell\) denotes a rising factorial, with its value at \(\ell=0\) equal to one. Conditioning on \(V\), for every integer \(k\ge1\),
\[
u_{2k}=(2k-1)!!\,u_2^k
\sum_{\ell=0}^{\lfloor k/2\rfloor}
{\binom{k}{2\ell}}c^{2\ell}\frac{(1/2)_\ell}{(q+1/2)_\ell}.
\]
In particular,
\[
A=\frac{c^2}{2q+1},\qquad
B=\frac{3c^4}{(2q+1)(2q+3)},\qquad
R=\frac{2q+1}{2q+3}.
\]
One also obtains \(u_6=15u_2^3(1+3A)\), with all odd moments zero.

**3. Complete inverse and feasible domain.** The map \(q\mapsto(2q+1)/(2q+3)\) is strictly increasing from \(1/3\) to \(1\). Therefore
\[
q=\frac{3R-1}{2(1-R)},\qquad
c^2=A(2q+1)=\frac{2AR}{1-R}.
\]
The conditions \(q>0\), \(A>0\), and \(0<c<1\) are precisely
\[
A>0,\qquad \frac13<R<\frac1{1+2A}.
\]
Together with \(u_2>0\), these conditions give a positive mean diffusivity, a positive switching rate, and two strictly ordered positive diffusivities through the displayed inverse. They also prove **surjectivity** onto this domain: construction with those recovered parameters realizes each candidate triple. Injectivity follows from the same explicit inverse. The upper bound automatically requires \(A<1\), so no additional inequality is necessary.

**4. Sharp minimal moment order.** Any stationary odd moment is zero. All even moments through degree six depend only on \(u_2,A\): they are \(u_2\), \(3u_2^2(1+A)\), and \(15u_2^3(1+3A)\). Fix arbitrary \(u_2>0\), \(0<A<1\); for every \(0<\gamma<a(A^{-1}-1)\), the choices
\[
c=\sqrt{A(1+\gamma/a)},\qquad
D_\pm=au_2(1\pm c)
\]
are physical and have the same moments through order seven but distinct switching rates and contrasts. Order eight restores unique recovery by step 3. No smaller maximal raw moment order suffices.

## Verification

The included dependency-free `VERIFY.py` evaluates the closed moments and an independent two-state stationary generator recurrence using exact rational arithmetic. It checks 144 positive rational parameter quadruples, in each case all even moments through order 12, plus the sixth-moment law and inversion. An exact example with \(a=1\), \(D_-=1\), \(D_+=3\), and \(\gamma=2\) has
\[
u_2=2,\qquad u_4=13,\qquad u_6=150,\qquad u_8=2541.
\]
The numerical checks do not establish the theorem for infinitely many parameters; the preceding analytic steps do.

## Relationship to prior work

Chubynsky and Slater [1] study diffusing diffusivity and non-Gaussian Brownian displacement **without harmonic confinement**. Huang and collaborators [2] establish a general **forward** Markov-modulated Ornstein–Uhlenbeck moment recursion. Their framework subsumes computation of the moments used here and is not claimed to be new. Miyaguchi, Akimoto and Yamamoto [3] study a two-state fluctuating diffusivity with primarily free-particle displacements and time-averaged observables. Zhang and Wang [4] investigate stationary Markov-switching OU densities and transforms. Wang and Wang [5] study fluctuation-diffusivity confinement, focusing in the accessible abstract on transport/ergodicity observables. The assessed result is instead the **minimal-degree inverse problem** and its sharp realizable moment cone. Comparison with incomplete source texts limits any historical-priority claim.

## Limitations

The theorem assumes symmetric environmental switching, independent white noise, a constant known harmonic relaxation rate, strictly positive unequal diffusivities, and exact stationary moments. It does not describe asymmetric environmental switching, spatially varying diffusivity, hidden correlated noise, finite-sample estimation precision, or the unknown-trap-constant inverse problem. The eighth moment may be empirically difficult to estimate. A close stationary-OU paper [4] and a 2024 confined-diffusivity article [5] could not be inspected in full; their complete results may affect historical priority. No independent scientific audit has been performed.

## References

[1] M. V. Chubynsky and G. W. Slater, *Diffusing diffusivity: A model for anomalous and anomalous yet Brownian diffusion*, arXiv:1404.3573, first posted 2014-04-14.

[2] G. Huang, M. Jansen, M. Mandjes, P. Spreij, K. De Turck, *Markov-modulated Ornstein–Uhlenbeck processes*, arXiv:1412.7952, first posted 2014-12-26; especially the general stationary-moment recursion.

[3] T. Miyaguchi, T. Akimoto, E. Yamamoto, *Langevin equation with fluctuating diffusivity: A two-state model*, arXiv:1605.00106, 2016-04-30.

[4] Z. Zhang and W. Wang, *The stationary distribution of Ornstein–Uhlenbeck process with a two-state Markov switching*, DOI 10.1080/03610918.2015.1132321, author-accepted version available online 2016-01-20.

[5] *Landscapes of random diffusivity processes in harmonic potential*, Physica A 633 (2024), article 129433, DOI 10.1016/j.physa.2023.129433. (Post-cutoff comparison only; full text not accessed.)
