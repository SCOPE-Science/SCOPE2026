# Exact pair-merging distances and sharp diameter in a two-contraction cyclic automaton

## Finding

For every integer \(n\ge5\), let \(\mathcal A_n\) be the binary deterministic automaton with state space \(Q_n=\mathbb Z/n\mathbb Z\) and generators
\[
a(i)=i+1\pmod n,\qquad
b(0)=1,\quad b(2)=3,\quad b(i)=i\quad(i\notin\{0,2\}).
\]
Thus \(b\) is an idempotent of rank \(n-2\) with two disjoint adjacent merges. For distinct states \(x,y\), write \(T_n(\{x,y\})\) for the minimum number of generators in a word sending the two states to the same state. A word is read left to right.

Put \(r_n(z)\in\{0,\ldots,n-1\}\) for the least nonnegative residue of \(z\) modulo \(n\). For \(1\le j\le n-1\) set
\[
\begin{aligned}
u_1&=2,&v_1&=n-2,\\
u_j&=n\left(\left\lceil\frac j2\right\rceil+
  \mathbf1_{\{2\mid n,\ j=n-2\}}\right),&
v_j&=n\left(\left\lceil\frac{j+1}2\right\rceil+
  \mathbf1_{\{2\mid n,\ j=n-1\}}\right)-2 \quad(j\ge2).
\end{aligned}
\]
For \(x\in Q_n\), define the oriented cost \(F_n(x,d)\), \(1\le d\le n-1\), by the exhaustive cases
\[
F_n(x,d)=
\begin{cases}
1+\min\{r_n(-x),r_n(2-x)\},& d=1,\\
n-1+r_n(2-x),& d=2,\\
1+r_n(-x)+u_{d-1},& d=n-2,\\
1+\min\{r_n(-x)+u_{d-1},r_n(2-x)+v_{d-1}\},
  &3\le d\le n-1,\ d\ne n-2.
\end{cases}
\]
The three exceptional cases are disjoint because \(n\ge5\). The complete shortest-merger formula is
\[
\boxed{T_n(\{x,y\})=\min\{F_n(x,d),F_n(y,n-d)\},\quad d=r_n(y-x).}
\]
In particular every unordered pair is mergable, and its sharp worst-case distance is
\[
\boxed{P_n:=\max_{\{x,y\}\subset Q_n}T_n(\{x,y\})=
\begin{cases}
k^2+k-2,&n=2k\ge6,\\
k(k+1)+\lceil k/2\rceil,&n=2k+1\ge5.
\end{cases}}
\]
The formula computes an individual labeled pair distance in constant arithmetic time. It implies that \(\mathcal A_n\) synchronizes, but does **not** assert the length of a shortest word resetting all \(n\) states simultaneously.

## Assumptions and scope

The alphabet has precisely the two generators \(a,b\). The parameter \(n\) ranges over **all** integers at least five, and \(x\) and \(y\) are distinct residue classes. The action of \(b\) is simultaneous on both moved states, not a free choice of two separately available merger letters. Distances refer to words over the original alphabet and count each letter as one step. Repeated rotations count as repeated letters.

## Proof

**1. Directed gap-reduction costs.** Represent a pair of currently distinct states in cyclic order as \((x,x+d)\) for \(1\le d\le n-1\); this orientation fixes which token is regarded as first. Define a *descending-gap strategy* to be a sequence of rotations by \(a\), interspersed with applications of \(b\) which reduce the positive oriented gap by one until the final merge, without ever exchanging the two token roles. For \(d=1\), a merge occurs upon rotating the first token to \(0\) or \(2\) and applying \(b\). Consequently the minimum descending-gap cost is
\[F_n(x,1)=1+\min\{r_n(-x),r_n(2-x)\}.\]
For \(d\ge2\), move the first token by rotations to \(L\in\{0,2\}\) and apply \(b\). Its new state is \(L+1\), and the new oriented gap is \(d-1\), *provided that the second token was not at the other exceptional source*. The disallowed sites are: \(L=0\) when \(d=2\), and \(L=2\) when \(d=n-2\). At such a disallowed site, both tokens move and their gap is unchanged. All other choices are admissible. Thus the shortest descending-gap cost obeys the exact recursion
\[
F_n(x,d)=1+\min_{L\in\Lambda_d}
  \{r_n(L-x)+F_n(L+1,d-1)\},\quad
\Lambda_2=\{2\},\quad\Lambda_{n-2}=\{0\},\quad
\Lambda_d=\{0,2\}\ \text{otherwise}.
\]
Here \(1<d<n\); the recursion is terminating. Rotations between effective contractions can always be chosen in the forward direction, with the minimum number of steps to the selected site. Extra ineffective applications of \(b\) cannot improve a descending-gap strategy: they either leave the pair fixed, or move it identically as one rotation, already available as \(a\).

**2. Solving the recurrence.** Abbreviate \(u_d=F_n(1,d)\), \(v_d=F_n(3,d)\). The base cases are
\[
u_1=2,\quad v_1=n-2,\qquad u_2=n,\quad v_2=2n-2.
\]
At every \(3\le d\le n-1\) except \(d=n-2\), the residue distances to \(0,2\) give
\[
u_d=\min\{n+u_{d-1},\,2+v_{d-1}\},\qquad
v_d=\min\{n-2+u_{d-1},\,n+v_{d-1}\}.
\]
At \(d=n-2\), only the \(L=0\) channel is allowed, hence
\[
u_{n-2}=n+u_{n-3},\qquad v_{n-2}=n-2+u_{n-3}.
\]
Induction in \(d\), separating odd/even \(d\) and the unique forbidden-channel position, gives exactly
\[
u_d=n\left(\left\lceil\frac d2\right\rceil+
\mathbf1_{\{2\mid n,\ d=n-2\}}\right),\qquad
v_d=n\left(\left\lceil\frac{d+1}2\right\rceil+
\mathbf1_{\{2\mid n,\ d=n-1\}}\right)-2
\]
for \(2\le d\le n-1\). One direct way to verify the induction is to insert \(u_{d-1},v_{d-1}\) into the displayed two-term minima: before the forbidden channel, the active term alternates with the parity of \(d\); at the forbidden channel it is uniquely the \(L=0\) term; the exceptional addition of \(n\) is then transmitted to \(v_{n-1}\) only when \(n\) is even. Substitution back into the gap recursion produces the stated closed form for every \(F_n(x,d)\).

**3. Optimality against arbitrary, possibly gap-increasing words.** The following monotonicity is crucial:
\[
F_n(x,1)\le F_n(x,2)\le\cdots\le F_n(x,n-1)
\qquad\text{for each fixed }n,x.
\]
For generic adjacent values of \(d\), it follows immediately from monotonicity of the explicit \(u_j,v_j\) and the minimum of the two residue-affine terms. The exceptional transitions can be checked without a numerical bound on \(n\): at \(d=1\to2\), use \(F_n(x,1)\le1+r_n(2-x)\le F_n(x,2)\); at \(2\to3\), compare \(r_n(2-x)-r_n(-x)\in\{2,2-n\}\) with the first channel of \(F_n(x,3)\) (for \(n=5\), this is the sole available channel); at \(n-3\to n-2\), retaining the \(L=0\) option and \(u_{n-4}\le u_{n-3}\) suffices; at \(n-2\to n-1\), use
\[
v_{n-2}-u_{n-3}=n-2,
\qquad r_n(2-x)-r_n(-x)\ge2-n,
\]
plus \(u_{n-2}\ge u_{n-3}\). Overlaps between these exceptional transitions for \(n=5\) satisfy the same inequalities. This proves the monotonicity for every integer \(n\ge5\).

Define
\[
G_n(\{x,y\}):=\min\{F_n(x,d),F_n(y,n-d)\},
\quad d=r_n(y-x),\qquad G_n(\{x,x\})=0.
\]
By construction, there exists a word of length at most \(G_n\) which merges any given distinct pair. For the reverse inequality, verify the *one-step potential inequality*
\[
G_n(S)\le1+G_n(cS)\qquad (c\in\{a,b\})
\]
for every pair \(S\). For \(c=a\), prepend one rotation to an oriented descending-gap strategy in either orientation. For \(c=b\), if a token at the first exceptional source moves alone, an available descending-gap contraction gives the inequality. If the second token moves alone, the oriented gap grows by one while the first token remains fixed, and the just-proved monotonicity supplies the inequality. If both tokens occupy \(0,2\), applying \(b\) has precisely the same effect on this pair as applying \(a\). If neither token is moved, the pair is unchanged. Finally, if \(b\) merges the pair directly (necessarily \(\{0,1\}\) or \(\{2,3\}\)), its cost is one. These cases exhaust the two generators, and the argument applies to each orientation, hence to their minimum. Summing the potential inequality along any merging word \(w\) of length \(\ell\) yields \(G_n(S)\le\ell+G_n(wS)=\ell\). Therefore \(T_n=G_n\), proving the exact all-pair formula. Iteratively merging any surviving pair gives a full reset word, although the theorem gives no optimal full-reset length.

**4. Exact worst-pair distance.** For \(1\le d\le\lfloor n/2\rfloor\), put
\[
H_n(d)=\max_{x\in Q_n}\min\{F_n(x,d),F_n(x+d,n-d)\}.
\]
Each residue \(r_n(L-x)\), as a function of the integer representative \(x\) on the cyclic interval, decreases by one until its sole jump immediately after \(x=L\). Thus each of the two oriented costs, and hence their minimum, decreases by exactly one on any interval containing no jump of the four residue terms. A maximum can therefore be found among the four phases
\[
 x\in\{1,3,1-d,3-d\}\pmod n.
\]
Substitution of the closed \(u_j,v_j\) into these four explicit possibilities and taking their maximum yields the following **finite algebraic case table**, valid for all integers in the stated ranges:
\[
\begin{array}{c|c}
\text{range}&H_n(d)\\\hline
 d=1&n-2\\
2\le d<\lfloor n/2\rfloor,\ d\text{ even}
 &(d/2+1)n-2\\
3\le d<\lfloor n/2\rfloor,\ d\text{ odd}
 &((d+1)/2)n\\
d=k,\ n=2k,\ k\text{ even}&k^2+k-2\\
d=k,\ n=2k,\ k\text{ odd}&k^2\\
d=k,\ n=2k+1,\ k\text{ even}&k(k+1)+k/2\\
d=k,\ n=2k+1,\ k\text{ odd}&(k+1)n/2.
\end{array}
\]
For full reproducibility of this arithmetic reduction, no numerical optimization is needed: for a chosen \(n,d\), evaluate exactly the four integers \(\min\{F_n(x,d),F_n(x+d,n-d)\}\) with \(x=1,3,1-d,3-d\), then take the largest. The parity table follows by separating \(n\) and \(d\) into even and odd cases and applying the two indicator terms in \(u,v\) only at their declared endpoints. The first three rows increase sufficiently for the boundary and penultimate bands to control the maximum. If \(n=2k\) with even \(k\), the boundary gives \(k^2+k-2\); with odd \(k\), the penultimate even gap gives \(k^2+k-2\), exceeding the boundary \(k^2\) for \(k\ge3\). If \(n=2k+1\), the boundary gives \(k(k+1)+\lceil k/2\rceil\) for either parity of \(k\). This establishes the sharp diameter formula.

## Verification

The included standalone Python program `verify.py` independently constructs the reverse directed graph of unordered pairs and performs multi-source breadth-first search from pairs that are merged in one letter. For every \(5\le n\le120\), it compares **all** such exact finite shortest distances against the formula, verifies the oriented recurrences and monotonicity, checks the four critical phases for each gap, and compares the resulting band maxima and global maximum with the stated expressions. Its expected successful output is:

`VERIFY_OK n=5..120 pair_distances=287970 all_oriented_masks=checked monotonicity=checked four_phase_maxima=checked diameter=checked`

The finite checks are evidence for reproducibility and detection of slips; the proofs of all-\(n\) correctness and the sharp maximum are Steps 1–4, not extrapolation of the checker output.

## Relationship to prior work

Rystsov and Szykuła, *Primitive Automata that are Synchronizing* (first public July 3, 2023), analyze primitivity and synchronizability for permutation/semiconstant generators, not the sharp labeled-pair metric of a rank-\(n-2\) two-merger idempotent. Their *Reset Thresholds of Transformation Monoids* (first public September 15, 2023) gives general monoidal reset-threshold bounds and qualitative pair compressibility; its one-point-contraction hypothesis has kernel type \((k,1,\ldots,1)\), whereas the present \(b\) has two disjoint size-two kernel classes.

Ananichev, Volkov, and Zaks, *Synchronizing automata with a letter of deficiency 2* (2007), give a different two-merger cyclic family: their Section 2 generator maps \(0,1\) to \(-2,-1\) respectively while fixing other states, and the other generator is a backward rotation. Those merger source positions are adjacent and their fixed-point targets are at cyclic displacement two, unlike the present source positions \(0,2\) with displacement-one targets \(1,3\). They study full-reset lengths of their family, not the current all-pair metric. Generic cyclic-automata reset-length results likewise do not imply the exact \(n\)-dependent four-phase maxima.

## Limitations

The theorem does not determine the optimal **full-state** reset threshold; the maximum of pair-specific optimum lengths is a different invariant. It assumes both contractions are triggered by one common letter and are separated as \(0\mapsto1\) and \(2\mapsto3\), with \(n\ge5\). Other relative separations or jump lengths are not covered. The literature comparison includes the closest inspected full texts but cannot exclude an unindexed older equivalent derivation.

## References

1. I. Rystsov and M. Szykuła, *Primitive Automata that are Synchronizing*, arXiv:2307.01302, version 1, first public July 3, 2023. https://arxiv.org/abs/2307.01302
2. I. Rystsov and M. Szykuła, *Reset Thresholds of Transformation Monoids*, arXiv:2309.08321, first public September 15, 2023 (the available PDF includes a later metadata revision). https://arxiv.org/abs/2309.08321
3. D. S. Ananichev, M. V. Volkov and Y. I. Zaks, *Synchronizing automata with a letter of deficiency 2*, Theoretical Computer Science 376 (2007), 30–41, doi:10.1016/j.tcs.2007.01.010.
4. M. V. Volkov, *Slowly Synchronizing Automata with Idempotent Letters of Low Rank*, arXiv:1807.07048, first public July 18, 2018. https://arxiv.org/abs/1807.07048
