# The characteristic-five Clebsch cubic: a six-point conic resolution, full automorphism group and zeta function

## Finding

Let \(k\) be an algebraic closure of \(\mathbb F_5\), and define the integral-model special fibre
\[
X=\left\{[x_0:\cdots:x_4]\in\mathbb P^4_k:
\sum_{i=0}^4x_i=\sum_{i=0}^4x_i^3=0\right\}.
\]
The geometric automorphism group of this **singular** surface has exactly \(120\) elements:
\[
\operatorname{Aut}_k(X)=\mathfrak S_5
\cong \operatorname{PGL}_2(\mathbb F_5).
\]
Here the first isomorphism is the *entire* automorphism group, not just the evident subgroup of coordinate permutations. Every geometric automorphism is defined over \(\mathbb F_5\). Its faithful permutation action on the six lines through the unique singular point is the exceptional six-point action of \(\mathfrak S_5\), equivalently the natural action of \(\operatorname{PGL}_2(\mathbb F_5)\) on \(\mathbb P^1(\mathbb F_5)\).

More precisely, the minimal resolution of \(X\) is the blowup of \(\mathbb P^2_{\mathbb F_5}\) at **all six** \(\mathbb F_5\)-points of an explicit smooth conic. The strict transform of that conic is the unique contracted \((-2)\)-curve. Consequently, for every \(n\ge1\), with \(q=5^n\),
\[
\#X(\mathbb F_q)=q^2+6q+1,
\qquad
Z(X/\mathbb F_5,T)=\frac1{(1-T)(1-5T)^6(1-25T)}.
\]
The group-order, resolution and zeta statements form one classification of this bad-reduction fibre. The earlier identification of its singular point and its twenty-one geometric lines is not claimed as new.

## Assumptions and scope

All geometric assertions concern the scheme \(X\) **defined by the two displayed equations in characteristic five**, not a smooth cubic surface elsewhere. Automorphisms mean automorphisms of the projective \(k\)-scheme (geometric points of the automorphism functor); no claim about infinitesimal structure of that functor is necessary. A point count counts geometric projective points rational over each extension. The variable \(T\) is the formal zeta variable.

Write \(P=[1:1:1:1:1]\). In the four-dimensional vector space \(H=\{\sum_i x_i=0\}\) choose coordinates
\[
x=s(1,1,1,1,1)+(a,b,c,-a-b-c,0).
\]
Put
\[
Q(a,b,c)=a^2+b^2+c^2+(a+b+c)^2
=2(a^2+b^2+c^2+ab+ac+bc),
\]
\[
D(a,b,c)=-(a+b)(a+c)(b+c).
\]
The cubic equation is \(sQ+D=0\). Let
\[
B=V(Q,D)\subset\mathbb P^2_{\mathbb F_5}.
\]
We establish that \(B=V(Q)(\mathbb F_5)\) as a set of six reduced, rational points.

## Proof

**1. The unique node and projection.** In the hyperplane \(\sum_i x_i=0\), a singular point has \(x_i^2=x_j^2\) for all \(i,j\), by the Jacobian criterion and because \(3\) is invertible. Each coordinate is then either \(z\) or \(-z\). The sum of five signs can vanish in characteristic five only when all five signs agree. Therefore \(P\) is the unique singular point. The binomial expansion in the displayed coordinates gives
\[
\sum_i x_i^3=3sQ+3D.
\]
The conic \(Q=0\) is nonsingular: its symmetric matrix is \(I+J\), with determinant \(4\ne0\) in characteristic five. Thus in the chart \(s=1\), the tangent cone at \(P\) is a smooth quadric, so \(P\) is an ordinary double point of type \(A_1\). In particular, \(X\) is a normal irreducible cubic surface.

**2. All six blowup centres are rational.** The factorization \(D=-(a+b)(a+c)(b+c)\) shows that \(B\) is the intersection of the smooth conic with three lines. Its points, normalized by \(a=1\), are
\[
(1:2:3),\ (1:2:4),\ (1:3:2),\ (1:3:4),\ (1:4:2),\ (1:4:3).
\]
Direct substitution verifies all six, and none lies on two of the three lines. Bézout's theorem gives total intersection multiplicity six, so these are all the basepoints and each intersection is transverse; the base locus is reduced. Since a smooth conic with an \(\mathbb F_5\)-point has exactly six \(\mathbb F_5\)-points, \(B\) equals \(Q(\mathbb F_5)\).

**3. The global resolution.** Projection from \(P\) maps \(X\) birationally to the projective plane of directions \([a:b:c]\). An explicit inverse on \(Q\ne0\) is
\[
[a:b:c]\longmapsto
[Qa-D:Qb-D:Qc-D:-Q(a+b+c)-D:-D].
\]
Because \(B\) is the complete intersection of \(Q\) and \(D\), the degree-three part of its homogeneous ideal is precisely spanned by \(Qa,Qb,Qc,D\). Thus the displayed four independent cubic forms are the complete anticanonical system through the six simple basepoints. After blowing up \(B\), these sections are basepoint-free: locally at every centre the linear terms of \(Q\) and \(D\) are independent, so the blowup separates their ratio. For \(Y=\operatorname{Bl}_B\mathbb P^2\), the associated divisor is \(3H-\sum_{j=1}^6E_j=-K_Y\). The resulting anticanonical morphism \(Y\to X\) is birational and maps the strict transform \(\widetilde Q\) to \(P\). Since
\[
\widetilde Q\sim2H-\sum E_j,\qquad
\widetilde Q^2=4-6=-2,
\qquad (-K_Y)\cdot\widetilde Q=0,
\]
and projection is an isomorphism away from \(P\), this is the minimal resolution of the unique \(A_1\) singularity. In particular, all six exceptional divisors of the blowup map to distinct rational lines through \(P\).

**4. The upper bound on geometric automorphisms.** The cubic hypersurface \(X\subset\mathbb P^3\) is Gorenstein with dualizing sheaf \(\omega_X\simeq\mathcal O_X(-1)\). Consequently, every abstract automorphism acts on the complete four-dimensional anticanonical system \(H^0(X,\mathcal O_X(1))\), so extends to a projective transformation of its ambient \(\mathbb P^3\). Uniqueness of the node forces it to fix \(P\). Hence it induces a projectivity of the plane of directions preserving the set \(B\) of directions of the six node-lines.

The homomorphism from \(\operatorname{Aut}_k(X)\) to the projective stabilizer of \(B\) is injective. Indeed, an automorphism fixing every projective direction can, up to a common scalar, be written \(s\mapsto\alpha s+L(a,b,c)\), \((a,b,c)\mapsto(a,b,c)\), where \(L\) is linear. Preservation of the irreducible cubic \(sQ+D\), on comparing the coefficient of \(s\), forces its multiplier to be \(\alpha\). Comparison of the constant terms then yields
\[
(\alpha-1)D=LQ.
\]
Because \(Q\) is irreducible and does not divide \(D\), this forces \(\alpha=1\) and \(L=0\).

Any projectivity preserving the six-point set \(B\subset Q\) must preserve the conic \(Q\), because another conic through six distinct points on \(Q\) would meet it in more than four points unless identical. Thus the stabilizer embeds in \(\operatorname{Aut}(Q)\simeq\operatorname{PGL}_2(k)\). Under the rational identification \(Q\simeq\mathbb P^1\), it preserves \(\mathbb P^1(\mathbb F_5)\). An element of \(\operatorname{PGL}_2(k)\) carrying the set \(\mathbb P^1(\mathbb F_5)\) to itself must lie in \(\operatorname{PGL}_2(\mathbb F_5)\): its images of the ordered triple \((0,1,\infty)\) determine it uniquely, and the same triple can be matched by an element over \(\mathbb F_5\). Hence
\[
|\operatorname{Aut}_k(X)|\le |\operatorname{PGL}_2(\mathbb F_5)|=5(5^2-1)=120.
\]
The obvious permutations of five coordinates preserve \(X\) and give a faithful subgroup \(\mathfrak S_5\) of order \(120\) (faithfulness can be checked on the six displayed directions). Equality follows. Every element is represented by a coordinate permutation over \(\mathbb F_5\), proving the descent statement. The action on \(B\) is the faithful, degree-six action of \(\operatorname{PGL}_2(\mathbb F_5)\), equivalently the exceptional six-point action of \(\mathfrak S_5\).

**5. Exact extension-field point counts.** For \(q=5^n\), the six blowup centres are all \(\mathbb F_q\)-rational. Replacing each rational point of \(\mathbb P^2\) by \(\mathbb P^1\) adds \(q\) points, whence \(\#Y(\mathbb F_q)=q^2+7q+1\). The strict transform \(\widetilde Q\) is a split conic with \(q+1\) rational points, and its contraction replaces that entire fibre by the one rational node \(P\). Thus
\[
\#X(\mathbb F_q)=(q^2+7q+1)-(q+1)+1=q^2+6q+1.
\]
Applying the defining identity \(Z(T)=\exp(\sum_{n\ge1}\#X(\mathbb F_{5^n})T^n/n)\) yields the stated rational zeta function.

## Verification

Run `python3 verify_clebsch_aut.py` with Python 3; no external packages are needed. Its checked output ends with `CLEBSCH_CHAR5_BLOWUP_AUT_ZETA_PASS`. The checker verifies all six conic points and basepoints directly, certifies the \(120\) different six-point permutations arising from coordinate permutations, enumerates all rational projective lines over \(\mathbb F_5\), verifies the simple-node-line tangent-space distinction, and directly enumerates points over \(\mathbb F_5\) and \(\mathbb F_{25}\), obtaining \(56\) and \(776\). These finite computations check the explicit algebra and provide consistency witnesses; they do not substitute for the argument over arbitrary algebraically closed extensions or for the all-\(n\) point count.

## Relationship to prior work

Keneshlou [1] studies Clebsch and the Eckardt hypersurface, including the classical five-coordinate permutation action on the smooth Clebsch cubic. Dolgachev and Duncan [2, Remark 6.2 and Section 12] explicitly record that its characteristic-five model acquires the singular point \(P\), but their classification concerns **smooth** cubic surfaces and does not determine the full automorphism group of this singular special fibre. Vikulova [3, Proposition 1] independently records the bad-reduction singularity, likewise in a classification of smooth cubic automorphism groups. Earlier calculations of the six singular-point lines and their exceptional permutation action, and of the full line Hilbert scheme, are antecedents and are not asserted to be new here. The asserted addition is a complete **singular-fibre** automorphism classification together with its explicit rational six-point resolution and every-extension zeta function. Neither standard smooth-surface automorphism results nor the mere list of lines yields those conclusions without the geometric upper bound and resolution argument above.

## Limitations

The theorem pertains only to the explicit characteristic-five reduction of the displayed integral Clebsch equations. It does not classify other singular cubic surfaces, their automorphism schemes as nonreduced group schemes, or the integral geometry of the family. The literature comparison includes the relevant primary papers, but an equivalent treatment in classical or unindexed literature could affect historical priority. All assertions have been checked in a self-review only; no independent audit or independent validation has been performed.

## References

[1] Hanieh Keneshlou, *Cubic surfaces on the singular locus of the Eckardt hypersurface*, arXiv:1909.05554v1 (first submitted 12 September 2019), https://arxiv.org/abs/1909.05554 .

[2] Igor Dolgachev and Alexander Duncan, *Automorphisms of cubic surfaces in positive characteristic* (2019), especially Remark 6.2 and Section 12, https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/autocubic.pdf .

[3] Anastasia V. Vikulova, *The most symmetric smooth cubic surface*, arXiv:2407.09997v1 (13 July 2024), https://arxiv.org/abs/2407.09997 .
