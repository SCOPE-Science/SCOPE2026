# Exact two-defect stability at the critical quarter shift

## Finding
Fix an integer \(p\geq3\). For each \(s=(s_0,\ldots,s_{p-1})\in\{+1,-1\}^p\), define the normalized Fourier--Vandermonde matrix
\[
H_{p,s}=\left[p^{-1/2}\exp\!\left(-\frac{2\pi i j(r+s_r/4)}p\right)\right]_{0\leq j,r<p}.
\]
Assume exactly two signs are negative. Their cyclic separation is \(\ell\in\{1,\ldots,p-1\}\). Put \(g=\pi/(2p)\), \(\beta=\pi\ell/p\) and
\[
d=\frac1{p\sin g},\quad b=\frac1{p\sin(\beta-g)},\quad c=\frac1{p\sin(\beta+g)},\quad
\eta_{p,\ell}=\frac{\sqrt{4d^2+(b+c)^2}-|b-c|}{2}.
\]
Then the exact squared lower synthesis/Riesz bound is
\[
\boxed{\lambda_{\min}(H_{p,s}^*H_{p,s})=1-\sqrt{1-\eta_{p,\ell}^2}.}
\]
Among all such sign words, its minimum is attained **exactly when the two negative signs are cyclically adjacent** (\(\ell=1\) or \(p-1\)). With
\[
q_p=(3-4\sin^2 g)^{-1},\qquad
\eta_p=\frac{\sqrt{4+(1+q_p)^2}-(1-q_p)}{2p\sin g},
\]
the sharp two-defect lower bound at period \(p\) is \(a_p=1-\sqrt{1-\eta_p^2}\). It decreases strictly with \(p\), and
\[
\boxed{\inf_{p\ge3}a_p=1-\sqrt{1-\frac{4(\sqrt{13}-1)^2}{9\pi^2}}\;=0.166762438881\ldots>0.}
\]
Thus two displaced frequency classes cannot cause the complete critical collapse possible for sign patterns with a growing number of displaced classes.

## Assumptions and scope
The operator is the *auxiliary periodic shifted-sinc synthesis model*, represented exactly by \(H_{p,s}\). The sign \(+1\) means a quarter shift and \(-1\) means a negative quarter shift. There are precisely two minus classes modulo \(p\); all other classes have plus shifts. A global sign exchange would produce an equivalent formulation with two plus classes. This is a theorem about the optimal \(\ell^2\) synthesis lower bound and not a theorem about arbitrary nonperiodic binary patterns or about the distinct genuine two-index Gram model.

## Proof
**Fourier reduction.** Let \(u_j\) be the unit vector with entries \(p^{-1/2}e^{-2\pi i r(j+1/4)/p}\), indexed by \(r\). The \(p\) vectors \(u_j\) form an orthonormal basis. For the two minus indices \(j_0,j_1\), replace \(u_{j_k}\) by \(v_{j_k}\), whose entries are \(p^{-1/2}e^{-2\pi i r(j_k-1/4)/p}\). The two \(v\)'s are orthonormal as well. After a simultaneous cyclic relabeling, set \(j_0=0\), \(j_1=\ell\).

Write the two new vectors in the \(u\)-basis and split their coordinates into the \(p-2\) retained indices and the two removed indices. Denote the resulting blocks by \(L\) and \(K\), respectively. Orthonormality gives \(L^*L+K^*K=I_2\). The Gram matrix of all retained vectors together with the two new ones is
\[
\begin{pmatrix}I_{p-2}&L\\L^*&I_2\end{pmatrix}.
\]
Its smallest eigenvalue equals \(1-\|L\|=1-\sqrt{1-s_{\min}(K)^2}\), including the case \(p=3\), in which \(L\) has one row.

**A two-by-two Cauchy compression.** With
\[
D_m=\frac1p\sum_{r=0}^{p-1}e^{2\pi i(m-1/2)r/p},
\]
the matrix \(K\), up to complex conjugation dictated by the inner-product convention, has the form
\[
K=\begin{pmatrix}D_0&D_\ell\\ D_{-\ell}&D_0\end{pmatrix}.
\]
The finite geometric sum gives \(|D_m|=\bigl[p|\sin(\pi(m-1/2)/p)|\bigr]^{-1}\) and
\[
\frac{D_\ell D_{-\ell}}{D_0^2}=-\frac{\sin^2 g}{\sin(\beta-g)\sin(\beta+g)}<0.
\]
Consequently, left and right diagonal unitaries transform \(K\) into \(\bigl(\begin{smallmatrix}d&b\\-c&d\end{smallmatrix}\bigr)\). If the singular values of this real matrix are \(t_+\ge t_-\), then \(t_+t_-=d^2+bc\), \((t_++t_-)^2=4d^2+(b+c)^2\), and \(t_+-t_-=|b-c|\). Hence \(t_-=\eta_{p,\ell}\), proving the exact profile.

**Strict adjacent extremality.** Symmetry in \(\ell\) and \(p-\ell\) allows \(\beta\in[2g,\pi/2]\). Set \(y=\sin^2g\), \(v=y/(\sin^2\beta-y)\). Direct substitution yields
\[
\frac{\eta_{p,\ell}}d=F_y(v):=
\sqrt{1+(1-y)v(v+1)}-\sqrt{(1-y)v^2-yv}.
\]
Here \(0<y\le1/4\), \(v\ge y/(1-y)\), and \(v\) strictly decreases as \(\beta\) increases. At the left endpoint the second radical is zero. In its interior, both numerators in the derivative comparison are positive; squaring the proposed inequality \(F_y'(v)<0\) reduces it to positivity of
\[
(1-y)(3-2y)v^2-3y(1-y)v+y^2.
\]
Its leading coefficient is positive and its discriminant is \(-y^2(1-y)(3+y)<0\). Thus \(F_y'(v)<0\) everywhere in the interior. Since \(v\) decreases with \(\beta\), \(\eta_{p,\ell}\), and therefore the lower bound, strictly increase with the shorter cyclic separation. Exactly adjacent negative classes minimize the bound.

**Sharp uniform constant.** At adjacency \(\beta=2g\), one has \(b=d\) and \(c/d=\sin g/\sin3g=q_p\). This gives the stated expression for \(\eta_p\). Writing \(d=2g/(\pi\sin g)\), both \(d\) and \(q_p\) are strictly increasing functions of \(g\in(0,\pi/6]\), and \(\sqrt{4+(1+q)^2}-(1-q)\) is strictly increasing in \(q>0\). Since \(g=\pi/(2p)\) decreases with \(p\), \(\eta_p\), and therefore \(a_p\), strictly decrease with \(p\). The limits \(d\to2/\pi\), \(q_p\to1/3\) give \(\eta_p\to2(\sqrt{13}-1)/(3\pi)\), completing the proof.

## Verification
A standalone NumPy checker in `check.py` computes the smallest eigenvalue of the actual \(p\)-by-\(p\) Fourier matrix and compares it with the analytical two-by-two formula over all separations for \(3\le p\le25\), with additional samples through \(p=120\), as well as adjacent optimality and monotonicity tests. Its finite checks passed. These diagnostics are not used to infer any universal claim: the proof above covers all integral periods and separations.

## Relationship to prior work
Vellucci and Samad (arXiv:2610.31956v1, 22 October 2026) proved the constant-matrix reduction, gave the period-three formula, and conjectured that contiguous sign blocks are optimal under a prescribed sign count (Conjecture 7.4). The theorem above uses their matrix model and establishes the **exact two-minus-class case for all periods**, with its entire separation profile and its sharp, strictly positive uniform-in-period bound. Their general balanced-block conjecture and critical logarithmic-degeneration conjecture are not resolved. General work on Fourier/Vandermonde conditioning supplies background but not this exact profile in the inspected material.

## Limitations
The result treats only exactly two negative sign classes (or, after globally reversing signs, two positive classes); it does not classify three or more minority classes. It concerns the model defined here, not a nonperiodic pattern or an unrelated true two-index Gram perturbation. The proof and numerical diagnostics have not been independently validated. A statement equivalent under a different Fourier-frame convention may exist outside the literature inspected.

## References
1. P. Vellucci and G. S. Samad, *Perturbed Exponential Systems, Pattern-Dependent Shifted-Sinc Operators, and Matrix Symbols on Finite Unions of Intervals*, arXiv:2610.31956v1 (first public 2026-10-22), Sections 5--7, especially Theorem 6.1, Remark 6.8, and Conjecture 7.4. https://arxiv.org/html/2610.31956v1
2. V. Y. Pan, *How Bad Are Vandermonde Matrices?*, SIAM Journal on Matrix Analysis and Applications **37** (2016), 676--694; arXiv:1504.02118. https://arxiv.org/abs/1504.02118
3. D. Batenkov, L. Demanet, G. Goldman and Y. Yomdin, *Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes*, SIAM Journal on Matrix Analysis and Applications **41** (2020), 199--220. https://doi.org/10.1137/18M1212197
