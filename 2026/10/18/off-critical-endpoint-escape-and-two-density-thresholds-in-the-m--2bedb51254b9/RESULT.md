# Off-critical endpoint escape and two density thresholds in the modified Boyarsky–Góra–Islam map

## Finding

The random interval map of Hata and Yano has a first transition at the balanced probability \(p=2/3\), separating almost-sure endpoint escape from the existence of a normalizable dyadic-shell-constant invariant density. Above this balance point the density undergoes a second, independent regularity transition at \(p=6/7\): it changes from a power singularity to a logarithmic singularity at the threshold and a bounded endpoint limit above it. The stationary shell depth has an exact rational probability-generating function, and its rescaled law tends to a mean-one exponential distribution on approach to the balance point.

## Assumptions and scope

Take independent random choices at each iteration, choosing \(\tau_1\) with probability \(0<p<1\) and \(\tau_2\) with probability \(q=1-p\). On the open interval, away from the finite branch boundaries, the maps are

\[
\tau_1(x)=\begin{cases}
2x,&0<x<1/4,\\
1-2x,&1/4<x<1/2,\\
2-2x,&1/2<x<3/4,\\
2x-1,&3/4<x<1,
\end{cases}\qquad
\tau_2(x)=\begin{cases}
1-x/4,&0<x<1/2,\\
(1-x)/4,&1/2<x<1.
\end{cases}
\]

The finite and countable collections of dyadic branch endpoints have zero probability under any absolutely continuous initial law. Define the two shells

\[
I_k^-=(2^{-k-2},2^{-k-1}),\qquad
I_k^+=(1-2^{-k-1},1-2^{-k-2}),\qquad k\ge0.
\]

The shell-depth observable is \(K(x)=k\) on either of these cells. Statements about stationary density uniqueness are explicitly restricted to the class of probability measures having densities constant on each cell; other absolutely continuous invariant probabilities are not classified here. Statements about spatial convergence refer to the annealed law under independent random choices, not the almost-sure convergence of the spatial coordinate to a single endpoint.

## Proof

**Exact shell process.** The affine-image identities in the source, and direct evaluation of the displayed branches, give the following transitions for each side. Applying \(\tau_2\) flips side and sends shell \(k\) to shell \(k+2\). Applying \(\tau_1\) leaves side unchanged and sends \(k\ge1\) to \(k-1\). For \(k=0\), the image of \(\tau_1\) covers the corresponding entire half interval; conditional on an initially uniform point in that cell, the new shell is \(j\ge0\) with probability \(2^{-j-1}\). Every branch is affine and therefore preserves the requisite conditional uniformity. The induced shell-and-side chain is consequently exact for densities constant on the shell cells.

**Positive-recurrence side of the transition.** Suppose \(2/3<p<1\). Let \(w_k\) be the total stationary mass of depth \(k\), with equal mass \(w_k/2\) in each side. The stationary equations are

\[
w_k=pw_{k+1}+q\mathbf1_{k\ge2}w_{k-2}+\frac{pw_0}{2^{k+1}},\qquad k\ge0.
\]

For \(W_p(z)=\sum_{k\ge0}w_kz^k\), multiplication by \(z^{k}\) and summation give

\[
W_p(z)=\frac pz(W_p(z)-w_0)+qz^2W_p(z)+\frac{pw_0}{2-z}.
\]

Factoring \(z-p-qz^3=(z-1)(p-qz-qz^2)\) yields

\[
W_p(z)=\frac{2pw_0}{(2-z)(p-qz-qz^2)}.
\]

Normalization \(W_p(1)=1\) forces \(w_0=(p-2q)/(2p)=(3p-2)/(2p)\). Therefore

\[
\boxed{W_p(z)=\frac{3p-2}{(2-z)(p-qz-qz^2)},\qquad
\mathbb E_p[K]=W_p'(1)=\frac1{3p-2}.}
\]

The coefficients are strictly positive because \(p>2q\): both inverse series \((2-z)^{-1}\) and \((p-qz-qz^2)^{-1}\) have strictly positive coefficients. Their sum is one, so this gives an invariant probability whose density on either cell of depth \(k\) equals \(h_p(x)=2^{k+1}w_k\). The shell-side Markov chain is irreducible (the depth-zero branch accesses every depth and the other map flips side) and aperiodic (the depth-zero reset has a self-loop). This stationary probability is thus unique within the shell-cell-constant class.

**Sharp boundedness transition.** Let \(r=r(p)>1\) be the positive root of \(q(r^2+r)=p\). The other quadratic root is \(-1-r\) and has strictly larger modulus. If \(2/3<p<6/7\), then \(1<r<2\); the simple pole at \(z=r\) is dominant, and

\[
w_k\sim\frac{3p-2}{q(2-r)(2r+1)r}\,r^{-k}.
\]

Consequently \(h_p\) diverges at both endpoints at the power-law rate \((2/r)^k\). At \(p=6/7\), the pole at \(z=2\) becomes double and the partial fraction identity is

\[
W_{6/7}(z)=\frac4{(2-z)^2(z+3)},\qquad
w_k=\left(\frac{k}{5}+\frac7{25}\right)2^{-k}
+\frac4{75}\left(-\frac13\right)^k.
\]

Hence \(h_{6/7}\) equals \(2k/5+14/25+(8/75)(-2/3)^k\) on either cell of depth \(k\), proving the precise logarithmic endpoint singularity. For \(6/7<p<1\), the pole at \(z=2\) is strictly dominant, so

\[
w_k\sim\frac{3p-2}{2(7p-6)}2^{-k},\qquad
\lim_{k\to\infty}h_p|_{I_k^\pm}=\frac{3p-2}{7p-6}.
\]

Every finitely many remaining shell densities are finite, proving that boundedness is equivalent to \(p>6/7\).

**Critical scaling.** Write \(\varepsilon=3p-2>0\). For any \(t\ge0\), substitution \(z=e^{-\varepsilon t}\) yields

\[
\mathbb E_p[e^{-t\varepsilon K}]=W_p(e^{-\varepsilon t})
\longrightarrow\frac1{1+t},\qquad p\downarrow2/3.
\]

The right-hand side is the Laplace transform of a mean-one exponential law. The continuity theorem proves \(\varepsilon K\) converges in distribution to this law.

**Escape side of the transition.** Suppose \(0<p<2/3\). Independently of the current shell, a \(\tau_1\) iteration decreases its depth by one whenever \(k\ge1\), and at depth zero can only reset to a nonnegative depth. A \(\tau_2\) iteration always increases depth by two. Thus, for i.i.d. increments \(\xi_n\) equal to \(-1\) with probability \(p\) and \(+2\) with probability \(q\),

\[
K_n\ge K_0+\sum_{j=1}^n\xi_j.
\]

By the strong law, the right-hand side diverges linearly at rate \(2-3p>0\). Therefore depth zero is visited only finitely many times. After its last visit, equality in the increment rule holds at every subsequent time, giving \(K_n/n\to2-3p\) almost surely. On depth \(k\), the distance to the nearest endpoint lies between \(2^{-k-2}\) and \(2^{-k-1}\), proving the claimed logarithmic rate. The half-interval side flips exactly on iterations choosing \(\tau_2\), independently with probability \(q>0\). Its law tends to the symmetric two-point law, and since depth tends to infinity, the spatial annealed law converges weakly to \((\delta_0+\delta_1)/2\). A stationary absolutely continuous probability would contradict this weak limit, because it is stationary at every time yet is supported away from the two endpoints. Thus no such invariant probability exists for \(p<2/3\).

## Verification

Run `python verify.py` in the directory containing the accompanying standalone program. It checks the exact affine branch itineraries at multiple dyadic levels, exact stationary balance of rational Taylor coefficients for six rational parameters, an exact closed coefficient formula at the logarithmic threshold, and finite numeric diagnostics of the critical Laplace scaling. The all-parameter invariance, recurrence, pole order, law of large numbers, and weak convergence are proved above, not inferred from these finite checks.

## Relationship to prior work

Hata and Yano, *Arcsine and Darling–Kac laws for piecewise linear random interval maps* (arXiv:2108.01332, initially made public 2021-08-03), define the mBGI branches and dyadic partition in their equations (1.22)–(1.24). Their equations (4.1)–(4.5) establish the transition identities at the **critical** weight \(p=2/3\), and their Theorem 1.3 establishes the infinite invariant measure and Darling–Kac law at that weight. These facts are prior results, not new claims here. The analysis above solves the different questions of the **off-critical** stationary distribution, its second boundedness threshold, critical approach scaling, and endpoint escape for the same map family. The earlier Boyarsky–Góra–Islam article (2005) treats a related rather than identical random-map construction; no priority claim about that paper's uninspected full text is made. All rational-generating-function and pole methods used here are classical.

## Limitations

Only the shell-constant absolutely continuous stationary class is characterized uniquely above \(p=2/3\); an independent uniqueness theorem covering all possible absolutely continuous invariant probabilities is not asserted. At \(p=2/3\), the existence of a nonnormalizable invariant measure is due to Hata and Yano, not this result. The weak endpoint mixture when \(p<2/3\) does not mean individual sample trajectories converge to one endpoint: the side switches infinitely often. No quenched invariant density, universal perturbation theorem, or statement on other random-map families is claimed. Priority regarding related unpublished or inaccessible literature remains open to independent checking.

## References

1. Genji Hata and Kouji Yano, *Arcsine and Darling–Kac laws for piecewise linear random interval maps*, arXiv:2108.01332 (version 1 submitted August 3, 2021; version 3 September 22, 2022), especially Theorem 1.3 and equations (4.1)–(4.5). https://arxiv.org/abs/2108.01332 ; full text: https://arxiv.org/html/2108.01332v3 .
2. Abraham Boyarsky, Paweł Góra and Md. Shafiqul Islam, *Randomly chosen chaotic maps can give rise to nearly ordered behavior*, Physica D **210** (2005), 284–294, doi:10.1016/j.physd.2005.07.015. This related precursor is not treated as proving the displayed off-critical formulas.
