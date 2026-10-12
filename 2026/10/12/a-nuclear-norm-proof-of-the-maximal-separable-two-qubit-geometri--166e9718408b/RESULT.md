# A nuclear-norm proof of the maximal separable two-qubit geometric discord
## Finding
For every separable two-qubit state \(\rho\), write its Bloch representation as
\[
\rho=\frac14\left(I\otimes I+x^T\sigma\otimes I+I\otimes y^T\sigma+\sum_{i,j=1}^3T_{ij}\sigma_i\otimes\sigma_j\right).
\]
Use the normalized Hilbert--Schmidt geometric discord convention of Gharibian and Rana--Parashar,
\[
\mathcal D(\rho)=\frac12\left(\|x\|_2^2+\|T\|_F^2-\lambda_{\max}(xx^T+TT^T)\right).
\]
Then
\[
\boxed{\mathcal D(\rho)\le\frac14}.
\]
Equality holds if and only if \(\rho\) is locally-unitarily equivalent to
\[
\sigma=\frac12|00\rangle\langle00|+\frac12|+1\rangle\langle+1|,
\qquad |+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2}.
\]
Consequently every maximally non-classical separable two-qubit state has rank two. This proves the conjecture stated by Gharibian and restated by Rana--Parashar that no separable state of rank greater than two can attain normalized geometric discord \(1/4\).

## Assumptions and scope
The statement concerns two qubits, separability across the two-qubit bipartition, and the squared Hilbert--Schmidt geometric discord normalized so that the two-qubit closed formula carries the prefactor \(1/2\). The measurement is on the first qubit, exactly as in the displayed Bloch formula. Local unitaries preserve separability, rank, and this discord, so the equality classification is naturally stated up to local-unitary equivalence.

No claim is made that Hilbert--Schmidt geometric discord is monotone under arbitrary local channels on the unmeasured subsystem. The theorem is an exact optimization statement on the separable state set.

## Proof
A finite-dimensional separable state admits a finite pure-product decomposition
\[
\rho=\sum_k p_k\,\rho(a_k)\otimes\rho(b_k),
\qquad p_k>0,\quad\sum_kp_k=1,
\]
where \(a_k,b_k\in\mathbb R^3\) are unit Bloch vectors. Therefore
\[
x=\sum_kp_ka_k,
\qquad
T=\sum_kp_ka_kb_k^T.
\]
Form the \(3\times4\) real matrix
\[
M=[x\;T].
\]
For \(c_k=(1,b_k^T)^T\in\mathbb R^4\),
\[
M=\sum_kp_k a_kc_k^T,
\qquad \|a_k\|_2=1,
\qquad \|c_k\|_2=\sqrt2.
\]
The nuclear norm is convex and a rank-one matrix has nuclear norm equal to the product of the Euclidean norms of its factors. Hence every separable state satisfies the sharp inequality
\[
\boxed{\|M\|_*\le\sqrt2}.
\]

Let \(s_1\ge s_2\ge s_3\ge0\) be the singular values of \(M\). Since
\[
MM^T=xx^T+TT^T,
\]
the discord formula becomes
\[
\mathcal D(\rho)=\frac12(s_2^2+s_3^2).
\]
The nuclear-norm bound gives \(s_1+s_2+s_3\le\sqrt2\). Because \(s_1\ge s_2\),
\[
2s_2+s_3\le\sqrt2.
\]
Also \(s_2\ge s_3\), so \(0\le s_3\le\sqrt2/3\). Therefore
\[
s_2^2+s_3^2
\le
\left(\frac{\sqrt2-s_3}{2}\right)^2+s_3^2.
\]
Writing \(s_3=\sqrt2\,w\) with \(0\le w\le1/3\), the right side is
\[
\frac12-w+\frac52w^2\le\frac12,
\]
because its difference from \(1/2\) is \(w(5w/2-1)\le0\) on this interval. Thus \(\mathcal D(\rho)\le1/4\).

Suppose equality holds. The preceding one-variable inequality and the singular-value ordering force
\[
s_3=0,
\qquad
s_1=s_2=\frac1{\sqrt2},
\qquad
\|M\|_*=\sqrt2.
\]
Let \(Q\) be the rank-two polar partial isometry of \(M\), so \(\|Q\|_{\mathrm{op}}=1\), its two-dimensional initial space is a subspace \(S\subset\mathbb R^4\), and
\[
\operatorname{tr}(Q^TM)=\|M\|_*=\sqrt2.
\]
Using the product decomposition,
\[
\sqrt2
=
\sum_kp_k\,a_k^TQc_k
\le
\sum_kp_k\|a_k\|_2\|Qc_k\|_2
\le
\sum_kp_k\|c_k\|_2
=
\sqrt2.
\]
Every term with positive weight must therefore saturate both inequalities. In particular \(\|Qc_k\|_2=\|c_k\|_2\), which for a partial isometry means \(c_k\in S\), and positive Cauchy equality gives \(Qc_k=\sqrt2\,a_k\).

Every such \(c_k\) also satisfies \((c_k)_0=1\) and \(\|c_k\|_2=\sqrt2\). Since \(S\) is two-dimensional, the set
\[
S\cap\{c_0=1}\}
\]
is an affine line. Its intersection with the sphere \(\|c\|_2=\sqrt2\) contains at most two points. For each allowed \(c_k\), the equation \(a_k=Qc_k/\sqrt2\) fixes the first-qubit pure state. Hence the separable decomposition uses at most two distinct pure product projectors, so \(\operatorname{rank}\rho\le2\).

Gharibian's rank-at-most-two classification then applies: a rank-two separable two-qubit state reaches normalized geometric discord \(1/4\) exactly on the local-unitary orbit of \(\sigma\) displayed above. Conversely that state has
\[
M=\begin{pmatrix}
1/2&0&0&-1/2\\
0&0&0&0\\
1/2&0&0&1/2
\end{pmatrix},
\]
whose singular values are \(1/\sqrt2,1/\sqrt2,0\), so it indeed has \(\mathcal D=1/4\).

## Verification
The infinite bound is proved analytically above; no finite sample is used as a substitute. The accompanying `verify.py` checks with exact rational arithmetic that the displayed extremizer has Gram matrix eigenvalues \(1/2,1/2,0\), that its discord is \(1/4\), and that the scalar reduction of the singular-value optimization has no second equality point on \(0\le w\le1/3\). It also checks the endpoint \(w=1/3\), where the upper expression is \(4/9<1/2\).

The nonstandard equality step is the polar-witness argument: equality in the nuclear-norm triangle bound forces all augmented Bloch vectors \(c_k=(1,b_k)\) into one two-dimensional initial space. The fixed first coordinate converts that plane into an affine line, and the fixed norm converts it into at most two product states. This is the step that upgrades the numerical value bound to the rank/equality classification.

## Relationship to prior work
Gharibian's 2012 paper characterizes maximally non-classical separable two-qubit states of rank at most two and explicitly conjectures that higher-rank separable states cannot attain the same value. Rana and Parashar restate the conjecture, formulate it as maximizing the two smaller eigenvalues of \(G=xx^T+TT^T\), prove it for separable \(X\)-states, and report only partial progress for general states. Their paper also records the standard necessary separability bound \(\|T\|_*\le1\), which by itself does not control the contribution of \(x\).

The present proof instead uses the augmented one-sided matrix \(M=[x\;T]\) and the direct separable decomposition to obtain \(\|M\|_*\le\sqrt2\). This single inequality yields the global discord bound and, through its equality conditions, forces rank at most two.

Later extended-correlation-matrix separability criteria bound trace norms of larger matrices containing both local Bloch vectors and \(T\). They provide related separability tests, but the inspected theorem does not state the sharp \(\|[x\;T]\|_*\le\sqrt2\) optimization, the \(1/4\) geometric-discord maximum, or the equality-rank argument. A 2021 correlation-minor paper uses the phrase “two-qubit separable state with maximal discord” in connection with standard discord literature; its cited sources there concern a different discord optimization and do not supply the Gharibian geometric-discord theorem proved here.

## Limitations
The result is specific to the normalized squared Hilbert--Schmidt geometric discord for two qubits. It does not extend automatically to entropic discord, trace-distance discord, Bures geometric discord, higher local dimensions, or arbitrary resource monotones. The bibliographic searches and full-text comparisons found no covering analytic proof, but differently phrased or poorly indexed later work remains a residual originality risk.

## References
1. S. Gharibian, “Quantifying non-classicality with local unitary operations,” arXiv:1202.1598; Phys. Rev. A 86, 042106 (2012), DOI 10.1103/PhysRevA.86.042106.
2. S. Rana and P. Parashar, “Maximally discordant separable two qubit \(X\) states,” arXiv:1311.1671; Quantum Information Processing 13, 2815–2822 (2014), DOI 10.1007/s11128-014-0865-0.
3. S.-Q. Shen, M. Li, X.-F. Duan, and S.-M. Fei, “Improved separability criteria based on Bloch representation of density matrices,” arXiv:1608.01547; Scientific Reports 6, 28850 (2016).
4. “Correlation minor norms, entanglement detection and discord,” Scientific Reports 11, 2849 (2021), DOI 10.1038/s41598-021-82303-3.
