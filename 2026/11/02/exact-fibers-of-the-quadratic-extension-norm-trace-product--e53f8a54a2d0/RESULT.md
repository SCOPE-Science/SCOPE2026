# Exact fibers of the quadratic-extension norm–trace product

## Finding
Let \(q\) be any prime power, \(k=\mathbb F_q\), \(K=\mathbb F_{q^2}\), and let
\[
P(x)=\operatorname{Tr}_{K/k}(x)\operatorname{N}_{K/k}(x)=x^{q+2}+x^{2q+1}\in k.
\]
For \(y\in k\), write \(N(y)=\#\{x\in K:P(x)=y\}\). Then \(N(0)=q\) for every \(q\).

If \(3\nmid(q-1)\), every fiber is balanced: \(N(y)=q\) for every \(y\in k\).

If \(3\mid(q-1)\), take either nontrivial multiplicative character \(\rho:k^\times\to\{1,\omega,\omega^2\}\) of order three and put
\[
S=\sum_{\substack{z\in K\\\operatorname{Tr}_{K/k}(z)=1}}\rho(\operatorname{N}_{K/k}(z)).
\]
Then \(|S|^2=q\), and for every \(y\in k^\times\),
\[
N(y)=q+\rho(y)\overline S+\overline{\rho(y)}S.
\]
Thus the nonzero-target counts are constant on the three cubic-residue cosets, and their exact squared deviation is
\[
\sum_{y\in k^\times}(N(y)-q)^2=2q(q-1).
\]
In particular, uniform fibers occur exactly when \(3\nmid(q-1)\).

The map \(P:K\to k\) is onto for every prime power except \(q=4\). For \(q=4\), its zero fiber has size four, its two represented nonzero fibers have size six each, and its remaining nonzero fiber is empty; in fact \(P(K)=k\setminus\{1\}\).

## Assumptions and scope
All prime powers \(q\ge2\) and both even and odd characteristic are included. Trace and norm are the field-theoretic maps for the degree-two extension \(K/k\), and \(\rho(0)\) is never used in the character sum: on the trace-one line every element is nonzero. The variance above is an unnormalized sum over nonzero target values, centered at \(q\). Complex conjugation is taken after embedding the cube roots of unity in \(\mathbb C\).

## Proof
**1. Trace decomposition and cube fibers.** The trace map is a surjective \(k\)-linear functional \(K\to k\), since finite-field extensions are separable; each trace fiber has \(q\) elements. Because the norm vanishes only at zero, \(P(x)=0\) if and only if \(\operatorname{Tr}(x)=0\), proving \(N(0)=q\).

For every \(x\) with \(t=\operatorname{Tr}(x)\ne0\), write uniquely \(x=tz\) with \(\operatorname{Tr}(z)=1\). Scalar extension gives \(\operatorname{N}(tz)=t^2\operatorname{N}(z)\), hence
\[
P(tz)=t^3\operatorname{N}(z).
\]
The trace-one line contains \(q\) nonzero elements. If the cube map on \(k^\times\) is bijective, each such \(z\) yields precisely one \(t\) for each prescribed \(y\ne0\), so \(N(y)=q\). This is equivalent to \(3\nmid(q-1)\).

If \(3\mid(q-1)\), the number of solutions \(t\in k^\times\) to \(t^3=a\) is \(1+\rho(a)+\overline{\rho(a)}\). Summing over \(\operatorname{Tr}(z)=1\) yields
\[
N(y)=q+\rho(y)\sum_{\operatorname{Tr}(z)=1}\overline{\rho(\operatorname{N}(z))}
+\overline{\rho(y)}\sum_{\operatorname{Tr}(z)=1}\rho(\operatorname{N}(z)),
\]
which is the asserted character formula. Orthogonality of the nontrivial cubic characters gives
\[
\sum_{y\in k^\times}(N(y)-q)^2=2(q-1)|S|^2.
\]

**2. The trace-one norm character sum in odd characteristic.** Suppose \(q\) is odd; in this branch \(3\mid(q-1)\), so both the quadratic character \(\chi\) and the cubic character \(\rho\) are nontrivial and their product is nontrivial. For each \(n\in k\), the number of elements \(z\in K\) with trace one and norm \(n\) equals
\[
1-\chi(1-4n),
\]
where \(\chi(0)=0\). Indeed \(z\) satisfies \(Z^2-Z+n=0\). A nonsquare discriminant gives two conjugate roots in \(K\) with trace one; a nonzero square gives roots in \(k\), neither of which has trace one, except for the repeated-root case, when \(z=1/2\) has trace one. Hence
\[
S=-\rho(4)^{-1}J(\rho,\chi),\qquad
J(\rho,\chi)=\sum_{u\in k}\rho(u)\chi(1-u).
\]
The classical Jacobi–Gauss identity \(J(\rho,\chi)=G(\rho)G(\chi)/G(\rho\chi)\), applicable because all three characters are nontrivial, together with \(|G(\eta)|=\sqrt q\) for any nontrivial multiplicative \(\eta\), proves \(|S|^2=q\). These standard Gauss identities follow by expanding the sums and using additive/multiplicative character orthogonality.

**3. The trace-one norm character sum in characteristic two.** Now suppose \(q\) is even and \(3\mid(q-1)\). Let \(\psi(n)=(-1)^{\operatorname{Tr}_{k/\mathbb F_2}(n)}\), a nontrivial additive character. The polynomial \(Z^2+Z+n\) is irreducible over \(k\) exactly when \(\psi(n)=-1\); then its two conjugate roots in \(K\) both have trace one and norm \(n\). If it splits, neither root has extension trace one. Thus the number of trace-one elements with norm \(n\) is \(1-\psi(n)\). Consequently
\[
S=-G(\rho,\psi),\qquad
G(\rho,\psi)=\sum_{n\in k^\times}\rho(n)\psi(n).
\]
The elementary multiplicative/additive orthogonality identity \(|G(\rho,\psi)|^2=q\) yields \(|S|^2=q\). This completes the variance and nonuniformity assertions in every characteristic.

**4. Surjectivity and the exceptional field.** For \(3\mid(q-1)\), the character formula and the triangle inequality yield
\[
N(y)\ge q-2\sqrt q>0\quad(q>4),
\]
so all nonzero targets occur whenever \(q>4\). The fields \(q=2,3\) belong to the balanced branch. When \(q=4\), choose \(\omega\in k\) of order three. In characteristic two, the norm of a trace-one element has absolute trace one; over \(k=\mathbb F_4\) these norms are precisely \(\omega,\omega^2\), each attained twice. Since every \(t\in k^\times\) satisfies \(t^3=1\), each of those two targets has six preimages, whereas \(1\) has none. The zero fiber has four elements as already proved. This establishes the claimed unique exception and completes the proof.

## Verification
Run \(\texttt{python3 verify.py}\) in a standard Python 3 environment. The script constructs finite fields by explicit irreducible prime-field polynomial quotients, enumerates every source element for each chosen field, verifies the trace and norm land in the base field, and checks the exact zero-fiber, balanced/nonbalanced variance, cubic-coset constancy, image-size, and four-element exceptional cases. It checks \(q\in\{2,3,4,5,7,8,9,11,13,16\}\), a total of 794 input elements. A successful run ends with \(\texttt{VERIFY_OK cases=10 inputs=794}\). This is finite corroboration, not a substitute for the proof for all prime powers.

## Relationship to prior work
Mullen, Wan and Wang (2012, arXiv:1210.8119) establish general upper bounds on finite-field polynomial-map value-set sizes (their Theorem 2.1), but do not classify the fibers of this trace–norm product. Gao and Wang (2014, arXiv:1407.5884) study value-set distributions for random polynomials and cyclotomic maps, rather than the deterministic norm–trace product on quadratic extensions. Ding, Xiong and Zieve (2025, arXiv:2510.16640) classify complete/permutation mappings within a cubic Frobenius-polynomial family that includes the present two-term expression; their classification is of bijections from \(K\) to \(K\), while this expression maps into the proper subfield \(k\), and their stated theorems do not determine its \(K\to k\) fiber sizes. The character-sum evaluation uses standard Gauss and Jacobi identities. Possible equivalent coverage in broader norm–trace counting literature cannot be excluded.

## Limitations
This result applies to the single specified norm–trace product on quadratic finite-field extensions; it does not classify products of arbitrary trace and norm powers, higher extension degrees, or the complete multiplicity spectrum as a function only of \(q\) in the nonuniform regime without evaluating the indicated cubic character sum. The finding has not undergone independent validation. The possibility of an earlier equivalent theorem in specialized finite-field literature remains an originality risk.

## References
1. Gary L. Mullen, Daqing Wan and Qiang Wang, *Value sets of polynomial maps over finite fields*, arXiv:1210.8119v1, public 2012-10-30, https://arxiv.org/html/1210.8119v1.
2. Zhicheng Gao and Qiang Wang, *A probabilistic approach to value sets of polynomials over finite fields*, arXiv:1407.5884v1, public 2014-07-22, https://arxiv.org/html/1407.5884v1.
3. Zhiguo Ding, Wei Xiong and Michael E. Zieve, *Determination of all complete mappings of finite quadratic fields of a prescribed cubic Frobenius form*, arXiv:2510.16640v1, public 2025-10-18, https://arxiv.org/html/2510.16640v1.
