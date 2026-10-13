# Bath-independent ergotropy crossing levels for mixed qubits under thermal amplitude damping

## Finding

**Theorem (exact mixed-state crossing law).** Let \(h>0\), let \(H=h\sigma_z\), and take any two physical qubit states \(\rho_i=(I+x_i\sigma_x+y_i\sigma_y+z_i\sigma_z)/2\), \(i=1,2\). Put \(b_i=x_i^2+y_i^2\) and assume \(b_i+z_i^2\leq1\). Let both states evolve under the *same* thermal generalized amplitude-damping semigroup with emission and absorption rates \(\gamma_-\geq\gamma_+\geq0\) and \(\kappa=\gamma_-+\gamma_+>0\). Assume the initial ergotropies obey \(\mathcal W_1(0)>\mathcal W_2(0)\).

Then a finite-time **strict order reversal** occurs if and only if \(b_1<b_2\), and it occurs **exactly once**. Its common dimensionless ergotropy is

\[
 e_*=\frac{b_2-b_1}{2(z_1-z_2)}>0,
 \qquad \mathcal W_1(t_*)=\mathcal W_2(t_*)=h e_*.
\]

In particular, **the common extractable work is independent of the bath temperature and both damping rates**. Define the thermal bias \(\eta=(\gamma_- -\gamma_+)/\kappa\in[0,1]\). The unique crossing time is given *for arbitrary mixed or pure inputs* by

\[
q_*=\frac{e_*(e_*+2\eta)}{2e_*(z_1+\eta)+b_1}
=\frac{e_*(e_*+2\eta)}{2e_*(z_2+\eta)+b_2}\in(0,1),
\qquad
 t_*=-\frac{\log q_*}{\kappa}.
\]

At a fixed total relaxation rate \(\kappa\), the crossing occurs strictly **earlier for a colder bath** (larger \(\eta\)): \(q_*\) strictly increases with \(\eta\). If \(b_1\geq b_2\), the initially larger ergotropy never becomes strictly smaller, although two diagonal states can eventually share zero ergotropy on a time interval. These zero-ergotropy coincidences are not crossings.

## Assumptions and scope

The Hamiltonian \(H=h\sigma_z\) has excited level \(+h\) and ground level \(-h\). The Markov generator is

\[
 \mathcal L(\rho)=-i[H,\rho]+\gamma_-\!\left(\sigma_-\rho\sigma_+-\tfrac12\{\sigma_+\sigma_-,\rho\}\right)
 +\gamma_+\!\left(\sigma_+\rho\sigma_- -\tfrac12\{\sigma_-\sigma_+,\rho\}\right).
\]

The inverse-temperature range is nonnegative, including zero-temperature emission only (\(\eta=1\)) and the infinite-temperature limit (\(\eta=0\)). The two states share the same semigroup. Ergotropy means global-unitary work extraction from a single qubit: \(\mathcal W(\rho)=\operatorname{tr}(H\rho)-\min_U\operatorname{tr}(HU\rho U^\dagger)\). There is no further pure-state or nonzero-coherence hypothesis.

## Proof

**1. Exact evolution and normalization.** Let \(q=e^{-\kappa t}\). Directly solving the population and coherence components of the master equation gives

\[
 z_i(q)=-\eta+q(z_i+\eta),\qquad
 x_i(q)^2+y_i(q)^2=q b_i.
\]

The Bloch radius is \(r_i(q)=\sqrt{z_i(q)^2+qb_i}\). Since the eigenvalues of \(\rho_i(q)\) are \((1\pm r_i(q))/2\), its passive energy is \(-hr_i(q)\), and its normalized ergotropy is

\[
 e_i(q)=\frac{\mathcal W_i(q)}h=z_i(q)+r_i(q)\geq0.
\]

Equivalently, for any \(e=e_i(q)>0\), removing the square root gives the **exact inverse level equation**

\[
 e^2+2\eta e=q\bigl(2e(z_i+\eta)+b_i\bigr).\tag{1}
\]

**2. A temperature-independent common level.** If the two positive ergotropies agree at any \(q>0\), subtracting (1) for the two states cancels both the equilibrium bias and the common evolution parameter:

\[
 2e(z_1-z_2)=b_2-b_1.\tag{2}
\]

Because \(e_1(1)>e_2(1)\), the ordered inputs cannot have \(z_1=z_2\) and a positive-ergotropy coincidence. If \(b_1<b_2\), the same initial inequality and monotonicity of \(z+\sqrt{z^2+b}\) in both \(z\) and \(b\) force \(z_1>z_2\). Thus (2) uniquely fixes a positive \(e_*\). Solving (1) for \(q\) gives the two equal formulas for \(q_*\) above.

**3. Existence, uniqueness and direction.** Each \(e_i(q)\) is continuous and nonnegative for \(q\in[0,1]\), with \(e_i(0)=0\). On its strictly positive locus, implicit differentiation of (1) yields

\[
 \frac{de_i}{dq}=\frac{e_i(e_i+2\eta)}{2q\,r_i(q)}>0.\tag{3}
\]

Hence either input can attain the prescribed *positive* common level at most once; (2) shows any positive coincidence must occur at that same level. There can therefore be at most one positive crossing. When \(b_1<b_2\), the initially larger state has the smaller long-time ergotropy: for \(\eta>0\), \(e_i(q)=qb_i/(2\eta)+O(q^2)\) if \(b_i>0\), whereas \(b_i=0\) gives \(e_i(q)=0\) for all sufficiently small \(q\); for \(\eta=0\), \(e_i(q)=\sqrt{qb_i}+O(q)\) if \(b_i>0\), and \(e_i(q)=2q\max(z_i,0)\) if \(b_i=0\). Since \(b_2>b_1\), the second ergotropy strictly dominates for small positive \(q\). The initial ordering is reversed at \(q=1\); continuity gives a crossing at \(q_*\in(0,1)\), whose common ergotropy is positive because \(b_2>0\). Its uniqueness follows from (2)–(3).

For \(b_1\geq b_2\), strict reversal cannot occur: if there were one, the late-time ordering (when unequal transverse weights) or the pointwise monotonicity in \(z\) (when weights coincide) would force a further positive crossing, contradicting uniqueness. More directly, with \(b_1>b_2\), the late-time ordering agrees with the initial ordering, while any interior positive equality is transverse because \(z_1\ne z_2\): differentiating at an equal \(e>0\) gives different slopes in (3) unless \(z_1=z_2\), which is impossible by (2). Thus a positive equality would reverse the ordering and require another. Equal transverse weights imply \(z_1>z_2\) and pointwise ordered ergotropy. Possible simultaneous zero plateaux are excluded by the definition of strict reversal.

**4. Thermal-bias monotonicity.** Differentiating the exact \(q_*\) expression at fixed state preparations yields

\[
 \frac{dq_*}{d\eta}=
 \frac{2e_*\bigl(2e_*z_1+b_1-e_*^2\bigr)}{\bigl(2e_*(z_1+\eta)+b_1\bigr)^2}.
\]

The factor in parentheses is positive because the proven crossing at \(\eta=0\) satisfies \(q_*(0)=e_*^2/(2e_*z_1+b_1)<1\). Thus \(dq_*/d\eta>0\), so \(t_*=-\log(q_*)/\kappa\) decreases strictly with \(\eta\) when \(\kappa\) is held fixed.

## Verification

Run `python verify_crossing.py` with Python 3 and no third-party packages. The included script checks four exact-rational instances of the inverse-level equation for one pair of physical mixed states at distinct bath biases, and compares the closed formula with 12,000 seeded physical-state tests (5,011 crossings) and additional no-crossing grid checks. It returns `VERIFY_OK`. Numerical sampling is not used to prove any quantifier over all states, temperatures or times.

For example, choose \(z_1=3/5\), \(b_1=1/25\), \(z_2=0\), \(b_2=1/4\). Both are physical mixed qubit inputs, and \(e_*=7/40\). At \(\eta=1\), \(q_*=203/320\); at \(\eta=0\), \(q_*=49/400\). Both crossings have work \(7h/40\) despite their different times.

## Relationship to prior work

Sapui, Konar and Sen (De), arXiv:2602.11056, derive the full single-state generalized-amplitude-damping ergotropy dynamics and a necessary-and-sufficient *coherence-ordering* test for whether two qubit preparations cross. Their Section II.1 and Appendix C derive an explicit crossing time for *pure* states. In contrast, (1)–(3) solve the arbitrarily **mixed** pairwise crossing *level and time* exactly, prove uniqueness for any finite temperature, and expose a bath-independent crossing-work invariant plus a monotonic temperature response at fixed total rate. These statements are derived from the known dynamics, not an independently introduced dynamical model; in particular, the qualitative coherence-ordering criterion is not presented as new.

Choquehuanca, Obando, Sarandy and de Paula, arXiv:2504.07200, analyze single-qubit ergotropy-based thermodynamics and generalized amplitude damping; their work is relevant to the ergotropy and thermal-map framework, not an explicit pairwise mixed-state crossing level classification.

## Limitations

This is a semigroup result for a thermal, non-inverted two-level bath with no additional pure dephasing. Arbitrary non-Markovian revivals, unrelated channels on the two preparations, and rate profiles with a changing equilibrium bias are outside the theorem. The common work is temperature-independent, but the elapsed crossing time generally is not. The result is an analytic consequence of exact Lindblad dynamics already present in the principal source, and a hidden equivalent derivation in another treatment of that formula remains a scientific originality risk. No experimental implementation or thermodynamic-engine performance is claimed.

## References

1. T. Sapui, T. K. Konar and A. Sen (De), *Ergotropic Mpemba crossings in finite-dimensional quantum batteries*, arXiv:2602.11056v1 (first submitted 2026-02-11 UTC), current accessible full text arXiv:2602.11056v3, Sections II.1 and Appendices B.1, C. https://arxiv.org/html/2602.11056v3
2. J. M. Z. Choquehuanca, P. A. C. Obando, M. S. Sarandy and F. M. de Paula, *Ergotropy-Based Quantum Thermodynamics*, arXiv:2504.07200v1 (2025-04-09), current accessible full text arXiv:2504.07200v3, Sections VI and VII.1. https://arxiv.org/html/2504.07200v3
