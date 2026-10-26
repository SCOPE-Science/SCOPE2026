# Sharp dimension-seven deletion of nearest-neighbor edges in fastest-mixing binary walks

## Finding

For each integer \(d\ge3\), let \(G_d\) have vertex set \(\{0,1\}^d\). Distinct vertices are adjacent precisely when their Hamming distance is \(1\) or \(3\). Among all real symmetric, entrywise nonnegative, row-stochastic matrices \(P\) whose off-diagonal support is contained in \(E(G_d)\), minimize the second-largest eigenvalue modulus
\[
\mu(P)=\max\{|\lambda|:\lambda\in\operatorname{spec}(P),\ \lambda\text{ nonconstant}\}.
\]
The constant eigenvalue is excluded with multiplicity one, equivalently \(\mu(P)=\|P-2^{-d}{\bf1}{\bf1}^{\mathsf T}\|_2\).

There is an optimal matrix that assigns probabilities \(a_d\) to each Hamming-distance-one edge and \(b_d\) to each Hamming-distance-three edge. Its exact parameters and the optimal value are
\[
\begin{array}{c|c|c|c}
 d&a_d&b_d&\mu_d^*\\\hline
 3&1/6&1/6&1/3\\
 4&1/12&1/12&1/3\\
 5&1/22&1/22&4/11\\
 6&1/52&3/104&5/13\\
 d\ge7&0&\displaystyle\frac{6}{(d+3)(d-1)(d-2)}&\displaystyle\frac{d-3}{d+3}
\end{array}
\]
Every optimizer invariant under translations and coordinate permutations has precisely the displayed probabilities. More strongly, **every** globally optimal matrix, whether invariant or not, assigns probability zero to **every distance-one edge** for \(d\ge7\). Conversely, every global optimizer for \(d=5,6\) assigns positive probability to at least one distance-one edge. The cutoff at \(d=7\) is therefore sharp. For \(d\ge7\), the optimizing chain holds at a vertex with probability \(3/(d+3)\) and otherwise flips three distinct coordinates, uniformly among the \(\binom d3\) choices.

## Assumptions and scope

Self-loops (holding probabilities) are permitted; other loops and transitions to nonadjacent vertices are not decision variables. Zero probabilities on permitted graph edges are allowed. Symmetry means \(P=P^{\mathsf T}\), hence the stationary distribution is uniform. These requirements are essential: the objective is not total-variation mixing time, not a nonreversible-chain optimum, and not optimization over arbitrary stationary distributions. The graph \(G_d\) is connected for every \(d\ge3\) because its distance-one edges form the ordinary hypercube. The optimal matrices displayed are also irreducible: for \(d\ge7\), weight-three coordinate flips span the binary vector space (two such flips can generate any weight-two difference, and weight-three vectors have odd weight).

## Proof

**1. Exact symmetry reduction.** The translations of \(\mathbb F_2^d\) and coordinate permutations preserve \(G_d\), are transitive on each of the two permitted edge types, and preserve feasibility. The spectral norm expression for \(\mu\) is convex. Averaging any minimizer over this finite group gives a minimizer determined by nonnegative \(a,b\), with holding probability \(1-da-\binom d3b\ge0\). Thus a globally optimal value is achieved among this two-parameter family; nothing about uniqueness of unrestricted matrices is assumed.

**2. Fourier eigenvalues.** Let \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\), with \(|S|=j\). For a distance-three neighbor, the character sum is the binary Krawtchouk number
\[
K_3^{(d)}(j)=\sum_{h=0}^{3}(-1)^h\binom jh\binom{d-j}{3-h}
=\frac{(d-2j)^3-(3d-2)(d-2j)}6.
\]
Consequently the complete list of nonconstant eigenvalues, each repeated \(\binom dj\) times, is
\[
\theta_j=1-2ja-\left(\binom d3-K_3^{(d)}(j)\right)b,
\qquad 1\le j\le d.
\]
The original problem is exactly the minimax of their absolute values over \(a,b\ge0\) and \(da+\binom d3b\le1\).

**3. The two small complete-bipartite cases.** For \(d=3,4\), every pair of opposite binary parity differs in Hamming distance \(1\) or \(3\); hence \(G_d\) is \(K_{m,m}\) for \(m=2^{d-1}\). Full bipartition automorphism averaging reduces its optimal chain to one cross-edge probability \(w\). Nonconstant eigenvalues are \(1-mw\) and \(1-2mw\), with constraint \(0\le mw\le1\). The unique minimax cross probability is \(w=2/(3m)\), giving \(\mu=1/3\) and the first two table rows.

**4. Exact dual bounds for dimensions five and six.** For \(d=5\), the three nonconstant spectral functions at Hamming weights \(1,3,5\) are
\[
\theta_1=1-2a-12b,\quad\theta_3=1-6a-8b,\quad\theta_5=1-10a-20b.
\]
Their signed convex combination is the constant
\[
\frac5{22}\theta_1+\frac5{11}\theta_3-\frac7{22}\theta_5=\frac4{11}.
\]
As the coefficients of \(\theta_1,\theta_3,-\theta_5\) are positive and sum to one, every feasible chain satisfies \(\mu\ge4/11\). At \(a=b=1/22\), all nonconstant eigenvalues by increasing weight are \((4,3,4,3,-4)/11\). Hence this bound is attained. Positivity of all three dual coefficients makes equality require \(\theta_1=\theta_3=-\theta_5=4/11\), which uniquely gives those two edge weights.

For \(d=6\), similarly
\[
\theta_1=1-2a-20b,\quad\theta_4=1-8a-16b,\quad\theta_6=1-12a-40b,
\]
with exact identity
\[
\frac4{13}\theta_1+\frac5{13}\theta_4-\frac4{13}\theta_6=\frac5{13}.
\]
At \(a=1/52,b=3/104\), the nonconstant Fourier eigenvalues by weight are \((5,3,4,5,3,-5)/13\). The displayed dual bound is tight, and its strict positive coefficients force the three active contacts and uniquely determine \(a,b\).

**5. The universal range and its sharp threshold.** For any \(d\ge7\), put \(B=(d-1)(d-2)\). Since \(K_3^{(d)}(1)=\binom d3-B\) and \(K_3^{(d)}(d)=-\binom d3\),
\[
\theta_1=1-2a-Bb,\qquad \theta_d=1-2da-\frac d3Bb.
\]
The exact identity
\[
\frac d3\theta_1-\theta_d=\frac{d-3+4da}{3}
\]
and the two constraints \(\theta_1\le\mu\), \(-\theta_d\le\mu\) imply
\[
\mu\ge\frac{d-3+4da}{d+3}\ge\frac{d-3}{d+3}.
\]
Equality requires \(a=0\), \(\theta_1=\mu\), and \(\theta_d=-\mu\); solving yields uniquely
\[
b=\frac6{(d+3)(d-1)(d-2)}.
\]
The row sum of off-diagonal weights is \(\binom d3b=d/(d+3)<1\), so the candidate is feasible. To verify **every** remaining Fourier mode, note first that \(|K_3^{(d)}(j)|\le\binom d3\), by the character-sum triangle inequality. This gives \(\theta_j\ge1-2\binom d3 b=-(d-3)/(d+3)\).

For the upper bound, a direct cubic subtraction factors as
\[
K_3^{(d)}(1)-K_3^{(d)}(j)
=\frac{j-1}{3}\left(4j^2+(4-6d)j+3d^2-9d+6\right).
\]
For real \(j\), the quadratic factor has minimum \((3d^2-24d+20)/4>0\) whenever \(d\ge8\). For \(d=7\) it equals \(2(j-5)(2j-9)\), nonnegative at each integer \(1\le j\le7\) (with equality also at \(j=5\)). Thus \(K_3^{(d)}(j)\le K_3^{(d)}(1)\) for all integers \(d\ge7\), \(1\le j\le d\), proving \(\theta_j\le\theta_1=(d-3)/(d+3)\). The universal minimum and unique invariant probabilities follow.

**6. All unrestricted optima delete nearest-neighbor edges.** Given any unrestricted minimizer \(P\), its group average is also minimizing, so in \(d\ge7\) every distance-one entry of the average equals zero, by the uniqueness just proved. These entries are averages of nonnegative probabilities. Therefore each distance-one entry of \(P\) itself is zero. For \(d=5,6\), the unique invariant average has strictly positive \(a\), so an unrestricted optimizer cannot vanish on all distance-one edges. This proves the sharp, unrestricted edge-use transition.

## Verification

The standalone standard-library program `verify.py` checks both finite linear dual certificates, the factored Krawtchouk identity over wide integer ranges, every Fourier mode for dimensions \(3\) through \(128\), and independent full-row character sums for dimensions \(3\) through \(9\). Run `python3 verify.py` in the package directory. Its recorded output is included in `verification_output.txt`. The proof above, not finite enumeration, establishes the statements for every integer dimension.

## Relationship to prior work

Boyd, Diaconis, and Xiao (2004) formulate fastest symmetric nonnegative stochastic mixing as a convex semidefinite optimization problem. Boyd, Diaconis, Parrilo, and Xiao (2009; preprint publicly dated 2007) prove general symmetry reduction and provide explicit results for ordinary hypercubes and Hamming graphs with **distance-one** transitions. These general tools justify the starting reduction but do not state the present two-orbit minimax, its exceptional dimensions, or mandatory abandonment of distance-one edges. Karlin, Lindqvist, and Yao (1993) investigate spectra and majorization for hypercube walks; their available abstract does not resolve whether any equivalent extremal statement appears in their inaccessible full text.

The \(d=3,4\) complete-bipartite conclusions follow directly from established methods and are included only to delimit the natural family. The claim of added value concerns the exact \(d=5,6\) optimizer and the all-dimensional, all-optimizer transition at \(d=7\).

## Limitations

No uniqueness of arbitrary nonsymmetric-invariant optimizers is asserted, except the proved zero-weight property for their distance-one edges in dimensions at least seven. The result concerns the second-largest eigenvalue **modulus**, not all mixing-time metrics. The 1993 hypercube-spectrum paper was not available in full text from accessible open sources, and its relevance remains an explicit possible historical-priority risk. The scientific comparison cannot establish absolute absence of equivalent specialized literature. No independent audit has been performed.

## References

1. S. Boyd, P. Diaconis, and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review **46** (2004), 667–689, DOI `10.1137/S0036144503423264`; electronically published 2004-10-29. Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf.
2. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization **20** (2009), 792–819, DOI `10.1137/070689413`; arXiv `0709.0955` (2007-09-06). Full text: https://stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf.
3. S. Karlin, B. Lindqvist, and Y.-C. Yao, *Markov Chains on Hypercubes: Spectral Representations and Several Majorization Relations*, Random Structures & Algorithms **4** (1993), 1–36, DOI `10.1002/rsa.3240040102` (abstract inspected; full text not accessible).
