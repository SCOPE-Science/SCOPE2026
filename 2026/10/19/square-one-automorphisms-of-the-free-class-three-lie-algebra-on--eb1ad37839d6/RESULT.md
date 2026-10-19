# Square-one automorphisms of the free class-three Lie algebra on two generators

## Finding
Let \(q\) be any prime power and let \(L\) be the five-dimensional free nilpotent Lie algebra of rank two and class three over \(\mathbb F_q\). Then the number of automorphisms \(\varphi\in\operatorname{Aut}_{\mathbb F_q}(L)\) satisfying \(\varphi^2=\mathrm{id}_L\), **including the identity**, is
\[
I_L(q)=\begin{cases}
q^5+q^4-q^3,&\operatorname{char}(\mathbb F_q)=2,\\
q^5+q^4+q^2+1,&\operatorname{char}(\mathbb F_q)\ne2.
\end{cases}
\]
Thus the number of automorphisms of exact order two is \(I_L(q)-1\). The formula is valid without algebraic-closure assumptions, including nonprime finite fields.

## Assumptions and scope
Use the basis \((x,y,z,u,v)\) with \([x,y]=z\), \([x,z]=u\), \([y,z]=v\), and all brackets involving \(u\) or \(v\) zero. These relations define the free two-generator class-three nilpotent Lie algebra in every characteristic; the bracket is alternating also in characteristic two.

Every automorphism is uniquely specified by
\[
\begin{aligned}
\varphi(x)&=ax+by+cz+du+ev,\\
\varphi(y)&=fx+gy+hz+iu+jv,
\end{aligned}
\]
where \(A=\left(\begin{smallmatrix}a&f\\b&g\end{smallmatrix}\right)\in\mathrm{GL}_2(\mathbb F_q)\) and the other six parameters are arbitrary. Indeed, the induced matrix is lower triangular by the lower-central-series grading and has determinant \((\det A)^5\). Consequently \(|\operatorname{Aut}(L)|=|\mathrm{GL}_2(\mathbb F_q)|q^6\).

## Proof
Put \(\delta=\det A\), \(C=(c,h)\), \(D=\left(\begin{smallmatrix}d&i\\e&j\end{smallmatrix}\right)\), \(B=\delta A\), and \(E=(ah-cf,bh-cg)^{\mathsf T}\). Direct expansion of the Lie brackets gives the block matrix, in dimensions \(2,1,2\),
\[
T_\varphi=\begin{pmatrix}A&0&0\\C&\delta&0\\D&E&B\end{pmatrix}.
\]
It follows that \(T_\varphi^2=I\) requires
\[
A^2=I_2,\quad C(A+\delta I_2)=0,\quad DA+BD+EC=0,
\]
together with \(\delta^2=1\), \(B^2=I_2\), and \((B+\delta I_2)E=0\). The latter three conditions follow from the first two. In particular, write \(J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\); then \(E=AJC^{\mathsf T}\). Since \(AJA^{\mathsf T}=\delta J\) and \(CA=-\delta C\), one obtains \(E=-JC^{\mathsf T}\) and \(AE=-E\), establishing the last condition.

Suppose first that the characteristic is odd. The matrices \(A\in\mathrm{GL}_2(\mathbb F_q)\) satisfying \(A^2=I_2\) are \(I_2\), \(-I_2\), and the \(q(q+1)\) matrices whose \(+1\) and \(-1\) eigenspaces are distinct ordered projective lines. For \(A=I_2\), the equations force \(C=0\) and \(D=0\), giving one lift. For \(A=-I_2\), every \(C\) is allowed and \(D=EC/2\) is determined, giving \(q^2\) lifts. For any split reflection, conjugate to \(A=\operatorname{diag}(1,-1)\), the equation for \(C\) forces \(C=(c,0)\). Then \(E=(0,c)^{\mathsf T}\), and the equation for \(D=\left(\begin{smallmatrix}d&i\\e&j\end{smallmatrix}\right)\) forces \(i=0\), \(e=-c^2/2\), while \(d,j\) are free. There are \(q^3\) lifts per reflection. Hence
\[
I_L(q)=1+q^2+q(q+1)q^3=q^5+q^4+q^2+1.
\]

In characteristic two, \(\delta=1\) for every square-one \(A\). Such \(A\) are either \(I_2\) or \(I_2+N\), with \(N\ne0\) rank-one nilpotent; there are \(q^2-1\) nonzero choices of \(N\). For \(A=I_2\), the square-one condition reduces to \(EC=0\), forcing \(C=0\), and \(D\) is arbitrary: \(q^4\) lifts. For any nonidentity \(A\), conjugate it to \(\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)\). The equation for \(C\) makes \(C=(0,h)\), and \(E=(h,0)^{\mathsf T}\). Writing \(D=\left(\begin{smallmatrix}d&i\\e&j\end{smallmatrix}\right)\), its remaining equation becomes
\[
\begin{pmatrix}e&d+j\\0&e\end{pmatrix}
=\begin{pmatrix}0&h^2\\0&0\end{pmatrix}.
\]
Thus \(e=0\), \(j=d+h^2\), and \(d,i,h\) are arbitrary: \(q^3\) lifts per nonidentity \(A\). We conclude
\[
I_L(q)=q^4+(q^2-1)q^3=q^5+q^4-q^3.
\]
This proves the assertion for all finite fields.

## Verification
The self-contained script `square_one_check.py` constructs the automorphisms directly from the images of the two free generators and tests equality of the full \(5\times5\) square with the identity. Exhaustive checks give \(I_L(2)=40\), \(I_L(3)=334\), and \(I_L(4)=1216\). The last check uses \(\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\). Every possible linear block \(A\) with \(A^2=I_2\) and every six-parameter lift were examined; restricting to such \(A\) is exhaustive because it is a necessary condition for \(T_\varphi^2=I\). These computations corroborate, but do not replace, the preceding arbitrary-field proof.

## Relationship to prior work
Drensky and Fındık (2010) describe inner and outer automorphisms of free metabelian nilpotent Lie algebras in characteristic zero; rank-two class-three free nilpotent Lie algebras are metabelian. Benito and de-la-Concepción (2013) study the five-dimensional free class-three algebra and its extensions over \(\mathbb C\). Benito and Roldán-López (2019) give a general automorphism parametrization of free nilpotent Lie algebras. These papers supply the structural context, but the inspected sections do not give the finite-field square-one census or its characteristic-two branch. The theorem above counts individual elements, not conjugacy classes, in this fixed natural algebra.

## Limitations
No claim is made about conjugacy classification, fields that are not finite, or general rank and class. The combinatorial census has undergone internal proof checking and finite-field enumeration, but not independent mathematical audit. A specialized automorphism-group or algebraic-group reference not recovered in the literature comparison might imply the counting formula.

## References
1. V. Drensky and Ş. Fındık, *Inner and Outer Automorphisms of Free Metabelian Nilpotent Lie algebras*, arXiv:1003.0350v1 (first public version 2010-03-01), https://arxiv.org/abs/1003.0350.
2. P. Benito and D. de-la-Concepción, *A note on extensions of nilpotent Lie algebras of Type 2*, arXiv:1307.8419v1 (first public version 2013-07-31), https://arxiv.org/abs/1307.8419.
3. P. Benito and J. Roldán-López, *Derivations and automorphisms of free nilpotent Lie algebras and their quotiens*, arXiv:1911.01897v2 (first public version 2019-11-05), https://arxiv.org/abs/1911.01897.
