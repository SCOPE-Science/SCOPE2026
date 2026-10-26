# Joint rank, domain, and image-block spectrum of uniform-partition partial idempotents

## Finding
Fix an integer \(n\ge1\). On a labeled set \(X\) partitioned into \(m\ge0\) distinguishable classes of size \(n\), let \(P_{m,n}\) be the monoid of all partial maps preserving the equivalence relation. Write \(E_{m,n}=\{f\in P_{m,n}:f^2=f\}\). For \(f\in E_{m,n}\), put \(r(f)=|\operatorname{im}f|\), \(d(f)=|\operatorname{dom}f|\), and \(k(f)\) equal to the number of partition classes that meet its image. Set
\[
F_{m,n}(t,u,v)=\sum_{f\in E_{m,n}}t^{r(f)}u^{d(f)}v^{k(f)}.
\]
The complete trivariate distribution is given, as an identity of formal power series with polynomial coefficients, by
\[
\boxed{\displaystyle
\sum_{m\ge0}F_{m,n}(t,u,v)\frac{z^m}{m!}
=\exp\!\left(z+vz\sum_{s=1}^{n}\binom ns(tu)^s(1+su)^{n-s}\exp\!\left(z\bigl((1+su)^n-1\bigr)\right)\right).}
\]
In particular, for every \(m\ge1\),
\[
[t]F_{m,n}(t,u,1)=mn\,u(1+u)^{mn-1}.
\]
For \(m\ge1\) and \(n\ge2\), exactly \(mn^2\) idempotents have image rank \(mn-1\); the rank-\(mn\) idempotent is uniquely the identity. The coefficient of \(u^{mn}\) recovers the previously studied enumeration of **full** uniform-partition-preserving idempotents and is not asserted to be new.

## Assumptions and scope
A partial transformation is a map \(f:D\to X\) with arbitrary \(D\subseteq X\), including the empty map. It preserves the partition if every two defined points in one class have images in a common class. Its square is the ordinary partial composition; an idempotent satisfies \(f^2=f\). All blocks and underlying points are individually labeled. The variable \(t\) marks total image rank, \(u\) marks domain size, and \(v\) marks the number of blocks containing an image point. The formula holds for all integers \(m\ge0\) and \(n\ge1\), with \(F_{0,n}=1\). Coefficient extraction is formal in \(z\); no convergence assumption is made.

## Proof
**Fixed-image lemma.** If \(f^2=f\) is a partial map, then every \(y\in\operatorname{im}f\) belongs to its domain and satisfies \(f(y)=y\). Conversely, if every defined point maps to a fixed point, then \(f^2=f\). This follows immediately by applying the equation to any defined \(x\), since \(f(f(x))=f(x)\).

Call a partition class *rooted* if it contains at least one image point. Suppose a rooted class contains exactly \(s\) image points, where \(1\le s\le n\). These points must be fixed. The remaining \(n-s\) points may each either be undefined or be defined with image any of the \(s\) fixed points **in that same class**: preservation forces all points defined in a rooted class to map into its own class. Consequently the entire root-class weight (without its block-label factor) is
\[
w_s(t,u)=\binom ns(tu)^s(1+su)^{n-s}.
\]
A class that contains no image points may not map to itself on a nonempty domain: its images would then have to be fixed points in that class. If its domain is nonempty, preservation forces all its defined points to map into one particular rooted class, and each has \(s\) choices of fixed image points there. For a chosen root with \(s\) fixed points, the weight of such a *satellite* class is
\[
a_s(u)=(1+su)^n-1,
\]
where subtraction removes the empty-domain choice. A class with empty domain contributes a separate isolated component of weight \(z\).

This description is a reversible decomposition of an idempotent into unordered components: each rooted class (with \(s\) fixed image points) together with every nonempty-domain class mapping to it forms a rooted star; all completely undefined classes form isolated one-block components. There is no ambiguity in the root of any satellite because it has nonempty domain and all its images lie in one root class. Conversely, independently selecting the fixed image set of each root, the allowed maps from each root and satellite, and the empty classes always produces a partition-preserving idempotent.

For a rooted star, the root's block-label contribution is \(z\), the factor \(v\) marks its one image-bearing class, and arbitrarily many independently labeled satellites contribute \(\exp(za_s(u))\) by the exponential formula. Summing over \(s\) gives
\[
C_n(z;t,u,v)=vz\sum_{s=1}^{n}w_s(t,u)\exp(za_s(u)).
\]
Unordered sets of these stars, together with isolated undefined classes, have exponential generating series \(\exp(z+C_n(z;t,u,v))\), which is precisely the asserted identity. The apparent factorial denominators disappear on extraction of \(m!\,[z^m]\), because this construction counts labeled set partitions of the given \(m\) blocks.

For the rank-one specialization, choose its sole image point in \(mn\) ways. It must be fixed; every other point independently may be undefined or map to that fixed point, with no further restriction. This yields \(mn\,u(1+u)^{mn-1}\). Finally, a rank-\(mn-1\) idempotent has exactly one nonfixed point. It can either be undefined (\(mn\) choices, giving domain size \(mn-1\)), or be defined and map to one of the other \(n-1\) fixed points in its own class (\(mn(n-1)\) choices, giving full domain). This proves \(mn^2\) for \(n\ge2\). At rank \(mn\), every point is fixed, leaving only the identity.

## Verification
The self-contained Python file `verify_uniform_partition_idempotents.py` computes the trivariate polynomials from the labeled-root-star recurrence and independently enumerates actual partial maps, tests partition preservation, tests the equation \(f^2=f\), and records all three parameters. Exact coefficient equality was checked for \((m,n)=(1,1),(1,4),(4,1),(2,2),(3,2),(2,3)\). Further values were checked at \((3,3),(4,2),(5,2),(2,5)\), including the rank-one and rank-\(mn-1\) formulas and the full-domain specialization. Run using `python3 verify_uniform_partition_idempotents.py`; no third-party libraries or downloaded datasets are needed. Successful completion prints `VERIFY_OK_UNIFORM_PARTITION_PARTIAL_IDEMPOTENT_TRIVARIATE`.

For example, \((m,n)=(2,2)\) has 76 partial idempotents, of which 21 are full-domain. The corresponding totals for \((m,n)=(3,2)\) are 1236 and 189; for \((m,n)=(2,3)\) they are 1291 and 256. These are finite consistency checks, not a replacement for the all-parameter proof.

## Relationship to prior work
Cicalò, Fernandes and Schneider [1] established the order, generator rank, wreath-quotient description and presentation of the same **partial** uniform-partition-preserving monoid, but the inspected main results do not enumerate its idempotents by the three statistics above. Dolinka and East [2, Proposition 11] enumerated idempotents in the corresponding **full** transformation monoid. Their formula supplies the \(u^{mn}\) specialization and is expressly credited, not claimed as new. The present trivariate formula includes strictly partial transformations and resolves the simultaneous image-rank, domain-size, image-block-support census. In particular, a total count or a full-domain specialization does not determine its other coefficients. The finite-case full-domain counts match their table.

## Limitations
The formula assumes equal block sizes and labeled points. It is an element count, not a count of conjugacy classes, generating sets, products of idempotents or nonuniform blocks. An equivalent historical presentation in less accessible literature remains a priority risk. The proof has received a self-review, not an independent mathematical audit. The standalone finite computations test only the stated finite parameter ranges.

## References
[1] S. Cicalò, V. H. Fernandes, C. Schneider, *Partial transformation monoids preserving a uniform partition*, arXiv:1210.4775v1 (17 October 2012); Semigroup Forum 90 (2015), 532–544. https://arxiv.org/abs/1210.4775

[2] I. Dolinka, J. East, *Idempotent generation in the endomorphism monoid of a uniform partition*, arXiv:1407.3312v1 (11 July 2014); Communications in Algebra 44 (2016), 5179–5198. https://arxiv.org/abs/1407.3312
