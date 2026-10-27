# Sharp relaxation and Catalan extremizer census for cyclic Rule 184

## Finding
For integers \(n\ge3\) and \(1\le k<n\), consider all binary words of length \(n\), with exactly \(k\) ones, under synchronous Rule 184. Write \(m=\min\{k,n-k\}\). A configuration is *relaxed* if it has no adjacent ones when \(2k\le n\), and no adjacent zeros when \(2k\ge n\), with periodic adjacency and simultaneous updates. In the equal-density case the relaxed words are precisely the two alternating words, so either description agrees. Let \(\tau(x)\) be the least nonnegative integer \(t\) for which the time-\(t\) configuration is relaxed.

**Theorem.** For every \(n,k\) in this domain,
\[
\max_{|x|=k}\tau(x)=m-1,\qquad
\#\{x:|x|=k,\ \tau(x)=m-1\}=nC_{m-1},
\]
where \(C_j=\frac{1}{j+1}\binom{2j}{j}\) denotes the \(j\)-th Catalan number. In the sparse case \(2\le k\le n/2\), every extremizer has exactly one adjacent pair of occupied cells at time \(k-2\). That unique surviving pair admits an explicit description as a length-\(k-1\) strict cyclic record in an initial particle-gap walk.

## Assumptions and scope
Cells are indexed by \(\mathbb Z/n\mathbb Z\). The rule moves each occupied cell one place clockwise exactly when the next site is empty, all moves simultaneously; equivalently,
\[
(Fx)_i=x_{i-1}(1-x_i)+x_ix_{i+1},\qquad x_i\in\{0,1\}.
\]
The two summands cannot both be one. The particle count is conserved. A word with no adjacent occupied sites travels clockwise by one cell per update. A word with no adjacent empty sites travels counterclockwise by one cell per update. Both sets are forward invariant. The theorem counts distinct **labeled** binary words, not equivalence classes under rotation. For \(k=0\) and \(k=n\), the constant states are already relaxed and have relaxation time zero; they are not included in the displayed extremal census.

## Proof
It suffices initially to consider \(1\le k\le n/2\). Unroll the cyclic order of the \(k\) particles as positions \(p_i\) for integer \(i\), with \(p_{i+k}=p_i+n\). Let \(P_i(t)\) be the position of particle \(i\) at time \(t\) in the same unrolling; particles never overtake. Its precise exclusion update is
\[
P_i(t+1)=\min\big(P_i(t)+1,P_{i+1}(t)-1\big).
\]
Put \(B_i=p_i-2i\), so \(B_{i+k}=B_i+\delta\) with \(\delta=n-2k\ge0\). Induction from the preceding recurrence gives the exact min-plus formula
\[
P_i(t)=t+2i+\min_{i\le j\le i+t} B_j. \tag{1}
\]
The gap after particle \(i\) at time \(t\) is therefore
\[
G_i(t)=P_{i+1}(t)-P_i(t)-1
=1+\min_{i+1\le j\le i+t+1}B_j
-\min_{i\le j\le i+t}B_j. \tag{2}
\]
At \(t=k-1\), the newly appended endpoint is \(B_{i+k}=B_i+\delta\ge B_i\), hence cannot lower the previous window minimum; the new window minimum is at least the old one. Equation (2) gives \(G_i(k-1)\ge1\) for all \(i\). Thus all configurations relax by time \(k-1\).

Suppose \(k\ge2\), and take \(t=k-2\). Since \(B_{j+1}-B_j=g_j-1\ge-1\), where \(g_j=p_{j+1}-p_j-1\ge0\) are the initial empty-cell gaps, the new minimum in (2) can drop below the old one by at most one. Consequently \(G_i(k-2)=0\) exactly when the newly added endpoint \(\ell=i+k-1\) is a strict record below all preceding \(k-1\) values:
\[
B_\ell<\min_{\ell-k+1\le j<\ell} B_j. \tag{3}
\]
For \(q=1,\ldots,k-1\), expand \(B_\ell-B_{\ell-q}=\sum_{j=\ell-q}^{\ell-1}(g_j-1)\). Criterion (3) is equivalent to the simultaneous inequalities
\[
\sum_{j=\ell-q}^{\ell-1}g_j\le q-1\qquad(1\le q\le k-1). \tag{4}
\]
These inequalities are Catalan: the reversed length-\(k-1\) gap tuple \((g_{\ell-1},\ldots,g_{\ell-k+1})\) consists of nonnegative integers whose first \(q\) entries sum to at most \(q-1\). Standard first-return decomposition of such lists gives the recurrence \(A_0=1\), \(A_s=\sum_{j=0}^{s-1}A_jA_{s-1-j}\), so their count is \(A_s=C_s\). Equivalently, represent each gap entry by its many up-steps followed by a down-step; condition (4) is the Dyck prefix condition and the final balancing step closes the path.

There cannot be two different strict records of the form (3) in one cyclic word. Indeed, suppose they appear at \(\ell\) and \(\ell'<\ell+k\), with \(\ell<\ell'\). Then the second record forces \(B_{\ell'}<B_\ell\). But the first record repeats at \(\ell+k\), because every \(B\)-value increases by the same \(\delta\) under translation by \(k\); since \(\ell'\) occurs among the immediately previous \(k-1\) indices of \(\ell+k\), it forces \(B_{\ell+k}<B_{\ell'}\). This contradicts \(B_{\ell+k}=B_\ell+\delta\ge B_\ell\).

To enumerate words satisfying (3), choose the physical position \(p_\ell\) of its unique record particle: there are \(n\) choices. Choose the \(k-1\) preceding gaps meeting (4): there are exactly \(C_{k-1}\) choices. The remaining omitted gap is uniquely set by the conserved total \(h=n-k\) empty cells. The Catalan constraints imply that the sum of chosen gaps is at most \(k-2\), so the omitted gap is at least \(h-(k-2)\ge2\); every choice is feasible, and all choices produce distinct labeled configurations by record uniqueness. Thus exactly \(nC_{k-1}\) words have a blocked pair at time \(k-2\). Since none can remain blocked after time \(k-1\), these and only these have \(\tau=k-1\). For \(k=1\) every state has \(\tau=0\), and there are \(n=nC_0\) such states.

For \(k>n/2\), the operation \((Rx)_i=1-x_{-i}\) (complement followed by spatial reflection) conjugates the Rule-184 map to itself and exchanges the low- and high-density relaxation conditions. Applying the sparse case with \(n-k\) particles proves the same bound and enumeration. This completes the proof. \(\square\)

## Verification
The accompanying stdlib-only `verify.py` independently applies the synchronous Boolean-cell update, computes relaxation times by iteration, evaluates the Catalan counts, and compares the unique-record criterion with actual near-final adjacent pairs. Run it with `python verify.py`; its expected successful termination begins `VERIFY_OK`. The actual recorded run was:

```text
VERIFY_OK exhaustive_n=3..16 random_cases=10500 checks=289999 ring_sizes=14
```

Every configuration is examined exhaustively for all lengths from three through sixteen. A further 10,500 reproducible random configurations are checked at lengths \(17,19,23,37,64,81,99\). Finite checks are not a substitute for the all-length argument above.

## Relationship to prior work
H. Fukś's 1997 density-classification analysis already provides exact local Rule-184 preimage/ballot formulas and a general finite-time stabilization bound; those local ballot counts are **not claimed as new**. Earlier exact traffic-rule analyses likewise use preimage/lattice-path and min-plus (ultradiscrete Burgers) methods. Belitsky and Ferrari analyze invariant measures and convergence for the infinite rule. Recent work by Jha, Wiesenfeld, Lee and Laval measures the finite-ring jam relaxation time numerically, and a later Jha–Wiesenfeld–Laval paper develops a height-function/Dyck-path description and thermodynamic-limit scaling theory; Dyck paths and traffic height mappings themselves are **not new here**. The present theorem instead supplies the sharp **fixed-particle-count finite-ring extremal bound**, the **exact count of labeled extremizers** and the **unique final-blockage record proof**. These precise claims were not stated in the inspected texts, although the pre-existing height and ballot techniques create a genuine risk of other equivalent formulations elsewhere. A search failure is not proof of historical priority.

## Limitations
The result concerns deterministic synchronous parallel Rule 184 on finite periodic rings, with fixed particle number and the particular relaxation criterion stated above. It does not give the full transient-length distribution, random-ensemble scaling exponents, asynchronous dynamics, or open-boundary models. The exact finite-ring Catalan census has not been independently audited; historical priority is provisional. The methods of local ballot enumeration, min-plus particle representation, and Dyck-height paths are acknowledged as established.

## References
1. H. Fukś, *Solution of the Density Classification Problem with Two Cellular Automata Rules* (1997), arXiv:comp-gas/9703001, https://arxiv.org/abs/comp-gas/9703001.
2. H. Fukś, *Exact results for deterministic cellular automata traffic models* (1999), arXiv:comp-gas/9902001, https://arxiv.org/abs/comp-gas/9902001.
3. V. Belitsky and P. Ferrari, *Invariant Measures and Convergence for Cellular Automaton 184 and Related Processes* (1998), arXiv:math/9811103, https://arxiv.org/abs/math/9811103.
4. K. Nishinari and D. Takahashi, *Analytical properties of ultradiscrete Burgers equation and rule-184 cellular automaton*, J. Phys. A 31 (1998), DOI:10.1088/0305-4470/31/24/006.
5. A. Jha, K. Wiesenfeld, G. Lee and J. Laval, *Evidence of Non-Equilibrium Critical Phenomena in a Simple Model of Traffic* (2025), arXiv:2501.08417, https://arxiv.org/abs/2501.08417.
6. A. Jha, K. Wiesenfeld and J. Laval, *Equilibrium-like statistical mechanics in space-time for a deterministic traffic model far from equilibrium* (2026), arXiv:2602.08991, https://arxiv.org/abs/2602.08991.
