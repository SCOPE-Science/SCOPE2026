# Projective stabilizer of Kollár's characteristic-two cuspidal plane curves

## Finding
Let \(k=\overline{\mathbb F}_2\), let \(n\ge2\), and set \(q=2^n\). Consider the reduced, irreducible degree-\(q+2\) plane curve
\[
C_q:\quad Z^2Y^q=X^{q+2}+XZ^{q+1}\quad\subset\mathbb P^2_k.
\]
Its full *geometric projective stabilizer* is the cyclic group of odd order \(q+1\):
\[
\operatorname{Stab}_{\operatorname{PGL}_3(k)}(C_q)
=\bigl\{\operatorname{diag}(u^q,u,1):u^{q+1}=1\bigr\}
\cong\mathbb Z/(q+1)\mathbb Z.
\]
These matrices are understood up to projective scalars. In particular, no nontrivial translation of the affine normalization extends to a projective linear automorphism of the embedded curve.

## Assumptions and scope
All statements are over the algebraic closure \(k\) of the two-element field, for integer \(n\ge2\). The word *stabilizer* means the ordinary group of \(k\)-rational projective transformations preserving the embedded curve, not the possibly nonreduced projective-stabilizer group scheme. No claim is made about abstract automorphisms of the singular curve or of its normalization.

The affine chart \(Z=1\) has equation \(y^q=x^{q+2}+x\). It is smooth because the derivative of its defining polynomial with respect to \(x\) is \(1\). The affine parametrization
\[
\varphi:\mathbb A^1_k\longrightarrow C_q\cap\{Z=1\},\qquad t\longmapsto (t^q,t^{q+2}+t)
\]
is an isomorphism (Kollár, Lemma 2 and Example 3). The only point at infinity is \(P=[0:1:0]\). In the chart \(Y=1\), its local equation begins with \(z^2\); it is singular of multiplicity two and has the unique tangent line \(Z=0\). Consequently every projective transformation stabilizing \(C_q\) fixes \(P\) and preserves \(Z=0\).

## Proof
Fix \(g\in\operatorname{PGL}_3(k)\) with \(g(C_q)=C_q\). The distinguished singular point and its unique tangent are invariant. Thus the matrix of \(g\), after choosing a scalar with bottom-right entry one, has the form
\[
[X:Y:Z]\longmapsto[AX+CZ:DX+BY+EZ:Z]
\]
with \(A,B\in k^\times\) and \(C,D,E\in k\). Indeed, fixing \(P\) forces the middle column to have vanishing top and bottom entries; invariance of its tangent line forces the bottom-left entry to vanish. The matrix is invertible precisely when \(A B\ne0\).

Its restriction to the affine curve is an automorphism of \(\mathbb A^1_k\) under \(\varphi\); hence on the normalization parameter it is \(t\mapsto at+b\) with \(a\in k^\times\), \(b\in k\). The affine \(x\)-coordinate gives
\[
A t^q+C=(at+b)^q=a^qt^q+b^q,
\]
so \(A=a^q\) and \(C=b^q\). The affine \(y\)-coordinate gives the polynomial identity
\[
D t^q+B(t^{q+2}+t)+E=(at+b)^{q+2}+at+b.
\]
Because \(q\) is a power of two,
\[
(at+b)^{q+2}=a^{q+2}t^{q+2}+a^q b^2t^q+b^qa^2t^2+b^{q+2}.
\]
The five degrees \(q+2,q,2,1,0\) are pairwise distinct for \(q\ge4\). Comparing the coefficient of \(t^2\) yields \(b^qa^2=0\), so \(b=0\). Comparing the remaining coefficients gives \(C=D=E=0\), \(B=a^{q+2}\) from the highest degree, and \(B=a\) from degree one. Thus \(a^{q+1}=1\), proving necessity.

Conversely, if \(a^{q+1}=1\), then \(a^{q+2}=a\) and \(a^{q(q+2)}=a^q\). The substitution \((x,y)\mapsto(a^qx,ay)\) preserves \(y^q=x^{q+2}+x\) and thus the projective curve. Distinct values of \(a\) yield distinct projective transformations, and all \(q+1\) roots are simple since \(q+1\) is odd. They form the claimed cyclic group. This finishes the proof.

## Verification
The proof uses a formal coefficient comparison valid for every integer \(n\ge2\), not finite sampling. The accompanying `verify.py` independently expands the characteristic-two binomial power and checks its degree pattern for \(q=4,8,16,32,64\); run with `python3 verify.py`. It does not replace the universal polynomial-identity argument.

## Relationship to prior work
Kollár's 2026 construction establishes the family, its affine-line parametrization and its unique multiplicity-two cusp; these are credited as premises. The additional assertion here determines **all** projective linear symmetries of those specific plane embeddings, a different invariant from their singularity type or normalizations. The familiar affine automorphisms of a rational normalization do not automatically preserve a fixed plane embedding. Related results on stabilizers of other plane curves and on positive-characteristic Kummer coverings concern different equations and do not imply this exact classification.

## Limitations
The result holds for \(q=2^n\) with \(n\ge2\); the comparison of degrees \(q\) and \(2\) does not apply unchanged at \(q=2\). The projective stabilizer **group scheme** could have infinitesimal directions in characteristic two: this theorem classifies only its geometric points. It does not describe the full group of automorphisms of the abstract singular curve. Priority searches cannot rule out earlier unindexed or differently formulated computations.

## References
1. J. Kollár, *Planar, rational curves over \(\mathbb F_2\) whose only singularity is a double point*, arXiv:2603.04211, submitted 2026-03-04, Example 3 and Lemma 2; https://arxiv.org/abs/2603.04211.
2. Mathematical Sciences Classification 2020, code 14H37, automorphisms of curves; https://mathscinet.ams.org/msc/msc2020.html?t=14H37.
