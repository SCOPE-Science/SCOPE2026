# A sharp nonneutral speed optimum on every properly two-coloured Moran star

## Finding

Let \(K_{1,\ell}\) be the undirected star with \(\ell\ge2\) leaves. In the habitat-matching birth–death Moran model below, start with exactly one red individual at the RED centre and blue individuals at all BLUE leaves. Although the probability \(\rho_\ell(r)\) of eventual all-red fixation is independent of the habitat-matching fecundity \(r>0\), the *mean number of discrete updates conditioned on fixation* is strictly convex in \(r\) and has its unique minimum at a **nonneutral** value \(r>1\).

Define \(d=\ell^2+1\) and \(H_m=\sum_{j=1}^{m}1/j\), with \(H_0=0\). Precisely,

\[
\rho_\ell(r)=\frac1d,\qquad
T_\ell(r)=A_\ell r+B_\ell+\frac{C_\ell}{r},
\]

where

\[
A_\ell=\frac{\ell^4(\ell-1)(2\ell-1)}{6(\ell+1)d},\qquad
B_\ell=\frac{\ell}{\ell+1}\left(\ell+H_\ell+\frac{\ell^3(\ell-1)(\ell+4)}{3d}\right),
\]
\[
C_\ell=A_\ell+\frac{\ell}{\ell+1}\bigl(\ell H_{\ell-1}-(\ell-1)\bigr)>A_\ell>0.
\]

Consequently, the exact unique optimum is

\[
r_\ell^*=\sqrt{C_\ell/A_\ell}>1,\qquad
\min_{r>0}T_\ell(r)=B_\ell+2\sqrt{A_\ell C_\ell}.
\]

The mean conditioned fixation time decreases for \(0<r<r_\ell^*\) and increases for \(r>r_\ell^*\), despite the unchanged fixation probability. For every \(\ell\ge2\), the advantage over neutral matching is exactly \(T_\ell(1)-T_\ell(r_\ell^*)=(\sqrt{C_\ell}-\sqrt{A_\ell})^2>0\). Moreover,
\[
r_\ell^*=1+\frac{3\log\ell}{2\ell^2}+O(\ell^{-2})\qquad(\ell\longrightarrow\infty).
\]

For the three-site path \(\ell=2\), the concrete law is
\[
\rho_2(r)=\frac15,\qquad T_2(r)=\frac{8r^2+67r+18}{15r},\qquad r_2^*=\frac32,
\]
with \(T_2(1)=31/5\) and \(T_2(3/2)=91/15\).

## Assumptions and scope

Each vertex always contains one individual of genotype red or blue. The hub's fixed background colour is RED; all leaves' fixed background colour is BLUE. An individual's fecundity is \(r>0\) on a matching vertex and \(1\) on a nonmatching vertex. In each discrete update, choose one parent with probability proportional to its fecundity and replace one uniformly selected adjacent vertex with an offspring of the same genotype. An update replacing a vertex with the genotype already occupying it *still counts as one unit of time*. There is no mutation, environmental switching, immigration, or self-replacement by the parent. The starting hub contains the sole red mutant. The two monomorphic states are absorbing. Time is conditioned on eventual absorption in the all-red state, which has strictly positive probability for all \(r>0\). The result is not an assertion about arbitrary starting locations, other updating rules, arbitrary habitat colourings, or ecological real time.

## Proof

**1. Symmetric state reduction and the embedded jump chain.** Write \(A_k\) for a red hub with exactly \(k\) red leaves, \(0\le k\le\ell-1\), and \(B_k\) for a blue hub with exactly \(k\) red leaves, \(1\le k\le\ell-1\). The absorbing states are \(B_0\) (all blue) and \(A_\ell\) (all red). With total fecundities
\[
F_A(k)=r(\ell-k+1)+k,\qquad F_B(k)=k+1+r(\ell-k),
\]
the only changes of genotype configuration have probabilities
\[
\begin{aligned}
\Pr(A_k\to A_{k+1})&=\frac{r(\ell-k)}{\ell F_A(k)},&
\Pr(A_k\to B_k)&=\frac{r(\ell-k)}{F_A(k)},\\
\Pr(B_k\to B_{k-1})&=\frac{k}{\ell F_B(k)},&
\Pr(B_k\to A_k)&=\frac{k}{F_B(k)}.
\end{aligned}
\]
Every remaining update leaves the genotype configuration unchanged. On deleting these holding steps, the resulting embedded jump chain has the \(r\)-independent transitions
\[
A_k\to(A_{k+1},B_k)\text{ with probabilities }\left(\frac1{\ell+1},\frac\ell{\ell+1}\right),
\]
\[
B_k\to(B_{k-1},A_k)\text{ with probabilities }\left(\frac1{\ell+1},\frac\ell{\ell+1}\right).
\]
At boundaries the indicated next state may be absorbing.

**2. Fixation probability.** Let \(h\in\{0,1\}\) indicate a red hub and put \(S(h,k)=h+\ell k\). The embedded jumps of \(S\) are \(+\ell,-1\) from any \(A_k\), and \(-\ell,+1\) from any \(B_k\), with respective probabilities \(1/(\ell+1),\ell/(\ell+1)\). Hence \(S\) is a bounded martingale. It equals \(0\) at all-blue absorption and \(d=\ell^2+1\) at all-red absorption. The finite chain is absorbing almost surely, so optional stopping gives
\[
h(A_k)=\frac{1+\ell k}{d},\qquad h(B_k)=\frac{\ell k}{d},\qquad \rho_\ell(r)=h(A_0)=\frac1d.
\]
This neutrality of fixation probability for proper two-colourings is also a known general theorem; the new conclusion concerns conditional *time*.

**3. Exact visit counts.** For the embedded jump chain started at \(A_0\), write \(u_k\) and \(v_k\) for the mean number of visits to \(A_k\) and \(B_k\) before absorption, respectively (counting the initial visit). First-step occupation balance is
\[
u_0=1,\quad (\ell+1)u_k=u_{k-1}+\ell v_k,\quad (\ell+1)v_k=\ell u_k+v_{k+1},\quad v_\ell=0.
\]
The unique finite solution is
\[
u_k=\frac{d-\ell k}{d}\quad(0\le k<\ell),\qquad
v_k=\frac{\ell(\ell-k)}{d}\quad(1\le k<\ell).
\]
To see uniqueness, an absorbing finite Markov chain has invertible transient fundamental matrix; direct substitution proves the displayed solution. Under conditioning on eventual fixation, the Markov property weights every visit at state \(s\) by \(h(s)/h(A_0)\). Thus the corresponding conditioned visit expectations are
\[
U_k=\frac{(d-\ell k)(1+\ell k)}d,
\qquad V_k=\frac{\ell^2 k(\ell-k)}d.
\]
For \(1\le k<\ell\) one has \(U_k=1+V_k\), and \(U_0=1\).

**4. Update holding times and summation.** Conditional on a departure from a configuration, the number of original updates spent there is geometric, independent of the next jump and of subsequent fixation. Its mean is
\[
w_A(k)=\frac\ell{\ell+1}\left(1+\frac1{\ell-k}+\frac{k}{r(\ell-k)}\right),
\]
\[
w_B(k)=\frac\ell{\ell+1}\left(1+\frac1k+\frac{r(\ell-k)}k\right).
\]
Therefore, by linearity of conditional expectation,
\[
T_\ell(r)=\sum_{k=0}^{\ell-1}U_k w_A(k)+\sum_{k=1}^{\ell-1}V_k w_B(k).
\]
The coefficient of \(r\) is \(\frac\ell{\ell+1}\sum_{k=1}^{\ell-1}V_k(\ell-k)/k=A_\ell\). The constant coefficient is
\[
\frac\ell{\ell+1}\left[\ell+H_\ell+\frac{\ell^3(\ell-1)(\ell+4)}{3d}\right]=B_\ell.
\]
The coefficient of \(r^{-1}\) is
\[
\frac\ell{\ell+1}\sum_{k=0}^{\ell-1}\frac{kU_k}{\ell-k}
=A_\ell+\frac\ell{\ell+1}\bigl(\ell H_{\ell-1}-(\ell-1)\bigr)=C_\ell.
\]
These identities follow from \(\sum_{k=1}^{\ell-1}k=\ell(\ell-1)/2\), \(\sum_{k=1}^{\ell-1}k^2=\ell(\ell-1)(2\ell-1)/6\), and \(\sum_{k=1}^{\ell-1}k/(\ell-k)=\ell H_{\ell-1}-(\ell-1)\).

**5. Sharp optimum and large-star limit.** For \(\ell\ge2\), every summand \(k/(\ell-k)\) in the last identity is positive, giving \(C_\ell>A_\ell>0\). Thus \(T_\ell''(r)=2C_\ell/r^3>0\) for all \(r>0\); its derivative vanishes only at \(r=\sqrt{C_\ell/A_\ell}>1\). Finally \(A_\ell=\ell^3/3+O(\ell^2)\) and \(C_\ell-A_\ell=\ell\log\ell+O(\ell)\). Expanding the square root yields the stated asymptotic with an \(O(\ell^{-2})\) remainder. This proves every assertion.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. Its first method explicitly enumerates all \(2^{\ell+1}\) *labelled* red/blue configurations of the original process, constructs the full transient transition matrix with exact rational probabilities, and solves the absorption-probability and fixation-conditioned-duration systems by exact Gauss–Jordan elimination. For \(2\le\ell\le5\), each of the six rational fitness parameters \(1/2,1,6/5,3/2,2,3\) agrees exactly with the displayed probability and duration formulas. A separate calculation checks the jump-chain occupation balance and independently sums its conditional holding times for \(2\le\ell\le6\). Execution passed 128 exact checks. The symbolic proof above covers all real \(r>0\) and integer \(\ell\ge2\); the finite checker alone does not.

Run `python3 verify.py` from the directory containing the two files, using Python 3 and no additional packages.

## Relationship to prior work

Maciejewski and Puleo's *Environmental Evolutionary Graph Theory* (first public preprint November 13, 2013) defines this habitat-matching birth–death model and proves selection-independent fixation *probabilities* on all properly two-coloured graphs (their Theorem 1). The present fixation-probability calculation is an instance of that result, **not a new probability theorem**. Their fixation-*time* treatment instead compares a three-background-colour three-site example and an all-red background; it does not state the all-size two-colour star duration law or its nonneutral optimizer.

Broom, Hadjichrysanthou and Rychtář (2010) give exact star fixation-time formulas for constant genotype fitness or neighbour-game payoffs. Their genotype-based symmetric payoff matrix is not the same as fixed per-vertex habitat matching (in this model, red individuals at the hub and leaves have different fecundities even when their neighbours' types agree). Hindersin and Traulsen (2014) analyze fixed genotype fitness and other network fixation-time effects; the matching-habitat dependence is absent. Kaveh and collaborators (2020) develop broader two-chromatic fixation-probability theory and explicit star cases, but their inspected results do not determine this conditional duration law. Standard Markov-chain linear equations apply to every finite model and are not themselves claimed as new; the explicit all-size identity and strict optimizer are the distinguishing statement.

## Limitations

This theorem concerns a single red genotype initially at the specifically coloured hub. The model assumes one breeder per vertex, time-homogeneous environmental matching, birth–death rather than death–birth updating, and counting of null configuration changes as updates. The same threshold is not asserted for other starts, colourings, games or times measured only by nontrivial jumps (the latter jump-chain law is independent of \(r\)). Exact priority over all historical formulations is not independently established; general finite-state Markov methods could in principle yield equivalent expressions through specialization. No biological parameter calibration or claim about real-time ecological fixation is made.

## References

1. W. Maciejewski and G. J. Puleo, *Environmental Evolutionary Graph Theory*, first public November 13, 2013, https://arxiv.org/abs/1311.3214 (especially Theorem 1 and Section 4).
2. M. Broom, C. Hadjichrysanthou and J. Rychtář, *Evolutionary games on graphs and the speed of the evolutionary process* (2010), https://openaccess.city.ac.uk/id/eprint/1005/1/Evolutionary%20games%20on%20graphs%20and%20the%20speed%20of%20the%20evolutionary%20process_Final.pdf (star equations and fixation-time section).
3. L. Hindersin and A. Traulsen, *Counterintuitive properties of the fixation time in network-structured populations*, first public June 17, 2014, https://arxiv.org/abs/1406.4415.
4. K. Kaveh, A. McAvoy, K. Chatterjee and M. A. Nowak, *The Moran process on 2-chromatic graphs* (2020), https://doi.org/10.1371/journal.pcbi.1008402.
