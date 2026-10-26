# A parity-repaired Poisson crossover for competitive monomer–dimer adsorption on complete graphs

## Finding

**Theorem (uniform weak-rate approximation).** Let \(n\ge4\) be an integer. Initially every vertex of the complete graph \(K_n\) is empty. Each empty vertex accepts an irreversible monomer at rate \(\varepsilon\), and each edge whose two endpoints are empty accepts an irreversible dimer at rate one, independently, with no removal. Let \(K_n^{\mathrm{mon}}\) be the total number of vertices finally occupied by monomers. For \(0<\varepsilon\le1/4\), put
\[
m=\lfloor n/2\rfloor,\qquad
\lambda_n=\varepsilon\sum_{j=2}^{m}\frac1j,
\qquad R_n(k)=k+\mathbf 1_{\{n-k\text{ odd}\}}.
\]
If \(P_n\) is Poisson with mean \(\lambda_n\), then
\[
\boxed{d_{\mathrm{TV}}\bigl(\mathcal L(K_n^{\mathrm{mon}}),\mathcal L(R_n(P_n))\bigr)\le5\varepsilon.}
\]
The distribution on the right is a Poisson law **rounded upward to the parity of \(n\)**; it is not a Poisson law conditioned to have that parity. At every finite \(n\), conditional on \(K_n^{\mathrm{mon}}=k\), the set of monomer-labelled vertices is uniformly distributed over the \(\binom nk\) subsets.

In particular, for fixed \(c>0\) and \(\varepsilon_n=c/\log n\), the total-variation error against \(R_n(P)\), with \(P\sim\operatorname{Poisson}(c)\), is \(O_c((\log n)^{-1})\). Along even and odd sizes, respectively, its limiting probability generating functions are
\[
\boxed{\mathbb E z^{K_{\mathrm{even}}}=e^{-c}\bigl(\cosh(cz)+z\sinh(cz)\bigr),\quad
\mathbb E z^{K_{\mathrm{odd}}}=e^{-c}\bigl(\sinh(cz)+z\cosh(cz)\bigr).}
\]
For example, the even-size probability of no monomers tends to \(e^{-c}\), whereas the odd-size probability of exactly one monomer tends to \((1+c)e^{-c}\). The limiting mean monomer counts are \(c+(1-e^{-2c})/2\) on even sizes and \(c+(1+e^{-2c})/2\) on odd sizes.

More generally, the first boxed bound holds for arbitrary sequences \(\varepsilon_n\to0\). Hence if \(\varepsilon_n\log n\to0\), the final count equals the minimum possible parity count with probability tending to one; if \(\varepsilon_n\log n\to\infty\), then, with \(\lambda_n\) as above,
\[
\frac{K_n^{\mathrm{mon}}-\lambda_n}{\sqrt{\lambda_n}}\ \xrightarrow{d}\ \mathcal N(0,1).
\]
The latter Gaussian limit concerns the large-mean regime and is a consequence of the same Poisson approximation, not a separate finding.

## Assumptions and scope

The substrate is exactly \(K_n\), not a sparse or geometric lattice. All monomer proposal clocks have the same positive rate \(\varepsilon\); all possible dimer edges have unit-rate clocks. A successful adsorption permanently removes its one or two endpoints from the vacancy set. Independent exponential clocks make the current vacant-vertex count a decreasing Markov chain. No equilibrium monomer–dimer Gibbs weighting or desorption is assumed. The number of accepted deposition events is finite almost surely, because each removes at least one vacant vertex and a monomer can always occupy the last vacant vertex. Total variation uses \(d_{\mathrm{TV}}(\mu,\nu)=\sup_A|\mu(A)-\nu(A)|\). The finite-size inequality assumes \(n\ge4\), \(0<\varepsilon\le1/4\); the asymptotics keep \(c\) fixed, or otherwise require \(\varepsilon_n\to0\) as stated.

## Proof

**1. Exact vacancy-chain reduction.** At \(k\ge2\) vacant vertices, the total eligible monomer rate is \(k\varepsilon\) and the total eligible dimer rate is \(\binom{k}{2}\). Consequently the next accepted event removes one vertex with probability
\[
q_k=\frac{k\varepsilon}{k\varepsilon+\binom{k}{2}}=\frac{2\varepsilon}{k-1+2\varepsilon},
\]
and otherwise removes two. At \(k=1\), the final event is necessarily a monomer. This supplies an exact finite recursion for the count polynomial \(G_k(z)\):
\[
G_0(z)=1,\quad G_1(z)=z,\quad
G_k(z)=q_k zG_{k-1}(z)+(1-q_k)G_{k-2}(z),\quad k\ge2.
\]
In particular, exactly \(n-K_n^{\mathrm{mon}}\) vertices are consumed by dimers, so \(K_n^{\mathrm{mon}}\equiv n\pmod2\).

**2. Couple rare voluntary monomers to independent Bernoulli events.** Choose independent uniforms \(U_k\), \(2\le k\le n\), to decide a monomer at visited vacancy state \(k\) when \(U_k\le q_k\). Partition the state numbers above two into pairs \(\{2j,2j-1\}\), \(2\le j\le m\). Every decreasing path with steps of size one or two visits at least one state in each pair. Its *first* visited state in pair \(j\), denoted \(V_j\), is determined before either of the uniforms in that pair is exposed. Define
\[
B_j=\mathbf1_{\{U_{V_j}\le\varepsilon/j\}}.
\]
Although \(V_j\) is random, its choice is predictable from states above the pair. Therefore, by conditioning successively on the previous choices, the \(B_j\) are mutually independent and \(\Pr(B_j=1)=\varepsilon/j\). Put \(B=\sum_{j=2}^{m}B_j\); its mean is \(\lambda_n\).

For every \(j\ge2\) and \(0<\varepsilon\le1/4\), direct subtraction gives
\[
\left|q_{2j}-\frac\varepsilon j\right|\le\frac\varepsilon{j^2},\qquad
\left|q_{2j-1}-\frac\varepsilon j\right|\le\frac{2\varepsilon}{j^2}.
\]
Thus first-visit monomer indicators can be coupled with the \(B_j\), with a total mismatch probability at most \(2\varepsilon\sum_{j=2}^{\infty}j^{-2}\). A second state in a pair can be visited only when a first visit at \(2j\) deposits a monomer. The probability that this *second* visit also deposits a monomer is at most \(q_{2j}q_{2j-1}\), whose total sum is bounded by
\[
4\varepsilon^2\sum_{j=2}^{\infty}\frac1{(2j-1)(2j-2)}
=4\varepsilon^2(1-\log2).
\]
The optional monomer at vacancy state two has probability at most \(q_2\le2\varepsilon\); for odd \(n\), the unpaired initial state \(n\) contributes at most \(q_n\le\varepsilon/2\). Let \(K_n^*\) count monomer depositions at states \(k\ge2\), excluding the compulsory final state \(k=1\). A union bound therefore gives
\[
d_{\mathrm{TV}}\bigl(\mathcal L(K_n^*),\mathcal L(B)\bigr)
\le \left(\frac52+2\sum_{j=2}^{\infty}j^{-2}\right)\varepsilon
+4(1-\log2)\varepsilon^2.
\]
Le Cam's elementary independent-Bernoulli Poisson bound gives
\[
d_{\mathrm{TV}}\bigl(\mathcal L(B),\operatorname{Poisson}(\lambda_n)\bigr)
\le2\varepsilon^2\sum_{j=2}^{\infty}j^{-2}.
\]
Since \(\varepsilon\le1/4\), the sum of the last two displayed bounds is less than \(5\varepsilon\). No independence assumption was made about the original accepted adsorption events.

**3. Exact parity repair.** At termination, the one possible remaining monomer at vacancy count one is compulsory precisely when \(n-K_n^*\) is odd. Thus, path by path,
\[
K_n^{\mathrm{mon}}=R_n(K_n^*).
\]
A deterministic map cannot increase total-variation distance. Apply \(R_n\) to the coupling in step 2 to obtain the finite-size theorem.

**4. Critical window, mean and larger-mean consequences.** For \(m=\lfloor n/2\rfloor\), \(\sum_{j=2}^{m}j^{-1}=\log n+O(1)\). If \(\varepsilon_n=c/\log n\), then \(|\lambda_n-c|=O_c((\log n)^{-1})\), and Poisson distributions of two means differ by at most the absolute difference of their means in total variation. The displayed generating functions follow by splitting a Poisson law into its even and odd terms; the parity-repair map contributes a factor \(z\) to the opposite-parity terms. Using \(\mathbb E P=c\) and \(\Pr(P\text{ odd})=(1-e^{-2c})/2\) gives the stated means. For an arbitrary vanishing sequence \(\varepsilon_n\), the finite bound tends to zero. If \(\lambda_n\to\infty\), the Poisson central limit theorem and \(0\le R_n(P_n)-P_n\le1\) give the Gaussian limit; if \(\lambda_n\to0\), the parity-minimal count occurs with probability tending to one.

**5. Label exchangeability.** Every vertex and every edge of \(K_n\) has the same rate as all of its kind. Relabelling vertices preserves the full adsorption law, and the permutation group acts transitively on all subsets of a given size. Therefore the final monomer-label set is exactly uniform conditional on its cardinality. This is an exchangeability consequence, not a geometric assertion about positions on \(K_n\).

## Verification

The standalone file `verify.py` implements two independent finite-state descriptions: a rational recursion for the total monomer count and a separate exact recursion over labelled vacant subsets and terminal monomer labels. It verifies their agreement, exact conditional label uniformity and count parity on small graphs. An additional direct product check covers the probability of all-dimer deposition on even graphs. Larger numerical recurrences compare the finite distributions with the parity-repaired Poisson prediction. The program uses only the Python standard library and can be run as `python verify.py`. These finite calculations are diagnostic; all infinite-size conclusions rest on the analytical coupling above.

## Relationship to prior work

Random sequential adsorption, including mixed monomer–dimer species, has a substantial literature. Cadilhe and Privman (2003/2004) analyze competitive deposition on a pretreated infinite Bethe lattice; their accessible source and first-page preview concern a fixed-connectivity infinite tree rather than a complete graph with an \(n\)-dependent vanishing monomer rate. Pippenger (1989) treats random sequential graph adsorption and edge occupation, including a large-girth setting; the available abstract does not supply this mixed-species rare-rate theorem. Chen (2015) analyzes monomer-number fluctuations for an *equilibrium Gibbs measure* on complete graphs, including imitative interactions; its displayed Hamiltonian and stationary Gibbs law are not the irreversible kinetic vacancy chain considered here. Boscoboinik, Manzi and Pereyra (2010) examine a kinetic lattice-gas monomer–dimer mixture with adsorption/desorption/diffusion. These models are not interchangeable even when the terms “monomer–dimer” and “complete graph” coincide.

The novel candidate asserted here is specifically the **uniform weak-monomer-rate Poisson coupling, its upward parity repair rather than parity conditioning, and the logarithmic crossover for the terminal count**. It is not a claim to have originated monomer–dimer adsorption, the parity identity \(2D+K=n\), or the Poisson approximation theorem. Full texts of several nearby older kinetic papers were not accessible in this review; a more general matching-process result could imply some or all of the claim. Priority beyond the inspected evidence is not asserted.

## Limitations

The result assumes a complete graph, irreversible monomer or dimer placement, uniform independent exponential clocks, and a weak monomer rate. The explicit \(5\varepsilon\) error is not informative for nonvanishing rates, and does not describe sparse graphs, finite-dimensional substrates, reversible adsorption, species-dependent site activities, or deposition durations. Conditional vertex-label uniformity reflects graph symmetry, not a physical spatial point process. The published-source comparison is finite and not exhaustive; no independent scientific audit has been performed.

## References

1. A. M. R. Cadilhe and V. Privman, “Random Sequential Adsorption of Mixtures of Dimers and Monomers on a Pre-Treated Bethe Lattice,” arXiv:cond-mat/0311190, first publicly posted 2003-11-08; *Modern Physics Letters B* 18 (2004), 207–211, doi:10.1142/S0217984904006846.
2. N. Pippenger, “Random Sequential Adsorption on Graphs,” *SIAM Journal on Discrete Mathematics* 2 (1989), 393–401, doi:10.1137/0402034.
3. W.-K. Chen, “Limit Theorems in the Imitative Monomer-Dimer Mean-Field Model via Stein's Method,” arXiv:1506.08484 (2015), doi:10.1063/1.4960673.
4. J. A. Boscoboinik, S. J. Manzi and V. D. Pereyra, “Adsorption–desorption kinetics of the monomer–dimer mixture,” *Physica A* 389 (2010), 1317–1328, doi:10.1016/j.physa.2009.12.018.
5. J. W. Evans, “Random and cooperative sequential adsorption,” *Reviews of Modern Physics* 65 (1993), 1281–1329, doi:10.1103/RevModPhys.65.1281.
