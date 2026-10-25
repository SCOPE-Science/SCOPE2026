# Rectangular nilpotent-product law over finite fields and its semisimple-ring consequence

## Finding

Let \(\mathbb F_q\) be a finite field, and let \(m,n\geq1\) be integers. For independently and uniformly chosen \(A\in M_{m\times n}(\mathbb F_q)\) and \(B\in M_{n\times m}(\mathbb F_q)\),
\[
\Pr(AB\text{ is nilpotent})=q^{-m}+q^{-n}-q^{-(m+n)}.
\]
More precisely, for **every fixed** \(A\) of rank \(r\), precisely \(q^{mn-r}\) matrices \(B\) make \(AB\) nilpotent. Hence the number of successful ordered pairs is
\[
q^{2mn-m}+q^{2mn-n}-q^{2mn-m-n}.
\]

Consequently, for any nonzero finite semisimple unital ring
\(R\cong\prod_{i=1}^{s}M_{d_i}(\mathbb F_{q_i})\), with \(s\geq1\) and \(d_i\geq1\), its nilpotent-product probability is
\[
P_{\mathrm{nil}}(R):=\frac{|\{(a,b)\in R^2:ab\text{ is nilpotent}\}|}{|R|^2}
=\prod_{i=1}^s\bigl(2q_i^{-d_i}-q_i^{-2d_i}\bigr).
\]
In particular, the noncommutative ring \(M_d(\mathbb F_q)\), for \(d\geq2\), and the field \(\mathbb F_{q^d}\) have **identical** nilpotent-product probabilities \(2q^{-d}-q^{-2d}\), although they are not isomorphic as rings. This coincidence is an equality of a statistic, not an isomorphism or equality of ring orders.

## Assumptions and scope

The field order \(q\) is any prime power. Matrices are chosen uniformly and independently. Nilpotent means that some positive matrix power is zero; for a square matrix of dimension \(j\), equivalently its \(j\)-th power is zero. For \(m\ne n\), the product \(AB\) is an \(m\)-square matrix. The semisimple-ring statement uses the standard Artin–Wedderburn decomposition and applies to finite nonzero rings with identity and zero Jacobson radical. No claim is made here for rings with nonzero radical.

## Proof

**1. A nilpotent-matrix count.** We first establish for every \(j\geq0\) the classical identity
\[
N_j:=|\{T\in M_j(\mathbb F_q):T\text{ nilpotent}\}|=q^{j^2-j},
\]
with the convention \(N_0=1\). Let \(C_j=\prod_{i=1}^j(1-q^{-i})\) and \(C_0=1\). There are \(q^{j^2}C_j\) invertible endomorphisms on a \(j\)-space. For a \(d\)-space, Fitting decomposition uniquely specifies an invariant direct sum \(V=U\oplus W\) on which an endomorphism is invertible on \(U\) and nilpotent on \(W\). For \(\dim W=k\), there are \({d\brack k}_q q^{k(d-k)}\) choices of ordered complementary subspaces: first choose \(W\), then a complementary \(U\), of which there are \(q^{k(d-k)}\). Here \({d\brack k}_q\) is the Gaussian binomial coefficient.

Thus
\[
q^{d^2}=\sum_{k=0}^d{d\brack k}_q q^{k(d-k)}q^{(d-k)^2}C_{d-k}N_k.
\]
Using \({d\brack k}_q=q^{k(d-k)}C_d/(C_kC_{d-k})\), the candidate \(N_k=q^{k^2-k}\) turns the right side into
\[
q^{d^2}C_d\sum_{k=0}^d\frac{q^{-k}}{C_k}=q^{d^2}.
\]
The final equality follows by telescoping: for \(k\geq1\), \(q^{-k}/C_k=1/C_k-1/C_{k-1}\), and the \(k=0\) term is \(1\). The coefficient of \(N_d\) in the original recurrence is \(1\), while all other \(N_k\) have \(k<d\), so induction from \(d=0\) uniquely proves the count. Hence a uniformly chosen \(r\)-square matrix is nilpotent with probability \(q^{-r}\), including \(r=0\).

**2. The fixed-factor conditional law.** Fix \(A:\mathbb F_q^n\to\mathbb F_q^m\) of rank \(r\). Write \(U=\operatorname{im}A\) and choose any complementary subspace \(W\) so that \(\mathbb F_q^m=U\oplus W\). As \(B\) varies uniformly in \(\operatorname{Hom}(\mathbb F_q^m,\mathbb F_q^n)\), the map \(B\mapsto AB\) is a surjective linear map onto \(\operatorname{Hom}(\mathbb F_q^m,U)\); its fibers all have size \(q^{m(n-r)}\). Relative to this direct sum, every such product has block form
\[
AB=\begin{pmatrix}C&D\\0&0\end{pmatrix},\qquad C\in M_r(\mathbb F_q),
\]
with \(C\) uniformly distributed and \(D\) unrestricted. The block matrix is nilpotent exactly when \(C\) is nilpotent (its characteristic polynomial is the characteristic polynomial of \(C\) multiplied by a power of the indeterminate, or use block powers). By step 1 this has probability \(q^{-r}\). Therefore precisely \(q^{mn-r}\) out of the \(q^{mn}\) possible \(B\) succeed. This also covers rank zero and \(m=1\) or \(n=1\).

**3. Averaging ranks without a rank-distribution sum.** The left kernel of \(A\), viewed as \(A^\mathsf{T}:\mathbb F_q^m\to\mathbb F_q^n\), has size \(q^{m-r}\). Thus the desired probability is
\[
\mathbb E_A[q^{-\operatorname{rank}(A)}]
=q^{-m}\sum_{y\in\mathbb F_q^m}\Pr(y^\mathsf{T}A=0).
\]
For \(y=0\), the inner probability is \(1\). For each of the \(q^m-1\) nonzero vectors \(y\), every one of the \(n\) independent uniform columns of \(A\) must lie in the hyperplane \(y^\perp\), a probability of \(q^{-n}\). Thus
\[
q^{-m}\bigl[1+(q^m-1)q^{-n}\bigr]
=q^{-m}+q^{-n}-q^{-(m+n)},
\]
which proves both the probability and the total ordered-pair count after multiplication by \(q^{2mn}\).

**4. Semisimple rings and collisions.** By Artin–Wedderburn, each finite semisimple unital \(R\ne0\) is a finite product of full matrix rings over finite division rings; by Wedderburn's little theorem each finite division ring is a finite field. In a direct product an element is nilpotent exactly when every component is nilpotent (take the maximum of finitely many nilpotency indices). Independent uniform factors in \(R\) give independent uniform factors in each simple component. Apply step 3 at \(m=n=d_i\) and multiply componentwise probabilities. For the comparison field \(\mathbb F_{q^d}\), a product is nilpotent exactly when it is zero, so its probability is \(1-(1-q^{-d})^2=2q^{-d}-q^{-2d}\). This coincides with the matrix-ring formula, completing the proof.

## Verification

The supplied standalone `verify_rectangular_npp.py` independently constructs every ordered matrix pair in fifteen small prime-field cases, tests nilpotence via powers, determines each fixed-factor rank by elimination, and verifies both the conditional fiber count and the aggregate count. Cases cover \(q=2,3,5\), both rectangular orientations, and the \(3\times3\) binary case. Reproduce with `python3 verify_rectangular_npp.py`; the successful terminal marker is `VERIFY_OK`. These are finite corroborations; the unbounded prime-power theorem follows from the foregoing proof.

## Relationship to prior work

Sarma and Subedi introduced and investigated nilpotent-product probability for finite rings, proved direct-product multiplicativity (Proposition 2.2), and computed it for upper-triangular and scalar-diagonal matrix subrings (Section 2.3) in their October 2026 preprint. The matrix factors considered here are full matrix algebras, not those triangular subrings. The rectangular fixed-rank law and the full semisimple-ring formula are not asserted in those inspected sections. Leinster gave an exposition of the classical nilpotent-operator probability over finite fields; its single-operator count is reconstructed independently in step 1, while the probability of a product of two independent matrices is a different question. The componentwise product step itself is already known from Sarma–Subedi's Proposition 2.2; novelty is claimed only for the full-matrix rectangular calculation and its explicit semisimple consequence.

## Limitations

No formula is asserted for arbitrary finite nonsemisimple rings. The same probability need not determine a ring up to isomorphism; the explicit matrix/field collision demonstrates non-injectivity. Previous unindexed matrix-product literature could contain equivalent statements despite the reported comparisons, so originality remains subject to broader expert checking. The supplied exhaustive enumerations cover only small prime fields, while the proof handles all finite fields.

## References

1. D. Sarma and T. Subedi, *Nilpotent product probability of finite rings*, arXiv:2610.07892v1 (posted 6 October 2026), especially Proposition 2.2 and Section 2.3. https://arxiv.org/html/2610.07892v1
2. T. Leinster, *The probability that an operator is nilpotent*, arXiv:1912.12562 (2019), for the classical single-operator nilpotence count. https://arxiv.org/abs/1912.12562
