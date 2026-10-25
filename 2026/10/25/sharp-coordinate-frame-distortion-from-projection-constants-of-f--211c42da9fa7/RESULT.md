# Sharp coordinate-frame distortion from projection constants of finite-dimensional hyperplanes

## Finding
Let \(\mathbb K\in\{\mathbb R,\mathbb C\}\), let \(N\ge2\), and let \(V=\ker f\subset\ell_\infty^N(\mathbb K)\), where the nonzero linear functional \(f\) has coordinates \(f_1,\ldots,f_N\) normalized by \(\sum_{j=1}^N|f_j|=1\). Define \(a_j=|f_j|\) and \(a=\max_j a_j\). Denote the absolute projection constant of \(V\) by \(\lambda(V)\).

For each \(j\) with \(f_j\ne0\), coordinate deletion gives a linear isomorphism \(D_j:V\to\ell_\infty^{N-1}(\mathbb K)\). Its optimal coordinate-frame distortion is
\[
\Delta(V):=\min_{j:f_j\ne0}\|D_j\|\,\|D_j^{-1}\|=\max\left\{1,\frac{1-a}{a}\right\}.
\]
The projection constant is exactly
\[
\lambda(V)=\begin{cases}
1,&a\ge\tfrac12,\\
1+\left(\displaystyle\sum_{j:a_j>0}\frac{a_j}{1-2a_j}\right)^{-1},&a<\tfrac12.
\end{cases}
\]
Consequently, for every such real or complex hyperplane, \(1\le\lambda(V)<2\) and
\[
\boxed{\quad d\bigl(V,\ell_\infty^{N-1}(\mathbb K)\bigr)\le\Delta(V)\le\frac{\lambda(V)}{2-\lambda(V)}.\quad}
\]
Equality in the second inequality occurs precisely when either \(a\ge\tfrac12\) (and both quantities are \(1\)), or all nonzero coefficient moduli \(a_j\) coincide. In the latter case, the support has cardinality \(k\ge3\), \(\lambda(V)=2-2/k\), and \(\Delta(V)=k-1\). Sharpness asserted here concerns \(\Delta(V)\), **not** the unrestricted Banach--Mazur distance.

## Assumptions and scope
The field is real or complex, \(N\) is any integer at least \(2\), and zero coefficients of \(f\) are allowed. The Banach--Mazur distance is the infimum of \(\|T\|\|T^{-1}\|\) over all linear isomorphisms \(T\) between spaces of equal dimension, over the indicated field. The *absolute* projection constant is the supremum, over all isometric embeddings into Banach spaces, of the least norm of a projection onto the embedded copy. No assumption of norm attainment outside finite dimension is used. The coordinate-frame invariant \(\Delta(V)\) minimizes only among the \(N\) coordinate-deletion maps, not among arbitrary isomorphisms.

## Proof
**Step 1: coordinate frames.** If \(f_j\ne0\), any \(y\in\ell_\infty^{N-1}\) has a unique preimage \(x\in V\) whose coordinates away from \(j\) equal those of \(y\), and whose missing coordinate equals \(x_j=-\sum_{i\ne j}f_i y_i/f_j\). Therefore
\[
\|D_j^{-1}\|=\max\left\{1,\frac{1-a_j}{a_j}\right\}.
\]
The displayed maximum is achieved by choosing the phases of the surviving \(y_i\) to align the terms \(f_i y_i\), unless its first entry is larger, in which case a unit surviving coordinate suffices. The norm of deletion is at most \(1\). If \(a<1/2\), the support of \(f\) has at least three elements, and for every admissible \(j\) there is a nonzero element of \(V\) with \(j\)-th coordinate zero; hence \(\|D_j\|=1\). As the displayed inverse bound decreases with \(a_j\), the least product occurs at a maximal coefficient and equals \((1-a)/a\). If \(a\ge1/2\), deleting an index of maximal modulus preserves the supremum norm on \(V\), because \(|x_j|\le(1-a)\max_{i\ne j}|x_i|/a\le\max_{i\ne j}|x_i|\). Thus deletion is an isometry, and \(\Delta(V)=1\). The two claims combine into the formula for \(\Delta(V)\).

**Step 2: absolute equals relative projection constant.** Since \(\ell_\infty^N(\mathbb K)\) is \(1\)-injective, for any isometric copy of \(V\) in a larger Banach space, the coordinate functionals of its original embedding into \(\ell_\infty^N\) extend by Hahn--Banach without norm increase. Composing these extensions with a projection \(\ell_\infty^N\to V\) transfers that projection to the larger space without increasing its norm. The reverse inequality follows by taking the original ambient space itself. Hence the absolute constant equals the least norm of a projection \(\ell_\infty^N\to V\).

**Step 3: minimal projections.** Every such projection has the form \(P=I-u\otimes f\), where \(f(u)=1\). For \(a_j>0\), write \(t_j=f_ju_j\); then \(\sum_{j:a_j>0}t_j=1\). The \(j\)-th absolute row sum is
\[
R_j=|1-t_j|+\frac{1-a_j}{a_j}|t_j|.
\]
At any zero coefficient we may set \(u_j=0\), giving row sum \(1\). If \(a\ge1/2\), the coordinate-elimination projection associated with an index of maximal modulus has norm \(1\), so \(\lambda(V)=1\).

Suppose now \(a<1/2\) and define positive \(c_j=(1-2a_j)/a_j\) for all \(a_j>0\). By the triangle inequality,
\[
R_j\ge1+c_j|t_j|.
\]
If every row sum is at most \(L\), then \(|t_j|\le(L-1)/c_j\). Since \(1=|\sum_jt_j|\le\sum_j|t_j|\), it follows that \(L\ge1+(\sum_jc_j^{-1})^{-1}\). Equality is attained by taking every \(t_j\) to be the nonnegative number \(c_j^{-1}/\sum_i c_i^{-1}\), so that \(\sum_jt_j=1\) and \(R_j=1+c_jt_j\) for all nonzero coefficients; set \(u_j=t_j/f_j\) and zero otherwise. This proves the exact projection-constant formula in either field.

**Step 4: sharp comparison and equality.** For \(a<1/2\), every positive \(a_j\le a\) satisfies
\[
\frac{a_j}{1-2a_j}\le\frac{a_j}{1-2a}.
\]
Summing and using \(\sum_j a_j=1\) gives \(\lambda(V)-1\ge1-2a\), that is, \(\lambda(V)\ge2-2a\). The function \(t\mapsto t/(2-t)\) is strictly increasing for \(1\le t<2\); therefore
\[
\frac{\lambda(V)}{2-\lambda(V)}\ge\frac{2-2a}{2a}=\frac{1-a}{a}=\Delta(V).
\]
Equality in the summed inequality holds exactly when each positive \(a_j=a\). The case \(a\ge1/2\) was resolved in Steps 1 and 3. Since every finite coefficient list produces \(\lambda(V)<2\), the comparison is defined on the full stated domain. The lower displayed inequality in the theorem follows because a coordinate-deletion map is an admissible Banach--Mazur isomorphism.

## Verification
The standalone checker `checker.py` uses exact rational arithmetic to test the comparison and equality criterion, and a separate linear program to minimize all real projection row norms directly. A run with Python 3 and SciPy completed 1,001 distinct configurations, including equal-weight support families, uneven weights, and zero coefficients. The code tests necessary finite instances only; Steps 1--4 supply the proof over both scalar fields and all finite dimensions.

## Relationship to prior work
Deregowska and Lewandowska [1], Theorem 2.4 and Proposition 3.1, prove for **real** hyperplanes, subject to \(\lambda(V)<4/3\), the dimension-independent estimate \(d\le\lambda/(4-3\lambda)\). Their paper does not derive the coordinate-frame invariant, its sharp equality classification, or the stronger bound \(d\le\lambda/(2-\lambda)\) on the full hyperplane interval \(1\le\lambda<2\). Near \(\lambda=1\), the new bound has linear coefficient \(2\) rather than \(4\) in the displacement from \(1\). The proof here also applies over complex scalars. Classical minimal-projection literature includes Blatter and Cheney [2], so the isolated exact formula for the minimal projection norm is not asserted to be historically new; the new claim is the quantitative comparison with coordinate-frame distortion and its complete equality statement. The inaccessible historical source [2] leaves a priority risk for equivalent reformulations.

## Limitations
The sharp constant is sharp for the best **coordinate-deletion** isomorphism, and not claimed sharp for the unrestricted Banach--Mazur distance. The proof does not settle the codimension-two or arbitrary-codimension conjecture of [1]. It says nothing about infinite-dimensional subspaces. Historical priority cannot be certified by a finite literature search, particularly because [2] was not readable in full.

## References
[1] B. Deregowska and B. Lewandowska, *Projection Constants and Banach-Mazur Distance in Codimension Two*, arXiv:2610.06141v1, 5 October 2026; especially Theorem 2.4, Proposition 3.1, and Section 3. https://arxiv.org/html/2610.06141v1.

[2] J. Blatter and E. W. Cheney, *Minimal projections on hyperplanes in sequence spaces*, Annali di Matematica Pura ed Applicata 101 (1974), 215–227. DOI 10.1007/BF02417105. The full text was not accessible for the comparison.
