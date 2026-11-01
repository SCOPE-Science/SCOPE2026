# Exact majority basins and a Gaussian hub-memory crossover on clique windmills

## Finding

Fix an odd integer \(n\ge3\) and an even integer \(m\ge4\). Form the clique windmill \(W_{n,m}=K_1\vee(nK_m)\): a hub is connected to every vertex of \(n\) otherwise disjoint complete graphs of order \(m\). Run synchronous strict open-neighbor binary majority with retention at ties. Let \(F\) be the simultaneous global update and put
\[
 u_m=2^{m-1}-\tfrac12\binom{m}{m/2},\qquad
 v_m=2^{m-1}+\tfrac12\binom{m}{m/2}.
\]
All trajectories satisfy \(F^3=F^2\), and the bound is sharp: for every permitted \((n,m)\), some initial state first becomes fixed at time two. There are exactly \(2^n\) fixed states and no other recurrent states. A fixed state consists of a uniform bit on each clique and a hub bit equal to the strict majority of these \(n\) clique bits.

For each fixed configuration whose set of one-cliques is a particular subset \(P\subseteq\{1,\dots,n\}\), with \(p=|P|\), its **individual attraction basin** has exactly
\[
 \boxed{B_{n,m}(P)=u_m^p v_m^{n-p}+v_m^p u_m^{n-p}}
\]
initial states. Consequently the two monochromatic fixed states have the uniquely largest basins, of size \(u_m^n+v_m^n\) each, while the smallest basins occur precisely at \(p=(n-1)/2\) or \(p=(n+1)/2\).

If the initial bits are all independent and fair, let \(H_0\) and \(H_\infty\) denote the initial and eventual hub bits. Then, with \(q_m=2^{-m}\binom{m}{m/2}\),
\[
 \boxed{\Pr(H_\infty=H_0)=\sum_{j=(n+1)/2}^{n}\binom nj
 \left(\frac{1+q_m}{2}\right)^j
 \left(\frac{1-q_m}{2}\right)^{n-j}.}
\]
In every sequence of odd \(n\to\infty\) and even \(m\to\infty\) such that \(n/m\to\lambda\in(0,\infty)\), this probability converges to
\[
 \boxed{\Phi\!\left(\sqrt{2\lambda/\pi}\right),}
\]
where \(\Phi\) is the standard normal distribution function. When \(n/m\to0\) the limit is \(1/2\); when \(n/m\to\infty\) the limit is \(1\). Thus a graph-theoretic one-bit memory transition is governed by the ratio between the number and size of the cliques.

## Assumptions and scope

All graphs are finite, simple and undirected, with labelled peripheral cliques. The network has \(1+nm\) vertices. Every vertex receives the strict majority bit among its **open** neighbors, or keeps its own current bit when those neighbors split equally. Initial configurations are arbitrary for the exact dynamical and basin statements; the probability statements alone assume independent, uniform binary initial states. Only odd \(n\ge3\) and even \(m\ge4\) are covered. All time indices start at zero.

## Proof

Write \(m=2r\), with \(r\ge2\). Let the original hub bit be \(c\in\{0,1\}\), and let \(k_i\) be the initial number of ones in peripheral clique \(i\). For a peripheral vertex currently equal to zero, there are \(k_i+c\) one-neighbors; it becomes one exactly when \(k_i+c\ge r+1\). For a vertex currently equal to one, there are \(k_i-1+c\) one-neighbors; it stays one exactly when \(k_i-1+c\ge r\), because ties retain the current bit. These criteria coincide. Hence **every peripheral clique is monochromatic at time one**, with bit
\[
 s_i=\mathbf1\{k_i+c\ge r+1\}.
\]
Once a clique is monochromatic, every member has \(m-1\ge m/2\) agreeing clique-neighbors; at a tie it retains its bit. Therefore its bit never changes again, regardless of the hub.

At the next update the hub sees \(m\sum_i s_i\) ones among its \(mn\) neighbors. Since \(n\) is odd, its new bit is the strict majority of the \(s_i\), independent of its time-one bit. It then stays there. Thus \(F^3=F^2\), no nontrivial periodic orbits exist, and the stated configurations are exactly the fixed points. There are \(2^n\) of them.

For sharpness take initial hub \(c=0\), choose exactly \((n+1)/2\) cliques to have \(k_i=r+1\), and every other clique to have \(k_i=0\). The time-one cliques have strict majority bit one, whereas the original total one-count satisfies
\[
 \sum_i k_i=\frac{(n+1)(r+1)}{2}\le nr=\frac{nm}{2}.
\]
Indeed, the inequality is equivalent to \(n(r-1)\ge r+1\), valid for \(n\ge3\), \(r\ge2\). The hub therefore remains zero at time one (including equality) but becomes one at time two. This proves sharpness for the full parameter domain.

For basin counting, when \(c=0\), any specified clique ending at one has \(u_m\) possible initial binary patterns (strictly more than \(r\) initial ones), and any specified clique ending at zero has \(v_m\) patterns. This uses symmetry of the binomial coefficients: the number with at least \(r+1\) ones is \(2^{m-1}-\binom mr/2\). When \(c=1\), the corresponding counts are interchanged. For any prescribed subset \(P\) of final one-cliques, the two choices for the initial hub contribute independently \(u_m^p v_m^{n-p}\) and \(v_m^p u_m^{n-p}\). Each resulting final hub is forced by the odd majority. This gives the displayed basin formula. Summing over subsets produces
\[
 \sum_{P\subseteq[n]}B_{n,m}(P)=2(u_m+v_m)^n=2^{nm+1},
\]
so the basins partition the entire state space. Since \(0<u_m<v_m\), their sizes strictly increase as \(|p-n/2|\) increases, proving the extremizers.

Condition on initial hub \(c=1\). The final clique bits are then independent Bernoulli variables of success probability \(v_m/2^m=(1+q_m)/2\). The eventual hub is their majority. Condition on \(c=0\) and use bit-complement symmetry to obtain the identical retention probability. This proves the exact binomial tail.

Finally, Stirling's formula gives
\[
 q_m=\frac{\binom m{m/2}}{2^m}=\sqrt{\frac{2}{\pi m}}(1+O(m^{-1})).
\]
For \(n/m\to\lambda\in(0,\infty)\), the binomial central limit theorem for success probabilities tending to \(1/2\) yields a standardized threshold of \(-q_m\sqrt n/\sqrt{1-q_m^2}\to-\sqrt{2\lambda/\pi}\), hence the normal-distribution limit. The same argument gives \(1/2\) when \(n/m\to0\), assuming \(n\to\infty\). When \(n/m\to\infty\), Chebyshev's inequality bounds the failure probability by \(O((nq_m^2)^{-1})=O(m/n)\), giving limit one.

## Verification

Two standalone direct-neighborhood enumeration programs accompany this result. `verify_majority.py` enumerates all \(8192\) configurations for \((n,m)=(3,4)\) and all \(524288\) configurations for \((3,6)\). `verify_majority.cpp` independently enumerates those cases and all \(2097152\) configurations for \((5,4)\). Each program checks the second-iterate fixedness identity, the fixed-state structure, exact individual basin counts, and the existence of initial states requiring two updates. Output files record the completed executions. These finite checks corroborate, but do not replace, the general proof above. They may be replayed with `python3 verify_majority.py` and `g++ -std=c++17 -O3 verify_majority.cpp -o verifier && ./verifier`.

## Relationship to prior work

Goles and Olivos established eventual fixed-point/two-cycle behavior for symmetric threshold systems, but not an individual-basin classification for these windmills. Benjamini, Chan, O'Donnell, Tamuz and Tan (arXiv:1405.2486v1) investigate majority dynamics and consensus probabilities on infinite unimodular graphs and random finite graphs; their objects and probability questions do not yield the finite-clique-windmill basin formula. Tamuz and Tessler (arXiv:1307.4035v1) study information retention in majority dynamics, principally for bounded-degree graph families and general structural arguments, without this two-scale exact formula. Kaaser, Mallmann-Trenn and Natale (arXiv:1508.03519v1) use clique and independent-set modules to bound convergence time; the modular reduction does not calculate individual windmill basins or the growing-clique Gaussian crossover. The triangle-windmill (two-vertex petal) analogue is already known separately and is deliberately excluded; the present asymptotic requires growing even clique order.

## Limitations

The odd number of cliques avoids tie behavior at the hub. Odd peripheral clique order is not covered and may sustain different behavior. The stated crossover concerns the hub's initial bit, not recovery of an externally designated correct signal, and not global unanimity. The proofs are mathematical and not independently certified. Literature searching cannot rule out equivalent results in unindexed sources; no claim is made that the broad Goles–Olivos periodicity theorem is new.

## References

- E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI: 10.1016/0012-365X(80)90121-1.
- O. Tamuz and R. J. Tessler, *Majority Dynamics and the Retention of Information*, arXiv:1307.4035v1, 15 July 2013, https://arxiv.org/abs/1307.4035.
- I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, 11 May 2014, https://arxiv.org/abs/1405.2486.
- D. Kaaser, F. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519v1, 14 August 2015, https://arxiv.org/abs/1508.03519.
