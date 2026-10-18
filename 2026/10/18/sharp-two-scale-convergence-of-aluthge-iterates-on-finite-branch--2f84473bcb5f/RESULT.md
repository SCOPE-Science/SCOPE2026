# Sharp two-scale convergence of Aluthge iterates on finite-branch weighted trees

## Finding
Fix \(0<t<1\). Iterating the \(t\)-Aluthge transform on a rooted directed tree consisting of finitely many infinite rays joined at their common root produces operator-norm convergence whenever the weights along each ray are positive constants. The limit is quasinormal, and the norm error has an exact two-scale phase diagram governed by the intrinsic radial rate \(\rho\) and the Aluthge relaxation rate \(\eta=1-t\). At equality of the rates the two independent errors add in quadrature; even on the relaxation-dominated side, one precisely tunable initial normalization eliminates the slower mode.

Let \(d\ge2\), \(a_i,c_i>0\) for \(1\le i\le d\), and \(C=\max_i c_i\). Suppose first that at least one \(c_i<C\). Define
\[
I=\{i:c_i=C\},\quad A_*=\sum_{i\in I}a_i^2,\quad
\eta=1-t,\quad \rho=\max_{i\notin I}(c_i/C)^t,
\]
\[
Q=\sum_{i\notin I:\,(c_i/C)^t=\rho}a_i^2/A_*\,>0,\qquad
z_m=\log\left(1+\sum_{i\notin I}\frac{a_i^2}{A_*}(c_i/C)^{2tm}\right).
\]
For \(\eta\ge\rho\), the series
\[
H=\log\frac{\sum_i a_i^2}{C^2}
+\sum_{j=0}^{\infty}\eta^{-j-1}(z_{j+1}-z_j)
\]
converges absolutely. Let \(E_m=\|\Delta_t^m(S_0)-S_\infty\|\), where the limiting operator is specified below. Then
\[
\begin{array}{c|c|c}
\text{condition}&\text{normalization}&\text{strictly positive limit}\\ \hline
\eta<\rho&E_m/\rho^m&C\sqrt Q\\
\eta=\rho&E_m/\rho^m&C\sqrt{Q+H^2/4}\\
\eta>\rho,\ H\ne0&E_m/\eta^m&C|H|/2\\
\eta>\rho,\ H=0&E_m/\rho^m&C\sqrt Q
\end{array}
\]
The coefficient \(H\) changes by twice the logarithm of a common positive scaling of all root-edge weights, while \(\rho,Q\) do not change; consequently the exceptional cancellation \(H=0\) can always be achieved by exactly one such scaling.

## Assumptions and scope
Work in the complex Hilbert space \(\ell^2(V)\) with orthonormal basis \(e_o\) for a root and \(e_{i,j}\) for \(1\le i\le d\), \(j\ge1\). Set
\[
S_0e_o=\sum_{i=1}^d a_i e_{i,1},\qquad
S_0e_{i,j}=c_i e_{i,j+1}.
\]
All \(a_i,c_i\) are strictly positive real constants. There is no upper bound on \(d\) other than finiteness. For every bounded operator \(T=U|T|\) in polar form use \(\Delta_t(T)=|T|^tU|T|^{1-t}\); the exponent \(t\) is held fixed across all iterations. Let \(C=\max_i c_i\), \(I=\{i:c_i=C\}\), and \(A_*=\sum_{i\in I}a_i^2\). The limit is the bounded shift
\[
S_\infty e_o=\sum_{i\in I} C\frac{a_i}{\sqrt{A_*}}e_{i,1},\qquad
S_\infty e_{i,j}=c_i e_{i,j+1}.
\]
Thus the slower rays remain present in the operator but cease to receive any mass from the root. The limit is quasinormal rather than normal in general: \(S_\infty\) commutes with \(S_\infty^*S_\infty\), because the column norm is \(C\) at the root and on every ray with nonzero root weight, while every other ray has its own constant column norm \(c_i\). It is not asserted that \(S_\infty\) is normal.

## Proof
**1. Polar recursion.** Distinct columns of a weighted-tree shift have disjoint support. The modulus of \(S_m\) is diagonal, with diagonal entry \(\sqrt{R_m}\) at the root and \(c_i\) at each vertex on ray \(i\), where \(R_m=\sum_i a_{i,m}^2\). Applying the polar definition directly yields
\[
a_{i,m+1}=a_{i,m}c_i^t R_m^{-t/2},\qquad
S_me_{i,j}=c_i e_{i,j+1},
\tag{1}
\]
with \(a_{i,0}=a_i\). The sums \(R_m\) remain positive, so there is no polar-domain ambiguity. Formula (1) is the specialization of the general one-step weighted-tree identity in Trepkowski [1], but is also derived here.

**2. Solving the finite nonlinear recurrence.** Divide the squares of the root weights by their sum. The common \(R_m^{-t}\) factor in (1) cancels, giving exactly
\[
\frac{a_{i,m}^2}{R_m}=
\frac{a_i^2(c_i/C)^{2tm}}{
 A_*\left(1+\sum_{j\notin I}(a_j^2/A_*)(c_j/C)^{2tm}\right)}.
\tag{2}
\]
Put \(h_m=\log(R_m/C^2)\) and \(z_m\) as in the statement. Summing (1) and using (2) gives
\[
h_0=\log\frac{\sum_i a_i^2}{C^2},\qquad
h_{m+1}=\eta h_m+z_{m+1}-z_m.
\tag{3}
\]
Consequently, for every \(i,m\),
\[
a_{i,m}= C\frac{a_i}{\sqrt{A_*}}
 \exp\left(\frac{h_m-z_m}{2}\right)
 \left(\frac{c_i}{C}\right)^{tm}.
\tag{4}
\]
Let \(r_i=(c_i/C)^{2t}\), \(r=\max_{i\notin I}r_i=\rho^2\), and \(q_i=a_i^2/A_*\). By finiteness and positivity,
\[
z_m=Qr^m+o(r^m),\qquad
z_{m+1}-z_m=O(r^m),\qquad 0<r<\rho<1.
\tag{5}
\]
Equation (3) and (5) imply \(h_m\to0\): the scalar linear recurrence has a contractive homogeneous factor \(0<\eta<1\) and forcing tending to zero. Equation (4) now gives \(a_{i,m}\to C a_i/\sqrt{A_*}\) for \(i\in I\), and \(a_{i,m}\to0\) otherwise. Since only the finite-dimensional root column changes, the convergence is in the full operator norm, not merely strong or coordinatewise convergence.

**3. Exact operator norm of the error.** Subtract the root columns from (4). Contributions on \(I\) and its complement are orthogonal. Using (2) to sum the complementary squared weights gives the identity, valid for every integer \(m\ge0\),
\[
\boxed{\displaystyle
 \frac{E_m^2}{C^2}=
 \left[\exp\!\left(\frac{h_m-z_m}{2}\right)-1\right]^2
 +e^{h_m}(1-e^{-z_m}).}
\tag{6}
\]
No estimate or neglected tail enters (6), because the original and limiting shifts agree at every nonroot column.

**4. Sharp asymptotic separation.** If \(\eta<\rho\), the solution of (3) satisfies \(h_m=o(\rho^m)\), including the possible repeated-forcing case \(\eta=r\), where \(h_m=O(mr^m)\). Also \(z_m=O(r^m)=o(\rho^m)\). The first squared term in (6) is therefore \(o(\rho^{2m})\), while the second is \(Qr^m(1+o(1))\). This proves the first case.

If \(\eta\ge\rho\), then \(r=\rho^2<\eta\); multiplying (3) by \(\eta^{-m-1}\) and summing proves absolute convergence of \(H\) and
\[
h_m=H\eta^m+O(r^m).
\tag{7}
\]
If \(\eta=\rho\), equations (5)--(7) show that the squared first term in (6), divided by \(\rho^{2m}\), tends to \(H^2/4\), while the complementary second term tends to \(Q\). Hence the second case, including resonance when \(H=0\).

If \(\eta>\rho\), then the second term of (6) is \(o(\eta^{2m})\). For \(H\ne0\) the first yields \(E_m/\eta^m\to C|H|/2\). If instead \(H=0\), the estimate in (7) sharpens to \(h_m=O(r^m)\), the first term is \(o(r^m)\), and the second restores \(E_m/\rho^m\to C\sqrt Q\). Thus all four limits follow and each given limit is positive.

**5. Tunability and equal-ray boundary.** If all \(a_i\) are multiplied by \(s>0\), the ratios \(q_i\), all \(z_m\), \(Q\), and \(\rho\) remain unchanged; the initial \(h_0\) increases by \(2\log s\), so \(H\) increases by exactly \(2\log s\). One and only one positive choice of \(s\) makes \(H=0\). When all \(c_i=C\), there are no slow rays and \(z_m=0\). Equation (3) becomes \(h_m=\eta^m h_0\); (4) and (6) reduce to
\[
E_m=C\left|\exp\left(\frac{\eta^m}{2}\log\frac{\sum_i a_i^2}{C^2}\right)-1\right|.
\tag{8}
\]
This is identically zero when \(\sum_i a_i^2=C^2\), and otherwise \(E_m/\eta^m\to(C/2)|\log(\sum_i a_i^2/C^2)|\). The theorem includes this boundary separately rather than assigning an undefined \(\rho\).

## Verification
The independently implementable finite-weight recursion (1), closed expressions (2)--(6), all four asymptotic normalizations, cancellation by common scaling, and the equal-tail identity (8) are exercised by the accompanying standalone `artifacts/verify.py` script (Python standard library only). Its deterministic run reports **6,800 scalar assertions passed**, using direct finite-depth tree-weight transformations, distinct decay regimes, and the exact error norm. The finite-depth checks corroborate the algebra, but **do not prove** convergence or sharp limits in the infinite-dimensional setting; those are established by equations (1)--(8). Run with `python3 artifacts/verify.py` from the extracted package root.

## Relationship to prior work
Trepkowski [1] gives the general one-step \(t\)-Aluthge transform formula for shifts on directed trees, including unbounded examples and domain phenomena. Its one-step formula alone does not state this closed recurrence, full norm limit, or the sharp two-rate and resonance classification. Antezana, Pujals, and Stojanoff [2] survey convergence for finite matrices and exhibit failure of weak convergence for some infinite-dimensional operators; their open-problems section treats infinite-dimensional convergence as a distinct challenge. Exner, Jung, and Lee [3] treat the same rooted one-branching tree class, but their theorems concern \(n\)-contractivity and hyponormality rather than iteration or convergence rates. Exner and collaborators [4] study quasinormality/paranormality of one-branching tree shifts without an Aluthge iteration analysis. Rion [5] considers Aluthge sequences of classical unilateral shifts with eventually lower-bounded weights; that one-ray setting does not directly imply this multiple-ray interaction. An equivalent historical theorem could remain unlocated, notably because the complete text of [5] was unavailable for comparison.

## Limitations
Only finitely many rays, strictly positive real root and constant-tail weights, and a fixed \(0<t<1\) are treated. No statement is made for variable tail weights, zero initial weights, general infinitely branching trees, time-dependent \(t\), or a uniform convergence constant as \(t\) approaches an endpoint. The limiting shift is quasinormal but need not be normal. The exact rates are pointwise in the fixed positive parameters. Numerical checks do not constitute an infinite-dimensional proof. Literature comparison cannot establish global priority, and one plausibly relevant historical paper was not available in full text.

## References
[1] J. Trepkowski, *Aluthge transforms of weighted shifts on directed trees*, arXiv:1401.4415v1 (public 17 January 2014); J. Math. Anal. Appl. 425 (2015), 886--899; DOI:10.1016/j.jmaa.2015.01.027.

[2] J. Antezana, E. R. Pujals and D. Stojanoff, *Iterated Aluthge transforms: a brief survey*, Rev. Unión Mat. Argentina 49 (2008), 27--40. Open full text: https://sedici.unlp.edu.ar/handle/10915/156336.

[3] G. R. Exner, I. B. Jung and M. R. Lee, *Weighted shifts on directed trees with one branching vertex: n-contractivity and hyponormality*, Osaka J. Math. 58 (2021), 803--814; DOI:10.18910/84950.

[4] G. R. Exner et al., *Weighted shifts on directed trees with one branching vertex: between quasinormality and paranormality*, Math. Inequal. Appl. 26 (2023), available at https://files.ele-math.com/articles/mia-26-37.pdf.

[5] K. Rion, *Convergence properties of the Aluthge sequence of weighted shifts*, Houston J. Math. 42 (2016), 1217--1226. Complete original unavailable for this comparison.
