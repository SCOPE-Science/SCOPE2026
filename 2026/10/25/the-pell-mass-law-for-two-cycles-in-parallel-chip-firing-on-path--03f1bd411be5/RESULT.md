# The Pell mass law for two-cycles in parallel chip-firing on paths

## Finding
For every labelled open path \(P_n\), \(n\ge2\), the conserved-chip enumerator of **distinct primitive two-cycles**, counting each unordered pair of consecutive states once, is
\[
C_n(z)=\sum_{\mathcal O:\,|\mathcal O|=2}z^{\operatorname{mass}(\mathcal O)}.
\]
It is given exactly by
\[
C_2(z)=z,\qquad C_3(z)=z^2(1+z),\qquad
C_n(z)=z(1+z)C_{n-1}(z)+z^3C_{n-2}(z)\quad(n\ge4),
\]
and equivalently by the rational bivariate generating function
\[
\sum_{n\ge2}C_n(z)u^{n-2}=\frac{z}{1-z(1+z)u-z^3u^2}
\]
and the explicit coefficient-finite expansion
\[
C_n(z)=\sum_{j=0}^{\lfloor(n-2)/2\rfloor}
\binom{n-2-j}{j}z^{n-1+j}(1+z)^{n-2-2j}.
\]
In particular, the number of primitive two-cycles is the Pell number
\[
C_n(1)=\frac{(1+\sqrt2)^{n-1}-(1-\sqrt2)^{n-1}}{2\sqrt2}.
\]
The polynomial is reciprocal in the precise sense
\[
C_n(z)=z^{3n-4}C_n(z^{-1}).
\]
For a uniformly sampled primitive two-cycle and its total chip count \(M_n\),
\[
\mathbb E M_n=\frac{3n-4}{2},\qquad
\frac{M_n-(3n-4)/2}{\sqrt n}\ \Longrightarrow\
\mathcal N\left(0,\frac{\sqrt2}{8}\right).
\]
The exact mass support is every integer from \(n-1\) through \(2n-3\), inclusive. The two boundary coefficients are one. These boundary values are compatible with the previously established tree chip-total interval; the new quantitative content is the complete polynomial, orbit enumeration and limiting law.

## Assumptions and scope
The graph is the simple labelled path with vertices \(1,\ldots,n\) and edges between successive labels. At each integer time, every vertex with at least its degree in nonnegative integer chips fires simultaneously, sending exactly one chip to each neighbour. In a single step, a nonfiring vertex does not send chips. Total chip mass is invariant. A primitive two-cycle is a pair of distinct chip configurations exchanged by one update. Initial transient trajectories are not counted; a cycle is counted once, without choice of phase. There is no cap on the initial chip counts, but all primitive two-cycle states satisfy the explicit bounds derived below.

## Proof
**1. The two-phase description.** Let \(G\) be any finite simple connected graph. In a primitive two-cycle, write \(f_v\in\{0,1\}\) for the first-round firing indicator, and \(g_v\) for the second-round indicator. Returning to the same configuration gives \(L(f+g)=0\), with \(L\) the graph Laplacian. Connectedness forces \(f_v+g_v\) to be a constant \(k\in\{0,1,2\}\), independent of the vertex. If \(k=0\), no vertex ever fires and the configuration is fixed; if \(k=2\), all vertices fire in both rounds and the configuration is likewise fixed. Thus a genuine two-cycle has \(k=1\): every vertex fires in exactly one round. This standard periodic-firing principle is consistent with the earlier general criteria in the references.

For a chosen first-round firing pattern \(f\), put
\[
c_v=|\{w:w\sim v,\ f_w\ne f_v\}|.
\]
If \(f_v=1\), the update subtracts \(c_v\) chips at \(v\), so alternation is possible exactly for the integers \(x_v\in[\deg(v),\deg(v)+c_v-1]\). If \(f_v=0\), the update adds \(c_v\) chips, so alternation is possible exactly for \(x_v\in[\deg(v)-c_v,\deg(v)-1]\). All intervals are nonempty precisely when \(c_v\ge1\) for every vertex. Each \(x_v\) is uniquely parametrized by an independent integer \(a_v\in\{0,\ldots,c_v-1\}\), added to the displayed lower endpoint. Every choice is nonnegative and does give a two-cycle: the second-round firing pattern is \(1-f\), and the second update cancels the first one.

Write \(S=\{\{v,w\}\in E:f_v\ne f_w\}\). The chip total is
\[
\sum_vx_v=2|E|-|S|+\sum_va_v.
\]
Indeed, each cut edge has exactly one nonfiring endpoint, so the total correction \(\sum_{f_v=0}c_v\) equals \(|S|\). On a tree, choosing \(S\subseteq E\) determines the firing pattern up to global complementation. These two patterns are the two phases of the same primitive cycle; the numbers \(a_v\) are preserved by the exchange. Thus primitive cycles on the path are in bijection with cut-edge patterns and offset tuples, subject only to \(c_v\ge1\). This also proves finiteness of the enumerator without restricting allowable chip counts artificially.

**2. Weighted transfer.** For the successive path edges let \(b_i\in\{0,1\}\) indicate membership in \(S\). Then \(c_1=b_1\), \(c_n=b_{n-1}\), and \(c_i=b_{i-1}+b_i\) for internal vertices. Hence \(b_1=b_{n-1}=1\) and consecutive edge bits cannot both be zero. Write \([h]_z=1+z+\cdots+z^{h-1}\) for \(h\ge1\), and \([0]_z=0\). The weight for a cut is \(z^{2(n-1)-\sum b_i}\prod_i[c_i]_z\), with the product representing independently chosen offsets. The internal transitions are therefore represented by the ordered row/column matrix
\[
T(z)=\begin{pmatrix}0&z^{-1}\\ 1&(1+z)/z\end{pmatrix},
\qquad
C_n(z)=z^{2n-3}\big(T(z)^{n-2}\big)_{1,1},
\]
where the matrix indices are \(0,1\). The formula holds also for \(n=2\) with the zeroth matrix power. As \(\operatorname{tr}T(z)=(1+z)/z\) and \(\det T(z)=-1/z\), Cayley–Hamilton yields the stated polynomial recurrence. The first values follow from one or two path edges; summing the recurrence over lengths gives the rational generating function, and expanding its denominator by the standard finite binomial expansion yields the explicit formula.

**3. Exact census and symmetry.** Setting \(z=1\) yields \(C_n(1)=2C_{n-1}(1)+C_{n-2}(1)\), with values \(1,2\), giving the stated Pell expression. The recurrence and both initial conditions show inductively that \(C_n(z)=z^{3n-4}C_n(z^{-1})\). Its coefficients are nonnegative and the explicit formula's \(j=0\) term \(z^{n-1}(1+z)^{n-2}\) is strictly positive at every degree in the claimed interval. All terms lie in that interval, and the edge coefficients come exclusively from \(j=0\). Coefficient symmetry gives the exact mean for a uniformly sampled cycle.

**4. Limiting Gaussian law.** Define
\[
\lambda_{\pm}(z)=\frac z2\left(1+z\pm\sqrt{1+6z+z^2}\right).
\]
Solving the recurrence gives
\[
C_n(z)=z\,\frac{\lambda_+(z)^{n-1}-\lambda_-(z)^{n-1}}{\lambda_+(z)-\lambda_-(z)}.
\]
Near \(z=1\), the positive root \(\lambda_+\) is analytic and strictly dominates the other root in modulus: at \(1\) they are \(1+\sqrt2\) and \(1-\sqrt2\). Consequently the logarithm of the moment-generating function \(C_n(e^t)/C_n(1)\), uniformly for small complex \(t\), has leading term \((n-1)(\log\lambda_+(e^t)-\log\lambda_+(1))\), plus an analytic bounded term and an exponentially small correction. Direct differentiation gives
\[
\left.\frac{d}{dt}\log\lambda_+(e^t)\right|_{t=0}=\frac32,\qquad
\left.\frac{d^2}{dt^2}\log\lambda_+(e^t)\right|_{t=0}=\frac{\sqrt2}{8}.
\]
Evaluating this expansion at \(t=s/\sqrt n\), centering by the exact mean, shows convergence of the moment-generating functions to \(\exp(\sqrt2\,s^2/16)\), which is the stated normal law.

## Verification
The companion standalone Python program independently enumerates bounded candidate states by direct two-step simulation for \(2\le n\le10\), enumerates all admissible cuts and offsets, evaluates the polynomial recurrence and the closed binomial expression, and compares all four methods. Direct enumeration covered 349,524 candidate states, and the four enumerators agreed for every tested length. Additional exact coefficient, support, reciprocity, total count and mean checks ran up to \(n=40\). The computer checks corroborate finite instances only; the argument above, rather than finite enumeration, proves the infinite-family statements. Run `python3 artifacts/verify.py` with Python 3's standard library; the associated deterministic output is in `artifacts/verification_output.txt`.

## Relationship to prior work
Jiang (2010) establishes the equal-periodic-firing-count principle used in Step 1. Scully, Zhang and Jiang, *Total Chip Numbers and Motors in the Parallel Chip-Firing Game*, Section 4, already provide the general period-two inequalities (Lemma 4.1) and classify eventual period from total chip number on any tree (Theorem 4.4). Those pre-existing facts are not claimed as discoveries here. Bitar and Goles (1992) give the classical tree period-one-or-two bound. Dall'Asta (2006) analyzes the same degree-threshold rule on a **ring**, explicitly enumerating some periodic populations with periodic boundary conditions; its degree-two ring does not supply the open-path chip-mass enumerator with degree-one endpoints. The additional contribution is an exact mass-resolved number of **primitive two-cycle orbits**, including its rational generating series, Pell count, reciprocal coefficient law and Gaussian limit. Mullen–Nowakowski–Cox (2020) count configurations of **parallel diffusion** on paths; its transfers occur along concentration gradients and are not the degree-threshold firing rule studied here. Searches using both chip-firing and fixed-energy-sandpile terminology did not uncover an already-published identical orbit enumerator, but cannot prove historical uniqueness.

## Limitations
The result concerns primitive period-two **orbits at time zero**, not the sizes of their basins of attraction or transient-time distributions. It treats open paths, not cycles, arbitrary trees or alternate firing conventions. General-period and mass-threshold theorems predate the exact enumeration; external certification is not claimed. A full copy of Bitar–Goles (1992) was not available for detailed comparison; only its bibliographic description and conclusions reported in later primary literature were available. Unindexed equivalent enumerations are a residual originality risk.

## References
1. Tian-Yi Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, first posted 2010-03-04, https://arxiv.org/abs/1003.0943 (Sections 1–2).
2. Ziv Scully, Yan Zhang and Damien Jiang, *Total Chip Numbers and Motors in the Parallel Chip-Firing Game*, 2011 manuscript, https://math.mit.edu/research/highschool/primes/materials/2011/Scully-Zhang-Jiang.pdf (especially Section 4). Its exact first public day has not been independently established.
3. Tian-Yi Jiang, Ziv Scully and Yan X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, first posted 2012-11-29, https://arxiv.org/abs/1211.6786 (general periodic firing-pattern classification).
4. Javier Bitar and Eric Goles, *Parallel Chip Firing Games on Graphs*, Theoretical Computer Science 92 (1992), https://doi.org/10.1016/0304-3975(92)90316-8 (period bound for trees; full text not examined).
5. Luca Dall'Asta, *Exact Solution of the One-Dimensional Deterministic Fixed-Energy Sandpile*, first posted 2006-01-12, https://arxiv.org/abs/cond-mat/0601267 (a degree-two periodic ring, not an open path).
6. Todd Mullen, Richard Nowakowski and Danielle Cox, *Counting Path Configurations in Parallel Diffusion*, first posted 2020-10-09, https://arxiv.org/abs/2010.04750 (different update rule).
