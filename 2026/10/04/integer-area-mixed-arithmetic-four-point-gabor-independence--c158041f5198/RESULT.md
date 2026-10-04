# Integer-area mixed-arithmetic four-point Gabor independence

## Finding

Let
\[
\sigma((x,\omega),(y,\eta))=x\eta-y\omega,
\]
and let \(u,v\in\mathbb R^2\) be linearly independent. Write
\[
\nu=\alpha u+\beta v.
\]
Assume that \(0,u,v,\nu\) are distinct, that
\[
q=|\sigma(u,v)|\in\mathbb N,
\]
and that
\[
\dim_{\mathbb Q}\operatorname{span}_{\mathbb Q}\{1,\alpha,\beta\}=2.
\]
Then, for every nonzero \(f\in L^2(\mathbb R)\), the four vectors
\[
f,\qquad \pi(u)f,\qquad \pi(v)f,\qquad \pi(\nu)f
\]
are linearly independent.

The case \(q=1\) is the recent critical mixed-arithmetic theorem. The new content is the full integer supercritical family \(q\ge2\).

## Assumptions and scope

The time-frequency shift convention is
\[
\pi(x,\omega)=M_\omega T_x,
\]
with the usual projective commutation law. Only the absolute symplectic area \(q\) is assumed integral. No smoothness, decay, or continuity is imposed on \(f\) beyond \(f\in L^2(\mathbb R)\).

The theorem is restricted to positive integer values of \(|\sigma(u,v)|\). It does not claim a classification for noninteger supercritical area and does not contradict known subcritical four-point counterexamples.

## Proof

It is enough to prove the case \(\sigma(u,v)=q>0\), since interchanging \(u\) and \(v\) changes the sign. Let \(S\) be the real matrix with columns \(u,v\), so \(\det S=q\). Put
\[
D=\begin{pmatrix}1&0\\0&q\end{pmatrix},
\qquad
C=DS^{-1}.
\]
Then \(\det C=1\). In dimension two, \(\operatorname{Sp}(2,\mathbb R)=\operatorname{SL}(2,\mathbb R)\), so \(C\) is symplectic. Metaplectic covariance therefore reduces the configuration to
\[
0,\qquad e_1,\qquad q e_2,\qquad (\alpha,q\beta).
\]
Because multiplication by the nonzero rational number \(q\) does not change rational span,
\[
\dim_{\mathbb Q}\operatorname{span}_{\mathbb Q}\{1,\alpha,q\beta\}=2.
\]
Choose a primitive integer relation
\[
k_1\alpha+k_2q\beta=r\in\mathbb Q,
\]
and complete \((k_1,k_2)\) to a matrix
\[
A=\begin{pmatrix}\ell_1&\ell_2\\k_1&k_2\end{pmatrix}\in\operatorname{SL}(2,\mathbb Z).
\]
Then
\[
A(\alpha,q\beta)^T=(a,r)^T,
\]
where \(a\notin\mathbb Q\); otherwise the invertibility of \(A\) over \(\mathbb Z\) would force both \(\alpha\) and \(q\beta\), hence both \(\alpha\) and \(\beta\), to be rational. Write \(r=p/m\) in lowest terms. The two core vectors become
\[
\lambda_1=Ae_1,\qquad \lambda_2=qAe_2.
\]
They lie in \(\mathbb Z^2\) and satisfy
\[
|\det(\lambda_1,\lambda_2)|=q.
\]
Thus they generate an index-\(q\) sublattice of \(\mathbb Z^2\).

Suppose a nontrivial four-term dependence exists. The complete three-point theorem forces all four coefficients to be nonzero. Applying the Zak transform gives the same one-step scalar equation as in the critical proof,
\[
P(x,s)F(x,s)+c_3e^{-2\pi i(p/m)x}F(x-a,s+p/m)=0,
\]
where
\[
P=c_0+c_1\chi_{\lambda_1}+c_2\chi_{\lambda_2}
\]
is a nonzero lattice trinomial. Iterating exactly \(m\) times closes the rational frequency displacement and yields
\[
F(x-\theta,s)=B_s(x)F(x,s),
\qquad
\theta=ma\notin\mathbb Q,
\]
with \(B_s(x)=L(e^{2\pi is},e^{2\pi ix})\) for a nonzero Laurent polynomial \(L\). The derivation uses only that \(\lambda_1,\lambda_2\in\mathbb Z^2\), not that they form a unimodular basis.

The only place where unimodularity enters the critical proof is the finiteness of the zero set of \(P\). Here it has a finite-index replacement. Define
\[
\Phi:\mathbb T^2\longrightarrow\mathbb T^2,
\qquad
z\longmapsto\bigl(\chi_{\lambda_1}(z),\chi_{\lambda_2}(z)\bigr).
\]
Since \(|\det(\lambda_1,\lambda_2)|=q\), the induced map on character lattices has cokernel of order \(q\). Hence \(\Phi\) is a surjective covering homomorphism of degree \(q\). In the target torus the equation
\[
c_0+c_1z_1+c_2z_2=0,
\qquad |z_1|=|z_2|=1,
\]
has at most two solutions: after eliminating \(z_2\), the equation
\[
|c_0+c_1z_1|=|c_2|
\]
is a nonconstant first-harmonic equation on the circle. Therefore
\[
\#\{z\in\mathbb T^2:P(z)=0\}\le2q.
\]
The return multiplier \(B\) is a nonvanishing monomial times a product of \(m\) torus translates of \(P\), so its torus zero set is finite as well.

From this point every hypothesis of the source paper's post-finiteness argument is unchanged. The finite zero set leaves a connected transverse arc carrying a positive-measure family of nonzero Zak fibres on which \(B\) is zero-free. After the standard periodicizing gauge, the fibre equation is a measurable cocycle over the irrational rotation by \(\theta\). The measurable winding lemma forces winding zero. A periodic logarithm therefore exists; continued-fraction returns quantize its holonomy into the source paper's Haar-null resonance group, and real-analytic dependence on the transverse parameter forces that holonomy to be constant. Undoing the gauge makes the Laurent holonomy equal on an interval to
\[
Ce^{-2\pi i\theta s}.
\]
On the other hand, the Laurent-polynomial structure of \(B\) gives a nontrivial polynomial relation over \(\mathbb C(e^{2\pi is})\) for the same holonomy. Since \(\theta\notin\mathbb Q\), the frequencies \(k-r\theta\) occurring after expansion are all distinct, so no nontrivial Laurent relation can vanish on an interval. This contradiction proves linear independence.

## Verification

The proof was checked at the level of hypotheses used in each stage of the recent critical argument. Its normal-form and return-cocycle derivations require only an integral three-point core after symplectic normalization. The source paper's later measurable-dynamical and Laurent-algebra lemmas require only: an irrational return angle, a nonzero Laurent return multiplier, a finite exceptional-fibre set, and the resulting zero-free active arc. All four are established above.

The new finite-index lemma is independent of computation: an integer character matrix of determinant \(q\) induces a degree-\(q\) torus covering, and the target trinomial has at most two zeros. Thus the source's finite-zero argument changes only from the bound \(2\) to the bound \(2q\).

No finite numerical experiment is used as evidence for the infinite-dimensional statement.

## Relationship to prior work

Oussa's 2026 critical mixed-arithmetic theorem proves the statement when \(|\sigma(u,v)|=1\) and explicitly records the supercritical mixed-arithmetic cell as only partially classified. Its proof isolates the finite-zero lemma for a unimodular lattice trinomial as the critical-lattice input; all subsequent winding, holonomy, and Laurent-algebra steps are formulated after that finiteness reduction.

Oussa's earlier 2026 large-covolume theorem proves the supercritical case when \(1,\alpha,\beta\) are rationally independent, and separately handles rational coordinates. It does not cover rational rank two. The 2025 mixed-integer trichotomy supplies necessary conditions for the remaining branch for Schwartz windows, but does not establish all-window \(L^2\) independence there.

The present result fills a natural infinite arithmetic slice of the remaining supercritical mixed cell: every positive integer covolume. The mechanism is a finite-index replacement of the source's unimodular torus automorphism by a finite covering.

## Limitations

The proof needs \(|\sigma(u,v)|\in\mathbb N\) in order to place the normalized three-point core inside \(\mathbb Z^2\) while preserving symplectic area. It gives no conclusion for noninteger supercritical values. It also does not claim that the integer-area family exhausts the supercritical mixed-arithmetic configurations accessible to the holonomy method.

The originality comparison is limited by the possibility that an equivalent finite-index extension exists under different notation outside the sources and searches inspected here. No such statement was found.

## References

1. V. Oussa, *The critical mixed-arithmetic four-point HRT theorem*, arXiv:2609.27970v1, 2026.
2. V. Oussa, *Lean-certified four-point HRT results for three lattice points and one off-lattice point*, arXiv:2604.21228, 2026.
3. V. Oussa, *A Trichotomy and Rigidity Constraints for the HRT Conjecture in the Mixed-Integer Case*, arXiv:2508.04613v2, 2026 revision of the 2025 preprint.
