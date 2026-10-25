# Square-one conjugacy-class spectra in three-block unipotent radicals over even fields

## Finding
For each positive triple \(a,b,c\) and each even prime power \(q\), let \(G_{a,b,c}(q)\) denote the three-block upper-unitriangular group whose elements are
\[
 g(X,Y,Z)=\begin{pmatrix}I_a&X&Z\\0&I_b&Y\\0&0&I_c\end{pmatrix},
 \quad X\in M_{a,b}(\mathbb F_q),\quad Y\in M_{b,c}(\mathbb F_q),\quad Z\in M_{a,c}(\mathbb F_q).
\]
For \(0\le r\le\min(a,b)\), \(0\le s\le\min(c,b-r)\), define
\[
 N_{r,s}=\genfrac{[}{]}{0pt}{}{a}{r}_q\genfrac{[}{]}{0pt}{}{b}{r}_q |\mathrm{GL}_r(q)|
 \genfrac{[}{]}{0pt}{}{b-r}{s}_q\genfrac{[}{]}{0pt}{}{c}{s}_q|\mathrm{GL}_s(q)|,
 \qquad d(r,s)=as+cr-rs.
\]
The Gaussian binomial \(\genfrac{[}{]}{0pt}{}{u}{v}_q\) counts \(v\)-subspaces of \(\mathbb F_q^u\), and \(|\mathrm{GL}_0(q)|=1\). Then the **complete class-size enumerator for solutions of \(g^2=1\)** (including the identity) is
\[
 \boxed{K_{a,b,c;q}(T)=\sum_{r=0}^{\min(a,b)}\ \sum_{s=0}^{\min(c,b-r)}
 N_{r,s}q^{ac-d(r,s)}T^{d(r,s)}.}
\]
The coefficient of \(T^d\) counts the conjugacy classes of square-one elements whose cardinality is \(q^d\). To count nonidentity involution classes, subtract one from the constant coefficient. In particular, there are exactly \(q^{ac}\) singleton classes (all central); all conjugacy-class sizes occurring among these elements are powers of \(q\).

The greatest attained class size is \(q^{D}\), where
\[
 \boxed{D=\begin{cases}ac,&b\ge\min(a,c),\\b\max(a,c),&b<\min(a,c).\end{cases}}
\]
Thus a middle block of dimension at least the smaller outside dimension is necessary and sufficient for square-one classes to attain \(q^{ac}\), the full cardinality of the central matrix block. When \(b<\min(a,c)\), the number of conjugacy classes attaining \(q^D\) is \(\genfrac{[}{]}{0pt}{}{c}{b}_q|\mathrm{GL}_b(q)|\) if \(a>c\), is \(\genfrac{[}{]}{0pt}{}{a}{b}_q|\mathrm{GL}_b(q)|\) if \(c>a\), and twice \(\genfrac{[}{]}{0pt}{}{a}{b}_q|\mathrm{GL}_b(q)|\) if \(a=c\).

The total number of square-one elements is \(q^{ac}\sum_{r,s}N_{r,s}\). As the group has order \(q^{ab+bc+ac}\) and exponent dividing four, the number of elements of order four is \(q^{ab+bc+ac}-q^{ac}\sum_{r,s}N_{r,s}\).

For example, when \((a,b,c,q)=(2,1,2,2)\), there are \(16\) singleton classes and \(24\) classes of size four: precisely \(112\) square-one elements, of which \(111\) have order two, in a group of order \(256\).

## Assumptions and scope
All three block sizes are positive integers; the finite field has characteristic two and cardinality any \(q=2^f\) with \(f\ge1\). Conjugation is *within the unipotent group* \(G_{a,b,c}(q)\), not within its ambient general linear or parabolic group. The variable \(T\) records the base-\(q\) exponent of the conjugacy-class size. Rank pairs \((r,s)\) are ranks of the upper-first and upper-second off-diagonal blocks, respectively, and Gaussian coefficients vanish when the lower index is outside its range. The results are uniform in all positive block sizes and all even finite fields.

## Proof
**1. Products, powers, and the square-one condition.** Direct block multiplication gives
\[
 g(X,Y,Z)g(A,B,C)=g(X+A,Y+B,Z+C+XB).
\]
In characteristic two, \(g(X,Y,Z)^2=g(0,0,XY)\). Hence \(g^2=1\) if and only if \(XY=0\). Equivalently, \(\operatorname{im}Y\subseteq\ker X\). Since \((g-I)^3=0\), every group element has order one, two or four.

**2. Exact rank-pair multiplicities.** For fixed rank \(r\), the number of \(a\)-by-\(b\) matrices \(X\) is \(\genfrac{[}{]}{0pt}{}{a}{r}_q\genfrac{[}{]}{0pt}{}{b}{r}_q|\mathrm{GL}_r(q)|\): choose image, quotient kernel and induced isomorphism. Its kernel has dimension \(b-r\). Matrices \(Y:\mathbb F_q^c\to\ker X\) of rank \(s\) number \(\genfrac{[}{]}{0pt}{}{b-r}{s}_q\genfrac{[}{]}{0pt}{}{c}{s}_q|\mathrm{GL}_s(q)|\). Multiplication gives precisely \(N_{r,s}\) ordered pairs with \(XY=0\), proving the asserted ranges are exhaustive and disjoint.

**3. Conjugation and orbit dimension.** Conjugating by \(g(A,B,C)\) fixes \(X\) and \(Y\) and shifts \(Z\) by \(AY-XB\). The image of the linear map
\[
 (A,B)\longmapsto AY-XB\in M_{a,c}(\mathbb F_q)
\]
contains all maps factoring through \(Y\) (dimension \(as\)) and all maps with image in \(\operatorname{im}X\) (dimension \(cr\)). Their intersection consists of maps factoring through \(Y\) with image in \(\operatorname{im}X\), of dimension \(rs\). Thus its image has dimension \(d(r,s)=as+cr-rs\), and every conjugacy orbit at that rank pair has \(q^{d(r,s)}\) elements. Since \(Z\) varies over an \(ac\)-dimensional vector space, there are \(q^{ac-d(r,s)}\) distinct classes for each fixed \((X,Y)\). Combine with step 2 and sum to obtain \(K\). The sole rank pair with \(d=0\) is \((0,0)\); it contributes \(q^{ac}\) singleton classes.

**4. Sharp largest class.** The alternative identity \(d(r,s)=ac-(a-r)(c-s)\) gives \(d\le ac\), with equality exactly if \(r=a\) or \(s=c\). Such a rank pair with \(r+s\le b\) exists if and only if \(b\ge\min(a,c)\). If \(b<\min(a,c)\), then
\[
 d(r,s)\le \max(a,c)(r+s)\le b\max(a,c).
\]
Equality occurs at \((r,s)=(b,0)\) when \(c>a\), at \((0,b)\) when \(a>c\), and at both those distinct pairs when \(a=c\) (since \(d=\max(a,c)(r+s)-rs\) then requires \(rs=0\)). Substituting those rank pairs in \(N_{r,s}\) gives the asserted multiplicities of maximum-size classes. Each attained class-size exponent is bounded by this sharp maximum.

**5. Orders.** Summing \(N_{r,s}\) over rank pairs counts all \((X,Y)\) satisfying \(XY=0\); the upper-right block has \(q^{ac}\) unconstrained choices. This proves the order-two-inclusive total and its complement, the order-four total. No infinite-case claim rests on finite enumeration.

## Verification
A standalone standard-library Python script `verify.py` independently enumerates group products, inverses, conjugacy orbits and square-one conditions, rather than using the proof's orbit formula to produce the observed spectrum. It uses complete element enumeration for eight small cases over \(\mathbb F_2\) and \(\mathbb F_4\), checking the complete class-size distribution and the sharp largest class. Execute `python3 verify.py`; its final success marker is `VERIFY_OK_THREE_BLOCK_SQUARE_ONE_CONJUGACY`. The tested cases are \((1,1,1,2)\), \((1,2,1,2)\), \((2,1,1,2)\), \((1,1,2,2)\), \((2,1,2,2)\), \((2,2,1,2)\), \((1,1,1,4)\), and \((1,1,2,4)\). These finite checks are corroboration, not proof for all dimensions.

## Relationship to prior work
Diaconis and Thiem [1, especially Section 5, Example 3 and Corollary 5.1] *already describe* this three-block pattern group, the fact that its superclasses are ordinary conjugacy classes, and the underlying affine corner-block orbit mechanism. The group model and conjugation mechanism are therefore **not new**. Goodwin and Röhrle [2] prove polynomiality of the *total* number of conjugacy classes for parabolic unipotent radicals with at most five steps and derive general centralizer formulas. Soffer [3] gives upper bounds for the number of conjugacy classes in full unitriangular groups. None of the inspected statements supplies a rank-pair-classified, size-resolved count **restricted to order dividing two in even characteristic** or the sharp middle-block saturation threshold. The novelty claim is restricted to this explicit conditional enumerator and extremal count, derived by combining the known orbit framework with the square-zero restriction and exact compatible-rank enumeration. In the boundary \(a=b=c=1\), classical Heisenberg-group class sizes are recovered and are not claimed new.

## Limitations
The result concerns the unipotent group's own conjugacy action in characteristic two and does not classify ambient-parabolic or general-linear conjugacy or odd-characteristic involutions. It does not enumerate the conjugacy-class sizes of elements of order four individually. Earlier general orbit machinery provides substantial prior coverage of the basic action: an older explicit specialization or a straightforward corollary in another source could reduce priority. Independent mathematical review and exhaustive historical-priority confirmation have not occurred.

## References
[1] Persi Diaconis and Nathaniel Thiem, *Supercharacter formulas for pattern groups*, arXiv:math/0610161v1 (4 October 2006), especially Section 5, Example 3 and Corollary 5.1. https://arxiv.org/abs/math/0610161

[2] Simon M. Goodwin and Gerhard Röhrle, *Counting conjugacy classes in the unipotent radical of parabolic subgroups of* \(\mathrm{GL}_n(q)\), arXiv:0901.0667v1 (6 January 2009), especially Theorem 1.2 and Corollary 3.1. https://arxiv.org/abs/0901.0667

[3] Andrew Soffer, *Upper bounds on the number of conjugacy classes in unitriangular groups*, arXiv:1411.5389v1 (19 November 2014), especially Sections 1, 5 and 6. https://arxiv.org/abs/1411.5389
