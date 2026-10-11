# A surjective image of a closed fusion subspace need not be closed

## Finding
Huang--Yang Theorem 3.5(1) states that if \(U\) is surjective, \(UK=KU\), and
\[
\Lambda=\{(W_j,\Lambda_j,v_j)\}_{j\in J}
\]
is a \(K\)-\(g\)-fusion frame, then
\[
\Phi=\{(UW_j,\Lambda_j\pi_{W_j}U^*,v_j)\}_{j\in J}
\]
is again a \(K\)-\(g\)-fusion frame. The statement omits a necessary admissibility condition: the paper defines fusion subspaces to be closed, but surjectivity of \(U\) does not imply that \(UW_j\) is closed.

Let
\[
H=\ell^2(\mathbb N)
\]
with standard orthonormal basis \((e_n)_{n\ge1}\), and define
\[
Ue_{2n}=e_n,\qquad Ue_{2n-1}=0.
\]
Then \(UU^*=I\), so \(U\) is a coisometry and in particular is surjective.

Let \(D\) be the closed diagonal operator
\[
Dx=(n x_n)_{n\ge1}
\]
with domain
\[
\operatorname{Dom}(D)=
\{x\in\ell^2(\mathbb N):(n x_n)_{n\ge1}\in\ell^2(\mathbb N)\}.
\]
Define
\[
W=
\left\{
\sum_{n\ge1}
\bigl(n x_n e_{2n-1}+x_n e_{2n}\bigr):
x\in\operatorname{Dom}(D)
\right\}.
\]
The interlacing unitary
\[
\ell^2\oplus\ell^2\longrightarrow\ell^2
\]
identifies \(W\) with the graph of \(D\). Since \(D\) is closed, \(W\) is a closed subspace of \(H\). On the other hand,
\[
U\left(
\sum_{n\ge1}
(n x_n e_{2n-1}+x_n e_{2n})
\right)
=
\sum_{n\ge1}x_ne_n,
\]
so
\[
UW=\operatorname{Dom}(D).
\]
This domain is dense and nonclosed in \(\ell^2\). For example,
\[
x=(1/n)_{n\ge1}\in\ell^2
\]
does not belong to \(\operatorname{Dom}(D)\), while its finite truncations do and converge to \(x\).

Now put
\[
K=I,\qquad
J=\{1,2\},\qquad
W_1=W,\qquad W_2=H,
\]
take \(v_1=v_2=1\), and define
\[
\Lambda_1=\pi_W,\qquad \Lambda_2=I.
\]
Then, for every \(f\in H\),
\[
\sum_{j=1}^2
\|\Lambda_j\pi_{W_j}f\|^2
=
\|\pi_Wf\|^2+\|f\|^2.
\]
Hence
\[
\|f\|^2
\le
\sum_{j=1}^2
\|\Lambda_j\pi_{W_j}f\|^2
\le
2\|f\|^2,
\]
so the original family is an \(I\)-\(g\)-fusion frame with bounds \(1\) and \(2\). The operator \(U\) is surjective and commutes with \(K=I\), so all hypotheses of Theorem 3.5(1) hold. Nevertheless its proposed first fusion subspace
\[
UW_1=\operatorname{Dom}(D)
\]
is not closed. Thus the conclusion is not an object of the class defined in the paper, and the orthogonal projection \(\pi_{UW_1}\) used in the proof is unavailable.

For a surjective bounded operator \(U\), the exact closed-image criterion is
\[
UW\text{ is closed}
\quad\Longleftrightarrow\quad
W+N(U)\text{ is closed}.
\]
Therefore the theorem needs, at minimum, the hypothesis
\[
W_j+N(U)\text{ is closed for every }j,
\]
or its projection formulas must use \(\overline{UW_j}\), as the paper's own Lemma 2.8 already does.

## Assumptions and scope
The counterexample uses the same ambient Hilbert space for domain and codomain, a coisometry rather than merely an arbitrary surjection, and the ordinary case \(K=I\). It therefore applies both to Theorem 3.5(1) and to the coisometric Corollary 3.6(1).

The conclusion is deliberately limited to the closed-subspace and orthogonal-projection part of the construction. Replacing \(UW_j\) by \(\overline{UW_j}\) makes the relevant projection well-defined and matches Lemma 2.8, but no claim is made here that this alone resolves any separate convention concerning the codomain of the transformed analysis operator.

## Proof
The operator \(D\) is closed: if \(x^{(r)}\to x\) in \(\ell^2\) and \(Dx^{(r)}\to y\) in \(\ell^2\), then coordinatewise convergence gives
\[
y_n=nx_n
\]
for every \(n\), hence \(x\in\operatorname{Dom}(D)\) and \(Dx=y\). Its graph is therefore closed. The interlacing map
\[
(a,b)\longmapsto
\sum_{n\ge1}(a_ne_{2n-1}+b_ne_{2n})
\]
is unitary from \(\ell^2\oplus\ell^2\) onto \(H\), so the image of the graph of \(D\) is the closed subspace \(W\).

The formula for \(U\) shows directly that
\[
UW=\operatorname{Dom}(D).
\]
The sequence
\[
x=(1/n)_{n\ge1}
\]
belongs to \(\ell^2\), but
\[
Dx=(1,1,\ldots)
\]
does not. The finite truncations \(x^{(N)}\) lie in \(\operatorname{Dom}(D)\) and converge to \(x\), proving that \(UW\) is nonclosed.

For the exact boundary, let
\[
q:H\to H/N(U)
\]
be the quotient map. Since \(U\) is bounded and surjective, it factors as
\[
U=\widetilde U q,
\]
where \(\widetilde U:H/N(U)\to H\) is a Banach-space isomorphism. Hence
\[
UW\text{ is closed}
\quad\Longleftrightarrow\quad
q(W)\text{ is closed}.
\]
By the definition of the quotient topology,
\[
q(W)\text{ is closed}
\quad\Longleftrightarrow\quad
q^{-1}(q(W))\text{ is closed}.
\]
But
\[
q^{-1}(q(W))=W+N(U).
\]
This proves
\[
UW\text{ is closed}
\quad\Longleftrightarrow\quad
W+N(U)\text{ is closed}.
\]

## Verification
The target article defines every \(W_j\) as a closed subspace and uses \(\pi_{W_j}\) for its orthogonal projection. Its Lemma 2.8 states the general identity
\[
\pi_WT^*=\pi_WT^*\pi_{\overline{TW}},
\]
with the closure explicitly present.

Theorem 3.5 then assumes only that \(U\) is surjective and replaces the closed \(W_j\) by \(UW_j\), while its proof writes \(\pi_{UW_j}\) without establishing that \(UW_j\) is closed. The coisometric Corollary 3.6 inherits the same issue because a coisometry can have infinite-dimensional kernel.

Every step of the counterexample is exact. No finite experiment, numerical approximation, or timeout is used as evidence for the infinite-dimensional claim.

## Relationship to prior work
The fact that images of closed subspaces under bounded operators need not be closed is standard functional analysis. The source-specific issue is that Theorem 3.5 uses such images as fusion subspaces under only surjectivity, despite its own definition requiring closed subspaces.

The paper itself cites an operator-perturbation lemma in the form
\[
\pi_WT^*=\pi_WT^*\pi_{\overline{TW}},
\]
so the closure needed by the projection identity is already visible in its preliminaries. Later relay-fusion-frame literature likewise states the corresponding projection identity with \(\overline{TW}\), not \(TW\) without a closedness condition.

Targeted searches for the exact DOI, theorem number, image-subspace closedness, quotient-kernel criterion, and closure repair did not locate an indexed correction of Theorem 3.5. The closest indexed frame-theoretic findings concern other range-compression, scaling, perturbation, or operator-orbit mechanisms and do not imply this source-specific admissibility obstruction.

## Limitations
The result identifies the exact condition for the image subspace \(UW_j\) to remain closed under a surjective \(U\). It does not claim that closedness is the only issue in every formalization of \(g\)-fusion frames.

Replacing \(UW_j\) by \(\overline{UW_j}\) repairs the projection domain appearing in the proof, but this finding does not assert a fully revised theorem under every possible codomain convention for \(\Lambda_j\).

An unindexed erratum, thesis remark, or informal correction may contain the same source-specific observation.

## References
1. Y. Huang and Y. Yang, *K-g-fusion frames in Hilbert spaces*, Journal of Inequalities and Applications 2020, article 57, DOI 10.1186/s13660-020-02320-0.
2. X. Li, S. Yang and Y. Zhu, *Some results about operator perturbation of fusion frames in Hilbert spaces*, Journal of Mathematical Analysis and Applications 421 (2015), 1417--1427.
3. G. Hong and P. Li, *Relay fusion frames and bridging results for fusion frames*, Journal of Mathematical Analysis and Applications 489 (2020), article 124124, DOI 10.1016/j.jmaa.2020.124124.
