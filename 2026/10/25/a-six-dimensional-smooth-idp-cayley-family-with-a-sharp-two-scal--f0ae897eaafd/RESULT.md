# A six-dimensional smooth IDP Cayley family with a sharp two-scale \(h^*\)-log-concavity window

## Finding
For positive integers \(a,b\), define the \(3\times4\) matrix
\[
M_{a,b}=\begin{pmatrix}a&b&1&1\\a&1&b&1\\a&1&1&b\end{pmatrix}
\]
and the associated six-dimensional Cayley lattice polytope \(P_{a,b}\) (defined precisely below). Every \(P_{a,b}\) is smooth and admits a regular unimodular flag triangulation; in particular it has the integer decomposition property (IDP).

Its Ehrhart numerator is \(h^*_{P_{a,b}}(z)=1+H_1z+H_2z^2+H_3z^3\), where
\[
\begin{aligned}
H_1&=a^3+3a^2+3a+12b+6,\\
H_2&=4a^3+3a^2b+6a^2+12ab+9a+9b^2+18b+6,\\
H_3&=(a+b+1)^3.
\end{aligned}
\]
These coefficients are log-concave if and only if \(F(a,b)\ge0\), where
\[
\begin{aligned}
F(a,b)={}&69b^4+(-a^3+51a^2+177a+282)b^3\\
&+(6a^4+132a^3+306a^2+495a+378)b^2\\
&+(21a^5+117a^4+300a^3+387a^2+387a+186)b\\
&+15a^6+42a^5+93a^4+131a^3+123a^2+87a+30.
\end{aligned}
\]
For each fixed positive \(a\), the open real negative locus \(\{b>0:F(a,b)<0\}\) is either empty or one interval. For all sufficiently large \(a\) it is a nonempty interval \((b_-(a),b_+(a))\) with sharp asymptotic endpoints
\[
b_-(a)\sim\rho a,\qquad b_+(a)\sim a^3/69,
\]
where \(\rho=8.6335955628\ldots\) is the unique positive root of \(15+21r+6r^2-r^3=0\). For integer \(b\), failure occurs exactly when the integer lies in this interval.

For every integer \(t\ge100\), \(P_{t,36t}\) is a smooth six-dimensional IDP polytope with a non-log-concave Ehrhart numerator, whereas all integers \(1\le t\le99\) on that ray are log-concave. At \((a,b)=(100,3600)\),
\[
h^*(z)=1+1073506z+233085706z^2+50694081101z^3,
\]
and \(H_2^2-H_1H_3=-91453884891670\).

## Assumptions and scope
For \(j=0,1,2,3\) let \(D_j=\prod_{i=1}^{3}[0,M_{a,b}(i,j)]\subset\mathbb R^3\). Write \(v_0=(0,0,0)\) and \(v_1,v_2,v_3\) for the three standard basis vectors in \(\mathbb R^3\). Set
\[
P_{a,b}=\operatorname{conv}\bigcup_{j=0}^{3}\bigl(D_j\times\{v_j\}\bigr)\subset\mathbb R^6.
\]
The ambient lattice is \(\mathbb Z^6\). Positivity of all entries for \(a,b\ge1\) ensures dimension six. The assertion is about the coefficient log-concavity of the \(h^*\)-polynomial, **not** about log-concavity of the infinite Ehrhart counting sequence, nor about non-unimodality. The real parameter \(b\) in the root analysis is only an auxiliary polynomial continuation; geometric polytopes always have integer parameters.

## Proof
1. **Smoothness and decomposition.** Ferroni's propositions on Cayley sums of coordinate boxes prove that the polytope associated to any nonnegative matrix with nonzero rows has a regular unimodular flag triangulation and that positive entries make it smooth [1, Propositions 2.2 and 2.3]. These hypotheses hold for \(M_{a,b}\). Unimodular triangulation implies IDP.

2. **Counting.** For each \(k\ge0\), Ferroni's lattice-slice formula [1, Theorem 3.1] specializes to
\[
L_{P_{a,b}}(k)=\sum_{c_0+c_1+c_2+c_3=k\atop c_j\ge0}
\prod_{i=1}^{3}\bigl(1+ac_0+bc_i+\sum_{1\le j\le3,\ j\ne i}c_j\bigr).
\]
His binomial-basis formula also shows that the numerator has degree at most three, despite the ambient dimension six. Taking \(L(0),L(1),L(2),L(3)\) and using the denominator \((1-z)^7\) gives \(H_1=L(1)-7\), \(H_2=L(2)-7L(1)+21\), and \(H_3=L(3)-7L(2)+21L(1)-35\). Direct expansion yields the displayed coefficients; there are no higher terms.

3. **Only one possibly negative log-concavity difference.** Direct algebra gives
\[
\begin{aligned}
H_1^2-H_2={}&a^6+6a^5+15a^4+24a^3b+26a^3+69a^2b+39a^2\\
&+60ab+27a+135b^2+126b+30>0.
\end{aligned}
\]
The remaining nontrivial inequality is \(H_2^2\ge H_1H_3\), and expansion shows \(H_2^2-H_1H_3=F(a,b)\). The coefficient sequence has no internal zeros, and the trailing zero inequalities are automatic.

4. **Topology of the negative locus.** For each positive \(a\), read \(F(a,b)\) as a quartic in real \(b>0\). Its leading, quadratic, linear and constant coefficients are strictly positive. The cubic coefficient is the only one that can be negative. Therefore its ordered nonzero coefficients have either zero or two sign changes. Descartes's rule of signs gives at most two positive roots counted with multiplicity. Since \(F(a,0)>0\) and \(F(a,b)\to+\infty\) as \(b\to+\infty\), any negative region must be one interval bounded by two simple positive roots; otherwise the root count would exceed two. There is no negative region when the cubic coefficient is nonnegative.

5. **Two asymptotic scales.** Polynomial inspection gives, for every fixed positive real \(r,c\),
\[
\lim_{a\to\infty}\frac{F(a,ra)}{a^6}=15+21r+6r^2-r^3=:f(r),
\qquad
\lim_{a\to\infty}\frac{F(a,ca^3)}{a^{12}}=c^3(69c-1).
\]
Descartes's rule applied to \(r^3-6r^2-21r-15\) gives exactly one positive root \(\rho\); thus \(f(r)>0\) below it and is negative above it. For any fixed \(r>\rho\), \(F(a,ra)<0\) for large \(a\), whereas \(F(a,0)>0\). At cubic scale the sign switches across \(c=1/69\). The at-most-two-root conclusion forces the two roots to satisfy the asserted ratios: bracket the first using \(r\) on either side of \(\rho\), and bracket the second using \(c\) on either side of \(1/69\). No additional roots can intervene.

6. **An exact infinite ray with sharp integer onset.** Substitution yields
\[
F(t,36t)=-38109t^6+2554782t^5+124559085t^4+13812575t^3+503943t^2+6783t+30.
\]
By Descartes's rule, this polynomial has exactly one positive real root (one sign change and opposite signs at zero/infinity). Direct exact substitution gives \(F(99,3564)=395358876665409>0\) and \(F(100,3600)=-91453884891670<0\). Its unique root lies strictly between 99 and 100, establishing the claimed sharp integer threshold and infinitely many distinct Ehrhart numerators along the ray (since \(H_1\) is strictly increasing in \(t\)).

## Verification
The accompanying `check_cayley.py` independently evaluates the lattice-slice sum for every \(1\le a\le12\), \(1\le b\le16\) and dilation \(0\le k\le6\); it compares those counts with the Ehrhart series reconstructed from the stated numerator. It checks both coefficient inequalities and the quartic expansion in 192 parameter pairs, as well as the sharp ray signs for 200 positive integers and the full large witness by exact integers. It uses only the Python standard library. The proof of the unbounded parameter claim is symbolic and does not rely on this finite test.

## Relationship to prior work
Ferroni [1] introduced the ambient Cayley-box construction, proved the smoothness and triangulation theorems, and derived the general Ehrhart counting and numerator formulas. He exhibited nonunimodal examples in dimension forty and a nine-dimensional family whose **Ehrhart counting sequence** is not log-concave. The present work specializes his formulas to a positive \(3\times4\) matrix and determines an exact two-parameter **numerator** log-concavity phase condition and a six-dimensional smooth infinite family. Hofscheier, Kurylenko and Nill [2] previously exhibited a seven-dimensional IDP polytope with a non-log-concave \(h^*\)-vector; their construction is different and does not imply this smooth dimension-six phase diagram. Related preservation results for Cartesian segment factors do not cover Cayley sums with independently varying fiber boxes.

## Limitations
The theorem makes no claim of globally smallest possible dimension, nor does it settle Stanley's unimodality conjecture: these examples have an increasing nonzero \(h^*\)-coefficient sequence for the exhibited large parameters. All assertions about smoothness and existence of a regular unimodular flag triangulation rely on the cited published general theorems. Historical novelty is judged relative to the inspected primary sources and record searches; equivalent descriptions in unindexed literature remain possible. Independent scientific audit has not been performed.

## References
[1] Luis Ferroni, *Unimodality shenanigans in Ehrhart theory*, arXiv:2609.10513 (first public version 2026-09-09), especially Propositions 2.2--2.3 and Theorem 3.1. https://arxiv.org/pdf/2609.10513

[2] Johannes Hofscheier, Vadym Kurylenko and Benjamin Nill, *Examples of IDP lattice polytopes with non-log-concave \(h^*\)-vector*, arXiv:2505.18896 (2025), especially Theorem 1.2. https://arxiv.org/pdf/2505.18896
