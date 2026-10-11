# Critical atomic leverage exactly controls singleton erasure for continuous frames

## Finding
Rahimi--Darvishi--Daraby Theorem 3.7 treats the critical case of removing one atom from a continuous frame. Its printed conclusion cannot hold as stated.

Let \(F:\Omega\to H\) be a continuous frame with frame operator \(S\), fix \(\omega_0\in\Omega\), and write
\[
m=\mu(\{\omega_0\}),
\qquad
\ell=m\langle F(\omega_0),S^{-1}F(\omega_0)\rangle.
\]
The theorem assumes \(\ell=1\) and concludes that there is a measurable set \(\Omega_0\) containing \(\omega_0\) with \(\mu(\Omega_0)=0\). But \(\ell=1\) forces \(m>0\). Therefore every measurable set containing \(\omega_0\) has measure at least \(m\), so the stated null-set conclusion is impossible.

The same critical quantity has an exact structural meaning:
\[
F|_{\Omega\setminus\{\omega_0\}}\text{ is a continuous frame}
\quad\Longleftrightarrow\quad
\ell<1.
\]
At \(\ell=1\), the erased frame operator has the explicit nonzero null vector
\[
S^{-1}F(\omega_0).
\]
Thus the correct critical conclusion is failure of the lower frame bound after erasing the atom, not existence of a null set that contains a positive-measure atom.

## Assumptions and scope
The measure is positive, as in the source. The hypothesis \(\ell=1\) implicitly ensures that \(0<m<\infty\): the scalar product is finite because \(F(\omega_0)\in H\) and \(S^{-1}\) is bounded, while a zero atom would give \(\ell=0\).

Only singleton erasure is considered. No assertion is made about arbitrary finite or measurable erasure sets.

The result concerns the canonical leverage \(\ell\), not an arbitrary alternate dual value. The source's preceding Theorem 3.5 supplies a sufficient noncritical condition for arbitrary dual pairs; the exact dichotomy here uses the canonical dual and the positive rank-one structure of the frame operator.

## Proof
Let
\[
F_0=F(\omega_0)
\]
and let \(S_{-0}\) be the frame operator of the restricted mapping on \(\Omega\setminus\{\omega_0\}\). Since the singleton has mass \(m\),
\[
S_{-0}=S-m\,\theta_{F_0,F_0},
\]
where
\[
\theta_{F_0,F_0}f=\langle f,F_0\rangle F_0.
\]
Put
\[
u=\sqrt m\,S^{-1/2}F_0.
\]
Then
\[
S_{-0}
=
S^{1/2}(I-\theta_{u,u})S^{1/2}
\]
and
\[
\|u\|^2
=
m\langle F_0,S^{-1}F_0\rangle
=
\ell.
\]
Because \(S_{-0}\) is an integral of positive rank-one operators, \(S_{-0}\ge0\). Conjugating by the invertible positive operator \(S^{-1/2}\) gives
\[
I-\theta_{u,u}\ge0.
\]
For a rank-one operator this is equivalent to
\[
\|u\|^2\le1.
\]
Hence
\[
0\le\ell\le1.
\]

The restricted mapping is a continuous frame exactly when \(S_{-0}\) is boundedly invertible. Since \(S^{1/2}\) is invertible, this is equivalent to invertibility of \(I-\theta_{u,u}\). Its spectrum consists of \(1\) on \(u^\perp\) and \(1-\|u\|^2\) on \(\operatorname{span}\{u\}\). Therefore it is invertible exactly when
\[
\ell<1.
\]

At \(\ell=1\), direct calculation gives
\[
S_{-0}S^{-1}F_0
=
F_0-m\langle S^{-1}F_0,F_0\rangle F_0
=
(1-\ell)F_0
=0.
\]
Since \(F_0\ne0\), the vector \(S^{-1}F_0\) is nonzero. Thus the erased mapping has no positive lower frame bound.

Finally, the source's minimal-norm calculation yields
\[
\langle S^{-1}F_0,F(\omega)\rangle=0
\]
for almost every \(\omega\in\Omega\setminus\{\omega_0\}\). Its set
\[
\Omega_0=\{\omega:\langle S^{-1}F_0,F(\omega)\rangle\ne0\}
\]
therefore differs from \(\{\omega_0\}\) only by a null set outside the atom. Because the critical hypothesis gives
\[
\langle S^{-1}F_0,F_0\rangle=1/m\ne0,
\]
one has
\[
\mu(\Omega_0)=m,
\]
not zero.

## Verification
The first public preprint and the published full text were inspected at Theorems 3.5 and 3.7 and at the minimal-norm Lemma 3.6. Theorem 3.7 explicitly assumes the critical equality and explicitly states that a zero-measure set containing \(\omega_0\) exists. Its proof defines the support set above and then calls it a null set, despite the atom itself having positive measure under the theorem's hypothesis.

The earlier 2006 paper by Rahimi--Najati--Dehghan was inspected at its robustness theorem. It proves the complementary noncritical implication: when
\[
\mu(\{\omega_0\})\ne
\frac{1}{\langle F(\omega_0),S^{-1}F(\omega_0)\rangle},
\]
erasing \(\omega_0\) leaves a continuous frame. It does not supply the false null-set conclusion of the 2017 theorem.

The operator proof above independently establishes both directions of the exact canonical criterion and identifies the critical null vector. No finite experiment or numerical approximation is used.

## Relationship to prior work
Singleton erasure criteria are classical for discrete frames, and the 2006 continuous-frame paper proves the noncritical direction. The 2017 source explicitly asks what happens at equality and attempts to fill that gap in Theorem 3.7.

The correction shows that the critical case is governed by a rank-one leverage parameter. The erased frame operator is an invertible conjugate of
\[
I-\theta_{u,u},
\]
so there are only two possibilities: \(\ell<1\), when the atom is redundant for the frame property, and \(\ell=1\), when it is essential and the lower frame bound vanishes.

Targeted searches for the exact theorem, the critical equality, singleton erasure, canonical-dual leverage, and null-set formulation did not locate an indexed correction of Theorem 3.7. Later continuous-frame literature discusses null-set sensitivity and frame ranges, but the checked sources did not state this source-specific correction.

## Limitations
The claim is an exact correction of the singleton canonical-erasure boundary. It does not classify simultaneous erasure of several positive-measure atoms or arbitrary measurable subsets.

Pointwise completeness of a continuous family can depend on changes on null sets. The robust conclusion proved here is failure or preservation of the continuous-frame lower bound; the source's stronger point-set incompleteness statement can be recovered only after removing the full exceptional support set, whose measure is \(m\), not zero.

A nonindexed erratum or informal author correction may exist.

## References
1. A. Rahimi, Z. Darvishi and B. Daraby, *Dual pair and Approximate dual for continuous frames in Hilbert spaces*, arXiv:1706.04003v1, first public version 13 June 2017; Mathematical Reports 21(71), no. 2 (2019), 173--191.
2. A. Rahimi, A. Najati and Y. N. Dehghan, *Continuous frames in Hilbert spaces*, Methods of Functional Analysis and Topology 12(2) (2006), 170--182.
