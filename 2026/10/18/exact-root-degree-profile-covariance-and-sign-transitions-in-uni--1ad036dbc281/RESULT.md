# Exact root–degree-profile covariance and sign transitions in uniform plane trees

## Finding

Let \(\mathcal T_n\) be uniform over rooted ordered (plane) trees on \(n\ge2\) vertices. Let \(R_n\) be the number of children of its root and let \(N_{n,k}\) count all vertices, including the root, with exactly \(k\) children, where \(0\le k\le n-1\). Define

\[
P_n(k)=(n^2+3n+2)k^2+(-5n^2+n+6)k+2n^2-6n+4.
\]

Then, **exactly at every finite size**,

\[
\boxed{\operatorname{Cov}(R_n,N_{n,k})
=\frac{n\binom{2n-k-3}{n-2}}{\binom{2n-2}{n-1}}\,
\frac{P_n(k)}{n(n-1)(n+1)}.}
\]

Because both \(\sum_{k=0}^{n-1}N_{n,k}=n\) and \(\sum_{k=0}^{n-1}kN_{n,k}=n-1\) hold deterministically, the profile covariances obey two balancing constraints; the theorem identifies all individual signs compatible with them.

The sign classification is complete. At \(n=2\), all covariances vanish. For \(n\ge3\), the covariance is positive for \(k=0\) and negative for \(k=1\). For \(k=2\) it is positive only at \(n=3\), negative thereafter; for \(k=3\) it is positive for \(4\le n\le7\), negative for \(n\ge8\); for \(k=4\) it is positive for \(5\le n\le24\), negative for \(n\ge25\). Every feasible \(k\ge5\) has positive covariance. These statements apply only when \(0\le k\le n-1\), and every listed nonzero sign is strict. For \(k\ge n\), \(N_{n,k}\) is identically zero.

For each **fixed** nonnegative integer \(k\),

\[
\lim_{n\to\infty}\operatorname{Cov}(R_n,N_{n,k})
=\frac{k^2-5k+2}{2^{k+1}}.
\]

## Assumptions and scope

Trees are unlabeled, rooted, and plane, with all possible finite ordered shapes equally likely. The root is a distinguished vertex; outdegree means number of children, **not** undirected graph degree. Every one of the \(C_{n-1}=\binom{2n-2}{n-1}/n\) shapes has probability \(1/C_{n-1}\). All moments and signs are exact finite-population identities, not asymptotic estimates.

## Proof

Let \(T=T(z)\) be the ordinary generating function for the trees, counted by vertices. Ordered sequences of child trees give \(T=z/(1-T)\), equivalently \(z=T(1-T)\), with \(T(0)=0\). To mark every vertex of outdegree \(k\), introduce \(v\) and define

\[
T(z,v)=\frac{z}{1-T(z,v)}+z(v-1)T(z,v)^k.
\]

Thus the extra summand marks the unique root offspring count, while each child subtree is recursively marked. To mark root outdegree by \(u\) independently, use

\[
F(z,u,v)=\frac{z}{1-uT(z,v)}+z(v-1)u^kT(z,v)^k.
\]

The normalizing coefficient \([z^n]F(z,1,1)\) is \(C_{n-1}\). Differentiating formally at \(u=v=1\) gives

\[
\left.\partial_u F\right|_{1,1}=\frac{T^3}{z},\qquad
\left.\partial_v F\right|_{1,1}
=\frac{T^{k+1}(1-T)^2}{1-2T},
\]

and, crucially,

\[
\left.\partial_u\partial_vF\right|_{1,1}
=\frac{T^{k+2}(1+T)}{1-2T}+kzT^k.
\]

The differentiations yield \(\mathbb E R_n\), \(\mathbb E N_{n,k}\), and \(\mathbb E(R_nN_{n,k})\) upon extracting \([z^n]\) and dividing by \(C_{n-1}\). Since \(dT/dz=(1-2T)^{-1}\), the first mixed term is the derivative of \(T^{k+3}/(k+3)+T^{k+4}/(k+4)\). Lagrange inversion supplies, for \(1\le j\le a\),

\[
[z^a]T^j=\frac{j}{a}\binom{2a-j-1}{a-j},
\]

with out-of-range binomials defined as zero. Consequently,

\[
[z^n]\partial_u\partial_v F
=\binom{2n-k-2}{n-k-2}+\binom{2n-k-3}{n-k-3}
+\frac{k^2}{n-1}\binom{2n-k-3}{n-k-1}.
\]

(The last summand is zero when \(k=0\).) Elementary binomial identities now yield

\[
\mathbb E R_n=\frac{3(n-1)}{n+1},\qquad
\mathbb E N_{n,k}=
\frac{n\binom{2n-k-3}{n-2}}{\binom{2n-2}{n-1}},
\]

\[
\mathbb E(R_nN_{n,k})=
\mathbb E N_{n,k}\cdot
\frac{(n-k-1)(3n-2k-4)+nk^2}{n(n-1)}.
\]

Subtract the product of expectations and put the result over the common denominator \(n(n-1)(n+1)\). The numerator simplifies to the displayed polynomial \(P_n(k)\); this proves the exact covariance for all stated indices, including the extremal case \(k=n-1\).

For sign analysis, direct factorization yields

\[
\begin{aligned}
P_n(0)&=2(n-1)(n-2),\\
P_n(1)&=-2(n-2)(n+3),\\
P_n(2)&=-4(n^2-2n-6),\\
P_n(3)&=-4(n^2-6n-10),\\
P_n(4)&=-2(n^2-23n-30),\\
P_n(5)&=2(n^2+37n+42).
\end{aligned}
\]

The given finite ranges follow by integer comparisons of the quadratic factors. Furthermore, \(P_n(k)\) is a convex quadratic in \(k\) whose derivative at \(k=5\) is \((n+1)(5n+26)>0\); hence \(P_n(k)>0\) for every \(k\ge5\). The factor \(\mathbb E N_{n,k}\) is strictly positive for all feasible \(k\). For fixed \(k\), \(\mathbb E N_{n,k}/n\to2^{-k-1}\) and \(P_n(k)/(n(n-1)(n+1))\sim(k^2-5k+2)/n\), proving the limit.

## Verification

The attached standard-library script `verify_plane_root_degree.py` enumerates every valid preorder outdegree word of every plane tree through \(n=11\). It independently recomputes the two means, mixed moment, covariance, and sign for every feasible degree. The exact-rational replay succeeds over 23,713 tree shapes and 45,489 checks, including a separate sweep of all feasible size/degree pairs through \(n=300\) and fixed-degree numerical limits. Execute `python3 verify_plane_root_degree.py`. Finite checks provide additional evidence; the unbounded result follows from the formal-series proof.

## Relationship to prior work

Janson's survey identifies uniform ordered trees as conditioned Galton–Watson/Catalan trees, obtains global offspring-profile limits and discusses the distinguished root's limiting degree; see Examples 9.1 and 11.3, Lemma 16.1 and §20.2. Those results do not themselves give the mixed finite-size covariance or its sign classification. The degree-profile allocation equivalence retains the global degree multiset but does not preserve the distinguished root under cyclic rotation.

Dershowitz and Zaks establish broad enumeration formulas for ordered-tree patterns and multisets of patterns, potentially relevant to mixed degree statistics. Their generic theorem is a genuine priority risk for derivability of the mixed moment after a suitable encoding of the root. Their inspected text does not explicitly give this root-versus-global covariance polynomial or the complete strict sign changes at sizes 8 and 25. The independent root/profile marking and exact sign analysis are the claims assessed here, **not** the separate known Catalan counts or individual degree marginals.

## Limitations

This theorem is limited to uniform ordered tree shapes. It does not assert the same signs for unordered, labeled, recursive or arbitrarily weighted conditioned trees. The constant-covariance limit is for fixed \(k\), not for degrees scaling with tree size. Independent historical priority review has not been performed; general pattern-enumeration results could make portions of the calculation recoverable as nontrivial specializations.

## References

1. S. Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, arXiv:1112.0510 (first public version 2011-12-02), https://arxiv.org/html/1112.0510v1.
2. N. Dershowitz and S. Zaks, *Patterns in Trees*, MIT-LCS-TM-271, 1984/1985, https://groups.csail.mit.edu/tds/papers/Zaks/TM-271.pdf.
3. N. Dershowitz and S. Zaks, *Enumerations of Ordered Trees*, Discrete Mathematics 31 (1980), 9–28.
4. K. O. Lumumba, I. O. Okoth and D. M. Kasyoki, *Refined Enumeration of 2-Plane Trees*, European Journal of Mathematics and Applications 5:8 (2025), https://ejma.euap.org/contents/ejma20250508.pdf.
