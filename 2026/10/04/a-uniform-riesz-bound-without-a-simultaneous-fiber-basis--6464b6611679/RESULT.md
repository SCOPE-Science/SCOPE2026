# A uniform Riesz bound without a simultaneous fiber basis
## Finding
Let \(p\ge 3\) be an odd prime, let \(H=\mathbb F_2^2\), and put \(G_p=H\times\mathbb Z_p\). Define
\[
F_1=\{(0,0),(0,1)\},\qquad F_2=\{(0,0),(1,0)\},\qquad F_3=\{(0,0),(1,1)\},
\]
and
\[
E_p=(F_1\times\{0\})\cup(F_2\times\{1\})\cup(F_3\times\{2,3,\ldots,p-1\}).
\]
The three fibers \(F_1,F_2,F_3\) have no simultaneous exponential basis in \(\widehat H\), but nevertheless
\[
\rho(E_p)<251
\]
for every odd prime \(p\ge3\).

Write \(e_1=(1,0)\), \(e_2=(0,1)\), let \(\omega=e^{2\pi i/p}\), and set
\[
S=\{0,1,\ldots,(p-1)/2\},\qquad T=\mathbb Z_p\setminus S.
\]
An explicit frequency set of cardinality \(2p\) is
\[
B_p=\{(0,t):t\in\mathbb Z_p\}\cup\{(e_1,t):t\in S\}\cup\{(e_2,t):t\in T\}.
\]
The Fourier matrix for \((E_p,B_p)\) is invertible and has squared condition number less than \(251\).

## Assumptions and scope
Characters of \(H\) are identified with \(H\) by \(\chi_\xi(x)=(-1)^{\xi\cdot x}\), and characters of \(\mathbb Z_p\) are \(z\mapsto\omega^{tz}\). The Riesz ratio \(\rho(E_p,B_p)\) is the squared spectral condition number of the corresponding Fourier evaluation matrix, and \(\rho(E_p)\) is the infimum over all exponential bases. The claim concerns exactly the family above; it does not assert that the numerical constant \(251\) is sharp.

## Proof
Order the two points in each fiber by writing the row block at height \(z\) as \(\{0,x_z\}\), where \(x_0=e_2\), \(x_1=e_1\), and \(x_z=e_1+e_2\) for \(2\le z\le p-1\). Apply the normalized two-point Hadamard transform to every row block. This is unitary, so it does not change singular values.

For a column indexed by \((0,t)\), the transformed column lies entirely in the plus channel and equals \(\sqrt2\,\omega^{tz}\) at every height \(z\). For the second column at frequency \(t\), use \(e_1\) when \(t\in S\) and \(e_2\) when \(t\in T\). If \(t\in S\), then \(e_1\cdot x_0=0\) and \(e_1\cdot x_z=1\) for every \(z\ne0\), so that column lies in the plus channel only at \(z=0\) and in the minus channel elsewhere. If \(t\in T\), then \(e_2\cdot x_1=0\) and \(e_2\cdot x_z=1\) for every \(z\ne1\), so that column lies in the plus channel only at \(z=1\) and in the minus channel elsewhere.

After the common scaling by \((2p)^{-1/2}\), let \(\mathcal F\) be the unitary \(p\)-point Fourier matrix. For coefficient vectors \(a,b\in\mathbb C^p\), the transformed synthesis operator is
\[
(a,b)\longmapsto\bigl(\mathcal F a+Pb,\;\mathcal F b-Pb\bigr),
\]
where
\[
Pb=e_0\frac1{\sqrt p}\sum_{t\in S}b_t+e_1\frac1{\sqrt p}\sum_{t\in T}\omega^t b_t.
\]
The two defining functionals of \(P\) have disjoint frequency supports, hence are orthogonal, and therefore
\[
\|P\|^2=\max\left\{\frac{|S|}{p},\frac{|T|}{p}\right\}=\frac{p+1}{2p}\le\frac23.
\]
Left multiplication by \(\operatorname{diag}(\mathcal F^*,\mathcal F^*)\) is unitary. With \(K=\mathcal F^*P\), the matrix is therefore unitarily equivalent to
\[
\mathcal T=\begin{pmatrix}I&K\\0&I-K\end{pmatrix},
\qquad \|K\|=q\le\sqrt{\frac23}<1.
\]
Thus \(I-K\) is invertible. Put \(r=(1-q)^{-1}\). Using the matrix of block norms gives
\[
\|\mathcal T\|^2\le 1+q^2+(1+q)^2=2(1+q+q^2),
\]
and, since
\[
\mathcal T^{-1}=\begin{pmatrix}I&-K(I-K)^{-1}\\0&(I-K)^{-1}\end{pmatrix},
\]
we have
\[
\|\mathcal T^{-1}\|^2\le 1+q^2r^2+r^2
=1+\frac{1+q^2}{(1-q)^2}.
\]
Both right-hand sides increase with \(q\in[0,1)\). At \(q=\sqrt{2/3}\), their product is
\[
\frac{380+152\sqrt6}{3}<251.
\]
The final strict inequality follows from \(152\sqrt6<373\), equivalently \(6\cdot152^2<373^2\). Therefore \(\rho(E_p,B_p)<251\), and hence \(\rho(E_p)<251\) for every odd prime \(p\ge3\).

## Verification
The accompanying checker verifies the fiber channel assignments, the exact cardinality bound \(3|S|\le2p\), the disjoint-support computation of \(\|P\|^2\), and the integer inequality \(6\cdot152^2<373^2\) for representative odd primes. These checks replay the finite combinatorial and arithmetic parts of the proof; the uniform theorem follows from the analytic operator estimate above.

## Relationship to prior work
Ferguson, Mayeli, and Sothanaphan introduce this exact family as an example where the translated fibers do not admit a simultaneous basis. Their full text states that their main theorem therefore does not apply and that they do not know whether the condition number of this family is bounded independently of \(p\). The construction above answers that question positively, with an explicit uniform bound, and shows that the simultaneous-fiber-basis hypothesis is not necessary in general for bounded Riesz behavior.

Targeted searches for the exact family, the simultaneous-basis hypothesis, and bounded Riesz ratios located no later statement covering this conclusion. The closest retrieved records concern unrelated Riesz-basis or finite Fourier questions and do not imply a uniform bound for this family.

## Limitations
The constant \(251\) is an explicit proof bound, not an optimized value. The argument is tailored to the three-fiber family in \(\mathbb F_2^2\times\mathbb Z_p\); it does not remove the simultaneous-basis hypothesis from the general multi-tiling theorem. Search-based originality assessment cannot exclude unindexed or differently phrased later work.

## References
1. S. Ferguson, A. Mayeli, and N. Sothanaphan, “Riesz bases of exponentials and multi-tiling in finite abelian groups,” arXiv:1904.04487, first public version 2019-04-09. The current full text contains the simultaneous-basis discussion, the main finite multi-tiling theorem, and the unresolved family used here.
