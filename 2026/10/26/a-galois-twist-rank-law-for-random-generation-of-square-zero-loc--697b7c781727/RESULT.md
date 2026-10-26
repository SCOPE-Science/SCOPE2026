# A Galois-twist rank law for random generation of square-zero local algebras

## Finding

Let \(q\) be any prime power, \(m\geq1\), \(K=\mathbb F_{q^m}\), \(Q=q^m\), and \(\Gamma=\operatorname{Gal}(K/\mathbb F_q)\). Let \(A\) be a finite-dimensional associative unital \(\mathbb F_q\)-algebra whose Jacobson radical \(J\) satisfies \(J^2=0\) and whose residue algebra \(A/J\) is \(K\). After choosing a coefficient-field section, decompose the \(K\)-bimodule
\[
 J=\bigoplus_{\sigma\in\Gamma} K^{k_\sigma},\qquad a\cdot v\cdot b=a\,v\,\sigma(b),
\]
where all \(k_\sigma\) are nonnegative integers. Choose \(r\geq1\) independent uniform elements \(X_1,\ldots,X_r\in A\), put \(B=\mathbb F_q\langle X_1,\ldots,X_r\rangle\) (with identity), and condition on the event \(\pi(B)=K\), where \(\pi:A\to K\) is the radical quotient map.

For each \(\sigma\), define \(H_\sigma=\dim_K((B\cap J)\cap K^{k_\sigma})\) and
\[
 n_\sigma=\begin{cases}r,&\sigma=\mathrm{id},\\r-1,&\sigma\ne\mathrm{id}.\end{cases}
\]
**The joint conditional law of all \(H_\sigma\) is a product of independent finite-field matrix-rank laws:**
\[
 \Pr\bigl((H_\sigma)_\sigma=(h_\sigma)_\sigma\mid\pi(B)=K\bigr)
 =\prod_{\sigma\in\Gamma}Q^{-n_\sigma k_\sigma}
 {k_\sigma\brack h_\sigma}_Q
 \prod_{j=0}^{h_\sigma-1}(Q^{n_\sigma}-Q^j).
\]
Here the Gaussian coefficient counts \(h_\sigma\)-subspaces of \(K^{k_\sigma}\), and factors outside \(0\le h_\sigma\le\min(n_\sigma,k_\sigma)\) mean zero. In particular, \(\dim_{\mathbb F_q}B=m(1+\sum_\sigma H_\sigma)\) on this event.

The unconditional probability of generating the entire algebra is exactly
\[
 \boxed{\Pr(B=A)=\left(\sum_{d\mid m}\mu(m/d)q^{dr-mr}\right)
 \prod_{\sigma\in\Gamma}\prod_{j=0}^{k_\sigma-1}(1-Q^{j-n_\sigma}).}
\]
An empty product is one. The least **positive** \(r\) with nonzero probability is
\[
 \max\!\left(1,k_{\mathrm{id}},1+\max_{\sigma\ne\mathrm{id}}k_\sigma\right),
\]
where the last maximum is defined to be zero when there are no nonidentity components. When \(A=\mathbb F_q\), the algebra also admits the empty generating set; the displayed formula concerns positive tuple lengths.

## Assumptions and scope

All algebras are associative, unital, and finite-dimensional over \(\mathbb F_q\). The residue \(A/J\) must be a **single** finite field, not a product of fields or a matrix algebra, and \(J^2=0\). The Wedderburn--Malcev splitting is available because the residue field is separable over \(\mathbb F_q\). The square-zero multiplication is \((a,u)(b,v)=(ab,av+ub)\), with right actions twisted by the specified \(\sigma\). The tuple length \(r\) is any positive integer. No restriction on characteristic or multiplicities is imposed.

The event \(\pi(B)=K\) has positive probability for every \(r\ge1\), because \(K\) admits one generator over \(\mathbb F_q\). The multiplicities \(k_\sigma\) are intrinsic to the \(K\)-bimodule up to the naturally specified coefficient field; changing a coefficient section does not change their values because \(J^2=0\).

## Proof

**1. Split the radical into Galois-twisted summands.** The separability of \(K/\mathbb F_q\) yields a copy of \(K\) inside \(A\). Its enveloping algebra is
\[
 K\otimes_{\mathbb F_q}K\cong\prod_{\sigma\in\Gamma}K
\]
via \(a\otimes b\mapsto(a\sigma(b))_\sigma\). Since \(J\) is a module over this finite product of fields, it decomposes uniquely into the indicated isotypic \(K\)-spaces.

**2. Identify the radical part of a generated algebra.** Fix residues \(a_i=\pi(X_i)\) that generate \(K\) as an \(\mathbb F_q\)-algebra; write \(X_i=(a_i,(b_{i,\sigma})_\sigma)\). Let \(N=B\cap J\). Because \(\pi(B)=K\) and \(J^2=0\), multiplying elements of \(N\) on either side by lifts from \(B\) makes \(N\) a \(K\)-sub-bimodule of \(J\); hence \(N=\bigoplus_\sigma N_\sigma\).

The restriction \(B\to K\) has kernel \(N\), and hence defines an algebra section \(s:K\to A/N\). Its \(\sigma\)-component has form \(s(a)=(a,D_\sigma(a))\), with
\[
 D_\sigma(ab)=aD_\sigma(b)+D_\sigma(a)\sigma(b).
\]
When \(\sigma=\mathrm{id}\), every such \(\mathbb F_q\)-linear derivation is zero because \(K/\mathbb F_q\) is separable. When \(\sigma\ne\mathrm{id}\), commutativity of \(K\) gives
\[
 D_\sigma(a)(\sigma(c)-c)=D_\sigma(c)(\sigma(a)-a).
\]
Choosing \(c\) with \(\sigma(c)\ne c\) shows \(D_\sigma(a)=t_\sigma(\sigma(a)-a)\) for a fixed \(t_\sigma\in K^{k_\sigma}/N_\sigma\). This derivation identity is valid in every characteristic.

Set \(d_{i,\sigma}=\sigma(a_i)-a_i\). For \(\sigma=\mathrm{id}\), put \(M_\sigma=\operatorname{span}_K\{b_{1,\sigma},\ldots,b_{r,\sigma}\}\). For \(\sigma\ne\mathrm{id}\), since the residues generate \(K\), some \(d_{j,\sigma}\ne0\). Fix any such index \(j=j(\sigma)\), and put
\[
 M_\sigma=\operatorname{span}_K\{b_{i,\sigma}-d_{i,\sigma}d_{j,\sigma}^{-1}b_{j,\sigma}:i\ne j\}.
\]
The section formula shows \(M_\sigma\subseteq N_\sigma\) in all cases.

Conversely, form \(M=\bigoplus_\sigma M_\sigma\) and define a map \(D_M:K\to J/M\) with identity component zero and nonidentity components
\[
 D_{M,\sigma}(a)=d_{j,\sigma}^{-1}b_{j,\sigma}(\sigma(a)-a)\pmod {M_\sigma}.
\]
Each component is a derivation. Consequently the inverse image in \(A\) of its graph \(\{(a,D_M(a)):a\in K\}\subset A/M\) is a unital subalgebra. By construction it contains each \(X_i\), and intersects \(J\) in exactly \(M\). Thus \(B\cap J\subseteq M\). Together with the preceding inclusion this gives \(N=M\), with no assumption that \(B\) already contains the chosen coefficient field.

**3. Calculate the conditional law.** Given the residues \((a_i)\), the vectors \(b_{i,\sigma}\) are independent and uniform in their respective \(K^{k_\sigma}\). For \(\sigma=\mathrm{id}\), the \(r\) spanning vectors defining \(N_\sigma\) are independent uniform vectors. For \(\sigma\ne\mathrm{id}\), the invertible linear change of variables that keeps \(b_{j,\sigma}\) and replaces all other vectors by the displayed differences makes the \(r-1\) spanning vectors independent uniform vectors. These changes are separate for every \(\sigma\); the ranks remain mutually independent and their distribution does not depend on which field-generating residue tuple was fixed.

For \(n\) independent uniform vectors in \(K^k\), the number of ordered \(n\)-tuples spanning a prescribed \(h\)-dimensional subspace equals \(\prod_{j=0}^{h-1}(Q^n-Q^j)\), by counting surjective maps \(K^n\to K^h\). Multiplying by \({k\brack h}_Q\) and dividing by \(Q^{nk}\) proves the joint rank formula.

**4. Uncondition and extract generation.** The residues generate \(K\) precisely when they do not all lie in any proper subfield. Möbius inversion in the divisor lattice of \(m\) yields
\[
 \#\{(a_1,\ldots,a_r):\mathbb F_q[a_1,\ldots,a_r]=K\}
 =\sum_{d\mid m}\mu(m/d)q^{dr}.
\]
Full generation requires both \(\pi(B)=K\) and \(N=J\). Evaluating the independent rank probabilities at \(h_\sigma=k_\sigma\) proves the boxed formula and its strict positivity threshold. When \(\pi(B)=K\), the rank identity also yields \(\dim_{\mathbb F_q}B=m(1+\sum_\sigma H_\sigma)\).

## Verification

The standalone `verify_generation.py` implements the multiplication law for \(K=\mathbb F_4\), enumerates all ordered generating pairs for six small square-zero algebras, and independently closes each generated subalgebra under linear combination and multiplication. Its outputs agree exactly with the predicted pair-generation counts \(12/16\), \(180/256\), \(144/256\), \(2160/4096\), \(0/4096\), and \(2160/4096\) for the six listed twist multiplicities. It also checks two one-generator counts, the complete two-component conditional profile \((48,144,720,2160)\) in a fixed ordering, and the repeated-twist rank distribution \((192,2880)\). The script uses no third-party package. These checks establish finite instances only; the all-field/all-multiplicity assertion follows from the proof.

## Relationship to prior work

Sercombe and Shalev, *Random generation of associative algebras* (arXiv:2009.01115, first public version 2020-09-02; subsequently J. London Math. Soc. 109 (2024), e12827), establish random-generation bounds and a classification of conjugacy classes of maximal subalgebras (notably their Theorems 1.10 and 2). Those results supply the broad random-generation framework but do not state the above independent full conditional Galois-isotypic rank law or its explicit all-tuple-length product formula. Iovanov and Sistko, *Maximal Subalgebras of Finite-Dimensional Algebras* (arXiv:1705.00762), give a general structural theory of maximal subalgebras; this is compatible with, but does not explicitly enumerate, the conditional generated-subalgebra profiles here. Kravchenko, Mazur, and Petrenko, *Generators of maximal orders* (J. Algebra 426 (2015), 32–50), develop general finite-algebra generator counting and lifting recursions, not this explicit twist-rank distribution. Standard Wedderburn--Malcev separability and finite-field rank counts are used, not claimed as new.

The present claim is an explicit, testable refinement for all square-zero local algebras with **one finite-field residue**, including noncommutative Galois-twisted examples. No claim is made for multiple simple residue factors or radicals with nonzero square.

## Limitations

The original formulation requires a square-zero radical and a single field residue. The conditional rank law does not describe arbitrary generated subalgebras whose residue image is a proper subfield; only their contribution to the full-generation probability is handled through Möbius inversion. The theorem is not independently audited. Although targeted comparisons found no identical closed law, earlier equivalent formulas could exist under terminology involving bimodule multiplicities, field complements, or algebra-generation zeta functions. General prior maximal-subalgebra theorems are strong structural antecedents and represent a residual priority risk.

## References

1. D. Sercombe and A. Shalev, *Random generation of associative algebras*, arXiv:2009.01115, first posted 2020-09-02; J. London Math. Soc. 109 (2024), e12827, doi:10.1112/jlms.12827.
2. M. Iovanov and A. Sistko, *Maximal Subalgebras of Finite-Dimensional Algebras*, arXiv:1705.00762, first posted 2017-05-02; Forum Math. 31 (2019), doi:10.1515/forum-2019-0033.
3. R. Kravchenko, M. Mazur, and B. Petrenko, *Generators of maximal orders*, J. Algebra 426 (2015), 32–50, doi:10.1016/j.jalgebra.2014.11.020.
