# Complete equality classification for the third inverse Hankel determinant of starlike functions

## Finding
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), and let \(\mathcal S^*\) consist of functions \(f(z)=z+\sum_{n\ge2}a_nz^n\) analytic in \(\mathbb D\) with \(\operatorname{Re}(zf'(z)/f(z))>0\). The inverse series at the origin is \(f^{-1}(w)=w+\sum_{n\ge2}A_nw^n\). Define
\[
\mathcal H(f)=\det\begin{pmatrix}1&A_2&A_3\\A_2&A_3&A_4\\A_3&A_4&A_5\end{pmatrix}.
\]
The sharp inequality \(|\mathcal H(f)|\le1\) for this class is due to Allu and Kumar [1]. **The complete equality statement is**
\[
|\mathcal H(f)|=1\quad\Longleftrightarrow\quad
f(z)=\frac{z}{(1-\xi z)(1-\eta z)}\quad\text{for some}\quad|\xi|=|\eta|=1.
\]
For each such extremizer, \(\mathcal H(f)=(\xi\eta)^3\). In particular, the Koebe extremizers \(\xi=\eta\) are only one boundary stratum of a continuous family; the distinct-pole extremizers are genuine additional cases. After rotation and interchange, the family retains a real separation parameter.

## Assumptions and scope
The condition defining \(\mathcal S^*\) includes normalization \(f(0)=0\), \(f'(0)=1\). The inverse is its local holomorphic inverse near zero, not a global inverse on the whole image. The determinant uses precisely the first five inverse coefficients, with \(A_1=1\). The two boundary parameters need not be distinct. No external assertion of independent review is made.

## Proof
**Step 1: all stated maps really are equality cases.** Set \(a=\xi+\eta\), \(b=\xi\eta\). Then \(f(z)=z/(1-az+bz^2)\) and
\[
\frac{zf'(z)}{f(z)}=1+\frac{\xi z}{1-\xi z}+\frac{\eta z}{1-\eta z}.
\]
Each of the last two summands has real part strictly greater than \(-1/2\) on \(\mathbb D\), so \(f\in\mathcal S^*\). Direct inversion, or coefficient comparison in \(w(1-az+bz^2)=z\), gives
\[
A_2=-a,\qquad A_3=a^2+b,\qquad A_4=-(a^3+3ab),\qquad A_5=a^4+6a^2b+2b^2.
\]
Expansion of the displayed determinant simplifies **identically** to \(b^3\). Since \(|b|=1\), equality holds.

**Step 2: reduce any equality case to the boundary of the Carathéodory coefficient body.** Write \(P(z)=zf'(z)/f(z)=1+c_1z+c_2z^2+c_3z^3+c_4z^4+\cdots\). Rotational invariance allows \(c_1=p\in[0,2]\). The standard Libera--Złotkiewicz--Kwon parametrization supplies \(\gamma,\eta_0,\rho\in\overline{\mathbb D}\) for these coefficients. Allu and Kumar [1, proof of Theorem 2.1] derive the **exact upper envelope**
\[
1152|\mathcal H(f)|\le \mathscr E(p,x,y)
=1152-(4-p^2)(1-x)\Phi(p,x,y),
\]
with \(x=|\gamma|\), \(y=|\eta_0|\) and the explicit trivariate polynomial \(\Phi\) of [1, equation (2.6)]. Their displayed Bernstein matrices express \(\Phi(2u,x,y)\) in bidegrees \((4,3,2)\), with **all 60 Bernstein coefficients nonnegative**. The 12 coefficients in the \(u\)-index-zero row are all strictly positive (the minimum is \(160\)). Consequently \(\Phi(p,x,y)>0\) whenever \(0\le p<2\), for every \(0\le x,y\le1\): the \(u\)-index-zero Bernstein basis factor \((1-p/2)^4\) is strictly positive and the remaining Bernstein basis functions sum to one. Thus equality in the sharp bound forces either \(p=2\) or \(|\gamma|=1\). The latter case is the boundary of the second Carathéodory coefficient disk and eliminates the remaining Schur parameters.

**Step 3: classify which unimodular \(\gamma\) really attain equality.** When \(|\gamma|=1\), substitution of the Carathéodory coefficient formulas from [1, Lemma 1.1] into the determinant gives \(\mathcal H(f)=D(p,\gamma)\), where
\[
\begin{aligned}
1152D(p,\gamma)={}&18p^6+51\gamma(p^6-4p^4)
+\gamma^2p^2(688-368p^2+49p^4)\\
&+\gamma^3(-1152+704p^2-172p^4+17p^6)
+\gamma^4p^2(4-p^2)^2.
\end{aligned}
\]
Put \(t=p^2/4\in[0,1]\), \(v=(1+\operatorname{Re}\gamma)/2\in[0,1]\). An **exact Laurent-polynomial identity**, using \(\overline\gamma=\gamma^{-1}\), is
\[
1-|D(p,\gamma)|^2=\frac{t(1-t)v}{20736}Q(t,v),
\]
where, writing \(q=4t\), \(x=2v-1\),
\[
\begin{aligned}
Q(t,v)=4\big[&36q^4x^3+321q^4x^2+542q^4x+257q^4\\
&-144q^3x^3-2136q^3x^2-3936q^3x-1944q^3\\
&+6000q^2x^2+13032q^2x+7608q^2\\
&-30752qx-14624q+50688\big].
\end{aligned}
\]
Although expressed with \(q,x\) for readability, this is a polynomial of bidegree \((4,3)\) in \((t,v)\). Here is an **exact positivity certificate**: in the tensor-product Bernstein basis of bidegree \((4,3)\) on \([0,1/2]\times[0,1]\), all 20 coefficients are strictly positive and the smallest is \(78336\). On \([1/2,1]\times[0,1]\), all 20 are strictly positive and the smallest is \(78848\). The self-contained `verify_inverse_hankel.py` computes those rational coefficients from the displayed polynomial, and verifies this factorization coefficientwise. It follows that, for \(|\gamma|=1\), equality is possible **only when** \(p=0\), \(p=2\), or \(\gamma=-1\).

**Step 4: recover the analytic maps; no equality cases remain.** If \(p=2\), the equality case of the Carathéodory coefficient bound gives \(P(z)=(1+z)/(1-z)\), hence \(f(z)=z/(1-z)^2\). If \(0<p<2\) and \(\gamma=-1\), equality in the second Carathéodory coefficient disk yields the exact Schur function
\[
P(z)=\frac{1-z^2}{1-pz+z^2},\qquad
f(z)=\frac{z}{1-pz+z^2}.
\]
The two reciprocal factors have parameters on the unit circle because \(0\le p\le2\). If \(p=0\) and \(|\gamma|=1\), the analogous Schur boundary condition gives
\[
P(z)=\frac{1+\gamma z^2}{1-\gamma z^2},\qquad
f(z)=\frac{z}{1-\gamma z^2}.
\]
These are also two-pole maps, with opposite pole parameters. Restoring arbitrary rotations of \(f\) yields precisely the family in the statement. Conversely, Step 1 showed every member works. This completes both directions.

## Verification
Run `python3 verify_inverse_hankel.py` with Python 3; it uses only the standard library, with exact rational arithmetic (no floating point). It recomputes all 60 source-envelope Bernstein entries, checks the strict first row, establishes the full Laurent-coefficient identity, constructs the 40 positive Bernstein coefficients on two rectangles, verifies boundary identities, and expands the inverse determinant to \(b^3\). The minimal coefficients obtained are \(0\) overall for the source envelope, \(160\) on its index-zero row, and \(78336\), \(78848\) for the two positive defect certificates. These are exact finite algebraic certificates for the specified polynomial identities, not numerical sampling of an infinite class.

## Relationship to prior work
Allu and Kumar [1] prove the sharp inequality \(|\mathcal H(f)|\le1\), and explicitly exhibit the Koebe function; their estimate is a premise, not claimed anew. The classification above extracts equality rigidity from their published upper envelope and adds a **new strict phase-defect factorization** needed to exclude the other unimodular Schur parameters. Rath and collaborators [2] earlier prove a similarly sharp inequality for the different *symmetric-point starlike* class and display \(z/(1-z^2)\) as an equality example; this already-known example is not presented as novel. Neither inspected manuscript states or implies the full necessity-and-sufficiency characterization in the ordinary starlike class. An equivalent earlier equality classification not located in the inspected sources remains a bibliographic possibility.

## Limitations
This is an equality-case theorem, **not a new numerical sharp constant** or a stability estimate near extremizers. It uses the established sharp inequality and Carathéodory coefficient parametrization. The exact algebra and coefficient positivity are independently replayable, but no independent mathematical audit is represented. The proof does not classify extremizers for determinants of other orders or other analytic subclasses.

## References
[1] Vasudevarao Allu and Shobhit Kumar, *On the Third Hankel Determinant for Inverse Coefficients of Starlike Functions: A Bernstein Polynomial Approach*, arXiv:2604.23220v1 (first posted 2026-04-25), especially Lemma 1.1, Theorem 2.1 and equations (2.4)--(2.6). https://arxiv.org/pdf/2604.23220

[2] B. Rath, D. V. Krishna, K. S. Kumar and G. K. S. Viswanadh, *The sharp bound of the third Hankel determinants for inverse of starlike functions with respect to symmetric points*, Matematychni Studii 58 (2022), 45--50, DOI:10.30970/ms.58.1.45-50. https://matstud.org.ua/ojs/index.php/matstud/article/download/344/159/
