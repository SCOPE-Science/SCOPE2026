# Deterministic character-sum pruning for no-hint elliptic-code key recovery

## Statement

Consider the no-hint structural attack of Kuninets, Malygina and Melnichuk on an elliptic AG code over a finite field \(\mathbb F_q\) of characteristic greater than \(3\). Their normalization step fixes a rational point \(R_0\), obtains a nonconstant vector
\[
g=(g_2,\ldots,g_n)
\]
from the two-dimensional code corresponding to \(L(2R_0)\), and enumerates affine pairs
\[
(a,b)\in\mathbb F_q^*\times\mathbb F_q
\]
until
\[
ag_i+b\in V\qquad(i=2,\ldots,n),
\]
where \(V=f_2^{(R_0)}(E(\mathbb F_q)\setminus\{R_0\})\) is the finite value set of the degree-two map \(f_2^{(R_0)}\). The source gives a rigorous \(O(nq^2)\) bound for this affine-pair search and an \(O(q^2)\) average estimate under an explicit heuristic independence assumption.

For \(q\ge 11\), the attacker may choose \(R_0=(\alpha,\beta)\) with \(\beta\ne0\). Put \(\beta'=-\beta\) and
\[
\gamma=\frac{3\alpha^2+A}{2\beta'}
\]
for the short Weierstrass model
\[
E:y^2=x^3+Ax+B.
\]
Define
\[
H(z)=1-4\gamma z+12\alpha z^2-8\beta' z^3.
\]
Then \(H\) is squarefree and, with \(\chi\) the quadratic character of \(\mathbb F_q\),
\[
\boxed{V=\{z\in\mathbb F_q:\chi(H(z))\in\{0,1\}\}.}
\]

Let \(h_1,\ldots,h_m\) be distinct coordinates among the \(g_i\), and let \(M_m\) denote the number of affine pairs \((a,b)\in\mathbb F_q^*\times\mathbb F_q\) satisfying
\[
ah_j+b\in V\qquad(j=1,\ldots,m).
\]
Then
\[
\boxed{
M_m\le \frac{q^2}{2^m}+\frac32 m q^{3/2}+3m^2q.
}
\]
Since a nonconstant element of \(L(2R_0)\) has fibres of size at most two, the vector \(g\) contains at least \(\lceil(n-1)/2\rceil\) distinct values. Hence, if
\[
L=\left\lceil\frac12\log_2q\right\rceil,
\qquad n\ge2L,
\]
the affine-pair stage can be implemented deterministically in
\[
\boxed{O\!\left(q^2+nq^{3/2}\log q\right)}
\]
field/dictionary operations, replacing the source's rigorous \(O(nq^2)\) bound for that stage. No independence hypothesis is used.

This does not replace the source's heuristic \(O(q^2)\) average estimate; rather, it supplies a strictly stronger worst-case guarantee than the previously proved \(O(nq^2)\) bound. Other stages of the complete key-recovery attack may dominate the total running time for some parameter regimes.

## Value-set character description

For \(R_0=(\alpha,\beta)\) with \(\beta\ne0\), the source writes
\[
f_2^{(R_0)}(x,y)=
\frac{y-\beta'-\gamma(x-\alpha)}{(x-\alpha)^2}.
\]
For a prescribed finite value \(z\), writing \(d=x-\alpha\) and eliminating \(y\) gives the quadratic equation
\[
z^2d^2+(2z\gamma-1)d+(2z\beta'+\gamma^2-3\alpha)=0.
\]
Its discriminant is exactly
\[
H(z)=1-4\gamma z+12\alpha z^2-8\beta' z^3.
\]
Thus a finite fibre contains an \(\mathbb F_q\)-point exactly when \(H(z)\) is a square or zero. The degenerate value \(z=0\) is included as well, since \(H(0)=1\).

The cubic is squarefree. A direct discriminant computation gives
\[
\operatorname{disc}(H)
=-\frac{64(4A^3+27B^2)}{\beta^2},
\]
which is nonzero because the elliptic curve is nonsingular and \(\beta\ne0\).

## Character-sum bound for affine candidates

Fix distinct \(h_1,\ldots,h_m\). For \(a\ne0\), the roots in the variable \(b\) of
\[
H(ah_i+b)
\]
are \(r-ah_i\), where \(r\) runs through the three roots of \(H\) in an algebraic closure. Two factors corresponding to \(i\ne j\) can share a root only if
\[
a=\frac{r-s}{h_i-h_j}
\]
for two distinct roots \(r,s\) of \(H\). Therefore at most
\[
6\binom m2=3m(m-1)
\]
nonzero values of \(a\) are exceptional. For every other \(a\), every product
\[
\prod_{i\in S}H(ah_i+b),\qquad \varnothing\ne S\subseteq[m],
\]
is squarefree of degree \(3|S|\), and the standard Weil bound gives
\[
\left|\sum_{b\in\mathbb F_q}
\chi\!\left(\prod_{i\in S}H(ah_i+b)\right)\right|
\le (3|S|-1)\sqrt q.
\]

Away from the roots of \(H\), membership in \(V\) is
\[
1_V(z)=\frac{1+\chi(H(z))}{2}.
\]
Tuples for which one of the \(m\) arguments hits a root contribute at most \(3m(q-1)\) in total. Expanding the product of the remaining indicators over subsets \(S\subseteq[m]\), using
\[
\sum_{S\subseteq[m]}|S|=m2^{m-1},
\]
and bounding the exceptional scalings trivially yields
\[
M_m
\le
\frac{q(q-1)}{2^m}
+\frac32m q^{3/2}
+3m(m-1)q+3mq,
\]
which implies the stated bound.

## Deterministic running-time consequence

Order the membership tests so that the first \(L\) tested coordinates have pairwise distinct \(g_i\)-values. Such a choice is possible when \(n\ge2L\), because a degree-two map has fibres of size at most two, and an affine change of its values preserves fibre sizes.

Let \(M_j\) be the number of candidates remaining after the first \(j\) distinct-value tests. The work spent on the first \(L\) tests is proportional to
\[
\sum_{j=0}^{L-1}M_j.
\]
The preceding bound gives
\[
\sum_{j=0}^{L-1}M_j
=O\!\left(q^2+q^{3/2}L^2+qL^3\right)=O(q^2)
\]
for \(L=\lceil\tfrac12\log_2q\rceil\). After these tests,
\[
M_L=O(q^{3/2}\log q).
\]
All remaining membership checks and the source's per-survivor reconstruction can therefore be bounded by
\[
O(nM_L)=O(nq^{3/2}\log q).
\]
Together this proves the deterministic
\[
O(q^2+nq^{3/2}\log q)
\]
bound for the affine normalization stage.

For example, when \(n=\Theta(q)\), this stage improves from the proved \(O(q^3)\) worst-case bound to \(O(q^{5/2}\log q)\). The source's separate code-filtration and recovery of the second divisor are unchanged here.

## Reproducibility

`artifacts/verify_affine_value_filter.py` uses prime fields as finite sanity checks. For three nonsingular curves it verifies directly that the values of the degree-two function agree with the cubic-character description, enumerates all affine pairs for several distinct test values, and confirms the explicit upper bound for every tested prefix. `artifacts/verification_output.txt` records the output. These computations support the formulas but do not replace the general proof.

## Originality boundary

The elliptic-code attack, its degree-two map, the affine normalization search, and the source's heuristic average-case analysis are due to Kuninets, Malygina and Melnichuk. Weil bounds for multiplicative character sums and related pseudorandomness consequences for quadratic residues are classical; no originality is claimed for that technique itself.

The contribution here is the cubic-character representation of the exact value set in the form needed by the no-hint search, the uniform bound on surviving affine pairs, and the resulting deterministic worst-case complexity improvement for that stage. Searches by the source title and identifier, by elliptic-code/McEliece affine normalization terminology, and by equivalent value-set/character-sum formulations found no inspected prior application yielding this bound. Originality is claimed only to the best of our knowledge. Because the motivating preprint is very recent, a contemporaneous observation or later revision remains a material residual risk.

## Limitations

The theorem concerns the affine-pair normalization stage, not every cost in the full structural attack. In parameter regimes where filtration, Schur-product linear algebra, or recovery of the second divisor dominates, the displayed improvement need not change the leading total complexity. The clean cubic description is stated for characteristic greater than \(3\) and a chosen non-2-torsion point; for \(q\ge11\) such a rational point always exists because \(|E(\mathbb F_q)|>4\) by Hasse's bound, while the finitely many smaller cases can be handled directly. No claim is made that the \(q^{3/2}\log q\) survivor term is optimal.

## References

1. A. Kuninets, E. Malygina, E. Melnichuk, *A Polynomial-Time Attack on the McEliece Cryptosystem on Elliptic Codes with Arbitrary Divisors*, arXiv:2609.17732 (2026). https://arxiv.org/abs/2609.17732
2. B. McDonald, A. Sahay, E. L. Wyman, *The VC-dimension of quadratic residues in finite fields*, arXiv:2210.03789 (2022). https://arxiv.org/abs/2210.03789
3. D. Wan, Q. Wang, *Index bounds for character sums with polynomials over finite fields*, arXiv:1507.00988 (2015). https://arxiv.org/abs/1507.00988
