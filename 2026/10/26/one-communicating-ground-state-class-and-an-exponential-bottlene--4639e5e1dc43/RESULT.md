# One communicating ground-state class and an exponential bottleneck for stochastic minority on balanced tripartite graphs

## Finding

Let \(m\ge 1\) and let \(G_m=K_{m,m,m}\) have three *labelled* independent parts \(A,B,C\), each with \(m\) labelled vertices. At each discrete time, independently choose one of the \(3m\) vertices uniformly and update its Boolean spin to the minority spin in its **closed** neighborhood (neighbors plus itself), retaining its spin only if the two closed-neighborhood counts tie. This is the stochastic minority rule of Rouquier, Regnault and Thierry. Since every closed neighborhood has \(2m+1\) vertices, a chosen vertex flips precisely when at least \(m\) of its \(2m\) neighbors currently agree with it.

For **every** integer \(m\ge1\), the chain has exactly one closed communicating class, reached almost surely from every starting configuration. It is the set \(\mathcal R_m\) of all configurations in which two of \(A,B,C\) are monochromatic in opposite colors and the third part is arbitrary. In particular,
\[
|\mathcal R_m|=6(2^m-1).
\]
There are no absorbing states, and the unique stationary law on \(\mathcal R_m\) is uniform. The six configurations in which *every* part is monochromatic and both colors occur form a junction set \(J_m\) with stationary mass \(1/(2^m-1)\); its stationary mean return time is exactly \(2^m-1\) updates.

For \(m\ge2\), the total-variation mixing time of the chain restricted to \(\mathcal R_m\), with threshold \(1/4\) and worst starting state, satisfies the explicit exponentially growing lower bound
\[
 t_{\mathrm{mix}}(1/4)\ \ge\ 2^{m-1}.
\]
This last inequality concerns equilibration **after** entry into the recurrent class, not the hitting time of that class.

## Assumptions and scope

Vertices and configurations are labelled. All three parts have exactly \(m\) vertices; the result makes no claim for unequal parts or for other tie conventions. Updates are fully asynchronous, one uniform vertex at each integer time. A communicating class is closed if no allowed transition leaves it. Mixing time is the least nonnegative integer \(t\) such that every starting configuration in \(\mathcal R_m\) is within total-variation distance \(1/4\) of its stationary law after \(t\) steps. The expected return to \(J_m\) starts from the stationary distribution conditioned on \(J_m\) and asks for the first strictly positive return time.

## Proof

**1. Energy and all its minimizers.** For part \(i\in\{A,B,C\}\), let \(s_i\in\{-m,-m+2,\ldots,m\}\) be the number of ones minus the number of zeros in that part. Let \(E\) be the number of monochromatic (same-spin) *edges* of \(G_m\), so this is one half of the vertex-counting energy used in [1]. Directly counting same-spin edges between parts gives
\[
  E=\tfrac12(3m^2+s_As_B+s_As_C+s_Bs_C).
\]
Writing \(u_i=s_i/m\in[-1,1]\), fix \(u_A,u_B\) and minimize over \(u_C\). Since
\[
 1+u_Au_B\ge |u_A+u_B|,
\]
which follows from the nonnegativity of both \((1-u_A)(1-u_B)\) and \((1+u_A)(1+u_B)\), one gets \(E\ge m^2\). The equality cases of these two inequalities and the minimization over \(u_C\) show that equality holds **if and only if** two of the three parts have extreme magnetizations \(+m\) and \(-m\), respectively; the remaining part is unrestricted. This includes the boundary case \(u_A+u_B=0\), where equality forces \(u_A=-u_B=\pm1\). Thus \(E=m^2\) precisely on \(\mathcal R_m\).

**2. Every state has a non-increasing path to that minimum.** Flipping one spin in part \(i\) changes its magnetization by \(\pm2\), hence changes \(E\) by \(\pm(s_j+s_k)\), where \(\{i,j,k\}=\{A,B,C\}\). The minority update allows exactly the nonpositive changes, including zero changes when \(s_j+s_k=0\). Holding the other two parts fixed, we may therefore turn every spin in part \(i\) to zero if \(s_j+s_k\ge0\), or to one if \(s_j+s_k<0\), using only permitted updates. Do this successively to part \(A\), then \(B\), then \(C\), with at most \(3m\) flips. The first two parts are now monochromatic. If their colors differ, the configuration is already in \(\mathcal R_m\). If they agree, the third part was driven to their opposite color, again producing a state in \(\mathcal R_m\). Every nonminimum configuration consequently has a permitted path with a strict energy decrease somewhere along it. Because the chain is finite and every prescribed vertex choice has positive probability, no closed communicating class can lie outside \(\mathcal R_m\).

**3. Ground-state communication and counting.** When two parts are monochromatic and opposite, every vertex in the third part has \(m\) neighbors of each color, so each chosen vertex there flips at unchanged energy. The set with these two fixed opposite parts is an \(m\)-dimensional Boolean hypercube of communicating configurations. Its two monochromatic endpoints are configurations where all three parts are monochromatic but not all the same. There are six such endpoints; a flip sequence through a free part joins the endpoints in a six-cycle (successively switching one of the two equal-colored parts). Consequently, all six hypercubes belong to one communicating class. There are exactly \(6\) choices of free part together with the two opposite colors on the other labelled parts. Each hypercube contributes \(2^m\) configurations. Every non-monochromatic free-part configuration is unique to its hypercube; each of the six all-monochromatic nonconstant endpoints belongs to exactly two hypercubes. Therefore the union has \(6\cdot2^m-6=6(2^m-1)\) elements. No state in it is absorbing, since a free part always has flippable vertices.

**4. Stationary law and return times.** Every allowed transition inside \(\mathcal R_m\) between *distinct* states is an energy-preserving single-spin flip and is reversible by choosing the same vertex again; each direction has probability \(1/(3m)\). Thus the restricted transition matrix is symmetric and doubly stochastic. The connectedness above gives a unique uniform stationary distribution. Every ground state has an inactive vertex, so it has positive holding probability, hence the chain is aperiodic. The six junction configurations have stationary mass \(6/[6(2^m-1)]=1/(2^m-1)\). Kac's return-time identity for a finite stationary Markov chain then gives mean return time \(2^m-1\) from stationarity conditioned on the junction set.

**5. Exponential mixing obstruction.** Fix one pair of labelled parts with opposite monochromatic spins and let \(S\) be the configurations for which the third part is *mixed* (contains both colors). For \(m\ge2\), \(|S|=2^m-2\), and the uniform stationary law \(\pi\) gives \(\pi(S)=(2^m-2)/[6(2^m-1)]<1/6\). A transition from \(S\) to its complement must make the third part monochromatic. Exactly \(2m\) directed single-spin-flip edges cross this boundary, each with transition probability \(1/(3m)\). (This remains true at \(m=2\), where both outgoing flips from either mixed configuration are counted.) Hence, with \(Q(S,S^c)=\sum_{x\in S}\pi(x)P(x,S^c)\),
\[
 \Phi_S:=\frac{Q(S,S^c)}{\pi(S)}=\frac{2}{3(2^m-2)}.
\]
Start from \(\mu=\pi(\cdot\mid S)\). Since \(\mu P^k\le\pi/\pi(S)\) pointwise as measures for every \(k\ge0\), each step has probability at most \(\Phi_S\) of crossing from \(S\) to \(S^c\). A union bound yields \(\mu P^t(S^c)\le t\Phi_S\), and therefore
\[
\|\mu P^t-\pi\|_{\mathrm{TV}}\ge 1-\pi(S)-t\Phi_S.
\]
At the integer time \(t=2^{m-1}-1=(2^m-2)/2\), the right-hand side exceeds \(1/2\). Convexity of total variation implies that at least one deterministic starting configuration in \(S\) also has distance greater than \(1/2\) then. This proves \(t_{\mathrm{mix}}(1/4)\ge2^{m-1}\).

## Verification

Run `python3 verify.py` using Python 3 and no third-party packages. The checker enumerates all \(2^{3m}\) labelled configurations for each \(1\le m\le5\), verifies the energy formula, the precise ground-state condition, energy monotonicity along every allowed single-spin transition, a constructive route to the minimum from every state, and irreducibility of the ground class by reachability. It also checks the six junctions and the exact number of crossing directed edges in the mixing argument. Recorded output is in `verification_output.txt`. These finite tests do not certify the infinite parameter range; the proof above does.

## Relationship to prior work

Rouquier, Regnault and Thierry [1] introduce exactly this closed-neighborhood asynchronous minority convention, its edge-monochromatic energy, and the general characterization of recurrent states through energy-nondecreasing plateaux. They analyze cliques and various other graph topologies, including bipartite graph methods, but their source's inspected sections do **not** state the balanced-tripartite ground-class geometry, \(6(2^m-1)\) recurrence census, its stationary junction mass, or the exponentially slow mixing lower bound. The energy principle and general Markov-chain identities are antecedents; the multipartite equality classification, global accessibility, glued-hypercube structure, and explicit bottleneck computation are the specialized contribution. Related zero-temperature Ising studies [2] concern different lattice/interaction settings, and complete-multipartite Ising mixing studies [3] analyze positive-temperature heat-bath dynamics, not this zero-temperature tie-flipping chain.

## Limitations

The result is specialized to three equal-sized parts and to the specific tie-flipping rule, and provides a lower bound rather than a matching upper bound for the stationary mixing time. It does not quantify the expected time from an arbitrary configuration to the recurrent class. The literature comparison is bounded: an inaccessible or unindexed equivalent result may exist. The finite checks do not replace the general analytic proof. No independent external mathematical audit has been performed.

## References

[1] J.-B. Rouquier, D. Regnault, and É. Thierry, *Stochastic Minority on Graphs*, arXiv:1011.5119, first posted 2010-11-23; *Theoretical Computer Science* (2011), doi:10.1016/j.tcs.2011.02.028. Open HTML full text: https://ar5iv.labs.arxiv.org/html/1011.5119 .

[2] V. Spirin, P. L. Krapivsky, and S. Redner, *Freezing in Ising Ferromagnets*, arXiv:cond-mat/0105037 (2001). Comparison of abstract and model only, not an exhaustive examination.

[3] H. Kim, *Cutoff phenomenon of the Glauber dynamics for the Ising model on complete multipartite graphs in the high temperature regime*, arXiv:2102.05279 (first posted 2021-02-10); *Markov Processes and Related Fields* 28 (2022), 113–148. Comparison of abstract and model only, not an exhaustive examination.
