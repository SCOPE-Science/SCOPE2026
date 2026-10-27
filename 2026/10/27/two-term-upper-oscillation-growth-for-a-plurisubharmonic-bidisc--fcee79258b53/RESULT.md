# Two-term upper-oscillation growth for a plurisubharmonic bidisc counterexample

## Finding
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), and define the extended-valued plurisubharmonic function
\[
\phi(z,w)=-\sqrt{(\log|z|+\log|w|)\log|w|},
\]
with value \(-\infty\) on the coordinate axes. For \(A,B>0\), let
\[
P_{A,B}=\{(z,w)\in\mathbb D^2: |z|<e^{-A},\ |w|<e^{-B}\}.
\]
Using ordinary Lebesgue volume \(dV\), define upper oscillation by
\[
\operatorname{UO}_{P}(\phi)=\sup_{P}\phi-\frac{1}{\operatorname{Vol}(P)}\int_P\phi\,dV.
\]
For every fixed \(B>0\), as \(A\to\infty\),
\[
\operatorname{UO}_{P_{A,B}}(\phi)=c(B)\sqrt A+\frac{d(B)}{\sqrt A}+O_B(A^{-3/2}),
\]
where
\[
c(B)=\frac{e^{2B}}{\sqrt2}\,\Gamma\!\left(\frac32,2B\right)-\sqrt B>0
\]
and
\[
d(B)=\frac{e^{2B}}{2^{5/2}}\left[\Gamma\!\left(\frac52,2B\right)+\Gamma\!\left(\frac32,2B\right)\right]-\frac12 B^{3/2}.
\]
Here \(\Gamma(s,x)=\int_x^\infty t^{s-1}e^{-t}\,dt\) is the upper incomplete gamma function. The remainder constant may depend on the fixed value of \(B\).

## Assumptions and scope
The parameter \(B\) is fixed and strictly positive; only \(A\) tends to infinity. Thus the second polydisc radius \(e^{-B}\) is fixed while the first radius \(e^{-A}\) shrinks to zero. The measure in the average is normalized Lebesgue volume on the polydisc. The plurisubharmonicity of this particular \(\phi\) is established in Chen and Wang, Theorem 3.5; the claim here is a quantitative asymptotic for its upper oscillation, not a theorem for arbitrary plurisubharmonic functions.

## Proof
Under normalized area measure on the disk \(|z|<e^{-A}\), the random variable
\[
X=-\log\left(\frac{|z|}{e^{-A}}\right)
\]
has density \(2e^{-2x}\) for \(x\ge0\). Likewise, under normalized area measure on \(|w|<e^{-B}\),
\[
Y=-\log\left(\frac{|w|}{e^{-B}}\right)
\]
has the same density. The variables are independent because normalized volume on a polydisc is a product measure. Hence \(X,Y\) are independent exponential random variables of rate \(2\), and
\[
\log|z|=-A-X,\qquad \log|w|=-B-Y.
\]
Consequently,
\[
\phi(z,w)=-\sqrt{(A+B+X+Y)(B+Y)}
\]
under the normalized volume average. The function \((x,y)\mapsto-\sqrt{(x+y)y}\) is increasing in each variable on \(( -\infty,0)^2\), as verified in the cited source. Its supremum over the open polydisc is therefore the boundary limit \(-\sqrt{(A+B)B}\). It follows that the exact oscillation identity is
\[
\operatorname{UO}_{P_{A,B}}(\phi)=\mathbb E\sqrt{(A+B+X+Y)(B+Y)}-\sqrt{(A+B)B}.
\]
Set \(S=B+X+Y\). For \(u\ge0\), Taylor's theorem and \(|(\sqrt{1+u})''|\le1/4\) give
\[
\sqrt{1+u}=1+\frac u2+R(u),\qquad |R(u)|\le\frac{u^2}{8}.
\]
Since \(X,Y\) have exponential tails, \(\mathbb E[S^2\sqrt{B+Y}]<\infty\). Applying this remainder bound with \(u=S/A\) yields
\[
\mathbb E\sqrt{(A+S)(B+Y)}=\sqrt A\,\mathbb E\sqrt{B+Y}+\frac{\mathbb E[S\sqrt{B+Y}]}{2\sqrt A}+O_B(A^{-3/2}).
\]
The same expansion gives
\[
\sqrt{(A+B)B}=\sqrt A\sqrt B+\frac{B^{3/2}}{2\sqrt A}+O_B(A^{-3/2}).
\]
Subtracting proves the two-term expansion with
\[
c(B)=\mathbb E\sqrt{B+Y}-\sqrt B,
\]
\[
d(B)=\frac12\mathbb E[(B+X+Y)\sqrt{B+Y}]-\frac12B^{3/2}.
\]
Because \(Y>0\) almost surely and the square-root function is strictly increasing, \(c(B)>0\).

For \(s>-1\), direct substitution \(u=B+y\) gives the exact moment formula
\[
\mathbb E(B+Y)^s=2e^{2B}\int_B^\infty e^{-2u}u^s\,du=2^{-s}e^{2B}\Gamma(s+1,2B).
\]
Using \(\mathbb E X=1/2\), the expression for \(d(B)\) becomes
\[
d(B)=\frac12\mathbb E(B+Y)^{3/2}+\frac14\mathbb E(B+Y)^{1/2}-\frac12B^{3/2},
\]
which is the stated incomplete-gamma formula. All error terms are controlled by finite exponential moments, so no numerical extrapolation is used.

## Verification
The normalization follows from the radial density \(2r\,dr\) on a disk after scaling its radius to one. The exact oscillation identity separates the boundary supremum from the normalized volume average. The two Taylor remainders are bounded by constants times \(A^{-3/2}\), with finite expectation for fixed \(B>0\). The incomplete-gamma expressions follow by integration of the rate-\(2\) exponential density. The result is an asymptotic statement for fixed \(B\); it does not assert uniformity as \(B\) varies.

## Relationship to prior work
Chen and Wang introduced this same plurisubharmonic counterexample to show that arbitrary bidiscs do not admit a uniform local upper-oscillation bound. Their Theorem 3.5 and Lemmas 3.6–3.7 establish divergence of the relevant oscillation but do not state the two-term expansion or the coefficient \(c(B)\). The present claim quantifies the failure along the specific path with one fixed radius and the other tending to zero; it does not replace their broader qualitative theorem.

## Limitations
The asymptotic holds only for the stated function and fixed \(B>0\). It gives no uniform estimate in \(B\), no growth law for general plurisubharmonic functions, and no optimality statement among all possible counterexamples. The literature search cannot rule out an unindexed source containing the same calculation.

## References
Bo-Yong Chen and Xu Wang, “Bergman kernel and oscillation theory of plurisubharmonic functions,” arXiv:1906.10170 (first public date 2019-06-24); *Mathematische Zeitschrift* 297 (2021), 1507–1527. DOI: 10.1007/s00209-020-02567-9. Relevant material: Theorem 1.1, Theorem 3.5, and Lemmas 3.6–3.7.
