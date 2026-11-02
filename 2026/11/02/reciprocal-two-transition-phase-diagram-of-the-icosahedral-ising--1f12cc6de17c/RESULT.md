# Reciprocal two-transition phase diagram of the icosahedral Ising \(J_1\)–\(J_2\) antiferromagnet

## Finding

For the twelve-vertex icosahedron with positive nearest- and distance-two antiferromagnetic exchange, there are exactly **two** positive-coupling ground-state transitions. Put \(r=J_2/J_1\). The exact normalized ground energy is

\[
\frac{E_0}{J_1}=\begin{cases}
-10+6r,&0<r\le \frac13,\\
-6-6r,&\frac13\le r\le3,\\
6-10r,&r\ge3.
\end{cases}
\]

The corresponding multiplicities on the five intervals or points \(0<r<1/3\), \(r=1/3\), \(1/3<r<3\), \(r=3\), and \(r>3\) are exactly \(60,80,20,80,60\). Every ground state has zero net Ising spin. The distance-two correlation \(\partial E_0/\partial J_2\) jumps from \(6\) to \(-6\) at \(r=1/3\) and from \(-6\) to \(-10\) at \(r=3\), at fixed positive \(J_1\). This is a finite-cluster zero-temperature level crossing, not a thermodynamic-limit critical point.

The intermediate 20 states have three up and three down **antipodal pairs**, the two spins in each pair agreeing. The outer sets each contain 60 states and have exactly two parallel antipodal pairs, with opposite pair spins, and four antiparallel pairs. The critical states are exactly the union of adjacent phase families (80 distinct states at each transition).

## Assumptions and scope

Let \(G\) be the ordinary simple icosahedral graph, not the dodecahedron or the icosidodecahedron. It has 12 vertices, 30 distance-one pairs, 30 distance-two pairs, and six distance-three (antipodal) pairs. Each vertex carries \(\sigma_v\in\{-1,+1\}\). For \(d=1,2,3\), set

\[
S_d(\sigma)=\sum_{\{u,v\}:\operatorname{dist}_G(u,v)=d}\sigma_u\sigma_v.
\]

The Hamiltonian is exactly \(H(\sigma)=J_1S_1(\sigma)+J_2S_2(\sigma)\), with strictly positive \(J_1,J_2\), no magnetic field, no external spins and no anisotropic bonds. All multiplicities count distinct labeled spin assignments, including global spin inversion.

## Proof

**Antipodal reduction.** Label the six antipodal pairs \((a_i,b_i)\), \(1\le i\le6\), and put \(u_i=\sigma_{a_i}+\sigma_{b_i}\), \(v_i=\sigma_{a_i}-\sigma_{b_i}\). Any two different antipodal pairs have precisely two distance-one and two distance-two bonds; each layer forms a matching between the pairs. Fix one orientation of each pair and let \(\varepsilon_{ij}=+1\) when the matching in the distance-one layer preserves the orientations, and \(-1\) otherwise. It follows by direct expansion that

\[
S_1+S_2=\sum_{i<j}u_i u_j,\qquad S_1-S_2=\sum_{i<j}\varepsilon_{ij}v_i v_j.
\]

One possible exact signed upper-triangle matrix, with zero diagonal and symmetric completion, is

```
 0  1 -1 -1  1  1
 1  0  1 -1  1 -1
-1  1  0 -1 -1 -1
-1 -1 -1  0  1 -1
 1  1 -1  1  0 -1
 1 -1 -1 -1 -1  0
```

**Six-variable extremal certificate.** Suppose \(p\) antipodal pairs have parallel spins, \(q=6-p\) have antiparallel spins. On the first set write \(u_i=2t_i\), \(t_i\in\{-1,1\}\); on the second write \(v_i=2z_i\), \(z_i\in\{-1,1\}\). Define \(T=\sum_{\mathrm{parallel}}t_i\) and \(C=\sum_{i<j\in\mathrm{antiparallel}}\varepsilon_{ij}z_i z_j\). Then the exact identities are

\[
S_1=T^2-p+2C,\qquad S_2=T^2-p-2C.
\]

The following *finite complete* sign table is obtained by considering the \(\binom6q\) choices of antiparallel pairs and their \(2^q\) signs for each \(q\), using only the displayed matrix. Both column extrema are sharp:

| \(q\) | \(\min C\) | \(\max C\) | Minimizing sign assignments, all supports |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 1 |
| 1 | 0 | 0 | 12 |
| 2 | -1 | 1 | 30 |
| 3 | -3 | 3 | 20 |
| 4 | -4 | 4 | 30 |
| 5 | -4 | 4 | 60 |
| 6 | -5 | 5 | 12 |

For \(q=4\), *every* four-pair support has exactly two \(C=-4\) and two \(C=+4\) signings; these differ by global sign. The table has at most \(\binom6q2^q\) entries per row, and its exact independently executable enumeration is included in `checker.py`.

Since \(T^2\ge0\) for even \(p\), and \(T^2\ge1\) for odd \(p\), this table yields four sharp global supporting inequalities:

\[
S_1\ge-10,\quad S_2\ge-10,\quad 3S_1+S_2\ge-24,\quad S_1+3S_2\ge-24.
\]

Equality in \(3S_1+S_2=-24\) occurs only when either \(p=6\) with three up and three down parallel pairs (20 states), or \(p=2,q=4\) with opposite signs on the parallel pairs and \(C=-4\) (\(\binom62\cdot2\cdot2=60\) states). The equality cases for \(S_1+3S_2=-24\) are the same first family plus \(p=2,q=4,C=+4\), again 60 outer-family states. The \(S_1=-10\) and \(S_2=-10\) bounds have in addition \(q=6\) equality cases, but for strictly positive \(r\) they do not minimize the full two-range Hamiltonian.

**Exact lower envelope.** If \(0<r<1/3\), write \(S_1+rS_2=(1-3r)S_1+r(3S_1+S_2)\). The supporting inequalities give \(S_1+rS_2\ge-10+6r\), with equality precisely in the 60-state \(C=-4\) family. For \(1/3<r<3\), write

\[
S_1+rS_2=\frac{3-r}{8}(3S_1+S_2)+\frac{3r-1}{8}(S_1+3S_2).
\]

The lower bound is \(-6(1+r)\), with equality only for the 20 all-parallel-pair configurations with three pairs of each sign. Finally, for \(r>3\), use \(S_1+rS_2=(S_1+3S_2)+(r-3)S_2\), giving \(6-10r\) and the 60-state \(C=+4\) family. At each threshold one coefficient vanishes, and the stated 20 and 60 configurations jointly give 80 ground states. All these configurations have six plus and six minus vertices. The differing one-sided slopes prove both energy cusps. This completes the proof for all \(J_1,J_2>0\).

## Verification

Run `python3 checker.py` with any standard Python 3 interpreter; no third-party packages, data downloads or finite-precision arithmetic are required. The checker builds the graph distances from an explicit 30-edge list, verifies the six antipodal pairs and signed-pair decomposition, evaluates every entry of the small signed extremum table, and **exhaustively** checks all \(2^{12}=4096\) Ising spin assignments. It confirms the four supporting inequalities, equality profiles, exactly 60/80/20/80/60 degeneracies, and rational sample coupling values. The proof for arbitrary positive real coupling ratios follows analytically from the exact inequalities and lower-envelope decomposition, not from a finite sample of coupling ratios.

## Relationship to prior work

The nearest-neighbor antiferromagnet on the same icosahedron was studied in the Heisenberg setting by Konstantinidis (2005, arXiv:cond-mat/0503658) and in the icosahedral-connectivity analysis by Konstantinidis (2014, arXiv:1410.3444). Jeon and Lee (arXiv:2306.07434, first posted 2023-06-12) classify the **72 nearest-neighbor Ising ground states** into a 60-state non-fivefold family and a 12-state fivefold family; that is acknowledged prior art. In this theorem, an arbitrarily small positive distance-two antiferromagnetic coupling selects the 60-state family, and the competing second shell produces the additional exact 20-state antipodal phase and two reciprocal thresholds. The distance-two bonds connect vertices in the **same** icosahedral shell, unlike intershell interactions in the quasicrystal analysis. The triangle-strip phrase “next-nearest” in the 2014 paper concerns the strip's one-dimensional labeling inside a nearest-neighbor icosahedral Hamiltonian, not the present distance-two graph interaction.

## Limitations

The result is an exact zero-temperature classification for a twelve-spin finite graph, not a positive-temperature or thermodynamic-limit phase transition. It does not establish a Heisenberg/XY quantum analogue, disorder robustness, field-dependent magnetization plateaux or material-specific exchange measurements. Historical priority remains provisional pending independent literature review; no independent scientific audit is claimed.

## References

- N. P. Konstantinidis, *The Antiferromagnetic Heisenberg Model on Clusters with Icosahedral Symmetry*, arXiv:cond-mat/0503658 (first posted 2005-03-29). https://arxiv.org/abs/cond-mat/0503658
- N. P. Konstantinidis, *Antiferromagnetic Heisenberg Model on the Icosahedron: Influence of Connectivity and the Transition from the Classical to the Quantum Limit*, arXiv:1410.3444 (first posted 2014-10-13). https://arxiv.org/abs/1410.3444
- J. Jeon and S. Lee, *Unveiling unique properties of icosahedral magnetic quasicrystals—Multipole physics and frustration*, arXiv:2306.07434 (first posted 2023-06-12); published as *Unveiling multipole physics and frustration of icosahedral magnetic quasicrystals*, npj Quantum Materials 9, 5 (2024). https://arxiv.org/abs/2306.07434
