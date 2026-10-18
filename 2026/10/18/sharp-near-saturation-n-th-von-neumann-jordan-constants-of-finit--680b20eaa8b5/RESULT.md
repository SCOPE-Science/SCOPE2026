# Sharp near-saturation \(n\)-th von Neumann–Jordan constants of finite real cubes

## Finding
For all integers \(n\ge2\) and \(2^{n-2}\le m\le2^{n-1}\), put \(k=2^{n-1}\), \(r=k-m\), and \(A=2-4r/k\). The upper \(n\)-th von Neumann–Jordan constant of the **real** coordinate cube is exactly
\[
\overline C_{NJ}^{(n)}(\ell_\infty^m(\mathbb R))=
\frac{n+\sqrt{(n-2)^2+(n-1)A^2}}{2}.
\]
The statement includes the endpoint \(m=k\), where the value is \(n\); its substantive region is \(k/2\le m<k\). A stronger sharp statement fixes the input norms: for any nonnegative \(t_1,\ldots,t_n\), with \(T=\sum_jt_j\) and \(b=\min_jt_j\),
\[
\max_{\|x_j\|_\infty=t_j}\;2^{1-n}\sum_{\varepsilon_2,\ldots,\varepsilon_n=\pm1}
\left\|x_1+\sum_{j=2}^n\varepsilon_jx_j\right\|_\infty^2
=T^2-\frac{4r}{k}\,b(T-b).
\]
In the first previously unsaturated five-dimensional four-input example this gives
\[
\overline C_{NJ}^{(4)}(\ell_\infty^5(\mathbb R))=2+\frac{\sqrt{19}}4,
\]
strictly between the values \(3\) at dimension \(4\) and \(4\) at dimension \(8\).

## Assumptions and scope
All scalars, signs, normed spaces and linear combinations here are real. For any real Banach space \(X\), define
\[
\overline C_{NJ}^{(n)}(X)=\sup_{\sum_j\|x_j\|^2>0}
\frac{2^{1-n}\sum_{(\varepsilon_2,\ldots,\varepsilon_n)\in\{-1,1\}^{n-1}}
\|x_1+\sum_{j=2}^n\varepsilon_jx_j\|^2}{\sum_{j=1}^n\|x_j\|^2}.
\]
The integer restriction \(2^{n-2}\le m\le2^{n-1}\) is essential for the simple exact nearest-neighbor row-covering formula. No result is asserted here for smaller dimensions, other scalar fields, or modified constants requiring all input norms to equal one.

## Proof
**1. Endpoint rows and projective sign classes.** Fix \(t_j\ge0\) and write each \(x_j\in\ell_\infty^m\) as a column of an \(m\)-by-\(n\) real matrix, with coordinate bounds \(|x_{ij}|\le t_j\). Each squared maximum of finitely many linear forms is convex in the full matrix, so the averaged objective is convex on the box of entries. A convex function on a box has a maximizing vertex; each entry can therefore be chosen as \(\pm t_j\). Such vertex columns have exactly the prescribed norms. When a weight vanishes the same reasoning applies with coincident endpoints.

Let \(k=2^{n-1}\). The \(2^n\) sign vectors modulo simultaneous sign reversal give \(k\) projective classes. Each of the \(m\) coordinate rows of a vertex matrix represents one class (allowing repetition). At a class represented by some row, the square of the largest absolute signed sum is \(T^2\). At an unrepresented class \(s\), every row class is different, so for each row both its agreement and disagreement sets with \(s\) are nonempty after choosing one of the two global signs. Their \(t\)-weights are each at least \(b\) when \(b>0\). Thus the absolute signed sum is at most \(T-2b\). For \(b=0\) the same bound \(T\) is immediate. Since at least \(r=k-m\) sign classes are unrepresented and \((T-2b)^2\le T^2\), the averaged square is at most
\[
\frac{mT^2+r(T-2b)^2}{k}=T^2-\frac{4r}{k}b(T-b).
\]

**2. Sharp covering.** Choose an index \(j_*\) attaining the minimum weight \(b\). Flipping only sign \(j_*\) gives a fixed-point-free involution on the \(k\) projective classes, partitioning them into \(k/2\) disjoint pairs (for \(n=2\) it is one pair). Since \(r\le k/2\), delete precisely one class from each of \(r\) distinct pairs and represent every remaining class by one matrix row. Every deleted class then has a represented class differing only in sign \(j_*\). Its attained absolute signed sum is \(T-2b\); represented classes attain \(T\). This realizes the upper bound simultaneously for every sign class and proves the fixed-input-norm formula.

**3. Optimize the norms.** Put \(d=n-1\), \(h=4r/k\in[0,2]\), and normalize \(\sum_jt_j^2>0\). Fix \(b=\min_jt_j\) and \(M=\sum_jt_j^2\). The numerator \(T^2-hb(T-b)\) is nondecreasing in \(T\ge nb\), because its derivative is \(2T-hb\ge0\). The Cauchy–Schwarz bound \(T\le b+\sqrt{d(M-b^2)}\) is attained when the other \(d\) weights all equal \(a\ge b\). Write \(q=b/a\in[0,1]\), with the all-zero case excluded. The quotient is exactly
\[
F(q)=\frac{d^2+dAq+q^2}{d+q^2},\qquad A=2-h\in[0,2].
\]
This is the Rayleigh quotient of the symmetric matrix
\[
\begin{pmatrix}d&\sqrt d\,A/2\\ \sqrt d\,A/2&1\end{pmatrix}
\]
on the vector \((\sqrt d,q)\). Its largest eigenvalue is
\[
\lambda_+=\frac{d+1+\sqrt{(d-1)^2+dA^2}}2.
\]
For \(d>1\), the maximizing positive eigenvector has \(q\le1\), since the ratio \(q=dA/[2(\lambda_+-1)]\le1\); the inequality follows from \(\lambda_+\ge(dA+2)/2\) for \(0\le A\le2\) (equivalently, square the nonnegative sides). For \(d=1\), the same eigenvector has \(q=1\) when \(A>0\), and when \(A=0\) every \(q\) is optimal. Alternatively, \(F'(0)\ge0\) and \(F'(1)=d(d-1)(A-2)/(d+1)^2\le0\) give direct feasible attainment. Consequently the supremum equals \(\lambda_+\), the displayed formula. The row-covering construction supplies concrete norm-attaining vectors.

**4. Sharp five-dimensional instance.** For \(n=4,m=5\), take \(a=1\), \(b=q=\sqrt{19}-4\) and five rows
\[
\begin{pmatrix}
1&1&-q&1\\
1&1&-q&-1\\
1&-1&q&-1\\
1&-1&-q&1\\
1&-1&-q&-1
\end{pmatrix}.
\]
The remaining three projective classes are obtained by flipping column three in the three distinct indicated pairs. Direct substitution gives the exact value \(2+\sqrt{19}/4\).

## Verification
The finite combinatorial fixed-weight optimization was independently recomputed by an exact-rational exhaustive checker for all admissible dimensions through \(n=4\), over three prescribed nonnegative weight profiles per \((n,m)\), comprising 30 checks in total. This is a finite diagnostic, not a proof for arbitrary \(n\). The theorem follows instead from the endpoint-row lemma, the projective pairing construction, and the two-variable Rayleigh quotient. The five-dimensional optimizer additionally satisfies the exact algebraic identities \(q^2+8q-3=0\) and \(F(q)=2+\sqrt{19}/4\). A standalone standard-library checker is included.

## Relationship to prior work
Kato, Takahashi and Hashimoto introduced the \(n\)-th von Neumann–Jordan constant and its Banach-space geometric interpretation. Ciesielski and Płuciennik (Proposition 4(b), 2020) explicitly establish the saturated value \(n\) for real \(\ell_\infty^m\) when \(m\ge2^{n-1}\). Their displayed proposition does not give the strict intermediate-dimensional values established here. A separately reported computation for three inputs in dimension three agrees with the present formula at \(n=m=3\); this already-known special case is not claimed to be new. The work treats unrestricted input lengths, not the modified unit-sphere constant. Broader literature equivalences to finite Rademacher type-two bounds were examined for possible implication rather than compared by title alone.

## Limitations
The source record and accessible synopsis of the 1998 foundational paper were checked, but the complete original PDF could not be retrieved, leaving a bibliographic residual risk. The 2020 full open-access article was materially inspected at its definitions, theorem and proof of Proposition 4(b). No absolute claim of priority or exhaustive literature coverage is made. The result does not cover \(m<2^{n-2}\), complex cubes, or sphere-normalized modified constants.

## References
- M. Kato, Y. Takahashi, K. Hashimoto, *On n-th von Neumann–Jordan Constants for Banach Spaces*, Bulletin of the Kyushu Institute of Technology, Pure and Applied Mathematics 45 (1998), 25–33. DOI: https://doi.org/10.18997/00002034. Public repository entry: https://kyutech.repo.nii.ac.jp/records/2040.
- M. Ciesielski, R. Płuciennik, *On some modifications of n-th von Neumann–Jordan constant for Banach spaces*, Banach Journal of Mathematical Analysis 14 (2020), 650–673, especially Proposition 4(b). DOI: https://doi.org/10.1007/s43037-019-00033-1. Earlier preprint: https://arxiv.org/abs/1811.01652.
