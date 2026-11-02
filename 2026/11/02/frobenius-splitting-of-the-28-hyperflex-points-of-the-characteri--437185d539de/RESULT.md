# Frobenius splitting of the 28 hyperflex points of the characteristic-three Klein quartic

## Finding
For the smooth projective plane quartic \(C:x^3y+y^3z+z^3x=0\) over \(\mathbb F_3\), the reduced locus \(H\) of points at which the tangent has intersection multiplicity four has exactly \(28\) geometric points. The absolute arithmetic Frobenius \(\operatorname{Fr}_3\) has cycles \((1,3,6,6,6,6)\) on \(H(\overline{\mathbb F}_3)\). Thus
\[
Z(H/\mathbb F_3,T)=\frac1{(1-T)(1-T^3)(1-T^6)^4},\qquad
\#H(\mathbb F_{3^m})=1+3\mathbf1_{3\mid m}+24\mathbf1_{6\mid m}.
\]
The 28 geometric hyperflexes themselves, and the fact that every point is a flex, are classical; the finding is their explicit degree distribution for the displayed \(\mathbb F_3\)-equation.

## Assumptions and scope
Everything is in characteristic three, with \(m\) an arbitrary positive integer. "Hyperflex" means the tangent intersection multiplicity is \(4\), not merely \(3\). The scheme \(H\) is the **reduced** subscheme supported on these geometric points; no statement about the potentially nonreduced intrinsic jet-degeneracy scheme is made. The cubic and quartic expansions below take place over an algebraic closure. The field \(\mathbb F_{729}\) is \(\mathbb F_{3^6}\).

## Proof
The partial derivatives of \(F=x^3y+y^3z+z^3x\) are \((z^3,x^3,y^3)\), with no common projective zero, proving smoothness. At \(P=[a:b:c]\), put \(U=(u,v,w)\). Exactly in characteristic three,
\[
F(sP+tU)=s^4F(P)+s^3t(c^3u+a^3v+b^3w)+st^3(bu^3+cv^3+aw^3)+t^4F(U).
\]
Consequently all tangent lines are flex lines; contact is four precisely when the cubic term vanishes on the tangent plane \(c^3u+a^3v+b^3w=0\). Since the cubic term is a linear form in the independent cubes of \(u,v,w\), this is equivalent to
\[
[b:c:a]=[c^9:a^9:b^9],\quad\text{or}\quad[a^9:b^9:c^9]=[c:a:b].
\]
Scale homogeneous coordinates to make \(a^9=c,\ b^9=a,\ c^9=b\) hold literally: an eighth root of the projective proportionality factor exists in the algebraic closure. In particular \(a^{729}=a\), and \(a\ne0\); the solutions have the unique form \([a:a^{81}:a^9]\), with \(a\in\mathbb F_{729}^{\times}\) modulo the eight scalars \(\mathbb F_9^\times\).

Substitution into \(F\) gives
\[
F(a,a^{81},a^9)=a^{28}(1+a^{56}+a^{224}).
\]
Setting \(s=a^{56}\), we have \(s^{13}=1\), and the equation becomes \(1+s+s^4=0\). In \(\mathbb F_3[s]\), the polynomial \(s^4+s+1=(s-1)(s^3+s^2+s-1)\) divides \(s^{13}-1\) and is squarefree. Therefore precisely four thirteenth roots are admissible. Each has 56 lifts in \(\mathbb F_{729}^\times\), or exactly seven distinct projective classes modulo \(\mathbb F_9^\times\), giving \(28\) points.

Choose a generator \(g\) of the cyclic group \(\mathbb F_{729}^\times\). The 91 potential projective classes are indexed by \(k\in\mathbb Z/91\mathbb Z\) via \(a=g^k\). Arithmetic Frobenius sends \(k\) to \(3k\). Over the root \(s=1\) are exactly the seven indices divisible by \(13\): multiplication by three has cycles \((1,6)\). The remaining three roots form a degree-three Frobenius orbit; each contributes seven indices and, by the Chinese remainder theorem modulo \(7\cdot13\), the resulting 21 indices form one cycle of length three and three cycles of length six. This proves \((1,3,6,6,6,6)\), and the formulas follow from the standard finite-étale zeta-product identity.

## Verification
A standalone standard-library implementation in `verify.py` checks irreducibility of a degree-six defining polynomial, enumerates all 91 projective Frobenius-fixed candidates over \(\mathbb F_{729}\), selects exactly 28 on the quartic, checks the exact hyperflex tangent criterion for all 28, and computes their Frobenius orbit lengths \((1,3,6,6,6,6)\). The program's preserved output is `verify_output.txt`. The proof above independently establishes geometric completeness; it does not infer it from a bounded point scan.

## Relationship to prior work
The classical characteristic-three Klein quartic is projectively equivalent over the algebraic closure to the Hermitian/Fermat quartic. Hartshorne's funny-curve example and the characteristic-three discussions of Meagher–Top and Oyono–Ritzenthaler already cover its Frobenius-nonclassical tangent geometry and its special geometric bitangents. The geometric count of 28 hyperflexes is **not** asserted as new. The precise Frobenius splitting and degree-three/degree-six arithmetic of the reduced hyperflex locus for this particular \(\mathbb F_3\) model were not located in the inspected primary literature or the referenced mathematical-result search; this absence is not a priority proof.

## Limitations
The claim concerns the displayed plane model and its reduced hyperflex support, not all twists, intrinsic jet schemes, bitangent schemes with multiplicities, or stable reduction. A historical source not indexed in the searched material could contain equivalent arithmetic orbit data. There has been no independent human audit.

## References
Top, *Curves of genus 3 over small finite fields*, arXiv:math/0301264 (posted 2003-01-23). Meagher–Top, *Twists of genus three curves over finite fields*, Finite Fields Appl. 16 (2010), 347–368, DOI:10.1016/j.ffa.2010.06.001. Oyono–Ritzenthaler, *On Rationality of the Intersection Points of a Line with a Plane Quartic* (2010), DOI:10.1007/978-3-642-13797-6_16. Hartshorne, *Algebraic Geometry* (1977), IV.2.4.
