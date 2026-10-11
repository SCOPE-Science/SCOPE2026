# Balanced Grassmannians defeat the proposed Kähler diameter equality rigidity

## Finding

Let \(k\ge2\) and \(N\ge2k\) be integers. Consider the complex Grassmannian
\[
G_{k,N}=\operatorname{Gr}_{\mathbb C}(k,N)
\]
with its standard Kähler metric \(g_0\) pulled back from projective space by the Plücker embedding. We normalize the Fubini–Study metric so that on \(\mathbb{CP}^{1}\) its diameter is \(\pi/2\).

The Einstein-normalized metric is
\[
g=2N g_0.
\]
It satisfies
\[
\operatorname{Ric}_g=g,\qquad m:=\dim_{\mathbb C}G_{k,N}=k(N-k),
\]
and its intrinsic Riemannian diameter is
\[
\boxed{\operatorname{diam}(G_{k,N},g)=\pi\sqrt{Nk/2}.}
\]
Consequently,
\[
\boxed{\pi^2m-\operatorname{diam}(G_{k,N},g)^2
=\frac{\pi^2k}{2}(N-2k).}
\]
Thus this family attains the proposed Kähler diameter bound precisely when \(N=2k\).

For every \(k\ge2\), the balanced Grassmannian \(G_{k,2k}\) satisfies
\[
\operatorname{Ric}_g=g,
\qquad
\operatorname{diam}(G_{k,2k},g)=\pi k=\pi\sqrt{\dim_{\mathbb C}G_{k,2k}},
\]
but it is **not** biholomorphically isometric to \((\mathbb{CP}^{1})^{k^2}\). Indeed,
\[
b_2(G_{k,2k})=1,
\qquad
b_2((\mathbb{CP}^{1})^{k^2})=k^2>1.
\]
The first counterexample in this family is the irreducible Hermitian symmetric space
\[
\boxed{G_{2,4}=\operatorname{Gr}_{\mathbb C}(2,4),\quad m=4,\quad\operatorname{diam}_g=2\pi.}
\]
This **disproves the uniqueness-of-equality clause**, but **does not contradict the conjectured universal upper bound**, of the recent Kähler diameter conjecture of Chakraborty, Wang, and Wu.

## Assumptions and scope

The complex Grassmannian consists of the complex \(k\)-planes in \(\mathbb C^N\) with the standard Hermitian inner product. It is smooth, compact, connected and Kähler. The metric \(g_0\) is **intrinsic** to the Grassmannian: it is the Riemannian metric induced infinitesimally by the Plücker embedding, and its distances are lengths of curves *within* the Grassmannian. The ambient projective-space distance between Plücker points is generally smaller and must not be substituted into the diameter calculation.

The Riemannian Ricci convention is the one in which the ordinary round \(2\)-sphere of radius \(1\) has \(\operatorname{Ric}=g\). The scaled Plücker metric is chosen to satisfy this same Einstein condition. The conjecture in the motivating paper applies to all closed Kähler manifolds of complex dimension at least \(2\) with \(\operatorname{Ric}\ge g\).

The displayed family formula is proved for \(k\ge2\), \(N\ge2k\). Complementation gives analogous formulas when \(N<2k\), but those cases are not needed or claimed. No global sharp bound for all Kähler manifolds is proved or disproved.

## Proof

**1. Metric and Ricci normalization.** In a Grassmann graph chart, write a nearby plane as the graph of a complex matrix
\[
Z\in\mathbb C^{(N-k)\times k}.
\]
The Plücker Fubini–Study Kähler potential is
\[
\Phi(Z)=\log\det(I_k+Z^\ast Z).
\]
Put
\[
S=I_k+Z^\ast Z,\qquad T=I_{N-k}+ZZ^\ast.
\]
The associated Hermitian squared-length tensor is
\[
h_Z(H,H)=\operatorname{tr}(S^{-1}H^\ast T^{-1}H),
\quad H\in\mathbb C^{(N-k)\times k}.
\]
In particular, at \(Z=0\) its real metric is
\[
g_0(H,H)=\operatorname{tr}(H^\ast H).
\]
This is exactly the canonical Grassmann metric normalization used in the principal-angle distance theorem of Chen, Deng, and Zhang. Both metrics are \(U(N)\)-invariant, so this identification holds globally.

The determinant of the Hermitian metric matrix in these \(k(N-k)\) complex coordinates satisfies
\[
\det h_Z=(\det S)^{-(N-k)}(\det T)^{-k}=(\det S)^{-N},
\]
using the matrix determinant identity \(\det(I+ZZ^\ast)=\det(I+Z^\ast Z)\). With
\[
\omega_0=\frac{i}{2}\,\partial\bar\partial\Phi,
\]
the Ricci form is
\[
\rho_0=-i\partial\bar\partial\log\det h_Z
=iN\partial\bar\partial\Phi
=2N\omega_0.
\]
Hence
\[
\operatorname{Ric}_{g_0}=2N g_0.
\]
Constant rescaling preserves the Ricci tensor as a covariant \(2\)-tensor, so for \(g=2N g_0\),
\[
\operatorname{Ric}_g=\operatorname{Ric}_{g_0}=2N g_0=g.
\]

**2. Intrinsic diameter.** Let \(U,V\) be \(k\)-planes. Their principal angles \(\theta_1,\ldots,\theta_k\) are defined by the singular values \(\cos\theta_j\) of the restricted orthogonal projection between their unitary frames; each belongs to \([0,\pi/2]\). In the trace metric identified above, the *intrinsic* Grassmann geodesic formula is
\[
d_{g_0}(U,V)^2=\sum_{j=1}^k\theta_j^2.
\]
For clarity, the minimizing path rotates independent orthogonal principal-vector pairs by \(t\theta_j\) and has constant speed \((\sum_j\theta_j^2)^{1/2}\). The matching lower bound for arbitrary paths follows by choosing horizontal orthonormal frames and applying the sphere-distance bound to each frame vector, followed by the vector integral triangle inequality; this is the full argument in Lemma 3.2 of Chen, Deng, and Zhang.

Since every \(\theta_j\le\pi/2\),
\[
\operatorname{diam}(G_{k,N},g_0)\le\frac\pi2\sqrt{k}.
\]
When \(N\ge2k\), two orthogonal complex \(k\)-planes exist, and all their principal angles are \(\pi/2\). They realize equality, proving
\[
\operatorname{diam}(G_{k,N},g_0)=\frac\pi2\sqrt{k}.
\]
Rescaling by \(2N\) multiplies distances by \(\sqrt{2N}\), hence
\[
\operatorname{diam}(G_{k,N},g)
=\sqrt{2N}\frac\pi2\sqrt{k}
=\pi\sqrt{Nk/2}.
\]

**3. Comparison and non-productness.** The standard complex dimension is
\[
m=k(N-k).
\]
Subtracting squares gives the claimed nonnegative gap
\[
\pi^2m-\operatorname{diam}_g^2
=\pi^2k(N-k)-\frac{\pi^2Nk}{2}
=\frac{\pi^2k}{2}(N-2k),
\]
which vanishes exactly at \(N=2k\).

A complex Grassmannian has a Schubert cell decomposition with exactly one complex codimension-one Schubert cell. Consequently, its second Betti number is \(1\). In contrast, the Künneth formula gives
\[
b_2((\mathbb{CP}^{1})^{k^2})=k^2.
\]
For \(k\ge2\), these values differ; hence the balanced Grassmannian cannot be biholomorphic (or even homeomorphic) to the proposed product equality model. This completes the counterexample to the equality-only-if-product statement.

## Verification

The bundled \(\texttt{verify.py}\) carries out exact symbolic checks of the two central normalizations. It constructs a nontrivial \(2\)-by-\(2\) Grassmann graph chart and verifies
\[
\det h=(\det S)^{-N},
\]
which yields the Einstein factor \(2N\). It checks algebraically for an exact range of integer parameter pairs that the diameter-square gap is
\[
\frac{\pi^2k}{2}(N-2k),
\]
and that equality occurs in this family exactly at \(N=2k\). It also verifies the projective-space \(k=1\) normalization and the explicit \(G_{2,4}\) diameter \(2\pi\).

These finite symbolic checks are not used to prove the arbitrary-parameter theorem. The global intrinsic distance formula is supplied by its cited full proof, and the Ricci and dimension identities are proved symbolically in the graph chart above.

## Relationship to prior work

Chakraborty, Wang, and Wu conjecture that \(\operatorname{Ric}\ge g\) on a closed Kähler manifold of complex dimension \(m\ge2\) implies \(\operatorname{diam}\le\pi\sqrt m\), with equality **only** for the product \((\mathbb{CP}^{1})^m\) with factorwise Einstein normalization. Their examples discuss projective space and products of projective lines; their inspected full paper does not test this rigidity against higher-rank Grassmannians.

Chen, Deng, and Zhang independently establish, for the canonical Grassmann trace metric, the principal-angle distance formula and exact unscaled diameter \(\pi\sqrt{k}/2\) when \(N\ge2k\). Their 2026 symmetric-space diameter-gap paper concerns **isometric quotient diameters** and does not analyze the Ricci-normalized Grassmannians as equality cases of the Chakraborty–Wang–Wu conjecture. The present result supplies the Ricci normalization and exact comparison to \(\pi\sqrt m\), identifying an entire irreducible non-product equality family.

Chu, Lee, and Zhu study a different diameter-rigidity problem with a **lower bound on holomorphic sectional curvature** rather than merely \(\operatorname{Ric}\ge g\); their results and reducible examples do not establish the equality-rigidity assertion under the present hypotheses.

The individual geometric ingredients about Grassmannians are classical. The new point is their direct implication for the recently stated Kähler diameter equality conjecture: the prescribed product is **not** its unique equality geometry, even within irreducible homogeneous Kähler–Einstein spaces.

## Limitations

This counterexample concerns **only** the conjectured characterization of equality. The family computed here **satisfies** the proposed universal upper inequality, so its validity for arbitrary closed Kähler manifolds remains open on the evidence in this result.

The proof does not classify all possible equality manifolds or provide an optimal replacement for the conjecture. It does not infer rigidity of nonhomogeneous metrics from the homogeneous examples. Its use of the intrinsic Grassmannian metric is essential: the ambient projective distance between Plücker images is not the relevant Riemannian diameter.

## References

1. Sayantan Chakraborty, Xiaodong Wang, and Tian Wu, *Spectral Improvements of Geometric Inequalities on Closed Kähler Manifolds*, arXiv:2609.03287v1, first submitted 3 September 2026 (diameter conjecture in the introduction).
2. Zhiqi Chen, Shaoqiang Deng, and Hui Zhang, *A diameter gap for irreducible compact symmetric spaces of fixed rank*, arXiv:2609.21535v1, first submitted 18 September 2026 (Lemmas 3.2 and 3.4, full intrinsic metric-distance proof).
3. Jianchun Chu, Man-Chun Lee, and Jintian Zhu, *On diameter rigidity for Kähler manifolds with positive holomorphic sectional curvature*, Mathematische Zeitschrift 314 (2026), article 18, DOI:10.1007/s00209-026-04132-2.
