# Adjoint-rank distribution and commuting probability of radical-square-zero cyclic Nakayama algebras

## Finding

Let \(q\) be any prime power and \(n\ge2\). For the oriented cycle \(Q_n\) on vertices \(\mathbb Z/n\mathbb Z\), let \(J\) denote the arrow ideal in its path algebra, and set
\[
A_n(q)=\mathbb F_qQ_n/J^2.
\]
For \(x\in A_n(q)\), write \(r(x)=\operatorname{rank}_{\mathbb F_q}(\operatorname{ad}_x)\), where \(\operatorname{ad}_x(y)=xy-yx\). The complete rank enumerator is
\[
\boxed{P_{n,q}(z):=\sum_{x\in A_n(q)}z^{r(x)}
=(1+(q^2-1)z)^n+(q-1)(1-z)^n+q(q-1)^n(z^{n-1}-z^n).}
\]
Equivalently, for \(0\le k\le n\), the number of elements with adjoint rank \(k\) is exactly
\[
\boxed{N_{n,q}(k)=\binom nk\left((q^2-1)^k+(q-1)(-1)^k\right)
+q(q-1)^n\left(\mathbf1_{k=n-1}-\mathbf1_{k=n}\right).}
\]
Every rank from \(0\) to \(n\) occurs. In particular, exactly \(q\) elements are central, and the probability that two uniformly independently sampled elements commute is
\[
\boxed{\operatorname{Pr}(A_n(q))=
\frac{(q^2+q-1)^n+(q+1)(q-1)^{n+1}}{q^{3n}}.}
\]
The correction involving the two highest ranks comes from the unique cycle: it is absent when the incidence support is a proper forest.

## Assumptions and scope

The field \(\mathbb F_q\) is arbitrary and includes characteristic two. The quiver has \(n\) different vertices \(i\), exactly one arrow \(a_i:i\to i+1\) at each vertex, and indices are modulo \(n\). When \(n=2\), the two arrows point in opposite directions; they are distinct. All paths of length at least two vanish in the quotient. Its standard basis consists of primitive idempotents \(e_i\) and arrows \(a_i\), so \(\dim_{\mathbb F_q}A_n(q)=2n\) and \(|A_n(q)|=q^{2n}\). We fix multiplication by
\[
e_i e_j=\delta_{ij}e_i,\qquad e_i a_j=\delta_{ij}a_j,\qquad a_j e_i=\delta_{i,j+1}a_j,\qquad a_i a_j=0.
\]
The centralizer \(C_A(x)\) is the kernel of \(\operatorname{ad}_x\). The commuting probability is \(|\{(x,y)\in A^2:xy=yx\}|/|A|^2\).

## Proof

**1. Commutator rows.** Write arbitrary elements as
\[
x=\sum_i d_i e_i+\sum_i u_i a_i,\quad
y=\sum_i c_i e_i+\sum_i v_i a_i.
\]
By the multiplication rules, the diagonal coefficients of every commutator vanish and its coefficient on \(a_i\) is
\[
[x,y]_{a_i}=(d_i-d_{i+1})v_i-(c_i-c_{i+1})u_i.
\]
Put \(\delta_i=d_i-d_{i+1}\), and let \(S=\{i:\delta_i\ne0\}\). In the matrix of \(\operatorname{ad}_x\), each row indexed by \(i\in S\) has a unique pivot in the input-arrow column \(v_i\). These rows are independent and independent of all rows indexed by the complement \(S^c\). The remaining rows are scalar multiples \(-u_i(c_i-c_{i+1})\) of the oriented vertex-edge incidence rows. Consequently,
\[
r(x)=|S|+\operatorname{rank}\left(\{u_i(c_i-c_{i+1}):i\in S^c\}\right).
\]

**2. Forest versus full-cycle dependence.** If \(S\ne\varnothing\), the edge set \(S^c\) is a proper subset of an \(n\)-cycle and hence is a forest (for \(n=2\), the two opposite arrows give the two rows of the ordinary two-edge cycle). Incidence rows of an oriented forest are linearly independent over every field: eliminate a leaf and its unique incident edge, iteratively. Therefore
\[
r(x)=|S|+|\{i\notin S:u_i\ne0\}|\qquad(S\ne\varnothing).
\]
If \(S=\varnothing\), all diagonal coefficients \(d_i\) equal one common scalar. The full oriented cycle incidence rows have exactly one relation (their sum vanishes), and every proper subset is independent. Hence
\[
r(x)=\begin{cases}
|\{i:u_i\ne0\}|,&\text{if some }u_i=0,\
n-1,&\text{if all }u_i\ne0.
\end{cases}
\]
This exhausts all \(x\), all \(n\ge2\), and all characteristics.

**3. Weighted cycle transfer.** For a fixed diagonal vector \(d=(d_1,\ldots,d_n)\) with \(s=|S|>0\), the generating contribution from its \(q^n\) possible arrow coefficients equals
\[
\sum_{u\in\mathbb F_q^n}z^{r(d,u)}=(qz)^s(1+(q-1)z)^{n-s}.
\]
The same expression would count the case \(s=0\) if the full-cycle dependence did not occur. For a diagonal vector with \(s=0\), exactly \((q-1)^n\) all-nonzero arrow vectors have rank \(n-1\), rather than the naively assigned \(n\); and exactly \(q\) diagonal vectors have \(s=0\). Thus the required total correction is
\[
q(q-1)^n(z^{n-1}-z^n).
\]
To evaluate the naive contribution, put \(U=1+(q-1)z\) (the weight when \(d_i=d_{i+1}\)) and \(V=qz\) (the weight when \(d_i\ne d_{i+1}\)). The \(q\times q\) transfer matrix with diagonal \(U\) and off-diagonal \(V\) is \((U-V)I+V\mathbf1\mathbf1^T\), with eigenvalues \(U+(q-1)V\) of multiplicity one and \(U-V\) of multiplicity \(q-1\). For a closed cycle, its trace to the power \(n\) enumerates all diagonal colorings:
\[
\sum_{d\in\mathbb F_q^n}U^{n-|S|}V^{|S|}
=(U+(q-1)V)^n+(q-1)(U-V)^n.
\]
Substitution gives \(U+(q-1)V=1+(q^2-1)z\) and \(U-V=1-z\). Adding the full-support correction proves the asserted generating polynomial and its coefficient formula.

**4. Nonempty ranks and commuting probability.** The rank-zero coefficient is \(1+(q-1)=q\), corresponding precisely to scalar identity multiples. For \(1\le k\le n-2\), \((q^2-1)^k>(q-1)\) for \(q\ge2\) except vacuous cases, so the coefficients are positive; \(N_{n,q}(n-1)>0\) from its explicit positive correction. For \(k=n\), choose diagonal labels with \(d_i\ne d_{i+1}\) for at least one edge and choose \(u_i\ne0\) for every remaining equal-labeled edge, giving rank \(n\); such a coloring exists for all \(n\ge2\), so the last coefficient is positive. Therefore every rank occurs.

Since \(\ker\operatorname{ad}_x=C_A(x)\), its cardinality is \(q^{2n-r(x)}\), and summing over \(x\) yields
\[
\operatorname{Pr}(A_n(q))
=\frac{\sum_xq^{2n-r(x)}}{q^{4n}}=q^{-2n}P_{n,q}(q^{-1}).
\]
Inserting the polynomial and simplifying gives exactly
\[
\frac{(q^2+q-1)^n+(q+1)(q-1)^{n+1}}{q^{3n}}.
\]
This completes the proof.

## Verification

The included standalone program `verify.py` constructs the full multiplication table in the basis \(e_i,a_i\), forms each full \(2n\times2n\) commutator matrix independently of the incidence or transfer-matrix proof, and computes its rank by Gaussian elimination. It exhaustively enumerates elements for the pairs
\[
(q,n)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2),(4,3),(5,2).
\]
The \(q=4\) cases use \(\mathbb F_2[t]/(t^2+t+1)\); all other checked fields are prime fields. The computed rank histograms exactly match \(N_{n,q}(k)\) and sum to \(q^{2n}\). The program prints `VERIFY_OK`. These finite tests corroborate the general proof but cannot replace it.

## Relationship to prior work

Chen and Yang's work on radical-square-zero quiver algebras studies homotopy categories and Gorenstein-projective representations. Gao, Külshammer, Kvamme, and Psaroudakis explicitly treat cyclic radical-square-zero Nakayama algebras in representation-theoretic categories. Their inspected structural results concern modules and functors rather than the rank distribution of inner derivations.

Dutta, Basnet, and Nath examine finite-ring commuting probabilities and centralizer constraints; their inspected results do not imply this cyclic quiver formula. An independently published count for generalized Kronecker path algebras treats two vertices linked by parallel arrows all in one direction, not an oriented cycle. In that acyclic family, an element's arrow-space commutator has a single common diagonal difference; no full-cycle incidence relation of the present form appears.

The rank polynomial here records every centralizer dimension, not only the commuting probability. Its top-two-rank correction isolates exactly the global cycle dependence. The derivation uses an ordinary weighted transfer matrix but combines it with a rank-sensitive incidence argument.

## Limitations

The result is for the split, basic, radical-square-zero Nakayama algebra with exactly one arrow per edge and a consistently oriented cycle. It is not a classification of all finite rings, all cyclic quiver algebras with longer radical length, or all radical-square-zero quivers. The rank distribution does not determine full commutator fibers or the lattice of distinct centralizers. Potential coverage by an unlocated general theorem on commutator rank enumerators for quiver algebras remains an originality risk. Independent mathematical validation has not been performed.

## References

1. X.-W. Chen and D. Yang, “Homotopy categories, Leavitt path algebras, and Gorenstein projective modules,” arXiv:1301.0195v1, first public 2 January 2013.
2. J. Dutta, D. K. Basnet, and R. K. Nath, “On commuting probability of finite rings,” arXiv:1510.08211v1, first public 28 October 2015.
3. N. Gao, J. Külshammer, S. Kvamme, and C. Psaroudakis, “A functorial approach to monomorphism categories II: Indecomposables,” arXiv:2303.07753v1, first public 14 March 2023.
