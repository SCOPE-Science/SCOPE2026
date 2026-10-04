# Center-preserving order automorphisms of matrix partial isometries have Möbius boundary dynamics
## Finding
Let \(n\ge3\). Jia and Ji associate to every \(A\in M_n(\mathbb C)\) such that
\[
I-(A+A^*)
\]
is positive or negative invertible a normalized order automorphism \(\Psi_A\) of the partial isometries, with \(\Psi_A(I)=I\).

The scalar unitary circle is preserved by \(\Psi_A\),
\[
\Psi_A(\mathbb T I)=\mathbb T I,
\]
if and only if
\[
A=\alpha I
\]
for a scalar \(\alpha\) satisfying
\[
\delta=1-2\operatorname{Re}\alpha\ne0.
\]
In fact, it is enough that two distinct points \(a,b\in\mathbb T\setminus\{1\}\) have scalar images.

For \(A=\alpha I\), the induced map on the scalar circle is
\[
u_\alpha(a)=
\frac{a(1-\overline\alpha)-\alpha}
{1-\alpha-a\overline\alpha}.
\]
If \(\delta>0\), put
\[
c=\frac{\alpha}{1-\overline\alpha}\in\mathbb D.
\]
Then
\[
u_\alpha(a)=
\frac{1-\overline\alpha}{1-\alpha}
\frac{a-c}{1-\overline c\,a},
\]
so the scalar-circle action is the boundary action of a Möbius automorphism of the unit disk fixing \(1\).

If \(\delta<0\), put
\[
d=\frac{1-\overline\alpha}{\alpha}\in\mathbb D.
\]
Then, for \(a\in\mathbb T\),
\[
u_\alpha(a)=
\frac{\alpha}{\overline\alpha}
\frac{\overline a-d}{1-\overline d\,\overline a},
\]
so the action is anti-Möbius and fixes \(1\).

Conversely, every Möbius or anti-Möbius automorphism of the unit disk fixing \(1\) occurs uniquely as this scalar-circle restriction. Thus the center-preserving part of the new order-automorphism family has a complete one-complex-parameter boundary model.

## Assumptions and scope
Here
\[
\operatorname{PI}(M_n(\mathbb C))
\]
is the set of partial isometries with the star order, and
\[
\mathbb T I=\{aI:|a|=1\}
\]
is the center of the unitary group inside that set. The result concerns the normalized Jia--Ji family \(\Psi_A\), not an arbitrary factorization \(\Delta_{CD}\circ\Psi_A\).

The source gives, for every \(a\in\mathbb T\),
\[
\Psi_A(aI)=U_a,\qquad
U_a=(a-1)(I-A-aA^*)^{-1}+I.
\]
It also proves that \(I-A-aA^*\) is invertible for every \(a\in\mathbb T\).

## Proof
Suppose first that \(a\in\mathbb T\setminus\{1\}\) and \(U_a=u_aI\) is scalar. Since
\[
U_a-I=(a-1)(I-A-aA^*)^{-1},
\]
the matrix \(U_a-I\) is invertible, so \(u_a\ne1\). Inverting the displayed identity gives
\[
I-A-aA^*=\frac{a-1}{u_a-1}I.
\]
Hence there is a scalar \(\gamma_a\) such that
\[
A+aA^*=\gamma_a I.
\]
If the same holds for a distinct \(b\in\mathbb T\setminus\{1\}\), then subtraction gives
\[
(a-b)A^*=(\gamma_a-\gamma_b)I.
\]
Because \(a\ne b\), \(A^*\), and therefore \(A\), is scalar. This proves the two-point rigidity implication.

Conversely, let \(A=\alpha I\). The admissibility condition becomes
\[
I-(A+A^*)=\delta I,\qquad
\delta=1-\alpha-\overline\alpha\ne0.
\]
Substitution into the source formula yields
\[
u_\alpha(a)=
1+\frac{a-1}{1-\alpha-a\overline\alpha}
=
\frac{a(1-\overline\alpha)-\alpha}
{1-\alpha-a\overline\alpha},
\]
so every scalar unitary has a scalar unitary image.

Assume \(\delta>0\). Since
\[
|1-\alpha|^2-|\alpha|^2=\delta>0,
\]
the number
\[
c=\frac{\alpha}{1-\overline\alpha}
\]
lies in \(\mathbb D\). Factoring numerator and denominator gives
\[
u_\alpha(a)=
\frac{1-\overline\alpha}{1-\alpha}
\frac{a-c}{1-\overline c\,a}.
\]
The unimodular prefactor is exactly the one making the disk automorphism fix \(1\).

Conversely, every holomorphic disk automorphism fixing \(1\) has the unique form
\[
m_c(z)=
\frac{1-\overline c}{1-c}
\frac{z-c}{1-\overline c\,z},
\qquad c\in\mathbb D.
\]
Given \(c\), set
\[
\alpha=\frac{c(1-\overline c)}{1-|c|^2}.
\]
Then
\[
1-2\operatorname{Re}\alpha=
\frac{|1-c|^2}{1-|c|^2}>0
\]
and \(c=\alpha/(1-\overline\alpha)\), so \(m_c=u_\alpha\).

Now assume \(\delta<0\). Then \(\alpha\ne0\), and
\[
|1-\alpha|^2-|\alpha|^2=\delta<0
\]
shows that
\[
d=\frac{1-\overline\alpha}{\alpha}
\]
belongs to \(\mathbb D\). Since \(\overline a=a^{-1}\) on \(\mathbb T\), multiplying numerator and denominator of \(u_\alpha(a)\) by \(\overline a\) gives
\[
u_\alpha(a)=
\frac{\alpha}{\overline\alpha}
\frac{\overline a-d}{1-\overline d\,\overline a}.
\]
Conversely, every anti-Möbius disk automorphism fixing \(1\) has the unique form
\[
\widetilde m_d(z)=
\frac{1-\overline d}{1-d}
\frac{\overline z-d}{1-\overline d\,\overline z},
\qquad d\in\mathbb D.
\]
Taking
\[
\alpha=\frac{1-\overline d}{1-|d|^2}
\]
gives
\[
1-2\operatorname{Re}\alpha=
-\frac{|1-d|^2}{1-|d|^2}<0,
\]
together with \(d=(1-\overline\alpha)/\alpha\), and hence \(\widetilde m_d=u_\alpha\).

Therefore scalar-circle preservation is equivalent to scalarity of \(A\), two nonidentity scalar probes already detect it, and the complete scalar action is precisely the Möbius/anti-Möbius stabilizer of \(1\).

Finally, Jia and Ji prove that \(\Psi_A\) preserves orthogonality exactly for \(A=0\) or \(A=I\). In the formulas above these are respectively \(c=0\), giving \(u(a)=a\), and \(d=0\), giving \(u(a)=\overline a\).

## Verification
The proof uses only the source formula for \(\Psi_A(aI)\), its invertibility statement, elementary matrix subtraction, and the standard normal forms of holomorphic and antiholomorphic automorphisms of the unit disk.

The sign split was checked from the exact identity
\[
|1-\alpha|^2-|\alpha|^2=1-2\operatorname{Re}\alpha.
\]
The inverse parameterizations were substituted algebraically:
\[
\alpha=\frac{c(1-\overline c)}{1-|c|^2}
\]
for the holomorphic branch and
\[
\alpha=\frac{1-\overline d}{1-|d|^2}
\]
for the antiholomorphic branch. No finite experiment is used as proof.

## Relationship to prior work
Jia and Ji classify all order automorphisms of finite-dimensional matrix partial isometries and derive the explicit scalar-unitary formula for \(U_a=\Psi_A(aI)\). Their paper does not state a classification of automorphisms preserving the scalar unitary circle, does not identify the resulting circle maps as the full Möbius/anti-Möbius stabilizer of \(1\), and does not give the two-point scalarity test.

Molnár's earlier theorem treats the substantially narrower class of automorphisms preserving both order and orthogonality, together with a continuity hypothesis. In that setting he proves preservation of scalar partial isometries and obtains only the two continuous multiplicative circle characters \(a\mapsto a\) and \(a\mapsto\overline a\). The present result explains how dropping orthogonality enlarges those two boundary actions to the full holomorphic and antiholomorphic disk-automorphism families fixing \(1\).

## Limitations
The classification is for the canonical normalized maps \(\Psi_A\) in the Jia--Ji parametrization. It does not classify center preservation for every non-normalized factorization \(\Delta_{CD}\circ\Psi_A\), where the outer unitary or conjugate-unitary factors must also be accounted for.

The result identifies the induced action on scalar unitaries and a two-point detection principle. It does not claim that the star order alone intrinsically singles out the scalar circle without additional structure.

## References
1. F. Jia and G. Ji, *Order automorphisms of partial isometries in \(M_n(\mathbb C)\)*, arXiv:2609.25559v1, 2026.
2. L. Molnár, *On certain automorphisms of sets of partial isometries*, arXiv:math/0011028v1; Archiv der Mathematik 78 (2002), 43--50.
