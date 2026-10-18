# Complete ternary-convolution nullity laws on finite dihedral groups

## Finding
For every integer \(n\ge3\), write \(D_{2n}=\langle r,s\mid r^n=s^2=e,\ srs=r^{-1}\rangle\). For every three-element subset \(A\subset D_{2n}\), let \(T_A\) be convolution by \(1_A\) on \(\mathbb C[D_{2n}]\), or equivalently left multiplication by \(\sum_{a\in A}a\). Its complex nullity is governed by the following exhaustive alternatives.

**Pure type.** If all three elements lie in the rotation coset or all in the reflection coset, write their exponents \(u,v,w\in\mathbb Z_n\), set \(g=\gcd(n,u-v,u-w)\), and let \(q=n/g\). The nullity is \(4g\) exactly when \(3\mid q\) and \(\{0,(v-u)/g,(w-u)/g\}\) represents all three residues modulo \(3\). Otherwise it is zero. The integer quotients are well defined because \(g\) divides both differences.

**Mixed type.** If precisely two elements belong to one coset and one to the other, let \(d\) be the difference of the exponents of the same-coset pair, \(g=\gcd(n,d)\), and \(q=n/g\). The nullity is \(2g\) exactly when \(3\mid q\); otherwise it is zero. Both mixed orientations obey the same law.

Thus **every such convolution is invertible for every three-element support** exactly when \(3\nmid n\). More precisely, if \(v=v_3(n)\), \(m=n/3^v\), then the number of singular operators among the \(\binom{2n}{3}\) unordered three-element supports is
\[
\boxed{\displaystyle S(n)=n^2(n-m)+\frac{n^3}{12}(1-3^{-2v}).}
\]
Here \(v=0\) gives \(S(n)=0\). The formula includes supports containing the identity; no symmetry or generating hypothesis is imposed.

The **entire nonzero-nullity multiplicity distribution** is also explicit. For each positive divisor \(g\mid n\) with \(q=n/g\) divisible by \(3\), there are exactly
\[
\boxed{\displaystyle n^2\varphi(q)}
\]
mixed supports of nullity \(2g\), and exactly
\[
\boxed{\displaystyle \frac{2nq^2}{27}\prod_{\substack{\ell\mid q\\\ell\ne3\ \mathrm{prime}}}(1-\ell^{-2})}
\]
pure supports of nullity \(4g\). An empty product is one. Counts from the two families are added when their numerical nullities coincide. All remaining supports have nullity zero.

For example, \(S(3)=20\), \(S(6)=160\), \(S(9)=708\), and \(S(12)=1280\). These counts are among respectively \(20,220,816,2024\) possible three-element supports.

## Assumptions and scope
All group elements are distinct and have coefficient \(1\) in the convolution kernel. Multiplication is \((r^a s^\epsilon)(r^b s^\delta)=r^{a+(-1)^\epsilon b}s^{\epsilon+\delta}\), with exponents taken modulo \(n\). Left convolution on the regular representation is used; right convolution has the same nullity. The theorem is for every \(n\ge3\), including composite, even, and prime-power \(n\), and does not assert the same result for arbitrary complex coefficients or general finite groups.

## Proof
Let \(\zeta=e^{2\pi i/n}\). Every one-dimensional character of the dihedral group takes values in \(\{1,-1\}\); its sum on exactly three group elements is nonzero. The two-dimensional irreducible representations are indexed by \(1\le k<n/2\) and satisfy
\[
\rho_k(r)=\begin{pmatrix}\zeta^k&0\\0&\zeta^{-k}\end{pmatrix},\qquad
\rho_k(s)=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Each two-dimensional representation appears twice in the regular representation. When \(n\) is even, the excluded \(k=n/2\) character is one-dimensional; its three-sign sum also cannot vanish.

For a pure rotation triple, the Fourier block is diagonal with entries \(U_k=\zeta^{ku}+\zeta^{kv}+\zeta^{kw}\) and \(\overline U_k\). For a pure reflection triple it is off-diagonal with those entries. Either block has rank zero exactly when \(U_k=0\), and rank two otherwise. Three unit complex numbers sum to zero precisely when they are the three equally spaced cube roots multiplied by a common unit scalar. Set \(g=\gcd(n,u-v,u-w)\); the subgroup \(\langle r^{v-u},r^{w-u}\rangle\) has order \(q=n/g\). Its restriction character must have order exactly three and the two generators must map to the two different nontrivial cube roots. Such characters exist exactly under the stated residue condition. There are two on the generated cyclic subgroup, each with exactly \(g\) extensions to \(\langle r\rangle\), hence precisely \(2g\) zero Fourier frequencies. All come in distinct \(\{k,-k\}\) pairs and each zero two-dimensional block contributes four to the regular nullity. The result is \(4g\).

For a mixed triple with two rotations at exponents \(a,c\) and one reflection at exponent \(b\), the Fourier block has determinant
\[
\left|\zeta^{ka}+\zeta^{kc}\right|^2-1
=1+2\cos\!\left(\frac{2\pi k(a-c)}n\right).
\]
For one rotation and two reflections the determinant has the opposite sign with the two reflection exponents in place of \(a,c\). It vanishes precisely if \(\zeta^{kd}\) is a primitive cube root. With \(g=\gcd(n,d)\), \(q=n/g\), this happens for exactly \(2g\) Fourier frequencies when \(3\mid q\), and never otherwise. A singular mixed block has rank exactly one because a unit off-diagonal or diagonal entry survives. Pairing \(k\) with \(-k\) and accounting for regular multiplicity two gives nullity \(2g\). This proves the individual nullity laws.

For the refined counts, fix \(g\mid n\) with \(q=n/g\) divisible by three. Exactly \(n\varphi(q)/2\) unordered same-coset pairs have exponent difference of additive order \(q\). Choose their remaining opposite-coset singleton in \(n\) ways and either coset in two ways. Hence there are \(n^2\varphi(q)\) mixed supports of nullity \(2g\).

For pure supports, fix an anchor exponent \(u\). The ordered normalized differences \(((v-u)/g,(w-u)/g)\) run through pairs in \(\mathbb Z_q\) with joint gcd one with \(q\) and residues \(1,2\) modulo three in either order. There are
\[
2(q/3)^2\prod_{\substack{\ell\mid q\\\ell\ne3\ \mathrm{prime}}}(1-\ell^{-2})
\]
such ordered pairs: enforce primitivity at every prime other than three by inclusion-exclusion. Multiplying by \(n\) anchor choices, dividing by the six orderings of each triple, and multiplying by the two group cosets yields the stated pure-type multiplicity.

Finally, the mixed supports are singular exactly when their pair difference is not in the unique subgroup of \(\mathbb Z_n\) of order \(m=n/3^v\). This gives \(n^2(n-m)\) singular mixed triples. A pure triple is singular exactly when its first unequal ternary digit consists of one point in each of the three children of a common residue class modulo \(3^j\), for some \(0\le j<v\). For each coset there are \(3^j(n/3^{j+1})^3\) choices. Counting both cosets and summing the geometric series gives \(\frac{n^3}{12}(1-3^{-2v})\). This proves the total and shows its dependence only on the three-primary part of \(n\).

## Verification
The accompanying standalone C++17 program, `checker.cpp`, constructs exact integer \(2n\)-by-\(2n\) left-convolution matrices for every three-element support for each \(3\le n\le14\). It compares the proved formula with matrix ranks independently evaluated modulo each of two distinct primes, and checks the divisor-resolved multiplicity formulas and total singular-support formula. Run `c++ -std=c++17 -O2 checker.cpp -o checker && ./checker`. Both modular rank tests agreed with the predicted exact nullity in every case, and the executable ended with `CHECK_PASS`. The proof above, not finite computation or modular reduction, establishes the theorem for all \(n\ge3\).

## Relationship to prior work
General irreducible-representation decompositions of Cayley digraph adjacency matrices and characteristic polynomials are established by Arezoomand and Taeri (2013). Al-Tarimshawy (2018) and Al-Tarimshawy–Siemons (2020) analyze singular undirected dihedral-transitive graphs using circulant/cyclotomic tests. These supply broad context but do not state the complete arithmetic nullity law and three-element support census here, which allows directed, looped, nongenerating, and symmetric cases uniformly. In the pure-type case the required three-root cancellation is an elementary cyclic Fourier fact; the nonabelian mixed-type classification and its combination with the divisor-refined global census are the additional content. This classification does not replace the earlier general representation-theoretic framework.

## Limitations
The statements concern the specified coefficient-one three-element kernels and algebraic nullity over \(\mathbb C\), not singular values, condition numbers, arbitrary weights, or non-dihedral groups. The modulo-prime checker is a finite consistency check, not a standalone proof of the infinite-family formula. An equivalent specialized enumeration in an older graph-spectral or group-ring source remains a bibliographic possibility.

## References
1. M. Arezoomand and B. Taeri, *On the Characteristic Polynomial of \(n\)-Cayley Digraphs*, Electronic Journal of Combinatorics **20** (2013), #P57, doi:10.37236/3105.
2. A. S. A. Al-Tarimshawy, *Singular Graphs on which the Dihedral Group Acts Vertex Transitively*, arXiv:1810.03406, first public 2018-10-08.
3. A. S. A. Al-Tarimshawy and J. Siemons, *Singular Graphs with Dihedral Group Action*, arXiv:2006.12875, first public 2020-06-23.
4. C. Liu and J. Zhou, *Eigenvalues of Cayley Graphs*, Electronic Journal of Combinatorics **29** (2022), #P2.9, doi:10.37236/8569.
