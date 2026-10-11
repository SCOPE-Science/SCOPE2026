# Orthogonal homology characters and quotient dichotomy for finite subset spheres

## Finding
For integers \(n\geq 2\) and \(d\geq 2\), let \(X_{n,d}=\operatorname{exp}_n(S^d)\) be the space of nonempty subsets of the unit sphere in \(\mathbb R^{d+1}\) having cardinality at most \(n\). The orthogonal group \(O(d+1)\) acts by applying an isometry to each point. Write \(\delta\) for the one-dimensional rational orientation character \(g\mapsto\det(g)\).

**Theorem.** As graded rational \(O(d+1)\)-representations, all reduced homology vanishes except for the following one-dimensional groups:

For **even** \(d\),
\[
\widetilde H_{nd}(X_{n,d};\mathbb Q)\cong\delta^{\otimes n},\qquad
\widetilde H_{(n-1)d}(X_{n,d};\mathbb Q)\cong\delta^{\otimes(n-1)}.
\]
For **odd** \(d\geq3\), put \(a=\lceil n/2\rceil\) and \(t=a(d+1)-1\). Then
\[
\widetilde H_t(X_{n,d};\mathbb Q)\cong\delta^{\otimes a}.
\]

**Finite orthogonal quotients.** Let \(G\) be any finite subgroup of \(O(d+1)\), and put \(Y_{n,d,G}=X_{n,d}/G\). If every element of \(G\) preserves orientation, \(Y_{n,d,G}\) has precisely the same rational homology ranks as \(X_{n,d}\). If \(G\) contains an orientation-reversing element, the complete reduced rational homology of \(Y_{n,d,G}\) is as follows:

* For even \(d\), there is exactly one nonzero group, of rank one in degree \(nd\) when \(n\) is even, or degree \((n-1)d\) when \(n\) is odd.
* For odd \(d\geq3\), there is exactly one nonzero group, of rank one in degree \(t\), when \(n\equiv0,3\pmod4\). For \(n\equiv1,2\pmod4\), all reduced rational homology groups of the quotient vanish.

The quotient is not claimed to be contractible when rationally acyclic.

## Assumptions and scope
The topology on \(X_{n,d}\) is the quotient topology from \((S^d)^n\) under equality of the underlying *sets*, rather than equality of multisets. In particular it differs from a symmetric power for \(n\geq3\). Homology coefficients are \(\mathbb Q\) unless explicitly noted. The standard sphere is the unit sphere in \(\mathbb R^{d+1}\). A reflection is the restriction of a hyperplane reflection in the ambient Euclidean space. Quotients are topological orbit spaces, not homotopy orbit spaces. All statements quantify over every integer \(n\geq2\), every integer \(d\geq2\), and every finite subgroup \(G\leq O(d+1)\).

The nonequivariant rational Betti numbers are those of Mostovoy's Theorem 1 [1]. The new content concerns their induced orthogonal characters and rational homology of all finite orthogonal quotients.

## Proof
**1. Known dimensions.** By [1, Theorem 1], for even \(d\) the only nonzero positive-degree rational homology groups of \(X_{n,d}\) are one-dimensional in degrees \(nd\) and \((n-1)d\). For odd \(d>1\), the only such group is one-dimensional in degree \(t=\lceil n/2\rceil(d+1)-1\). For odd \(d\), \(t\) is odd. Consequently it remains to find the sign on each one-dimensional group.

**2. Reduction to a reflection.** The induced map on \(X_{n,d}\) varies continuously with an orthogonal transformation. The identity component \(SO(d+1)\) is path connected, so each of its elements acts homotopically to the identity. All elements of \(O(d+1)\) having determinant \(-1\) lie in its other path component and hence induce the same homology map as a fixed reflection \(r\). All possible actions are therefore signs determined by \(r\).

**3. Euler characteristic of the fixed subsets.** Write \(E=S^{d-1}\) for the equator fixed by \(r\), and let \(H\) be an open hemisphere. Then \(H\cong\mathbb R^d\). A nonempty finite subset invariant under \(r\) consists uniquely of \(j\) equatorial points and \(k\) unordered off-equator pairs, represented by \(k\) points of \(H\), with \(1\leq j+2k\leq n\). Its corresponding locally closed stratum is \(C_j(E)\times C_k(H)\), where \(C_q(Z)\) denotes the unordered configuration space of \(q\) distinct points of \(Z\) and \(C_0(Z)\) is a point.

For semialgebraic spaces, compact-support Euler characteristic is additive on finite locally closed decompositions and multiplicative on products. The standard unordered-configuration identity, proved by inclusion-exclusion on collisions and division by the free permutation action, is
\[
\sum_{q\geq0}\chi_c(C_q(Z))z^q=(1+z)^{\chi_c(Z)}.
\]
As \(\chi(E)=1+(-1)^{d-1}\) and \(\chi_c(H)=(-1)^d\), the generating function for Euler characteristics of reflection-invariant subsets with a *specified exact* total cardinality is
\[
F_d(z)=(1+z)^{1+(-1)^{d-1}}(1+z^2)^{(-1)^d}.
\]
It follows that
\[
F_d(z)=\begin{cases}
1+z^2,&d\text{ even},\\
(1+z)^2/(1+z^2),&d\text{ odd}.
\end{cases}
\]
The fixed-subset space \(X_{n,d}^{r}\) is compact and is the union of the strata whose total cardinalities lie between one and \(n\). Thus \(\chi(X_{n,d}^{r})=\sum_{q=1}^{n}[z^q]F_d(z)\). Evaluating the coefficients gives
\[
\chi(X_{n,d}^{r})=\begin{cases}
1,&d\text{ even},\\
2,&d\text{ odd and }n\equiv1,2\pmod4,\\
0,&d\text{ odd and }n\equiv0,3\pmod4.
\end{cases}
\]
The empty subset contributes the constant term and is excluded from this Euler characteristic.

**4. The homology signs.** The finite-order homeomorphism \(r\) admits an equivariant triangulation, so the Lefschetz number of \(r\) equals \(\chi(X_{n,d}^{r})\). The zero-degree trace is one because \(X_{n,d}\) is connected.

For odd \(d\), let \(\lambda\) be the sign of \(r\) on the unique one-dimensional homology group in odd degree \(t\). The Lefschetz equation reads \(1-\lambda=\chi(X_{n,d}^{r})\). Thus \(\lambda=-1\) for \(n\equiv1,2\pmod4\) and \(\lambda=+1\) for \(n\equiv0,3\pmod4\). This is exactly \(\lambda=(-1)^{\lceil n/2\rceil}\).

For even \(d\), the open dense stratum of \(n\) distinct points is an orientable \(nd\)-manifold \(C_n(S^d)\), since swapping two points has orientation sign \((-1)^d=+1\). Its complement has codimension at least \(d\geq2\), so its top fundamental class generates \(H_{nd}(X_{n,d};\mathbb Q)\) (also independently established in [1, Section 2.3]). An ambient orientation-reversing orthogonal transformation reverses the orientation in every one of the \(n\) coordinates. Hence its action on this generator is \((-1)^n\). If \(\mu\) denotes its sign on the other nonzero degree, the Lefschetz equation reads \(1+(-1)^n+\mu=\chi(X_{n,d}^{r})=1\). Therefore \(\mu=(-1)^{n-1}\). This proves the two asserted orthogonal characters.

**5. Finite orbit spaces.** The finite orthogonal action admits a triangulation whose barycentric subdivision has pointwise simplex stabilizers. Over \(\mathbb Q\), the quotient cellular cochain complex identifies with invariant cochains; equivalently, averaging is exact, and
\[
H^i(X_{n,d}/G;\mathbb Q)\cong H^i(X_{n,d};\mathbb Q)^G.
\]
The same rank conclusion holds for homology by duality of finite-dimensional rational vector spaces. If \(G\leq SO(d+1)\), every displayed character is trivial, and all groups survive. Otherwise \(G\) contains a determinant-minus-one element; a one-dimensional character \(\delta^{\otimes k}\) has nonzero invariants precisely when \(k\) is even. Keeping the even-exponent groups yields the stated degrees and the sharp modulo-four transition.

## Verification
The accompanying standalone Python file `verify.py` independently expands the reflection-fixed-stratum generating series using integer generalized binomial coefficients for all \(2\leq d\leq18\) and \(2\leq n\leq130\) (2,193 parameter pairs). For each, it checks the predicted exact fixed-point Euler characteristic, the signed Lefschetz equation, parity of the surviving quotient homology, and the Burnside Euler-characteristic identity
\[
2\chi(X_{n,d}/\langle r\rangle)=\chi(X_{n,d})+\chi(X_{n,d}^{r}).
\]
Run `python verify.py`; the observed result is `VERIFY_OK cases= 2193`. These finite checks are not used in place of the infinite proof above. Independent examples: \(\operatorname{exp}_2(S^2)=\mathbb{CP}^2\), on which reflection changes the generator in degree two by \(-1\) and the top generator by \(+1\), and Tuffley's degree formula for the excluded circle case [2] agrees with the odd-parity pattern.

## Relationship to prior work
Mostovoy [1, Theorem 1] gives exactly the nonequivariant rational homology ranks used in step 1. Its statement does not identify the \(O(d+1)\)-module or the rational homology of its finite isometry-group orbit spaces. Tuffley [2, Theorem 7] gives the map-degree formula for the circle case, hence that dimension is deliberately excluded. Tuffley [3, Theorems 1–2] calculates \(d=2\) rational homology and integral generators, giving some orientation information implicitly in that special dimension but not the full higher-dimensional parity dichotomy. The reflected configuration-stratum formula and consequent all-parameter quotient classification are what extend the cited literature. Related Euler-characteristic work [4] concerns ordinary Euler counts; a stronger, unindexed equivariant computation remains a possibility, not an asserted absence.

## Limitations
The classification is over \(\mathbb Q\). Rational acyclicity is not contractibility and does not rule out torsion. No integral module decomposition, equivariant homotopy splitting, classification of arbitrary self-maps of the sphere, or computation of homotopy orbit spaces is asserted. The known nonequivariant Betti numbers and standard Euler and Lefschetz identities are credited explicitly. Novelty searches cannot exclude unindexed or inaccessible equivalent treatments, especially in literature on equivariant Euler characteristics and finite-subset functors.

## References
1. Jacob Mostovoy, *Finite subset spaces of spheres*, arXiv:2603.01439v1 (first public 2026-03-02), Theorem 1 and Sections 2–4. https://arxiv.org/html/2603.01439v1
2. Christopher Tuffley, *Finite subset spaces of \(S^1\)*, Algebraic & Geometric Topology 2 (2002), 1119–1145; arXiv:math/0209077v3, especially the induced-map degree theorem. https://arxiv.org/html/math/0209077v3
3. Christopher Tuffley, *Finite subset spaces of closed surfaces*, arXiv:math/0311371v1 (2003), Theorems 1–2 and Section 3. https://arxiv.org/html/math/0311371v1
4. Walid Taamallah, *The Euler Characteristic of Finite Subset Spaces*, arXiv:2607.17830v1 (2026). Abstract available; full text not inspected, and no claim of complete noncoverage by the unseen text is made. https://arxiv.org/abs/2607.17830
