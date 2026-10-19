# Vacancy-stabilized alternating domains in the kinetic spin-one Blume–Capel ring

## Finding
Let \(B_n(z;d)\) be the generating polynomial of strictly absorbing states of the periodic nearest-neighbor spin-one Blume–Capel model, marking the number of zero spins by \(z\), with \(n\ge3\) and \(d=D/J\ge0\). For every \(0<d<1\),
\[
B_n(z;d)=2+z^n+\sum_{\substack{k\ge2\ \mathrm{even}\\3k\le n}}\frac{2n}{k}\binom{n-2k-1}{k-1}z^k.
\]
For \(d=0\), \(B_n=2\); for \(1\le d<2\), \(B_n=2+z^n\); and for \(d\ge2\), \(B_n=z^n\). In particular, infinitely many nonuniform absorbing configurations exist precisely when \(0<d<1\). The absorbing-state entropy density exists and is
\[
\lim_{n\to\infty}\frac1n\log B_n(1;d)=
\begin{cases}\log\lambda,&0<d<1,\\0,&d=0\text{ or }d\ge1,\end{cases}
\qquad \lambda^3-\lambda^2-1=0,\ \lambda>1.
\]
Moreover, in \(0<d<1\), a uniformly selected absorbing configuration has a fraction of zero spins converging in probability to \(1/(\lambda^2+3)\). The strict-stability counting polynomial, including both transition equalities, is the single result claimed here.

## Assumptions and scope
Sites \(i\in\mathbb Z/n\mathbb Z\) carry \(s_i\in\{-1,0,+1\}\); \(n\ge3\), \(J>0\), \(D\ge0\). The energy is
\[
H(s)=-J\sum_{i=0}^{n-1}s_is_{i+1}+D\sum_{i=0}^{n-1}s_i^2.
\]
The allowed zero-temperature single-site dynamics can substitute either of the *other two* states with positive rate whenever this does not increase the energy, including energy-neutral substitutions. A configuration is strictly absorbing exactly when every such substitution *increases* energy. This definition is not equivalent to weak (nonstrict) local-minimum counting, positive-temperature metastability, or the equilibrium partition function. Vertices are labeled, so spatial rotations count as distinct configurations.

## Proof
Put \(h_i=s_{i-1}+s_{i+1}\), \(d=D/J\). At fixed neighbors, the local energy in units of \(J\) is \(e_i(t)=d t^2-t h_i\). Therefore a zero spin is strictly stable precisely when \(d>|h_i|\); a nonzero spin of sign \(\sigma\in\{\pm1\}\) is strictly stable precisely when \(\sigma h_i>d\) (the latter simultaneously defeats the other sign). The neighbor sum is an integer between \(-2\) and \(2\).

At \(d=0\), zeros fail strict stability. A stable nonzero has \(\sigma h_i>0\), ruling out any interface between two opposite signs; therefore only the two uniform polarized configurations survive.

When \(0<d<1\), each stable zero must satisfy \(h_i=0\). Each stable nonzero has \(\sigma h_i\ge1\), so a nonzero cannot neighbor an opposite nonzero; and any nonzero run bounded by zeros has length at least two. If a configuration contains both zero and nonzero spins, no block of consecutive zeros can have length at least two: its zero on the boundary of a polarized run would have neighbor sum \(\pm1\). Consequently zero spins occur singly and separate runs of opposite polarizations, each of length at least two. Cyclic consistency forces an even number \(k\ge2\) of separators. Conversely, every such configuration meets the stated strict local-energy tests. The two uniformly polarized and the uniformly zero configurations complete the classification.

For \(1\le d<2\), a nonzero spin is strictly stable only if both neighboring spins have its own sign, forcing any nonzero present to fill the ring uniformly. The all-zero state is also strictly stable. At \(d\ge2\), no nonzero can be strictly stable; only all zero remains. This proves all cases including \(d=1\) and \(d=2\), where neutral moves disqualify additional states.

To count nonuniform configurations when \(0<d<1\), fix an even separator count \(k\). At each separator, one polarized run of length at least two follows. Positive integers \(\ell_1,\ldots,\ell_k\ge2\) have total \(n-k\), hence their ordered count is \(\binom{n-2k-1}{k-1}\). There are \(n\) choices of a distinguished labeled separator, two choices of initial sign, and each resulting configuration is counted \(k\) times by the distinguished separator. Thus the exact coefficient is \(\frac{2n}{k}\binom{n-2k-1}{k-1}\), as claimed.

For asymptotics, write \(f(x,z)=zx^3/(1-x)\). The ordinary generating function of the nonuniform count is
\[
\sum_{n\ge3}(B_n(z;d)-2-z^n)x^n
=2x\frac{f(x,z)\,\partial_x f(x,z)}{1-f(x,z)^2}.
\]
At \(z=1\), the unique dominant positive singularity \(r\in(0,1)\) solves \(f(r,1)=1\), or \(r^3+r-1=0\). Uniqueness on the convergence circle follows since the powers \(x^3,x^4,\ldots\) appearing in \(f\) are aperiodic: equality in \(|f(x,1)|\le f(|x|,1)\) requires \(x=r\). The generating function has a simple pole with principal part \(x/(r-x)\), hence \(B_n(1;d)=r^{-n}(1+o(1))\). Set \(\lambda=1/r\), so \(\lambda^3-\lambda^2-1=0\). All other parameter ranges have at most three absorbing states, giving zero entropy density.

For \(z\) in a neighborhood of \(1\), the dominant singularity is the reciprocal of the analytic positive root \(\lambda(z)\) of \(\lambda(z)^3-\lambda(z)^2-z=0\). Uniform simple-pole asymptotics for the positive vacancy-weighted generating polynomials give \(n^{-1}\log\mathbb E[z^{K_n}]\to\log\lambda(z)-\log\lambda(1)\), locally analytically, where \(K_n\) is the vacancy count in a uniformly chosen absorbing state. Differentiation and a second-moment bound imply convergence in probability of \(K_n/n\) to \(\lambda'(1)/\lambda(1)=1/(\lambda^2+3)\).

## Verification
The standalone `verify_blume.py` directly enumerates all \(3^n\) spin states for \(3\le n\le11\) and checks eight exact rational crystal fields at each size (72 full-energy comparisons). It separately compares 26 coefficients of the renewal generating function to the finite-size counting formula, using integer recurrences. These checks test signs, threshold equalities, small rings and integrality. They do *not* prove the infinite-family statements, which follow from the local inequalities and analytic arguments above. Run `python verify_blume.py` with Python 3 and no external modules.

## Relationship to prior work
Cirillo and Olivieri (1995) study low-temperature nucleation and local minima of a two-dimensional Blume–Capel system in a nonzero-field regime; Section 3 analyzes two-dimensional droplet geometries, not the strict zero-field one-dimensional periodic count. Almeida and Dalmazi (2005) solve the equilibrium partition function and Yang–Lee zero problem on one-dimensional Blume–Capel rings (including the same spin alphabet and nearest-neighbor interaction), but do not count kinetically absorbing configurations. Keskin, Canko and Kantar (2006) study mean-field oscillating-field dynamic phase transitions of a kinetic spin-one model, without the present ring classification. Work on conventional binary-spin zero-temperature Ising freezing likewise lacks the vacancy-stabilized alternating sign interfaces. Equality of an entropy constant with another symbolic-dynamics or Ising count does not itself imply identity of strict local-energy conditions.

## Limitations
This is a one-dimensional, zero-external-field, nonnegative-crystal-field, strictly one-site-absorbing classification. It does not calculate probabilities of reaching individual frozen states from a quench, coarsening dynamics, finite-temperature lifetimes, or equilibrium phase transitions. Unindexed earlier equivalent counts remain possible.

## References
1. E. N. M. Cirillo and E. Olivieri, *Metastability and Nucleation for the Blume-Capel Model. Different mechanisms of transition* (first public version 10 May 1995), arXiv:hep-th/9505055v1, https://arxiv.org/html/hep-th/9505055v1.
2. L. A. F. Almeida and D. Dalmazi, *The Yang-Lee zeros of the 1D Blume-Capel model on connected and non-connected rings* (24 May 2005), arXiv:cond-mat/0505605v1, https://arxiv.org/abs/cond-mat/0505605.
3. M. Keskin, O. Canko and E. Kantar, *Dynamic dipole and quadrupole phase transitions in the kinetic spin-1 model* (5 October 2006), arXiv:cond-mat/0610149v1, https://arxiv.org/abs/cond-mat/0610149.
4. V. Spirin, P. L. Krapivsky and S. Redner, *Freezing in Ising Ferromagnets* (2 May 2001), arXiv:cond-mat/0105037v1, https://arxiv.org/abs/cond-mat/0105037.
