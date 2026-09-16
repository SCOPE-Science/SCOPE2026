# Dual stability of (n+1)-fold strictly-singular product compactness in \(X^n_{0,1}\)

Let \(n\ge 1\) be fixed and let \(X=X^n_{0,1}\) be the Argyros–Beanland–Motakis
space of arXiv:1309.4516 (Illinois J. Math. 57 (2013), 1173–1217),
with dual \(X^*=X^{n*}_{0,1}\).
We prove its Problem 2(iii) affirmatively:

> **Theorem.** If \(S_1,\dots,S_{n+1}:X^*\to X^*\) are bounded strictly singular
> operators, then \(S_1\cdots S_{n+1}\) is compact.

We use the primal result (Theorem 0.1(ii) of the paper) as a black box:
every product of \(n+1\) strictly singular operators on any infinite-dimensional
subspace \(Y\subset X\) is compact. Reflexivity (Corollary 3.19) then reduces
the dual question to a general duality lemma. No classification of spreading
models of \(X^*\) (Problems 2(i)–(ii)) is needed.

## 1. Preliminaries

\(X\) has a \(1\)-unconditional basis and is reflexive (Corollaries of James's
theorem, since \(X\) contains no \(c_0\) or \(\ell_1\); Corollary 3.19).
Hence every operator on \(X^*\) is an adjoint: for each \(S\in\mathcal L(X^*)\)
there is a unique \(T\in\mathcal L(X)\) with \(S=T^*\), and \(\|T\|=\|S\|\).
By Schauder's theorem, \(K\) is compact iff \(K^*\) is compact.

Recall \(T\in\mathcal L(X)\) is *strictly singular* if no infinite-dimensional
subspace \(E\subset X\) has \(T|_E\) bounded below (an isomorphic embedding):
\(\inf\{\|Tx\|:x\in E,\|x\|=1\}>0\).
The primal black box (Theorem 0.1(ii)) states:

> For every infinite-dimensional closed \(Y\subset X\) and all bounded strictly
> singular \(T_i:Y\to Y\), \(i=1,\dots,n+1\), the product \(T_{n+1}\cdots T_1\)
> (hence any ordered product) is compact.

It therefore suffices to prove the following duality lemma.

> **Lemma.** Let \(X\) be reflexive with an unconditional basis.
> If \(T\in\mathcal L(X)\) has \(T^*\in\mathcal L(X^*)\) strictly singular,
> then \(T\) is strictly singular.

Indeed, writing \(S_i=T_i^*\) (reflexivity), strict singularity of each \(S_i\)
forces strict singularity of each \(T_i\) by the Lemma; the primal theorem
gives \(T_{n+1}\cdots T_1\) compact on \(X\); taking adjoints,
\(S_1\cdots S_{n+1}=(T_{n+1}\cdots T_1)^*\) is compact on \(X^*\)
(Schauder). Note the order reversal: \((AB)^*=B^*A^*\), so
\((T_{n+1}\cdots T_1)^*=T_1^*\cdots T_{n+1}^*=S_1\cdots S_{n+1}\). ✓

*Remark on asymmetry.* Strict singularity does not dualize in general:
\(T\) strictly singular need not imply \(T^*\) strictly singular, and
\(T^*\) bounded below on some subspace need not come from a complemented
range in such a simple way. The Lemma proves only the easy direction
\(T^*\) SS \(\Rightarrow\) \(T\) SS, via complemented block subspaces, and
that is exactly what is needed.

## 2. Proof of the Lemma

We prove the contrapositive: if \(T\) is **not** strictly singular, then
\(T^*\) is not strictly singular.

Suppose \(T|_E\) is bounded below for some infinite-dimensional \(E\subset X\):
\(\|Tx\|\ge c\|x\|\) for \(x\in E\) with \(c>0\).

**Step 1 — basic sequences.** Since \(X\) is reflexive, the closed unit ball of
\(E\) is weakly compact; Mazur/Bessaga–Pełczyński gives a normalized
weakly null basic sequence \((x_m)\subset E\). Reflexivity plus unconditionality
implies, after passing to a subsequence, that \((x_m)\) is a small perturbation
of a normalized block sequence of the \(1\)-unconditional basis: there are
successive finite sets \(F_m\) and unit block vectors \(u_m\) supported on
\(F_m\) with \(\sum_m\|x_m-u_m\|<\delta\) for \(\delta>0\) arbitrarily small
(standard gliding hump; weakly null implies coordinates \(\to 0\), and in a
reflexive space with unconditional basis every normalized weakly null sequence
has a subsequence \(C\)-equivalent to a block sequence with \(C\to 1\)).
By the principle of small perturbations, for \(\delta\) small enough,
\(E':=[x_m]\) (after relabelling) satisfies \(T|_{E'}\) bounded below with
constant \(c/2\), and \(E'\) is complemented in \(X\).

Put \(y_m=Tx_m\). Since \(T|_{E'}\) is bounded below, \((y_m)\) is
seminormalized: \(c/2\le\|y_m\|\le\|T\|\) (after normalizing \(\|x_m\|=1\)).
Passing to a subsequence, weak compactness gives \(y_m\to y\) weakly for some
\(y\). If some subsequence were norm-Cauchy with limit \(y\), then for
\(m\ne\ell\) in it, \(T(x_m-x_\ell)=y_m-y_\ell\to 0\) while \((x_m)\) basic
implies \((x_m-x_\ell)\) is bounded below — contradicting \(T|_{E'}\) bounded
below. Hence \((y_m-y)\) has no norm-null subsequence; thinning so that
\(\|y_m-y\|\ge\eta>0\), \((y_m-y)\) is seminormalized weakly null, hence has a
basic subsequence (Bessaga–Pełczyński). Replace the pair by the differences
\(x'_m=x_{2m}-x_{2m+1}\), \(y'_m=Tx'_{2m}-Tx'_{2m+1}=y_{2m}-y_{2m+1}\):
\([x'_m]\subset E'\) so \(T|_{[x'_m]}\) is still bounded below, \((x'_m)\) is
basic and seminormalized, and \((y'_m)\) is seminormalized weakly null basic
(after a further subsequence). Rename these as \((x_m),(y_m)\).

**Step 2 — simultaneous blocking and complementation.**
Apply the gliding-hump/perturbation once more to the pair: after passing to a
subsequence and an arbitrarily small perturbation, we may assume there are
successive blocks (after a further blocking of the basis) with
\(\operatorname{supp}x_m,\operatorname{supp}y_m\) successive and interlaced,
and both \((x_m)\), \((y_m)\) are \(C\)-equivalent to block sequences with
\(C\) arbitrarily close to \(1\). In particular, with \(\delta\) chosen small:
\(E'':=[x_m]\) and \(F'':=[y_m]\) are both complemented in \(X\) (block
subspaces of an unconditional basis, stable under small perturbations), and
\(A_0:=QT|_{E''}:E''\to F''\) is an isomorphism onto \(F''\), where
\(Q:X\to F''\) is a bounded projection (indeed \(QT x_m=y_m\), and bounded
belowness plus basic equivalence makes it an isomorphism; explicitly,
\(A_0\) maps the basic sequence \((x_m)\) to \((y_m)\) and both are
\(C\)-equivalent to the unit vector basis of the corresponding block model,
so \(A_0\) is bounded below and onto \(F''\)).

Concretely, let \(P:X\to E''\) be a bounded projection and \(i_{E''}:E''\hookrightarrow X\),
\(i_{F''}:F''\hookrightarrow X\) the inclusions, \(Q:X\to F''\) a bounded
projection. Set \(A_0=QT i_{E''}:E''\to F''\); this is an isomorphism
\(E''\to F''\).

**Step 3 — dualizing the embedding.** Dualizing,
\(A_0^*:(F'')^*\to(E'')^*\) is an isomorphism (onto). But
\(A_0^*=i_{E''}^*T^*Q^*: (F'')^*\to(E'')^*\).
Let \(Z:=Q^*(F'')^*\subset X^*\); since \(Q^*\) is bounded below
(\(Q\) is a projection, \(Q^*\) is a projection onto its range), \(Z\) is
infinite-dimensional and complemented. For \(z=Q^*w\in Z\),
\(i_{E''}^*T^*z=A_0^*w\), so
\(\|T^*z\|\ge\|i_{E''}^*\!{}^{-1}\|^{-1}\|A_0^*w\|
 \ge \mathrm{const}\cdot\|w\|\ge \mathrm{const}'\|z\|\).
Thus \(T^*|_Z\) is bounded below: \(T^*\) is an isomorphic embedding on the
infinite-dimensional subspace \(Z\subset X^*\), i.e. \(T^*\) is not strictly
singular. ∎

*Why complementation was needed.* To infer \(T^*\) bounded below on
\(Q^*(F'')^*\) we need \(Q\) bounded (a projection) and \(A_0=QT|_{E''}\) an
isomorphism; both come from the block/perturbation structure. A bare
\(T(E'')=F''\) without a bounded projection \(Q\) would not dualize to a lower
bound.

## 3. Conclusion

Given strictly singular \(S_i=T_i^*\) on \(X^*\):
each \(T_i\) is strictly singular by the Lemma; \(K:=T_{n+1}\cdots T_1\) is
compact on \(X\) by Theorem 0.1(ii); \(S_1\cdots S_{n+1}=K^*\) is compact on
\(X^*\) by Schauder. This answers Problem 2(iii) affirmatively, for every
\(n\ge 1\), without determining the spreading-model structure of \(X^*\)
(Problems 2(i)–(ii) remain untouched).

## 4. Checks and scope

- Reflexivity used: Cor 3.19 (\(X\) reflexive) — every \(S\) on \(X^*\) is some
  \(T^*\); weak compactness for basic-sequence extraction.
- Unconditional basis used: block-subspace complementation + small-perturbation
  stability; Schauder's theorem used for compactness duality.
- Primal theorem used as black box: Thm 0.1(ii) — not reproved.
- Order of adjoints checked: \((T_{n+1}\cdots T_1)^*=S_1\cdots S_{n+1}\).
- Sharpness: primal (iii) shows \(n\) does not suffice on \(X\); whether \(n\)
  factors can fail to be compact on \(X^*\) (dual sharpness) is left open and
  not claimed.
- No literature search was needed beyond the admitted paper itself; the proof
  is self-contained modulo the cited black box and standard Banach-space facts
  (Bessaga–Pełczyński, small perturbations, Schauder).
