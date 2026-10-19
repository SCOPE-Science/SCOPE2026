# Subgroup meet profiles and intersection-graph degree spectra of scalar Frobenius groups

## Finding

Let \(p\) be an odd prime, \(n\ge 2\), and \(m>1\) a divisor of \(p-1\). Fix a scalar \(\lambda\in\mathbb F_p^\times\) of order \(m\), and let \(G=V\rtimes\langle\lambda\rangle\), where \(V=\mathbb F_p^n\) is additive and the complement acts by scalar multiplication. Let \(\Gamma(G)\) have the proper nonidentity subgroups as vertices, two distinct vertices being adjacent when their intersection is nonidentity.

This theorem gives (i) the complete joint distribution of subgroup dimensions, complement orders, and *orders of pairwise intersections*; and (ii) the resulting complete vertex-degree polynomial of \(\Gamma(G)\), for every indicated \(p,n,m\). The explicit formulas require only Gaussian coefficients, powers of \(p\), and divisors of \(m\).

Put \(\mathcal D=\{d\in\mathbb N:d\mid m\}\), \(\tau=|\mathcal D|\), and use \({a\brack b}_p\) for the Gaussian binomial coefficient (zero outside \(0\le b\le a\)). A subgroup has a unique *type* \((k,d)\), where \(k\) is its kernel-intersection dimension and \(d\in\mathcal D\) is the order of its image in the scalar complement. Exactly
\[
M_{k,d}={n\brack k}_p\,p^{(n-k)\mathbf 1_{d>1}}
\]
subgroups have type \((k,d)\).

**Ordered-pair meet spectrum.** Define
\[
S_{k,\ell,r}={n\brack k}_p{k\brack r}_p{n-k\brack \ell-r}_p
p^{(k-r)(\ell-r)},
\quad \max(0,k+\ell-n)\le r\le\min(k,\ell).
\]
For every \(d,e\in\mathcal D\), put \(T_{k,\ell,d,e}=p^{(n-k)\mathbf 1_{d>1}+(n-\ell)\mathbf 1_{e>1}}\). If \(d,e>1\) and \(g=\gcd(d,e)>1\), there are exactly
\[
S_{k,\ell,r}\,p^{n-r}
\]
ordered pairs \((H,K)\) with types \((k,d),(\ell,e)\), \(\dim((H\cap V)\cap(K\cap V))=r\), and \(|H\cap K|=p^rg\). Exactly \(S_{k,\ell,r}(T_{k,\ell,d,e}-p^{n-r})\) remaining ordered pairs with those types have intersection order \(p^r\). In all other cases, every one of the \(S_{k,\ell,r}T_{k,\ell,d,e}\) ordered pairs has intersection order \(p^r\). Terms with impossible indices are zero. The two cases exhaust *all* ordered subgroup pairs, including trivial and whole-group subgroups.

**Vertex-degree polynomial.** Let
\[
B=\sum_{j=0}^{n}{n\brack j}_p(1+(\tau-1)p^{n-j}),
\qquad
c(d)=\begin{cases}0&d=1,\\
|\{e\mid m:e>1,\ \gcd(d,e)>1\}|&d>1.
\end{cases}
\]
Define
\[
Z(k,d)=\sum_{j=0}^{n-k}{n-k\brack j}_p p^{kj}
\bigl(1+(\tau-1)p^{n-j}-c(d)p^k\bigr).
\]
Then every proper nonidentity subgroup of type \((k,d)\) has degree precisely \(B-Z(k,d)-2\), and the full degree-generating polynomial is
\[
\boxed{\displaystyle
D_{p,n,m}(t)=\!
\sum_{\substack{0\le k\le n,\ d\mid m\\
(k,d)\ne(0,1),(n,m)}}
{n\brack k}_p p^{(n-k)\mathbf 1_{d>1}}
 t^{B-Z(k,d)-2}.}
\]
Here the exclusions remove only the identity subgroup and the whole group. In particular, the degree polynomial determines the number of edges by \(D'_{p,n,m}(1)/2\).

For \((p,n,m)=(3,2,2)\), one gets \(D_{3,2,2}(t)=13t^4+13t^{16}\), and for \((3,3,2)\) one gets \(D_{3,3,2}(t)=40t^{26}+130t^{92}+40t^{182}\). Thus these naturally defined connected subgroup intersection graphs have markedly nonuniform degree spectra. For \((7,2,6)\), complementary subgroups of type \((0,2)\) have degree \(18\), while those of type \((0,6)\) have degree \(28\); complement-order arithmetic is visible in local graph degrees.

## Assumptions and scope

The kernel is the elementary abelian group of dimension \(n\) over the prime field. The complement has order \(m>1\), divides \(p-1\), and acts through a faithful *scalar*, not an arbitrary linear representation. All subgroups are actual embedded subgroups, not isomorphism classes. The graph excludes the trivial and whole subgroups and has no loops. Ordered-pair counts include ordered diagonal pairs \((H,H)\); the graph itself excludes such pairs. No assertion is made for non-scalar, reducible but nonhomogeneous, or irreducible higher-degree complement actions.

## Proof

**1. Parametrization of all subgroups.** Write group elements as \((v,\lambda^i)\), with \((v,a)(w,b)=(v+aw,ab)\). Any subgroup \(H\) meets \(V\) in an \(\mathbb F_p\)-subspace \(U\) of dimension \(k\), and its image in the cyclic complement is the unique subgroup \(C_d\) for some \(d\mid m\). Scalar action stabilizes all \(U\). For \(d>1\), the prime-to-\(p\) extension of \(U\) splits inside \(H\), and each complement acting on \(V/U\) is conjugate by a translation: a generator \((v,a)\), with \(a\ne1\), has the unique fixed point \((1-a)^{-1}v\) modulo \(U\). Hence
\[
H=U\rtimes C_d^{\,x}\quad\text{for a unique }x+U\in V/U.
\]
Conversely every such triple gives a subgroup. If \(d=1\), the subgroup is simply \(U\) and there is no translation choice. This proves the type multiplicities.

**2. Intersections of two subgroups.** Let \(U,W\) be their kernel subspaces, and set \(r=\dim(U\cap W)\). All common kernel elements form \(U\cap W\), of order \(p^r\). Their images in the complement intersect in the cyclic group of order \(g=\gcd(d,e)\). If \(g=1\), this is the whole intersection. If \(g>1\), their intersection projects onto the common complement precisely when their translated complement fixed-point cosets \(x+U\) and \(y+W\) intersect. Indeed, for any nonidentity \(a\in C_g\), the translation of its lift is \((1-a)x\) modulo \(U\), respectively \((1-a)y\) modulo \(W\). Since \(1-a\) is an invertible scalar, compatibility is equivalent to \(x-y\in U+W\), and then every element of \(C_g\) has a compatible lift. Therefore the intersection has order \(p^rg\) in the aligned case and \(p^r\) otherwise; intermediate complement orders cannot occur.

There are \(p^{n-k}\) choices of \(x+U\) and \(p^{n-\ell}\) choices of \(y+W\) when \(d,e>1\). For each fixed \(x+U\), exactly \(p^{\dim(U+W)-\ell}=p^{k-r}\) of the \(y+W\) cosets satisfy \(x-y\in U+W\). Thus exactly \(p^{n-r}\) ordered choices align. This proves the two lift-pair counts once the number of \((U,W)\) pairs is determined.

**3. Counting subspace pairs.** Choose \(U\) in \({n\brack k}_p\) ways; choose \(R=U\cap W\) inside \(U\) in \({k\brack r}_p\) ways; choose the \((\ell-r)\)-dimensional image of \(W\) in \(V/U\) in \({n-k\brack\ell-r}_p\) ways. For any such image, lifts of \(W/R\) are graphs of linear maps into \(U/R\), giving \(p^{(k-r)(\ell-r)}\) possibilities. Their product is \(S_{k,\ell,r}\), proving the meet spectrum.

**4. Counting disjoint subgroup partners.** Fix \(H\) of type \((k,d)\) with kernel \(U\). A subgroup \(K\) of type \((j,e)\) intersects \(H\) trivially only if \(W=K\cap V\) is disjoint from \(U\). For a given \(j\le n-k\) there are \({n-k\brack j}_p p^{kj}\) such \(W\). For each \(W\), there is one kernel-only subgroup of type \((j,1)\) and \(p^{n-j}\) choices for each \(e>1\). If \(d,e>1\) and \(\gcd(d,e)>1\), exactly \(p^k\) of those \(e\)-lifts intersect \(H\) in a nontrivial complement (the preceding aligned-coset count with \(r=0\), now keeping \(H\) fixed). Summing the \(\tau-1\) complement divisors and subtracting the \(c(d)\) forbidden classes gives exactly \(1+(\tau-1)p^{n-j}-c(d)p^k\) trivial-intersection partners for this \(W\). Summing over \(j\) proves \(Z(k,d)\). This count includes the trivial subgroup.

**5. From disjoint partners to degree.** Summing the subgroup multiplicities over all \(j,e\) gives \(B\). For each proper nonidentity \(H\), the \(B-Z(k,d)\) subgroups meeting \(H\) nontrivially include \(H\) itself and \(G\); both must be deleted from the graph-neighbor set. Therefore its degree is \(B-Z(k,d)-2\). Summing over all possible vertex types yields the stated polynomial.

## Verification

A standalone standard-library Python checker, `check_intersection_profile.py`, enumerates subspaces in reduced-row-echelon form, constructs the semidirect-product multiplication, and explicitly enumerates all subgroups in small instances. It compares actual vertex degrees with the closed formula for seven configurations, including \((p,n,m)=(3,3,2)\), and independently compares every ordered pair's intersection order with the proposed joint distribution in five configurations. The largest pair check has \(328^2=107584\) ordered pairs. In total 12 comparisons pass and the checker prints `ALL_INTERSECTION_PROFILE_CHECKS_PASSED 12`. These are finite tests; the preceding structural and Gaussian-counting proof is needed for the arbitrary-parameter theorem.

Run with `python3 check_intersection_profile.py`; no third-party packages are required.

## Relationship to prior work

Khudhur, Haji, and Khasraw (2021) study the intersection graph of dihedral groups with cyclic kernel of order the product of two distinct primes, obtaining metric and eccentricity invariants. Ramdani, Wardhana, and Awanis (2022) study related dihedral groups with cyclic prime-power kernels and numerical graph invariants. Neither inspected full article provides the Gaussian meet-order and full vertex-degree profile above, which concern elementary abelian kernels of rank at least two. Earlier general subgroup-intersection graph studies develop connectivity, girth, or group-characterization theory rather than this specific uniform distribution.

Lee and Rekvényi (2026), Lemma 2.2, provide a general criterion for diameter two in subgroup intersection graphs; it implies a diameter-two corollary for the present group family. Consequently no originality is claimed for any diameter-two assertion. The subgroup-commutativity and cyclic-subgroup graph literature uses *permutability* or different adjacency definitions and cannot imply this entire subgroup-meet census merely from its published numerical invariants.

## Limitations

Novelty is assessed only against accessible and searched literature, not certified historically. A derivation of the same meet profile from a previously published universal subgroup-lattice formula remains a possible overlap. The full text of every older related general group-intersection article could not be inspected; in particular, earlier general intersection-graph theory and unpublished subgroup-enumeration formulas remain residual risks. The result is not an assertion about arbitrary affine group actions or all Frobenius groups. No independent mathematical audit has been performed.

## References

1. P. M. Khudhur, R. R. Haji, S. M. S. Khasraw, *The Intersection Graph of Subgroups of the Dihedral Group of Order 2pq*, Iraqi Journal of Science 62 (2021), 4923–4929, doi:10.24996/ijs.2021.62.12.30. First public date verified from journal: 2021-12-30.
2. D. S. Ramdani, I. G. A. W. Wardhana, Z. Y. Awanis, *The Intersection Graph Representation of a Dihedral Group with Prime Order and Its Numerical Invariants*, BAREKENG 16 (2022), 1013–1020, doi:10.30598/barekengvol16iss3pp1013-1020.
3. M. Lee, K. Rekvényi, *On the Diameter of Intersection Graphs of Finite Groups*, Bulletin of the Australian Mathematical Society, published online 2026-09-24, Cambridge Core identifier CF895A249313C0DD3C8AE5EDDBC2D67D, Lemma 2.2.
4. S. Akbari, F. Heydari, M. Maghasedi, *The intersection graph of a group*, Journal of Algebra and Its Applications 14 (2015), article 1550065, doi:10.1142/S0219498815500656. General background on the invariant; only bibliographic abstract and derived summaries were accessible in this comparison.
