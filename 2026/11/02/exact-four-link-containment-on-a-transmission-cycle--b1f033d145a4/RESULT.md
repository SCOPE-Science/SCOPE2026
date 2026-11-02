# Exact four-link containment on a transmission cycle

## Finding

Consider a ring of \(n\ge4\) individuals. Exactly four distinct contacts are independently transmissible with probability \(q\in(0,1)\); every other neighboring contact transmits with probability one. A uniformly chosen initial case infects its entire open-edge component, and \(X\) is the final outbreak size including the initial case. Number the four intervening arcs cyclically and let their positive integer population sizes be \(\ell_0,\ell_1,\ell_2,\ell_3\), with \(\sum_i\ell_i=n\). The following is a complete and strict placement classification, up to rotation and reflection.

Writing \(n=4m+r\), \(0\le r\le3\), the minimum of \(\mathbb E[X]\), over all choices of four distinct weakened contacts, is attained exactly by these cyclic arc-size patterns:

| \(r\) | Optimal cyclic arc sizes |
|---|---|
| \(0\) | \((m,m,m,m)\) |
| \(1\) | \((m+1,m,m,m)\) |
| \(2\) | \((m+1,m,m+1,m)\) |
| \(3\) | \((m+1,m+1,m+1,m)\) |

Here \(m\ge1\), because \(n\ge4\). In the nontrivial remainder-two case, the two larger arcs **must be opposite**; making them adjacent strictly increases mean outbreak size by

\[
\frac{2q(1-q)^2}{n}.
\]

Put
\[
\lambda_0=1+2q+2q^2+2q^3-3q^4,\quad
\lambda_1=(1-q^2)^2,\quad
\lambda_2=(1-q)^2(1+q^2).
\]
Then the exact optimum is
\[
\min\mathbb E[X]=\frac{n\lambda_0}{4}+\frac{B_r}{n},\qquad
B_0=0,\quad B_1=B_3=\frac{\lambda_1}{2}+\frac{\lambda_2}{4},\quad B_2=\lambda_2.
\]

## Assumptions and scope

The underlying simple contact graph is the undirected cycle \(C_n\), \(n\ge4\). Four distinct edges are selected before disease introduction and independently declared open with common probability \(q\), with \(0<q<1\). All remaining edges are surely open. A single introduction vertex is sampled uniformly from the \(n\) vertices, independently of the four edge states. The final affected set is, by definition, the connected component of this vertex in the realized open-edge graph. This is also the independent-edge percolation representation of a single-seed, final-size Reed–Frost-type spreading experiment with independent transmissibilities. The four arc sizes count the vertices in the deterministic paths between successive weakened edges, and are therefore positive integers summing to \(n\). No individual-level recovery times, repeated introductions, directed asymmetry, or correlation between transmissions are asserted.

## Proof

**Step 1: Exact expected component size.** Contract each deterministic arc to one weighted vertex of weight \(\ell_i\); the resulting four-link multiscale graph is the four-cycle. For distinct arcs separated by \(d\in\{1,2,3\}\) weakened links clockwise, the two edge-disjoint routes are simultaneously blocked precisely when neither route is fully open. Their independent success probabilities are \(q^d\) and \(q^{4-d}\). Thus the probability of connection is
\[
q^d+q^{4-d}-q^4.
\]
Pairs of individuals within the same arc are connected surely. If \(C\) is the symmetric four-by-four matrix of these arc-connectivity probabilities, then
\[
C=\begin{pmatrix}
1&c_1&c_2&c_1\\
c_1&1&c_1&c_2\\
c_2&c_1&1&c_1\\
c_1&c_2&c_1&1
\end{pmatrix},\quad
c_1=q+q^3-q^4,\quad c_2=2q^2-q^4.
\]
The uniform-introduction identity \(\mathbb E[X]=n^{-1}\sum_{u,v}\mathbb P(u\leftrightarrow v)\) gives the exact finite formula
\[
\mathbb E[X]=\frac{1}{n}\boldsymbol\ell^{\mathsf T}C\boldsymbol\ell.
\]
This identity includes the diagonal vertex pairs and is valid for every placement and every \(n\ge4\).

**Step 2: Positive Fourier decomposition.** The constant vector has eigenvalue \(\lambda_0=1+2c_1+c_2\); the two independent opposite-pair contrasts have the same eigenvalue \(\lambda_1=1-c_2\), and the alternating contrast has eigenvalue \(\lambda_2=1-2c_1+c_2\). With \(a=\ell_0+\ell_2\), \(b=\ell_1+\ell_3=n-a\), \(u=\ell_0-\ell_2\), and \(v=\ell_1-\ell_3\), orthogonality gives
\[
\boxed{\mathbb E[X]=\frac{n\lambda_0}{4}+\frac1n\left\{\frac{\lambda_1}{2}(u^2+v^2)+\frac{\lambda_2}{4}(a-b)^2\right\}.}
\]
Here \(\lambda_1,\lambda_2>0\) and, crucially,
\[
\lambda_1-\lambda_2=2q(1-q)^2>0.
\]

**Step 3: Integer minimization and equality.** The sums \(a,b\) are integers at least two, total \(n\), and \(u\equiv a\pmod2\), \(v\equiv b\pmod2\). At fixed \(a,b\), the smallest possible \(u^2\) is zero for even \(a\) and one for odd \(a\); likewise for \(v^2\). These minima are attained by positive individual arc sizes whenever \(a,b\ge2\). Therefore only the parity of \(a,b\) and the distance \(\lvert a-b\rvert\) need be compared.

If \(n=4m\), choose \(a=b=2m\) even, \(u=v=0\), making the nonconstant energy zero. All three squares can vanish only in this configuration. If \(n=4m+2\), the sums have the same parity. Both odd, the least energy is \(\lambda_1\), at \(a=b=2m+1\). Both even, the least energy is \(\lambda_2\), at \(\lvert a-b\rvert=2\) and \(u=v=0\). Because \(\lambda_2<\lambda_1\), only the opposite-long-arcs pattern wins. If \(n\) is odd, \(a,b\) have opposite parity: \(u^2+v^2\ge1\) and \((a-b)^2\ge1\). Equality in both inequalities is feasible and characterizes exactly one arc size differing by one from the other three (for remainder one), or one arc size smaller by one (for remainder three). These are precisely the tabulated patterns. The strict inequalities establish all equality classifications.

**Step 4: Exact risk and the parity penalty.** Insert the minimum nonconstant energies \(B_r\) into the boxed expression. When \(n=4m+2\), the adjacent-long-arcs arrangement has \(a=b\) odd and energy \(\lambda_1\), whereas opposite long arcs have energy \(\lambda_2\). Their exact difference is \((\lambda_1-\lambda_2)/n=2q(1-q)^2/n\). This is positive for every \(q\in(0,1)\); the distinction vanishes at both excluded endpoints. The proof is global over all positive integral arc partitions, not just over balanced candidates.

## Verification

The standalone dependency-free file `verify.py` enumerates all \(2^4\) weakened-edge states and computes each component's squared-size contribution exactly using rational arithmetic. For every positive four-part composition with total \(n\) from four through ten, it checks the pair-connection quadratic formula at \(q=2/5\). For totals four through sixteen it independently checks the complete set of minimizing compositions at \(q=1/9\), \(q=1/2\), and \(q=9/10\), plus samples against the direct sixteen-state computation. It also prints the exact six-person example \(\mathbb E[X]_{(2,1,2,1)}=187/48\) and \(\mathbb E[X]_{(2,2,1,1)}=63/16\) when \(q=1/2\). Run `python3 verify.py` from the extracted package directory. Exact finite checks corroborate the derivation; the proof above establishes all population sizes and all real \(q\in(0,1)\).

## Relationship to prior work

Deijfen [1] provides the older edge-weighted Reed–Frost epidemic framework and studies epidemic thresholds and vaccination on configuration-model graphs, not optimal placement of four imperfect edges on one finite cycle. Russo, Russo, and Siettos [2] study computational location of wildfire barriers on heterogeneous spatial networks, motivated by reducing spread, rather than the finite closed-form four-barrier susceptibility problem. Mann and collaborators [3] compute connection expressions for homogeneous cyclic motifs within percolation/network generating-function frameworks, but their simple-cycle section does not classify heterogeneous four-edge interventions on a finite cycle by average outbreak size. Their generic methodology motivates checking cyclic connectivity carefully; it does not directly imply the exact strict optimizer classification and parity penalty. The elementary connection-probability and Fourier tools are standard and are not claimed independently novel.

## Limitations

The result is an exact benchmark for a one-dimensional closed contact loop with exactly four equal-strength partially effective barriers and otherwise certain transmission. It is not a prediction of real infection rates, not a general optimal-vaccination theorem on arbitrary graphs, and not valid without qualification for random recovery periods or correlated contacts. The finite numerical enumerations are not substitutes for the algebraic proof. Historical priority of the precise arrangement theorem is provisional: the broader network-reliability and rearrangement literature may contain equivalent statements not identified in the inspected sources. No independent validation or expert certification is claimed.

## References

[1] Maria Deijfen, *Epidemics and vaccination on weighted graphs*, arXiv:1101.4154v1, first public 2011-01-21. https://arxiv.org/abs/1101.4154

[2] Lucia Russo, Paola Russo, Constantinos I. Siettos, *A complex network theory approach for the spatial distribution of fire breaks in heterogeneous forest landscapes for the control of wildland fires*, arXiv:1509.04065v1, first public 2015-09-14. https://arxiv.org/abs/1509.04065

[3] Peter Mann, V. Anne Smith, John B. O. Mitchell, Christopher Jefferson, Simon Dobson, *An exact formula for percolation on higher-order cycles*, arXiv:2102.09261v1, first public 2021-02-18. https://arxiv.org/abs/2102.09261
