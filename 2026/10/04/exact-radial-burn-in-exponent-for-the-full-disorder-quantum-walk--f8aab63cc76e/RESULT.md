# Exact radial burn-in exponent for the full-disorder quantum-walk Riccati circle

## Finding

Consider the full-phase-disorder Riccati recursion of the one-dimensional discrete-time quantum walk at quasienergy \(z=1\). For \(0<\theta<\pi/2\), set \(s=\sin\theta\), \(c=\cos\theta\), and
\[
w_n=\frac{r_n-c^{{-1}}}{\tan\theta}.
\]
The source recursion becomes exactly
\[
w_{{n+1}}=e^{{-i\chi_n}}\frac{{w_n+s}}{{1+s w_n}},
\]
where the full-disorder phases \(\chi_n\) are independent and uniform modulo \(2\pi\).

If \(|w_0|<1\), then every nondegenerate update makes the angle of \(w_{{n+1}}\) exactly Haar-uniform and independent of \(|w_{{n+1}}|\). The exceptional input \(w_n=-s\) gives \(w_{{n+1}}=0\); the following update has nonzero radius and Haar-uniform angle. Hence exact angular isotropy is reached after at most two updates.

For the radial defect
\[
\delta_n=1-|w_n|^2,
\]
one has the almost-sure sharp law
\[
\lim_{{n\to\infty}}\frac1n\log\delta_n
=\log(1-s^2)=2\log c.
\]
Equivalently, the defect from the invariant circle has exact logarithmic contraction factor \(c^2=\cos^2\theta\) per Riccati step. Once the Haar angular reset has occurred,
\[
\mathbb E[\log\delta_{{n+1}}]-\mathbb E[\log\delta_n]=2\log c.
\]
Writing \(L=\log((1+s)/(1-s))\), the finite-step fluctuations obey
\[
\mathbb P\!\left(
\left|\log\delta_n-\log\delta_1-(n-1)\log(c^2)\right|\ge u
\right)
\le 2\exp\!\left(-\frac{u^2}{2(n-1)L^2}\right).
\]

## Assumptions and scope

The statement uses the source's full-disorder regime, in which the effective phase \(\chi_n\) is independent and uniform modulo \(2\pi\), and the source's \(z=1\) reduced Riccati map. The coupling satisfies \(0<\theta<\pi/2\). The radial claim is stated for initial data inside the normalized invariant circle, \(|w_0|<1\). It does not assert a mixing rate for moderate or weak disorder, where the phase law is not Haar-uniform.

The primary classification is MSC 81Q35, quantum mechanics on special spaces such as graphs and lattices, because the object is a one-dimensional lattice quantum walk and the claim concerns its exact random transfer/Riccati dynamics.

## Proof

Write the source's reduced variable as \(R_n=r_n-c^{{-1}}\). Its full-disorder map is
\[
R_{{n+1}}=e^{{-i\chi_n}}\frac{{R_n+c^{{-1}}-c}}{{cR_n+1}}.
\]
Since \(c^{{-1}}-c=s^2/c\) and \(\tan\theta=s/c\), substitution of \(R_n=(s/c)w_n\) gives
\[
w_{{n+1}}=e^{{-i\chi_n}} f_s(w_n),\qquad
f_s(w)=\frac{{w+s}}{{1+s w}}.
\]
The map \(f_s\) is a disk automorphism and satisfies the exact identity
\[
1-|f_s(w)|^2=
\frac{{(1-s^2)(1-|w|^2)}}{{|1+s w|^2}}.
\]
Thus the open unit disk is invariant.

Conditional on \(w_n\), the radius of \(w_{{n+1}}\) is the deterministic number \(|f_s(w_n)|\), while its angle is shifted by the independent Haar variable \(-\chi_n\). If \(f_s(w_n)\ne0\), this angle is therefore exactly Haar-uniform and independent of the radius. The only zero of \(f_s\) is \(-s\); from that point the next state is zero and the following state is \(s e^{{-i\chi}}\), which has Haar angle.

Taking logarithms of the automorphism identity gives
\[
\log\delta_{{n+1}}-
\log\delta_n
=
\log(1-s^2)-2\log|1+s w_n|.
\]
After angular Haar reset, write \(w_n=\rho_n e^{{i\Theta_n}}\), where \(\Theta_n\) is uniform and independent of \(\rho_n\). Since \(s\rho_n<1\), Jensen's circle identity yields
\[
\frac1{{2\pi}}\int_0^{{2\pi}}
\log|1+s\rho_n e^{{it}}|\,dt=0.
\]
Consequently the conditional mean of \(X_n=\log|1+s w_n|\) is zero. Also
\[
\log(1-s)\le X_n\le\log(1+s),
\]
so \((X_n)\) is a bounded martingale-difference sequence after the reset. The martingale strong law gives
\[
\frac1n\sum_{{k=1}}^n X_k\longrightarrow0
\quad\text{{almost surely}}.
\]
Summing the logarithmic defect identity and dividing by \(n\) proves
\[
\frac1n\log\delta_n\longrightarrow\log(1-s^2)=2\log c.
\]
Taking expectations instead gives, for every \(n\ge2\),
\[
\mathbb E[\log\delta_n]=\log\delta_1+(n-1)\log(1-s^2).
\]
More quantitatively, each martingale difference lies in the interval \([\log(1-s),\log(1+s)]\), whose width is
\[
L=\log\frac{1+s}{1-s}.
\]
Hoeffding--Azuma therefore gives, for every \(u>0\),
\[
\mathbb P\!\left(
\left|\log\delta_n-\log\delta_1-(n-1)\log(1-s^2)\right|\ge u
\right)
\le
2\exp\!\left(-\frac{u^2}{2(n-1)L^2}\right).
\]
Thus the source's burn-in can be replaced by an explicit finite-horizon probabilistic certificate as well as an almost-sure asymptotic rate.

## Verification

The accompanying `verify.py` checks the disk-automorphism defect identity at representative complex points, numerically evaluates the Haar/Jensen integral for several radii and couplings, replays the telescoping logarithmic identity, and checks the predicted mean finite-horizon slope by seeded simulation; the finite-time tail inequality follows analytically from the verified increment range and Hoeffding--Azuma. It returns `VERIFY_OK`.

The computational replay is supplementary. The infinite-time statement follows from the bounded martingale-difference argument, not from simulation.

## Relationship to prior work

Derevyanko identifies the same invariant Riccati circle \(|R|=\tan\theta\), obtains the exact localization length \(1/|\log\cos\theta|\), and says that full disorder randomizes the reduced phase so that the circle becomes uniformly populated. The paper supports that phase statement with histograms and, for the stationary Riccati statistics, uses \(10^7\) iterations with the first tenth discarded as burn-in. It does not state a finite-step Haar reset, an exact finite-step mean defect law, a concentration bound, or a radial approach rate to the invariant circle.

Dorsch and Schulz-Baldes develop a general perturbative theory for random Möbius dynamics on the unit disk and invariant Furstenberg measures. Their results concern small-parameter random rotations and radial distributions in perturbative regimes. The inspected statements do not give the exact full-disorder quantum-walk map above, its immediate Haar angular reset, or the exact boundary-defect exponent \(2\log\cos\theta\).

The exact angular reset is a direct consequence of the source's full-disorder phase law, but the finite-horizon burn-in law requires combining the disk-automorphism defect identity with Haar conditional expectation and martingale concentration; the almost-sure exponent then follows from the martingale strong law. It therefore supplies a quantitative burn-in theorem for the limiting manifold used in the source's localization analysis.

## Limitations

The theorem concerns the normalized full-disorder Riccati dynamics and interior initial data. It does not change the source's localization-length formula and does not establish analogous convergence for partial disorder. The originality search cannot exclude an equivalent theorem phrased purely in random-Möbius or SU(1,1) language; this remains the main residual literature risk.

## References

1. S. Derevyanko, “Anderson localization of a one-dimensional quantum walker,” *Scientific Reports* **8**, 1795 (2018). DOI: 10.1038/s41598-017-18498-1.
2. F. Dorsch and H. Schulz-Baldes, “Random Möbius dynamics on the unit disc and perturbation theory for Lyapunov exponents,” *Discrete and Continuous Dynamical Systems B* **27** (2022), 945–976. DOI: 10.3934/dcdsb.2021076; arXiv:2008.02174.
3. C. McCarthy, G. Nop, R. Rastegar, and A. Roitershtein, “Random walk on the Poincaré disk induced by a group of Möbius transformations,” *Markov Processes and Related Fields* **25** (2019), 915–940.
