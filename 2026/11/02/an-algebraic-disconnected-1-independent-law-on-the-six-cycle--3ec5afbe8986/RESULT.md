# An algebraic disconnected 1-independent law on the six-cycle

## Finding

Define
\[
F(t)=t^6+12t^5-72t^4+74t^3-24t^2+1.
\]
There is a unique real zero \(p_*\) of \(F\) in \((0.597345,0.597346)\), and
\(p_*=0.5973455474145\ldots\). On the six-cycle \(C_6\), there exists a
**dihedrally invariant 1-independent bond-percolation measure** under which
all six edges are open with marginal probability exactly \(p_*\), yet the
random spanning graph is disconnected with probability one. Consequently,
if \(p_{\rm zero}(C_6)\) denotes the supremum of marginal parameters for
which a disconnected-almost-surely 1-independent law exists, then
\[
p_{\rm zero}(C_6)\ge p_*>0.597345>1/\sqrt3.
\]
By independent edge thinning, the same conclusion holds with every edge
marginal equal to any prescribed \(p\in[0,p_*]\). Thus \(f_{1,C_6}(p)=0\) throughout this
closed interval. This is an explicit algebraic lower-bound witness, **not** a
proof of the optimal threshold or of the full connectivity function.

## Assumptions and scope

Let the vertices of \(C_6\) be \(0,1,2,3,4,5\) modulo six, with
\(e_i=\{i,i+1\}\) and open indicators \(X_i\in\{0,1\}\).
A bond measure is **1-independent** when the states of any two nonempty edge
families whose incident-vertex sets are disjoint are independent as random
vectors. This is stronger than independence of pairs of disjoint edges.

Encode a spanning subgraph by its six-bit binary mask, bit \(i\) indicating
whether \(e_i\) is open. For the representative masks in the table, let
\(\mathcal O(m)\) be the orbit under the full dihedral group of \(C_6\).
Assign **total orbit probability** \(w_m\) as follows, uniformly among the
\(|\mathcal O(m)|\) labeled masks in that orbit; all unlisted masks receive
probability zero. Every polynomial is evaluated at \(t=p_*\).

| Orbit representative | Orbit size | Total orbit probability |
|---|---:|---|
| `001001` | 3 | \(w_9=t^5+12t^4-72t^3+82t^2-36t+6\) |
| `001011` | 12 | \(w_{11}=-2(t^5+12t^4-73t^3+85t^2-36t+5)\) |
| `001111` | 6 | \(w_{15}=t^5+12t^4-74t^3+79t^2-30t+4\) |
| `010101` | 2 | \(w_{21}=2(1-t)^3\) |
| `010111` | 6 | \(w_{23}=2(2t-1)(t^2-t+1)\) |
| `011011` | 3 | \(w_{27}=-(2t-1)(t^2-4t+1)\) |

These are orbit **total masses**, not probabilities per labeled graph.

## Proof

**1. Algebraic parameter and positivity.** Direct rational substitution gives
\(F(597345/10^6)>0\) and \(F(597346/10^6)<0\).
On this interval \(F'\) is strictly negative: the elementary derivative
Lipschitz bound
\[
|F'(x)-F'(597345/10^6)|
\le (10^{-6})\sum_{k=2}^{6}k(k-1)|[t^k]F|
\]
is smaller than \(-F'(597345/10^6)\). Hence the specified root is unique.
Each of the six listed orbit masses is positive throughout the same rational
interval, as verified by the analogous coefficient-wise Lipschitz inequality
\(w_m(x)\ge w_m(597345/10^6)-10^{-6}\sum k|[t^k]w_m|>0\).

**2. Probability normalization.** The six orbit representatives have sizes
\(3,12,6,2,6,3\), with disjoint orbits. Direct polynomial addition modulo
\(F(t)\) gives \(\sum_m w_m(t)=1\) at \(t=p_*\). Thus these weights define
a nonnegative normalized probability law, invariant under rotations and
reflections.

**3. Marginals and independence.** For any set of edge indices
\(S\subseteq\{0,\dots,5\}\), put
\(M(S)=\mathbb E\prod_{i\in S}X_i\), with \(M(\varnothing)=1\).
Counting orbit members gives \(M(\{i\})=t\) for all \(i\).
Let \(a=M(\{0,1\})\) and \(b=M(\{0,1,2\})\). The following six
identities hold exactly at \(F(t)=0\):
\[
\begin{aligned}
M(\{0,2\})&=t^2,&M(\{0,3\})&=t^2,\\
M(\{0,2,3\})&=t a,&M(\{0,2,4\})&=t^3,\\
M(\{0,2,3,4\})&=t b,&M(\{0,1,3,4\})&=a^2.
\end{aligned}
\]
To verify without numerical approximation, compute each moment as the
weighted fraction of masks containing the indicated edges, expand the
products in \(\mathbb Q[t]\), and reduce modulo the monic sextic \(F\).
Every displayed difference has identically zero remainder. The provided
`verify.py` implements the calculation using exact `fractions.Fraction`
arithmetic, no floating-point assertion and no external library.

Up to dihedral automorphism and interchange of the two families, the 36
unordered pairs of nonempty edge sets with disjoint incident-vertex sets
have **exactly six** orbit types, represented by
\[
(\{0\},\{2\}),\quad (\{0\},\{3\}),\quad
(\{0\},\{2,3\}),\quad (\{0\},\{2,4\}),\quad
(\{0\},\{2,3,4\}),\quad (\{0,1\},\{3,4\}).
\]
The six identities above are exactly the six factorization requirements
\(M(A\cup B)=M(A)M(B)\) for these representatives. Dihedral symmetry gives
all 36 cases. Because arbitrary joint zero-one pattern probabilities are
linear combinations of the product moments (inclusion-exclusion), these
factorizations prove independence of the full edge-state vectors on every
vertex-disjoint pair of edge families.

**4. Disconnection.** All 32 supported labeled configurations have at most
four open edges, whereas a connected spanning subgraph of \(C_6\) needs at
least five. Thus connectivity has probability zero. Independently retaining each original open edge with
probability \(p/p_*\) preserves 1-independence, cannot add connected
configurations, and sets the marginal to any \(0\le p\le p_*\). The exact
assertion in the Finding follows, including the strict numerical improvement
over \(1/\sqrt3\).

## Verification

Run `python3 verify.py`. It constructs the six dihedral orbits on 64
labeled configurations; proves the algebraic root interval by exact rational
signs and a derivative bound; proves all orbit masses positive by rational
interval estimates; verifies normalized mass and the six single-edge
marginals; and verifies **all 36** vertex-disjoint moment-factorization
identities in \(\mathbb Q[t]/(F)\). It checks that all 32 supported
configurations are disconnected. Exact polynomial reduction, not sampled
simulation, establishes the finite identities.

## Relationship to prior work

Day, Falgas-Ravry and Hancock (2019, Sections 8.1, 8.3, 11.5) give the
nonlinear finite-configuration program for \(C_6\), an upper bound on its
connectivity function, and a **numerical suggestion** that the zero-connectivity
threshold is approximately \(0.59733\). Their rigorous exact connectivity
functions concern cycles of length at most five. The algebraic model here
provides a closed polynomial and exact positive weights certifying a lower
bound at essentially the numerically suggested scale; it does not establish
the numerical conjecture's upper-bound half or solve their full Problem 11.20.
The same paper's general program is background methodology rather than an
explicit proof of this particular algebraic witness.

## Limitations

No claim is made that \(p_*\) is the true optimal disconnected threshold,
that dihedral symmetry is without loss of generality in the nonlinear
optimization, or that the full function \(f_{1,C_6}(p)\) is determined.
The statement concerns precisely a finite six-cycle with the specified
1-independence notion. The construction does not imply results for
infinite lattices, longer cycles, higher dependence radii, or arbitrary
nonuniform marginals. Priority for an equivalent exact construction is not
conclusively settled by the literature comparisons performed.

## References

1. A. Nicholas Day, Victor Falgas-Ravry, and Robert Hancock,
   *Long paths and connectivity in 1-independent random graphs*, first public
   preprint 2019-09-30, arXiv:1909.13771; Sections 8.1, 8.3, 11.5 and
   Problem 11.20. https://arxiv.org/abs/1909.13771
2. Paul Balister and Béla Bollobás,
   *Critical Probabilities of 1-Independent Percolation Models*,
   Combinatorics, Probability and Computing 21 (2012), 11–22,
   DOI:10.1017/S0963548311000538.
