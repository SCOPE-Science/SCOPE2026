# Sharp variance-tail threshold in the \(\mathrm{Beta}(1,b)\) family
## Finding
For \(b>0\), let \(X_b\sim\mathrm{Beta}(1,b)\). Write
\[
\mu_b=\frac1{b+1},\qquad v_b=\frac{b}{(b+1)^2(b+2)}.
\]
There is a unique constant
\[
b_\star=3.7534772184455018\ldots
\]
such that the variance-scale Gaussian right-tail bound
\[
\Pr\{X_b-\mu_b\ge \varepsilon\}\le
\exp\!\left(-\frac{\varepsilon^2}{2v_b}\right)
\qquad(\varepsilon\ge0)
\]
holds for every deviation if and only if \(0<b\le b_\star\).

For \(b>2\), define
\[
t_b=\frac12\left(1+\sqrt{\frac{b-2}{b+2}}\right),
\qquad
H(b)=\log\!\frac{b+1}{b}-\log(1-t_b)-\frac{b+2}2t_b^2.
\]
Then \(b_\star\) is the unique zero of \(H\) on \((2,\infty)\). If \(b>b_\star\), the bound fails at the explicit deviation
\[
\varepsilon_b=\frac{b}{b+1}t_b.
\]
Thus an asymmetric beta law can have a variance-sharp Gaussian bound on its heavier right tail even though it is not strictly sub-Gaussian in the moment-generating-function sense.

## Assumptions and scope
The claim concerns the exact one-sided probability tail of the one-parameter family \(\mathrm{Beta}(1,b)\), not an MGF bound and not a two-sided concentration inequality. The parameter \(b\) is any positive real number. For deviations beyond the upper support endpoint the left side is zero, so only \(0\le\varepsilon<b/(b+1)\) needs analysis.

## Proof
Put
\[
q_b=\frac{b}{b+1},\qquad t=\frac{\varepsilon}{q_b}\in[0,1).
\]
The exact survival function of \(X_b\) is \(\Pr\{X_b\ge x\}=(1-x)^b\). Therefore
\[
\Pr\{X_b-\mu_b\ge\varepsilon\}=(q_b-\varepsilon)^b=[q_b(1-t)]^b.
\]
Also
\[
\frac{\varepsilon^2}{2v_b}=\frac{b(b+2)}2t^2.
\]
After taking logarithms and dividing by \(b\), the desired inequality is equivalent to
\[
f_b(t):=\log\!\frac{b+1}{b}-\log(1-t)-\frac{b+2}2t^2\ge0
\qquad(0\le t<1).
\]
Its derivative is
\[
f_b'(t)=\frac{1-(b+2)t(1-t)}{1-t}.
\]
If \(0<b\le2\), then \(t(1-t)\le1/4\) gives \(f_b'(t)\ge0\), hence \(f_b(t)\ge f_b(0)=\log((b+1)/b)>0\).

Now suppose \(b>2\). The two critical points solve \(t(1-t)=1/(b+2)\). They are
\[
t_b^- =\frac12\left(1-\sqrt{\frac{b-2}{b+2}}\right),
\qquad
t_b^+ =\frac12\left(1+\sqrt{\frac{b-2}{b+2}}\right).
\]
The derivative is positive on \((0,t_b^-)\), negative on \((t_b^-,t_b^+)\), and positive on \((t_b^+,1)\). Thus \(t_b^-\) is a local maximum and \(t_b^+=t_b\) is the only interior local minimum. Since \(f_b(0)>0\) and \(f_b(t)\to+\infty\) as \(t\uparrow1\), the inequality holds for all \(t\) exactly when \(H(b)=f_b(t_b)\ge0\).

The function \(H\) is strictly decreasing. Indeed, because \(f_b'(t_b)=0\), differentiation along the minimizing critical point gives
\[
H'(b)=\frac{\partial f_b}{\partial b}(t_b)
=-\frac1{b(b+1)}-\frac{t_b^2}2<0.
\]
As \(b\downarrow2\),
\[
H(b)\longrightarrow \log 3-\frac12>0.
\]
Also \(t_b>1/2\) and \((1-t_b)t_b=1/(b+2)\), so \(-\log(1-t_b)<\log(b+2)\); hence
\[
H(b)<\log\!\frac{b+1}{b}+\log(b+2)-\frac{b+2}8\longrightarrow-\infty.
\]
Continuity and strict monotonicity therefore give one and only one root \(b_\star\). The numerical bracket in the verification artifact gives
\[
3.75347721<b_\star<3.75347722.
\]
For \(b>b_\star\), \(H(b)<0\), so choosing \(t=t_b\), equivalently \(\varepsilon=\varepsilon_b\), gives a strict counterexample to the variance-scale Gaussian tail bound.

## Verification
The proof is analytic and uses only the elementary survival function of \(\mathrm{Beta}(1,b)\). The accompanying checker independently evaluates \(H\) at the endpoints of the stated decimal bracket, checks the critical-point identity, and stress-tests the transformed inequality on a fine grid for representative parameters on both sides of the transition. These finite computations support the numerical location only; the all-\(b\), all-deviation statement follows from the derivative and monotonicity argument above.

## Relationship to prior work
Marchal and Arbel determine the optimal MGF proxy variance for general beta distributions and prove that \(\mathrm{Beta}(\alpha,\beta)\) is strictly sub-Gaussian exactly in the symmetric case \(\alpha=\beta\). That statement is stronger in transform space but answers a different question: it does not classify when one exact one-sided tail is bounded by the Gaussian exponent using the true variance.

Skorski derives variance-matched Bernstein-type bounds for beta laws. On the right tail with \(\beta\ge\alpha\), his bound introduces a positive linear Bernstein correction and his numerical discussion explicitly notes room for improvement at larger deviations. In the specialization \(\alpha=1\), the present result gives a sharp phase diagram for when that linear correction is unnecessary for the exact right-tail probability, despite asymmetry.

Zhang and Zhou establish matching-order upper and lower beta tail bounds with universal constants. Their results concern non-asymptotic rate equivalence and do not give the exact variance-scale threshold above.

## Limitations
The result is specific to the \(\mathrm{Beta}(1,b)\) family and to the right tail. It does not determine the optimal Bernstein scale when \(b>b_\star\), does not imply MGF strict sub-Gaussianity, and does not classify general \(\mathrm{Beta}(\alpha,\beta)\) parameters. The originality comparison cannot exclude an equivalent statement hidden under different terminology or in an unindexed source.

## References
1. O. Marchal and J. Arbel, *On the sub-Gaussianity of the Beta and Dirichlet distributions*, Electronic Communications in Probability 22 (2017), DOI 10.1214/17-ECP92, arXiv:1705.00048.
2. M. Skorski, *Bernstein-type bounds for beta distribution*, Modern Stochastics: Theory and Applications 10 (2023), 211–228, DOI 10.15559/23-VMSTA223, arXiv:2101.02094.
3. A. R. Zhang and Y. Zhou, *On the Non-asymptotic and Sharp Lower Tail Bounds of Random Variables*, Stat 9 (2020), e314, DOI 10.1002/sta4.314, arXiv:1810.09006.
