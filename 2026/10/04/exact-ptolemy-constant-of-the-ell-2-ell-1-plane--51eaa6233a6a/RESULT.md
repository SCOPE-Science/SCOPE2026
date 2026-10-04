# Exact Ptolemy constant of the \(\ell_2-\ell_1\) plane
## Finding
For the real plane \(X=(\mathbb R^2,\|\cdot\|_{2,1})\), where \(\|(u,v)\|_{2,1}=\sqrt{u^2+v^2}\) when \(uv\ge 0\) and \(\|(u,v)\|_{2,1}=|u|+|v|\) when \(uv\le 0\), the Ptolemy constant is exactly \(C_{\mathrm{Pt}}(X)=\sqrt 2\).

Here \(C_{\mathrm{Pt}}(X)\) denotes
\[
C_{\mathrm{Pt}}(X)=\sup_{x,y,z\in X\setminus\{0\},\;x,y,z\ {\rm pairwise\ distinct}}
\frac{\|x-y\|\,\|z\|}{\|x-z\|\,\|y\|+\|z-y\|\,\|x\|}.
\]

## Assumptions and scope
The scalar field is real. The norm is the \(p=2\) member of the \(\ell_p-\ell_1\) family studied by Yang and Li. The claim concerns only this two-dimensional normed space and the standard Ptolemy constant above.

## Proof
For \(w=(u,v)\), set
\[
E(w)=\sqrt{u^2+v^2},\qquad F(w)=|u-v|.
\]
Then
\[
\|w\|_{2,1}=\max\{E(w),F(w)\}.
\]
Indeed, if \(uv\ge 0\), then \(F(w)\le E(w)\); if \(uv\le 0\), then \(F(w)=|u|+|v|\ge E(w)\). Also
\[
F(w)\le \sqrt 2\,E(w)
\]
by Cauchy--Schwarz.

Fix admissible \(x,y,z\). In the numerator
\[
\|x-y\|_{2,1}\|z\|_{2,1},
\]
choose for each factor a maximizing branch \(E\) or \(F\). There are three cases up to symmetry.

If both factors use \(E\), Euclidean Ptolemy gives
\[
E(x-y)E(z)\le E(x-z)E(y)+E(z-y)E(x),
\]
and each term on the right is at most the corresponding term with \(\|\cdot\|_{2,1}\). Hence the ratio is at most \(1\).

If both factors use \(F\), apply the ordinary one-dimensional Ptolemy inequality after the linear map \((u,v)\mapsto u-v\):
\[
F(x-y)F(z)\le F(x-z)F(y)+F(z-y)F(x).
\]
Again the ratio is at most \(1\).

In a mixed case, for example when the two numerator branches are \(E\) and \(F\),
\[
E(x-y)F(z)\le \sqrt 2\,E(x-y)E(z).
\]
Euclidean Ptolemy followed by \(E\le\|\cdot\|_{2,1}\) therefore gives an upper bound of \(\sqrt 2\) for the ratio. The other mixed case is identical. Thus
\[
C_{\mathrm{Pt}}(X)\le \sqrt 2.
\]

For the reverse inequality, let \(a>0\) and take
\[
x=(a,0),\qquad y=(0,a),\qquad z=(a,a).
\]
Then
\[
\|x-y\|_{2,1}=2a,\quad \|z\|_{2,1}=\sqrt 2\,a,
\]
while
\[
\|x-z\|_{2,1}=\|y\|_{2,1}=\|z-y\|_{2,1}=\|x\|_{2,1}=a.
\]
The Ptolemy ratio is therefore
\[
\frac{(2a)(\sqrt 2\,a)}{a^2+a^2}=\sqrt 2.
\]
Combining the two bounds proves the claim.

## Verification
The proof uses only the exact identity \(\|\cdot\|_{2,1}=\max\{E,F\}\), the sharp comparison \(F\le\sqrt 2\,E\), and Ptolemy inequalities for the Euclidean plane and real line. The extremizing triple is explicit and valid for every \(a>0\). No finite computation is used as a substitute for an infinite argument.

## Relationship to prior work
Yang and Li (2015) define the same \(\ell_p-\ell_1\) family and compute James-type and von Neumann--Jordan-type constants; the inspected article contains no Ptolemy computation.

Zuo (2012) gives exact Ptolemy formulas for absolute normalized norms under comparison hypotheses. After the linear coordinate change
\[
(s,b)=\left(\frac{u+v}{\sqrt 2},u-v\right),
\]
the present norm becomes
\[
\max\left\{\sqrt{s^2+b^2/2},|b|\right\},
\]
with associated absolute-normalized function
\[
\psi(t)=\max\left\{\sqrt{(1-t)^2+t^2/2},t\right\}.
\]
For the Euclidean comparison function \(\psi_2(t)=\sqrt{(1-t)^2+t^2}\), the ratio \(\psi_2/\psi\) is not maximized at \(t=1/2\): at \(t=1/2\) it equals \(2/\sqrt 3\), while at \(t=2-\sqrt 2\) it equals \(\sqrt{3/2}\). Thus the exact-value criterion of Zuo (2012) based on a midpoint extremum does not imply the claim.

Zuo (2018) develops further comparison theorems and concrete symmetric examples. The inspected theorems either retain a midpoint-extremum condition or, in the more general comparison result, assume symmetry of the associated function about \(t=1/2\); the function above is not symmetric. No exact value for this \(\ell_2-\ell_1\) norm was located in the inspected 2018 paper.

## Limitations
The literature comparison is bounded by accessible material. The full text of Zuo's 2015 reconsideration of absolute normalized norms could not be inspected; its abstract states that it gives additional sufficient conditions. This leaves a residual possibility that the present value follows from an uninspected criterion there. The mathematical proof above is independent of that access limitation.

## References
1. C. Yang and H. Li, “On the James type constant of \(\ell_p-\ell_1\),” Journal of Inequalities and Applications 2015, 79 (2015). DOI: 10.1186/s13660-015-0598-3.
2. E. Llorens-Fuster, E. M. Mazcuñán-Navarro, and S. Reich, “The Ptolemy and Zbăganu constants of normed spaces,” Nonlinear Analysis 72 (2010), 3984–3993. DOI: 10.1016/j.na.2010.01.030.
3. Z. Zuo, “The Ptolemy constant of absolute normalized norms on \(\mathbb R^2\),” Journal of Inequalities and Applications 2012, 107 (2012). DOI: 10.1186/1029-242X-2012-107.
4. Z. Zuo, “A Reconsideration on the Ptolemy Constant of Absolute Normalized Norms,” Acta Mathematica Sinica, Chinese Series 58 (2015), 337–344. DOI: 10.12386/A2015sxxb0033.
5. Z. Zuo, “On the Ptolemy constant of some concrete Banach spaces,” Mathematical Inequalities & Applications 21 (2018), 945–956. DOI: 10.7153/mia-2018-21-64.
