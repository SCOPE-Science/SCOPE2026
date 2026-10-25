# A four-spin obstruction to two-point factorization in a periodic three-temperature Glauber chain

## Finding

For the one-dimensional kinetic Ising spin chain with three periodically repeated heat-bath parameters, the familiar ordered-pair factorization of stationary four-spin correlations can fail, even when **all three bath temperatures are strictly positive and finite**. The failure has an exact negative defect at a convenient infinite-temperature reference point and survives a uniform, finite-volume-independent perturbation to three finite temperatures.

Write \(\langle\cdot\rangle_{\delta}\) for stationary expectation and define the observable

\[
F_\delta=\langle\sigma_0\sigma_1\sigma_2\sigma_3\rangle_\delta-\langle\sigma_0\sigma_1\rangle_\delta\langle\sigma_2\sigma_3\rangle_\delta.
\]

For every \(0<a,b<1\), at \(\delta=0\),

\[
F_0=-\frac{a^2b^2}{(16-ab)^2},\qquad
\kappa_4(\sigma_0,\sigma_1,\sigma_2,\sigma_3)=-\frac{2a^2b^2}{(16-ab)^2}.
\]

For all \(0\le\delta<1\), with \(0<a,b<1\), the finite-temperature perturbation satisfies the **uniform** inequality

\[
|F_\delta-F_0|\le16\delta.
\]

Therefore direct ordered-pair factorization fails whenever

\[
0\le\delta<\frac{a^2b^2}{16(16-ab)^2}.
\]

For example, the *three different strictly finite* parameter values
\(\delta=10^{-6}\), \(a=1/2\), \(b=1/3\) obey

\[
F_\delta\le-\frac1{9025}+16\cdot10^{-6}<0.
\]

The inequalities and exact endpoint formula hold independently of the size of the ring and also for the unique infinite-volume stationary state. They provide a concrete answer concerning direct two-point factorization, not a classification of all possible alternative multispin representations.

## Assumptions and scope

Let \(N\ge6\) be divisible by three and consider Ising spins \(\sigma_i\in\{-1,1\}\) on the ring \(\mathbb Z/N\mathbb Z\). Each spin flips at rate

\[
w_i(\sigma)=1-\frac{\gamma_i}{2}\sigma_i(\sigma_{i-1}+\sigma_{i+1}),\qquad
(\gamma_{3j},\gamma_{3j+1},\gamma_{3j+2})=(\delta,a,b).
\]

Assume \(0<a,b<1\) and \(0\le\delta<1\). All rates are positive, hence the finite chain has a unique stationary law. For ferromagnetic exchange \(J>0\), the bath parameters correspond to physical temperatures through \(\gamma_i=\tanh(2J/(k_BT_i))\). Thus \(0<\gamma_i<1\) means strictly positive finite temperature; \(\gamma_i=0\) is the infinite-temperature endpoint used solely to calculate the reference correlations.

The same statements concern the unique stationary process on the bi-infinite spin chain with spatial period three. In that setting graphical backward ancestries terminate almost surely because the copying probabilities are bounded strictly below one, giving a unique stationary spin field.

## Proof

**1. Exact finite- or infinite-volume moments at the hot reference point.** Put \(\delta=0\). Every site congruent to zero modulo three flips autonomously, so the four-spin process \(X=\sigma_0\), \(U=\sigma_1\), \(V=\sigma_2\), \(Y=\sigma_3\) is a *closed autonomous Markov chain* in every ring of the stated size, as well as in infinite volume. Its generator on individual spins is

\[
LX=-2X,\quad LU=-2U+a(X+V),\quad LV=-2V+b(U+Y),\quad LY=-2Y.
\]

For products of distinct spins, only the flips of those spins contribute, and the product-rule term from the generator is a sum, not an Itô correction. The stationary two-spin equations \(\langle L(XU)\rangle=0\) and analogous identities imply, with \(D=16-ab\),

\[
\begin{array}{lll}
\langle XU\rangle=4a/D,&\langle XV\rangle=ab/D,&\langle XY\rangle=0,\\
\langle UV\rangle=4(a+b)/D,&\langle UY\rangle=ab/D,&\langle VY\rangle=4b/D.
\end{array}
\]

For illustration, \(4\langle XU\rangle=a(1+\langle XV\rangle)\) and \(4\langle XV\rangle=b\langle XU\rangle\), which yield the first two identities. The remaining formulas follow from the same linear moment equations; \(\langle XY\rangle=0\) follows from the independent autonomous hot-site flips.

The stationary four-spin generator equation is

\[
8\langle XUVY\rangle=a(\langle VY\rangle+\langle XY\rangle)+b(\langle XU\rangle+\langle XY\rangle),
\]

hence \(\langle XUVY\rangle=ab/D\). Consequently

\[
F_0=\frac{ab}{D}-\frac{16ab}{D^2}=-\frac{a^2b^2}{D^2}.
\]

Since the distribution is invariant under simultaneous spin reversal, all four means vanish. Subtracting the *three* pair-partition products gives the connected fourth cumulant

\[
\kappa_4=\langle XUVY\rangle-\langle XU\rangle\langle VY\rangle-\langle XV\rangle\langle UY\rangle-\langle XY\rangle\langle UV\rangle=-\frac{2a^2b^2}{D^2}.
\]

**2. Uniform continuity from a graphical coupling.** Construct all chains with rate-two site clocks. At a clock ring at site \(i\), use the same independent uniform mark in the reference and perturbed systems: with probability \(\gamma_i\), copy the spin of a uniformly selected neighbor; otherwise replace the current spin by a fresh fair independent sign. The rate of an actual flip in spin configuration \(\sigma\) is precisely \(1-\gamma_i\sigma_i(\sigma_{i-1}+\sigma_{i+1})/2\), so this is the required Glauber dynamics.

Couple the \(\delta\) system to the \(\delta=0\) reference using the same marked Poisson clocks and the same independent copies, neighbors, and fair signs. A backwards ancestry for one reference spin follows a *single* chain of copying events and terminates when it reaches its first resetting event. If it terminates at a cold site, both systems reset together. If it terminates at a hot site \(i\equiv0\pmod3\), the only possible discrepancy arises when the shared uniform mark is below \(\delta\) instead of causing a reset. The stopping hot-site mark is independent of the previously exposed backwards ancestry, so the probability of such a discrepancy is at most \(\delta\), uniformly in system size and queried site. Once the reference path and the perturbed path have met identical resetting events, their sampled values agree.

It follows that each queried stationary spin can be coupled so that \(\Pr(\sigma_i^\delta\ne\sigma_i^0)\le\delta\). For a product of \(k\) distinct spins, the union bound and the fact that the product takes values in \(\{-1,1\}\) give

\[
\left|\langle\prod_{j=1}^k\sigma_{i_j}\rangle_\delta-\langle\prod_{j=1}^k\sigma_{i_j}\rangle_0\right|\le 2k\delta.
\]

Apply this to the four-spin moment (cost \(8\delta\)) and twice to the two-spin moments (each cost \(4\delta\)); using that all pair moments are in \([-1,1]\) yields

\[
|F_\delta-F_0|\le8\delta+4\delta+4\delta=16\delta.
\]

The ancestry argument is uniform in \(N\) and directly constructs both stationary infinite-chain measures because the maximal copy probability is less than one. The claimed sign and the all-finite-temperature witness follow immediately.

## Verification

The accompanying standalone `verify.py` independently constructs the complete finite-state Glauber generator, solves the stationary equations for rings of lengths six and nine, and checks seven exact rational moment formulas at \(\delta=0\). It also checks stationary residuals, positivity of probabilities, the fourth cumulant and the strict sign for the three-finite-bath example. Run with `python verify.py` after installing the packages named in `requirements.txt`. Exact rational algebra is separated from floating-point finite-generator calculations. Numerical checks do not establish the uniform-in-size or infinite-volume statement; those follow from the graphical proof.

## Relationship to prior work

Schmüser and Schmittmann (2002, arXiv:cond-mat/0206345) formulate this spatially temperature-dependent Glauber generator and study the two-temperature stationary measure perturbatively. Schmittmann and Schmüser (2002, arXiv:cond-mat/0212616), especially their Sections IV–V and Appendix A, prove ordered two-point factorization for alternating *two-temperature* stationary correlations; Section V explicitly asks whether a corresponding structure persists for periodically imposed more than two temperatures. Their one-infinite-bath special case remains two-periodic and is not claimed as new here.

Our three-periodic example is not a specialization of the alternating two-bath formula. Its negative four-spin defect proves failure of the *literal product of the two actual stationary two-point functions*—even with all three baths finite. It does not exclude suitably modified expressions with additional amplitudes or resolve the complete higher-order stationary hierarchy. Mayer and Sollich (2004) treat multispin correlations for the homogeneous Glauber chain after temperature quenches, a different temperature geometry.

## Limitations

Only period-three nearest-neighbor Glauber dynamics, the specified four consecutive spins, parameters \(0<a,b<1\), and the certified small \(\delta\) perturbation are covered. The bound \(16\delta\) is sufficient, not claimed sharp. It does not classify the full parameter region, all multispin observables, or arbitrary periods, nor does it establish the failure of every conceivable augmented factorization ansatz. This result does not establish exhaustive historical priority.

## References

1. F. Schmüser and B. Schmittmann, *Non-equilibrium stationary state of a two-temperature spin chain*, arXiv:cond-mat/0206345 (first posted 2002-06-18), `https://arxiv.org/abs/cond-mat/0206345`.
2. B. Schmittmann and F. Schmüser, *Stationary correlations for a far-from-equilibrium spin chain*, Physical Review E 66, 046130 (2002); arXiv:cond-mat/0212616 (posted 2002-12-27), `https://arxiv.org/abs/cond-mat/0212616`; DOI `10.1103/PhysRevE.66.046130`.
3. P. Mayer and P. Sollich, *General solutions for multispin two-time correlation and response functions in the Glauber–Ising chain*, Journal of Physics A 37, 9–49 (2004), DOI `10.1088/0305-4470/37/1/002`.
