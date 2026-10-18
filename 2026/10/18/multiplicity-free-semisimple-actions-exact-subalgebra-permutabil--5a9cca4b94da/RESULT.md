# Multiplicity-free semisimple actions: exact subalgebra-permutability counts

## Finding

Let \(q\) be a prime power, let \(r\ge2\), and let \(f_1,\ldots,f_r\in\mathbb F_q[t]\) be pairwise distinct monic irreducible polynomials of degrees \(d_i\ge2\). Put
\[
V_i=\mathbb F_q[t]/(f_i),\quad V=\bigoplus_{i=1}^rV_i,\quad d=\sum_{i=1}^r d_i.
\]
Let \(A\) act on \(V\) by multiplication by \(t\) and set \(L=\mathbb F_qh\ltimes_A V\), with \([h,v]=Av\) and \([V,V]=0\). Two Lie subalgebras \(U,W\) are *permutable* when \(U+W\) is a Lie subalgebra, equivalently \([U,W]\subseteq U+W\). Write \(\mathcal L(L)\) for all Lie subalgebras, including zero and \(L\), and \(\operatorname{sd}(L)\) for the proportion of ordered permutable pairs.

For every subset \(S\subseteq[r]\), write \(d_S=\sum_{i\in S}d_i\). Define
\[
G_a(q)=\sum_{k=0}^a {a\brack k}_q,\qquad
H_q(a,b)=\sum_{k=0}^a {a\brack k}_q q^{b(a-k)},
\]
where \({a\brack k}_q\) denotes the Gaussian binomial coefficient, with \(G_0(q)=1\). Then the subalgebra total and the **exact ordered permutable-pair count** are
\[
\boxed{N=|\mathcal L(L)|=G_d(q)+\prod_{i=1}^r(1+q^{d_i})},
\]
\[
\boxed{
P=G_d(q)^2+2\sum_{S\subseteq[r]}q^{d-d_S}
\sum_{T\subseteq[r]\setminus S}H_q(d_S,d_T)
+\prod_{i=1}^r(1+3q^{d_i})}.
\]
Thus \(\boxed{\operatorname{sd}(L)=P/N^2}\). In particular the number of ordered permutable pairs in which **neither subalgebra is contained in \(V\)** is the completely factored product
\[
\boxed{P_{\mathrm{ext},\mathrm{ext}}=\prod_{i=1}^r(1+3q^{d_i})}.
\]
These counts depend on the action only through the multiset of irreducible-factor degrees, not the coefficients of the polynomials.

For fixed degrees \(d_1,\ldots,d_r\) and \(q\to\infty\) through finite fields realizing the prescribed distinct irreducible factors,
\[
\boxed{\lim_{q\to\infty}\operatorname{sd}(L)=
\begin{cases}
\tfrac14,&d=4,\\
1,&d\ge5.
\end{cases}}
\]
Since \(r\ge2\) and all \(d_i\ge2\), these are the only possibilities. The \(d=4\) case necessarily has \(r=2\) and \(d_1=d_2=2\). There the formulas simplify to
\[
N=2q^4+3q^3+6q^2+3q+6,
\]
\[
P=q^8+6q^7+21q^6+34q^5+67q^4+64q^3+79q^2+36q+36.
\]
For instance two distinct irreducible quadratics over \(\mathbb F_3\) give \(N=312\), \(P=51264\), and \(\operatorname{sd}(L)=89/169\).

## Assumptions and scope

The characteristic is unrestricted. The irreducible factors must be **distinct** (multiplicity-free module) and each degree at least two (no invariant one-dimensional quotient). Existence for specified degrees is assumed; for fixed degrees all sufficiently large finite fields allow the required distinct irreducibles. The theorem concerns ordinary \(\mathbb F_q\)-linear Lie subalgebras and ordered pairs. It does not identify the factor polynomials from the probability, and does not cover one-dimensional factors, repeated factors, or nonsemisimple actions.

## Proof

**1. Subalgebra classification.** As an \(\mathbb F_q[t]\)-module, \(V=\bigoplus_iV_i\) is semisimple with pairwise nonisomorphic simple summands. Its \(A\)-invariant subspaces are therefore exactly \(V_S=\bigoplus_{i\in S}V_i\) for \(S\subseteq[r]\). Every vector subspace of \(V\) is an abelian Lie subalgebra, giving \(G_d(q)\) subalgebras. If a subalgebra \(X\) is not contained in \(V\), then \(X\cap V\) is \(A\)-invariant: an element \(h+u\in X\) acts on \(X\cap V\) by \(A\). Thus
\[
X=X_{S,u}=V_S\oplus\mathbb F_q(h+u),\qquad u\in V/V_S.
\]
Conversely all such spaces are subalgebras, and two of them are equal exactly when their subsets \(S\) and cosets \(u+V_S\) coincide. There are \(q^{d-d_S}\) for each \(S\). Summing gives \(N=G_d(q)+\sum_Sq^{d-d_S}=G_d(q)+\prod_i(1+q^{d_i})\).

**2. Pairs inside the abelian ideal.** Any two subspaces of \(V\) permute, yielding exactly \(G_d(q)^2\) ordered pairs.

**3. Mixed pairs.** Let \(U\subseteq V\) be a vector subspace, and let \(X=X_{S,u}\) be as above. Their sum is a Lie subalgebra precisely when \(A(U+V_S)\subseteq U+V_S\): all potentially nonzero brackets are of the form \([h+u,w]=Aw\). Under \(V/V_S\cong\bigoplus_{i\notin S}V_i\), the projected subspace \((U+V_S)/V_S\) must therefore equal \(V_T\) for a unique \(T\subseteq[r]\setminus S\). With \(a=d_S\), \(b=d_T\), the number of such \(U\) projecting **onto exactly** \(V_T\) equals
\[
H_q(a,b)=\sum_{k=0}^{a}{a\brack k}_q q^{b(a-k)}.
\]
Indeed choose \(K=U\cap V_S\), of dimension \(k\), in \({a\brack k}_q\) ways; then \(U/K\) is the graph of one of \(q^{b(a-k)}\) linear maps from \(V_T\) to \(V_S/K\). This count is independent of the coset \(u+V_S\). Multiplication by \(q^{d-d_S}\), summation over \(S,T\), and doubling for pair order gives the middle term in \(P\).

**4. Two exterior subalgebras.** Let \(X=X_{S,u}\), \(Y=X_{T,v}\), and \(W=V_{S\cup T}\). The vector sum \(X+Y\) is \(W+\mathbb F_q(h+u)+\mathbb F_q(h+v)\). Its closure under brackets is equivalent to \(A(v-u)\) lying in this vector sum. Modulo \(W\), either \(v-u\) is zero or it spans an \(A\)-invariant line. Every simple constituent of \(V/W\) has dimension at least two, and the quotient has no invariant line. Consequently
\[
X+Y\text{ is a Lie subalgebra}\quad\Longleftrightarrow\quad u-v\in W.
\]
Here the expression is independent of choices of coset representatives. Matching the images of \(u\) and \(v\) in \(V/W\) gives
\[
q^{d-d_{S\cup T}}q^{d_{S\cup T}-d_S}q^{d_{S\cup T}-d_T}
=q^{d+d_{S\cup T}-d_S-d_T}
\]
ordered pairs of the specified types. For each index \(i\), the exponent contribution is \(0\) when \(i\in S\cap T\) and \(d_i\) for any of the other three membership choices. Therefore
\[
\sum_{S,T\subseteq[r]}q^{d+d_{S\cup T}-d_S-d_T}
=\prod_{i=1}^r(1+3q^{d_i}).
\]
Adding the three disjoint categories proves \(P\).

**5. Degree rigidity and limiting probabilities.** The displayed formulas depend only on \(q\) and the multiset of dimensions \(d_i\). The dominant term of \(G_d(q)\) is \(c_dq^{\lfloor d^2/4\rfloor}\), where \(c_d=1\) for even \(d\) and \(c_d=2\) for odd \(d\). If \(d\ge5\), then \(\lfloor d^2/4\rfloor>d\), while \(\prod_i(1+q^{d_i})=O(q^d)\). Both the number of exterior subalgebras and hence the number of pairs involving one are negligible relative to \(G_d(q)^2\); thus \(\operatorname{sd}(L)\to1\). If \(d=4\), necessarily the factor degrees are \((2,2)\). In that case \(G_4(q)=q^4+3q^3+4q^2+3q+5\), the exterior-subalgebra count is \((1+q^2)^2\), and the explicit polynomial for \(P\) above has leading coefficient \(1\) at degree \(8\), versus leading coefficient \(4\) for \(N^2\). Thus \(\operatorname{sd}(L)\to1/4\).

## Verification

The standalone `verify.py` enumerates all subspaces of the abelian ideal using reduced row-echelon matrices, constructs all exterior subalgebras from the displayed classification, and independently checks every bracket and every ordered pair for closure of the vector sum. It separately computes the Gaussian-sum prediction. Three base cases use irreducible actions of degrees \(2\) or \(3\), and two genuinely multi-factor cases use distinct irreducibles of degrees \((2,2)\) over \(\mathbb F_3\) and \((2,3)\) over \(\mathbb F_2\). The corresponding exact pairs are \((N,P)=(312,51264)\) and \((419,144477)\). Every comparison passes. These are finite reproducibility checks; Steps 1–5 establish the theorem for all permitted fields and degrees.

## Relationship to prior work

Muhie, Otera, and Russo introduced the subalgebra-commutativity degree and studied Heisenberg and special-linear examples, with general inequalities [1]. A publicly accessible three-dimensional classification determines the same invariant in dimension three, including the case of one irreducible quadratic action [2]. Neither result covers the present multiplicity-free actions with at least two nonlinear irreducible constituents, hence dimensions at least five.

An indexed result for irreducible elementary-abelian Frobenius groups [3] has an analogous single-constituent subgroup formula; it is **not** a statement about Lie-subalgebra pairs with several invariant irreducible summands. The new two-exterior product \(\prod_i(1+3q^{d_i})\) and the mixed Gaussian graph count require interaction between distinct invariant blocks. Generic lattice/submodule classification does not by itself supply those pairwise bracket tests. The formula should not be construed as originality of Gaussian binomial coefficients, semisimple module theory, or the three-dimensional special case.

## Limitations

Multiplicity-freeness and the exclusion of linear factors are essential to this proof. Repeated irreducible factors admit many non-coordinate invariant subspaces. A one-dimensional factor permits invariant residual lines, invalidating the exterior–exterior criterion in Step 4. The invariant depends only on irreducible-factor degrees and therefore cannot distinguish different polynomials having the same degrees. The finite-field tests do not constitute a computer certification of arbitrary-parameter identities. An older equivalent result formulated as lattice-factorization enumerators, rather than subalgebra commutativity, remains a literature risk; no independent audit has been conducted.

## References

1. S. K. Muhie, D. E. Otera, F. G. Russo, *On the number of modular pairs in finite dimensional Lie algebras on finite fields*, arXiv:2609.19086v1 (first public 16 September 2026), https://arxiv.org/abs/2609.19086.
2. *Plane counts control subalgebra commutativity in dimension three*, publicly available mathematical record, 18 September 2026, publicly indexed at https://github.com/published-finding corpus/2026 (record title above).
3. *Relative subgroup commutativity in irreducible elementary-abelian Frobenius groups*, publicly available mathematical record, 4 October 2026, publicly indexed at https://github.com/published-finding corpus/2026 (record title above).
