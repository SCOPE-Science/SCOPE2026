# Sharp weighted-square criterion and logarithmic boundary at the critical Cayley-tree Ising field
## Finding
For the critical-field ferromagnetic Ising model on a Cayley tree studied by Bissacot, Endo, and van Enter, let the generation-dependent field be \(h_n=-h_c-\varepsilon_n\), where \((\varepsilon_n)_{n\ge1}\) is positive, nonincreasing, and tends to zero. Put
\[
S_N=\sum_{j=1}^N\left(\sum_{i=j}^N\varepsilon_i\right)^2,
\qquad
W_N=\sum_{n=1}^N n^2\varepsilon_n^2.
\]
Then, for every \(N\ge1\),
\[
W_N\le S_N\le4W_N.
\]
The upper constant \(4\) is optimal even among positive decreasing sequences. Hence the source criterion \(\sup_N S_N<\infty\) is equivalent to the local weighted-square condition
\[
\sum_{n\ge1}n^2\varepsilon_n^2<\infty.
\]

For perturbations that are eventually
\[
\varepsilon_n=c\,n^{-3/2}(\log n)^{-p},
\]
with \(c>0\), the source theorems therefore give a second-order critical boundary at \(p=1/2\): phase coexistence persists at low temperature for \(p>1/2\), while the Gibbs measure is unique for every temperature for \(p\le1/2\). At the boundary \(p=1/2\), adding a factor \((\log\log n)^{-q}\) creates the next threshold at \(q=1/2\).

## Assumptions and scope
The tree is the \((d+1)\)-regular Cayley tree \(\Gamma^d\) with the ferromagnetic nearest-neighbor Ising interaction used in the cited source. The source's critical homogeneous field is \(-h_c(\beta,d)\). The persistence conclusion is the source's low-temperature conclusion, in particular in its critical-field regime with \(\beta>\beta_c(d)\); the uniqueness conclusion is the source's all-temperature theorem. The perturbation is radial by generation, positive, nonincreasing, and tends to zero. For the logarithmic families only the eventual formula matters: a finite prefix may be chosen to make the complete sequence positive and nonincreasing.

## Proof
The lower estimate is the source's Proposition 1:
\[
S_N\ge\sum_{n=1}^N(n\varepsilon_n)^2=W_N.
\]
For the upper estimate define finite tails
\[
T_j=\sum_{i=j}^N\varepsilon_i,
\qquad T_{N+1}=0.
\]
Discrete summation by parts gives the exact identity
\[
\sum_{j=1}^NT_j^2
=\sum_{j=1}^N j\bigl(T_j^2-T_{j+1}^2\bigr)
=\sum_{j=1}^N j\varepsilon_j(T_j+T_{j+1}).
\]
Since \(T_{j+1}\le T_j\), Cauchy--Schwarz yields
\[
S_N\le2\sum_{j=1}^N j\varepsilon_jT_j
\le2W_N^{1/2}S_N^{1/2},
\]
and therefore \(S_N\le4W_N\). This part does not require monotonicity; monotonicity is needed for the source lower bound.

To see that \(4\) is optimal within the source class, take \(\varepsilon_n=n^{-3/2}\). Then \(W_N=H_N\), the \(N\)-th harmonic sum. For \(1\le j\le N\), the integral lower bound gives
\[
T_j\ge2\left(j^{-1/2}-(N+1)^{-1/2}\right).
\]
Consequently
\[
S_N\ge4H_N-\frac{8}{\sqrt{N+1}}\sum_{j=1}^N j^{-1/2}+\frac{4N}{N+1}
\ge4H_N-16,
\]
whereas the already-proved upper estimate gives \(S_N\le4H_N\). Since \(H_N\to\infty\), it follows that \(S_N/W_N\to4\).

Thus \(\sup_NS_N<\infty\) if and only if \(\sup_NW_N<\infty\), equivalently \(\sum_{n\ge1}n^2\varepsilon_n^2<\infty\). The primary source proves phase coexistence at low temperature in the first case and uniqueness for every temperature when its tail-square sum diverges.

For the logarithmic family,
\[
n^2\varepsilon_n^2=\frac{c^2}{n(\log n)^{2p}}.
\]
The integral test gives convergence exactly when \(2p>1\). Hence \(p>1/2\) lies on the phase-transition side and \(p\le1/2\) on the uniqueness side. At \(p=1/2\), an additional factor \((\log\log n)^{-q}\) reduces the weighted series to
\[
\sum_n\frac{1}{n\log n(\log\log n)^{2q}},
\]
which converges exactly when \(q>1/2\).

## Verification
The accompanying `verify.py` checks the finite summation-by-parts identity and both inequalities exactly over rational test families, independently checks that the lower bound from the source is respected for decreasing rational sequences, and numerically tracks the sharpness family \(\varepsilon_n=n^{-3/2}\) using a linear-time tail recursion. These computations corroborate the proof; no finite computation is used to establish the infinite statements.

## Relationship to prior work
Bissacot--Endo--van Enter formulate their phase criterion using \(S_N\), prove the lower estimate \(S_N\ge W_N\), and analyze the pure powers \(\varepsilon_n=n^{-\gamma}\), obtaining the critical exponent \(\gamma_c=3/2\) and uniqueness at equality. Their displayed upper estimate is instead \(N\)-dependent and does not yield the uniform converse \(S_N\le4W_N\). The present finding supplies that converse with the optimal constant, collapses the nonlocal criterion to a weighted \(\ell^2\) condition, and resolves logarithmic perturbations at the source's critical power. The weighted Hardy estimate used in the proof is elementary/classical in character; originality is claimed for this exact reduction and its model-specific critical logarithmic consequences, not for inventing Hardy's inequality.

A later dissertation exposition by Endo repeats the pure-power \(\gamma_c=3/2\) example and discusses broader-tree extensions as an open direction; the searches performed for the present comparison did not locate the weighted criterion or the \(p=1/2\) logarithmic boundary in the same model.

## Limitations
The result inherits the source's hypotheses: radial monotone perturbations of the critical field on a Cayley tree. It does not classify nonmonotone perturbations, arbitrary trees, nonradial fields, or critical behavior such as magnetization exponents. The phase-transition side is the low-temperature persistence conclusion of the source, whereas the divergence side inherits its stronger all-temperature uniqueness statement. The logarithmic thresholds concern eventual asymptotics; finite initial changes are immaterial to series convergence but must be chosen so the source monotonicity hypothesis holds.

## References
1. R. Bissacot, E. O. Endo, A. C. D. van Enter, *Stability of the Phase Transition of Critical-Field Ising Model on Cayley trees under Inhomogeneous External Fields*, arXiv:1611.00424v1 (2016); Stochastic Processes and their Applications 127 (2017), 4126--4138, DOI: 10.1016/j.spa.2017.03.023.
2. E. O. Endo, doctoral dissertation, University of Sao Paulo (2019), Section 4.4, reproducing the critical-field Cayley-tree analysis and pure-power \(\gamma_c=3/2\) example.
