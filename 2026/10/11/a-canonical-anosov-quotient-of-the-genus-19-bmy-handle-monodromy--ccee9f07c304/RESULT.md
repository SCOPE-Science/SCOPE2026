# A canonical Anosov quotient of the genus-19 BMY handle monodromy
## Finding
Let \(A=QR^{-1}\in\operatorname{Mod}(\Sigma_{19})\) be the genus-\(19\) handle monodromy in Baykur--Stipsicz--Szabó, and let \(S=A_*\) on \(H_1(\Sigma_{19};\mathbb Q)\). Put
\[
K=\ker(S^2+I),\qquad L=K\cap H_1(\Sigma_{19};\mathbb Z).
\]
The source computes
\[
\det(tI-S)=(t^2+1)^2h(t)h^*(t),\qquad h^*(t)=t^{17}h(t^{-1}),
\]
where
\[
h(t)=t^{17}-2t^{16}+2t^{15}-2t^{14}+t^{13}+2t^{11}-t^{10}-2t^8+2t^7-t^6-t^5+3t^4+t^3-2t^2+1.
\]
It also proves that \(h\) is irreducible over \(\mathbb Q\), that \(K\) has dimension \(2\), and that \(L\) is an \(S\)-invariant isotropic lattice.

The canonical symplectic quotient
\[
\Lambda=L^\perp/L
\]
is a free rank-\(34\) lattice. The induced automorphism \(\bar S\) has characteristic polynomial \(h(t)h^*(t)\) and has no eigenvalue on the unit circle. Consequently \(\bar S\) defines an Anosov automorphism of the torus \(\Lambda\otimes\mathbb R/\Lambda\), with stable and unstable real dimensions \(17\) each.

The full \((t^2+1)\)-primary space
\[
G=\ker((S^2+I)^2)
\]
has dimension \(4\) and is the nonsplit \(\mathbb Q[t]\)-module
\[
G\cong \mathbb Q[t]/((t^2+1)^2).
\]
Thus the only unit-circle eigenvalues of \(S\) are \(i\) and \(-i\), each of algebraic multiplicity \(2\) and geometric multiplicity \(1\). The rational finite-orbit subspace is exactly \(K\). Since the two handle monodromies \(A\) and \(B=R^{-1}Q\) are conjugate, the same conclusions hold for \(B_*\).

## Assumptions and scope
The statement uses the explicit genus-\(19\) fibration and handle map \(A=QR^{-1}\) from arXiv:2610.02261v1. The homology is rational unless an integral lattice is explicitly named. Orthogonality is with respect to the algebraic intersection form on \(H_1(\Sigma_{19};\mathbb Z)\). The term Anosov refers to the induced linear torus automorphism on the rank-\(34\) quotient lattice; it is not a claim about a new surface diffeomorphism or about the stretch factor of the pseudo-Anosov mapping class.

## Proof
Write \(p(t)=t^2+1\). Appendix D.5 of the source gives the characteristic polynomial \(p(t)^2h(t)h^*(t)\), proves that \(h\) is irreducible over \(\mathbb Q\), and proves \(\dim K=2\) for \(K=\ker p(S)\). The printed coefficient list has \(h\ne h^*\). Since \(h\) is irreducible, monic, and has the same degree as \(h^*\), this implies \(\gcd(h,h^*)=1\).

There are no roots of \(h\) on the unit circle. Indeed, if \(h(\alpha)=0\) and \(|\alpha|=1\), then the coefficients of \(h\) are real, so \(h(\bar\alpha)=0\). On the unit circle \(\bar\alpha=\alpha^{-1}\), hence
\[
h^*(\alpha)=\alpha^{17}h(\alpha^{-1})=0.
\]
This would make \(h\) and \(h^*\) share an algebraic root, contradicting coprimality. The same argument applies to \(h^*\).

The source gives an integral basis for \(L=K\cap H_1(\Sigma_{19};\mathbb Z)\) and verifies that \(L\) is isotropic. Because \(K\) is a rational subspace, \(L\) is saturated, hence primitive. A primitive isotropic sublattice of a unimodular symplectic lattice extends to a symplectic basis, so \(L^\perp/L\) is free of rank \(38-2-2=34\) and inherits a nondegenerate integral symplectic form. Since \(S\) is symplectic and preserves \(L\), it preserves \(L^\perp\) and induces \(\bar S\) on \(\Lambda=L^\perp/L\).

The action on \(L\) has characteristic polynomial \(p(t)\). Symplectic duality identifies the action on \(H_1/L^\perp\) with the contragredient of the action on \(L\), whose characteristic polynomial is again \(p(t)\). Multiplicativity of characteristic polynomials in the two invariant short exact sequences therefore gives
\[
\chi_{\bar S}(t)=\frac{\chi_S(t)}{p(t)^2}=h(t)h^*(t).
\]
The preceding unit-circle argument makes \(\bar S\) hyperbolic. Because its characteristic polynomial is reciprocal of degree \(34\), roots off the unit circle occur in reciprocal pairs, so exactly \(17\) eigenvalues, counted with algebraic multiplicity, lie inside the unit circle and exactly \(17\) lie outside. The associated real stable and unstable subspaces therefore both have dimension \(17\). The integral hyperbolic automorphism of \(\Lambda\) induces an Anosov automorphism of \(\Lambda\otimes\mathbb R/\Lambda\).

Finally, coprimality of \(p\) and \(hh^*\) makes the \(p\)-primary subspace \(G=\ker p(S)^2\) four-dimensional. As a finite \(\mathbb Q[t]\)-module with characteristic polynomial \(p^2\), it is either \(\mathbb Q[t]/(p^2)\) or \(\mathbb Q[t]/(p)\oplus\mathbb Q[t]/(p)\). In the split case \(\ker p(S)\) would have dimension \(4\), contradicting the source computation \(\dim K=2\). Hence \(G\cong\mathbb Q[t]/(p^2)\). Over \(\mathbb C\), this is one size-two Jordan block at each of \(i\) and \(-i\). Every vector of \(K\) has period dividing \(4\), while the source proves that every rational finite-orbit vector lies in \(K\), so \(K\) is exactly the rational finite-orbit subspace.

## Verification
The bundled script `artifacts/verify_spectral_reduction.py` uses exact rational polynomial arithmetic. It checks the printed degree-\(17\) coefficient vector, verifies \(h\ne h^*\), verifies \(\gcd(h,h^*)=1\) and coprimality with \(t^2+1\), expands the full degree-\(38\) reciprocal characteristic polynomial, and checks the rank bookkeeping for the primary block and the quotient. Its successful output is:

`VERIFY_OK deg_h=17 gcd_h_hstar=1 gcd_h_cyclotomic=1 char_degree=38 reciprocal=true primary_dim=4 kernel_dim=2 quotient_rank=34 stable_dim=17 unstable_dim=17`

The code is a consistency certificate for the algebraic arithmetic. The universal claims about the source monodromy use the exact source premises and the symbolic proof above, not numerical root sampling.

## Relationship to prior work
Baykur--Stipsicz--Szabó compute the characteristic polynomial, irreducibility of \(h\), the two-dimensional finite-orbit kernel, and its integral isotropic lattice in Appendix D.5, using those facts to rule out reducibility of the handle maps. They do not state the canonical quotient \(L^\perp/L\), its hyperbolicity, the \(17+17\) stable/unstable split, or the nonsplit rational primary block.

Akhmedov--Yeung study the same Cartwright--Steger Albanese fibration from a different marked-monodromy direction. Their introduction explicitly says that their results do not determine the handle monodromies. Thus their spanning theorem for transported vanishing classes does not imply the present spectral reduction.

## Limitations
The result is conditional on the exact homology data in arXiv:2610.02261v1. It does not compute the pseudo-Anosov dilatation, identify a Markov partition, prove that the Cartwright--Steger fibration is diffeomorphic to the newly constructed total space, or claim that the degree-\(17\) factor itself has a prescribed count of roots inside and outside the unit circle. The Anosov statement concerns the canonical homological quotient torus only.

## References
1. R. İnanç Baykur, András I. Stipsicz, Zoltán Szabó, *Small Lefschetz fibrations on the BMY line*, arXiv:2610.02261v1, especially Theorem A and Appendix D.5; see also the ancillary `homology.json`.
2. Anar Akhmedov, Sai-Kee Yeung, *A monodromy relation for the Cartwright--Steger fibration*, arXiv:2610.01467v1.
