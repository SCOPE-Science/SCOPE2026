# Stationary commutative powers in finite magma monoids: an exact binomial rank law

## Finding

Fix an integer \(n\ge2\) and a labeled \(n\)-element set \(X\). Let \(\mathcal M(X)\) be the monoid of all binary operations on \(X\) under
\[
(f\triangleleft g)(a,b)=g(f(a,b),f(b,a)).
\]
An operation \(f\) is **stationarily commutative** if, for some integer \(k\ge1\), its power satisfies both \(f^{\triangleleft k}=f^{\triangleleft(k+1)}\) and \(f^{\triangleleft k}(a,b)=f^{\triangleleft k}(b,a)\) for every \(a,b\in X\). Let \(R(f)\) be the cardinality of the image of the stabilized power as a map \(X^2\to X\). Then \(1\le R(f)\le n\), and for every integer \(r\) with \(1\le r\le n\),
\[
\#\{f\in\mathcal M(X): f\text{ stationarily commutative},\ R(f)=r\}
=\binom nr\,r\,n^{n^2-r-2}.
\]
Equivalently, the exact rank-enumerator polynomial is
\[
\sum_{f\text{ stationarily commutative}}z^{R(f)}
=n^{n^2-n-1}z(n+z)^{n-1}.
\]
In particular, exactly \(n^{n^2-2}\) of the \(n^{n^2}\) binary operations have a stationary power that is a *constant* operation; their unconditional proportion is exactly \(1/n^2\). The proportion having any stationary commutative power is
\[
\frac{(n+1)^{n-1}}{n^{n+1}}\sim\frac{\mathrm e}{n^2}.
\]
Conditioned on being stationarily commutative, \(R(f)-1\) has precisely the binomial law \(\operatorname{Bin}(n-1,1/(n+1))\); hence it converges in distribution to \(\operatorname{Poisson}(1)\) as \(n\to\infty\).

## Assumptions and scope

The set \(X\) is fixed and labeled; all \(n^{n^2}\) maps \(X\times X\to X\) are counted individually, without identifying isomorphic magmas. The term *stationary* means consecutive semigroup powers eventually agree, not merely that a subsequence repeats or that one isolated power is commutative. In particular, powers with nontrivial periodic cycles are excluded, even when some periodically repeating power happens to be commutative.

Define \(Y=X^2\), the coordinate transposition \(\tau(a,b)=(b,a)\), the diagonal \(D=\{(a,a):a\in X\}\), and \(m=\binom n2\). The \(m\) remaining \(\tau\)-orbits each have size two. Write \(T_f(a,b)=(f(a,b),f(b,a))\). The rank \(R(f)\) is the number of diagonal fixed points reached in the stationary limit.

A further sharp bound holds. Writing \(h(f)\) for the least positive integer \(k\) satisfying \(f^{\triangleleft k}=f^{\triangleleft(k+1)}\), each stationarily commutative \(f\) satisfies
\[
1\le h(f)\le n+\binom n2-R(f).
\]
For each \(n\ge2\) and each admissible \(r\), this upper bound is attained by an operation of stabilized rank \(r\).

## Proof

**1. Equivariant transformation model and power criterion.** The identity \(T_{f\triangleleft g}=T_g\circ T_f\) is a direct substitution. Conversely, every self-map \(T:Y\to Y\) commuting with \(\tau\) has the unique form \(T=T_f\): its first coordinate defines \(f\) and equivariance forces the second. Thus \(T_{f^{\triangleleft k}}=T_f^k\).

A finite self-map has eventually stationary consecutive powers precisely when all its directed cycles are fixed points. Here a power \(f^{\triangleleft k}\) is commutative exactly when \(T_f^k(Y)\subseteq D\). Consequently, stationarity *and* commutativity are equivalent to the requirement that every directed cycle of \(T_f\) be a fixed point of \(T_f\) belonging to \(D\). Every trajectory then ends at a diagonal fixed point, and the stabilized image consists exactly of the \(r\) diagonal fixed points. Equivariance ensures that a non-diagonal fixed point would be accompanied by its reversed fixed point and is rightly excluded.

**2. The diagonal forest.** Choose its exact root set \(R\subseteq D\) of size \(r\). Restriction of \(T_f\) to \(D\) must be a directed rooted forest on \(n\) labeled vertices with those roots fixed, all other vertices pointing toward a root. The complete directed-forest matrix-tree formula gives
\[
F_{n,r}=\det(nI_{n-r}-J_{n-r})=r n^{n-r-1}
\]
when \(r<n\), where \(J\) is the all-ones matrix. Indeed, on the \(n-r\) nonroot vertices this matrix has eigenvalue \(r\) once and eigenvalue \(n\) with multiplicity \(n-r-1\). For \(r=n\), the unique diagonal map is the identity, and the displayed expression equals one as well. The statement can alternatively be obtained from the usual prescribed-root Cayley forest formula.

**3. The free-orbit forest.** Collapse each unordered off-diagonal pair \(\{(a,b),(b,a)\}\) to a vertex. An equivariant map from any such orbit to a diagonal point offers one choice per diagonal target. A map to a *different* free orbit offers exactly two choices, because the representative can map to either orientation of that target. Self-loops and all directed cycles among free orbits are forbidden by the criterion in Step 1.

Hence we must count directed forests from \(m\) free-orbit vertices to any of the \(n\) diagonal vertices, where each edge into a diagonal target has weight one, and each edge to a distinct free-orbit target has weight two. The weighted directed-forest matrix-tree theorem gives the determinant
\[
G_{n,m}=\det\big((n+2m)I_m-2J_m\big)
=n(n+2m)^{m-1}.
\]
The eigenvalues of this matrix are \(n\) once and \(n+2m\) with multiplicity \(m-1\). This determinant is independent of the chosen diagonal forest because all diagonal vertices are valid destinations and eventually reach the prescribed roots. Since \(m=\binom n2\ge1\), we have \(n+2m=n^2\).

The diagonal and off-diagonal choices are independent. For a fixed root set \(R\), the number of valid maps is therefore
\[
F_{n,r}G_{n,m}
=(r n^{n-r-1})\,n(n^2)^{m-1}
=r n^{n^2-r-2}.
\]
Selecting the root set in \(\binom nr\) ways proves the coefficient formula. The case \(r=n\) is included in the same expression, with the convention \(F_{n,n}=1\).

**4. Binomial law and rarity.** Factor the coefficient formula:
\[
\sum_{r=1}^n\binom nr r n^{n^2-r-2}z^r
=n^{n^2-2}\,z\left(1+\frac z n\right)^{n-1}.
\]
Dividing by its value at \(z=1\) yields \(z[(n+z)/(n+1)]^{n-1}\), the generating polynomial of one plus a \(\operatorname{Bin}(n-1,1/(n+1))\) variable. Its binomial-to-Poisson limit is standard because \((n-1)/(n+1)\to1\) and the success probability tends to zero. Taking \(r=1\) gives \(n^{n^2-2}\). Taking \(z=1\) and dividing by \(n^{n^2}\) gives the asserted proportion.

**5. Sharp depth.** The directed quotient forest has precisely \(n+m\) vertices, of which \(r\) are roots. Thus every orbit reaches a root after at most \(n+m-r\) steps, giving the claimed stationary-power bound. Choose one diagonal root, attach the remaining \(n-r\) nonroot diagonal vertices in one directed chain ending at that root, and attach all \(m\) free-orbit vertices in a single chain ending at the first diagonal vertex of that chain (or at the root when no nonroot diagonal vertices exist); hold the other \(r-1\) roots fixed. Choosing any allowed orientation for the free-orbit edges gives an equivariant transformation. Its maximal trajectory has exactly \(n+m-r\) edges, so the bound cannot be lowered.

## Verification

Run the included standard-library script `python verify.py`. It exhaustively enumerates every binary operation on labeled sets of sizes two and three (respectively \(16\) and \(19683\) operations). For every operation it independently computes successive products from the defining formula and checks the stabilization/commutativity predicate. Separately, it constructs \(T_f\) and checks its cycles. The two tests agree operation by operation. It obtains the complete per-rank counts \((4,2)\) at \(n=2\) and \((2187,1458,243)\) at \(n=3\), exactly as predicted. The run ends `VERIFY_OK`. These finite checks support but do not prove the all-parameter theorem; the determinant and cycle arguments above provide the proof.

## Relationship to prior work

Baiduk and Kozerenko (2026) identify the binary-operation monoid with equivariant transformations and develop its ideals, regularity, idempotents, and related enumeration. Their transformation representation is used here as a known starting point, not claimed as new. López-Permouth (2026) characterizes and enumerates operations already satisfying \(f\triangleleft f=f\); those idempotents need not be commutative, and the theorem here concerns *eventually stationary, commutative* powers of otherwise arbitrary operations. The present exact rank distribution, asymptotic rarity and binomial/Poisson law are not supplied by either inspected result.

The rooted-forest determinant and the binomial-to-Poisson limit are classical tools, not new lemmas. Existing general descriptions of finite transformation semigroups could imply analogous forest-counting methods; the specific equivariant rank formula is the additional combined assertion. A 2022 foundational magma-monoid article was consulted through its abstract and citation information rather than its full text, which remains an originality limitation.

## Limitations

Only finite labeled sets and consecutive-power stabilization are treated; the result does not classify powers having periodic, nonstationary eventual behavior. The number of *isomorphism classes* of operations is not computed. The exact stabilization-depth **distribution** is not determined, only its sharp maximum at each rank. The priority comparison is not exhaustive of older or unindexed literature; in particular the full text of the 2022 foundational article was not accessible. No claim of independent external validation is made.

## References

1. Y. Baiduk and S. Kozerenko, *Transformation Semigroup Perspective on the Magma Monoid*, arXiv:2607.13746, first posted 2026-07-15; Semigroup Forum **113** (2026), 335–356, doi:10.1007/s00233-026-10659-x.
2. S. R. López-Permouth, *Idempotent elements in binary and s-ary magma monoids*, São Paulo Journal of Mathematical Sciences **20** (2026), article 14, doi:10.1007/s40863-025-00519-x.
3. S. R. López-Permouth, I. Owusu-Mensah, and A. Rafieipour, *A monoid structure on the set of all binary operations over a fixed set*, Semigroup Forum **104** (2022), 667–688, doi:10.1007/s00233-022-10280-8 (abstract and bibliographic information inspected).
4. Directed matrix-tree and prescribed-root forest formulas (classical); used in weighted form as shown in the proof.
