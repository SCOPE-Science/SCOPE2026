# Three-state excitation on cocktail-party graphs: a sharp period transition and exact orbit count

## Finding

Let \(m\ge2\), and let \(G_m\) be the simple graph obtained from the complete graph on the labelled vertices \(0,1,\ldots,2m-1\) by deleting the perfect matching \(\{\{2j,2j+1\}:0\le j<m\}\). On the state space \(\{0,1,2\}^{2m}\), apply the synchronous three-state Greenberg–Hastings map \(F_m\): excited vertices \(1\) become refractory \(2\), refractory vertices \(2\) become resting \(0\), and resting vertices \(0\) become excited \(1\) exactly when an adjacent vertex is excited.

For \(m=2\), \(G_m\) is a four-cycle; it has one fixed configuration (the all-zero state), two primitive temporal four-cycle orbits, and no other periodic orbits. For **every** \(m\ge3\), the all-zero state is again the only fixed configuration; **every other periodic orbit has least period three**; and the exact number of distinct primitive temporal three-cycle orbits is
\[
Q_m=3^{2m-1}-(2m+4)2^{2m-2}+2m+1.
\]
The result counts labelled configurations and identifies a temporal orbit with its time shifts, not with graph automorphism images. The exact proportion of configurations that are periodic immediately is
\[
\frac{1+3Q_m}{3^{2m}}=1-\frac{3\cdot2^{2m}+6m\,2^{2m-2}-6m-4}{3^{2m}}
=1-O\!\left(m(2/3)^{2m}\right).
\]
In particular, adjoining a third matched pair removes all four-cycles, while the number of three-cycles subsequently grows at the exponential rate \(3^{2m}/3\).

## Assumptions and scope

The vertices are distinct and labelled. The deleted pairs are exactly the nonedges, and \(p(v)=v\oplus1\) denotes the unique nonneighbor of \(v\) other than \(v\) itself. A state has coordinates in \(\{0,1,2\}\), with meanings resting, excited, refractory. For every integer \(t\ge0\), synchronous updating means that all new coordinates are computed from the state at time \(t\). A primitive temporal \(r\)-cycle consists of \(r\) distinct configurations returning after exactly \(r\) iterations. The formula is asserted for all integers \(m\ge3\), with the distinct small case \(m=2\) stated separately. No stochastic randomness, thresholds above one, or asynchronous updates are assumed.

## Proof

**1. The only possible defect from uniform color rotation.** Define \(R(x)_v=x_v+1\pmod3\), including \(0\mapsto1\). Let \(e(x)\) be the number of excited vertices in \(x\). Each vertex is adjacent to every other vertex except its matched partner. Therefore: if \(e(x)\ge2\), every resting vertex has an excited neighbor and \(F_m(x)=R(x)\); if \(e(x)=0\), the next state has no excited vertices and the following state is all zero. When \(e(x)=1\), say the excited vertex is \(u\), the single possible difference from \(R\) is at \(v=p(u)\): if \(x_v=0\), vertex \(v\) remains zero rather than advancing to one. Call precisely this event a *defect*. If \(x_v=2\), no defect occurs and \(F_m(x)=R(x)\). The all-zero state is the only fixed state, since a fixed state cannot contain either a \(1\) or a \(2\).

**2. A defect cannot recur indefinitely once \(m\ge3\).** At a defect, take time \(0\), write \(u\) for the sole excited vertex and \(v=p(u)\) for its resting partner. Among the remaining \(n-2\) vertices, with \(n=2m\ge6\), let \(R_0\) be the set of resting vertices and \(S_0\) the set of refractory vertices, with respective cardinalities \(r,s\). Thus \(r+s=n-2\ge4\). The following cases exhaust all possibilities.

* If \(r=0\), the next state has no excited vertices and the trajectory dies out.
* If \(s=0\), the successive configurations on the blocks \((u,v,R_0)\) are \((1,0,0)\), \((2,0,1)\), \((0,1,2)\), \((0,2,0)\), and finally all zero. The singleton excited vertex at the third displayed state has its partner resting, creating one more defect, after which excitation vanishes.
* If \(r\ge2\) and \(s\ge1\), the successive configurations on blocks \((u,v,R_0,S_0)\) are
  \[
  (1,0,0,2)\longmapsto(2,0,1,0)\longmapsto(0,1,2,1)\longmapsto(1,2,0,2)\longmapsto(2,0,1,0).
  \]
  At the second and third states in this sequence there are at least two excited vertices; at the fourth, the only excited vertex is \(u\), whose partner is refractory, so there is no defect. The displayed three states after the first transition form a pure rotation orbit.
* If \(r=1\), then \(s=n-3\ge3\). Write \(w\) for the unique vertex of \(R_0\). Its partner \(z=p(w)\) belongs to \(S_0\), because \(u,v\) already form a matched pair. Write \(S_0'=S_0\setminus\{z\}\), which contains at least two vertices. In block order \((u,v,w,z,S_0')\), the trajectory is
  \[
  (1,0,0,2,2)\mapsto(2,0,1,0,0)\mapsto(0,1,2,0,1)\mapsto(1,2,0,1,2)\mapsto(2,0,1,2,0)\mapsto(0,1,2,0,1).
  \]
  The first transition is a defect, and the second is a defect at \(z\). Thereafter at least two vertices are excited whenever a singleton's partner would be resting; at the final singleton excitation \(w\), its partner \(z\) is refractory. The last three distinct states are a pure rotation orbit.

Thus, following any defect the trajectory reaches all zero or a pure three-cycle after finitely many steps. A trajectory with no defects either follows pure rotation forever, or has a time with no excited vertices and becomes all zero. Consequently, for \(n\ge6\) no primitive period other than three exists. The case \(m=2\) is a finite connected four-vertex graph; the exhaustive \(3^4=81\) state analysis in `verify_ghm.py` verifies the one fixed point and exactly two primitive four-cycles without extrapolation from larger graphs.

**3. Characterize the three-cycles.** Let \(x\in\{0,1,2\}^{n}\), where \(n\ge6\). It is on a pure rotating three-cycle precisely if all three colors occur and, for every color \(c\in\{0,1,2\}\) represented at a single vertex \(w\), the partner \(p(w)\) does *not* have color \(c-1\pmod3\). Indeed, after the global color rotation, every color class becomes the excited class once in three steps. A singleton excited class causes a defect exactly when its partner belongs to the preceding color class. Larger excited classes never cause defects. These conditions are necessary and sufficient, and a three-color-surjective state cannot be fixed under a one-step global rotation.

**4. Count without overlapping exclusions.** The number of labelled colorings using every color is \(3^n-3\cdot2^n+3\). For a fixed color \(c\), let \(A_c\) be those surjective colorings with exactly one vertex of color \(c\) whose matched partner has color \(c-1\pmod3\). First choose that vertex in \(n\) ways, fix its partner's preceding color, and color the remaining \(n-2\) vertices with the two other colors, requiring at least one of the third color. Hence \(|A_c|=n(2^{n-2}-1)\). The three bad sets are pairwise disjoint: if \(A_c\) and \(A_{c-1}\) both held, the unique vertex of the preceding color would be the partner of the unique color-\(c\) vertex, but its own partner would then have color \(c\), contradicting the required color \(c-2\); every pair of distinct colors is consecutive on the three-color circle. The number of valid periodic configurations is therefore
\[
V_n=3^n-3\cdot2^n+3-3n(2^{n-2}-1).
\]
Each primitive three-cycle contributes exactly three configurations. Hence \(Q_m=V_{2m}/3\), giving the stated formula. Adding the unique all-zero fixed configuration yields the immediate-periodicity proportion.

## Verification

The standalone `verify_ghm.py` constructs the graph explicitly by its neighbor lists rather than reusing the proof's exceptional-vertex update, evaluates the full map on every one of the \(3^n\) configurations for \(n\in\{2,4,6,8,10,12\}\), and independently enumerates the directed cycles of the resulting finite functional graph. It also checks the exact periodic-state criterion against a threefold iterate for every state at the larger tested orders. The actual output in `verification_output.txt` records primitive orbit counts: \(2\) four-cycles for \(n=4\), and \(90,1428,16110,160776\) three-cycles respectively for \(n=6,8,10,12\). All observed values agree with the theorem. These finite computations check small cases and the four-vertex finite classification; the proof for arbitrary \(m\) is the preceding structural case analysis and inclusion–exclusion, not an extrapolation.

To reproduce from a shell with Python 3, execute `python verify_ghm.py` in the directory containing the standalone program. It has no nonstandard dependencies.

## Relationship to prior work

The three-state Greenberg–Hastings rule was introduced for excitable-media dynamics by Greenberg and Hastings (1978). Gravner, Lyu and Sivakoff (2016, arXiv:1610.07320, version 1 dated 2016-10-24) prove general graph-theoretic criteria for synchronization and asymptotic excitation rate via a covering-space construction. Those results address which initial states oscillate and at what average rate on an arbitrary graph, but do not give the number of immediately periodic labelled configurations or primitive temporal orbits for complete graphs with a perfect matching deleted. Doba (2018) independently studies maximum cycle density on arbitrary finite connected graphs; the inspected Sections 2, 3 and 7 do not supply the present exact graph-family census. Epperlein and Siegmund (2013) study phase-locked trajectories in a broader class of finite-state graph systems rather than this excitation rule's exact count.

The new statement is specific to the graph \(K_{2m}\) minus a perfect matching and gives an explicit recurrence census, including the four-to-three-period transition between \(m=2\) and \(m=3\). It is not an assertion of a new general convergence theorem. Published work using another vocabulary or an unindexed result may still overlap; the originality assessment is qualified accordingly.

## Limitations

No claim is made about exact basin sizes or sharp transient lengths, more than three states, higher excitation thresholds, stochastic updates, or other graph families. The proof uses the fact that every vertex has exactly one other nonneighbor and that there are at least six vertices. The exceptional four-vertex case is proved by a complete finite-state check provided here. The literature comparison is limited by coverage of discoverable and accessible sources; independent scientific validation has not been performed.

## References

1. J. M. Greenberg and S. P. Hastings, “Spatial patterns for discrete models of diffusion in excitable media,” *SIAM Journal on Applied Mathematics* **34** (1978), 515–523, doi:10.1137/0134040. (Foundational model; referenced by the inspected later papers.)
2. J. Gravner, H. Lyu, and D. Sivakoff, “Limiting behavior of 3-color excitable media on arbitrary graphs,” arXiv:1610.07320v1 (first public version 2016-10-24), https://arxiv.org/abs/1610.07320. (Full-text mathematical comparison.)
3. N. Doba, “The time evolution of a Greenberg–Hastings cellular automaton on a finite graph,” *Complex Systems* **27** (2018), 101–126, doi:10.25088/ComplexSystems.27.2.101, https://wpmedia.wolfram.com/sites/13/2018/09/27-2-1.pdf. (Full-text mathematical comparison.)
4. J. Epperlein and S. Siegmund, “Phase-locked trajectories for dynamical systems on graphs,” *Discrete and Continuous Dynamical Systems B* **18** (2013), 1827–1844, doi:10.3934/dcdsb.2013.18.1827. (Abstract and scope comparison.)
