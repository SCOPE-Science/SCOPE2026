# Total perfect Roman domination polynomial of crown graphs

## Finding
For every integer \(n\ge3\), let \(\operatorname{Cr}_n\) be the crown graph with vertices \(A_1,\ldots,A_n,B_1,\ldots,B_n\), where \(A_iB_j\) is an edge exactly when \(i\ne j\). Define the total perfect Roman domination polynomial
\[
\mathcal T_n(z)=\sum_{f\in\mathrm{TPR}(\operatorname{Cr}_n)}z^{\sum_v f(v)},
\]
where the vertex labels are in \(\{0,1,2\}\), a zero-labeled vertex has exactly one neighbor labeled \(2\), and every positive-labeled vertex has a positive-labeled neighbor.

Write \(\delta_{r,s}=1\) when \(r=s\) and \(0\) otherwise. For \(0\le a,b\le n\) and \(\max\{0,a+b-n\}\le k\le\min\{a,b\}\), put
\[
c_{a,b,k}=\frac{n!}{k!(a-k)!(b-k)!(n-a-b+k)!}.
\]
Define the finite, explicit polynomial
\[
\begin{aligned}
F_n(z)={}&\sum_{a=0}^n\sum_{b=0}^n
\sum_{k=\max\{0,a+b-n\}}^{\min\{a,b\}}
c_{a,b,k}z^{2(a+b)}\\
&\quad\cdot(z+\delta_{b,2})^{b-k}(z+\delta_{a,2})^{a-k}\\
&\quad\cdot(z+\delta_{b,1})^{n-a-b+k}(z+\delta_{a,1})^{n-a-b+k}.
\end{aligned}
\]
Terms with exponent zero are \(1\). **The entire polynomial** is
\[
\boxed{\mathcal T_n(z)=F_n(z)-2nz^{n+2}-2nz^4(1+z)^{n-1}+nz^4-2n\,\delta_{n,3}(z^6+z^7).}
\]
In particular, its least exponent is \(6\), and
\[
\boxed{\gamma_{tR}^{p}(\operatorname{Cr}_n)=6,\qquad
[z^6]\mathcal T_n(z)=\begin{cases}31,&n=3,\\n^2(n-1),&n\ge4.\end{cases}}
\]
For \(n\ge4\), every minimum function has one vertex labeled \(2\) on each side, with precisely one additional vertex labeled \(1\) on each side. If the two label-\(2\) vertices have distinct indices, the label-\(1\) vertices are forced to have the opposite two indices. If they share index \(i\), the two label-\(1\) vertices may independently take any indices different from \(i\). All remaining vertices are labeled \(0\). The special graph \(\operatorname{Cr}_3\) is the six-cycle and has thirteen further minimum functions.

## Assumptions and scope
All graphs are finite, undirected, and simple. A total perfect Roman function \(f:V(G)\to\{0,1,2\}\) satisfies (i) \(|N(v)\cap f^{-1}(2)|=1\) whenever \(f(v)=0\) and (ii) \(G[f^{-1}(\{1,2\})]\) has no isolated vertex. The theorem concerns labeled crown graphs with \(n\ge3\); polynomial coefficients count distinct vertex assignments, not automorphism orbits.

## Proof
**1. Positive-support reduction.** Write \(p=|\{i:f(A_i)=2\}|\) and \(q=|\{i:f(B_i)=2\}|\). For zero labels the exact rules are
\[
f(A_i)=0\ \Longrightarrow\ q-\mathbf1_{\{f(B_i)=2\}}=1,\qquad
f(B_i)=0\ \Longrightarrow\ p-\mathbf1_{\{f(A_i)=2\}}=1.
\]
Every total perfect Roman function has at least two positive vertices in each side. Indeed, if there were no positive vertices on side \(A\), all positive vertices on side \(B\) would be isolated. If the only positive vertex of side \(A\) were \(A_i\) with label \(1\), there would be no label \(2\) on side \(A\), so every \(B_j\), in particular \(B_i\), would be positive; \(B_i\) would be isolated. If that only positive vertex were \(A_i\) with label \(2\), the zero rule forces \(B_i\) positive, again isolated. The same applies with the sides exchanged. Conversely, if each side has at least two positive vertices, any positive vertex has a positive neighbor: it can be nonadjacent to at most one vertex of the opposite side. Thus, for a perfect Roman labeling on a crown, totality is **equivalent** to at least two positive vertices on each side.

**2. Enumerate the perfect Roman functions.** Let \(X=\{i:f(A_i)=2\}\), \(Y=\{i:f(B_i)=2\}\), with \(|X|=a\), \(|Y|=b\), and \(|X\cap Y|=k\). The four index classes \(X\cap Y\), \(X\setminus Y\), \(Y\setminus X\), and \([n]\setminus(X\cup Y)\) have sizes \(k,a-k,b-k,n-a-b+k\), with exactly \(c_{a,b,k}\) choices. Every label \(2\) contributes \(z^2\). For \(i\in Y\setminus X\), vertex \(A_i\) can receive label \(0\) precisely when \(b=2\), yielding factor \(z+\delta_{b,2}\); for \(i\in X\setminus Y\), vertex \(B_i\) can receive \(0\) precisely when \(a=2\). At an index outside both sets, the corresponding \(A_i\) can receive \(0\) precisely when \(b=1\), and \(B_i\) precisely when \(a=1\). Otherwise those vertices are forced to label \(1\). Their choices are independent once \(X,Y\) are fixed. Multiplication gives \(F_n(z)\), the weight enumerator of *all perfect Roman* functions, without the positive-support condition.

**3. Remove precisely the non-total functions.** A perfect Roman labeling cannot have zero positive vertices on a side when \(n\ge3\). Indeed, if every \(A_i\) were zero, all \(B_i\) would be positive (no \(B\)-zero could see an \(A\)-two). Writing \(q\) for the number of \(B\)-twos, the zero equations require \(q-\mathbf1_{\{B_i=2\}}=1\) for every index. If \(0<q<n\), indices with and without a \(B\)-two impose the incompatible equalities \(q-1=1\) and \(q=1\). If \(q=0\) no zero is defended, and if \(q=n\ge3\) every zero sees at least two twos. Hence zero-positive-side cases do not occur even before totality is imposed. By Step 1, the remaining non-total perfect Roman labelings have exactly one positive vertex on at least one side. Fix that vertex as \(A_i\). If it is labeled \(1\), the entire \(B\)-side is positive, and the zero rules allow only \(B_i=2\) with all other \(B\)'s labeled \(1\) (weight \(n+2\)); when \(n=3\) there is also the possibility that the other two \(B\)'s are labeled \(2\), while \(B_i=1\) (weight \(6\)). If \(A_i=2\), the zero rule forces \(B_i\) positive. There are (a) \(B_i=2\) with arbitrary \(0/1\) labels on the remaining \(B\)'s (enumerator \(z^4(1+z)^{n-1}\)), and (b), only when \(n=3\), \(B_i=1\) and both other \(B\)'s labeled \(2\) (weight \(7\)). All remaining \(A\)'s are zero. The generating function for the one-positive-\(A\)-side exceptions is consequently
\[
E_n(z)=nz^{n+2}+nz^4(1+z)^{n-1}+n\delta_{n,3}(z^6+z^7).
\]
The opposite side has the same exceptional enumerator. Their intersection consists exactly of \(n\) functions with \(A_i=B_i=2\) for one index and all other labels zero (weight \(4\)). Inclusion–exclusion gives \(\mathcal T_n=F_n-2E_n+nz^4\), as claimed.

**4. Minimum and optimizer classification.** Suppose \(n\ge4\). If \(p=0\), all \(B\)-vertices are positive. With \(q=0\), all vertices are positive and the weight is at least \(2n\); with \(q\ge1\), the \(B\)-side has weight at least \(n+1\) and at least two positive vertices on side \(A\) contribute two more, giving at least \(n+3\ge7\). The same reasoning applies if \(q=0\). Thus every function of weight at most \(6\) has \(p,q\ge1\). If \(p+q\ge4\), the twos alone have weight at least \(8\). If \(p+q=3\), one side has only one label \(2\), hence needs at least one additional positive label and the total weight is at least \(7\). Necessarily \(p=q=1\), and the two-positive-per-side condition forces at least one label \(1\) on each side, so weight at least \(6\). Put the two labels \(2\) at \(A_i,B_j\). If \(i\ne j\), then \(A_j,B_i\) are forced positive by the zero condition and must be the two labels \(1\). There are \(n(n-1)\) such functions. If \(i=j\), choose one other \(A\) and one other \(B\) independently for the labels \(1\); the \(n(n-1)^2\) assignments are valid. Hence the count is \(n^2(n-1)\), and the lower bound is attained.

For \(n=3\), the same analysis with \(p,q\ge1\) gives \(18\) weight-six assignments. The case \(p=q=0\) gives one all-one function, and the cases \((p,q)=(0,1),(1,0)\) give \(2n(n-1)=12\) further weight-six assignments. The other cases require weight above six. Thus the exact minimum count is \(18+1+12=31\), completing the proof.

## Verification
The standalone `verify.py` calculates the closed formula using exact integer polynomial arithmetic. Independently it enumerates all \(3^{2n}\) ternary labelings for \(n=3,4,5,6\) and checks every zero vertex's actual graph neighbors and every positive vertex's actual graph neighbors. All four coefficient lists agree, covering \(597780\) unrestricted assignments. Formula-only arithmetic checks the minimum coefficient through \(n=12\). The deterministic record is in `verification_output.txt`; these finite checks corroborate but do not replace the universal proof.

## Relationship to prior work
Almulhim's 2023 introduction of total perfect Roman domination gives the definition, foundational inequalities and complexity results; its Proposition 2 determines the minimum for complete multipartite graphs. A crown graph is **not** complete multipartite for \(n\ge3\). In particular, the prior bipartite formula gives \(\gamma_{tR}^p(K_{n,n})=4\), whereas this theorem proves \(\gamma_{tR}^p(K_{n,n}-M)=6\). The known cycle statement also implies the numerical value \(6\) at \(n=3\), but does not enumerate these functions. Separately, the published mathematical record *Perfect Roman domination of crown graphs* determines the weaker perfect Roman domination minimum \(4\) and its optimizer count; it does not assert the total-perfect weight polynomial. The extra positive-neighbor condition is essential and is not determined by that prior scalar invariant. The available source-summary evidence leaves a possibility of unidentified equivalent published results.

## Limitations
Only once-deleted perfect matchings in balanced complete bipartite graphs are considered; arbitrary deleted edges and unbalanced bipartite graphs are not classified. The integer polynomial counts labeled functions and does not classify automorphism orbits. Bibliographic priority against unindexed works is not independently certified. Independent validation has not been performed.

## References
1. A. Almulhim, *Total Perfect Roman Domination*, Symmetry **15** (2023), 1676, DOI: 10.3390/sym15091676, first published 31 August 2023. Full article contains Definition 1, Proposition 2, and the cycle observation.
2. *Perfect Roman domination of crown graphs*, published mathematical research record (2026), identifier `e57b781e4a71`. The accessible summary concerns ordinary perfect Roman domination, not total perfect Roman domination.
