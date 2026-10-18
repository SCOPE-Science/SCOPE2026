# Exact six-player mixed-order fixation thresholds on three regular hypergraph alignments

## Finding

**Theorem (complete first mixed-order ring alignment).** Let the pairwise interaction graph be the six-cycle on \(V=\mathbb Z/6\mathbb Z\), and add two disjoint three-player hyperedges whose union is \(V\). There are exactly three isomorphism classes under the dihedral symmetries of the ring, represented by the following three-player partitions:

* adjacent: \(\{0,1,2\}\mid\{3,4,5\}\);
* interlaced: \(\{0,1,3\}\mid\{2,4,5\}\);
* alternating: \(\{0,2,4\}\mid\{1,3,5\}\).

Under the precise nonlinear public-goods game and Fermi imitation update defined below, for every \(b,c,\delta_2,\delta_3>0\), the probability \(\rho_T(w)\) that a cooperator seeded uniformly at one vertex ultimately fixes satisfies
\[
\rho_T(w)=\frac16+w\left[-\frac54c+b\left(a_T+u_T\delta_2+v_T\delta_3+z_T\delta_3^2\right)\right]+O(w^2),\qquad w\downarrow0.
\]
Here the coefficients \((a_T,u_T,v_T,z_T)\) are exactly:

| Triple partition | \(a_T\) | \(u_T\) | \(v_T\) | \(z_T\) |
|---|---:|---:|---:|---:|
| adjacent | \(226939309381/975051893376\) | \(4181/31104\) | \(10860709/376177428\) | \(2514358699/121881486672\) |
| interlaced | \(1928892220173728284145/7878141219193012523808\) | \(16961/133344\) | \(20517216197359753/708975991648039284\) | \(3862525997180182316/246191913099781641369\) |
| alternating | \(23209/92016\) | \(89/720\) | \(643/23004\) | \(1481/115020\) |

All four benefit coefficients are strictly positive, so the exact weak-selection threshold for the benefit-to-cost ratio \(r=b/c\) is
\[
 r_T^*(\delta_2,\delta_3)=\frac{5}{4\left(a_T+u_T\delta_2+v_T\delta_3+z_T\delta_3^2\right)}.
\]
Consequently, for all sufficiently small positive selection intensities, cooperation is favored over neutral fixation precisely when \(r>r_T^*\), and suppressed when \(r<r_T^*\). At equality only the first-order term vanishes; no higher-order sign is asserted.

In particular, for the crossed nonlinearities \(\delta_2=1/2\), \(\delta_3=3\), with \(c=1\) and \(r=23/10\), the three critical ratios and fixation derivatives are:

| Triple partition | Critical \(r_T^*\) | \(\rho_T'(0)\) |
|---|---:|---:|
| adjacent | \(487525946688/223183700665\) | \(257965648415/3900207573504\) |
| interlaced | \(19695353047982531309520/8452601735895477225649\) | \(-2543690554229336905273/157562824383860250476160\) |
| alternating | \(1150200/472753\) | \(-628681/9201600\) |

Thus the **same six individuals, identical pair degree, identical triple degree, same payoff parameters, and uniform single-cooperator seeding** yield positive selection bias for adjacent triplets and negative bias for interlaced and alternating triplets. This is a first-order statement about ultimate fixation, not a claim about deterministic mean-field equilibria.

## Assumptions and scope

Write \(s_i\in\{0,1\}\) for the strategy at vertex \(i\), where \(1\) means cooperation. Every vertex participates in exactly two pairwise games and one three-player game. For each incident hyperedge \(e\), put \(n_e(s)=\sum_{j\in e}s_j\), and assign to vertex \(i\in e\) the payoff
\[
 \frac{b}{|e|}\sum_{j=0}^{n_e(s)-1}\delta_{|e|}^{j}-c s_i,
\]
with an empty sum interpreted as zero. The total payoff \(\pi_i(s)\) is the sum over all three incident hyperedges. The two independent nonlinearities are \(\delta_2\) and \(\delta_3\); all \(b,c,\delta_2,\delta_3\) are positive.

One update selects a focal vertex \(f\) uniformly from six vertices, then uniformly selects one of its three incident hyperedges, then uniformly selects a distinct model vertex \(m\) in that hyperedge. The focal strategy is replaced by the model strategy with probability \(\left[1+\exp(-w(\pi_m-\pi_f))\right]^{-1}\). Here \(w\ge0\) is selection intensity; no mutation or simultaneous update occurs. The initial state has exactly one cooperator, seeded uniformly among six vertices. For any finite \(w\) the only closed communicating classes are the two monochromatic states.

## Proof

**1. Completeness of the topology classification.** An unordered partition into two triplets has \(\binom63/2=10\) possibilities. The number of cycle edges lying inside one of the triplets is \(4\), \(2\), or \(0\): these correspond, respectively, to adjacent, interlaced, and alternating patterns, and account for \(3\), \(6\), and \(1\) partitions. Rotation and reflection act transitively within each of the three collections. The edge-incidence count distinguishes these three classes. Three players admit only one such topology, so six is the first feasible number of players at which placement of two disjoint triples on a cycle can vary.

**2. Neutral starting point.** Let \(W_{fm}\) be the probability of selecting model \(m\) conditional on focal \(f\). Then \(W_{fm}=1/3\) for a cycle edge \(\{f,m\}\), plus \(1/6\) if \(f,m\) lie in the same three-player hyperedge (both contributions are added when both relations hold). Hence \(W\) is symmetric, has zero diagonal, and has unit row sums. At \(w=0\), an unlike focal-model pair changes the focal with probability \(1/2\); symmetry makes the total number of cooperators a bounded martingale. Since the underlying cycle is connected, absorption in a monochromatic state occurs almost surely. Thus the neutral fixation probability from a configuration \(s\) equals \(h_0(s)=\sum_i s_i/6\).

**3. Exact first derivative.** For each of the \(62\) nonabsorbing configurations define \(P_w\) as the transition operator, and let \(Q_0\) be its restriction to transient states at neutrality. Set \(A=I-Q_0\). Differentiating the backward equation for the fixation probability at neutrality gives \(A h'_0=B\), with
\[
 B(s)=\frac1{4\cdot6^2}\sum_{f,m\in V}W_{fm}(s_m-s_f)(\pi_m(s)-\pi_f(s)).
\]
This follows directly from \(\frac{d}{dw}[1+\exp(-wz)]^{-1}_{w=0}=z/4\) and \(h_0(s^{f\leftarrow m})-h_0(s)=(s_m-s_f)/6\). The transient neutral chain is absorbing, so \(A\) is invertible. Fixation derivative from the uniformly seeded single cooperator is the average of \(h'_0(s)\) over the six singleton states.

All payoffs are linear in \(c,b,b\delta_2,b\delta_3,b\delta_3^2\), so the derivative is exactly linear in those five monomials. The rational matrix and right-hand sides can be quotiented by the finite hypergraph automorphism group. Orbit counts are \(22,34,11\), respectively, for adjacent, interlaced, alternating. The accompanying `verify.py` constructs these matrices from the game definition, solves their exact rational adjoint systems, checks the residuals and each displayed coefficient against the computed values, and exhausts the ten partitions. The standalone coefficient data are in `COEFFICIENTS.json`. These exhaustive finite computations determine, rather than estimate, the claimed rational quantities.

**4. Cost normalization.** When \(b=0\), each cooperator pays exactly \(3c\), and the instantaneous ratio of a state-increasing to state-decreasing update is \(\exp(-3cw)\), independent of the current configuration and triple placement: symmetric \(W\) pairs the two orientations of every discordant pair. The standard two-absorber birth-death calculation therefore gives, for a singleton,
\[
 \rho(w)=\frac{1-e^{3cw}}{1-e^{18cw}},
\]
whose derivative at zero is \(-5c/4\). This also independently verifies the common cost coefficient in the exact systems.

**5. Sign reversal.** Substitution \(\delta_2=1/2,\delta_3=3,c=1,b=23/10\) into the exact coefficient table yields the three nonzero fractions above: one positive and two negative. Because a finite absorbing chain has analytic transition probabilities and analytic fixation probabilities in a neighborhood of \(w=0\), each strict derivative sign persists for all sufficiently small positive \(w\). This proves the theorem.

## Verification

Run `python3 verify.py` in a directory containing the delivered `verify.py`; it uses only the Python standard library. The program builds all ten partitions, proves they form the stated three orbit classes by exhaustive group actions, forms all neutral transition rates from the update rule, verifies exact rational invertibility and the adjoint-system residuals, reconstructs every polynomial coefficient, and checks the strict sign reversal. `COEFFICIENTS.json` records coefficients as lossless rational strings. No stochastic simulations, floating-point tolerance, or external database are involved in this certificate.

## Relationship to prior work

Llabrés, Sadekar, Malizia, and Battiston (arXiv:2604.07228v1, 8 April 2026) specify the nonlinear public-goods payoff and Fermi imitation process and derive mean-field bifurcations for mixed pairs and triples; their structured experiments use much larger hypergraphs. The present theorem fixes a six-player regular mixed-order ring and determines exact finite-population fixation coefficients for every placement of two disjoint triplets. Mean-field fixed-point statements do not determine these finite absorption probabilities.

Sheng et al. (arXiv:2605.23444v1, May 2026) provide a large-population \(\ell\)-hyperedge approximation, including nonlinear public goods, for a uniform hyperedge size and a death-birth-type updating rule. Their formulas do not establish exact six-player mixed-order Fermi thresholds. McAvoy and Allen (arXiv:1908.03827) provide a general weak-selection formalism, but do not list the three alignment-specific rational values or establish the present opposite-sign comparison. Alvarez-Rodriguez et al. (arXiv:2001.10313) examine nonuniform group orders and cooperation, without this exact finite classification. The natural role of group alignment here is therefore distinct from previously reported degree heterogeneity effects.

## Limitations

This is an exact, fully classified **finite** problem restricted to the six-cycle plus a partition into two three-player games. It does not classify arbitrary mixed hypergraphs, population sizes, or update rules, and does not claim that the sign comparison holds at all positive selection strengths. The threshold is a first-order weak-selection criterion. Published results using other death-birth conventions or quasistationary densities are not interchangeable with these fixation probabilities. No claim of global novelty beyond the inspected literature and database overlap checks is logically guaranteed by finite searches; independent audit remains outstanding.

## References

1. J. Llabrés, O. Sadekar, F. Malizia, F. Battiston, *Emergence of cooperation in nonlinear higher-order public goods games*, arXiv:2604.07228v1 (first public 2026-04-08). https://arxiv.org/abs/2604.07228
2. A. Sheng, A. McAvoy, Y. Tian, S. Zhang, A. Fontan, J. B. Plotkin, *Hyperedge approximation for stochastic processes on higher-order networks*, arXiv:2605.23444v1 (2026). https://arxiv.org/abs/2605.23444
3. A. McAvoy, B. Allen, *Fixation probabilities in evolutionary dynamics under weak selection*, Journal of Mathematical Biology 82, 14 (2021), arXiv:1908.03827. https://arxiv.org/abs/1908.03827
4. U. Alvarez-Rodriguez et al., *Evolutionary dynamics of higher-order interactions in social networks*, 2020. https://arxiv.org/abs/2001.10313
