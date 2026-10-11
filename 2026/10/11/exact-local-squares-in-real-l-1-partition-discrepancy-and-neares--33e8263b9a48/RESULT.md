# Exact local squares in real \(L_1\): partition discrepancy and nearest square points

## Finding

Let \(X=L_1(\Omega,\Sigma,\mu;\mathbb R)\) have dimension at least two, with \(\mu\) a \(\sigma\)-finite measure. For each \(f\in S_X\), define
\[
R(f)=\inf_{g\in S_X}\max\{\|f+g\|_1,\|f-g\|_1\},\qquad
 d(f)=\min_{A\in\Sigma}\left|\int_A |f|\,d\mu-\int_{\Omega\setminus A}|f|\,d\mu\right|.
\]
Then both minima below are attained, and
\[
\boxed{R(f)=1+d(f)},\qquad
\boxed{\operatorname{dist}_1(f,E)=d(f)},\qquad
 E=\{h\in S_X:R(h)=1\}.
\]
In particular, the exact local square points are precisely the unit functions for which the finite measure \(|f|\,d\mu\) admits an equal-mass measurable bipartition. At such a point every exact square partner \(g\in S_X\) obeys \(|g|=|f|\) almost everywhere, and is obtained by changing the sign of \(f\) on a set of precisely half of its \(L_1\)-mass.

Write \(a_j\) for the (at most countably many) positive masses of the atoms of \(|f|\,d\mu\), and write \(c=1-\sum_j a_j\) for its atomless mass. The defect has the exact atomic/diffuse form
\[
\boxed{d(f)=\max\!\left\{0,\min_{\varepsilon_j\in\{-1,1\}}
\left|\sum_j\varepsilon_j a_j\right|-c\right\}}.
\]
The minimum exists even when there are countably infinitely many atoms. For finite-dimensional \(\ell_1^n\), this reads
\[
d(f)=\min_{\varepsilon_i\in\{-1,1\}}
\left|\sum_{i=1}^{n}\varepsilon_i|f_i|\right|.
\]
Consequently, deciding exact square-point membership in real \(\ell_1^n\), given nonnegative rational unit coordinates and variable \(n\), is NP-complete by equivalence with equal-sum PARTITION.

There is also a quantitative partner-stability statement: if \(f,g\in S_X\) and
\(\max\{\|f+g\|_1,\|f-g\|_1\}=1+\eta\), one may choose a measurable sign function \(\sigma:\Omega\to\{-1,1\}\) so that
\[
\boxed{\|g-\sigma f\|_1\le2\eta},\qquad
\boxed{\left|\int_\Omega\sigma |f|\,d\mu\right|\le\eta}.
\]
The coefficient two in the first inequality and the coefficient one in the second are sharp in dimensions at least two.

## Assumptions and scope

Only real-valued \(L_1\) spaces are asserted; the measure is \(\sigma\)-finite and \(\dim X\ge2\). The \(L_1\)-unit sphere is \(S_X=\{f:\|f\|_1=1\}\). An atom means an atom of the **finite** measure \(\nu_f(A)=\int_A|f|\,d\mu\); the atomless remainder is considered modulo \(\nu_f\)-null sets. Empty atomic families are allowed and their signed sum is zero. The case \(\dim X=1\) has \(R(f)=2\) but an empty exact-square locus \(E\), so is excluded from the distance formula.

## Proof

**1. Exact pair identity and lower bound.** Fix \(f,g\in S_X\), put \(u=|f|\), \(v=|g|\), and choose the measurable sign \(\sigma=1\) where \(fg\ge0\), \(\sigma=-1\) otherwise (either choice works on zero sets). Set
\[
e=\int_\Omega(u-v)_+\,d\mu=\int_\Omega(v-u)_+\,d\mu,\qquad
D=\int_\Omega\sigma\min(u,v)\,d\mu.
\]
Since \(|f+g|+|f-g|=2\max(u,v)\) and \(|f+g|-|f-g|=2\sigma\min(u,v)\), direct integration gives the **exact identity**
\[
\max\{\|f+g\|_1,\|f-g\|_1\}=1+e+|D|.
\]
Moreover, \(\left|\int\sigma u\,d\mu-D\right|\le\int(u-v)_+\,d\mu=e\). Consequently
\[
 e+|D|\ge\left|\int_\Omega\sigma u\,d\mu\right|\ge d(f),
\]
which proves \(R(f)\ge1+d(f)\). It also proves both stated stability inequalities, since \(\|g-\sigma f\|_1=\|v-u\|_1=2e\), while \(e+|D|=\eta\). For sharpness take \(f\) and \(g\) supported on distinct disjoint unit \(L_1\) directions: \(e=1\), \(\eta=1\), \(\|g-\sigma f\|_1=2\), \(\left|\int\sigma |f|\right|=1\).

**2. Attainment and partition formula.** The measure \(\nu_f=|f|\mu\) is finite of total mass one. Its positive atoms form a finite or countable family with masses \(a_j\); its atomless remainder has mass \(c\). Every measurable signed mass \(\int\sigma\,d\nu_f\) is of the form
\(\sum_j\varepsilon_j a_j+t\), where \(\varepsilon_j\in\{-1,1\}\) and \(-c\le t\le c\). Conversely every such value is realized, because a finite atomless measure can be subdivided into any prescribed fraction of its total mass. The signed subsums form a compact set as a continuous image of the product space \(\{-1,1\}^{\mathbb N}\): convergence is uniform since \(\sum_j a_j<\infty\). Hence distance to zero is achieved and equals \(\max\{0,\min_\varepsilon |\sum_j\varepsilon_j a_j|-c\}\). Thus the minimum in the definition of \(d(f)\) is attained by a measurable set \(A\).

For an optimal \(A\), let \(\sigma_A=1\) on \(A\) and \(-1\) off \(A\). Then \(g=\sigma_A f\) has unit norm, \(e=0\), and \(D=\int\sigma_A |f|=\pm d(f)\), so the identity in step 1 yields \(R(f)\le1+d(f)\). If \(R(f)=1\), the same identity forces \(e=D=0\); therefore \(|g|=|f|\) and \(\sigma\) exactly balances the mass. This proves the partner classification.

**3. Exact distance to the square locus.** The function \(d\) is 1-Lipschitz on the unit sphere: every test functional \(f\mapsto\int\sigma_A|f|\,d\mu\) changes by at most \(\|f-h\|_1\), and the same uniform bound passes to the infimum of absolute values. Thus, because \(d(h)=0\) for every \(h\in E\),
\(\operatorname{dist}_1(f,E)\ge d(f)\).

Choose an optimal measurable partition \(A,A^c\). Write \(p=\int_A|f|\), \(q=1-p\); interchanging parts if necessary makes \(p=(1+d(f))/2\) and \(q=(1-d(f))/2\). If \(d(f)<1\), both are positive. Define
\[
h=\frac{f\mathbf1_A}{2p}+\frac{f\mathbf1_{A^c}}{2q}.
\]
Then \(h\in S_X\), each part has mass one-half, so \(h\in E\), and \(\|f-h\|_1=|p-1/2|+|q-1/2|=d(f)\).

If \(d(f)=1\), the measure \(\nu_f\) cannot contain two disjoint sets of positive \(\nu_f\)-measure, so \(f\) is supported on a single \(\mu\)-atom. As \(\dim X\ge2\), there exists \(w\in S_X\) disjointly supported from \(f\). Setting \(h=(f+w)/2\) gives \(h\in E\) and \(\|f-h\|_1=1=d(f)\). Hence \(\operatorname{dist}_1(f,E)=d(f)\) with a nearest square point in every case.

**4. Finite-dimensional recognition.** On \(\ell_1^n\) with nonnegative rational \((f_i)\) of sum one, exact square membership is equivalent to a sign certificate \(\sum_i\varepsilon_i f_i=0\), so is in NP. Any instance of the classical equal-sum PARTITION problem for positive integers \((b_i)\) maps in polynomial time to \(f_i=b_i/\sum_j b_j\), with equivalence of the answers. Thus the stated recognition problem is NP-complete (without claiming strong NP-completeness).

## Verification

The included `verify.py` uses exact rational arithmetic to check the inequality for 80,722 signed candidate pairs in dimensions two through five, 575 minimizing sign partners, and 575 explicitly constructed nearest square points. These finite tests validate arithmetic and boundary cases but do not replace the analytical proof for arbitrary measures. The optional `stress_lp.py` uses SciPy HiGHS linear programming to minimize independently over sign orthants on 50 seeded rational profiles in dimensions two through six. Invoke `python3 verify.py`; optionally invoke `python3 stress_lp.py` with NumPy and SciPy installed.

## Relationship to prior work

The LASQ definition originates in Abrahamsen--Langemets--Lima. Ciaci studies positive local almost squareness of Banach lattices and notes that real \(L_1[0,1]\) is LASQ but cannot enjoy the positive variant. Rodríguez--Rueda Zoca establish weakly almost square behavior of atomless \(L_1\) and other function spaces by weakly null perturbations. Neither inspected article gives the exact single-point finite-measure discrepancy, closest exact square point, or finite-atomic membership decision problem stated here. A weakly null perturbation requirement is materially different from the single unrestricted unit perturbation optimized by \(R\). In particular, equal-mass atomic splittings may yield exact local squares although no nonzero weakly null perturbation exists in finite-dimensional \(\ell_1\).

## Limitations

The classification is for real \(L_1\), not complex-valued functions or other \(L_p\) exponents. The first equality extends to one-dimensional \(L_1\), but the distance identity requires dimension at least two. The finite calculations are not proofs of infinite-dimensional statements. Novelty is not certified against every unindexed formulation or unpublished work; an equivalent formulation of balanced local square partners could exist under different terminology. No independent audit has been performed.

## References

1. J. Rodríguez and A. Rueda Zoca, *On weakly almost square Banach spaces*, arXiv:2301.07943v1 (19 January 2023), https://arxiv.org/abs/2301.07943.
2. S. Ciaci, *Locally almost square Banach lattices*, arXiv:2210.13306v1 (24 October 2022), https://arxiv.org/abs/2210.13306.
3. T. A. Abrahamsen, J. Langemets, and V. Lima, *Almost square Banach spaces*, arXiv:1402.0818 (2014), https://arxiv.org/abs/1402.0818.
4. M. R. Garey and D. S. Johnson, *Computers and Intractability*, Freeman, 1979, PARTITION problem SP12 (standard NP-completeness source).
