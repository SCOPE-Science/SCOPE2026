# Singer-sharp variable thresholds for 2-adic quotient sets of diagonal forms

## Finding
For every prime power \(q\ge2\), put \(N=q^2+q+1\). Among the integral diagonal forms of degree \(N\)
\[
F(X_1,\ldots,X_r)=\sum_{i=1}^r a_iX_i^N,\qquad a_i\ne0,
\]
whose coefficient valuations \(\nu_2(a_i)\) are pairwise distinct modulo \(N\), the **minimum number of essential variables** for which the quotient set of integer values is dense in \(\mathbb Q_2\) is exactly \(q+1\). In particular, a form with only \(q+1\) variables exists for every prime power \(q\), whereas any such form with at most \(q\) variables is non-dense.

The proof also gives the following exact closure, valid more generally for any prime \(p\nmid N\), any degree \(N\ge3\), and distinct coefficient-valuation residues:
\[
\overline{R(F)}^{\,\mathbb Q_p}=\{0\}\cup\bigcup_{1\le i,j\le r}\frac{a_i}{a_j}(\mathbb Q_p^\times)^N,
\qquad
R(F)=\left\{\frac{F(\mathbf x)}{F(\mathbf y)}:\mathbf x,\mathbf y\in\mathbb Z^r,\ F(\mathbf y)\ne0\right\}.
\]
Thus the exact density condition is that the coefficient classes form a difference-cover of the finite quotient \(\mathbb Q_p^\times/(\mathbb Q_p^\times)^N\). In the primary \(p=2\), odd-degree case, this reduces to the finite condition
\[
\{\nu_2(a_i)-\nu_2(a_j)\bmod N:1\le i,j\le r\}=\mathbb Z/N\mathbb Z.
\]

## Assumptions and scope
A prime power is a positive power of a prime. The exponent \(N=q^2+q+1\) is odd; hence \(2\nmid N\). Each nonzero \(a_i\) is integral, and no two \(\nu_2(a_i)\) are congruent modulo \(N\). The minimum refers **only** to this natural distinct-valuation-residue family, not to arbitrary diagonal forms without that hypothesis. The form is evaluated on integer vectors, with zero allowed as an input coordinate. All closures are taken in the full field \(\mathbb Q_p\); \(0\) is included.

## Proof
**1. A local image lemma.** Fix any degree \(n\ge3\) and prime \(p\nmid n\), with \(F=\sum_i a_iX_i^n\) and distinct \(\nu_p(a_i)\) modulo \(n\). If \(F(\mathbf x)\ne0\) with integer coordinates, the valuations of the nonzero monomials \(a_i x_i^n\) are pairwise distinct modulo \(n\). They therefore have a unique smallest valuation, attained at some index \(i\), and
\[
F(\mathbf x)=a_ix_i^n(1+pz),\qquad z\in\mathbb Z_p.
\]
Here \(x_i\ne0\). Hensel's lemma applied to \(T^n-(1+pz)\) at \(T\equiv1\pmod p\) gives a root in \(\mathbb Z_p^\times\), because \(n\) is invertible modulo \(p\). Consequently \(F(\mathbf x)\in a_i(\mathbb Q_p^\times)^n\).

Conversely, restricting \(F\) to its \(i\)-th coordinate yields every \(a_i k^n\), \(k\in\mathbb Z\). For any pair \((i,j)\), their ratios include \((a_i/a_j)(k/\ell)^n\) for arbitrary nonzero integers \(k,\ell\). Since \(\mathbb Q^\times\) is dense in \(\mathbb Q_p^\times\), these ratios are dense in \((a_i/a_j)(\mathbb Q_p^\times)^n\). The subgroup of \(n\)-th powers is closed and open: its valuations are multiples of \(n\), and among unit groups it has finite index (Hensel's lemma handles the principal units). A finite union of its cosets is therefore closed in \(\mathbb Q_p^\times\). This proves the exact closure formula, with \(0\) supplied by the zero vector. It follows that density is equivalent to covering every class of the finite group \(\mathbb Q_p^\times/(\mathbb Q_p^\times)^n\).

**2. The finite cyclic reduction at two.** For odd \(n\), the map \(u\mapsto u^n\) is an automorphism of \(\mathbb Z_2^\times\): for any odd \(u\), successive Hensel lifts of an odd root of \(T^n-u\) exist uniquely. Thus \(\mathbb Q_2^\times/(\mathbb Q_2^\times)^n\cong\mathbb Z/n\mathbb Z\), via \(\nu_2\bmod n\). If \(D\) denotes the \(r\)-element subset \(\{\nu_2(a_i)\bmod n\}\), density holds if and only if \(D-D=\mathbb Z/n\mathbb Z\). There are at most \(r(r-1)\) ordered nonzero differences, together with zero. Necessarily
\[
n\le r(r-1)+1.
\]
For \(n=N=q^2+q+1\), this inequality forces \(r\ge q+1\): at \(r=q\), the right side is only \(q^2-q+1<N\).

**3. Singer's sharp construction, including its difference property.** Let \(K=\mathbb F_{q^3}\), with subfield \(k=\mathbb F_q\). Its multiplicative quotient \(G=K^\times/k^\times\) is cyclic of order \(N=(q^3-1)/(q-1)\). Choose a generator \(gk^\times\). The field trace \(\operatorname{Tr}_{K/k}:K\to k\) is a nonzero \(k\)-linear map; its kernel \(L\) is a two-dimensional \(k\)-plane. Define
\[
D=\{d\in\mathbb Z/N\mathbb Z:\operatorname{Tr}_{K/k}(g^d)=0\}.
\]
This is well-defined on cosets because multiplying by a nonzero element of \(k\) preserves trace-zero status. The plane \(L\) has exactly \((q^2-1)/(q-1)=q+1\) one-dimensional \(k\)-subspaces, so \(|D|=q+1\).

For every nonidentity coset \(c k^\times\in G\), the planes \(L\) and \(cL\) are distinct: equality would imply that the linear trace functionals \(z\mapsto\operatorname{Tr}(z)\) and \(z\mapsto\operatorname{Tr}(c^{-1}z)\) have equal kernels, hence are nonzero scalar multiples over \(k\); nondegeneracy of the finite-field trace pairing then forces \(c^{-1}\in k\), a contradiction. Two distinct two-dimensional subspaces of the three-dimensional \(k\)-vector space \(K\) meet in exactly one one-dimensional subspace. Consequently, for every nonidentity \(c k^\times\) there is exactly one ordered pair of trace-zero projective points whose quotient equals \(c k^\times\). In exponent notation, each nonzero residue modulo \(N\) occurs exactly once as \(d_i-d_j\), with \(d_i,d_j\in D\). Therefore \(D-D=\mathbb Z/N\mathbb Z\).

Choose the representatives \(0\le d_1<\cdots<d_{q+1}<N\) of this set, and define the integral form
\[
F_q(X_1,\dots,X_{q+1})=\sum_{i=1}^{q+1}2^{d_i}X_i^N.
\]
Its coefficient valuations are distinct modulo \(N\), and step 2 together with the exact local closure proves that \(R(F_q)\) is dense in \(\mathbb Q_2\). The lower bound in step 2 makes \(q+1\) optimal among the stated family. This establishes the theorem for every prime power \(q\), without any asymptotic or computational assumption.

## Verification
The self-contained `verify.py` checks complete finite unit-power images for eleven small prime-power moduli, 68,160 nonzero values of twelve binary forms, and exhaustive small-coordinate tests for the explicit sharp parameter triples below. For \(q=2,3,4\), it verifies the modular difference property with **no repetition of nonzero differences** and the resulting realized value/quotient power classes. The explicit exponent witnesses, respectively, are
\[
(q,N,D)=(2,7,\{0,1,3\}),\quad (3,13,\{0,1,3,9\}),\quad (4,21,\{0,1,4,14,16\}).
\]
Execute `python3 verify.py` with Python's standard library. These finite checks are reproducibility aids; the arbitrary-prime-power conclusion follows from the trace-plane argument, not extrapolation.

## Relationship to prior work
Antony, Barman and Miska's 2022 diagonal-form paper proves density under the same distinct-valuation hypothesis when \(\gcd(n,p(p-1))=1\) and \(r>n/2\) (Theorem 1.3), and gives a concrete construction with \(r=\lfloor n/2\rfloor\) (Remark 3.2). Its proof uses coefficient-valuation residue differences, so the **sufficiency of a difference-cover is closely implicit in that argument** and is not claimed here as a novel independent principle. The present result identifies an exact quotient-set closure and gives a different, sharp infinite family: for \(n=q^2+q+1\), the optimum is \(q+1\), much smaller than the earlier universal sufficient bound. The cyclic trace-zero difference sets are the classical Singer construction in finite geometry; no novelty is attributed to their standalone existence. The contribution is the exact sharp variable threshold and its structural realization within these 2-adic diagonal-form quotient sets.

## Limitations
The minimum is restricted to coefficient valuations distinct modulo the exponent. It need not be the global minimum for arbitrary diagonal forms. An implicit published link between Singer difference sets and these quotient sets would diminish originality. The code does not verify all prime powers and is not a proof of the infinite assertion.

## References
1. D. Antony, R. Barman, P. Miska, *\(p\)-Adic quotient sets: diagonal forms*, arXiv:2201.04372v1, publicly posted 2022-01-12, especially Theorem 1.3, its proof, and Remark 3.2. https://arxiv.org/abs/2201.04372
2. D. Antony and R. Barman, *\(p\)-adic quotient sets: cubic forms*, arXiv:2110.05420v1 (2021). https://arxiv.org/abs/2110.05420
3. D. Antony and R. Barman, *On \(p\)-adic denseness of quotients of values of integral forms*, arXiv:2308.08907v1 (2023). https://arxiv.org/abs/2308.08907
4. *SageMath Combinatorics Reference Manual*, “Singer difference set,” a standard finite-projective-geometry construction: https://doc-gitlab.sagemath.org/html/en/reference/combinat/sage/combinat/designs/difference_family.html
