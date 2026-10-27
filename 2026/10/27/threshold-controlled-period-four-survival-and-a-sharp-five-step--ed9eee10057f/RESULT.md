# Threshold-controlled period-four survival and a sharp five-step cutoff in bipartite excitation

## Finding
For every pair of positive integers \(a,b\) and every integer threshold \(k\ge2\), let \(F\) be synchronous three-state excitation on the labelled complete bipartite graph \(K_{a,b}\), with the local rule below. All recurrent orbits have primitive period one, three, or four, and the **universal finite-time identity** is
\[
F^{17}=F^5.
\]
Equivalently, every initial configuration becomes periodic after at most five updates, independently of \(a,b,k\). The all-rest fixed point is unique. Put
\[
B_k(n)=\sum_{j=k}^{n-k}\binom{n}{j},\qquad
T_k(n)=\sum_{\substack{i+j+h=n\\i,j,h\ge k}}\frac{n!}{i!j!h!},
\]
where an empty sum is zero. The numbers of **labelled periodic configurations** of exact periods one, three, and four are respectively
\[
1,\qquad T_k(a)T_k(b),\qquad 2B_k(a)B_k(b).
\]
Thus the numbers of distinct periodic orbits are \(1\), \(T_k(a)T_k(b)/3\), and \(B_k(a)B_k(b)/2\). Nontrivial recurrence exists precisely when \(\min(a,b)\ge2k\). Three-cycles exist precisely when \(\min(a,b)\ge3k\). For all \(a,b\ge2k\), the five-update entrance bound is attained.

## Assumptions and scope
Each vertex has state in \(\{0,1,2\}\), interpreted as rest, excited, refractory. At every integer time all vertices update simultaneously. Excited vertices update \(1\to2\), refractory vertices \(2\to0\), and a resting vertex updates \(0\to1\) if and only if at least \(k\) of its neighbours currently have state \(1\); otherwise it stays at rest. Graph parts \(A,B\) contain \(a,b\) distinctly labelled vertices, with every cross-part edge and no within-part edge. No assumption of \(a,b\ge k\) is needed for the general theorem. The inequality \(k\ge2\) matters for the sharpness witness; the count formulas and global bound can also be checked at threshold one, but that case is outside the original claim.

## Proof
**Counts and two activity channels.** Write \(a_i(t)\) and \(b_i(t)\) for the numbers of vertices in state \(i\) on each part. Let \(\alpha_t=[a_1(t)\ge k]\) and \(\beta_t=[b_1(t)\ge k]\), taking values zero or one. The complete-bipartite rule gives exactly
\[
(a_0',a_1',a_2')=(a_2+(1-\beta_t)a_0,\ \beta_ta_0,\ a_1),
\]
\[
(b_0',b_1',b_2')=(b_2+(1-\alpha_t)b_0,\ \alpha_tb_0,\ b_1).
\]
In particular \(\alpha_t=0\) implies \(\beta_{t+1}=0\), and \(\beta_t=0\) implies \(\alpha_{t+1}=0\). Hence each alternating-time activity channel, \(\alpha_0,\beta_1,\alpha_2,\beta_3,\ldots\) and \(\beta_0,\alpha_1,\beta_2,\alpha_3,\ldots\), can cease but never restart.

**Exact bound on activity gates.** If \((\alpha_0,\beta_0)=(0,0)\), all further gates are zero. If it is \((0,1)\), write the initial counts without a time argument. Successive gates are
\[
(0,1)\to([a_0\ge k],0)\to(0,[b_0+b_2\ge k])
\to([a_1+a_2\ge k],0).
\]
A zero test switches off both gates. If all three tests are true, subsequent gates alternate \((0,1),(1,0)\) forever: the next three needed tests are \([b_1\ge k]\), \([a_0\ge k]\), and \([b_0+b_2\ge k]\), and the underlying part counts then repeat. The initial gate \((1,0)\) is symmetric.

If \((\alpha_0,\beta_0)=(1,1)\), the next gate is \(([a_0\ge k],[b_0\ge k])\). If it is \((0,0)\), activity stops. If it is \((1,0)\), the following gate is \((0,[b_2\ge k])\); if that test succeeds, activity alternates thereafter, since \(a_1+a_2\ge k\) follows from the original \(a_1\ge k\). The case \((0,1)\) is symmetric. If the next gate is \((1,1)\), the gate two steps later is \(([a_2\ge k],[b_2\ge k])\). A zero pair stops activity; a singleton pair initiates permanent alternation (the remaining needed test follows from the original \(a_1,b_1\ge k\)); and another \((1,1)\) means that every one of the three initial colour classes in both parts has at least \(k\) vertices, so every vertex advances \(0\to1\to2\to0\) forever. Thus by time three, activity has stopped, become permanently alternating, or is permanently \((1,1)\).

If activity stops at time \(s\le3\), no further resting vertex is excited and every refractory vertex clears in at most two updates, so the all-rest configuration is attained by time \(s+2\le5\). During permanent alternation, every vertex experiences alternating local maps
\[
f_0:(0,1,2)\mapsto(0,2,0),\qquad
f_1:(0,1,2)\mapsto(1,2,0).
\]
The two-step composites are \(f_0\circ f_1:(0,1,2)\mapsto(2,0,0)\) and \(f_1\circ f_0:(0,1,2)\mapsto(1,0,1)\). The first maps to \(\{0,2\}\) and swaps those values on each further two-step iterate; the second maps to \(\{0,1\}\) and swaps those values likewise. After two alternating-gate steps the whole configuration is therefore on a period-four orbit. Since alternation begins by time three, the first periodic state is reached by time five. Permanent \((1,1)\) gives a three-cycle from the initial state. Hence \(F^{17}=F^5\), because twelve is divisible by both three and four.

**Orbit census.** A fixed point can have neither excited nor refractory vertices, since the latter states are forced to advance; thus only all-rest is fixed. In a three-cycle each vertex must rotate through all three states, so at every time both parts must supply \(k\) excited vertices. Consequently their three phase classes each have size at least \(k\); conversely every such assignment is a three-cycle. This gives \(T_k(a)T_k(b)\) period-three states. A four-cycle cannot contain permanent dual activity and must have one active channel. Its two-step composite forces each part to alternate between two permitted states, and each of the two phase classes must have at least \(k\) vertices to sustain its turn of excitation. There are \(B_k(a)B_k(b)\) phase assignments for one of the two orientations of the gates and the same number for the other orientation, yielding \(2B_k(a)B_k(b)\) exact period-four states. No nontrivial shorter period is possible under either pattern. The stated existence criteria and orbit counts follow.

**Sharpness.** Assume \(a,b\ge2k\) and \(k\ge2\). Start with exactly one refractory vertex in \(A\) and all other vertices in \(A\) at rest; put exactly \(k\) excited vertices in \(B\) and all other vertices in \(B\) at rest. The successive gate pairs are \((0,1)\to(1,0)\to(0,1)\to(0,0)\). The last excited cohort becomes refractory at time four and clears only at time five. Therefore the first periodic entry is time five, proving sharpness.

## Verification
The embedded standalone script `gh_bipartite_threshold_checker.py` applies the stated vertexwise map to every labelled configuration in ten parameter triples, including the first sharp case \((a,b,k)=(4,4,2)\), and checks the identity \(F^{17}=F^5\), the complete fixed/period-three/period-four census, and every trajectory's first periodic time. The output file `gh_bipartite_threshold_checks.txt` records the tested parameters and outcomes. These finite checks are corroboration, not the proof for unbounded parameters; the complete count and gate arguments above supply that proof.

## Relationship to prior work
Greenberg and Hastings introduced the three-state excitable-medium rule. Fisch, Gravner and Griffeath studied threshold-sensitive excitable cellular automata, motivating the dependence on the excitation threshold; their accessible full text treats lattice geometry and scaling, not the labelled complete-bipartite recurrent census. Related published single-neighbour-threshold \(k=1\) counts for the same graph family do not logically imply any result at thresholds \(k\ge2\): under increasing threshold the input Boolean gates, allowable recurrent colour partitions, and sharp entrance witnesses all change. The new claim is only the multi-neighbour-threshold classification and uniform sharp five-step bound; general eventual periodicity of finite maps is not claimed as new.

## Limitations
This concerns finite complete bipartite graphs with synchronous deterministic updating and a common integer threshold; it does not establish analogous formulas for arbitrary bipartite graphs, stochastic updates, spatial lattices or heterogeneous thresholds. Finite checks stop at the explicitly recorded sizes. An exact equivalent in unindexed literature cannot be ruled out, and some relevant historical full texts were not accessible for complete comparison. The result carries self-review only, not an independent audit.

## References
1. J. M. Greenberg and S. P. Hastings, *Spatial patterns for discrete models of diffusion in excitable media*, SIAM Journal on Applied Mathematics 34 (1978), 515–523, doi:10.1137/0134040. Foundational context; full historical article not inspected.
2. R. Durrett and D. Griffeath, *Asymptotic behavior of excitable cellular automata*, public arXiv record patt-sol/9303002, first posted 1993-03-22. General lattice excitation context; accessible abstract, not full primary text.
3. R. Fisch, J. Gravner and D. Griffeath, *Threshold-range scaling of excitable cellular automata*, public arXiv record patt-sol/9304001, first posted 1993-04-02; accessible full text at https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf. Threshold-specific lattice precedent.
