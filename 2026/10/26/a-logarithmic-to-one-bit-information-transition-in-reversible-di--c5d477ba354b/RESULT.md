# A logarithmic-to-one-bit information transition in reversible dimer adsorption

## Finding
For each integer \(m\ge 2\), consider a periodic chain with \(2m\) occupied/empty sites and two equal-sized alternating sublattices, \(U\) and \(V\). Adjacent empty pairs adsorb with positive rate \(r_{\mathrm a}\), adjacent occupied pairs desorb with positive rate \(r_{\mathrm d}\), and unequal adjacent sites may exchange at common rate \(d\ge 0\). Start with every site empty. Write \(z=\sqrt{r_{\mathrm a}/r_{\mathrm d}}\) and \(p=z/(1+z)\). Let \(I_m(d)=I(U;V)\) be stationary Shannon mutual information in **nats**.

When \(d=0\), let \(K\) count the occupied sites in *either* alternating sublattice. Then
\[
I_m(0)=H(K),\qquad
\Pr(K=j)=\frac{\binom mj^2 z^{2j}}{\sum_{k=0}^m\binom mk^2z^{2k}},\qquad 0\le j\le m.
\]
For every \(d>0\), put \(t=1-2p\) and \(q_m=(1+t^m)^2/[2(1+t^{2m})]\). Then
\[
I_m(d)=h(q_m),\qquad h(q)=-q\log q-(1-q)\log(1-q).
\]
These formulas hold for every finite \(m\) and every strictly positive adsorption/desorption rate. The positive-diffusion value is independent of the magnitude of \(d>0\).

For fixed \(0<p<1\), as \(m\to\infty\),
\[
I_m(0)=\tfrac12\log\bigl(\pi e m p(1-p)\bigr)+o(1),
\qquad I_m(d)=\log 2+o(1)\quad(d>0).
\]
Consequently the information difference between the zero-diffusion equilibrium and that for arbitrarily weak positive diffusion grows without bound with system size. The limit \(d\downarrow0\) at fixed finite size is singular: changing the rate from zero to positive opens new communicating configurations.

The fixed-density assumption matters. If \(p=p_m\) and \(mp_m\to\lambda\in(0,\infty)\), the zero-diffusion count distribution converges to the Bessel law
\[
\Pr(K_\lambda=j)=\frac{\lambda^{2j}}{(j!)^2 I_0(2\lambda)},\quad
I_0(2\lambda)=\sum_{j=0}^{\infty}\frac{\lambda^{2j}}{(j!)^2},
\]
with \(I_m(0)\to H(K_\lambda)<\infty\). For \(d>0\) the limit is \(h((1+e^{-2\lambda})^2/[2(1+e^{-4\lambda})])\). Particle–hole complementation gives the analogous sparse-vacancy regime.

At equal reaction rates, \(p=1/2\), the positive-diffusion measure makes **every proper subset of the \(2m\) sites independent fair bits**, while the two entire alternating halves still share exactly \(\log 2\) nats of mutual information. Without diffusion their mutual information instead grows as \(\tfrac12\log m\) plus an explicit constant.

## Assumptions and scope
The ring has at least four sites, with periodic nearest-neighbor bonds. Each \(00\to 11\) bond event occurs with rate \(r_{\mathrm a}>0\), its inverse \(11\to 00\) occurs at rate \(r_{\mathrm d}>0\), and \(01\leftrightarrow10\) exchanges occur at both directions with equal rate \(d\ge0\). Rates refer to each bond, not to the entire lattice. The initial state is completely empty. The two observed random vectors consist of all odd-indexed and all even-indexed physical occupancy bits, respectively, at the long-time stationary limit. Entropies are natural-logarithm Shannon entropies, and \(I_0\) in the sparse-limit formula denotes the modified Bessel function, not a mutual information.

The theorem is for the finite-state continuous-time Markov dynamics and its stationary limit. The \(m\to\infty\) statements concern a sequence of those equilibrium measures, not necessarily the stationary law of an infinite-volume dynamics. No temporal information or dynamical relaxation-rate claim is made.

## Proof
**(1) Communicating classes and stationary weights.** Every adsorption/desorption event changes the total particle number by two, so total parity is conserved. Without diffusion, each neighboring pair contains exactly one odd and one even site; therefore the difference between odd- and even-sublattice occupancies is conserved and starts at zero. Every state with equal sublattice counts is accessible: complement the even-sublattice bits, leaving the odd ones unchanged. Under this bijection an adjacent \(00\leftrightarrow11\) update becomes a nearest-neighbor \(01\leftrightarrow10\) particle exchange on the same connected ring. Starting from all physical sites empty, the transformed exclusion process has exactly \(m\) occupied transformed sites. Nearest-neighbor exclusion exchanges connect all configurations with that total, proving irreducibility on the equal-count class. If \(d>0\), physical exchanges connect all arrangements with a given total number; from any positive even number of occupied sites, rearrange an occupied pair onto adjacent sites and desorb it, iterating to the empty state. Hence the full class of even-total-count states is irreducible for \(d>0\).

Set \(\pi(x)\propto z^{|x|}\) on the relevant communicating class. Every adsorption changes \(|x|\) by two and has forward/backward rate ratio \(r_{\mathrm a}/r_{\mathrm d}=z^2\). Every physical diffusion exchange preserves \(|x|\) and is symmetric. Thus detailed balance holds across all permitted edges. Irreducibility proves that \(\pi\) is the unique limiting stationary law from the empty state in each case. Equivalently it is the law of independent \(\operatorname{Bernoulli}(p)\) bits conditioned on equal sublattice totals for \(d=0\), and conditioned on even total parity for every \(d>0\).

**(2) Conditional-independence reductions.** For \(d=0\), define \(K_U=\sum U_j\) and \(K_V=\sum V_j\). Their common value \(K\) is deterministically computable from either observed vector. Given \(K=j\), \(U\) and \(V\) are independent uniform vectors containing exactly \(j\) ones each. Therefore \(I(U;V)=I(K;V)+I(U;V\mid K)=H(K)\). Multiplicity \(\binom mj^2\) and equilibrium activity \(z^{2j}\) give the stated weights.

For \(d>0\), the parities of \(\sum U_j\) and \(\sum V_j\) are equal and are determined by either vector. Conditional on their common parity \(A\), the two vectors are independent Bernoulli-product vectors conditioned on their individual parity. Thus \(I(U;V)=H(A)\). An unconditioned \(m\)-bit Bernoulli-product vector has even-parity probability \(e_m=(1+(1-2p)^m)/2\), and odd-parity probability \(o_m=(1-(1-2p)^m)/2\). Conditioning two independent copies on equal parity gives
\[
\Pr(A=\mathrm{even})=\frac{e_m^2}{e_m^2+o_m^2}
=\frac{(1+t^m)^2}{2(1+t^{2m})}=q_m,
\]
which proves the second exact formula.

**(3) Fixed-activity entropy asymptotics.** Let \(f_{m,j}=\binom mjp^j(1-p)^{m-j}\) be the ordinary binomial probabilities. The zero-diffusion weights are exactly \(w_{m,j}=f_{m,j}^2/\sum_k f_{m,k}^2\). With \(\sigma^2=p(1-p)>0\), Stirling's formula and the binomial local central limit theorem, uniformly throughout an expanding central window with negligible complementary weight, give
\[
w_{m,j}=\frac{1+o(1)}{\sqrt{\pi m\sigma^2}}
\exp\!\left(-\frac{(j-mp)^2}{m\sigma^2}\right)
\]
in the region needed for the entropy calculation. Gaussian tails control the remaining entropy contribution. In particular
\(\operatorname{Var}_{w_m}(K)=m\sigma^2/2+o(m)\). Substituting the local asymptotic into \(-\sum_jw_{m,j}\log w_{m,j}\) gives
\[
H(K)=\tfrac12\log(\pi m\sigma^2)+\tfrac12+o(1)
=\tfrac12\log(\pi e m p(1-p))+o(1).
\]
For fixed \(p\in(0,1)\), \(|t|<1\), so \(t^m\to0\), \(q_m\to1/2\), and continuity of binary entropy gives \(h(q_m)\to\log2\).

**(4) Sparse-count crossover.** If \(mp_m\to\lambda\in(0,\infty)\), then \(m z_m\to\lambda\) and for each fixed \(j\), \(\binom mj z_m^j\to\lambda^j/j!\). Furthermore \(\binom mjz_m^j\le(mz_m)^j/j!\), and \(mz_m\) stays bounded. Dominated convergence of the normalizing series yields the Bessel count law. The same factorial majorant bounds the entropy terms and proves entropy convergence. Finally \((1-2p_m)^m\to e^{-2\lambda}\), giving the positive-diffusion limit. Exchanging particles and vacancies treats \(m(1-p_m)\to\lambda\).

**(5) Hidden dependence at equal rates.** At \(p=1/2\) with any positive diffusion, the stationary measure is uniform over even-parity bit strings. Every assignment of values to fewer than \(2m\) coordinates has exactly the same number of parity-completing extensions, so every proper marginal is an independent fair-bit product measure. The common parity of the full two alternating blocks is still uniform, hence their mutual information equals \(\log 2\). This information is genuinely global, and cannot be inferred from any proper-site marginal.

## Verification
An independent finite-state calculation constructs the generator from all permitted nearest-neighbor events, solves its stationary linear equations, checks detailed balance against the proposed weighted measure, and evaluates mutual information directly from the full state probability table. The accompanying \(check.py\) passes 30 combinations of ring sizes from four to eight sites, activities \(p\in\{0.18,0.5,0.76\}\), and zero/positive diffusion. Its maximum accepted generator, probability, and information discrepancy is \(2\times10^{-10}\). It also compares the fixed-density entropy asymptotic at sizes up to \(m=10000\), checks four dilute Bessel crossover values up to \(m=3000\), and checks the equal-rate parity entropy. These finite computations corroborate but do not replace the all-size proofs above. Run with Python 3, NumPy, and SciPy: \(\texttt{python check.py}\).

## Relationship to prior work
Mercado, Jung, Kim, Garcia, Nonaka and Bell, *Surface Coverage Dynamics for Reversible Dissociative Adsorption on Finite Linear Lattices* (arXiv:2212.12286, first public version 2022-12-23), derive the finite-ring accessible configuration classes, detailed-balance equilibrium weights, coverage and local two-site correlations, and the singular effect of diffusion on accessible configurations (Sections III–IV and Appendices). Those structural prerequisites are prior results and are **not** claimed as new. The present contribution is the exact global checkerboard mutual-information reduction to a conserved count or a parity bit, its logarithmic-versus-one-bit thermodynamic classification, and the dilute Bessel crossover. Their stationary configuration formulas permit these quantities to be computed, so this is a derived information-theoretic consequence of that model, not a new stationary ensemble.

Wilms, Troyer and Verstraete (arXiv:1011.4421) analyze classical spin-model mutual information using different Gibbs ensembles and spatial partitions, not the conserved checkerboard classes under reversible pair adsorption. Mobilia (arXiv:cond-mat/0204148) studies time-dependent multi-point correlations in a dimer adsorption/evaporation model; the stationary alternating-sublattice mutual-information transition above is not established there. Generic conditional-entropy identities and binomial asymptotics are standard tools and not asserted to be discoveries.

## Limitations
The result assumes a periodic even ring, initially empty, strictly positive reversible pair rates, and symmetric nearest-neighbor hopping when present. It concerns the entire interlaced checkerboard halves rather than contiguous spatial intervals. The discontinuity is for the limit of the stationary distribution as diffusion changes from zero to positive: mixing times may diverge as \(d\downarrow0\), and no instantaneous dynamical discontinuity is asserted. The \(\tfrac12\log m\) law assumes fixed interior activity \(p\); the sparse crossover explicitly shows why it cannot be extrapolated to vanishing occupancy. At zero diffusion, other initial communicating classes lead to different stationary laws. Information-theoretic derivations equivalent to these identities may exist in broader conditional-Bernoulli literature; definitive publication priority has not been independently established.

## References
1. E. Mercado, H. T. Jung, C. Kim, A. L. Garcia, A. J. Nonaka and J. B. Bell, *Surface Coverage Dynamics for Reversible Dissociative Adsorption on Finite Linear Lattices*, arXiv:2212.12286, first posted 2022-12-23; Sections III–IV, Appendix A; https://arxiv.org/abs/2212.12286.
2. J. Wilms, M. Troyer and F. Verstraete, *Mutual information in classical spin models*, arXiv:1011.4421; https://arxiv.org/abs/1011.4421.
3. M. Mobilia, *Exact multipoint and multitime correlation functions of a one-dimensional model of adsorption and evaporation of dimers*, arXiv:cond-mat/0204148; https://arxiv.org/abs/cond-mat/0204148.
