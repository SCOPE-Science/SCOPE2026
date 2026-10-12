# Biquadratic Galois action on the generic five-node Howe sextic, with an explicit prime-density specialization

## Finding
Let \(a,b,c,d,e\) be algebraically independent over \(\mathbb Q\), and set \(K=\mathbb Q(a,b,c,d,e)\). The Moriya--Kudo sextic \(\widetilde C\) in the five-node locus has one \(K\)-rational central node and four other nodes forming a single **regular** Galois orbit for \(C_2\times C_2\). Their common minimal defining field is biquadratic over \(K\).

For the explicit Howe-type tuple \((a,b,c,d,e)=(2,3,4,5,6)\), the complete geometric singular locus is
\[
\bigl\{[0:0:1]\bigr\}\ \cup\ 
\left\{\left[\epsilon\frac{\sqrt{385}}{140}:\delta\frac{\sqrt{14}}{28}:1\right]:\epsilon,\delta\in\{+1,-1\}\right\}.
\]
These are **five ordinary nodes**; the minimal common field is \(L=\mathbb Q(\sqrt{385},\sqrt{14})\), with \(\operatorname{Gal}(L/\mathbb Q)\cong C_2\times C_2\). For all but finitely many primes \(p\), the reduction of this particular curve has precisely \(1\) or \(5\) singular points rational over \(\mathbb F_p\). There are five if and only if both Legendre symbols \((385/p)\) and \((14/p)\) equal \(+1\), and otherwise there is one. Their respective natural densities are \(1/4\) and \(3/4\).

## Assumptions and scope
Work in characteristic zero for the generic and specialized field-of-definition statements. The parameters \(a,b,c,d,e\) are pairwise distinct and avoid \(0,1\). Write
\[
\phi(x)=x(x-1)(x-a),\quad Q_1(x)=(x-b)(x-c),\quad Q_2(x)=(x-d)(x-e),
\]
and define
\[
G(u,v)=\operatorname{Res}_x\bigl(\phi(x)u-Q_1(x),\,\phi(x)v-Q_2(x)\bigr),
\qquad f(Y,Z)=G(Y^2,Z^2).
\]
Homogenize \(f\) to degree six in \([Y:Z:W]\). This is the plane model in Moriya--Kudo [1, §3.2]. Their Proposition 4.2.6 establishes that for generic Howe-type parameters it has exactly five geometric double points: the origin and four points with independent sign choices for nonzero coordinates. The theorem here determines the **arithmetic Galois action**, not the already published geometric singularity count.

The prime-density statement concerns singular points defined over \(\mathbb F_p\), not smoothness of the full reduced curve and not the number of \(\mathbb F_p\)-points of the curve itself. It is asserted only outside a finite set of bad reduction primes.

## Proof
**1. A rational squared-coordinate pair.** The defining polynomial belongs to \(K[Y^2,Z^2]\) and is invariant under each independent sign change \(Y\mapsto-Y\), \(Z\mapsto-Z\). On the generic five-node locus, the source's complete geometric classification says the four noncentral nodes are \((\pm y,\pm z)\) with \(yz\ne0\). Since their squared-coordinate pair \((u_*,v_*)=(y^2,z^2)\) is unique, every element of \(\operatorname{Gal}(\overline K/K)\) fixes it; consequently \(u_*,v_*\in K^\times\). The field defining all four points is exactly \(K(\sqrt{u_*},\sqrt{v_*})\), so its Galois group embeds in the sign group \(C_2\times C_2\).

**2. An exact specialization to test independence.** Put \((a,b,c,d,e)=(2,3,4,5,6)\). The resultant is exactly
\[
\begin{aligned}
G(u,v)=-12\bigl(&600u^3-520u^2v-50u^2+142uv^2+33uv+u\\
&-12v^3+13v^2-v\bigr).
\end{aligned}
\]
Over \(\mathbb Q\), the reduced critical-point ideal \((G,G_u,G_v)\) has reduced Gröbner basis
\[
\bigl\{560u-11,\ 56v-1\bigr\},
\]
up to nonzero rational multiples. Thus its sole complex critical point is
\[
(u_*,v_*)=\left(\frac{11}{560},\frac1{56}\right).
\]
The Hessian determinant of \(G\) at this pair is \(-253584\ne0\); the corresponding four points of \(f(Y,Z)=G(Y^2,Z^2)\) have nondegenerate quadratic terms. At the origin, the lowest homogeneous part of \(f\) is \(-12(Y^2-Z^2)\), likewise an ordinary node. We have therefore exhibited five distinct nodes. The established geometric upper bound of five for these Howe sextics [1, §4.2] excludes further geometric singularities, including points at infinity.

Because
\[
\frac{11}{560}=\left(\frac{\sqrt{385}}{140}\right)^2,
\qquad \frac1{56}=\left(\frac{\sqrt{14}}{28}\right)^2,
\]
the four noncentral nodes have the announced coordinates. The squarefree integers \(385=5\cdot7\cdot11\) and \(14=2\cdot7\) represent independent square classes in \(\mathbb Q^\times/(\mathbb Q^\times)^2\). Their compositum has degree four, and both square-root sign automorphisms act freely on the four nodes. A noncentral node has the full degree-four residue field, not merely a quadratic field.

**3. Full generic arithmetic Galois group.** The unique nonzero squared-coordinate pair on the generic locus is a rational-function pair \((u_*,v_*)\). Near the rational tuple in Step 2, the equations \(G=G_u=G_v=0\), together with the nonzero Hessian, give a regular local branch of this unique squared-node pair. Thus \(u_*,v_*\) are units in the normal local parameter ring at the specialization. If any of \(u_*\), \(v_*\), or \(u_*v_*\) were a square in \(K\), its square root would be integral over that normal local ring, hence belong to it, and specialization would make one of \(11/560\), \(1/56\), or \(11/31360\) a square in \(\mathbb Q\). This contradicts independence of the specialized square classes. Thus the generic square classes \([u_*],[v_*]\) are independent and \([K(\sqrt{u_*},\sqrt{v_*}):K]=4\), proving a regular four-node \(C_2\times C_2\) action. (The conclusion is over \(\mathbb Q(a,b,c,d,e)\), **not** an assertion of geometric monodromy after adjoining all algebraic constants.)

**4. Reduction modulo primes.** The five ordinary nodes are distinct over \(\overline{\mathbb Q}\) and form a finite reduced singularity scheme. For all but finitely many rational primes, clearing denominators and reducing preserves this scheme and the absence of additional geometric singularities: the relative projective singular locus is finite étale of degree five on a suitable open subset of \(\operatorname{Spec}\mathbb Z\). The central node always reduces to a rational point, while the other four reduce to rational points exactly when both square roots exist in \(\mathbb F_p\); otherwise none of their sign-coordinate pairs is rational. Their rational count is therefore \(5\) or \(1\). The independent quadratic characters of \(385\) and \(14\) cut out the biquadratic extension \(L\); the four Frobenius classes are equidistributed by Chebotarev. The identity class (both symbols \(+1\)) has density \(1/4\), with all other classes totaling \(3/4\).

## Verification
The supplied `verify_howe_nodes.py` uses exact SymPy rational polynomial arithmetic: it reconstructs the source resultant from the five integer parameters, checks the reduced critical-point ideal, verifies the Hessian and four square-coordinate identities, and checks the square-class factorizations. It also independently enumerates all projective \(\mathbb F_p\)-rational singular points for 18 representative odd primes between \(13\) and \(83\), obtaining the predicted counts. These finite-field tests are consistency checks **only**; the infinite-prime density comes from the proven biquadratic field and Chebotarev, not enumeration.

To reproduce: install the pinned dependency from `requirements.txt`, then run `python verify_howe_nodes.py` with Python 3. The generic argument and good-reduction reasoning are given above; the verifier certifies the specialization arithmetic, not infinitely many primes.

## Relationship to prior work
Moriya and Kudo [1] introduced this explicit genus-five Howe plane sextic and proved its geometric singularity classification, including the generic five-node sign quartet. That geometric result is used, not claimed as new. Their follow-up [2] treats the different \((g_1,g_2,r)=(1,1,0)\) presentation and repeats the former model as background. Kudo and Harashita [3] give broader methods for genus-five plane sextic models. The new statement identifies the arithmetic splitting field and regular Galois action on the nodes, proves that the generic sign quartet has genuinely independent square classes, and derives an explicit rational specialization's full prime-density distribution. A general full-symmetric geometric monodromy theorem for an unrestricted Severi family would not imply this smaller sign-preserving arithmetic Galois action on the restricted Howe family.

## Limitations
The theorem does not classify arithmetic fields for all nongeneric three-double-point members or all rational specializations. The generic Galois assertion concerns the rational function field, not the complex geometric monodromy group. The exceptional bad primes are not enumerated exhaustively. A targeted literature comparison found no explicit equivalent arithmetic-node theorem, but older unindexed computations may exist. No classification of all bad reduction primes or all nongeneric specializations is asserted.

## References
[1] T. Moriya and M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, I*, arXiv:2310.15993v1, first public 2023-10-24; especially §3.2 and Proposition 4.2.6. https://arxiv.org/html/2310.15993v1

[2] T. Moriya and M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, II*, arXiv:2401.00760v1, 2024; especially §2.2. https://arxiv.org/html/2401.00760v1

[3] M. Kudo and S. Harashita, *Superspecial curves of genus 5: a possible approach by plane sextics*, arXiv:2102.07270v1 (2021), for the general plane-sextic framework. https://arxiv.org/abs/2102.07270
