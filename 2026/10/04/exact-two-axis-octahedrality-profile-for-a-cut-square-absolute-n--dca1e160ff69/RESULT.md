# Exact two-axis octahedrality profile for a cut-square absolute norm family
## Finding
For \(0\le t\le1\), define the absolute normalized norm
\[
N_t(a,b)=\max\!\left\{|a|,|b|,\frac{|a|+|b|}{1+t}\right\}.
\]
Let \(X\) and \(Y\) be nonzero real Banach spaces with octahedral norms, fix \(x\in S_X\) and \(y\in S_Y\), and put \(Z_t=X\oplus_{N_t}Y\). Define the two-axis simultaneous witness constant
\[
\Theta_t(x,y)=\sup_{(u,v)\in S_{Z_t}}\min\!\left\{
\|(x,0)+(u,v)\|_{N_t},\ \|(0,y)+(u,v)\|_{N_t}
\right\}.
\]
Then
\[
\Theta_t(x,y)=\max\!\left\{\frac{3+t}{2},\frac{2+t}{1+t}\right\}
=
\begin{cases}
\dfrac{2+t}{1+t},&0\le t\le \sqrt2-1,\\[4pt]
\dfrac{3+t}{2},&\sqrt2-1\le t\le1.
\end{cases}
\]
Hence \(\Theta_t(x,y)=2\) exactly at \(t=0\) and \(t=1\), while for every \(0<t<1\) the pair \(\{(x,0),(0,y)\}\) already gives a strict quantitative obstruction to octahedrality. The obstruction is largest at \(t=\sqrt2-1\), where
\[
\Theta_t(x,y)=1+\frac1{\sqrt2}.
\]

## Assumptions and scope
The spaces are real and both component norms are octahedral. The parameter family \(N_t\) interpolates between \(\ell_1^2\) at \(t=0\) and \(\ell_\infty^2\) at \(t=1\); in the positive quadrant its unit ball is the square \([0,1]^2\) cut by \(a+b\le1+t\). The claim concerns the exact best common witness for the two canonical axis points, not the average-roughness modulus or arbitrary finite subsets.

The result is a quantitative refinement of the positive-octahedrality criterion for absolute sums: positive octahedrality asks whether the corresponding two-axis value can reach \(2\), while the formula above gives the exact shortfall throughout this natural one-parameter family.

## Proof
We first isolate a general scalar reduction. Let \(N\) be any absolute normalized norm on \(\mathbb R^2\), let \(X,Y\) be octahedral, and let \(x\in S_X\), \(y\in S_Y\). Define
\[
\Omega(N)=\max_{\substack{c,d\ge0\\N(c,d)=1}}
\min\{N(1+c,d),N(c,1+d)\}.
\]
We claim that the analogue of \(\Theta_t(x,y)\) with \(N\) in place of \(N_t\) equals \(\Omega(N)\).

For the upper bound, take any \((u,v)\in S_{X\oplus_NY}\), set \(c=\|u\|\), \(d=\|v\|\), and note that \(N(c,d)=1\). By the triangle inequality and coordinatewise monotonicity of absolute normalized norms,
\[
\|(x,0)+(u,v)\|_N
=N(\|x+u\|,d)
\le N(1+c,d),
\]
and similarly
\[
\|(0,y)+(u,v)\|_N\le N(c,1+d).
\]
Thus every witness is bounded above by \(\Omega(N)\).

For the reverse inequality, fix \(c,d\ge0\) with \(N(c,d)=1\) and fix \(\varepsilon>0\). Octahedrality gives \(\xi\in S_X\) with \(\|x+\xi\|>2-\varepsilon\). If \(f\in S_{X^*}\) norms \(x+\xi\), then \(f(x)+f(\xi)>2-\varepsilon\), so each of \(f(x)\) and \(f(\xi)\) exceeds \(1-\varepsilon\). Therefore, for \(0\le c\le1\),
\[
\|x+c\xi\|\ge f(x+c\xi)>(1-\varepsilon)(1+c).
\]
Absolute normalized norms dominate the \(\ell_\infty\)-norm, hence every positive sphere point has \(0\le c,d\le1\). Applying the same argument in \(Y\), choose \(\eta\in S_Y\) with
\[
\|y+d\eta\|>(1-\varepsilon)(1+d).
\]
Then \((c\xi,d\eta)\in S_{X\oplus_NY}\), and coordinatewise monotonicity gives
\[
\|(x,0)+(c\xi,d\eta)\|_N
\ge(1-\varepsilon)N(1+c,d),
\]
\[
\|(0,y)+(c\xi,d\eta)\|_N
\ge(1-\varepsilon)N(c,1+d).
\]
Letting \(\varepsilon\downarrow0\) and maximizing over the compact positive sphere proves the scalar reduction.

Now specialize to \(N_t\). For a positive sphere point write \(s=c+d\) and \(m=\min\{c,d\}\). The conditions \(N_t(c,d)=1\) imply
\[
0\le c,d\le1,\qquad s\le1+t.
\]
Moreover,
\[
N_t(1+c,d)=\max\!\left\{1+c,\frac{1+s}{1+t}\right\},
\]
because \(1+c\ge d\), and similarly
\[
N_t(c,1+d)=\max\!\left\{1+d,\frac{1+s}{1+t}\right\}.
\]
Using \(\min\{\max(A,q),\max(B,q)\}=\max\{\min(A,B),q\}\), the objective becomes
\[
\max\!\left\{1+m,\frac{1+s}{1+t}\right\}.
\]
Since \(m\le s/2\le(1+t)/2\) and \(s\le1+t\), every positive sphere point satisfies
\[
\min\{N_t(1+c,d),N_t(c,1+d)\}
\le
\max\!\left\{\frac{3+t}{2},\frac{2+t}{1+t}\right\}.
\]
Equality is attained at the diagonal point
\[
(c,d)=\left(\frac{1+t}{2},\frac{1+t}{2}\right),
\]
which lies on the sphere because \((c+d)/(1+t)=1\). This proves the exact formula.

Finally,
\[
\frac{3+t}{2}=\frac{2+t}{1+t}
\]
is equivalent to \(t^2+2t-1=0\), whose unique root in \([0,1]\) is \(t=\sqrt2-1\). The rational branch \((2+t)/(1+t)\) decreases and the affine branch \((3+t)/2\) increases, so their maximum has its unique minimum at that crossing. Substitution gives \(1+1/\sqrt2\). The endpoint values are \(2\), and every interior value is strictly below \(2\).

## Verification
The proof is analytic and does not depend on finite enumeration. The accompanying `verify_two_axis_profile.py` uses exact rational arithmetic to enumerate dense rational samples on all three boundary segments of the positive \(N_t\)-sphere for many rational parameters, confirms that no sampled point exceeds the closed form, and confirms that the diagonal point attains it exactly. It also checks the branch comparison and the endpoint identities.

## Relationship to prior work
Haller, Langemets, and Nadel introduced positive octahedrality for absolute normalized norms and proved that, for octahedral \(X\) and \(Y\), the absolute sum \(X\oplus_NY\) is octahedral exactly when \((\mathbb R^2,N)\) is positively octahedral. Their endpoint characterization asks for one positive sphere point \((c,d)\) satisfying both \(N((1,0)+(c,d))=2\) and \(N((0,1)+(c,d))=2\). The scalar reduction above is the exact quantitative version of that two-endpoint test, and the displayed formula evaluates it on the cut-square family.

Haller, Pirk, and Veeorg later recast the same endpoint condition as \(\{(1,0),(0,1)\}\)-octahedrality while studying Daugavet points in absolute sums. The inspected material remains qualitative: it distinguishes whether the endpoint level \(2\) is attained, but it does not state the exact subcritical profile for the family \(N_t\), the crossing at \(\sqrt2-1\), or the minimum \(1+1/\sqrt2\).

## Limitations
The theorem computes one natural two-point obstruction, not a complete quantitative modulus for arbitrary finite subsets of an absolute sum. It does not determine the exact average-roughness constant of \(X\oplus_{N_t}Y\). The originality conclusion is based on targeted semantic and full-text searches and therefore cannot exclude an equivalent statement under substantially different terminology or in unindexed literature.

## References
1. R. Haller, J. Langemets, R. Nadel, *Stability of average roughness, octahedrality, and strong diameter two properties of Banach spaces with respect to absolute sums*, arXiv:1702.03140; Banach J. Math. Anal. 12 (2018), 222–239, DOI 10.1215/17358787-2017-0040.
2. R. Haller, K. Pirk, T. Veeorg, *Daugavet- and Delta-points in absolute sums of Banach spaces*, arXiv:2001.06197.
