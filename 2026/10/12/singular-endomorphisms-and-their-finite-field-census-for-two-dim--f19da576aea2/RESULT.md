# Singular endomorphisms and their finite-field census for two-dimensional perfect evolution algebras

## Finding
Let \(K\) be any field, and let \(E_A\) be the perfect evolution algebra with natural basis \(e_1,e_2\), \(e_1e_2=0\), and
\[
e_1^2=a e_1+b e_2,\qquad e_2^2=c e_1+d e_2,\qquad A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\quad ad-bc\ne0.
\]
The endomorphism monoid is a disjoint union of the zero map, the invertible automorphisms, and the following exhaustive list of nonzero singular homomorphisms:

* If \(b,c\ne0\), there are no nonzero singular endomorphisms.
* If \(c=0\), \(b\ne0\), then \(a,d\ne0\), and exactly the singular maps \(T(e_1)=z\), \(T(e_2)=0\) exist, where \(z=(a/d)e_2\), or \(z=e_1+y e_2\) with \(d y^2-a y+b=0\).
* If \(b=0\), \(c\ne0\), then \(a,d\ne0\), and exactly the singular maps \(T(e_1)=0\), \(T(e_2)=z\) exist, where \(z=(d/a)e_1\), or \(z=x e_1+e_2\) with \(a x^2-d x+c=0\).
* If \(b=c=0\), then \(a,d\ne0\). There are exactly six nonzero singular maps: three maps killing \(e_2\), with \(e_1\) sent to any nonzero element of \(\{0,e_1\}+\{0,(a/d)e_2\}\), and three maps killing \(e_1\), with \(e_2\) sent to any nonzero element of \(\{0,(d/a)e_1\}+\{0,e_2\}\).

Every nonzero singular endomorphism has rank one and is **either idempotent or square-zero**. For the one-sided cases, the distinguished image \((a/d)e_2\) or \((d/a)e_1\) gives the unique square-zero singular endomorphism, and each quadratic root gives an idempotent rank-one retraction. In the diagonal case, two of the six singular maps are square-zero and the other four are idempotent.

For every finite field \(\mathbf F_q\), **including characteristic two**, put \(s=\gcd(2,q-1)\), \(r=\gcd(3,q-1)\), and \(G=q(q-1)^2(q+1)\). Among all \(G\) invertible structure matrices \(A\), the exact numbers of pairs \((A,T)\) with \(T\) a rank-one idempotent and with \(T\) a nonzero square-zero endomorphism are, respectively,
\[
\boxed{2q(q-1)^2\qquad\text{and}\qquad2q(q-1)^2}.
\]
The exact total number of labeled pairs of a perfect evolution-algebra structure matrix and one of its endomorphisms is
\[
\boxed{\sum_{A\in\mathrm{GL}_2(\mathbf F_q)}|\operatorname{End}(E_A)|=2q(q-1)^2(q+1)+(q-1)^2(5q-s+r).}
\]
The equality of the global square-zero and rank-one idempotent counts is an arithmetic phenomenon that is independent of characteristic, even though the automorphism contribution depends on square and cube roots of unity.

## Assumptions and scope
The structure matrices are labeled relative to the ordered natural basis; the finite-field counts are **not** counts of isomorphism classes. Endomorphisms are \(K\)-linear and preserve the given multiplication, but need not be unital. The theorem holds over every field and requires only \(\det A\ne0\); no characteristic restriction or algebraic closure is needed. In characteristic two, subtraction equals addition in the quadratic-root equations. The counts use every prime power \(q\ge2\), not merely prime fields.

## Proof
**1. Rank restrictions.** Write \(T(e_1)=u e_1+v e_2\) and \(T(e_2)=w e_1+z e_2\). Since \(T(e_1e_2)=0\) and the two squares form a basis (\(A\) invertible), \(uw=vz=0\). A rank-two homomorphism is an automorphism: it is an invertible multiplicative map of a finite-dimensional algebra, with multiplicative inverse. A rank-zero homomorphism is zero. If a rank-one homomorphism has both \(T(e_1),T(e_2)\ne0\), these two vectors are proportional; their product is a nonzero scalar times the square of either, so the latter square is zero. But \(E_A^2=E_A\), and the images of both generator-squares then vanish, forcing \(T(E_A)=T(E_A^2)=0\), a contradiction. Thus exactly one generator has nonzero image.

**2. Necessary and sufficient singular maps.** If \(T(e_1)=v\ne0\), \(T(e_2)=0\), then \(T(e_2^2)=c v=0\), hence \(c=0\). Conversely, for \(c=0\), multiplication preservation reduces exactly to \(v^2=a v\). The determinant forces \(a,d\ne0\). Writing \(v=x e_1+y e_2\), the first coordinate gives \(x^2=x\), so \(x\in\{0,1\}\). For \(x=0\), excluding the zero vector gives uniquely \(y=a/d\); for \(x=1\), the remaining condition is \(d y^2-a y+b=0\). This proves the complete list for maps killing \(e_2\). Interchanging the basis roles gives the symmetric case for maps killing \(e_1\). If \(b=c=0\), both families apply without overlap, each with exactly three nonzero vectors: the quadratic splits as \(y(dy-a)=0\) or \(x(ax-d)=0\). If \(bc\ne0\), neither family is possible. These equations are necessary and sufficient, since checking generator products checks every bilinear product.

**3. Composition types.** For a map killing \(e_2\) and sending \(e_1\) to \(x e_1+y e_2\), we have \(T^2=xT\); in the classification \(x\in\{0,1\}\). Similarly, for a map killing \(e_1\), \(T^2=yT\) with \(y\in\{0,1\}\). Hence every nonzero singular map is square-zero or idempotent, and the respective lists follow. No finite enumeration is being used to justify this arbitrary-field statement.

**4. Finite-field counts for singular maps.** Write \(S=(q-1)^2\). There are \(S\) diagonal invertible matrices, each with two square-zero and four idempotent singular endomorphisms. In each one-sided triangular family (\(c=0,b\ne0\), or \(b=0,c\ne0\)), there are \(S(q-1)\) matrices, each with one square-zero map. Counting roots of \(d y^2-a y+b=0\) over triples \((a,d,b)\) with \(a,d,b\ne0\): for each ordered \((a,d)\), each \(y\notin\{0,a/d\}\) determines exactly one nonzero \(b=ay-dy^2\), giving precisely \(S(q-2)\) roots counted with their matrices, including repeated roots once. The other triangular family is symmetric. Therefore the total number of square-zero nonzero singular maps is \(2S+2S(q-1)=2qS\); the total number of idempotent rank-one maps is \(4S+2S(q-2)=2qS\). In particular the total rank-one count is \(4qS\).

**5. Automorphism contribution.** Every invertible endomorphism is monomial: \(uw=vz=0\), together with invertibility, forces precisely one nonzero entry in each row and each column. The identity contributes once for all \(G\) matrices. A nonidentity diagonal automorphism requires \(a=d=0\), \(bc\ne0\), and has scalars \(\lambda,\lambda^2\) with \(\lambda^3=1\). These provide \((r-1)S\) additional automorphisms summed over all structure matrices. For a nonidentity swapped monomial automorphism \(T(e_1)=x e_2\), \(T(e_2)=y e_1\), the four equations are
\[
x^2c=by,\quad x^2d=ax,\quad y^2a=dy,\quad y^2b=cx.
\]
They have solutions only in three support types. Diagonal matrices supply one swap per matrix, so \(S\) swaps. Fully supported matrices supply a unique swap precisely when \(a^3c=bd^3\): write \(b=t a^2/d\), \(c=t d^2/a\) with \(t\in\mathbf F_q^\times\), \(t^2\ne1\). Thus there are \(S(q-1-s)\) such swaps. Antidiagonal matrices supply \(r\) swaps exactly when \(b/c\) is a cube, and there are \(S/r\) such matrices, yielding another \(S\) swaps. No other zero patterns can obey all four equations. Therefore the number of automorphisms summed over all \(A\) is \(G+(r-1)S+S+S(q-1-s)+S=G+S(q-s+r)\).

Adding the \(G\) zero maps and \(4qS\) singular nonzero maps yields \(2G+S(5q-s+r)\), completing the proof.

## Verification
The self-contained `verify.py` checks the defining preservation equations for every labeled matrix \(A\in\mathrm{GL}_2(\mathbf F_q)\) and every \(2\times2\) linear map over \(\mathbf F_2,\mathbf F_3,\mathbf F_4,\mathbf F_5,\mathbf F_7\). Arithmetic in \(\mathbf F_4\) is implemented by \(\mathbf F_2[\alpha]/(\alpha^2+\alpha+1)\). For each field, it compares endomorphism totals, all rank-one maps, the division into idempotent and square-zero maps, and the automorphism-size histogram. Run `python3 verify.py`; success prints `VERIFY_OK`. These finite checks corroborate but do not replace the arbitrary-field proof.

## Relationship to prior work
Sriwongsa and Zou, *On Automorphism Groups of Idempotent Evolution Algebras* (arXiv:2202.01333, 2022), establish the monomial automorphism conditions and give two-dimensional automorphism classifications; those results are incorporated as antecedents, and automorphism enumeration alone is **not** claimed new. Cabrera Casado, Martín Barquero, and Martín González, *Two dimensional perfect evolution algebras over domains* (arXiv:2204.08410, 2022; later Journal of Algebraic Combinatorics), give the classification of the underlying perfect algebras, not a census of their singular endomorphisms. Wei and Zou, *Isomorphism Classes of Idempotent Evolution Algebras* (arXiv:2310.12368, 2023), count isomorphism classes, not the rank-one endomorphism and retraction fibers stated here. The added assertion is the complete singular endomorphism classification with its characteristic-uniform global equality and total count.

## Limitations
The exact finite-field formulas count labeled pairs \((A,T)\), not conjugacy classes of endomorphisms. The theorem does not assert a classification of endomorphism monoids in dimension three or higher. A closely related unpublished or differently indexed classification of two-dimensional evolution-algebra endomorphisms could still cover some statements; absence from inspected literature is not an absolute novelty proof.

## References
1. S. Sriwongsa and Y. M. Zou, *On Automorphism Groups of Idempotent Evolution Algebras*, arXiv:2202.01333 (first public 2022-02-02); later Linear Algebra and its Applications 641 (2022), DOI:10.1016/j.laa.2022.02.010.
2. Y. Cabrera Casado, D. Martín Barquero, C. Martín González, *Two dimensional perfect evolution algebras over domains*, arXiv:2204.08410 (first public 2022-04-18); DOI:10.1007/s10801-022-01196-1.
3. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368 (first public 2023-10-18); Linear Algebra and its Applications 675 (2023), DOI:10.1016/j.laa.2023.06.006.
