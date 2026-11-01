# A complete Catalan-logarithm census of relaxation layers in cyclic traffic Rule 184

## Finding

Consider the deterministic traffic cellular automaton Rule 184 on \(\mathbb Z/n\mathbb Z\) with \(n\ge2\). Let \(k\) sites initially hold a particle, and put \(m=\min\{k,n-k\}\). Define \(T\) to be the first update at which the orbit is periodic. With \(C_j=\frac{1}{j+1}\binom{2j}{j}\), define the finite bivariate polynomial
\[
B_t(u,z)=u+\sum_{j=1}^{t+1}C_{j-1}u^{2j}z^j
\qquad (t\ge0).
\]
Then the number of **labelled initial ring configurations** with \(k\) particles and \(T\le t\) is exactly
\[
\boxed{R_{n,k}(t)=n\,[u^nz^m]\log\frac{1}{1-B_t(u,z)}.}
\]
The complete first-entry distribution is \(R_{n,k}(t)-R_{n,k}(t-1)\), with \(R_{n,k}(-1)=0\). The logarithm is a formal power series, so the formula is exact rational arithmetic whose final coefficients are integers. It applies for every \(n\ge2\), every \(0\le k\le n\), and every integer \(t\ge0\); no limiting approximation is used.

For example, for \((n,k)=(8,4)\), the counts with \(T=0,1,2,3\) are respectively \(2,12,16,40\); for \((n,k)=(10,4)\), they are \(25,75,60,50\). An established extremal-layer identity is recovered as a special case: for \(m\ge2\), \(T\le m-1\), and exactly \(nC_{m-1}\) configurations have \(T=m-1\). The full distribution formula, not this known extremal special case, is the finding here.

## Assumptions and scope

At every integer time, each particle moves one lattice site clockwise if that target site is empty; otherwise it remains. All moves are simultaneous. Equivalently, for binary states \(x_i\in\{0,1\}\) and indices modulo \(n\),
\[
(Fx)_i=x_i x_{i+1}+(1-x_i)x_{i-1}.
\]
The number \(k\) of occupied sites is conserved. If \(k\le n/2\), the eventual periodic region consists of words having no cyclic block \(11\): every particle then advances one cell each update. If \(k\ge n/2\), exchange particle/hole and reverse orientation to obtain the dual region without a cyclic block \(00\). At equality the periodic words alternate. In empty and full sectors \(T=0\). We count physical binary words at fixed labelled sites, not rotation classes.

A **primitive positive Dyck block** of semilength \(j\ge1\) is a length-\(2j\) binary word containing \(j\) ones and \(j\) zeros, with all nonempty proper prefix sums of \(\#1-\#0\) strictly positive. It starts with \(1\) and ends with \(0\), and there are \(C_{j-1}\) such words. Throughout the proof, cyclic binary words are read in the direction opposite particle motion.

## Proof

**Step 1: a finite-time obstruction.** The standard local preimage characterization for Rule 184 (Fukś [1], Proposition 1, with particle-hole reversal) states the following. Read the \(2t+2\) initial sites in the backward light cone of an adjacent occupied pair at time \(t\) opposite the particle direction. The pair occurs if and only if the cone word begins with \(11\) and every nonempty prefix has strictly positive \(\#1-\#0\). This follows also by inductively cancelling the opposite-moving \(11\) and \(00\) defects. The criterion is local and remains valid on an \(n\)-cycle whenever \(2t+2\le n\), since the cone contains no repeated initial site.

Suppose \(k\le n/2\). For \(0\le t\le k-1\), the preimage criterion says that some \(11\) remains at time \(t\) exactly when the initial cyclic word contains a strictly positive prefix of length \(2t+2\) beginning \(11\). Such a prefix extends clockwise in the chosen reading orientation until its first return to height zero, since the full circuit has nonpositive total height \(2k-n\). That first-return block is a primitive positive Dyck block of semilength \(j\ge t+2\). Conversely, every primitive positive Dyck block with \(j\ge t+2\) supplies the required initial prefix of length \(2t+2\). Hence
\[
T\le t\quad\Longleftrightarrow\quad
\text{every maximal primitive positive Dyck block has semilength at most }t+1.
\]
For \(t=k-1\), no forbidden primitive block can occur because it would contain at least \(k+1\) particles. Thus all sectors stabilize by \(k-1\) steps, and for larger \(t\) the condition remains automatically true. For \(k=0,1\), stabilization is immediate. Particle-hole reflection gives the assertion for \(k>n/2\).

**Step 2: unique circular primitive-factor decomposition.** In any binary cyclic word with no more ones than zeros, match each \(1\) to its first following \(0\) (in the chosen cyclic reading orientation) at which the intervening one-minus-zero height first returns to zero. Existence follows from the nonpositive total height around the circle. These matches are noncrossing. Their outermost arcs are pairwise disjoint primitive positive Dyck blocks; all remaining letters are unmatched singleton zeros. This decomposition is unique as a **cyclic** sequence of atoms, and it reconstructs the original cyclic word. The atom classes are therefore: one singleton \(0\), weighted \(u\), and \(C_{j-1}\) primitive positive Dyck words, each weighted \(u^{2j}z^j\). Restricting every primitive semilength to \(j\le t+1\) gives exactly the atom polynomial \(B_t(u,z)\).

**Step 3: cycle counting with a distinguished lattice site.** Fix the number \(r\ge1\) of atoms. Their ordered circular arrangements contribute \(B_t(u,z)^r/r\) when the atom boundary is unmarked. A cyclic binary word occupying \(n\) labelled sites has \(n\) choices of distinguished physical site, so the corresponding contribution is \(nB_t(u,z)^r/r\). This orbit-counting equality remains correct for arrangements with rotational stabilizers, since the factors \(n\) and \(1/r\) count marks with their multiplicities. Summing over \(r\ge1\) yields
\[
\sum_{r\ge1}\frac{n}{r}[u^nz^m]B_t(u,z)^r
=n[u^nz^m]\log\frac{1}{1-B_t(u,z)}.
\]
This counts exactly those words with \(T\le t\) by Steps 1–2. Taking successive differences proves every exact-depth count.

**Step 4: the recovered extremal identity.** If \(m\ge2\), the only new atom when \(t\) increases from \(m-2\) to \(m-1\) is a primitive block of semilength \(m\), contributing \(C_{m-1}u^{2m}z^m\). In the \(z^m\) coefficient, other atoms with positive \(z\)-degree cannot coexist with it. The remaining atoms are singleton zeros, so its contribution to the logarithm is \(C_{m-1}u^{2m}z^m/(1-u)\), and \(R_{n,k}(m-1)-R_{n,k}(m-2)=nC_{m-1}\). This is an independent consistency check with the known extremal-layer classification, not an independent originality claim.

## Verification

Run `python3 verify.py` in the same directory as this document. The verifier independently constructs synchronous particle moves and determines eventual-cycle entry by full state-orbit repetition. It then computes the proposed coefficient by finite exact rational summation over cyclic atom counts, independently of the simulation. It checks every binary state for all ring sizes \(2\le n\le15\), every mass sector and every feasible time; it also checks \(5,460\) local preimage words with an independent ballot predicate. The recorded output is in `verification_output.txt`, with the expected final line `TRAFFIC_CATALAN_LOG_VERIFY_OK`. These finite checks supplement rather than replace the proof for all \(n\).

## Relationship to prior work

Fukś [1] establishes local ballot-preimage criteria and a uniform finite-ring classification-time bound. Fukś [2] derives infinite-volume traffic-flow formulas from block preimages. Those local and averaged statements motivate the proof, but do not state the simultaneous fixed-mass, fixed-ring, all-time first-periodic-entry distribution above. The later first-passage study [3] analyzes stopping times of **individual particles**, rather than the maximum stopping time over all particles on a fixed finite labelled ring; its full text was not retrieved for this assessment. Results on probabilistic exclusion processes with different update mechanisms [4] should not be identified with the deterministic Rule-184 first-entry census without a proven reduction. The earlier exact extremal-layer count \(nC_{m-1}\) is already known; it is only recovered here.

## Limitations

The theorem concerns deterministic parallel Rule 184, not stochastic TASEP or asynchronous updates. Its explicit coefficients use a truncated Catalan logarithm rather than a single closed binomial sum for every transient level. No asymptotic distribution for a joint growing-time/growing-size regime is asserted. The principal originality risk is that the cyclic primitive-Dyck factor interpretation may occur in less readily indexed symbolic-dynamics literature. This is a mathematical result subject to independent review; finite enumeration alone does not establish the infinite formula.

## References

1. H. Fukś, *Solution of the Density Classification Problem with Two Cellular Automata Rules*, arXiv:comp-gas/9703001, first posted 7 March 1997, especially Proposition 1 and Proposition 2. https://arxiv.org/abs/comp-gas/9703001
2. H. Fukś, *Exact results for deterministic cellular automata traffic models*, arXiv:math/9904182 (1999), especially the preimage enumeration sections. https://arxiv.org/abs/math/9904182
3. O. Biham, G. Hertzberg Rabinovich, and E. Katzav, *First-passage processes in a deterministic one-dimensional cellular automaton model of traffic flow*, arXiv:2605.19023 (2026); abstract consulted, full text unavailable in this assessment. https://arxiv.org/abs/2605.19023
4. J. G. Brankov et al., *The totally asymmetric exclusion process on a ring: Exact relaxation dynamics and associated model of clustering transition*, arXiv:cond-mat/0509736 (2005); abstract consulted. https://arxiv.org/abs/cond-mat/0509736
