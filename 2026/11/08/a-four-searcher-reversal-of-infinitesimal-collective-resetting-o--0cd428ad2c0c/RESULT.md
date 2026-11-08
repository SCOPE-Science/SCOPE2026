# A four-searcher reversal of infinitesimal collective resetting on a five-vertex path

## Finding

Put independent rate-one continuous-time simple random walkers on the five-vertex path \(0-1-2-3-4\), all initially at vertex \(2\), and stop at the first visit to absorbing target \(0\). A common Poisson clock of rate \(r\) sends every walker back to vertex \(2\) simultaneously. Write \(M_N(r)\) for the expected completion time with \(N\) walkers. For \(N\in\{1,2,3,4\}\) the exact right derivative at zero obeys
\[
M_N'(0)<0\ (N=1,2,3),\qquad M_4'(0)>0.
\]
Thus adding a sufficiently rare *simultaneous* reset helps a three-walker team but harms a four-walker team. The sign reversal is stable under sufficiently small positive changes in the path's edge conductances and common jump-time normalization. This is a statement about local response at zero, not global optimal resetting.

## Assumptions and scope

The graph is the undirected path with labeled vertices \(0,1,2,3,4\). Each nonabsorbed walker has an independent exponential rate-one jump clock and jumps to a uniformly chosen neighbor; at vertex \(4\) its only move is to \(3\). The first arrival to \(0\) by any walker terminates the entire trial. The independent common-reset clock at rate \(r\ge0\) restarts all walkers instantaneously at vertex \(2\), without counting a time penalty or changing their subsequent clocks. The process begins with every walker at \(2\). All expectations and derivatives are taken in physical continuous time, with the rate-one convention fixed.

## Proof

Let \(T_N\) be the first-arrival time without resetting and \(S_N(t)=\Pr(T_N>t)\). Because the finite-state killed chain has exponentially decaying survival, both of its first two moments are finite. Let
\[
h_N(r)=\int_0^\infty e^{-rt}S_N(t)\,dt.
\]
The last-reset renewal decomposition, or the first-cycle recursion, gives
\[
M_N(r)=\frac{h_N(r)}{1-rh_N(r)}
\]
for \(r\ge0\). Here the denominator equals \(\mathbb E[e^{-rT_N}]>0\) for \(r>0\) and equals one at zero. Differentiating at zero yields
\[
M_N'(0)=\bigl(\mathbb E[T_N]\bigr)^2-\frac12\mathbb E[T_N^2]. \tag{1}
\]

An exact finite-state formula computes both moments. Use states \(c=(c_1,c_2,c_3,c_4)\) with nonnegative integer entries and \(\sum_i c_i=N\), recording the counts of walkers at the transient vertices. The killed generator \(Q_N\) has off-diagonal rate \(c_i/\deg(i)\) from \(c\) to \(c-e_i+e_j\) for a neighboring transient vertex \(j\); a move from \(1\) to \(0\) kills the trial. Every diagonal entry is \(-N\). Set \(A_N=-Q_N\), let \(\mathbf1\) be the all-ones vector, and put \(c^0=(0,N,0,0)\). Since the killed chain is transient,
\[
u=A_N^{-1}\mathbf1,\qquad v=A_N^{-1}u,\qquad
\mathbb E[T_N]=u(c^0),\quad\frac12\mathbb E[T_N^2]=v(c^0). \tag{2}
\]
The \(A_N\) orders are \(4,10,20,35\) for \(N=1,2,3,4\). Exact rational Gaussian elimination produces the following certified derivative values:

| \(N\) | \(\mathbb E[T_N]\) | \(M_N'(0)\) |
|---:|---:|---:|
| 1 | \(12\) | \(-10\) |
| 2 | \(1555/272\) | \(-169263/73984\) |
| 3 | \(629176456/168587283\) | \(-4963736468372212/9473890663107363\) |
| 4 | \(98335794451053/35264790234112\) | \(52393068681552240430947689/1243605430255921087768428544\) |

The negative and positive signs are strict. Analyticity of the finite-state Laplace transform in \(r\) near zero then proves the small-positive-\(r\) comparison. For edge conductances sufficiently near one, with jump probabilities proportional to conductances and a common total jump-rate scaling sufficiently near one, the killed-generator matrices vary continuously and remain nonsingular. Their inverse moments and the derivative in (1) therefore vary continuously, preserving all strict signs.

## Verification

Run `python3 checker.py` using Python 3.9 or newer; it needs only the standard library. The script reconstructs the killed generator from the transition rules, solves both rational linear systems, and asserts every numerator and denominator in the table. It also reconstructs the *unsymmetrized labeled-walker* killed chains for \(N=1,2,3\) (of orders 4, 16 and 64) and checks agreement, independently of count-state lumping. The four-walker result is certified by the complete 35-state rational linear solve. No Monte Carlo approximation is used as a proof.

## Relationship to prior work

Biroli, Majumdar and Schehr (first posted 2023-03-31) study the effect of the number of independently moving *Brownian* searchers on the usefulness of individual or simultaneous Poisson resetting on the half-line; their simultaneous-reset analysis supplies the general renewal framework and finds a different, continuum critical team number. Their investigated Brownian survival function does not specify the killed generator or the rational sign change on this finite reflecting path. Wang, Chen and Huang (2021) analyze single random walks on networks with multiple resetting nodes via a renewal method, not the minimum hitting time of a simultaneously reset team. The present claim is the exact finite-graph sign reversal, not the general reset renewal identity.

## Limitations

Only \(N\in\{1,2,3,4\}\), the specified path, source and target, and sufficiently small rates \(r>0\) are proved. This does not show that \(r=0\) is a global optimum for four walkers, nor that every \(N\ge4\) has positive derivative. Independent scientific review has not been performed. The phenomenon uses simultaneous resetting, not independently resetting each walker.

## References

- M. Biroli, S. N. Majumdar and G. Schehr, *Critical number of walkers for diffusive search processes with resetting* (first posted March 31, 2023), https://arxiv.org/abs/2303.18012, especially Section IV, Eq. (20)-(29).
- S. Wang, H. Chen and F. Huang, *Random walks on complex networks with multiple resetting nodes: a renewal approach* (first posted May 18, 2021), https://arxiv.org/abs/2105.08323.
- S. Reuveni, *Optimal stochastic restart renders fluctuations in first passage times universal* (2016), https://doi.org/10.1103/PhysRevLett.116.170601.
