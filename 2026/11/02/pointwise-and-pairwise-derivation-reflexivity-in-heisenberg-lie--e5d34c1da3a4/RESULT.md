# Pointwise and pairwise derivation reflexivity in Heisenberg Lie algebras

## Finding

Let \(k\) be any field and \(r\geq1\). On the Heisenberg Lie algebra \(H=V\oplus kz\), where \(\dim_k V=2r\) and \([v,w]=\omega(v,w)z\) for a nondegenerate alternating form \(\omega\), the spaces of **linear local derivations**, **linear two-local derivations**, and ordinary derivations admit complete, different descriptions.

Write a linear map preserving \(kz\) uniquely as
\[
\Delta(v+tz)=Av+(\phi(v)+ct)z,
\qquad A\in\operatorname{End}_k(V),\quad\phi\in V^*,\quad c\in k.
\]
Then:

1. \(\Delta\) is a local derivation if and only if it preserves \(kz\); equivalently, every \(A,\phi,c\) in this display is permitted.
2. \(\Delta\) is a **linear two-local derivation** if and only if it preserves \(kz\) and \(A\) is conformally symplectic: some \(\mu\in k\) satisfies
\[
\omega(Av,w)+\omega(v,Aw)=\mu\omega(v,w)\qquad(v,w\in V).
\]
Here the central scalar \(c\) is **unrestricted** and need not equal \(\mu\).
3. \(\Delta\) is an ordinary derivation if and only if it has the preceding form **and** \(c=\mu\).

The dimensions of these three linear spaces, in the same order, are
\[
4r^2+2r+1,\qquad 2r^2+3r+2,\qquad 2r^2+3r+1.
\]
Thus the pairwise-pointwise gap has dimension \(2r^2-r-1\) (zero at \(r=1\)), whereas the pairwise-to-ordinary gap has dimension exactly one in every rank. Over \(\mathbb F_q\), their numbers of maps are respectively \(q^{4r^2+2r+1}\), \(q^{2r^2+3r+2}\), and \(q^{2r^2+3r+1}\). All statements hold in characteristic two without exceptions.

## Assumptions and scope

A derivation is a \(k\)-linear map \(D:H\to H\) obeying \(D([x,y])=[D(x),y]+[x,D(y)]\). A **local derivation** is a \(k\)-linear map \(\Delta\) for which, for every \(x\in H\), there exists a (possibly \(x\)-dependent) derivation \(D_x\) such that \(D_x(x)=\Delta(x)\). A **linear two-local derivation** is a \(k\)-linear map \(\Delta\) for which, for every ordered pair \((x,y)\in H^2\), one derivation \(D_{x,y}\) simultaneously agrees with \(\Delta\) at \(x\) and \(y\). Arbitrary non-linear two-local maps are not classified here. The center is \(Z(H)=kz\); the bracket does not depend on field characteristic beyond the usual alternating Lie axiom.

## Proof

**1. Ordinary derivations.** A derivation stabilizes the center: \(0=D([z,x])=[D(z),x]\), hence \(D(z)=cz\). Write \(D(v)=Av+\phi(v)z\). Applying the derivation identity to \([v,w]=\omega(v,w)z\) gives exactly
\[
\omega(Av,w)+\omega(v,Aw)=c\omega(v,w).
\]
Conversely this identity ensures the derivation rule on all brackets, since all brackets are central. Thus the description in part 3 is necessary and sufficient. For fixed conformal multiplier \(\mu\), the solutions \(A\) form a translate of \(\mathfrak{sp}(V,\omega)\). With a symplectic basis, \(\dim\mathfrak{sp}(V,\omega)=r(2r+1)\); this holds also in characteristic two because matrices satisfy \(B^{\mathsf T}J+JB=0\), with \(JB\) symmetric. The multiplier is surjective (take \(B\) zero on a Lagrangian and scalar \(\mu\) on its complementary Lagrangian). Hence \(\dim\mathfrak{csp}(V,\omega)=r(2r+1)+1\).

**2. Pointwise matching.** Every local derivation stabilizes \(kz\), because it agrees there with some derivation. Conversely, suppose \(\Delta\) preserves \(kz\). For \(x=tz\) choose any ordinary derivation with multiplier \(c\). For \(x=v+tz\) with \(v\ne0\), we need a derivation \(D\) such that its quotient block \(B\) sends \(v\) to \(Av\), while its central functional can then be freely chosen to match \(\phi(v)+ct\). The evaluation map \(\mathfrak{sp}(V,\omega)\to V\), \(B\mapsto Bv\), is onto for every nonzero \(v\). Indeed the rank-one maps \(T_u(w)=\omega(u,w)u\) all belong to \(\mathfrak{sp}(V,\omega)\). Their evaluations \(\omega(u,v)u\) span \(V\): the set \(\{u:\omega(u,v)=1\}\) is an affine hyperplane not passing through zero, whose linear span is \(V\), also over \(\mathbb F_2\). Thus we can choose \(B\) with multiplier zero and \(Bv=Av\), then adjust the central functional. This proves part 1.

**3. Pairwise necessity.** Suppose \(\Delta\) is linear two-local. It is local, so preserves \(kz\). Define the alternating bilinear form
\[
\beta_A(v,w)=\omega(Av,w)+\omega(v,Aw).
\]
If \(\omega(v,w)=0\), pairwise matching at \(v,w\) supplies a derivation with quotient block \(B\) and multiplier \(\lambda\), so \(\beta_A(v,w)=\lambda\omega(v,w)=0\). We show that an alternating form \(\beta\) vanishing on all \(\omega\)-orthogonal pairs must be a scalar multiple of \(\omega\). Choose a symplectic basis \(e_i,f_i\). The vanishing kills \(\beta(e_i,e_j)\), \(\beta(f_i,f_j)\), and \(\beta(e_i,f_j)\) whenever \(i\ne j\). Write \(b_i=\beta(e_i,f_i)\). For distinct indices \(i,j\), the pair \(e_i+e_j\) and \(f_i-f_j\) is \(\omega\)-orthogonal; hence \(b_i-b_j=0\). When \(r=1\), there is only one coefficient. Therefore \(\beta=\mu\omega\) in every rank, including characteristic two, and \(A\in\mathfrak{csp}(V,\omega)\).

**4. Pairwise sufficiency.** Conversely, let \(A\in\mathfrak{csp}(V,\omega)\) have multiplier \(\mu\), with arbitrary \(c,\phi\). Take two elements \(x=v+tz\) and \(y=w+sz\). If \(v,w\) are independent, use an ordinary derivation with quotient block \(A\) and multiplier \(\mu\), and choose its central functional \(\psi\) so that
\[
\psi(v)=\phi(v)+(c-\mu)t,\qquad
\psi(w)=\phi(w)+(c-\mu)s.
\]
Then this derivation matches \(\Delta\) on both elements. If \(v,w\) span a line, we instead obtain an ordinary derivation with multiplier \(c\) whose quotient block \(B\) agrees with \(A\) on their span. To see this, fix a generator \(u\ne0\) and choose a symplectic basis with \(e_1=u\). There is a conformally symplectic map \(C\) with multiplier \(c-\mu\) and \(Cu=0\): set \(Ce_i=0\) and \(Cf_i=(c-\mu)f_i\). Then \(B=A+C\) has the required properties. Take central functional \(\psi=\phi\), which matches both values. If both quotient vectors vanish, any conformally symplectic block of multiplier \(c\) works. Thus \(\Delta\) is two-local.

**5. Dimension and sharp distinctions.** Center-preserving maps have \((2r)^2+2r+1\) freely chosen scalar coordinates. Two-local maps have \(r(2r+1)+1\) quotient-block coordinates, plus \(2r\) central-functional coordinates and one independent central scalar. Derivations impose one scalar equation \(c=\mu\). This gives every dimension and finite-field count. The map \(\Delta(v+tz)=tz\) is linear two-local but is never a derivation. For \(r\ge2\), the map whose quotient sends \(e_2\mapsto e_1\) and annihilates the other symplectic basis vectors (and \(z\mapsto0\)) is local but not two-local, since its \(\beta_A(e_2,f_1)\ne0\) while \(\omega(e_2,f_1)=0\). All required maps are genuinely linear.

## Verification

The standalone standard-library script `verify.py` builds the ordinary derivation space directly from the bracket structure constants and tests pointwise/pairwise solvability using finite-field linear algebra. It exhaustively tests all \(512\) endomorphisms and all ordered point pairs of \(H_3(\mathbb F_2)\); checks \(80\) seeded maps against all pairs in \(H_3(\mathbb F_3)\); and evaluates \(28\) maps against all \(32^2\) pairs in \(H_5(\mathbb F_2)\), including ten constructed conformally symplectic maps. Its marker is `HEISENBERG_LINEAR_LOCAL_2LOCAL_OK`. Those finite checks support but do not replace the arbitrary-field proof above.

## Relationship to prior work

Ayupov and Kudaybergenov (2015 preprint) develop local derivations on finite-dimensional Lie algebras and exhibit local non-derivations among nilpotent cases, including a three-dimensional Heisenberg example. Those existence and low-rank observations are not new here. Ayupov, Kudaybergenov and Rakhimov (2015) prove existence of non-derivation two-local maps on nilpotent Lie algebras; their construction concerns unrestricted, generally nonlinear two-local maps. Hao and Chen (2025) compute local derivations of various low-dimensional nilpotent Lie algebras. The presently isolated claim is the complete **linear** pointwise-versus-pairwise reflexivity filtration for every Heisenberg rank over arbitrary fields, with its one-dimensional final defect and exact finite-field counts. The theorem is not a claim to classify nonlinear two-local maps. Publication-priority verification is not exhaustive.

## Limitations

This result applies to the standard Heisenberg Lie algebra with one-dimensional center, not arbitrary two-step nilpotent Lie algebras with larger center. Its two-local classification requires that the map itself be linear; arbitrary nonlinear two-local maps can behave differently. Published historical coverage beyond the inspected papers cannot be excluded; the mathematical proof has not undergone independent external validation.

## References

1. S. Ayupov and K. Kudaybergenov, *Local derivations on finite-dimensional Lie algebras*, arXiv:1508.03939v1, posted 2015-08-17, https://arxiv.org/abs/1508.03939.
2. S. Ayupov, K. Kudaybergenov and I. Rakhimov, *2-Local derivations on finite-dimensional Lie algebras*, Linear Algebra Appl. 474 (2015), 1–11, doi:10.1016/j.laa.2015.01.016.
3. Z. Hao and L. Chen, *A computational approach to local derivations and almost inner derivations*, publicly available 2025 preprint, doi:10.13140/RG.2.2.22944.44809.
4. Z. Hao and L. Chen, *Local derivations is a Lie algebra*, arXiv:2609.09198v1 (2026), for context on reflexive hulls; outside the historical cutoff of the first reference.
