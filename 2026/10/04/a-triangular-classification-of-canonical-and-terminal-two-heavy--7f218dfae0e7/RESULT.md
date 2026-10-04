# A triangular classification of canonical and terminal two-heavy weighted projective spaces
## Finding
Let \(r\ge 2\), let \(1\le a\le b\), put \(d=b-a\), and consider
\[
X_{r,a,b}=\mathbb P(\underbrace{1,\ldots,1}_{r},a,b).
\]
Then \(X_{r,a,b}\) has at worst canonical singularities if and only if
\[
d\le r\qquad\text{and}\qquad a\le r+d,
\]
and it has at worst terminal singularities if and only if
\[
d<r\qquad\text{and}\qquad a<r+d.
\]
Thus, at fixed \(r\), the canonical pairs \((a,b)\) form an integer triangle with exactly \(3r(r+1)/2\) points, while the terminal pairs number \(3r(r-1)/2\). Exactly \(3r\) canonical pairs are non-terminal; they are the union of the boundary families \(d=r\) and \(a=r+d\).

## Assumptions and scope
The base field is \(\mathbb C\). The integer \(r\) is at least \(2\), so \(X_{r,a,b}\) has dimension \(r+1\ge3\). Because at least two weights are \(1\), the weight vector is well formed. The statement concerns ordinary weighted projective spaces, not fake weighted projective spaces with additional finite class-group torsion.

## Proof
The charts corresponding to the unit weights are smooth. The two remaining affine charts are cyclic quotients of types
\[
\frac1a(\underbrace{1,\ldots,1}_{r},b)
\qquad\text{and}\qquad
\frac1b(\underbrace{1,\ldots,1}_{r},a).
\]
For a cyclic quotient \(\frac1m(1^r,c)\), the Reid--Tai criterion says that the \(k\)-th nontrivial group element has age
\[
\operatorname{age}_m(k)=\frac{rk+[kc]_m}{m},
\]
where \([u]_m\in\{0,\ldots,m-1\}\) is the least nonnegative residue. Canonicity requires every such age to be at least \(1\), and terminality requires every such age to be strictly greater than \(1\).

First suppose \(d=0\), so \(a=b\). Each heavy chart has type \(\frac1a(1^r,0)\), and its ages are \(rk/a\). Their minimum occurs at \(k=1\). Hence the space is canonical exactly when \(a\le r\), and terminal exactly when \(a<r\). These are precisely the asserted inequalities when \(d=0\).

Now suppose \(d>0\). On the \(b\)-chart, since \(a=b-d\), the age numerator is
\[
rk+[-kd]_b.
\]
At \(k=1\), canonicity forces \(d\le r\), and terminality forces \(d<r\). Conversely, if \(d\le r\) and \(rk<b\), then \(kd\le kr<b\), so \([-kd]_b=b-kd\), giving
\[
rk+[-kd]_b=b+k(r-d)\ge b.
\]
If \(rk\ge b\), the same age inequality is automatic. Replacing \(d\le r\) by \(d<r\) makes every inequality strict: when \(rk<b\) the displayed excess is positive, while when \(rk=b\) the residue is positive because \(d>0\) and \(kd<kr=b\). Thus the \(b\)-chart is canonical exactly when \(d\le r\), and terminal exactly when \(d<r\).

Assume henceforth the corresponding condition on \(d\). On the \(a\)-chart, the age numerator is
\[
rk+[kd]_a.
\]
For canonicity, if \(rk\ge a\) there is nothing to prove. If \(rk<a\), then \(kd\le kr<a\), so \([kd]_a=kd\), and the numerator is \(k(r+d)\). Therefore all ages are at least \(1\) exactly when \(a\le r+d\): necessity follows from \(k=1\) whenever \(a>r\), while if \(a\le r\) the inequality is automatic. For terminality, under \(d<r\), the same argument gives strict inequality exactly when \(a<r+d\). If \(rk=a\), equality cannot cause a failure: either \(d>0\), in which case \(0<kd<a\), or \(d=0\), which was already handled separately and forces \(a<r\).

Combining the two heavy charts proves the classification. For fixed \(r\), the canonical pairs are parametrized by
\[
0\le d\le r,\qquad 1\le a\le r+d,
\]
so their number is
\[
\sum_{d=0}^r(r+d)=\frac{3r(r+1)}2.
\]
The terminal pairs satisfy
\[
0\le d\le r-1,\qquad 1\le a\le r+d-1,
\]
and hence number \(3r(r-1)/2\). The difference is \(3r\). Equivalently, the canonical-but-not-terminal set is \(d=r\) or \(a=r+d\); inclusion--exclusion gives \(2r+(r+1)-1=3r\).

## Verification
The proof is symbolic and does not rely on enumeration. As a regression check, `verify_two_heavy_wps.py` independently compares the stated inequalities with both local Reid--Tai ages and Kasprzyk's global fractional-part criterion. It checks \(18{,}612\) parameter triples for \(2\le r\le12\), including a box extending beyond the feasible triangle, and checks the two counting formulas through \(r=30\). The script returns `VERIFY_OK`.

## Relationship to prior work
Kasprzyk's 2013 paper gives general fractional-part criteria for terminal and canonical weighted projective spaces and then performs exhaustive classifications in dimension four; it explicitly treats higher-dimensional classification as substantially harder. The present result is a closed-form all-dimensional specialization for the natural family with exactly two possibly non-unit weights. It replaces the many fractional-part tests by two linear inequalities and gives exact enumeration and boundary formulas.

Kasprzyk's 2008 work gives general weight-ratio bounds for terminal and canonical fake weighted projective spaces, while Ghirlanda's 2026 work gives a local age criterion and an all-dimensional classification algorithm for fake weighted projective spaces. The checked full texts do not state the two-heavy closed form above. Targeted searches also found related weighted-projective results on reflexive four- and six-dimensional families, but those concern Ehrhart or Gorenstein/reflexive restrictions and do not imply this classification.

## Limitations
This theorem does not classify weighted projective spaces with three or more non-unit weights, nor fake weighted projective spaces with nontrivial torsion. The literature comparison is necessarily a search-based originality assessment: no equivalent closed-form statement was located, but an equivalent result could exist under different notation. The finite checker is only a regression test and is not used as evidence for the infinite quantifiers in the theorem.

## References
1. A. M. Kasprzyk, *Classifying terminal weighted projective space*, arXiv:1304.3029, first posted 2013-04-10. https://arxiv.org/abs/1304.3029
2. A. M. Kasprzyk, *Bounds on Fake Weighted Projective Space*, arXiv:0805.1008, first posted 2008-05-07. https://arxiv.org/abs/0805.1008
3. M. Ghirlanda, *A canonicity criterion for toric varieties and the classification of canonical 4-simplices*, arXiv:2603.21198, 2026. https://arxiv.org/abs/2603.21198
4. M. Reid, *Young person's guide to canonical singularities*, Proc. Sympos. Pure Math. 46 (1987), 345--414.
