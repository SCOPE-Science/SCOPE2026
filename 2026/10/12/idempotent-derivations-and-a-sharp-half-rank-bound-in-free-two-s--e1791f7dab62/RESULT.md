# Idempotent derivations and a sharp half-rank bound in free two-step associative algebras

## Finding
Let \(n\ge2\) and let \(K\) be a field. The nonunital associative algebra \(N_n(K)=V\oplus W\), with \(V=K^n\), \(W=V\otimes_KV\), and \((v,w)(v',w')=(0,v\otimes v')\), is the positive-degree part of the cubic-truncated free associative algebra on \(n\) generators. Here “cubic-truncated” means that all words of length at least three vanish, whereas the ordered quadratic words remain linearly independent.

A derivation means a \(K\)-linear map \(D\) satisfying \(D(xy)=D(x)y+xD(y)\). A composition-idempotent derivation means \(D^2=D\), not a derivation whose values are idempotent elements.

**Theorem.** Over any field \(K\), every derivation has a unique pair of parameters \(A:V\to V\), \(f:V\to W\), and is given by
\[
D(v,w)=\bigl(Av, f(v)+Bw\bigr),\qquad B=A\otimes I+I\otimes A.
\]
If \(\operatorname{char}K\ne2\), only \(D=0\) is composition-idempotent. If \(\operatorname{char}K=2\), all composition-idempotent derivations are obtained by choosing a projection \(A^2=A\), setting \(U=\operatorname{im}A\), \(Z=\ker A\), and choosing an arbitrary linear map \(f\) satisfying
\[
f(U)\subseteq(U\otimes U)\oplus(Z\otimes Z),\qquad
f(Z)\subseteq(U\otimes Z)\oplus(Z\otimes U).
\]
Writing \(r=\dim U\), \(s=\dim Z=n-r\), the corresponding linear rank is precisely \(r+2rs\).

For any finite field \(\mathbb F_q\), the complete number of labeled composition-idempotent derivations, stratified by linear rank, is
\[
\mathcal D_{n,q}(T)=
\begin{cases}
1,&\text{if \(q\) is odd},\\[2pt]
\displaystyle\sum_{r=0}^n{n\brack r}_q q^{r(n-r)+r^3+3r(n-r)^2}T^{r+2r(n-r)},&\text{if \(q\) is even}.
\end{cases}
\]
Here \({n\brack r}_q\) is the Gaussian coefficient counting \(r\)-planes in \(\mathbb F_q^n\). The exponents \(r+2r(n-r)\) are pairwise distinct as \(r\) runs from \(0\) to \(n\).

**Sharp dimension bound.** In characteristic two, every composition-idempotent derivation satisfies
\[
\operatorname{rank}D\le\frac{n(n+1)}2=\frac{\dim_K N_n}2.
\]
Equality holds if and only if \(\dim\operatorname{im}A=\lceil n/2\rceil\). In other characteristics the unique rank is zero. For \(n=2,q=2\), the polynomial is \(1+256T^2+96T^3\), giving \(353\) such derivations of the \(6\)-dimensional algebra.

## Assumptions and scope
The field is arbitrary for the classification; no algebraic-closedness, finiteness, or characteristic restriction is required. The parameter \(n\) is any integer at least two. The finite-field polynomial holds for every prime power \(q\); the even case necessarily means characteristic two. Derivations need not preserve the word-length grading, because the parameter \(f\) may send a generator to arbitrary quadratic words. The algebra is explicitly nonunital. We count labeled \(K\)-linear derivations, not isomorphism classes or automorphism orbits.

## Proof
First, \(W=N_n^2\) is spanned by all products of elements of \(V\) and annihilates the whole algebra on both sides. Every derivation preserves \(W\): this follows directly from the Leibniz rule on products. Thus the \(V\to V\) component of \(D\) is some \(A\), the \(V\to W\) component is some \(f\), and \(D(W)\subseteq W\). For \(v,v'\in V\), the derivation rule requires
\[
D(v\otimes v')=Av\otimes v'+v\otimes Av'.
\]
Since elementary tensors span \(W\), this uniquely fixes \(D|_W=B=A\otimes I+I\otimes A\). Conversely, any \((A,f)\) defines a derivation: the displayed identity covers products of generators and all products with a quadratic element vanish. This proves the first assertion, including uniqueness.

Apply \(D\) twice. Direct block multiplication gives
\[
D^2=D\quad\Longleftrightarrow\quad
A^2=A,\qquad B^2=B,\qquad Bf+fA=f.
\]
If \(A^2=A\), there is a direct-sum decomposition \(V=U\oplus Z\) into image and kernel. With respect to
\[
W=(U\otimes U)\oplus(U\otimes Z)\oplus(Z\otimes U)\oplus(Z\otimes Z),
\]
the induced \(B\) acts by scalars \(2,1,1,0\), respectively. If \(\operatorname{char}K\ne2\) and \(U\ne0\), the nonzero space \(U\otimes U\) has \(B=2I\), while idempotency would require \(4I=2I\), contradicting \(2\ne0\). Hence \(A=0\), then \(B=0\), and \(Bf+fA=f\) forces \(f=0\). Conversely the zero map qualifies.

If \(\operatorname{char}K=2\), the scalar action of \(B\) is \(0,1,1,0\), so \(B^2=B\) for every projection \(A\). The remaining equation on inputs in \(U\) reads \(Bf(u)=0\), and on inputs in \(Z\) reads \(Bf(z)=f(z)\). The kernel and image of \(B\) are respectively \((U\otimes U)\oplus(Z\otimes Z)\) and \((U\otimes Z)\oplus(Z\otimes U)\), giving exactly the two announced conditions on \(f\). This proves both necessity and sufficiency.

A composition-idempotent endomorphism is a projection. The top component of \(D\) has rank \(r\); its restriction to \(W\) has image \(\operatorname{im}B=(U\otimes Z)\oplus(Z\otimes U)\), of dimension \(2rs\). Passing to the quotient by \(W\) gives an exact sequence of image spaces; equivalently, no vector with nonzero top component can cancel a quadratic image. Therefore \(\operatorname{rank}D=r+2rs\), independently of \(f\).

For finite \(K=\mathbb F_q\) of characteristic two, there are \({n\brack r}_q\) choices of the \(r\)-plane \(U\). After fixing \(U\), each complementary \(s\)-plane \(Z\) corresponds to a linear map from one fixed complement to \(U\), so there are \(q^{rs}\) complements; each \((U,Z)\) determines a unique projection \(A\). Allowed values of \(f\) on a basis of \(U\) lie in a space of dimension \(r^2+s^2\), and those on a basis of \(Z\) lie in a space of dimension \(2rs\). The total free dimension is
\[
r(r^2+s^2)+s(2rs)=r^3+3rs^2.
\]
Thus the number of \(f\)'s per projection is exactly \(q^{r^3+3rs^2}\). Multiplying counts and recording \(\operatorname{rank}D=r+2rs\) proves the polynomial. To show rank exponents cannot collide, observe for integers \(r,t\in[0,n]\) that
\[
[r+2r(n-r)]-[t+2t(n-t)]=(r-t)(2n+1-2r-2t).
\]
When \(r\ne t\), the second factor is odd and cannot vanish; hence all ranks are distinct.

Finally,
\[
\frac{n(n+1)}2-[r+2r(n-r)]=\frac{(n-2r)(n-2r+1)}2\ge0
\]
for all integers \(r\), since two consecutive integers have a nonnegative product. Equality requires \(n-2r\in\{0,-1\}\), giving the unique integral value \(r=\lceil n/2\rceil\). Such projections exist over any field, so the bound is sharp. This completes the proof.

## Verification
Run `python3 checker.py` with Python 3 and no third-party packages. It constructs the induced map \(B\) from the Leibniz rule rather than trusting its symbolic eigenspace count, solves the linear equations for all quadratic lifts, and compares complete rank multiplicities for \(n=1\) over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), \(n=2\) over the same four fields, and \(n=3\) over \(\mathbb F_2\). The one-generator cases are boundary checks, not extensions of the theorem's stated domain. The script also exhausts every \((A,f)\) for \(n=2,q=2\), tests \(D^2=D\) directly, verifies the Leibniz rule on all basis pairs, and recovers the \(353\) maps and rank polynomial above. A successful run prints `VERIFY_OK`. These finite computations confirm boundary cases but are not a substitute for the arbitrary-field proof.

## Relationship to prior work
Drensky and Makar-Limanov, *Locally Nilpotent Derivations of Free Algebra of Rank Two* (arXiv:1909.13262v1, first posted 2019-09-29), analyze derivations of the untruncated free associative algebra under characteristic-zero hypotheses; they do not state the present finite-dimensional composition-idempotence classification or characteristic-two rank census. La Rosa and Mancini, *Derivations of two-step nilpotent algebras* (arXiv:2301.11058v1, 2023-01-26), consider different two-step algebraic structures under non-two characteristic assumptions. Hristova, *On GL(n)-module structure of Lie nilpotent associative relatively free algebras* (arXiv:2209.10180v1, 2022-09-21), studies different associative quotients through representation-theoretic methods. These constructions motivate studying derivations of free quotients but do not imply the exact statement given here.

A commutative cubic-truncated algebra has quadratic piece \(\operatorname{Sym}^2(V)\), whereas this theorem retains all ordered products \(V\otimes V\); in particular, the two distinct mixed tensor summands are essential to its rank formula and half-dimension bound. The commutative or alternating quotients cannot recover the present labeled rank multiplicities just by replacing notation.

## Limitations
This theorem classifies only composition-idempotent **derivations**, not arbitrary algebra endomorphisms, and concerns the nonunital, free associative two-step algebra with no additional quadratic relations. It does not classify automorphism-conjugacy orbits. Counts are for all labeled maps. The bibliographic search may have missed an equivalent result under the terminology of two-step associative algebras or differential projections; the mathematical proof does not establish historical priority, and no independent audit has been performed.

## References
1. V. Drensky and L. Makar-Limanov, *Locally Nilpotent Derivations of Free Algebra of Rank Two*, arXiv:1909.13262v1 (2019), https://arxiv.org/abs/1909.13262.
2. S. La Rosa and M. Mancini, *Derivations of two-step nilpotent algebras*, arXiv:2301.11058v1 (2023), https://arxiv.org/abs/2301.11058.
3. R. Hristova, *On GL(n)-module structure of Lie nilpotent associative relatively free algebras*, arXiv:2209.10180v1 (2022), https://arxiv.org/abs/2209.10180.
