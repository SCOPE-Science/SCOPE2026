# Exact determinant fibers for six-entry cyclic matrix completions

## Finding

Fix a finite field \(\mathbb F_q\) of odd cardinality, and let \(a,b,c,u,v,w\in\mathbb F_q^\times\). The six fixed entries occupy the main diagonal and the directed cycle immediately above it (with wraparound). The three complementary entries \(x,y,z\in\mathbb F_q\) remain free:

\[
M(x,y,z)=\begin{pmatrix}a&u&x\\y&b&v\\w&z&c\end{pmatrix}.
\]

Put \(D=abc\), \(T=uvw\), and write \(\chi\colon\mathbb F_q\to\{-1,0,1\}\) for the quadratic character, with \(\chi(0)=0\). For *every* target \(t\in\mathbb F_q\), the exact determinant fiber is

\[
\boxed{N_t:=\#\{(x,y,z)\in\mathbb F_q^3:\det M(x,y,z)=t\}=q^2+1+q\chi((D+T-t)^2-4DT).}
\]

In particular, the number of singular completions is exactly \(q^2+1\) if \(D=T\), and exactly \(q^2+q+1\) otherwise. Consequently the count of invertible completions is respectively \(q^3-q^2-1\) or \(q^3-q^2-q-1\).

The three possible determinant-fiber sizes are \(q^2+q+1\), \(q^2+1\), and \(q^2-q+1\). Let \(z_0=2\) if \(DT\) is a square in \(\mathbb F_q^\times\), and \(z_0=0\) otherwise. These three sizes occur for precisely \((q-1-z_0)/2\), \(z_0\), and \((q+1-z_0)/2\) determinant targets respectively.

## Assumptions and scope

The field cardinality \(q\) is any odd prime power, not just a prime. All six prescribed entries must be *nonzero*; no condition is imposed on the three free entries or on the target determinant, which may be zero. The result counts ordered completions (one matrix for each ordered triple of free entries). The support of the prescribed entries is the union of the identity permutation and one cyclic permutation on three letters, not an arbitrary six-entry pattern.

## Proof

Expand the determinant and set \(C=D+T\):

\[
\det M=C-ucy-bwx+(xy-av)z.
\]

Because \(a,v\ne0\), exactly \(q-1\) pairs \((x,y)\) satisfy \(xy=av\), and the remaining \(q^2-q+1\) pairs have \(xy-av\ne0\). For each pair in the latter class, the displayed expression has exactly one choice of \(z\) yielding any prescribed target \(t\).

For an exceptional pair \(xy=av\), necessarily \(x\ne0\) and \(y=av/x\). Since \(b,w\ne0\), the substitution \(Z=bwx\) ranges bijectively over \(\mathbb F_q^\times\), and the determinant equation becomes

\[
 t=C-Z-\frac{DT}{Z},\qquad
 Z^2-(C-t)Z+DT=0.
\]

As \(DT\ne0\), no root is zero. The discriminant is \(\Delta_t=(D+T-t)^2-4DT\). In odd characteristic the polynomial has exactly \(1+\chi(\Delta_t)\) roots, and for each root the variable \(z\) is arbitrary, contributing \(q\) completions. Thus

\[
N_t=(q^2-q+1)+q(1+\chi(\Delta_t))=q^2+1+q\chi(\Delta_t).
\]

For \(t=0\) one has \(\Delta_0=(D-T)^2\). Its quadratic character is zero exactly if \(D=T\), and one otherwise, proving the singular and invertible counts.

It remains to count determinant targets of each fiber size. Since \(4DT\ne0\), the elementary character identity

\[
\sum_{s\in\mathbb F_q}\chi(s^2-4DT)=-1
\]

holds: the number of pairs \((s,r)\) satisfying \(r^2=s^2-4DT\) equals \(q-1\), because \((s-r)(s+r)=4DT\) has one solution for each nonzero first factor, and the change of variables is invertible in odd characteristic. Also \(\Delta_t=0\) has two distinct solutions \(t\) precisely when \(DT\) is a square and none otherwise. Writing \(z_0\) for that number, the displayed sum and the total number \(q\) of targets force \((q-1-z_0)/2\) square discriminants and \((q+1-z_0)/2\) nonsquare discriminants. This proves all stated multiplicities.

## Verification

The standalone program `verify.py` computes every fiber by direct enumeration of the three free entries and compares it with the character formula, with no floating-point arithmetic. It tested all nonzero six-tuples for fields of orders \(3\) and \(5\), as well as deterministic parameter samples over fields of orders \(7\), \(9\), and \(11\). In total: 4,544 parameter tuples, 24,128 determinant-fiber comparisons, and 4,544 independent total-count checks, all passed. The order-nine field is implemented directly as \(\mathbb F_3[\alpha]/(\alpha^2+1)\). The unrestricted theorem is proved above; the tests are not an exhaustive check over all fields or all fixed coefficients.

## Relationship to prior work

Gorodetsky [1, Theorem 1.4] gives exact counts with arbitrary prescribed *diagonal* entries of an invertible finite-field matrix, but does not prescribe an additional directed cycle or resolve the full determinant-target distribution of these six-entry completions. His submatrix count [1, Lemma 1.7] applies to complete rectangular entry constraints; the present six-entry pattern is nonrectangular.

Li and Hu [2, Theorem 2.1] evaluate general additive Fourier sums twisted by a multiplicative determinant character. In principle, multiple Fourier inversions express determinant fibers for arbitrary prescribed entry patterns, including this one, as unevaluated finite sums. The formula above is instead a direct, evaluated three-level profile controlled only by two cycle products and a quadratic discriminant. The earlier general transform is acknowledged; no claim that the existence of such a Fourier representation is new is made.

The precise evaluated identity has not been located in the examined sources or targeted mathematical research-record queries. This is a best-knowledge originality assessment, not a proof of priority or an independent audit.

## Limitations

This theorem does not address even-characteristic fields, fixed coefficients equal to zero, other sparse patterns, or matrices of order greater than three. It supplies exact finite-field counts, not an asymptotic or a computational-complexity improvement. As with any targeted novelty search, unindexed or implicit prior derivations remain possible.

## References

[1] Ofir Gorodetsky, *Statistics of entries of matrices from the general linear group over a finite field*, arXiv:2610.29305v1 (first public 2026-10-21), https://arxiv.org/html/2610.29305v1.

[2] Yan Li and Su Hu, *Gauss sums over some matrix groups*, arXiv:1105.4513v1 (2011), https://arxiv.org/abs/1105.4513.
