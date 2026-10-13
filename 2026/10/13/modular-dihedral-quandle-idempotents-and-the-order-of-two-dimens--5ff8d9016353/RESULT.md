# Modular dihedral-quandle idempotents and the order-of-two dimension jump

## Finding
Let \(p\) be an odd prime, let \(K\) be any field of characteristic \(p\), and let \(R_p=\mathbb Z/p\mathbb Z\) carry the dihedral quandle product \(i\triangleright j=2j-i\). The quandle algebra \(K[R_p]\) has basis \(e_i\) for \(i\in R_p\) and bilinear multiplication \(e_i e_j=e_{2j-i}\).

Write \(B=K[X]/(X^p-1)\) with its **ordinary associative multiplication**, and identify the vector \(\sum_i a_i e_i\) with \(\sum_i a_iX^i\). Put \(y=X-1\), \(t=\log(X)=\sum_{k=1}^{p-1}(-1)^{k+1}y^k/k\), and for \(h\in yB\) define the truncated exponential \(\exp(h)=\sum_{k=0}^{p-1}h^k/k!\). These operations are performed in the ordinary commutative algebra \(B\), not by iterating quandle multiplication.

Let \(d=\operatorname{ord}_p(2)\), and let
\[
S_p=\{j:1\le j\le p-1,\ j\text{ odd},\ d\mid j-1\},\qquad m_p=|S_p|.
\]
Then the **complete idempotent set** is
\[
\operatorname{Idem}(K[R_p])
=\{0\}\;\sqcup\;
\left\{\exp\!\left(\sum_{j\in S_p}c_j t^j\right):c_j\in K\right\}.
\]
The second piece is polynomially isomorphic to affine \(m_p\)-space over \(K\) (with inverse given by truncated logarithmic coordinates); the zero element is a separate point. Explicitly,
\[
m_p=\begin{cases}
1+\left\lfloor\dfrac{p-2}{d}\right\rfloor,&d\text{ even},\\
1+\left\lfloor\dfrac{p-2}{2d}\right\rfloor,&d\text{ odd}.
\end{cases}
\]
For any finite field \(K=\mathbb F_q\) of characteristic \(p\), the exact count is \(1+q^{m_p}\). For \(p=17\), \(S_p=\{1,9\}\), giving \(1+q^2\); for \(p=31\), \(S_p=\{1,11,21\}\), giving \(1+q^3\). Thus prime-dependent extra idempotent parameters already occur for the natural odd-prime dihedral family.

## Assumptions and scope
The prime \(p\) is odd, but \(K\) is otherwise arbitrary and need not be finite, perfect, or algebraically closed. In \(B\), \((X-1)^p=0\); all denominators \(k\) and \(k!\) for \(1\le k<p\) are invertible in \(K\). The notation \(\operatorname{Idem}\) refers to solutions of \(u\cdot u=u\) for the nonassociative quandle multiplication. Statements about exponentials, logarithms, powers, and factorization use the separately defined associative multiplication in \(B\).

## Proof
**1. Identify the quandle product.** Define \(\sigma_a:B\to B\) by \(\sigma_a(X)=X^a\), for \(a\in(\mathbb Z/p\mathbb Z)^\times\). Bilinearity of the quandle multiplication yields, for all \(F,G\in B\),
\[
F\star G=\sigma_{-1}(F)\,\sigma_2(G).
\]
The product on the right is ordinary commutative multiplication. The augmentation \(\varepsilon(F)=F(1)\) consequently obeys \(\varepsilon(F\star G)=\varepsilon(F)\varepsilon(G)\).

**2. Exclude nonzero augmentation-zero idempotents.** The augmentation ideal is \(J=(X-1)B=(y)\), with \(J^p=0\). If \(F\star F=F\), then \(\varepsilon(F)\in\{0,1\}\). If \(\varepsilon(F)=0\), then \(F\in J\); because \(\sigma_{-1}\) and \(\sigma_2\) preserve each \(J^s\), the equation forces \(F\in J^2\), then \(F\in J^4\), and inductively \(F\in J^{2^k}\). Eventually this is zero; therefore \(F=0\). This argument works over every coefficient extension as well, without an assumption that its coefficients are reduced.

**3. Linearize augmentation-one idempotency.** Every element with augmentation one belongs to the ordinary multiplicative group \(1+J\). For the nilpotent commutative ideal \(J\) with \(J^p=0\), the truncated series \(\exp:J\to1+J\) and \(\log:1+J\to J\) are inverse group isomorphisms. Indeed, the formal identities for \(\exp(u+v)=\exp(u)\exp(v)\), \(\log(uv)=\log u+\log v\), and composition of these series have only denominators invertible modulo \(p\) in total degrees less than \(p\), while every term of total degree at least \(p\) in \(J\) vanishes. These identities also commute with \(\sigma_a\).

For \(F\in1+J\), write \(h=\log(F)\). Applying the logarithm to \(F=\sigma_{-1}(F)\sigma_2(F)\) gives the **equivalent** linear equation
\[
h=\sigma_{-1}(h)+\sigma_2(h).
\]
Since \(t=\log X=y+\text{higher powers of }y\), \(t,t^2,\ldots,t^{p-1}\) form a \(K\)-basis of \(J\). The group-homomorphism property implies \(\sigma_a(t)=\log(X^a)=a t\), including \(a=-1,2\). Hence if \(h=\sum_{j=1}^{p-1}c_j t^j\), then
\[
\bigl(1-(-1)^j-2^j\bigr)c_j=0\quad(1\le j<p).
\]
For even \(j\), this scalar is \(-2^j\ne0\). For odd \(j\), it is \(2-2^j\), which vanishes precisely when \(d\mid(j-1)\). Thus the solutions are exactly \(h=\sum_{j\in S_p}c_jt^j\), and exponentiating proves both directions of the classification.

**4. Dimensions and finite-field counts.** Since \(t=y+O(y^2)\), the displayed logarithmic coordinates are polynomial and have polynomial inverse. There are exactly \(m_p\) unrestricted independent field parameters, so the augmentation-one locus is affine \(m_p\)-space. Because \(j=1+kd\) must be odd and \(j\le p-1\), when \(d\) is even every nonnegative \(k\le (p-2)/d\) is allowed, whereas when \(d\) is odd only even \(k\) are allowed. This proves the two cases for \(m_p\) and the count \(1+q^{m_p}\). Direct evaluation yields the two given examples.

## Verification
Run `python verify.py` using Python 3 and the standard library. The program implements quandle multiplication directly in the basis \((e_i)\), independently of the ordinary associative product used to construct candidate solutions. It exhaustively checks the entire \(3^3\)-element and \(5^5\)-element algebras and matches the classified idempotent sets. It additionally checks constructed and random samples for primes \(7,11,17,31\) with fixed seeds, including the multi-parameter cases, and prints `VERIFY_OK` on success. Finite enumerations validate examples and implementation only; the proof above establishes all primes and fields.

## Relationship to prior work
The earlier full-text study of Bardakov, Passi, and Singh (2022) treats quandle-algebra idempotents in specific small and integral examples. Churchill, Churchill, Fernando, and Kousik (2026, arXiv:2608.09149v1) study idempotents in core quandles of nonabelian dihedral groups and questions over integral quandle rings; their Section 3 concerns \(\operatorname{Core}(D_3)\), not the modular coefficient algebra \(K[R_p]\) for all odd primes. The 2026 papers arXiv:2609.03799v1 and arXiv:2609.09183v1 address integral quandle-ring idempotents for dihedral/Takasaki quandles, where the coefficient characteristic does not divide the quandle size. Their reported integral classifications do not logically imply the additional modular affine coordinates established here. A previously available characteristic-three result already gives the case \(p=3\) (published record `06aa9c19-e539-4456-a3ab-0164f6930052`); that special case is expressly not a new contribution. The new statement is the all-prime order-of-two law and its higher-dimensional changes.

## Limitations
This theorem does not classify idempotents of composite-order dihedral quandles, quandle algebras whose coefficient characteristic differs from the odd-prime quandle order, or arbitrary Alexander quandles. The counting law does not by itself describe other polynomial identities, automorphism groups, or invariant-based knot applications. Two highly relevant 2026 preprints were accessible by abstract and bibliographic information rather than fully inspected text, so an unknown equivalent result or appendix in that literature is a residual historical risk. No independent audit has been performed.

## References
1. G. Churchill, I. R. Churchill, N. Fernando, and B. Kousik, *A further study of quandles and quandle rings*, arXiv:2608.09149v1 (first posted 2026-08-10), Sections 3–4.
2. M. Elhamdadi, L. Ta, and B. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799v1 (2026-09-03).
3. D. Kaur and P. Singh, *A note on idempotents in quandle rings*, arXiv:2609.09183v1 (September 2026).
4. V. G. Bardakov, I. B. S. Passi, and M. Singh, *Zero-divisors and idempotents in quandle rings*, Osaka J. Math. 59 (2022), 611–637.
5. *A characteristic-three idempotent line in the quandle algebra of* \(R_3\), published research record `06aa9c19-e539-4456-a3ab-0164f6930052` (2026).
