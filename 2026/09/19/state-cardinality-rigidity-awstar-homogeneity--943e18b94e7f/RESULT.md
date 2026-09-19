# State-cardinality rigidity for transfinite AW*-homogeneity

## Statement

For a unital C*-algebra \(A\), let
\[
s(A):=\min\Bigl\{|\mathcal F|:\mathcal F\subseteq S(A),\
(\forall\,0\ne a\in A_+)(\exists\,\varphi\in\mathcal F)\ \varphi(a)>0\Bigr\}
\]
be the least cardinality of a family of ordinary states separating
\(A_+\setminus\{0\}\) from \(0\).

Let \(M\) be an AW*-algebra and let \(\kappa\) be an infinite cardinal. Suppose

1. \(M\) is \(\kappa\)-homogeneous in the sense of Arulseelan: there are
   pairwise orthogonal projections \((e_\alpha)_{\alpha<\kappa}\) with
   \[
   1=\bigvee_{\alpha<\kappa}e_\alpha,\qquad e_\alpha\sim 1;
   \]
2. \(M\) admits a separating family of ordinary states of cardinality at most
   \(\kappa\).

Then the cardinal \(\kappa\) is forced by the algebra:
\[
\boxed{\ \kappa=\max\{\aleph_0,s(M)\}\ }.
\tag{1}
\]
Moreover the complete infinite-cardinal homogeneity spectrum is
\[
\boxed{\ 
M\text{ is }\lambda\text{-homogeneous}
\quad\Longleftrightarrow\quad
\aleph_0\le \lambda\le\kappa .
\ }
\tag{2}
\]

Consequently:

- if \(\kappa=\aleph_0\), then \(M\) has a faithful ordinary state and
  \(s(M)=1\);
- if \(\kappa>\aleph_0\), then
  \[
  \boxed{s(M)=\kappa,}
  \tag{3}
  \]
  so the \(\kappa\)-state hypothesis in the uncountable case is cardinally
  optimal: fewer than \(\kappa\) ordinary states cannot separate
  \(M_+\setminus\{0\}\).

The point is that under the simultaneous homogeneity and state-separation
hypotheses of Arulseelan's Theorem A, \(\kappa\) is not an adjustable
mathematical parameter. It is the largest possible homogeneity cardinal and,
in the uncountable case, exactly the state-separation cardinal.

## Application to the local faithful-corner theorem

Arulseelan's Corollary 6.2 starts with a properly infinite AW*-factor \(M\)
and a nonzero projection \(p\) such that \(pMp\) has a faithful ordinary
state. A countably infinite orthogonal family of copies of \(p\) is extended
to a maximal orthogonal family
\[
(p_i)_{i\in I},\qquad p_i\sim p,
\]
and \(\kappa=|I|\ge\aleph_0\) is then used to construct both a
\(\kappa\)-indexed separating family of ordinary states and a
\(\kappa\)-homogeneous decomposition of \(1\).

For every maximal extension of this kind,
\[
\boxed{\ \kappa=\max\{\aleph_0,s(M)\}\ },
\tag{4}
\]
so its cardinal is independent of the choice of maximal extension. In
particular,
\[
\boxed{
\kappa=\aleph_0
\quad\Longleftrightarrow\quad
M\text{ admits a faithful ordinary state}.
}
\tag{5}
\]
If \(\kappa>\aleph_0\), then \(\kappa=s(M)\), every separating family has at
least \(\kappa\) members, and \(M\) is \(\lambda\)-homogeneous exactly for
the infinite cardinals \(\lambda\le\kappa\).

Thus the copy cardinal appearing in the local-corner proof is an intrinsic
state-separation/homogeneity invariant, despite arising there from a
maximal-family construction.

## Proof

### 1. A state sees only countably many members of an orthogonal projection family

Let \(A\) be any unital C*-algebra, let
\((f_i)_{i\in I}\) be pairwise orthogonal nonzero projections, and let
\(\varphi\) be a state. Put
\[
I_\varphi=\{i\in I:\varphi(f_i)>0\}.
\]
For \(n\ge1\), set
\[
I_{\varphi,n}
=\{i\in I:\varphi(f_i)\ge 1/n\}.
\]
If \(F\subseteq I_{\varphi,n}\) is finite, then
\(\sum_{i\in F}f_i\) is a projection bounded by \(1\), hence
\[
\frac{|F|}{n}
\le \sum_{i\in F}\varphi(f_i)
=\varphi\!\left(\sum_{i\in F}f_i\right)
\le1.
\]
Thus every \(I_{\varphi,n}\) is finite, and
\[
I_\varphi=\bigcup_{n\ge1}I_{\varphi,n}
\]
is countable.

Now let \(\mathcal F\) be a family of states separating positive nonzero
elements. Every \(f_i\) must be detected by at least one
\(\varphi\in\mathcal F\), so
\[
I=\bigcup_{\varphi\in\mathcal F} I_\varphi.
\]
Therefore
\[
\boxed{|I|\le |\mathcal F|\cdot\aleph_0.}
\tag{6}
\]
This counting lemma uses only finite additivity of states on finite
orthogonal sums; no normality is involved.

### 2. Countable separating families collapse to one faithful state

If \((\varphi_n)_{n<\omega}\) separates \(A_+\setminus\{0\}\), choose
strictly positive weights \(c_n\) with \(\sum_n c_n=1\), and put
\[
\varphi=\sum_{n<\omega}c_n\varphi_n.
\]
For \(a\ge0\), the equality \(\varphi(a)=0\) forces
\(\varphi_n(a)=0\) for every \(n\), hence \(a=0\). Thus \(\varphi\) is
faithful. The same applies to every finite separating family after
repetition. Consequently, for every unital C*-algebra,
\[
\boxed{s(A)=1\quad\text{or}\quad s(A)\text{ is uncountable}.}
\tag{7}
\]

### 3. The state-separation cardinal is forced

Apply (6) to the \(\kappa\) nonzero orthogonal projections in a
\(\kappa\)-homogeneous decomposition.

If \(\kappa=\aleph_0\), assumption (2) and Step 2 give \(s(M)=1\).

Suppose \(\kappa>\aleph_0\). If \(\mathcal F\) is any separating family,
(6) gives
\[
\kappa\le |\mathcal F|\cdot\aleph_0.
\]
Since \(\kappa\) is uncountable, this implies \(|\mathcal F|\ge\kappa\).
On the other hand, assumption (2) gives a separating family of size at most
\(\kappa\). Hence \(s(M)=\kappa\). This proves (1) and (3).

The same estimate also gives the upper bound on all possible homogeneity
cardinals. If \(s(M)=1\), a faithful state can be positive on only
countably many members of any orthogonal nonzero projection family, so no
uncountable homogeneity is possible. If \(s(M)=\kappa>\aleph_0\), (6)
shows that every orthogonal nonzero projection family has cardinality at
most \(\kappa\). Hence \(M\) cannot be \(\lambda\)-homogeneous for
\(\lambda>\kappa\).

### 4. Homogeneity is downward closed through all infinite cardinals

It remains to prove the converse half of (2). Let
\(\aleph_0\le\lambda\le\kappa\). Partition \(\kappa\) into
\(\lambda\) pairwise disjoint sets
\[
\kappa=\bigsqcup_{\beta<\lambda}J_\beta,
\qquad |J_\beta|=\kappa .
\]
Starting from a \(\kappa\)-homogeneous decomposition
\((e_\alpha)_{\alpha<\kappa}\), put
\[
f_\beta=\bigvee_{\alpha\in J_\beta}e_\alpha .
\]
The \(f_\beta\) are pairwise orthogonal and their join is \(1\).

For each \(\beta\), choose a bijection
\(b_\beta:\kappa\to J_\beta\). Since every \(e_\alpha\sim1\), for each
\(\alpha<\kappa\) choose a partial isometry carrying
\(e_\alpha\) to \(e_{b_\beta(\alpha)}\). The source projections and the
target projections are both orthogonal families. Berberian's addability
theorem for partial isometries therefore sums these partial isometries to
one whose initial projection is
\(\bigvee_{\alpha<\kappa}e_\alpha=1\) and whose final projection is
\(f_\beta\). Hence
\[
f_\beta\sim1.
\]
Thus \((f_\beta)_{\beta<\lambda}\) witnesses
\(\lambda\)-homogeneity. Together with Step 3 this proves (2).

### 5. The local faithful-corner cardinal is canonical

In the properly infinite case of Arulseelan's Corollary 6.2, every maximal
orthogonal \(p\)-copy family considered there extends an initial countable
\(p\)-copy family, so its cardinal \(\kappa\) is infinite. The proof of
that corollary constructs from this family both:

- a separating family of ordinary states of size at most \(\kappa\);
- a \(\kappa\)-homogeneous decomposition of \(1\).

The theorem above therefore applies to every such choice and yields (4).
Since the right-hand side of (4) depends only on \(M\), all such maximal
extensions have the same cardinal.

If that cardinal is countable, the constructed countable separating family
has a faithful weighted sum, proving the forward implication in (5).
Conversely, if \(M\) has a faithful state, Step 1 rules out every
uncountable orthogonal family of nonzero projections, so the construction
cannot produce an uncountable \(\kappa\). This proves (5).

## Model example

Let \(H=\ell_2(\tau)\) for an infinite cardinal \(\tau\), and
\(M=B(H)\). The algebra is \(\lambda\)-homogeneous for every infinite
\(\lambda\le\tau\), by decomposing \(H\) into \(\lambda\) orthogonal
subspaces each of Hilbert dimension \(\tau\).

If \(\tau>\aleph_0\), the \(\tau\) basis vector states separate positive
operators, while (6) applied to the \(\tau\) rank-one basis projections
shows that no smaller family can do so. Hence
\[
s(B(\ell_2(\tau)))=\tau.
\]
For \(\tau=\aleph_0\), a faithful density-matrix state exists and
\(s(B(\ell_2))=1\). This realizes both branches of (1).

## Relation to the recent transfinite result

Arulseelan introduced \(\kappa\)-homogeneity and proved that
\(\kappa\)-homogeneity gives \(\kappa\)-monotone completeness, while
\(\kappa\)-monotone completeness plus \(\kappa\) ordinary states
separating positive elements gives full monotone completeness. The paper
also observes that a countable separating family can be collapsed by a
weighted sum and notes that no such weighted-sum collapse is available in
the uncountable local-corner construction.

The result here identifies the missing converse cardinal obstruction:
an individual ordinary state can detect only countably many members of the
orthogonal projection family witnessing homogeneity. Hence in the
uncountable regime the number of separating states is not merely sufficient
for the proof of monotone completeness; it is the minimum possible number,
and simultaneously the maximal homogeneity cardinal.

The classical Christensen--Pedersen theorem supplies the
\(\aleph_0\)-homogeneous starting point for properly infinite AW*-algebras,
and Berberian's addability theorem supplies the projection-equivalence
aggregation used above. Those ingredients are prior art.

## Limitations and originality boundary

The elementary countability lemma (6), the weighted-sum construction for a
countable family of states, and Berberian addability are not claimed as new.
The claimed contribution is their cardinal synthesis with the newly
introduced \(\kappa\)-homogeneity notion: under the simultaneous hypotheses
of Arulseelan's Theorem A, the parameter \(\kappa\) is intrinsic, is the
largest homogeneity cardinal, and equals the exact state-separation
cardinality whenever it is uncountable. The local faithful-corner
construction then has a choice-independent copy cardinal and the faithful
global-state dichotomy (5).

No claim is made that arbitrary AW*-algebras have an interval-valued
homogeneity spectrum. The exact spectrum (2) is proved only under the
simultaneous \(\kappa\)-homogeneity and \(\le\kappa\)-state-separation
hypotheses. The result also concerns ordinary states; it does not identify
the corresponding invariant formed from normal states.

Originality is asserted only to the best of our knowledge. Arulseelan's
arXiv v1 was inspected through the definitions, Theorem A, Theorems 5.3--5.4,
and Corollary 6.2. It states the countable weighted-sum observation and the
uncountable local construction, but does not state the lower bound (6), the
identity (1), the exact spectrum (2), or the choice-independence consequence
(4). Literature on faithful families of normal states in von Neumann
algebras provides an analogous sigma-finiteness background but does not
cover this ordinary-state AW* statement.

A residual originality risk is older projection-cardinality theory in
Sterling Berberian's *Baer *-Rings* and related AW* dimension literature:
the cited addability and decomposition machinery was checked as prior
structure, but those sources were not exhaustively checked for an equivalent
cardinal invariant combining projection multiplicity with the minimum size
of an ordinary-state separating family. Because \(\kappa\)-homogeneity in
the present form was introduced only in the 2026 paper, any such coverage
would necessarily be in different terminology.

## References

1. J. Arulseelan, *A Transfinite Christensen--Pedersen Argument*,
   arXiv:2609.20718v1 (2026).
   https://arxiv.org/abs/2609.20718
2. E. Christensen and G. K. Pedersen,
   *Properly infinite AW*-algebras are monotone sequentially complete*,
   Bull. London Math. Soc. 16 (1984), 407--410.
   https://doi.org/10.1112/blms/16.4.407
3. S. K. Berberian, *Baer *-Rings*, Grundlehren der mathematischen
   Wissenschaften 195, Springer, 1972.
   https://doi.org/10.1007/978-3-642-15071-5
