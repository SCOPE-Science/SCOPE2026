# Certified length-7 closed mutation loop for the wild (3,2,2) rank-3 quiver

## Context

Rank-3 cluster mutation dynamics and the cycle structure (girth, periodicity,
cluster automorphisms) of wild exchange graphs are recognized open directions
(Fomin–Zelevinsky mutation dynamics; Ervin–Neville mutation-cycle program;
Seven's rank-3 mutation-class framework). For mutation-cyclic $3\times 3$
seeds, Seven (1207.6265) rules out only maximal-green (green-only) sequences,
leaving general closed mutation walks open, and Ervin–Neville (2504.06573)
builds cycles only from triangular extensions of seeds already possessing
reddening sequences. The seed below lies outside those constructions.

## Definitions

Fix the rank-3 skew-symmetric cyclic quiver $Q_C$ with exchange matrix

$$B_C=\begin{pmatrix}0&3&-2\\-3&0&2\\2&-2&0\end{pmatrix}$$

i.e. arrows $1\to 2$ of weight $3$, $2\to 3$ of weight $2$, $3\to 1$ of
weight $2$, with principal coefficients. A framed seed is a pair $(B,C)$
with $C$ the $3\times 3$ $c$-matrix (initially $I_3$), mutated by the
Fomin–Zelevinsky extended-matrix rule. A word $W=(k_1,\dots,k_L)$ over
$\{1,2,3\}$ has no factor $ii$ if $k_t\ne k_{t+1}$ for all $t$.
$P_\sigma$ denotes the permutation matrix with $(P_\sigma)_{i,j}=1$ iff
$i=\sigma(j)$.

## Result

For

$$W=(3,1,2,1,2,1,3),\qquad L=7,$$

with no factor $ii$, mutation of the framed seed $(B_C,I_3)$ along $W$
returns the seed to itself up to the explicit transposition
$\sigma=(12)$:

- $C_{\mathrm{final}}=\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix}=P_\sigma$;
- $B_{\mathrm{final}}=\begin{pmatrix}0&-3&2\\3&0&-2\\-2&2&0\end{pmatrix}
  =P_\sigma^T B_C P_\sigma$;
- $(x_1,x_2,x_3)\mapsto(x_2,x_1,x_3)$ as exact Laurent identities in the
  principal-coefficient cluster algebra;
- every per-step exchange identity
  $x_k x_k'=y^{[c_k]_+}M_+ + y^{[-c_k]_+}M_-$ holds with zero residual;
- all $c$-vector columns are sign-coherent at every step;
- final $F$-polynomials are $(1,1,1)$, as the final variables are permuted
  initials.

Per-step $(B,C)$ trajectory (mutation vertex $k$, then resulting $B,C$ and
numerator term counts of $(x_1,x_2,x_3)$):

| step | $k$ | $B$ | $C$ | #terms |
|---|---|---|---|---|
| 1 | 3 | [[0,-1,2],[1,0,-2],[-2,2,0]] | [[1,0,0],[0,1,0],[2,0,-1]] | 1,1,2 |
| 2 | 1 | [[0,1,-2],[-1,0,0],[2,0,0]] | [[-1,0,2],[0,1,0],[-2,0,3]] | 4,1,2 |
| 3 | 2 | [[0,-1,-2],[1,0,0],[2,0,0]] | [[-1,0,2],[0,-1,0],[-2,0,3]] | 4,5,2 |
| 4 | 1 | [[0,1,2],[-1,0,0],[-2,0,0]] | [[1,-1,0],[0,-1,0],[2,-2,-1]] | 4,5,2 |
| 5 | 2 | [[0,-1,2],[1,0,0],[-2,0,0]] | [[0,1,0],[-1,1,0],[0,2,-1]] | 4,1,2 |
| 6 | 1 | [[0,1,-2],[-1,0,2],[2,-2,0]] | [[0,1,0],[1,0,0],[0,2,-1]] | 1,1,2 |
| 7 | 3 | [[0,-3,2],[3,0,-2],[-2,2,0]] | [[0,1,0],[1,0,0],[0,0,1]] | 1,1,1 |

Hence $Q_C$ admits a nontrivial certified closed mutation loop of length
$7$ (within the pre-fixed window $5\le L\le 10$), i.e. a 7-cycle in its
exchange graph closing up to the cluster automorphism $(12)$.

## Proof / evidence

1. Integer $(B,C)$ closure: independent re-implementation of the
   Fomin–Zelevinsky extended-matrix mutation along $W$ yields exactly the
   table above, closing at $C_{\mathrm{final}}=P_{(12)}$ and
   $B_{\mathrm{final}}=P_{(12)}^T B_C P_{(12)}$.
2. Exact Laurent replay: with $X=(x_1,x_2,x_3)$, $y=(y_1,y_2,y_3)$, each
   step forms $N=y^{[c_k]_+}M_+ + y^{[-c_k]_+}M_-$ and sets
   $X_k\gets N/X_k$. Sympy rational simplification shows each difference
   $X_j-x_{\sigma(j)}$ at the end has identically zero numerator
   (denominators are nonzero generic monomial/binomial products), so all
   seven exchange identities and the final closure are exact Laurent
   identities, not numeric approximations.
3. Integer specializations: evaluation at
   $(x;y)=(2,3,5;2,3,7)$, $(7,11,13;5,7,11)$, $(1,1,1;1,1,1)$,
   $(4,9,2;3,5,2)$ with exact `Fraction` arithmetic closes at
   $(x_2,x_1,x_3)$ in every case.
4. $L=7\in[5,10]$, no adjacent equal letters, and $\sigma=(12)\ne\mathrm{id}$,
   so the loop is nontrivial and not a product of trivial $\mu_k^2$
   backtracks.

## Limitations

- Certifies one length-7 loop; no minimality (shortest-cycle) claim.
- Sibling $L=8,9$ enumeration hits are logged but not Laurent-replayed and
  form no part of this claim.
- No classification of the mutation class or census beyond this word.

## Reproducibility

- `output/artifacts/search_bc.py`: no-backtrack enumeration $L\le 10$
  over $\{1,2,3\}$ with full $(B,C)$-perm closure test.
- `output/artifacts/replay_sym.py` (copy `verify_target.py`): sympy
  rational-function replay asserting zero exchange residual at each step,
  then $B$, $C$, $x$-closure checks; writes `closed_loop_log.json`,
  `final_X.txt`, `Fpolys.txt`.
- Requires only Python 3 + sympy; reruns in seconds.

## References

- T. J. Ervin, S. Neville, Mutation cycles from reddening sequences,
  arXiv:2504.06573 (2025).
- A. Seven, Maximal green sequences of skew-symmetrizable $3\times 3$
  matrices, arXiv:1207.6265 (2012).
- A. Seven, Mutation classes of skew-symmetrizable $3\times 3$ matrices,
  arXiv:1012.3318 (2010).
- A. P. Fordy, R. J. Marsh, Cluster mutation-periodic quivers and
  associated Laurent sequences, arXiv:0904.0200 (2009).
- A. Felikson, P. Tumarkin, Geometry of mutation classes of rank 3
  quivers, arXiv:1609.08828 (2017).
