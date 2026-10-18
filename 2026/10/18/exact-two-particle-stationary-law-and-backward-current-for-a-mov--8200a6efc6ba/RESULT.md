# Exact two-particle stationary law and backward current for a moving-defect exclusion ring

## Finding

Consider a periodic ring of \(L\geq3\) sites with exactly two indistinguishable hard-core particles. A single active defect visits sites successively in the positive cyclic direction, remaining for \(\tau=1/v\) units of time at each site, where \(v>0\). During a dwell only a particle *at the active site* may move, at rate \(p/2\) to each vacant nearest neighbor, with \(p>0\); no other hopping is allowed. Positions below are measured immediately before each dwell, with the active site relabeled \(0\), and all other sites labeled \(1,\ldots,L-1\) in cyclic order.

Put \(z=e^{-p/(2v)}\), \(B_L=(L-2)(L+1)/4\), and
\[
T_L(z)=B_L(1+z^2)+z.
\]
The unique stationary probability of the two-particle configuration \(\{i,j\}\), with \(0\leq i<j\leq L-1\), in this defect-comoving, pre-dwell frame is
\[
\pi_L(\{i,j\})=\frac{1}{T_L(z)}
\begin{cases}
1,&i=0,\ 1\leq j\leq L-2,\\
z,&i=0,\ j=L-1,\\
(1+z^2)/2,&1\leq i<j\leq L-2,\\
z^2,&1\leq i\leq L-2,\ j=L-1.
\end{cases}
\]
The stationary mean signed displacement (positive minus negative hops) per defect dwell and the time-averaged current across any one ring bond are, respectively,
\[
\Delta_L=-\frac{(1-z)^2}{T_L(z)},\qquad
J_L=\frac{v}{L}\Delta_L
=-\frac{v(1-z)^2}{L\bigl[B_L(1+z^2)+z\bigr]}<0.
\]
Thus an unbiased local hop rule produces a *strictly backward* current for every finite positive \(p,v\) in the two-particle sector. The exact small-/large-speed limits (at fixed \(p,L\)) and the large-ring limit (at fixed \(p,v\)) are
\[
J_L\sim-\frac{4v}{L(L-2)(L+1)}\ (v\downarrow0),\quad
J_L\sim-\frac{p^2}{2vL^2(L-1)}\ (v\to\infty),\quad
J_L\sim-\frac{4v(1-z)^2}{L^3(1+z^2)}\ (L\to\infty).
\]

## Assumptions and scope

Each residence interval has fixed duration \(1/v\). While it lasts, at most one physical hop can occur, because a departing particle leaves the active site and hopping into that site has rate zero. Independent exponential attempts to each free neighbor have rates \(p/2\). The defect advances deterministically by one site after every residence interval. The process conserves two particles; positions are unordered. The stationary law is sampled immediately *before* the dwell, not after it. For \(L=3\), the cycle has two distinct neighbors for each site, and the formula remains valid. The strict-current statement requires \(0<z<1\), equivalently finite \(p,v>0\); at boundary limits the irreducibility argument need not apply.

## Proof

**One-step kernel.** For any two-site set \(S\), let \(R(S)=\{(i-1)\bmod L:i\in S\}\). The next pre-dwell state is \(R(S')\), where \(S'\) is the post-dwell state at the current defect. If \(0\notin S\), no move occurs. If \(0\in S\) and both neighboring sites are empty, the no-hop probability is \(z^2\), while a jump to either neighbor has probability \((1-z^2)/2\). If exactly one neighbor is empty, the no-hop probability is \(z\) and the permitted hop probability is \(1-z\). With two particles on a simple cycle, the two neighbors cannot both be occupied. This completely specifies a finite Markov kernel \(P_L\).

**A stationary measure.** Define unnormalized weights \(w(S)\) by the four cases displayed in the finding, and write \(a=(1+z^2)/2\). We verify \(wP_L=w\) directly, partitioning the possible target states. In the following checks, an unmentioned transition has probability zero:

- Target \(\{0,L-1\}\): it receives \(z\) from the no-hop transition out of \(\{0,1\}\), matching weight \(z\).
- Target \(\{0,L-2\}\): it receives \(1-z\) from the allowed left hop out of \(\{0,1\}\), \(z(1-z)\) from the allowed right hop out of \(\{0,L-1\}\), and \(z^2\) from the deterministic rotation of \(\{1,L-1\}\). Their sum is \(1\).
- Target \(\{0,j\}\), \(1\leq j\leq L-3\): it receives \(a\) from rotation of \(\{1,j+1\}\) and \((1-z^2)/2\) from a right hop out of \(\{0,j+1\}\). Their sum is \(1\).
- Target \(\{i,j\}\), \(1\leq i<j\leq L-3\): it receives \(a\) from deterministic rotation of \(\{i+1,j+1\}\).
- Target \(\{i,L-2\}\), \(1\leq i\leq L-3\): it receives \(z^2\) by rotation of \(\{i+1,L-1\}\) and \((1-z^2)/2\) from a left hop out of \(\{0,i+1\}\). Their sum is \(a\).
- Target \(\{i,L-1\}\), \(1\leq i\leq L-3\): it receives \(z^2\) from the no-hop transition out of \(\{0,i+1\}\).
- Target \(\{L-2,L-1\}\): it receives \(z\cdot z=z^2\) from the no-hop transition out of \(\{0,L-1\}\).

The indexed target ranges above may be empty. In particular, when \(L=3\), the second, first, and seventh cases cover all three states, with the same incoming-weight equations. Therefore the balance check holds for every \(L\geq3\). Counting the four groups gives
\[
\sum_S w(S)=(L-2)+z+\binom{L-2}{2}\frac{1+z^2}{2}+(L-2)z^2=B_L(1+z^2)+z=T_L(z),
\]
so \(\pi_L=w/T_L(z)\) is normalized and stationary.

**Uniqueness.** Fix \(0<z<1\). During a full tour the defect visits every site. Given any allowed elementary nearest-neighbor exclusion move \(x\to x\pm1\), there is positive probability to suppress all other hops during the tour and make precisely that hop when the defect reaches \(x\). As every transition on the connected two-token configuration graph of the ring can be implemented with positive probability by such a full tour, the \(L\)-step pre-dwell kernel is irreducible. The probability of no hops over an entire tour is positive, so its diagonal entries are positive. Consequently its stationary measure, and hence the stationary measure of the one-step comoving kernel, is unique.

**Current.** A configuration without a particle at site \(0\) produces no hop. If \(S=\{0,j\}\) with \(2\leq j\leq L-2\), either direction is available and the signed expected hop is zero. Only the two neighboring-pair configurations contribute: \(\{0,1\}\) allows a left jump with probability \(1-z\), and \(\{0,L-1\}\) allows a right jump with the same probability. Their stationary weights are \(1/T_L\) and \(z/T_L\). Thus
\[
\Delta_L=(1-z)\frac{z-1}{T_L(z)}=-\frac{(1-z)^2}{T_L(z)}.
\]
One complete tour consists of \(L\) dwells and lasts \(L/v\) units of time. Spatially averaging the signed particle flow among \(L\) bonds yields \(J_L=v\Delta_L/L\), which is strictly negative. The stated limits follow by expansion of \(z=e^{-p/(2v)}\) and \(B_L\).

## Verification

Two self-contained scripts are supplied: `verification/symbolic_stationarity.py` checks the entire exact symbolic one-step balance system, normalization and signed current for every \(3\leq L\leq20\), while `verification/independent_markov_solve.py` independently solves finite stationary linear systems for every \(3\leq L\leq11\) at \(z=0.13,0.37,0.8\) and compares currents. Execute from the artifact root with `python verification/symbolic_stationarity.py` and `python verification/independent_markov_solve.py`; the scripts require SymPy and NumPy respectively. The all-size conclusion rests on the explicit proof above, not finite testing.

## Relationship to prior work

Chatterjee, Chatterjee, Pradhan and Manna (2014) introduce exactly the single moving-defect exclusion rule in the \(q=r=0\) specialization, give dwell jump probabilities and exact density relations in terms of conditional probabilities, and approximate the stationary current with mean-field closure. Their formulas do not directly evaluate the full two-particle stationary measure or the finite-ring exact current above. Chatterjee, Chatterjee and Pradhan (2016) study multiple moving defects and a related ordered-update exclusion model; their approximate transport analysis likewise does not establish this two-particle stationary law. Das, Pradhan and Chatterjee (2023) consider moving barriers with nearest-neighbor interactions using mean-field theory and simulation rather than this explicit two-particle distribution. These are comparisons of mathematical conclusions, not a claim that literature searches prove absolute novelty.

## Limitations

The theorem is restricted to exactly two particles and one moving defect, with zero bulk and inward-to-defect hopping rates. It does not establish backward current for three or more particles or for positive bulk diffusion, multiple defects, random dwell times, or nonuniform directional hop rates. It makes no independent-validation or certification claim. Published-source indexing cannot rule out every prior formulation of the same exact law.

## References

1. R. Chatterjee, S. Chatterjee, P. Pradhan and S. S. Manna, *Interacting particles in a periodically moving potential: Traveling wave and transport*, Physical Review E **89**, 022138 (published 25 February 2014). DOI: `10.1103/PhysRevE.89.022138`; arXiv: `1404.4144`.
2. R. Chatterjee, S. Chatterjee and P. Pradhan, *Symmetric exclusion processes on a ring with moving defects*, Physical Review E **93**, 062124 (2016). DOI: `10.1103/PhysRevE.93.062124`; arXiv: `1602.02691`.
3. D. Das, P. Pradhan and S. Chatterjee, *Optimum transport in systems with time-dependent drive and short-ranged interactions*, Physical Review E **108**, 034107 (2023). DOI: `10.1103/PhysRevE.108.034107`; arXiv: `2304.06606`.
