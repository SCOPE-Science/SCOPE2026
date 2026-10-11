# Arbitrarily small synthesis perturbations can satisfy Proposition 3.3 yet destroy \(K\)-wovenness

## Finding
Proposition 3.3 of Agheshteh Moghaddam--Arefijamaal gives a synthesis-operator perturbation criterion intended to guarantee that two \(K\)-frames are woven. The criterion is false as stated, and the failure persists for arbitrarily small synthesis perturbations.

Let
\[
H=\mathbb C^2,\qquad
K=P_{\operatorname{span}\{e_1\}},
\]
and choose any
\[
0<a\le\frac18.
\]
Set
\[
g_a=e_1+a e_2,\qquad
h_a=e_1-a e_2.
\]
On the index set \(\mathbb N\), define
\[
\phi_1=g_a,\quad \phi_2=h_a,\qquad
\psi_1=h_a,\quad \psi_2=g_a,
\]
with
\[
\phi_i=\psi_i=0\qquad(i\ge3).
\]

Both families are \(K\)-frames. Their synthesis operators satisfy all quantitative hypotheses of Proposition 3.3 with
\[
A_\Phi=A_\Psi=2,\qquad
B_\Phi=B_\Psi=2,\qquad
\lambda=2\sqrt2\,a.
\]
However, the weave selecting \(\phi_1\) and \(\psi_2\) consists of two copies of \(g_a\) and zeros. It annihilates
\[
f_a=-a e_1+e_2,
\]
although
\[
K^*f_a=-a e_1\ne0.
\]
Hence that weave is not a \(K\)-frame.

Since
\[
\|T_\Phi-T_\Psi\|=2\sqrt2\,a,
\]
the synthesis perturbation tends to zero with \(a\), while the theorem remains false for every positive \(a\le1/8\).

## Assumptions and scope
The paper works with a separable Hilbert space and a countable index set. The construction uses \(\mathbb N\), with only its first two terms nonzero.

The operator \(K\) is the orthogonal projection onto a one-dimensional closed range. Thus
\[
K^\dagger=K,\qquad \|K^\dagger\|=1.
\]
No pathology involving a nonclosed range is present.

The claim concerns Proposition 3.3 as printed. It does not assert that all perturbation criteria for woven \(K\)-frames fail.

## Proof
For
\[
f=x e_1+y e_2,
\]
the two nonzero coefficients of \(\Phi\) give
\[
|\langle f,g_a\rangle|^2+
|\langle f,h_a\rangle|^2
=
|x+a y|^2+|x-a y|^2
=
2|x|^2+2a^2|y|^2.
\]
The same identity holds for \(\Psi\). Since
\[
\|K^*f\|^2=|x|^2,
\]
both families have lower \(K\)-frame bound \(2\). Because \(a\le1/8\),
\[
2|x|^2+2a^2|y|^2
\le
2\|f\|^2,
\]
so \(2\) is also an admissible upper bound.

The synthesis matrices on the first two coordinates are
\[
T_\Phi=
\begin{pmatrix}
1&1\\
a&-a
\end{pmatrix},
\qquad
T_\Psi=
\begin{pmatrix}
1&1\\
-a&a
\end{pmatrix}.
\]
Therefore
\[
T_\Phi T_\Phi^*
=
T_\Psi T_\Psi^*
=
\begin{pmatrix}
2&0\\
0&2a^2
\end{pmatrix},
\]
so
\[
\|T_\Phi\|=\|T_\Psi\|=\sqrt2.
\]
Also
\[
T_\Phi-T_\Psi=
\begin{pmatrix}
0&0\\
2a&-2a
\end{pmatrix},
\]
hence
\[
\|T_\Phi-T_\Psi\|=2\sqrt2\,a.
\]

Set
\[
\lambda=2\sqrt2\,a.
\]
The second hypothesis of Proposition 3.3 is exactly
\[
\|(T_\Phi-T_\Psi)c\|
\le
\lambda\|c\|.
\]
The first becomes
\[
\lambda(\|T_\Phi\|+\|T_\Psi\|)
=
(2\sqrt2\,a)(2\sqrt2)
=
8a
\le1
=
\frac{A_\Phi}{2}\|K^\dagger\|^{-2}.
\]
Thus every quantitative hypothesis holds.

Now take the partition that selects \(\phi_1\) from \(\Phi\) and \(\psi_2\) from \(\Psi\). Its only nonzero atoms are \(g_a,g_a\). For
\[
f_a=-a e_1+e_2,
\]
we have
\[
\langle f_a,g_a\rangle=0,
\]
so the weaving energy is zero. But
\[
\|K^*f_a\|^2=a^2>0.
\]
No positive lower \(K\)-frame bound can exist.

For the repair, additionally assume every atom of both families belongs to \(R(K)\). Given arbitrary \(f\in H\), put
\[
g=P_{R(K)}f.
\]
Then every weaving has the same coefficient energy at \(f\) and \(g\), and
\[
K^*f=K^*g.
\]
Because \(g\in R(K)\), the closed-range estimate
\[
\|g\|
\le
\|K^\dagger\|\|K^*g\|
\]
is valid. The source's frame-operator perturbation calculation can therefore be applied to \(g\), producing the lower bound
\[
\frac{A_\Phi}{2}\|K^*f\|^2.
\]
The standard sum of the two Bessel bounds supplies the same universal upper bound as in the source.

## Verification
The publisher PDF was inspected at Definition 3.1, the complete statement of Proposition 3.3, and its complete proof. The statement claims a \(K\)-frame lower bound on all of \(H\).

The proof first controls a frame-operator difference by a multiple of \(\|f\|^2\) for arbitrary \(f\in H\), then replaces that \(\|f\|^2\) term by
\[
\|K^\dagger\|^2\|K^*f\|^2.
\]
The paper itself records earlier that the relevant lower estimate for \(K^*\) is on \(R(K)\). The page image of the proof confirms that the disputed substitution is made without restricting \(f\) to \(R(K)\).

All calculations in the counterfamily are exact. No numerical approximation or finite search is used.

The article lists Mathematics Subject Classification \(42C15,42C40\). Its journal page gives an early-publication date of 15 August 2023.

## Relationship to prior work
The earlier paper *Weaving \(K\)-frames in Hilbert Spaces* gives a Paley--Wiener type perturbation theorem with additional structure. In its proof the critical estimate is made on
\[
N(K^*)^\perp,
\]
rather than by applying a closed-range inverse estimate to every vector of the ambient space. That theorem therefore does not imply Proposition 3.3.

The same 2024 source later gives another perturbation statement, Proposition 3.5, whose hypothesis directly controls
\[
\|(I-U^*)f\|
\]
by a multiple of
\[
\|K^*f\|.
\]
That \(K\)-scaled form avoids the uncontrolled \(R(K)^\perp\)-component exploited by the counterexample.

Targeted searches using the exact article title, proposition number, synthesis-operator condition, Moore--Penrose factor, orthogonal-complement mechanism, and correction terminology did not locate an indexed erratum or a source stating this counterfamily.

## Limitations
The finding refutes Proposition 3.3 as stated and gives one sufficient repair by forcing all atoms into \(R(K)\).

The added range condition is not claimed to be necessary. More general valid repairs can replace it with perturbation estimates formulated directly in the \(K^*\)-seminorm or with other hypotheses preventing cancellation by \(R(K)^\perp\).

An unindexed note, thesis, or informal correction may contain the same observation.

## References
1. E. Agheshteh Moghaddam and A. A. Arefijamaal, *New aspects of weaving \(K\)-frames: the excess and duality*, Hacettepe Journal of Mathematics and Statistics 53(3) (2024), 652--666, DOI 10.15672/hujms.1008448.
2. Deepshikha and L. K. Vashisht, *Weaving \(K\)-frames in Hilbert Spaces*, Results in Mathematics 73 (2018), DOI 10.1007/s00025-018-0843-4; preprint arXiv:1710.09562v1.
