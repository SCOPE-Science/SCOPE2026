# Three sharp budget regimes in clique–star multiplex coupling

## Finding

Let \(n\ge3\). Join the vertices of a unit-edge clique \(K_n\) to the corresponding vertices of a unit-edge star \(K_{1,n-1}\) by a perfect matching. The star center is paired with a distinguished clique vertex. The matching conductances are arbitrary nonnegative real numbers with sum \(B>0\); the intralayer edge conductances remain one. Let \(F_n(B)\) be the maximum possible second-smallest eigenvalue of the resulting \(2n\)-vertex weighted Laplacian. Put
\[
B_1=\frac{n^2}{n+1},\qquad
B_2=\begin{cases}\infty,&n=3,\\ \dfrac{(n-1)(n-2)}{n-3},&n\ge4.\end{cases}
\]
Then the optimal value, and an optimal allocation with center-to-center matching conductance \(x\) and each of the other \(n-1\) conductances equal to \(y\), are as follows.

* **Uniform regime, \(0<B\le B_1\):** \(x=y=B/n\) and \(F_n(B)=2B/n\). This allocation is the only global optimizer.
* **Balanced regime, \(B_1<B<B_2\):** \(x\) and \(y\) are uniquely specified **among center/leaf-symmetric allocations** by \(x+(n-1)y=B\), \(B/n<y<B/(n-1)\), and
\[
\frac{n+2x+2y-\sqrt{(n-2+2x-2y)^2+4(n-1)}}{2}
=
\frac{n+1+2y-\sqrt{(n-1)^2+4y^2}}{2}.
\]
Their common value is \(F_n(B)\). Equivalently, with \(t=F_n(B)\),
\[
x=\frac{(n-t)(2-t)}{2(t-1)},\qquad
y=\frac{(t-1)(n-t)}{n+1-2t},
\]
where \(2n/(n+1)<t<2\) is determined uniquely by \(B=x+(n-1)y\).
* **Hub-link extinction, \(n\ge4\) and \(B\ge B_2\):** every global optimizer has \(x=0\) and all leaf matching conductances equal to \(y=B/(n-1)\). Thus the global optimizer is unique, and
\[
F_n(B)=\frac{n+1+2B/(n-1)-\sqrt{(n-1)^2+4B^2/(n-1)^2}}{2}.
\]

For \(n=3\), the balanced regime persists at every finite budget above \(B_1\), with a positive center matching conductance tending to zero as \(B\to\infty\). For every \(n\ge3\), the optimal value tends to \((n+1)/2\) as \(B\to\infty\).

## Assumptions and scope

All graphs are undirected, simple within each layer, and use the unnormalized combinatorial weighted Laplacian \(L\), with \(L_{ii}=\sum_j w_{ij}\) and \(L_{ij}=-w_{ij}\) for \(i\ne j\). Only the \(n\) matching conductances may vary, subject to nonnegativity and the exact total budget. The index of the star center and its paired clique vertex is zero; each leaf pair has an index from \(1\) to \(n-1\). A zero matching weight removes that interlayer edge. The spectral gap is \(\lambda_2(L)\), counted with multiplicity, and is zero at \(B=0\). No uniqueness claim about nonsymmetric optimizers is made in the balanced regime.

## Proof

**1. Exact symmetry reduction.** The map from matching weights to \(\lambda_2(L)\) is concave: it is the infimum, over unit vectors orthogonal to the all-ones vector, of affine Rayleigh quotients. Simultaneously permuting the \(n-1\) leaf pairs leaves the objective invariant. Averaging an arbitrary feasible allocation over these permutations therefore cannot decrease the objective. Consequently an optimum exists with center matching weight \(x\) and a common leaf matching weight \(y\), where \(x+(n-1)y=B\).

Set \(m=n-1\). On the two-dimensional antisymmetric-between-layers sector of the four-dimensional center/constant-leaf subspace, the symmetric Laplacian has the matrix
\[
A(x,y)=\begin{pmatrix}m+2x&-\sqrt m\\-\sqrt m&1+2y\end{pmatrix}.
\]
The symmetric-between-layers sector contributes eigenvalues \(0,n\). On each of the \(m-1\) mutually orthogonal leaf-contrast directions, the two-layer block is
\[
C(y)=\begin{pmatrix}n+y&-y\\-y&1+y\end{pmatrix}.
\]
The smaller eigenvalues of these two blocks are respectively
\[
\mu(x,y)=\frac{n+2x+2y-\sqrt{(n-2+2x-2y)^2+4m}}2,
\qquad
\nu(y)=\frac{n+1+2y-\sqrt{m^2+4y^2}}2.
\]
Since \(\nu(y)\le1+y\) and \(\nu(y)<(n+1)/2<n\), the algebraic connectivity is exactly \(\min\{\mu(x,y),\nu(y)\}\). The expression for \(\nu\) is valid because \(m-1=n-2\ge1\).

**2. Monotone competition.** Fix \(B\) and substitute \(x=B-my\), so \(0\le y\le B/m\). The function \(\mu(B-my,y)\) is strictly concave in \(y\). Indeed, with \(\delta=n-2+2B-2ny\), its second derivative is
\[
-\frac{8n^2m}{(\delta^2+4m)^{3/2}}<0.
\]
At \(y=B/n\) its derivative vanishes, and \(\mu(B/n,B/n)=2B/n\). Meanwhile \(\nu'(y)=1-2y/\sqrt{m^2+4y^2}>0\). Thus no \(y<B/n\) improves the objective, whereas above \(B/n\) the \(\mu\)-branch strictly decreases and the \(\nu\)-branch strictly increases. At the uniform allocation,
\[
\nu(B/n)\ge2B/n\quad\Longleftrightarrow\quad B\le B_1.
\]
This proves the uniform regime. Its optimizer is globally unique: equality in the universal Rayleigh bound \(\lambda_2(L)\le2B/n\), obtained from a vector constant with opposite signs on the layers, forces that vector to be a Laplacian eigenvector and hence forces every matching weight to equal \(B/n\).

**3. The second sharp threshold.** Let \(t=\nu(y)\). The characteristic polynomial of \(C(y)\) gives
\[
y=\frac{(t-1)(n-t)}{n+1-2t},
\qquad 1\le t<\frac{n+1}{2}.
\]
When \(x=0\), evaluate the characteristic polynomial of \(A(0,y)\) at \(t\):
\[
\det(A(0,y)-tI)=\frac{(n-1)(n-t)(t-2)}{n+1-2t}.
\]
The larger eigenvalue of \(A(0,y)\) is greater than \(t\), so \(\mu(0,y)\ge\nu(y)\) if and only if \(t\ge2\). The increasing function \(\nu(y)\) reaches two precisely when \(n\ge4\) and \(y=(n-2)/(n-3)\); it never reaches two for finite \(y\) when \(n=3\). Because \(\mu\) strictly decreases and \(\nu\) strictly increases to the right of uniformity, the maximizing allocation follows their unique crossing until that crossing reaches \(x=0\), exactly at \(B=B_2\). At larger budgets, the unique symmetric optimum lies at \(x=0\). Solving \(\det(C(y)-tI)=0\) and \(\det(A(x,y)-tI)=0\) for the interior crossing gives the displayed rational expressions for \(x\) and \(y\), and therefore an exact implicit algebraic formula for \(t\).

**4. Extinction and uniqueness among all allocations.** Write the possibly unequal leaf weights as \(y_1,\ldots,y_m\), set \(\bar y=\sum_i y_i/m=(B-x)/m\), and let \((a,b)\) be a unit lowest-eigenvalue eigenvector of \(C(\bar y)\). For any leaf vector \(\theta\) with \(\sum_i\theta_i=0\) and \(\|\theta\|=1\), form a test vector with zero center coordinates, clique leaves \(a\theta_i\), and star leaves \(b\theta_i\). It is orthogonal to the global all-ones vector. Averaging its Rayleigh quotient over an orthonormal basis of the leaf zero-sum space gives exactly \(\nu(\bar y)\), because the average of the squared basis coordinates at each leaf is \(1/m\). Hence for **every**, not necessarily symmetric, feasible allocation,
\[
\lambda_2(L)\le\nu((B-x)/m)\le\nu(B/m).
\]
For \(n\ge4\) and \(B\ge B_2\), the symmetric allocation \(x=0\), \(y_i=B/m\) attains the final bound. Strict increase of \(\nu\) forces \(x=0\) in every global optimizer. Equality in the averaged Rayleigh bound forces every test vector described above to attain the minimum Rayleigh quotient, hence to be an eigenvector of \(L\). Comparing the clique-leaf eigenvector equation with the corresponding equation for \(C(\bar y)\) gives \((y_i-\bar y)(a-b)\theta_i=0\). Here \(a\ne b\), and for each \(i\) there exists a zero-sum unit \(\theta\) with \(\theta_i\ne0\). Thus every \(y_i=\bar y=B/m\), proving global uniqueness in the high-budget regime.

The limiting optimal value follows from the displayed formula for \(\nu(y)\), and, for \(n=3\), from \(\nu(y)\to2\) as \(y\to\infty\). This completes the proof.

## Verification

The standalone script `verify_multiplex.py` uses Python's standard library only. It checks exact rational characteristic identities at both transition budgets for integer \(3\le n\le24\), computes spectra of the full \(2n\)-vertex Laplacian using a symmetric Jacobi algorithm for \(3\le n\le11\), and checks 707 finite identities and neighboring allocations. It prints `PASS: 707 finite exact-identity, direct-spectrum, and neighboring-design checks`. These checks supplement, but do not replace, the preceding proof for all \(n\) and \(B\).

For example, \(n=4\) has transition budgets \(B_1=16/5\) and \(B_2=6\); for \(B\ge6\), every optimizer deletes the center-to-center matching edge. At \(n=3\), that matching edge remains positively weighted at every finite budget above \(9/4\), contrasting with all \(n\ge4\).

## Relationship to prior work

Shakeri et al. [1] formulate precisely the weighted one-to-one multiplex spectral-gap program and prove a universal linear-budget bound, uniform-weight necessity, and a general first-transition criterion. The **uniform regime is a specialization** of their general theory, and is not claimed as novel. The distinctive claims here are the complete algebraic solution beyond that regime, the explicit second threshold, the hub-link extinction and high-budget global uniqueness, and the exceptional behavior at three nodes. The broader treatments [2,3] develop semidefinite/embedding methods and general structural transitions, but the inspected full material of [3] does not specify this clique–star matching family or these exact formulas. The full text of [2] was not obtained, leaving a documented literature-coverage risk. An indexed-title or abstract search does not prove the absence of an equivalent formula in other literature.

## Limitations

Only one clique layer, one star layer, unit intralayer conductances, and the specified center-aligned perfect matching are covered. Negative matching conductances, unequal fixed intralayer weights, and other interlayer patterns are outside scope. Uniqueness of **arbitrary nonsymmetric** optimizers is not established for intermediate budgets. Independently verified novelty and external validation have not been performed. The complete text of one potentially relevant later paper [2] could not be inspected.

## References

[1] H. Shakeri, N. Albin, F. Darabi Sahneh, P. Poggi-Corradini, and C. Scoglio, “Maximizing Algebraic Connectivity in Interconnected Networks,” arXiv:1510.06785v1, first publicly posted 2015-10-22; Physical Review E 93 (2016), 030301, DOI:10.1103/PhysRevE.93.030301.

[2] H. Shakeri, A. Tavasoli, E. Ardjmand, and P. Poggi-Corradini, “Designing optimal multiplex networks for certain Laplacian spectral properties,” arXiv:1903.01073 (2019), Physical Review E 102 (2020), 022302, DOI:10.1103/PhysRevE.102.022302. Only title and abstract were accessible for comparison.

[3] A. Tavasoli, H. Shakeri, E. Ardjmand, and S. Rahman, “The art of interconnections: Achieving maximum algebraic connectivity in multilayer networks,” Network Science 12 (2024), 261–288, DOI:10.1017/nws.2024.9; freely readable complete HTML article.
