# A one-spike determinant law for prescribed diagonals over finite fields

## Finding

Fix a finite field \(\mathbb F_q\), where \(q\) is any prime power, and an integer \(n\ge1\). For a vector \(\mathbf x=(x_1,\ldots,x_n)\in\mathbb F_q^n\), write
\[
C_d(\mathbf x)=\#\{M\in\operatorname{GL}_n(\mathbb F_q):M_{ii}=x_i\ (1\le i\le n),\ \det M=d},\qquad d\in\mathbb F_q^\times.
\]
Let \(T(\mathbf x)=\sum_{d\ne0}C_d(\mathbf x)\). If at least one \(x_i=0\), then
\[
C_d(\mathbf x)=\frac{T(\mathbf x)}{q-1}\quad\text{for every }d\in\mathbb F_q^\times.
\]
If all \(x_i\ne0\), put \(P=\prod_i x_i\) and \(h=q^{\binom n2}\). Then **every determinant fiber** satisfies
\[
\boxed{C_d(\mathbf x)=\frac{T(\mathbf x)-h}{q-1}+h\,\mathbf1_{d=P}.}
\]
The difference between the fiber at the product of diagonal entries and every other nonzero fiber is therefore **exactly** \(q^{\binom n2}\), independent of the particular diagonal values.

The value \(T(\mathbf x)\) itself is explicit: let \(m\) be the number of zero coordinates of \(\mathbf x\). Gorodetsky's Theorem 1.4 gives
\[
T(\mathbf x)=q^{\binom n2-n}\sum_{r=0}^n\binom nr\prod_{i=1}^{n-r}(q^i-1)\sum_{j=0}^{\min(m,r)}(-q)^j\binom rj\frac{(m)_j}{(n)_j},
\]
where \((z)_j=z(z-1)\cdots(z-j+1)\), \((z)_0=1\), and an empty product is one. Substitution gives closed finite formulas for all \(C_d(\mathbf x)\).

## Assumptions and scope

The statements hold for every prime power \(q\), every \(n\ge1\), every diagonal vector, and every nonzero determinant. The case \(q=2\) is included, although there is only one nonzero determinant, so the single-spike distinction is vacuous. The count excludes singular matrices by definition. No asymptotic limit or restriction on characteristic is required.

## Proof

Fix a nontrivial additive character \(\psi\) of \(\mathbb F_q\). For a nontrivial multiplicative character \(\chi\colon\mathbb F_q^\times\to\mathbb C^\times\), let \(G(\chi)=\sum_{z\ne0}\chi(z)\psi(z)\). Define
\[
\mathcal G_\chi(A)=\sum_{M\in\operatorname{GL}_n(\mathbb F_q)}\chi(\det M)\psi(\operatorname{tr}(AM)).
\]
We first prove, without appealing to a nonstandard exponential-sum evaluation,
\[
\mathcal G_\chi(A)=\begin{cases}0,&\operatorname{rank}A<n,\\q^{\binom n2}G(\chi)^n\chi(\det A)^{-1},&A\in\operatorname{GL}_n(\mathbb F_q).\end{cases}
\tag{1}
\]
If \(A\) is singular, there exists for every \(c\in\mathbb F_q^\times\) an invertible \(V\) with \(AV=A\) and \(\det V=c\): choose a basis adapted to the nonzero kernel of \(A\) and scale one kernel direction. Replacing \(M\) by \(VM\) in the sum multiplies it by \(\chi(c)\); since \(\chi\) is nontrivial, the sum is zero.

If \(A\) is invertible, substituting \(B=AM\) reduces the sum to \(\chi(\det A)^{-1}\mathcal G_\chi(I_n)\). To evaluate \(\mathcal G_\chi(I_n)\), average the trace phase over the upper unitriangular group \(U\). Multiplication of \(B\) by each \(u\in U\) preserves determinant and permutes invertible matrices. Also
\[
\operatorname{tr}(uB)=\operatorname{tr}B+\sum_{i<j}u_{ij}B_{ji}.
\]
Additive orthogonality kills every matrix with a nonzero entry below the diagonal. Each remaining invertible upper-triangular matrix contributes a free choice of \(\binom n2\) off-diagonal entries, giving \(\mathcal G_\chi(I_n)=q^{\binom n2}G(\chi)^n\). This proves (1).

For a prescribed diagonal, put
\[
S_\chi(\mathbf x)=\sum_{M\in\operatorname{GL}_n(\mathbb F_q)\,:\,M_{ii}=x_i}\chi(\det M).
\]
Applying additive character orthogonality to the \(n\) diagonal equalities and then (1) with \(A=\operatorname{diag}(t_1,\ldots,t_n)\), all terms with some \(t_i=0\) vanish. Thus
\[
S_\chi(\mathbf x)=q^{\binom n2-n}G(\chi)^n\prod_{i=1}^n\sum_{t\ne0}\chi(t)^{-1}\psi(-tx_i).
\tag{2}
\]
If an \(x_i\) vanishes, its factor is \(\sum_{t\ne0}\chi(t)^{-1}=0\). If every \(x_i\ne0\), substitution \(z=-tx_i\) in each factor yields
\[
S_\chi(\mathbf x)=q^{\binom n2-n}\chi((-1)^nP)\bigl(G(\chi)G(\chi^{-1})\bigr)^n.
\]
The standard Gauss-product identity \(G(\chi)G(\chi^{-1})=q\chi(-1)\) follows by substituting \(a=tb\) in the product and using \(\sum_{b\ne0}\psi(cb)=q-1\) for \(c=0\) and \(-1\) otherwise. Hence
\[
S_\chi(\mathbf x)=q^{\binom n2}\chi(P)\qquad\text{if every }x_i\ne0.
\tag{3}
\]
Finally, multiplicative-character orthogonality on \(\mathbb F_q^\times\) recovers the determinant fibers from the trivial-character moment \(T(\mathbf x)\) and the nontrivial moments (2)–(3):
\[
C_d(\mathbf x)=\frac1{q-1}\sum_\chi\chi(d)^{-1}S_\chi(\mathbf x).
\]
For \(P\ne0\), \(\sum_{\chi\ne1}\chi(Pd^{-1})=(q-1)\mathbf1_{d=P}-1\). The announced formulas follow. When \(q=2\) there are no nontrivial multiplicative characters; the result follows directly from the only determinant being one.

## Verification

A standalone exact enumerator, `verify_counts.py`, exhaustively enumerates off-diagonal entries in nine finite prime-field examples, computes each determinant by modular Gaussian elimination, and compares every nonzero determinant count against the closed formula. It includes both all-nonzero and zero-containing prescribed diagonals, dimensions one through four as applicable, and prime fields of orders two, three and five. Running `python verify_counts.py` reports `VERIFY_OK 9 exhaustive configurations`. These checks validate finite examples, not the universal theorem; the proof above supplies the universal quantifiers and all finite field extensions.

For example, at \(n=3,q=3,\mathbf x=(1,1,1)\), the exact counts at determinants one and two are respectively \(249\) and \(222\); their difference is \(27=3^3\). For \(\mathbf x=(0,1,2)\), both counts equal \(204\).

## Relationship to prior work

Gorodetsky (2026), Theorem 1.4 and its proof in Section 3.4, explicitly count invertible matrices with a prescribed full diagonal but do **not** refine those totals by individual nonzero determinants. The theorem here supplies that determinant refinement with a rank-sensitive multiplicative-character argument and yields an exceptionally simple one-spike formula. Historical matrix Gauss-sum research by Kim (1997) and Li–Hu (2012) treats general and special linear groups with trace-exponential weights, providing related Fourier machinery. These general evaluations may offer another route to the present conclusion; priority claims should be interpreted with that possibility in mind. The present proof is self-contained once classical additive and multiplicative character orthogonality is granted.

## Limitations

This result does not count singular matrices by their determinant zero; it refines the invertible-matrix count only. It does not establish independence between the determinant and any arbitrary prescribed off-diagonal pattern. Related older Fourier identities for special linear groups may imply the conclusion after additional inversion, so independent novelty assessment is warranted. The supplied finite checker tests only prime fields and small dimensions; the algebraic argument proves the general prime-power case.

## References

1. O. Gorodetsky, *Statistics of entries of matrices from the general linear group over a finite field*, arXiv:2610.29305v1 (first public 21 October 2026), Theorem 1.4, Sections 1.2, 3.4, https://arxiv.org/html/2610.29305v1.
2. D. S. Kim, *Gauss sums for general and special linear groups over a finite field*, Archiv der Mathematik **69** (1997), 297–304, https://doi.org/10.1007/s000130050124.
3. Y. Li and S. Hu, *Gauss sums over some matrix groups*, Journal of Number Theory **132** (2012), 2967–2976, cited as reference [40] of the first source.
