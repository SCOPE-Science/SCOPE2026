# Embedded cyclic submonoids of finite full transformation monoids: exact refined enumeration and asymptotic generator uniqueness

## Finding
For every integer \(n\ge1\), let \(T_n\) be the monoid of all functions \([n]\to[n]\) under composition, let \(1_n\) be its identity, and let
\[
M_n=\bigl|\{\{1_n,f,f^2,\ldots\}:f\in T_n\}\bigr|.
\]
These are distinct **embedded subsets** of \(T_n\), not isomorphism classes or conjugacy classes. For a permutation \(\sigma\), let \(o(\sigma)\) be its order, with \(\varphi\) denoting Euler's totient (including \(\varphi(1)=1\)). Then
\[
\boxed{M_n=n^n-\sum_{k=1}^{n}\binom nk k^{n-k}\sum_{\sigma\in S_k}\left(1-\frac1{\varphi(o(\sigma))}\right).}
\tag{1}
\]
The summand over permutations can equally be computed by integer partitions: if \(\lambda\vdash k\) has \(a_j\) parts of size \(j\), set \(z_\lambda=\prod_{j\ge1}j^{a_j}a_j!\) and \(p_\lambda=\operatorname{lcm}\{j:a_j>0\}\). Then replace the permutation sum in (1) by
\[
\sum_{\lambda\vdash k}\frac{k!}{z_\lambda}\left(1-\frac1{\varphi(p_\lambda)}\right).
\]
The first ten values of \(M_n\), for \(n=1,\ldots,10\), are
\[
1,\ 4,\ 26,\ 237,\ 2842,\ 42488,\ 759166,\ 15712098,\ 368357033,\ 9630273372.
\]
More precisely, let \(h(f)\) be the maximal distance in the functional digraph of \(f\) from a vertex to a periodic cycle and let \(p(f)\) be the least common multiple of its cycle lengths. Put \(R_0(z)=z\) and \(R_h(z)=z\exp(R_{h-1}(z))\) for \(h\ge1\), and for positive \(d\) set
\[
F_{h,d}(z)=\exp\!\left(\sum_{j\mid d}\frac{R_h(z)^j}{j}\right),\qquad F_{-1,d}(z)=0.
\]
For \(h\ge0\) and \(p\ge1\), the number \(N_{n,h,p}\) of transformations having exact parameters \((h,p)\) is
\[
\boxed{N_{n,h,p}=n![z^n]\sum_{d\mid p}\mu(p/d)\bigl(F_{h,d}(z)-F_{h-1,d}(z)\bigr).}
\tag{2}
\]
The number of *distinct* embedded singly generated submonoids with these parameters is exactly
\[
\boxed{M_{n,h,p}=\begin{cases}N_{n,h,p}/\varphi(p),&h=0\text{ or }1,\\N_{n,h,p},&h\ge2.\end{cases}}
\tag{3}
\]
All such parameters are intrinsic to the generated submonoid (equivalently, invariant over its possible generators), and \(M_n=\sum_{h,p}M_{n,h,p}\).

If \(\rho\) is the unique positive solution of \(\rho e^\rho=1\) (so \(\rho=W(1)\)), the duplicate-generator deficit has the sharp asymptotic
\[
\boxed{n^n-M_n\sim\frac{n!\,\rho^{-n}}{1+\rho}.}
\tag{4}
\]
Consequently
\[
\frac{n^n-M_n}{n^n}\sim\frac{\sqrt{2\pi n}}{1+\rho}\left(\frac1{e\rho}\right)^n\longrightarrow0.
\]
Thus, a uniformly random self-map almost surely generates a cyclic submonoid with no other generator; the exceptional probability has the same displayed sharp asymptotic. The equality of the two asymptotics, rather than of the exact counts, is proved below.

## Assumptions and scope
Throughout, \(n\ge1\) and \([n]=\{1,\ldots,n\}\). Composition of self-maps is the usual associative operation, and the adjoined identity \(1_n\) is always included in \(\langle f\rangle_1\), even when \(f\) is noninvertible. Do not confuse this convention with the positive-power-only semigroup \(\{f,f^2,\ldots\}\). Every finite functional digraph has a unique decomposition into directed cycles decorated by in-trees. A vertex is periodic precisely when it lies on one of those cycles. The height \(h(f)\) is \(0\) for a permutation. The period \(p(f)\) is \(1\) for a map having only fixed-point cycles. The formal power-series variables are ordinary indeterminates and \(n![z^n]\) converts an exponential generating function coefficient into a count of labeled maps.

## Proof
**Generator fibers.** Fix \(f\in T_n\), and write \(h=h(f)\), \(p=p(f)\). Standard functional-digraph dynamics, verified directly by the paths into the cycles, implies that \(f^{h+p}=f^h\) and that the first repeat of the nonnegative-power sequence occurs at exponents \(h\) and \(h+p\). In particular, \(f^1\ne f^r\) for every integer \(r\ge2\) when \(h\ge2\). Any generator \(g\) for \(\langle f\rangle_1\) is itself a power \(f^a\) for some \(a\ge0\). If \(h\ge2\), the case \(a=0\) gives only the trivial submonoid; if \(a\ge2\), every nonidentity positive power of \(g\) has exponent at least two and cannot equal \(f\). Thus \(g=f\), showing uniqueness. If \(h=0\), \(f\) is a permutation of order \(p\) and exactly \(\varphi(p)\) powers generate its cyclic group. If \(h=1\) and \(f\) is not a permutation, its nonidentity powers \(\{f,f^2,\ldots,f^p\}\) form a cyclic group of order \(p\), with identity \(f^p\) distinct from \(1_n\); a power \(f^a\) generates the entire ambient-identity-containing submonoid if and only if \(\gcd(a,p)=1\). There are exactly \(\varphi(p)\) such powers. Every such generator has the same height and period. This proves (3).

**Exact total.** The maps of height at most one have a uniquely determined nonempty set \(C\) of cyclic vertices. If \(|C|=k\), choose \(C\) in \(\binom nk\) ways, permute it arbitrarily in \(k!\) ways, and map each of the \(n-k\) remaining vertices independently to any element of \(C\), in \(k^{n-k}\) ways. All these maps have height zero or one, and their period is the order of the permutation on \(C\). Every other map, with height at least two, contributes one distinct submonoid for each of its \(n^n-\sum_{k=1}^n\binom nk k!k^{n-k}\) generators. Weighting each height-at-most-one map by the inverse of its fiber size \(\varphi(p)\) yields precisely (1). The partition expression follows because there are \(k!/z_\lambda\) permutations of cycle type \(\lambda\).

**Complete parameter refinement.** A rooted in-tree with root at a specified cycle vertex and all nonroot vertices at distance at most \(h\) from the root has exponential generating series \(R_h\): its root uses one label and its children form an unordered labeled set of rooted trees of height at most \(h-1\). Each directed functional-digraph cycle of length \(j\) therefore has exponential series \(R_h^j/j\). Restricting the cycle length \(j\) to divisors of \(d\) and freely taking a set of components gives \(F_{h,d}\). Its coefficient \(n![z^n]\) counts exactly the maps with \(h(f)\le h\) and \(p(f)\mid d\). Möbius inversion on the divisor lattice isolates exact period \(p\), and subtracting heights at most \(h-1\) isolates exact height \(h\), producing (2). Dividing by the fiber size proved above yields (3) and its summation to (1). Every coefficient is finite, and no assumptions on the possible order of \(p\) beyond finiteness are needed.

**Sharp rarity asymptotic.** Let \(H_n\) be the number of maps of height at most one, and let \(G_n\) be their total inverse-generator-fiber weight. Then \(n^n-M_n=H_n-G_n\). The labeled exponential formula and the direct count above give
\[
\sum_{n\ge0}H_n\frac{z^n}{n!}=\frac1{1-z e^z},
\]
with the harmless empty transformation contributing the constant term. The smallest-modulus singularity is the unique real positive \(\rho\) satisfying \(\rho e^\rho=1\). Indeed, \(|z e^z|\le|z|e^{|z|}\), with equality at modulus \(\rho\) only for \(z=\rho\). Its simple-pole principal part is
\[
\frac1{1+\rho}\frac1{1-z/\rho},
\]
so singularity analysis gives \(H_n\sim n!\rho^{-n}/(1+\rho)\).

It remains essential to show \(G_n=o(H_n)\), rather than guessing that the inverse-totient weight is small. Fix an integer \(B\ge1\). Only finitely many positive integers \(p\) satisfy \(\varphi(p)\le B\), since \(\varphi(p)\to\infty\). Choose \(D\) divisible by all of them. Height-at-most-one maps whose period lies in that finite set are a subset of maps all of whose cycle lengths divide \(D\). The latter class has exponential generating function
\[
\exp\!\left(\sum_{j\mid D}\frac{(z e^z)^j}{j}\right),
\]
which is entire. By Cauchy's bound on any circle of radius \(R>\rho\), the number of these maps is \(O_R(n! R^{-n})=o(H_n)\). Every other height-at-most-one map has inverse-totient weight at most \(1/B\). Therefore \(0\le G_n/H_n\le o(1)+1/B\). Sending \(n\to\infty\), then \(B\to\infty\), proves \(G_n/H_n\to0\). Combining this with the pole estimate proves (4). A map has another generator for the same submonoid exactly if \(h(f)\le1\) and \(arphi(p(f))>1\); because \(arphi(p)=1\) holds only for \(p=1,2\), the maps in the height-at-most-one class without a second generator have an entire exponential generating function \(\exp((ze^z)+(ze^z)^2/2)\). As above, their count is \(o(H_n)\). Hence the actual number of maps having at least one other generator is \(\sim H_n\sim n^n-M_n\), although these two statistics are not exactly equal. Stirling's formula now gives both the displayed deficit proportion and the stated exceptional probability.

## Verification
The standalone `check_monogenic.py` performs two logically different calculations for each \(1\le n\le6\): direct enumeration of all \(n^n\) maps and their literal power-set submonoids, and independent exact rational series for every nonzero \((h,p)\) via (2)–(3). It verifies the complete parameter-distribution equality, the number of distinct submonoids, and individual generator-fiber sizes. The direct totals are \(1,4,26,237,2842,42488\). The independent `verify_partition.py` evaluates (1) using permutation conjugacy types and integral rational arithmetic through \(n=18\), checking the common small-size sequence and producing additional values. Both scripts use Python's standard library and can run independently from their own directory: `python3 check_monogenic.py` and `python3 verify_partition.py`. Their tests are finite corroboration; the general formulas and asymptotics are established by the proof, not by extrapolating test outcomes.

## Relationship to prior work
Elliott, Levine, and Mitchell (2023, arXiv:2303.12387) count **isomorphism classes** of monogenic transformation submonoids in terms of allowable periods and thresholds. That result characterizes which abstract monogenic monoids embed, but an isomorphism-class count does not specify how many distinct subsets of the ambient \(T_n\) realize each type. The present exact formulas count the actual embedded subsets and resolve the nonconstant generator-fiber issue; the complete height/period multiplicities and their asymptotic consequence are not implied by the published isomorphism-type count.

Earlier general enumeration of subsemigroups of small transformation semigroups (East, Egri-Nagy, and Mitchell, 2017) provides finite-degree context, but does not furnish (1)–(4) for arbitrary degree. Related enumeration of polymorphism-homogeneous finite monounary algebras yields the same analytic factor \(1/(1-z e^z)\) as one of its components; this is an overlap in the auxiliary *height-at-most-one mapping class*, not an enumeration of generated submonoids, their Euler-totient generator fibers, or the deficit \(n^n-M_n\). The analytic pole calculation is standard and is not asserted to be independently novel.

## Limitations
The originality comparison is bounded by the literature and indexed records searched. An equivalent count could exist under the language of cyclic transformation subsemigroups or functional-digraph generator equivalence, and a direct matching sequence-table search was inconclusive; these are residual originality risks, not proved absences. The exact counts concern submonoids containing the ambient identity, not positive-power-only subsemigroups, and concern full transformations, not partial transformations or conjugacy classes. Although the results are proved for every finite degree, direct exhaustive cross-checking ended at degree six. No independent audit has been performed.

## References
1. L. Elliott, A. Levine, J. D. Mitchell, “Counting monogenic monoids and inverse monoids,” Communications in Algebra 51 (2023), 4654–4661, DOI: 10.1080/00927872.2023.2214821; arXiv:2303.12387, initial version publicly posted 22 March 2023. Primary MSC2020: 20M20.
2. J. East, A. Egri-Nagy, J. D. Mitchell, “Enumerating transformation semigroups,” Semigroup Forum 95 (2017), 109–125, DOI: 10.1007/s00233-017-9869-2; arXiv:1403.0274.
3. “Labeled enumeration and asymptotic rarity of finite polymorphism-homogeneous monounary algebras” (2026), publicly available mathematical result; compared for the shared height-one EGF component, not for the distinct-submonoid claim.
4. P. Flajolet, R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), for standard labeled combinatorial constructions and singularity analysis.
