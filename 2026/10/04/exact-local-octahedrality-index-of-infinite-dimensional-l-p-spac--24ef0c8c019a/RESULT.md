# Exact local-octahedrality index of infinite-dimensional \(L_p\) spaces
## Finding
Let \((\Omega,\Sigma,\mu)\) be a complete sigma-finite measure space, let \(1\le p<\infty\), and assume \(L_p(\mu)\) is infinite-dimensional. Define Hardtke's local-octahedrality index by
\[
s(X)=\sup\left\{c\in[0,2]:\forall x\in S_X\ \forall\varepsilon>0\ \exists y\in S_X\ \min\{\|x+y\|,\|x-y\|\}\ge c-\varepsilon\right\}.
\]
Then
\[
s(L_p(\mu))=
\begin{cases}
2^{1/p},&1\le p\le2,\\
2^{1-1/p},&2<p<\infty\text{ and }\mu\text{ is atomless},\\
2^{1/p},&2<p<\infty\text{ and }\mu\text{ has an atom}.
\end{cases}
\]
In particular, when \(p>2\), this quantitative local-octahedrality invariant distinguishes atomless \(L_p\)-spaces from every infinite-dimensional \(L_p\)-space containing even one atom.

## Assumptions and scope
All spaces are real. The measure space is complete and sigma-finite, and \(L_p(\mu)\) is assumed infinite-dimensional. A measurable set \(A\) is an atom when \(\mu(A)>0\) and every measurable \(B\subseteq A\) has either \(\mu(B)=0\) or \(\mu(A\setminus B)=0\). The case \(p=\infty\) is not claimed.

The formula concerns the exact numerical index \(s(X)\), not merely the qualitative statement that \(X\) is locally octahedral. By definition, \(X\) is locally octahedral exactly when \(s(X)=2\).

## Proof
First record a support-escape lemma. Since \(L_p(\mu)\) is infinite-dimensional and \(\mu\) is sigma-finite, there are pairwise disjoint measurable sets \((E_n)\) with \(0<\mu(E_n)<\infty\). Indeed, either there are infinitely many atoms, or a nonzero atomless part can be split into countably many positive finite-measure pieces. For a fixed \(x\in S_{L_p}\), disjointness gives
\[
\sum_n\|x\mathbf 1_{E_n}\|_p^p\le1,
\]
so along a subsequence \(\|x\mathbf 1_{E_n}\|_p\to0\). Choose \(y_n\in S_{L_p}\) supported in \(E_n\). Writing \(u_n=x\mathbf 1_{E_n^c}\) and \(v_n=x\mathbf 1_{E_n}\), the supports of \(u_n\) and \(y_n\) are disjoint, hence
\[
\|u_n\pm y_n\|_p=(\|u_n\|_p^p+1)^{1/p}.
\]
Therefore
\[
\|x\pm y_n\|_p\ge(\|u_n\|_p^p+1)^{1/p}-\|v_n\|_p\longrightarrow2^{1/p}.
\]
Thus every infinite-dimensional \(L_p(\mu)\) satisfies \(s(L_p(\mu))\ge2^{1/p}\).

Assume first \(1<p\le2\), and put \(q=p/(p-1)\). Clarkson's inequality gives, for \(x,y\in S_{L_p}\),
\[
\left\|\frac{x+y}{2}\right\|_p^q+\left\|\frac{x-y}{2}\right\|_p^q\le1.
\]
Hence
\[
\min\{\|x+y\|_p,\|x-y\|_p\}\le2^{1/p}.
\]
Together with the support-escape lower bound this proves \(s(L_p(\mu))=2^{1/p}\). For \(p=1\), the same lower bound tends to \(2\), while no distance between two unit-ball points exceeds \(2\), so \(s(L_1(\mu))=2\).

Now let \(2<p<\infty\) and suppose \(\mu\) is atomless. Clarkson's other inequality gives
\[
\left\|\frac{x+y}{2}\right\|_p^p+\left\|\frac{x-y}{2}\right\|_p^p\le1,
\]
so for unit vectors
\[
\min\{\|x+y\|_p,\|x-y\|_p\}\le2^{1-1/p}.
\]
For the reverse inequality fix \(x\in S_{L_p}\). The finite measure \(\nu(B)=\int_B|x|^p\,d\mu\) is atomless, so choose \(A\in\Sigma\) with \(\nu(A)=1/2\). Put
\[
y=(2\mathbf 1_A-1)x.
\]
Then \(\|y\|_p=1\), and
\[
x+y=2x\mathbf 1_A,\qquad x-y=2x\mathbf 1_{A^c}.
\]
Consequently
\[
\|x+y\|_p=\|x-y\|_p=2^{1-1/p}.
\]
Thus \(s(L_p(\mu))=2^{1-1/p}\) in the atomless case.

Finally let \(2<p<\infty\) and suppose \(\mu\) has an atom \(A\). Sigma-finiteness implies \(\mu(A)<\infty\). Set \(x=\mu(A)^{-1/p}\mathbf 1_A\in S_{L_p}\). For arbitrary \(y\in S_{L_p}\), measurability on an atom gives \(y\mathbf 1_A=cx\) almost everywhere for some scalar \(c\). Put \(a=|c|\in[0,1]\). Then \(\|y\mathbf 1_{A^c}\|_p^p=1-a^p\), and choosing the smaller of the two signs yields
\[
\min\{\|x+y\|_p^p,\|x-y\|_p^p\}=(1-a)^p+1-a^p.
\]
The right-hand side is decreasing on \([0,1]\), because its derivative is
\[
-p(1-a)^{p-1}-pa^{p-1}<0.
\]
It is therefore at most \(2\), so
\[
\min\{\|x+y\|_p,\|x-y\|_p\}\le2^{1/p}.
\]
Combined with the universal support-escape lower bound, this proves \(s(L_p(\mu))=2^{1/p}\) whenever an atom is present.

## Verification
The proof was replayed case by case against the defining quantifiers of \(s(X)\). The lower bound uses only disjoint supports and the standard structure of infinite-dimensional sigma-finite measure spaces. The two upper bounds are exact Clarkson inequalities, and the atomless lower extremizer is an explicit sign split of an arbitrary unit vector. In the atomic case, the chosen unit vector is supported on one atom and the remaining scalar optimization is strictly monotone.

Boundary checks agree: at \(p=2\), both formulas give \(\sqrt2\); for counting measure, which is atomic, the formula gives \(s(\ell_p)=2^{1/p}\); for \(p=1\), it gives \(2\), consistent with local octahedrality. No finite experiment is used as evidence for the infinite-dimensional statement.

## Relationship to prior work
Hardtke introduced the numerical invariant \(s(X)\) while studying local octahedrality of absolute sums. In that paper he records \(s(\mathbb R)=0\), \(s(c_0)=s(\ell_\infty)=1\), the finite-dimensional sup-norm cases, and \(s(H)=\sqrt2\) for Hilbert spaces of dimension at least two. The inspected statement does not give the \(L_p\) classification above, and the Hilbert value is exactly the \(p=2\) boundary case of the present formula.

Hardtke's later Köthe-Bochner work proves qualitative preservation of local octahedrality and local almost squareness under broad function-space constructions. The inspected theorem does not introduce or compute the quantitative index \(s(X)\), and therefore does not imply the atomic-versus-atomless values above.

## Limitations
The theorem is restricted to complete sigma-finite measure spaces and \(1\le p<\infty\). It does not classify finite-dimensional \(L_p\)-spaces, non-sigma-finite measure spaces, or \(L_\infty\). Originality was checked by focused semantic searches and direct inspection of the most relevant public primary texts; that reduces but cannot eliminate the possibility of an equivalent result under different terminology.

## References
1. J.-D. Hardtke, *Summands in locally almost square and locally octahedral spaces*, arXiv:1705.06610v1 (2017); Acta Comment. Univ. Tartu. Math. 22 (2018), 149–162. DOI: 10.12697/ACUTM.2018.22.13.
2. J.-D. Hardtke, *Locally octahedral and locally almost square Köthe-Bochner spaces*, arXiv:2107.01180v1 (2021).
3. J. A. Clarkson, *Uniformly convex spaces*, Trans. Amer. Math. Soc. 40 (1936), 396–414.
