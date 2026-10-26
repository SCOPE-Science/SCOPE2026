# Square-zero geometry and a four-term recurrence for truncated cyclic Nakayama radicals

## Finding

Let \(n\ge4\) and let \(Q_n\) be the consistently oriented cycle on \(n\) vertices. Over any field \(k\), put \(A_n(k)=kQ_n/J^4\), where \(J\) is the arrow ideal, and write \(\mathcal X_n(k)=\{x\in\operatorname{rad}A_n(k):x^2=0\}\).

For a finite field \(k=\mathbb F_q\), write \(N_n(q)=|\mathcal X_n(\mathbb F_q)|\). A subset \(S\subseteq\mathbb Z/n\mathbb Z\) is *cyclically independent* when it contains no pair of consecutive vertices. Define

\[
p_j(S)=|\{i\in S:i+j\in S\}|,\qquad j\in\{2,3\},
\]

with all indices read modulo \(n\). Then

\[
\boxed{N_n(q)=\sum_{\substack{S\subseteq\mathbb Z/n\mathbb Z\\S\text{ cyclically independent}}}(q-1)^{|S|}q^{2n-2|S|+p_2(S)+p_3(S)}.}
\]

In particular, the entire sequence has an order-four recurrence with polynomial coefficients:

\[
\boxed{N_{n+4}(q)=q^2N_{n+3}(q)+q^3(q-1)N_{n+2}(q)-q^6(q-1)^2N_n(q),\quad n\ge4.}
\]

Initial values are

\[
\begin{aligned}
N_4(q)&=q^6(3q^2-2),\\
N_5(q)&=q^9(6q-5),\\
N_6(q)&=q^9(6q^3-9q+4),\\
N_7(q)&=q^{11}(8q^3-14q+7).
\end{aligned}
\]

Over any algebraically closed field \(k\), \(\mathcal X_n(k)\) is the \(k\)-point set of a reduced affine algebraic set of dimension exactly \(2n\). Its number of top-dimensional geometrically irreducible components is

\[
\boxed{c_n=1+\sum_{k=\lceil n/3\rceil}^{\lfloor n/2\rfloor}\frac{n}{k}\binom{k}{n-2k}.}
\]

Here “reduced affine algebraic set” refers to the reduced structure on the zero locus of \(x^2\), not an assertion that the scheme defined by the quadratic equations is reduced. For \(n=4,5,6,7,8\), the numbers of top-dimensional components are \(3,6,6,8,11\). For fields of characteristic two, \(N_n(q)\) also equals the number of elements \(g\in1+\operatorname{rad}A_n(\mathbb F_q)\) satisfying \(g^2=1\), including the identity.

## Assumptions and scope

The quiver \(Q_n\) has vertices \(i\in\mathbb Z/n\mathbb Z\) and one arrow from \(i\) to \(i+1\). For each \(j\in\{1,2,3\}\), let \(P_i^{(j)}\) be the unique oriented path of length \(j\) starting at \(i\). The radical is a \(3n\)-dimensional vector space with basis the \(P_i^{(j)}\). All proofs are characteristic-independent; \(q\) is an arbitrary prime power. The geometry concerns the reduced variety defined by the square-zero equations *inside the radical*, not all square-zero elements of a matrix algebra and not all representations of \(Q_n\).

## Proof

**1. Literal multiplication equations.** Each \(x\in\operatorname{rad}A_n(k)\) is uniquely

\[
x=\sum_i\bigl(\alpha_iP_i^{(1)}+\beta_iP_i^{(2)}+\gamma_iP_i^{(3)}\bigr).
\]

Concatenation of paths, with paths of length at least four set to zero, gives

\[
x^2=\sum_i\alpha_i\alpha_{i+1}P_i^{(2)}+
\sum_i(\alpha_i\beta_{i+1}+\beta_i\alpha_{i+2})P_i^{(3)}.
\]

Thus \(x^2=0\) if and only if

\[
\alpha_i\alpha_{i+1}=0,\qquad
\alpha_i\beta_{i+1}+\alpha_{i+2}\beta_i=0
\quad\text{for all }i.
\]

The \(\gamma_i\) are unrestricted. The support \(S=\{i:\alpha_i\ne0\}\) of a solution is cyclically independent. For fixed \(\alpha\), define \(L_\alpha:k^n\to k^n\) by \((L_\alpha\beta)_i=\alpha_{i+2}\beta_i+\alpha_i\beta_{i+1}\).

**2. Exact, coefficient-independent rank.** Consider the bipartite graph of nonzero entries of \(L_\alpha\), with vertices the row and column indices. Each occupied site \(i\in S\) contributes exactly two distinct edges: the entry at row \(i\), column \(i+1\), and the entry at row \(i-2\), column \(i-2\). There are therefore \(2|S|\) edges. A row has degree two exactly when \(i,i+2\in S\), accounting for \(p_2(S)\) degree-two row vertices. A column has degree two exactly when two occupied indices are three steps apart, accounting for \(p_3(S)\) degree-two column vertices.

No nonzero matrix entry can simultaneously belong to a degree-two row and a degree-two column. For the entry at row \(i\), column \(i+1\), this would require both \(i+2\in S\) and \(i+3\in S\), impossible by independence. For the entry at row \(i\), column \(i\), it would require both \(i\in S\) and \(i-1\in S\), again impossible. Hence every nontrivial connected component of the bipartite graph consists of either one edge or two edges meeting at one vertex. Since all its entries are nonzero, each such component contributes rank exactly one over **every** field. Consequently

\[
\operatorname{rank}(L_\alpha)=2|S|-p_2(S)-p_3(S).
\]

The argument uses \(n\ge4\) to ensure that each occupied site contributes two distinct matrix entries. Fixing \(S\), there are \((q-1)^{|S|}\) choices of \(\alpha\), exactly \(q^{n-\operatorname{rank}L_\alpha}\) choices of \(\beta\), and \(q^n\) choices of \(\gamma\). Summing gives the displayed exact point-count formula.

**3. Five-state transfer and recurrence.** For a cyclic support write \(s_i\in\{0,1\}\) for its indicator. The point count may be rewritten

\[
N_n(q)=q^{2n}\sum_{s_is_{i+1}=0}
\prod_i\left(\frac{q-1}{q^2}\right)^{s_i}
q^{s_is_{i+2}+s_is_{i+3}}.
\]

Use the ordered states \(000,001,010,100,101\), the binary words of length three with no adjacent ones. A transition \((a,b,c)\to(b,c,d)\) is allowed precisely when \(cd=0\); give it weight \(q^2\) if \(d=0\), and \((q-1)q^{a+b}\) if \(d=1\). The transfer matrix is

\[
M(q)=\begin{pmatrix}
q^2&q-1&0&0&0\\
0&0&q^2&0&0\\
0&0&0&q^2&q(q-1)\\
q^2&q(q-1)&0&0&0\\
0&0&q^2&0&0
\end{pmatrix}.
\]

A closed walk of length \(n\) is the data of one labeled cyclic support, and the product of its weights equals that support's contribution to \(N_n(q)\). Thus \(N_n(q)=\operatorname{tr}(M(q)^n)\) for \(n\ge4\). Direct expansion yields

\[
\det(zI-M(q))=z\left(z^4-q^2z^3-q^3(q-1)z^2+q^6(q-1)^2\right).
\]

Cayley–Hamilton gives the recurrence. Direct evaluation of the support sum for \(n=4,5,6,7\) gives the stated initial values.

**4. Dimension and top components.** For an independent \(S\), the locus of solutions with \(\operatorname{supp}(\alpha)=S\) is a vector bundle of rank \(n-\operatorname{rank}(L_\alpha)+n\) over the torus \((\mathbb G_m)^{|S|}\); its rank is constant by Step 2. It is therefore geometrically irreducible and has dimension

\[
d(S)=2n-|S|+p_2(S)+p_3(S).
\]

Every occupied vertex has at most one occupied successor two or three positions ahead, because those two candidate successors are adjacent. Hence \(p_2(S)+p_3(S)\le|S|\), and \(d(S)\le2n\). The empty-support stratum is an affine space of dimension \(2n\), so the whole reduced zero locus has dimension exactly \(2n\).

A nonempty independent support has dimension \(2n\) precisely when every gap between consecutive occupied vertices around the cycle is two or three. If such a support has \(k\) vertices and \(b\) gaps of length three, then \(2k+b=n\); the remaining gaps have length two. The number of labeled cyclic supports with those gaps is \(\frac nk\binom{k}{b}\): choose a distinguished occupied start and a cyclic ordered gap sequence, then divide by the \(k\) choices of distinguished occupied vertex. Distinct top-dimensional supports have distinct closures: a support can specialize only by deleting occupied positions, and deleting any position from a gap-two-or-three cyclic support produces a gap of length at least four. Their closures, together with the empty-support affine space, are therefore exactly the top-dimensional irreducible components. Summation over \(k\) proves the formula for \(c_n\).

Finally, in characteristic two, \((1+x)^2=1+x^2\), yielding the stated group interpretation.

## Verification

The accompanying standalone script `verify_cycle_squarezero.py` uses integer transfer matrices and literal finite-field multiplication. It verifies the support formula against exhaustive coefficient enumeration, with the free length-three coefficients accounted for by an exact factor \(q^n\), for \((n,q)=(4,2),(5,2),(6,2),(7,2),(4,3),(5,3),(6,3),(4,4),(5,4)\). For the extension field of order four it implements the irreducible polynomial \(t^2+t+1\), rather than treating it as integers modulo four. Additional checks compare literal path concatenation with the two displayed equations; matrix traces and the recurrence are checked over four finite-field sizes and the top-component support count over \(4\le n\le15\). All asserted infinite-field and all-\(n\) conclusions are proved above independently of these finite experiments.

## Relationship to prior work

Truncated cyclic quiver algebras are classical; Xu, Han and Jiang analyze Hochschild cohomology of general truncated quiver algebras, explicitly including truncated basic cycles. Their cohomological theorems do not provide a square-zero radical point count, transfer recurrence or top-component census. Wolf studies nilpotent representations of an oriented cycle through generic Hall algebras and generic-extension monoids; those are representations and extension-count invariants, not the locus of square-zero elements in the radical of the fixed finite-dimensional algebra. Related computations of ordinary conjugacy-class spectra for groups arising from fourth-truncated cyclic quiver algebras concern class sizes and do not assign the square-zero condition to elements. The statements above are compared as implications, not merely as title matches. None of these inspected results supplies the formulas without an additional calculation. This is not a claim that all earlier literature has been exhausted; a previously published equivalent enumeration under another name remains possible.

## Limitations

The theorem assumes a consistently oriented simple cycle with at least four vertices and truncation at paths of length four. It does not classify the scheme-theoretic embedded or nonreduced structure of the quadratic zero locus, nor all irreducible components of dimensions below \(2n\). The group involution interpretation is limited to characteristic two. Finite tests do not certify the general theorem; that rests on the supplied proof. Historical priority remains open to independent review.

## References

1. Y. Xu, Y. Han and W. Jiang, *Hochschild cohomology of truncated quiver algebras*, arXiv:math/0509202v1 (submitted 9 September 2005), https://arxiv.org/abs/math/0509202 .
2. S. Wolf, *The Hall algebra of a cyclic quiver at \(q=0\)*, arXiv:0709.4348v1 (submitted 27 September 2007), https://arxiv.org/abs/0709.4348 .
3. C. Cibils, *Rigidity of truncated quiver algebras*, Advances in Mathematics 79 (1990), 18–42; bibliographic identification via Reference [2] of Xu–Han–Jiang. The full text was not inspected for the present comparison.
