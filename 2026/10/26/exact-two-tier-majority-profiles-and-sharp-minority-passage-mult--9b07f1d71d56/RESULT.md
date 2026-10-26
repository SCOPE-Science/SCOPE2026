# Exact two-tier majority profiles and sharp minority-passage multiplicities on odd cycles

## Finding

Fix a labeled cycle with \(n\ge3\) vertices. A binary opinion vector \(x\in\{0,1\}^n\) produces a local majority vector \(y\) by
\[
y_i=\mathbf 1\{x_{i-1}+x_i+x_{i+1}\ge2\},
\]
with indices modulo \(n\). Write \(H=\sum_i x_i\) for initial supporters and \(P=\sum_i y_i\) for local proponents. Let \(N_{n,h,p}\) count labeled vectors with \(H=h\), \(P=p\).

For positive integers \(L,r\) and \(0\le s\le r\), define
\[
C(L,r,s)=
\begin{cases}
\binom r s\binom{L-r-1}{r-s-1},&s<r,\ L\ge2r-s,\\
1,&s=r,\ L=r,\\
0,&\text{otherwise}.
\end{cases}
\]
This is the number of ordered compositions of \(L\) into \(r\) positive parts with exactly \(s\) singleton parts. For \(1\le h\le n-1\), the exact **joint support–proponent distribution** is
\[
\boxed{N_{n,h,p}=\sum_{r=1}^{\min(h,n-h)}\frac nr
\sum_{s=0}^{r}\sum_{t=0}^{r}
C(h,r,s)C(n-h,r,t)\,\mathbf1\{p=h-s+t\}.}
\]
The remaining nonzero entries are \(N_{n,0,0}=N_{n,n,n}=1\). This formula is valid for every \(n\ge3\), including even \(n\).

For **odd** \(n\), passage requires \(P\ge(n+1)/2\). The smallest initial-support coalition able to achieve passage is
\[
\boxed{h_*(n)=\left\lceil\frac{n+3}{3}\right\rceil.}
\]
The exact number \(M_n\) of labeled initial configurations with \(H=h_*(n)\) that pass is
\[
\boxed{M_n=
\begin{cases}
3,&n=3,\\10,&n=5,\\35,&n=7,\\
n,&n=6k+3,\ k\ge1,\\
n(2k+3),&n=6k+5,\ k\ge1,\\
\dfrac{n(7k^2+3k+4)}{2},&n=6k+1,\ k\ge2.
\end{cases}}
\]
Thus the full input/output profile and the multiplicity at the sharp passage boundary are explicit for arbitrary cycle size. For example, at \(n=9\), exactly nine four-supporter inputs cause five local proponents; at \(n=13\), exactly 247 six-supporter inputs cause at least seven local proponents.

## Assumptions and scope

The network is a simple labeled cycle, with the local self vote counted once along with the two adjacent neighbors. Each person casts one binary first-stage vote; the local second-stage vote is a deterministic strict majority among those three votes. There is no iteration, probabilistic tie breaking, abstention, or strategic optimization. Winning means a strict majority of the \(n\) resulting local votes; the passage and sharp multiplicity claims assume odd \(n\). All counts distinguish rotations and reflections as labeled configurations whenever their bit strings differ.

## Proof

**1. Local run rule.** In a circular binary word containing both symbols, decompose into alternating maximal runs of ones and zeros. An interior cell of a run of length at least two retains its bit after the simultaneous radius-one majority update, including both boundary cells of that run. A singleton run flips because both its neighbors have the opposite bit. Therefore if there are \(s\) singleton one-runs and \(t\) singleton zero-runs, then \(P=H-s+t\).

**2. Joint enumeration.** Every nonconstant labeled cyclic binary vector with \(H=h\) has an equal positive number \(r\) of one-runs and zero-runs. For specified \(r,s,t\), choose a start for a marked one-run in \(n\) ways and independently choose the ordered \(r\)-tuples of one-run lengths and zero-run lengths. The counts are \(C(h,r,s)\) and \(C(n-h,r,t)\). Every resulting labeled vector has exactly \(r\) possible marks, so the number is \(nC(h,r,s)C(n-h,r,t)/r\). The formula for \(C\) follows by choosing singleton positions and distributing the residual length above two among the nonsingleton parts (or handling the all-singleton case). Summing over feasible tuples with \(p=h-s+t\) proves the joint count. The two constant vectors are handled separately.

**3. Sharp initial support.** Suppose \(1\le h<n/2\). As there are more zeros than ones, some zero-run is nonsingleton, so \(t\le r-1\). At least \(2r-h\) of the \(r\) one-runs must be singleton when \(2r>h\); hence \(s\ge\max(0,2r-h)\). Thus
\[
P\le h+r-1-\max(0,2r-h)
\le h+\left\lfloor\frac h2\right\rfloor-1.
\]
For \(h=1\), the sole one becomes zero and this bound also gives \(P=0\). For \(2\le h<n/2\), take \(r=\lfloor h/2\rfloor\) one-runs all of length two, except for one length-three run if \(h\) is odd, together with \(r-1\) singleton zero-runs and one zero-run of the remaining length (at least two). This construction attains the upper bound. Consequently, for \(h<(n+1)/2\), passage is possible exactly when \(h+\lfloor h/2\rfloor-1\ge(n+1)/2\), whose first integer solution (or the initial-majority boundary) is \(\lceil(n+3)/3\rceil\). For \(n=3,5,7\), a contiguous block of a strict initial majority supplies a witness at the same threshold.

**4. Sharp winning multiplicities.** Set \(h=h_*(n)\) and \(q=(n+1)/2\). A winning tuple must satisfy \(h-s+t\ge q\), \(t\le r-1\), and \(s\ge\max(0,2r-h)\). The exact feasible \((r,s,t)\) for \(n\ge9\), and their total labeled counts after insertion into the joint formula, are:

- \(n=6k+3\), \(k\ge1\): only \((k+1,0,k)\), contributing \(n\).
- \(n=6k+5\), \(k\ge1\): \((k+1,0,k)\) and \((k+2,1,k+1)\), contributing \(n(k+1)\) and \(n(k+2)\).
- \(n=6k+1\), \(k\ge2\): \((k,0,k-1)\), \((k+1,0,k-1)\), \((k+1,0,k)\), \((k+1,1,k)\), and \((k+2,2,k+1)\), contributing respectively \(nk(k+1)/2\), \(3nk(k-1)/2\), \(n\), \(nk(k+1)\), and \(n(k+1)(k+2)/2\). Their sum is \(n(7k^2+3k+4)/2\).

These lists are exhaustive because the displayed inequalities squeeze \(r\) to the listed values and \(s,t\) to the listed feasible endpoints. For \(n=3,5,7\), direct evaluation of the joint formula shows that the threshold equals the initial strict majority and every placement of exactly that many ones passes: there are \(\binom32=3\), \(\binom53=10\), and \(\binom74=35\) such placements, respectively.

## Verification

The accompanying standalone `verify.py` computes the formula using exact integer arithmetic and, independently, evaluates the local majority rule for every labeled binary input for each \(3\le n\le18\). It compares the entire joint \((H,P)\) histogram, not just totals or winning events. It also checks that all formula coefficients sum to \(2^n\), verifies the sharp threshold and passage multiplicity for every tested odd size, and checks the explicit multiplicity expressions symbolically by exact composition sums on odd rings through size 101. These are finite checks; the proof above supplies the infinite-family argument.

## Relationship to prior work

Chebotarev and Peleg study the power of coalitions under two-tier majority on regular graphs (arXiv:2210.03410, first publicly posted October 7, 2022); their results concern optimal coalitions over classes of regular graphs and other coalition-existence bounds, rather than the exact labeled joint input/output distribution and multiplicities at the boundary of the **fixed** cycle. Classical majority domination of closed neighborhoods (Broere et al., 1995) directly includes the minimum-support optimization as a notion, so the threshold alone is **not asserted to be novel**. Nakar and Ron (arXiv:2205.08972) study eventual fixed-point and periodic behavior in one-dimensional majority automata; this theorem instead counts all inputs by support and a single synchronous update, and does not classify attractors. The elementary local majority rule and circular-run decomposition are established tools. The contribution is the joint counting theorem and its sharp critical-coalition enumeration.

## Limitations

Results do not apply unchanged to directed or irregular networks, heterogeneous thresholds, updates repeated until convergence, nonuniform sampling, or coordinated strategic behavior. The one-step input/output distribution is distinct from distributions among stable configurations or distributions of eventual opinion outcomes. The relevant historical literature is extensive; exact equivalent counting identities expressed in cellular-automaton or majority-domination language may exist despite the comparisons undertaken. Independently verified novelty and independent scientific validation are not claimed.

## References

1. P. Chebotarev and D. Peleg, *The Power of Small Coalitions under Two-Tier Majority on Regular Graphs* (2022), arXiv:2210.03410, https://arxiv.org/abs/2210.03410.
2. Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity* (2022), arXiv:2205.08972, https://arxiv.org/abs/2205.08972.
3. I. Broere, J. H. Hattingh, M. A. Henning, and A. A. McRae, *Majority domination in graphs*, Discrete Mathematics 138 (1995), 125–135, https://doi.org/10.1016/0012-365X(94)00194-N.
4. P. C. Fishburn, F. K. Hwang, and H. S. Lee, *Do local majorities force a global majority?*, Discrete Mathematics 61 (1986), 165–179.
