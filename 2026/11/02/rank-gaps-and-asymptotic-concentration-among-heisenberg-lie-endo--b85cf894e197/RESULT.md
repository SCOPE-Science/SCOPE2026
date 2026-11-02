# Rank gaps and asymptotic concentration among Heisenberg Lie endomorphisms over finite fields

## Finding
Fix a prime power \(q\) and an integer \(m\ge1\). Write \(H_m=V\oplus \mathbb F_q z\), where \(V\) has dimension \(2m\), \(\omega\) is a nondegenerate alternating form on \(V\), and \([u+az,v+bz]=\omega(u,v)z\). Every endomorphism mentioned below is \(\mathbb F_q\)-linear and preserves this Lie bracket.

Put
\[
I_{m,r}(q)={m\brack r}_q\prod_{j=m-r+1}^{m}(q^j+1),\qquad
B_{m,r}(q)=I_{m,r}(q)\prod_{i=0}^{r-1}(q^{2m}-q^i)
\]
for integers \(0\le r\le m\), where \({m\brack r}_q\) is the Gaussian binomial coefficient; empty products equal one. Let \(N_{m,k}(q)\) be the number of Lie endomorphisms of \(H_m\) whose image has dimension \(k\). The **complete rank spectrum** is
\[
N_{m,k}(q)=\sum_{r=0}^{m}B_{m,r}(q)\left(q^r\mathbf1_{k=r}+(q^{2m}-q^r)\mathbf1_{k=r+1}\right)
+q^{2m}(q-1)q^{m^2}\prod_{i=1}^{m}(q^{2i}-1)\,\mathbf1_{k=2m+1}.
\]
Every rank \(0,1,\ldots,m+1\) and rank \(2m+1\) occurs; ranks \(m+2,\ldots,2m\) do not occur. (For \(m=1\), the missing interval is empty.) If \(f\) is uniform among the endomorphisms, then for every fixed prime power \(q\),
\[
\Pr(\operatorname{rank}f=m+1)=1-\frac{q^2}{q^2-1}q^{-m}+o(q^{-m})
\quad(m\to\infty).
\]
The probability statement uses the dimension limit at fixed field size, not a large-field limit at fixed dimension.

## Assumptions and scope
All fields are finite of size \(q\), in arbitrary characteristic, including characteristic two. The algebra is the standard \((2m+1)\)-dimensional two-step Heisenberg Lie algebra, with nondegenerate alternating quotient form. A Lie endomorphism is a linear map satisfying \(f([a,b])=[f(a),f(b)]\); maps that only preserve the associative matrix product or the underlying additive group are not counted. Image rank is vector-space dimension. The central vector \(z\) is fixed in the chosen presentation, and is not required to be fixed by an endomorphism.

## Proof
**1. Exact normal form.** Since the derived algebra is \(\mathbb F_q z\), every Lie endomorphism is necessarily of the form
\[
f(v+tz)=Av+(\ell(v)+ct)z,
\qquad A\in\operatorname{End}_{\mathbb F_q}(V),\ \ell\in V^*,\ c\in\mathbb F_q.
\]
Preservation of all brackets is equivalent to \(\omega(Au,Av)=c\omega(u,v)\) for all \(u,v\in V\). The scalar \(c\) is uniquely determined by \(A\), since \(\omega\) is nonzero. Conversely the displayed identity suffices for a Lie endomorphism. If \(c\ne0\), \(A\) is a nondegenerate symplectic similitude and thus invertible. The number of such pairs \((A,c)\) is \((q-1)|\operatorname{Sp}_{2m}(q)|\), because the similitude multiplier map is onto \(\mathbb F_q^\times\). There are \(q^{2m}\) free choices of \(\ell\), and every resulting endomorphism has rank \(2m+1\).

**2. Singular case and isotropic images.** If \(c=0\), the image \(W=A(V)\) is totally isotropic. Hence \(r=\dim W\) lies between zero and \(m\). The number of totally isotropic \(r\)-subspaces is
\[
I_{m,r}(q)={m\brack r}_q\prod_{j=m-r+1}^{m}(q^j+1).
\]
For a direct proof, construct an ordered isotropic basis successively: after \(i\) vectors, the perpendicular space has \(q^{2m-i}\) vectors, and the previously chosen span excludes \(q^i\) of them. Dividing \(\prod_{i=0}^{r-1}(q^{2m-i}-q^i)\) by the number \(\prod_{i=0}^{r-1}(q^r-q^i)\) of ordered bases of an \(r\)-space yields the stated expression (equivalently, its Gaussian-product form). For each \(W\), the number of surjections \(V\twoheadrightarrow W\) is \(\prod_{i=0}^{r-1}(q^{2m}-q^i)\), so the number of admissible \(A\) with rank \(r\) is \(B_{m,r}(q)\).

**3. Central functional and ranks.** The graph map \(v\mapsto Av+\ell(v)z\) has rank \(r\) exactly when \(\ell\) vanishes on \(\ker A\), i.e. when \(\ell\) lies in the \(r\)-dimensional row space of \(A\). There are precisely \(q^r\) such functionals. Each of the other \(q^{2m}-q^r\) functionals produces rank \(r+1\). As \(f(z)=0\) in this case, these are exactly the ranks of \(f\). Summing over \(r\), then adding the invertible-similitude case, proves the formula and the forbidden rank gap. Positivity for every permitted rank follows from the factors above.

**4. Dimension asymptotics.** Write \(B_r=B_{m,r}(q)\). For \(1\le r\le m\), direct cancellation gives
\[
\frac{B_r}{B_{r-1}}=\frac{q^{2(m-r+1)}-1}{q^r-1}\left(q^{2m}-q^{r-1}\right).
\]
These ratios decrease in \(r\); their minimum, at \(r=m\), has order \(q^m\). Consequently
\[
\sum_{r=0}^{m-1}\frac{B_r}{B_m}=\frac{B_{m-1}}{B_m}+O(q^{-2m})
=\frac{q^{-m}}{q^2-1}+o(q^{-m}).
\]
Using \(|\operatorname{Sp}_{2m}(q)|=q^{m^2}\prod_{i=1}^{m}(q^{2i}-1)\) and the product for \(B_m\), one obtains
\[
\frac{(q-1)|\operatorname{Sp}_{2m}(q)|}{B_m}
=O_q\left(q^{-m(m-1)/2}\right)=o(q^{-m}).
\]
(The displayed little-oh follows in particular as \(m\to\infty\).) The total number of endomorphisms is \(q^{2m}(\sum_{r=0}^{m}B_r+(q-1)|\operatorname{Sp}_{2m}(q)|)\), while exactly \((q^{2m}-q^m)B_m\) have rank \(m+1\). Dividing and expanding the denominator gives the probability asymptotic.

## Verification
A standalone standard-library Python program, `verify.py`, generates all allowed block matrices directly in dimensions \(3\) and \(5\) over prime fields, determines ranks by modular elimination, and compares the observed rank counts to the closed formula. Exhaustive instances \((m,q)=(1,2),(1,3),(2,2)\) give respectively \((1,21,18,24)\), \((1,104,192,432)\), and \((1,465,15750,37800,0,11520)\). The program also checks the forbidden gap and dimension-asymptotic trend for several larger dimensions using independent integer formulas. Run with `python verify.py`. The exhaustive checks apply only to the named finite instances; the unlimited assertions follow from the proof.

## Relationship to prior work
Ben Jmaa, Makhlouf, and Saadaoui (2022), Example 3, explicitly describe the Heisenberg Lie-endomorphism block matrix and the symplectic-similitude condition; that normal form is **prior work**, not a new claim here. Saadaoui (2017/2018) is cited there as an earlier source for the Hom-Lie setting. The present quantitative assertion instead enumerates **every linear endomorphism by its image dimension over each finite field**, detects the intermediate rank gap, and determines the fixed-field dimension-asymptotic coefficient. Kaygorodov and Khudoyberdiyev (2023) treat transposed Poisson structures on related complex solvable Lie algebras and do not enumerate these finite-field maps. Rossmann (2021) counts conjugacy classes of graphical groups over finite fields, a different object and statistic.

## Limitations
No publication-priority guarantee is asserted: older finite-field or Hom-Lie enumeration literature could contain an equivalent rank-refined formula under different language, and the complete Saadaoui precursor was not inspected. The result is exclusively for \(\mathbb F_q\)-linear Lie endomorphisms of the standard nondegenerate Heisenberg algebra; it does not cover arbitrary two-step nilpotent Lie algebras, semilinear maps, or all fields. Independent audit has not been performed. The finite verifier does not prove the dimension asymptotic.

## References
- T. Ben Jmaa, A. Makhlouf, and N. Saadaoui, *Current Hom-Lie algebras*, Acta Comment. Univ. Tartu. Math. 26(1) (2022), 103–127, DOI: 10.12697/ACUTM.2022.26.08, especially Example 3, p. 105. First publicly dated May 30, 2022.
- N. Saadaoui, *Cohomology of Heisenberg Hom-Lie algebras* (2017), arXiv:1701.07090; the earlier block-form source referenced in the 2022 paper. Full precursor not inspected.
- I. Kaygorodov and A. Khudoyberdiyev, *Transposed Poisson structures on solvable and perfect Lie algebras* (2023), arXiv:2310.00624v1.
- T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields* (2021), arXiv:2107.05564v3.
