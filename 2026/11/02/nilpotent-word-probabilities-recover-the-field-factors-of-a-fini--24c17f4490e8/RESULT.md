# Nilpotent word probabilities recover the field factors of a finite ring's semisimple quotient

## Finding
For a nonzero finite associative ring \(R\) with identity, write \(J=J(R)\). Suppose that its semisimple quotient is commutative:
\[
R/J\cong\prod_{i=1}^{s}\mathbb F_{q_i},\qquad s\ge1,
\]
where every \(q_i\) is a prime power, with repetitions allowed. For each integer \(k\ge1\), let \(P_k(R)\) be the probability that the ordered product of \(k\) independent uniform elements of \(R\) is nilpotent. Then:

**Exact law.** For all \(k\ge1\),
\[
P_k(R)=\prod_{i=1}^{s}\left(1-(1-q_i^{-1})^k\right).
\]
Thus the entire law is unaffected by the structure or size of \(J\), even when \(R\) is noncommutative.

**Complete inverse classification.** For any two rings in this class,
\[
\bigl(P_k(R)\bigr)_{k\ge1}=\bigl(P_k(S)\bigr)_{k\ge1}
\quad\Longleftrightarrow\quad R/J(R)\cong S/J(S).
\]
The field orders (with multiplicities) are constructively recoverable from the scalar probabilities.

**Finite determination.** If each quotient has at most \(r\ge1\) field factors, agreement through \(k=2^{r+1}-2\) already implies isomorphic quotients. Without any prior factor bound, put \(Q=1/P_1(R)\). Agreement through \(k=2Q-2\) identifies the quotient among *all* rings in the stated class. For the natural subclass with at most two field factors, \(P_1\) and \(P_2\) suffice, and two is the smallest universal number of initial probabilities.

The inversion and finite-identification assertions—not the field case of the forward multiplication probability—are the contribution established here.

## Assumptions and scope
All rings in the theorem are finite, associative, unital, and nonzero. The quotient \(R/J(R)\) must be a finite product of fields; the ring itself need not be commutative. The variables being multiplied are independent and *uniformly* distributed over the entire underlying ring, and the factors are ordered. Nilpotent means that some positive power of the resulting element is zero. Only the semisimple quotient is reconstructed: the radical, the multiplication on it, the ring order, and the ring isomorphism type are not determined by this probability profile.

## Proof
**1. Reduction of nilpotence to the quotient.** A finite ring is Artinian, so its Jacobson radical \(J\) is a nilpotent two-sided ideal: \(J^d=0\) for some integer \(d\ge1\). In particular every member of \(J\) is nilpotent. Conversely, if \(x\in R\) is nilpotent, its image in \(R/J\) is nilpotent. A product of fields has no nonzero nilpotent elements. Thus \(x\) is nilpotent if and only if \(x\in J\). The quotient map has fibers all of cardinality \(|J|\), so a uniform element of \(R\) maps to a uniform element of \(R/J\), and independent uniform samples remain independent on reduction.

Write \(a_i=1-q_i^{-1}\), so \(0<a_i<1\). For a fixed factor \(\mathbb F_{q_i}\), the product of \(k\) uniform field elements is nonzero if and only if all \(k\) are nonzero, an event of probability \(a_i^k\). The coordinates of a uniform element in the field product are mutually independent. The resulting product lies in \(J\) exactly when each field-coordinate product is zero. The displayed product formula follows for every integer \(k\ge1\), including \(k=1\).

**2. Exact inverse from the asymptotic spectrum.** Suppose a nonempty multiset \(A=\{a_1,\dots,a_s\}\subset(0,1)\) is unknown and \(P_k=\prod_i(1-a_i^k)\) is known for all positive integers \(k\). Put \(a_* =\max_i a_i\) and let \(m\) be its multiplicity. Inclusion-exclusion gives
\[
1-P_k=\sum_{\varnothing\ne U\subseteq[s]}(-1)^{|U|+1}
\left(\prod_{i\in U}a_i\right)^k.
\]
Exactly the \(m\) singleton terms with \(a_i=a_*\) have exponential base \(a_*\); every other term has base strictly less than \(a_*\). Therefore, for some \(0\le b<a_*\),
\[
1-P_k=m a_*^k+O(b^k).
\]
It follows rigorously that
\[
a_* =\lim_{k\to\infty}(1-P_k)^{1/k},\qquad
m=\lim_{k\to\infty}\frac{1-P_k}{a_*^k}.
\]
The corresponding field size is the integer \(q_*=(1-a_*)^{-1}\). Remove these \(m\) factors from the probability sequence by defining \(P'_k=P_k/(1-a_*^k)^m\). This is precisely the probability sequence of the remaining factors. Iterating terminates after finitely many stages; the empty product is the identically-one sequence. Hence the multiset of field sizes, including multiplicities, is uniquely and constructively recovered. A finite field is determined up to isomorphism by its cardinality, establishing the equivalence in the theorem.

**3. Finite prefixes via an exact Vandermonde argument.** Suppose the two quotients have \(s\) and \(t\) factors. Expand the difference of their probability formulas by inclusion-exclusion. The constant terms cancel, leaving an exact exponential sum
\[
P_k(R)-P_k(S)=\sum_{j=1}^{v}c_j b_j^k,
\]
where the \(b_j\) are distinct real numbers in \((0,1)\), the \(c_j\) are nonzero integers, and \(v\le(2^s-1)+(2^t-1)=2^s+2^t-2\). If the first \(v\) values of this difference vanish, the coefficient vector lies in the kernel of the matrix \((b_j^k)_{1\le k,j\le v}\). Its determinant is
\[
\left(\prod_{j=1}^{v}b_j\right)
\prod_{1\le i<j\le v}(b_j-b_i),
\]
which is nonzero. Thus every \(c_j\) is zero, so the full sequences coincide, and step 2 reconstructs identical field spectra. When each factor count is at most \(r\), the bound \(v\le2^{r+1}-2\) follows. If \(P_1(R)=P_1(S)\), then \(P_1^{-1}=\prod_i q_i=Q\) for both quotients. Since every \(q_i\ge2\), each factor count is at most \(\lfloor\log_2Q\rfloor\); therefore \(2^{r+1}-2\le2Q-2\), proving the unconditional prefix bound stated in the finding.

**4. The sharp two-factor case.** The first probability determines \(Q=\prod q_i\). For exactly one field, \(P_2=(2Q-1)/Q^2\). For exactly two fields of sizes \(u,v\), \(uv=Q\) and
\[
Q^2P_2=(2u-1)(2v-1)=4Q-2(u+v)+1.
\]
The one-factor and two-factor values cannot coincide: equality would imply \(u+v=Q+1\), equivalently \((u-1)(v-1)=0\), impossible since \(u,v\ge2\). Within the two-factor case, the sum \(u+v=(4Q+1-Q^2P_2)/2\) is determined; the pair is therefore the unordered root set of \(z^2-(u+v)z+Q\). This proves that the two probabilities determine any quotient with at most two field factors. One probability is insufficient: the quotients \(\mathbb F_4\) and \(\mathbb F_2\times\mathbb F_2\) both have \(P_1=1/4\), but their \(P_2\)'s are \(7/16\) and \(9/16\), respectively. This establishes sharpness of the two-length bound within the subclass.

## Verification
The accompanying standalone exact-arithmetic programs are `CHECK.py` and `CHECK_INVERSION.py`; their exact stdout records are `CHECK.out` and `CHECK_INVERSION.out`. Both returned `VERIFY_OK` when executed with Python 3. The first constructs finite rings directly, iterates complete product-count distributions for lengths one through six, and compares the nilpotence probabilities against the theorem: \(\mathbb Z/4\mathbb Z\), \(\mathbb F_2\times\mathbb F_2\), the noncommutative upper-triangular \(2\times2\) ring over \(\mathbb F_2\), \(\mathbb F_8\), and \(\mathbb F_2^3\times\mathbb F_3\). The second independently checks exact inclusion-exclusion spectra, dominant-base peeling and finite-horizon separation in numerous explicitly listed factor multisets. Exhaustive computations are confined to their stated finite samples; they do not replace any of the proofs above.

For example, the published two-factor collision
\[
P_2(\mathbb F_8)=P_2(\mathbb F_2^3\times\mathbb F_3)=15/64
\]
is broken at length three:
\[
P_3(\mathbb F_8)=169/512,\qquad
P_3(\mathbb F_2^3\times\mathbb F_3)=6517/13824.
\]
The noncommutative upper-triangular ring over \(\mathbb F_2\) and \(\mathbb F_2\times\mathbb F_2\) have identical \(P_k=(1-2^{-k})^2\) for every \(k\), showing why the theorem determines only the quotient.

## Relationship to prior work
Sarma and Subedi's October 6, 2026 paper `arXiv:2610.07892`, *Nilpotent Product Probability of Finite Rings*, investigates the two-factor probability. Its Theorem 2.15 includes the two-factor local-product formula, its Remark 2.17 gives the \(15/64\) collision above, and its Theorem 2.24 treats two-factor triangular matrices. These results are prior art, not contributions claimed here. The present result identifies exactly what the **whole ordered word-length profile** determines and gives finite recognition horizons, including the sharp two-length threshold for quotients with at most two field factors.

Their earlier paper `arXiv:2506.10392`, *The probability that the product of k elements in a finite ring is zero* (June 12, 2025), studies products that equal zero, not products that are nilpotent. Its field-product formulas already imply the elementary forward formula for reduced products of fields. The forward law alone is therefore not asserted to be new; the inverse, finite-horizon, and radical-invariance classification are the result's scientific content.

A published result titled *Degree distributions reconstruct finite-field factors in product trace graphs* concerns degree data from trace graphs of matrix-ring products, not random nilpotent word-products. Its conclusion is not the present inverse theorem. No inspected source states the all-length inverse implication or the exact finite bound; this literature comparison is not a universal priority certificate.

## Limitations
The quotient is assumed commutative. For quotients containing matrix-algebra factors, a nilpotent matrix need not belong to the Jacobson radical, so the basic reduction fails. The theorem does not reconstruct the radical or the full ring. The universal finite cutoff \(2Q-2\) and the factor-count cutoff \(2^{r+1}-2\) are sufficient, not claimed optimal for \(r\ge3\). Limits in the inversion are exact mathematical limits, not numerically stable estimators from noisy probabilities. Absolute historical priority has not been independently established, and the earlier zero-product literature covers part of the forward computation.

## References
1. D. Sarma and T. Subedi, *Nilpotent Product Probability of Finite Rings*, arXiv:2610.07892, first public October 6, 2026. https://arxiv.org/abs/2610.07892
2. D. Sarma and T. Subedi, *The probability that the product of k elements in a finite ring is zero*, arXiv:2506.10392, first public June 12, 2025. https://arxiv.org/abs/2506.10392
3. *Degree distributions reconstruct finite-field factors in product trace graphs*, publicly available research result (2026). https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-degree-distributions-reconstruct-finite-field-factors-in-product--3dd944f1d801
