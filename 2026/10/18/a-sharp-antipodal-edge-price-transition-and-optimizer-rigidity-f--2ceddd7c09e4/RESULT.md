# A sharp antipodal-edge price transition and optimizer rigidity for fastest diffusion on folded hypercubes

## Finding

**Theorem.** Let \(d\ge2\) be an integer, \(B>0\), and \(t>0\). Start with the \(d\)-dimensional Boolean hypercube \(Q_d\), and add the perfect matching joining every binary vector \(x\in\{0,1\}^d\) to its complement \(\overline x\). Assign independently chosen nonnegative conductances to all hypercube edges and added antipodal edges. Charge unit price per hypercube-edge conductance and price \(t\) per antipodal-edge conductance, with **exact** total budget \(B\). Maximize the algebraic connectivity \(\lambda_2(L)\) of the weighted combinatorial Laplacian \(L\). Put \(M=2^{d-1}\).

The optimum is
\[
\max\lambda_2(L)=\begin{cases}
\displaystyle\frac{4B}{M(d+t)},&0<t<d,\\[2mm]
\displaystyle\frac{2B}{Md},&t\ge d.
\end{cases}
\]
If \(0<t<d\), the **unique** optimizer places the common conductance \(a=b=B/[M(d+t)]\) on every hypercube edge and every antipodal edge. If \(t>d\), the **unique** optimizer places conductance \(a=B/(Md)\) on every hypercube edge and zero conductance \(b=0\) on every antipodal edge. At the critical price \(t=d\), the **entire optimizer set**, including all initially unrestricted assignments, consists exactly of common class weights satisfying
\[
a+b=\frac{B}{Md},\qquad 0\le b\le a.
\]
Thus the price \(t=d\) is an exact edge-deletion transition with a nontrivial one-dimensional optimal face precisely at equality. In particular, there are **no asymmetric optimizers** at any price.

## Assumptions and scope

For \(x\in\{0,1\}^d\) write \(x\oplus e_j\) for flipping coordinate \(j\) and \(\overline x=x\oplus(1,\ldots,1)\). There are \(dM\) ordinary edges and \(M\) antipodal edges. Because \(d\ge2\), these edge classes are disjoint. Set \(w_j(x)=w_j(x\oplus e_j)\ge0\) equal to the weight of the ordinary edge in coordinate \(j\) incident at \(x\); set \(v(x)=v(\overline x)\ge0\) for the antipodal edge at \(x\). Each edge appears twice in these endpoint-indexed arrays. We require
\[
\frac12\sum_{x,j}w_j(x)+\frac t2\sum_xv(x)=B.
\]
The Laplacian is \((Lf)(x)=\sum_j w_j(x)[f(x)-f(x\oplus e_j)]+v(x)[f(x)-f(\overline x)]\). The notation \(\lambda_2\) means the second-smallest eigenvalue **counting multiplicities**, including zero for disconnected choices. All conductances are free; no orbit symmetry is assumed.

## Proof

**Step 1 (two universal spectral certificates).** Let \(S_j=\frac12\sum_xw_j(x)\) and \(T=\frac12\sum_xv(x)\); then \(S_j,T\ge0\) and \(\sum_j S_j+tT=B\). For a nonempty coordinate set \(J\), its Walsh sign character is \(\chi_J(x)=(-1)^{\sum_{j\in J}x_j}\). It is orthogonal to constants and has squared Euclidean norm \(2^d=2M\). Consequently its Rayleigh quotient bounds \(\lambda_2\) from above.

For the \(d\) singleton characters and the \(\binom d2\) two-coordinate characters, direct edge-energy counting yields
\[
R(\chi_{\{j\}})=\frac{2(S_j+T)}M,
\qquad
R(\chi_{\{i,j\}})=\frac{2(S_i+S_j)}M.
\]
Averaging each of these two families separately gives
\[
\lambda_2\le A(T):=\frac{2[B+(d-t)T]}{Md},
\qquad
\lambda_2\le C(T):=\frac{4(B-tT)}{Md},
\qquad 0\le T\le\frac Bt.
\tag{1}
\]
These are genuine **global** bounds over all independently variable conductances, not only symmetric allocations.

If \(t<d\), then \(A(T)\) increases strictly with \(T\) and \(C(T)\) decreases strictly. Their unique crossing occurs at \(T=B/(d+t)\), and thus (1) bounds every feasible gap by \(4B/[M(d+t)]\). If \(t>d\), \(A(T)\le A(0)=2B/(Md)\), with equality only if \(T=0\). At \(t=d\), \(A(T)\equiv2B/(Md)\), independent of \(T\).

**Step 2 (attainability by explicit Walsh spectrum).** If all coordinate edges share conductance \(a\) and all antipodal edges share conductance \(b\), then the full family of \(2^d\) Walsh characters diagonalizes \(L\), with
\[
L\chi_J=\bigl(2a|J|+2b\,\mathbf1_{|J|\text{ odd}}\bigr)\chi_J.
\]
Since \(d\ge2\) and \(a,b\ge0\), it follows that
\[
\lambda_2(L)=\min\{2(a+b),4a\},
\qquad M(da+tb)=B.
\tag{2}
\]
For \(t<d\), take \(a=b=B/[M(d+t)]\); both branches in (2) equal the upper bound in Step 1. For \(t>d\), take \(a=B/(Md),b=0\); the first branch in (2) equals the upper bound. At \(t=d\), any \(a+b=B/(Md)\) with \(0\le b\le a\) has first branch equal to the bound and second branch no smaller. This proves all optimum values and exhibits the claimed allocations.

**Step 3 (equality rigidity when \(t<d\)).** Equality at the unique crossing in (1) forces *every* singleton and every two-coordinate Walsh character to attain the minimum Rayleigh quotient \(\lambda_2\): each individual quotient is at least \(\lambda_2\), and the average of its family equals \(\lambda_2\). By the spectral theorem each character must therefore be an actual \(\lambda_2\)-eigenvector. The pointwise eigen-equations, divided by the nowhere-zero Walsh signs, read
\[
2[w_j(x)+v(x)]=\lambda_2,
\qquad 2[w_i(x)+w_j(x)]=\lambda_2
\quad(i\ne j).
\]
For \(d=2\), the two singleton equalities and the one pair equality already imply \(w_1(x)=w_2(x)=v(x)=\lambda_2/4\). For \(d\ge3\), subtracting pair equations likewise gives all \(w_j(x)=\lambda_2/4\) and hence \(v(x)=\lambda_2/4\). This holds at every vertex, so the optimum has exactly the constant claimed conductances and is unique.

**Step 4 (rigidity when \(t>d\)).** Any optimizer must have \(T=0\) from strict decrease of \(A(T)\), so all antipodal conductances vanish. Equality in the singleton-average upper bound then makes each singleton character an eigenvector with eigenvalue \(\lambda_2\). Its pointwise equation yields \(2w_j(x)=\lambda_2\) for every \(j,x\). All ordinary edges therefore have the common required weight, proving uniqueness.

**Step 5 (the complete critical optimal face).** If \(t=d\), equality in \(A(T)=2B/(Md)\) forces every singleton character to be a \(\lambda_2\)-eigenvector. Thus
\[
w_j(x)+v(x)=\lambda_2/2\qquad\text{for every }j,x.
\]
Because the same ordinary edge satisfies \(w_j(x)=w_j(x\oplus e_j)\), these identities imply \(v(x)=v(x\oplus e_j)\) along every hypercube edge. The hypercube is connected, so \(v\) is constant; hence **every** \(w_j\) is the same constant, across coordinates and vertices. Write the resulting class weights as \(a,b\). The budget gives \(a+b=B/(Md)\), while (2) attains \(\lambda_2=2B/(Md)\) exactly when \(4a\ge2(a+b)\), equivalent to \(b\le a\). The family exhibited in Step 2 contains every possible optimizer. QED.

## Verification

The accompanying standalone `verify.py` reconstructs all weighted Laplacians directly, compares finite matrix eigenvalues with the exact formula, replays the entire critical optimal segment at eleven rational parameter values for each tested graph, checks Walsh eigen-equations, checks exact budgets, and tests two independent Rayleigh certificates on feasible nonuniform samples. It passed 2310 assertions for dimensions \(2\) through \(6\), multiple positive budgets and prices on both sides of and at the threshold. Finite checks are consistency tests; the theorem for **every** \(d\ge2\), \(B>0\), and \(t>0\) is established by the proof above.

## Relationship to prior work

Sun, Boyd, Xiao, and Diaconis [1] introduced the continuous-time fastest-mixing Markov-process problem, its convex/semidefinite formulation, and geometric duality. The current optimization objective and linear edge prices are direct instances of that general theory; this work does **not** claim them as innovations. Their detailed examples treat paths and cycles and do not give the folded-hypercube price transition or its full optimizer set. Boyd, Diaconis, Parrilo, and Xiao [2, Section 3.2.2] derive the Walsh-type spectrum for ordinary hypercubes in a **discrete-time** fastest-mixing problem; they do not treat independently priced antipodal matching edges or the global continuous-time optimal-face rigidity. Chen and Chen [3] derived spectra of the **unweighted** folded hypercube. Liu and colleagues [4] study Kirchhoff indices using unweighted Laplacian spectra, not fastest-diffusion conductance allocation.

The proof uses standard Walsh diagonalization for the symmetric representative, but the two Rayleigh certificates together with their **equality conditions** classify globally all independently adjustable edge weights, including the one-dimensional critical face. No claim is made that the underlying linear optimization framework or the folded-hypercube spectrum was previously unknown.

## Limitations

This is continuous-time, uniform-stationary diffusion measured by the weighted Laplacian's second eigenvalue, **not** the discrete-time fastest-mixing SLEM problem or an effective-resistance objective. The theorem assumes all original hypercube edges have unit price, all antipodal edges have a common price, and a fixed exact total conductance cost. Arbitrary within-class price heterogeneity is not covered. The dimension restriction \(d\ge2\) is essential for disjoint ordinary and antipodal edge classes. Finite numerical checks provide no independent proof of universal optimality. The bibliographic search may miss an equivalent theorem, including a specialization of general convex optimality conditions in inaccessible literature; independent validation has not been carried out.

## References

[1] J. Sun, S. Boyd, L. Xiao, and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48(4), 681–699 (2006), DOI: 10.1137/S0036144504443821, online 2006-11-02. Author-hosted full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf.

[2] S. Boyd, P. Diaconis, P. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs With Symmetries*, SIAM Journal on Optimization 20(2), 792–819 (2009), full text: https://stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf.

[3] M. Chen and B. Chen, *Spectrum of folded hypercubes*, Journal of East China Normal University (Natural Science), issue 2, 39–46 (2011), https://xblk.ecnu.edu.cn/CN/Y2011/V2011/I2/39.

[4] *The Kirchhoff Index of Folded Hypercubes and Some Variant Networks*, Mathematical Problems in Engineering (2014), DOI: 10.1155/2014/380874.
