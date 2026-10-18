# Exact fourth-order entropy production in the asymmetric metric kinetic Ising model

## Finding

For the finite periodic square-lattice kinetic Ising chain specified below, the stationary entropy production **per site and parallel update** has the following high-temperature expansion for every integer \(L\geq3\) and every \(0\leq\alpha\leq1\):

\[
\mathcal E_L(J,\alpha)=(1-\alpha)^2J^2-\frac{(1-\alpha)^2}{3}\left(7+\alpha+\alpha^2+3\alpha\mathbf1_{\{L=4\}}\right)J^4+O_{L,\alpha}(J^6),\qquad J\to0.
\]

The coefficient of \(J^4\), normalized by \((1-\alpha)^2\) away from \(\alpha=1\), depends nontrivially on the asymmetry parameter. Thus an exactly factorized entropy production \(\mathcal E_L(J,\alpha)=f(J,L)(1-\alpha)^2\) with \(f\) independent of \(\alpha\) is impossible in every neighborhood of \(J=0\). A four-site circumference has a special correction \(-\alpha(1-\alpha)^2J^4\), absent for circumference three or at least five. This is a finite-size wrapping effect; it is not a claim about criticality or thermodynamic-limit scaling.

## Assumptions and scope

Fix \(L\in\mathbb Z\) with \(L\geq3\). Let \(\Lambda_L=(\mathbb Z/L\mathbb Z)^2\), and let each site carry an Ising spin \(\sigma_i\in\{-1,1\}\). Set \(\alpha\in[0,1]\), \(J\in\mathbb R\), and for \(i=(x,y)\), use the local field

\[
h_i(\sigma)=J S_i(\sigma),\qquad S_{(x,y)}=\sigma_{(x-1,y)}+\alpha\sigma_{(x+1,y)}+\sigma_{(x,y-1)}+\sigma_{(x,y+1)}.
\]

Each discrete time step simultaneously samples all new spins independently given the previous configuration, with transition probability

\[
P_{J,\alpha}(\eta\mid\sigma)=\prod_{i\in\Lambda_L}\frac{\exp(\eta_i h_i(\sigma))}{2\cosh h_i(\sigma)}.
\]

All transitions are strictly positive, so the finite chain has a unique stationary law \(\pi_{J,\alpha}\). Define its dimensionless stationary two-time entropy production per site by the exact path-reversal Kullback–Leibler divergence

\[
\mathcal E_L(J,\alpha)=\frac1{L^2}\sum_{\sigma,\eta}\pi_{J,\alpha}(\sigma)P_{J,\alpha}(\eta\mid\sigma)\log\frac{\pi_{J,\alpha}(\sigma)P_{J,\alpha}(\eta\mid\sigma)}{\pi_{J,\alpha}(\eta)P_{J,\alpha}(\sigma\mid\eta)}.
\]

All Taylor expansions are for a **fixed finite** \(L\) and fixed \(\alpha\). At \(\alpha=1\), detailed balance makes \(\mathcal E_L=0\) exactly. No infinite-volume analyticity or uniformity as \(L\to\infty\) is asserted.

## Proof

**1. Exact flux formula.** Stationarity makes the mean of \(\log\pi(\sigma)-\log\pi(\eta)\) vanish. The terms \(\sum_i\log 2\cosh h_i\) cancel under stationarity as well. Conditional expectation of the updated spin is \(\mathbb E[\eta_i\mid\sigma]=\tanh(JS_i(\sigma))\). Consequently,

\[
\mathcal E_L=\frac{J}{L^2}\sum_{i,j}(w_{ij}-w_{ji})\mathbb E_{\pi_{J,\alpha}}[\sigma_j\tanh(JS_i)],
\]

where \(w_{ij}\) are the four dimensionless local-field coefficients and zero otherwise. Translation symmetry, the reciprocal vertical bonds, and left-right horizontal orientation reduce this to

\[
\mathcal E_L=J(1-\alpha)\bigl(\mathbb E_\pi[\sigma_{(-1,0)}\tanh(JS_0)]-\mathbb E_\pi[\sigma_{(1,0)}\tanh(JS_0)]\bigr).
\tag{1}
\]

**2. Analyticity and second-order correlations.** Strict positivity implies the simple stationary eigenvector is analytic in \(J\) around zero. Global spin inversion leaves \(P_{J,\alpha}\) invariant, whereas changing \(J\) to \(-J\) changes the sign of every updated spin. Uniqueness therefore gives \(\pi_{-J,\alpha}=\pi_{J,\alpha}\), so stationary moments of products of even numbers of spins are even analytic functions of \(J\).

Write \(C_{ij}=\mathbb E_\pi[\sigma_i\sigma_j]\). For \(i\ne j\), independent parallel updates conditioned on \(\sigma\) give

\[
C_{ij}=\mathbb E_\pi[\tanh(JS_i)\tanh(JS_j)]=J^2\sum_k w_{ik}w_{jk}+O(J^4).
\tag{2}
\]

For \(i=j\), \(C_{ii}=1\) exactly, not the right-hand side of (2). The zeroth-order stationary measure at \(J=0\) is the independent fair-spin product law.

**3. Cubic expansion of the flux.** For \(j\) equal to either horizontal neighbor of the origin,

\[
\begin{aligned}
\mathbb E_\pi[\sigma_j\tanh(JS_0)]
&=Jw_{0j}+J^3\left(\sum_{k\ne j}w_{0k}\sum_\ell w_{k\ell}w_{j\ell}-\tfrac13 \mathbb E_0[\sigma_jS_0^3]\right)+O(J^5),\\
\mathbb E_0[\sigma_jS_0^3]&=3w_{0j}(3+\alpha^2)-2w_{0j}^3.
\end{aligned}
\tag{3}
\]

The cubic identity follows by expanding the cube and retaining only those monomials with even multiplicities after multiplication by \(\sigma_j\). Every step uses four **distinct** neighbors, ensured by \(L\geq3\).

Let \(A_j=\sum_{k\ne j}w_{0k}\sum_\ell w_{k\ell}w_{j\ell}\), and let \(B_j=\mathbb E_0[\sigma_jS_0^3]\). Enumerating the four local interaction directions gives the complete, finite table

| Circumference | \(A_{(-1,0)}\) | \(A_{(1,0)}\) | \(B_{(-1,0)}\) | \(B_{(1,0)}\) |
|---|---|---|---|---|
| \(L=3\) or \(L\geq5\) | \(\alpha^2+2\alpha+2\) | \(3\alpha+2\) | \(7+3\alpha^2\) | \(9\alpha+\alpha^3\) |
| \(L=4\) | \(2\alpha^2+2\alpha+2\) | \(4\alpha+2\) | \(7+3\alpha^2\) | \(9\alpha+\alpha^3\) |

These are not extrapolations from finite sample sizes. To verify every entry for **all** circumferences, note that the input-neighbor sets of the left and right horizontal neighbors have exactly one common site, the origin, when \(L=3\) or \(L\geq5\); their weight-product there is \(\alpha\). When \(L=4\), they have a second common site at horizontal displacement two, also of weight-product \(\alpha\). Each of the upper and lower neighbors has exactly two common input sites with either horizontal neighbor, of combined weight-product \(1+\alpha\), for every \(L\geq3\). Thus \(A_{(-1,0)}=\alpha[\alpha+\alpha\mathbf1_{\{L=4\}}]+2(1+\alpha)\) and \(A_{(1,0)}=\alpha[1+\mathbf1_{\{L=4\}}]+2(1+\alpha)\), which are precisely the table entries. The only modular coincidence changes the horizontal common-input count at \(L=4\). The standalone integer-lattice enumerator independently reconstructs the table in representative finite sizes.

Subtract (3) for the two horizontal neighbors. Using the table yields

\[
\mathbb E_\pi[\sigma_{(-1,0)}\tanh(JS_0)]-\mathbb E_\pi[\sigma_{(1,0)}\tanh(JS_0)]
=(1-\alpha)J-\frac{1-\alpha}{3}(7+\alpha+\alpha^2+3\alpha\mathbf1_{\{L=4\}})J^3+O(J^5).
\]

Multiplication by \(J(1-\alpha)\) in (1) gives the theorem. In particular, comparison of \(\alpha=0\) and \(\alpha=1/2\), after division by \((1-\alpha)^2\), changes the \(J^4\) coefficient from \(-7/3\) to \(-31/12\) for \(L\ne4\), or to \(-37/12\) for \(L=4\). These unequal coefficients preclude exact quadratic factorization.

## Verification

The self-contained Python 3 program `check_entropy_series.py` uses exact rational-polynomial arithmetic, creates the finite-torus neighbor map from the model specification, and computes the length-two common-input sums and fair-spin cubic contractions independently of their closed expressions. Running `python3 check_entropy_series.py` completes **207 exact assertions**, covering every circumference \(3\leq L\leq25\) and several rational asymmetry values. The universal extension to all larger \(L\) is justified by the bounded-length displacement congruence argument in the proof, not by the finite testing range.

Separately, a direct 512-state stationary transition-matrix calculation on the \(3\times3\) torus, without using the correlation expansion, was checked at \(\alpha\in\{0,0.4,0.75\}\) and decreasing positive \(J\). Its deviations are consistent with sixth-order remainders. This is a finite numerical corroboration, not a second proof of the theorem.

## Relationship to prior work

Di Carlo's 2024 preprint, and the 2025 journal version, define the same asymmetric metric parallel-update kinetic Ising lattice and derive an exact entropy-flux identity. Their stated factorized \((1-\alpha)^2\) dependence is a numerical/coarse-grained **ansatz**, not a rigorously established microscopic identity. The present calculation derives the first asymmetry-dependent relative correction, identifies the four-site wrapping exception, and shows where exact factorization fails at high temperature. It does not dispute the utility of the reported numerical approximation near criticality.

Aguilera, Moosavi and Shimazaki (2021) formulate asymmetric kinetic Ising mean-field theories and general stationary entropy-production identities; no exact local fourth-order coefficient for this finite square-lattice model is given there. Aguilera, Igarashi and Shimazaki (2023) study the asymmetric Sherrington–Kirkpatrick model, not this metric torus. Nartallo-Kaluarachchi and collaborators (2024) numerically study entropy production and nonlinearity in directed-network Ising dynamics, but not this particular exact four-neighbor fourth-order expansion. A broader published lattice perturbation theorem could still imply the result; no exhaustive priority claim is made.

## Limitations

The remainder is for fixed finite \(L\) and fixed \(\alpha\). No phase-transition conclusions, thermodynamic-limit expansion, positivity estimate at finite \(J\), or globally monotone entropy-production curve is proved. The quantitative correction is a high-temperature microscopic statement and need not visibly dominate measurements at moderate coupling. A published treatment using an equivalent orientation convention or a general exact series expansion could establish prior coverage; independent literature assessment remains desirable.

## References

1. L. Di Carlo, *The off-equilibrium Kinetic Ising model: The Metric Case*, arXiv:2408.11690v1, posted 2024-08-21; *Physical Review Research* **7**, 013250 (2025), DOI:10.1103/PhysRevResearch.7.013250.
2. M. Aguilera, S. Moosavi, and H. Shimazaki, *A unifying framework for mean-field theories of asymmetric kinetic Ising systems*, *Nature Communications* **12**, 1197 (2021), DOI:10.1038/s41467-021-20890-5.
3. M. Aguilera, M. Igarashi, and H. Shimazaki, *Nonequilibrium thermodynamics of the asymmetric Sherrington–Kirkpatrick model*, *Nature Communications* **14**, 3685 (2023), DOI:10.1038/s41467-023-39107-y.
4. R. Nartallo-Kaluarachchi, M. Asllani, G. Deco, M. L. Kringelbach, A. Goriely, and R. Lambiotte, *Broken detailed balance and entropy production in directed networks*, arXiv:2402.19157 (2024); *Physical Review E* **110**, 034313 (2024), DOI:10.1103/PhysRevE.110.034313.
