# Strict positive-real instability of obligate cyclic ecological communities

## Finding

**Theorem (arbitrary-order cyclic ecological impossibility).** For every integer \(n\geq 3\), consider a Lotka–Volterra community of \(n\) obligate species in a directed single-prey cycle, with non-beneficial interactions to every other species. If a strictly positive equilibrium exists, it is unique and its Jacobian has a **strictly positive real eigenvalue**. In particular, no choice of admissible interaction magnitudes yields a locally stable equilibrium of full coexistence.

More explicitly, index species cyclically, so that the successor of \(n\) is \(1\). The dynamics are
\[
\dot x_i=x_i\left(-a_i-b_i x_i+c_i x_{i+1}-\sum_{j\notin\{i,i+1\}}d_{ij}x_j\right),\qquad i=1,\ldots,n,
\]
with \(a_i,b_i,c_i>0\) and \(d_{ij}\geq0\). Thus each species declines in isolation, benefits from exactly its successor, and experiences no additional beneficial interactions. The model permits arbitrarily asymmetric competitive and antagonistic magnitudes. Strictly positive \(d_{ij}\) for every pair not already specified yields a complete ecological network with predation along the cycle and competition along all non-cycle chords.

At every strictly positive equilibrium \(x^*\), write \(J(x^*)\) for the full \(n\)-dimensional Jacobian. The stronger, exact index statement is
\[
\boxed{\det(-J(x^*))<0.}
\]
The sign forces a positive real eigenvalue, not merely an unspecified unstable complex mode. The result is uniform in population size and all strictly positive parameters.

## Assumptions and scope

Fix any finite integer \(n\geq3\). All quantities are real. Each \(a_i\) is strictly positive (obligate negative intrinsic growth), each \(b_i\) strictly positive (intraspecific self-limitation), and each \(c_i\) strictly positive (benefit from one successor). Every remaining \(d_{ij}\) is nonnegative; the theorem includes zero competitive chords and strictly positive ones. Distinct species are not identified when taking the cyclic successor. A full-coexistence equilibrium means \(x^*_i>0\) for every \(i\). Local stability refers to stability in the complete \(n\)-species dynamical system, not merely a boundary subcommunity. No global attractor, extinction of a specific species, or exclusion of positive periodic trajectories is claimed.

Define the fixed interaction matrix \(B\) by \(B_{ii}=b_i\), \(B_{i,i+1}=-c_i\) (indices modulo \(n\)), and \(B_{ij}=d_{ij}\) otherwise, and the growth vector \(A=(-a_1,\ldots,-a_n)^\mathsf{T}\). Then \(\dot x_i=x_i(A_i-(Bx)_i)\).

## Proof

**Step 1: a feasible equilibrium forces an unusually strong signed dominance.** Suppose \(x^*\) is strictly positive. Its stationarity equations give, for every \(i\),
\[
c_i x^*_{i+1}=a_i+b_i x^*_i+\sum_{j\notin\{i,i+1\}}d_{ij}x^*_j
>b_i x^*_i+\sum_{j\notin\{i,i+1\}}d_{ij}x^*_j.
\]
Let \(X=\operatorname{diag}(x^*_1,\ldots,x^*_n)\) and \(M=BX\). In each row of \(M\), there is exactly one negative entry, in successor column \(i+1\), and its absolute value \(q_i=c_i x^*_{i+1}\) strictly exceeds the sum of the nonnegative entries in all other columns. The positive margin equals \(a_i\), not an asymptotic or numerical quantity.

**Step 2: exact determinant sign by a nonsingular homotopy.** Let \(P\) be the cyclic permutation matrix with \(P_{i,i+1}=1\) and \(D=\operatorname{diag}(q_1,\ldots,q_n)\). Write \(M=-DP+R\), where \(R\) is entrywise nonnegative and \(R_{i,i+1}=0\). Set
\[
M(s)=-DP+sR,\qquad 0\leq s\leq1.
\]
For every such \(s\), \(q_i>\sum_j sR_{ij}\). Reordering the columns by the cyclic permutation makes \(M(s)\) strictly row diagonally dominant. To see nonsingularity directly, if \(M(s)v=0\), choose an index \(j\) where \(|v_j|\) is maximal, and take the row whose successor is \(j\). Its negative term has absolute magnitude \(q_i|v_j|\); the other terms have total absolute magnitude at most \(s(\sum_k R_{ik})|v_j|<q_i|v_j|\), an impossibility unless \(v=0\). Consequently \(\det M(s)\) never vanishes on \([0,1]\) and retains its initial sign. Because an \(n\)-cycle has permutation sign \((-1)^{n-1}\),
\[
\det M(0)=(-1)^n\det(P)\prod_i q_i=-\prod_i q_i<0.
\]
It follows that \(\det(BX)=\det M(1)<0\). Since \(\det X>0\), \(\det B<0\); in particular \(B\) is invertible. Every strictly positive equilibrium solves \(Bx^*=A\), so at most one such equilibrium exists.

**Step 3: a positive real eigenvalue.** At a strictly positive equilibrium the per-capita terms vanish, and direct differentiation yields \(J(x^*)=-XB\). Hence
\[
\det(-J(x^*))=\det(XB)=\det(BX)<0.
\]
The real characteristic polynomial \(p(\lambda)=\det(\lambda I-J(x^*))\) satisfies \(p(0)<0\), whereas \(p(\lambda)>0\) for all sufficiently large positive real \(\lambda\), because it is monic of degree \(n\). The intermediate-value theorem supplies a real root \(\lambda_+>0\), which is an eigenvalue of \(J(x^*)\). Positive-real linear instability implies nonlinear Lyapunov instability of the equilibrium. This completes the theorem.

**Nonvacuity and exact example.** For every \(n\geq3\), set \(a_i=b_i=1\), \(c_i=n\), and \(d_{ij}=1\) for all remaining indices. The full-coexistence vector \(x^*=(1,\ldots,1)\) is an exact equilibrium, since each per-capita rate is \(-1-1+n-(n-2)=0\). Its Jacobian satisfies \(J(x^*)\mathbf1=\mathbf1\), displaying the unstable eigenvalue \(1\). Thus the theorem excludes *stable* coexistence, not the mere existence of a feasible coexistence point.

## Verification

The determinant argument is an all-order proof. A standalone Python 3 program, `verify.py`, provides separate finite exact-arithmetic checks of its algebra: a fixed-seed construction prescribes rational positive equilibria at orders \(3\) through \(9\), solves for the unique positive beneficial coefficient in each row, and tests exact stationarity, strict dominance, negative determinants, and five rational homotopy values. It additionally checks the explicit uniform witness at all orders \(3\) through \(15\). Execution with `python3 verify.py` yields `PASS: 84 nonuniform rational equilibria n=3..9, 5 exact homotopy points each; 13 explicit witnesses n=3..15.` The code uses only Python standard-library rational fractions. These finite checks do not establish the theorem for untested orders; Step 2 does.

## Relationship to prior work

Meng, Horvát, Modes, and Haas (arXiv:2309.16261v1, first posted September 28, 2023) introduce impossible ecological interaction topologies. In their Methods, the three-species obligate cyclic-predation case is proved impossible, while the four- and five-species classifications of impossible topologies rely on numerical sampling, not analytical impossibility proofs. They explicitly conjecture infinite impossible families associated with cycles of obligate predation. The present statement establishes one exact all-order family with strict destabilizing spectral information and an existence witness. Its \(n=3\) subcase is therefore acknowledged as known.

Their extension theorem says a nontrivial extension of a *possible* subecology remains possible; it does not rule out a full-coexistence equilibrium when every smaller subecology is trivial. In the one-benefactor cycle, deleting any species leaves at least one obligate species without its sole benefactor, so this extension result does not imply the present conclusion. The general Lotka–Volterra community-stability literature develops criteria for coexistence and exclusion, but the compared D-stability subcommunity theorems concern interactions of multiple stable communities rather than this obligatory single-benefactor sign pattern.

The determinant proof uses the classical elementary fact that a strictly row-diagonally-dominant square matrix is nonsingular after column permutation. The scientific distinction is the equilibrium-forced dominance and its cyclic determinant *sign*, which together supply a population-size-independent ecological impossibility criterion.

## Limitations

This result prohibits locally stable **equilibria** of strict full coexistence in the specified one-benefactor directed cycle; it neither prohibits unstable positive equilibria (which occur) nor proves extinction, global convergence, absence of positive periodic orbits, or permanence. The conclusions may fail outside the stated sign and intrinsic-growth assumptions, particularly with an additional positive interspecies interaction per species or intrinsically self-sustaining species. Nothing is asserted about discrete-time dynamics, higher-order interactions, or resource-conversion constraints. Bibliographic searches found no exact all-order covering statement in the checked sources, but cannot establish publication priority or exclude a differently formulated earlier theorem.

## References

1. Yu Meng, Szabolcs Horvát, Carl D. Modes, Pierre A. Haas, *Impossible ecologies: Interaction networks and stability of coexistence in ecological communities*, arXiv:2309.16261v1 (September 28, 2023), https://arxiv.org/html/2309.16261v1. Especially Results on three- and four-species ecologies and Methods on obligate cyclic predation and extensions.
2. Won Eui Hong and Robert L. Pego, *Exclusion and multiplicity for stable communities in Lotka–Volterra systems*, arXiv:2102.00611 (February 1, 2021), https://arxiv.org/abs/2102.00611. Especially Theorems 3.3 and 3.4 on coexistence and subcommunity exclusion.
3. M. N. Mooij, M. Baudena, A. S. von der Heydt, I. Kryven, *Stable coexistence in indefinitely large systems of competing species*, arXiv:2404.14031 (April 22, 2024), https://arxiv.org/abs/2404.14031. Abstract and scope comparison only.
