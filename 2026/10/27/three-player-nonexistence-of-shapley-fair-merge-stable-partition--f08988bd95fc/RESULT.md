# Three-player nonexistence of Shapley-fair merge-stable partitions

## Finding
For a finite transferable-utility coalition game with nonnegative singleton values, call a partition **Shapley-fair and merge-stable** (SFMS) when (i) every member of every block has a nonnegative Shapley value in that block's restricted game, and (ii) no two blocks admit a strict surplus-increasing merger. Every such game with at most two players possesses an SFMS partition. With three players, this may fail **even when every coalition has nonnegative value**. Indeed, the same three-player witness has a fair two-block partition whose strict profitable merger produces an unfair grand coalition, contradicting the unrestricted Lyapunov monotonicity claimed for the corresponding split-then-merge operator.

## Assumptions and scope
Let \(N=\{1,2,3\}\), let \(v:2^N\to\mathbb R\) with \(v(\varnothing)=0\), and write \(\phi_i(S)\) for player \(i\)'s ordinary Shapley value of the restricted game on \(S\). A partition \(\Pi\) is SFMS precisely if \(\phi_i(S)\ge0\) for every block \(S\in\Pi\) and every \(i\in S\), and \(v(A\cup B)\le v(A)+v(B)\) for every pair of distinct blocks.

The witness is the following complete characteristic function:

| Coalition \(S\) | \(\varnothing\) | \(\{1\}\) | \(\{2\}\) | \(\{3\}\) | \(\{1,2\}\) | \(\{1,3\}\) | \(\{2,3\}\) | \(N\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| \(v(S)\) | 0 | 2 | 2 | 0 | 5 | 0 | 0 | 6 |

Every coalition value is nonnegative; no monotonicity or superadditivity assumption is imposed. The relevant update operator first isolates every negative-Shapley player from each coalition (retaining the residual coalition if internally Shapley-fair, otherwise dissolving it) and then merges any pair of blocks with strictly positive surplus, to exhaustion.

## Proof
**One- and two-player lower bound.** For one player, its singleton partition is fair under nonnegative singleton values. For two players \(N=\{i,j\}\), if \(v(N)\le v(\{i\})+v(\{j\})\), the singleton partition is both fair and merge-stable. Otherwise \(v(N)>v(\{i\})+v(\{j\})\), and the grand coalition's Shapley payoffs satisfy
\[
\phi_i(N)=\frac{v(\{i\})+v(N)-v(\{j\})}{2}>v(\{i\})\ge0,
\qquad
\phi_j(N)>v(\{j\})\ge0.
\]
The grand coalition is therefore fair and vacuously merge-stable. This proves the strict lower bound of three players.

**Grand coalition.** Directly averaging marginal contributions across the six permutations gives
\[
(\phi_1(N),\phi_2(N),\phi_3(N))
=\left(\frac{19}{6},\frac{19}{6},-\frac13\right).
\]
The grand coalition is not Shapley-fair.

**Three two-block partitions.** For \(\Pi_{12}=\{\{1,2\},\{3\}\}\), both members of \(\{1,2\}\) receive \(5/2\), and player 3 receives zero. This partition is fair, but merging its blocks produces surplus \(v(N)-v(\{1,2\})-v(\{3\})=1>0\); thus it is not merge-stable. For \(\Pi_{13}=\{\{1,3\},\{2\}\}\), the Shapley values inside \(\{1,3\}\) are \((1,-1)\); likewise \(\Pi_{23}\) has value \(-1\) for player 3. Both partitions are unfair.

**Singleton partition.** The three singleton payoffs are \((2,2,0)\), so fairness holds, but merging \(\{1\}\) and \(\{2\}\) increases surplus by \(v(\{1,2\})-v(\{1\})-v(\{2\})=1>0\). This fifth and final partition is not merge-stable. Hence no SFMS partition exists.

**Consequences for the dynamics and proposed Lyapunov vector.** From \(\Pi_{12}\), the split phase makes no change and the profitable merger gives \(\Pi_N=\{N\}\). The negative Shapley mass \(\Psi\) increases from zero to \(1/3\), even though total surplus \(\Phi\) increases from 5 to 6. Consequently,
\[
\mathcal V(\Pi_{12})=(-\Psi,\Phi)=(0,5),\qquad
\mathcal V(\Pi_N)=\left(-\frac13,6\right)\prec(0,5)
\]
in lexicographic order. Thus the vector is **not** nondecreasing under the full split-then-merge update. Conversely, the split phase at \(\Pi_N\) isolates player 3, retaining the internally fair block \(\{1,2\}\); the subsequent merge restores \(\Pi_N\). Accordingly the full composite update can fix an unfair, non-SFMS partition. In a one-operation-per-iteration implementation, the same two partitions form a strict split/merge two-cycle.

This example contradicts the unconditional Lyapunov-monotonicity assertion under nonnegative singleton values. It does **not** contradict a separate conditional invariance theorem that explicitly *assumes* Lyapunov monotonicity as an additional hypothesis.

## Verification
The accompanying standard-library program `verify_sfms.py` computes each Shapley value independently by averaging marginal contributions over permutations, enumerates all five partitions and checks their exact fairness and merge-stability truth values using `fractions.Fraction`, and reconstructs both split and merge operations. It also verifies the lexicographic decrease and checks that no numerical approximations enter the certificate. Run `python3 verify_sfms.py`; expected terminal line begins `PASS:`. The program is a finite exact checker; the one/two-player universal boundary follows from the analytical argument above.

## Relationship to prior work
Zhu and Han (2026), *Split-Merge Dynamics for Shapley-Fair Coalition Formation*, arXiv:2603.17153, define precisely this Shapley-fair merge-stability solution concept and the fairness-stable split/surplus-positive merge operators. Its Lemma 3 asserts lexicographic monotonicity from nonnegative singleton values, and the subsequent discussion identifies fixed points with SFMS partitions. The explicit three-player game above violates those unconditional assertions by exhibiting an unfair composite fixed point and no SFMS partition at all. This result is not merely the generic possibility of split/merge cycling, which the paper already permits in its abstract invariance discussion: the obstruction occurs through a **strict surplus-increasing merger**, and the whole-cycle Lyapunov vector decreases at that merger. The conditional theorem with monotonicity separately assumed is not challenged. Apt and Witzel (2007/2009), *A Generic Approach to Coalition Formation*, study abstract stable partitions and preference-relation-dependent convergence conditions; those general principles do not directly assert existence of this specific Shapley/surplus-based SFMS notion under the source's weak singleton hypothesis.

## Limitations
The counterexample requires an unrestricted nonmonotone characteristic function; it says nothing about the existence of SFMS partitions under globally monotone, convex, or superadditive values. The source's additional Lyapunov-monotonicity assumption is false under its stated singleton hypothesis in general, but adding genuinely sufficient restrictions may restore convergence. No external independent scientific audit has been performed.

## References
1. Q. Zhu and Z. Han, *Split-Merge Dynamics for Shapley-Fair Coalition Formation*, arXiv:2603.17153, first submitted 2026-03-17. https://arxiv.org/abs/2603.17153
2. K. R. Apt and A. Witzel, *A Generic Approach to Coalition Formation*, arXiv:0709.0435, first submitted 2007-09-04; later *International Game Theory Review* 11 (2009), 347–367. https://arxiv.org/abs/0709.0435
