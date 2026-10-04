# Distinct-vector FUNTFs of every length \(n+1,\ldots,2n\) in real \(\ell_1^n\)

## Finding
For every integer \(n\ge 2\) and every integer \(k\) with \(1\le k\le n\), real \(\ell_1^n\) admits a finite unit-norm tight frame (FUNTF) of length \(N=n+k\) whose primal frame vectors are pairwise distinct. Thus every length from \(n+1\) through \(2n\) occurs without repetition of primal frame vectors. In particular, taking \(n=5\) and \(k=2\) gives a length-seven FUNTF in real \(\ell_1^5\), answering Cheng and Heil's Question 2.13 affirmatively.

## Assumptions and scope
A Banach-space FUNTF is a finite sequence of pairs \((x_j,f_j)\in X\times X^*\) satisfying \(\|x_j\|=\|f_j\|=f_j(x_j)=1\) for every \(j\), with frame operator
\[
Sx=\sum_j f_j(x)x_j
\]
equal to a positive scalar multiple of the identity. Here \(X=\ell_1^n\) over the reals and \(X^*=\ell_\infty^n\). The no-repetition assertion is for the primal vectors \(x_j\); consequently the sequence pairs are also pairwise distinct. No claim is made that the norming functionals themselves are pairwise distinct.

## Proof
Let \(e_1,\ldots,e_n\) be the standard basis. We first construct a positive \(k\times n\) matrix \(A=(a_{rj})\) whose row sums equal \(1\), whose column sums equal \(k/n\), and whose rows are pairwise distinct when \(k\ge2\).

For \(k=1\), set \(a_{1j}=1/n\). For \(k\ge2\), define
\[
u_r=r-\frac{k+1}{2},\qquad v_j=j-\frac{n+1}{2},
\]
\[
U=\frac{k-1}{2},\qquad V=\frac{n-1}{2},\qquad
\varepsilon=\frac{1}{4nUV},
\]
and
\[
a_{rj}=\frac1n+\varepsilon u_rv_j.
\]
Because \(|u_r|\le U\) and \(|v_j|\le V\), every entry obeys
\[
a_{rj}\ge \frac1n-\frac1{4n}=\frac{3}{4n}>0.
\]
Also \(\sum_j v_j=0\) and \(\sum_r u_r=0\), so every row sums to \(1\) and every column sums to \(k/n\). Since the \(u_r\) are distinct and \((v_j)_j\) is not the zero vector, the rows of \(A\) are distinct.

Define the primal vectors by
\[
x_j=e_j\quad(1\le j\le n),\qquad
x_{n+r}=(a_{r1},\ldots,a_{rn})\quad(1\le r\le k).
\]
Every vector has \(\ell_1\)-norm one. The added vectors have all coordinates positive, so none equals a standard basis vector, and their distinct rows make them pairwise distinct.

For \(1\le j\le n\), define \(f_j\in\ell_\infty^n\) by
\[
f_j(e_j)=1,\qquad f_j(e_m)=-\frac{k}{n}\quad(m\ne j).
\]
Since \(k\le n\), \(\|f_j\|_\infty=1\), and \(f_j(x_j)=1\). For each \(1\le r\le k\), let \(f_{n+r}\) be the all-ones functional. Positivity and unit row sum give \(\|f_{n+r}\|_\infty=1\) and \(f_{n+r}(x_{n+r})=1\).

Let \(J\) be the all-ones \(n\times n\) matrix. The contribution of the first \(n\) pairs to the frame operator is
\[
\sum_{j=1}^n e_j f_j^{\mathsf T}
=\left(1+\frac{k}{n}\right)I-\frac{k}{n}J.
\]
The contribution of the final \(k\) pairs is
\[
\sum_{r=1}^k x_{n+r}\mathbf 1^{\mathsf T}
=\frac{k}{n}J,
\]
because each column of \(A\) sums to \(k/n\). Therefore
\[
S=\left(1+\frac{k}{n}\right)I=\frac{n+k}{n}I.
\]
This is exactly the FUNTF condition.

For the specific open case \(n=5\), \(k=2\), one may take
\[
x_6=\left(\frac1{10},\frac3{20},\frac15,\frac14,\frac3{10}\right),\qquad
x_7=\left(\frac3{10},\frac14,\frac15,\frac3{20},\frac1{10}\right),
\]
with \(x_1,\ldots,x_5=e_1,\ldots,e_5\), with each \(f_j\) for \(j\le5\) equal to \(1\) on coordinate \(j\) and \(-2/5\) on the other coordinates, and with \(f_6=f_7=(1,1,1,1,1)\). The frame operator is \((7/5)I\), and all seven primal vectors are distinct.

## Verification
The proof is symbolic and valid for all stated \(n\) and \(k\); it does not rely on finite computation. The accompanying exact-arithmetic checker independently verifies the displayed \((n,k)=(5,2)\) example and the general formula for all \(2\le n\le12\) and \(1\le k\le n\). These finite checks are consistency tests only, not substitutes for the proof.

## Relationship to prior work
Cheng and Heil prove existence of FUNTFs of every length \(N\ge n\) in real \(\ell_1^n\), allowing repeated elements, and construct no-repetition families of lengths \(2n-2\) and \(2n-1\). They explicitly state that they had not constructed a length-seven FUNTF in real \(\ell_1^5\) without repeated elements and pose this as Question 2.13. The present construction supplies that missing case and, more generally, every length \(n+k\) with \(1\le k\le n\).

The earlier work of Chávez-Domínguez, Freeman, and Kornelson introduced the Banach-space frame-potential framework and established broad FUNTF existence results, including real \(\ell_1^n\) constructions in several cases. Their results do not imply the pairwise-distinct-vector family proved here. The construction above uses the freedom in norming functionals off their normed vector together with a positive transportation matrix having prescribed margins.

## Limitations
The theorem is specific to real \(\ell_1^n\) and only asserts pairwise distinctness of the primal vectors, not of the norming functionals. It gives no classification or uniqueness result, and it does not address arbitrary real Banach spaces. The literature comparison cannot rule out an obscure or unindexed equivalent construction; the principal checked sources do not contain this statement.

## References
1. Y.-S. Cheng and C. Heil, “Existence of finite unit-norm tight frames in Banach spaces,” Graduate Journal of Mathematics 7 (2022), 17–38. Public page: https://gradmath.org/2022/09/10/existence-of-finite-unit-norm-tight-frames-in-banach-spaces/
2. J. A. Chávez-Domínguez, D. Freeman, and K. Kornelson, “Frame potential for finite-dimensional Banach spaces,” Linear Algebra and its Applications 578 (2019), 1–26; arXiv:1804.03677.
