# Sharp fifth-moment excess per unit skewness excess for nonnegative laws

## Finding
Let \(X\) be any nonnegative real random variable with mean \(\mu>0\), positive finite variance, and finite fifth moment. Define \(Y=X/\mu\), \(v=\operatorname{Var}(X)/\mu^2>0\), and \(M_j=\mathbb E[(Y-1)^j]\). Introduce the endpoint-law moments
\[
B_3(v)=v(v-1),\qquad B_5(v)=v(v-1)(v^2+1).
\]
Then the following *sharp two-moment refinement* holds for every real \(v>0\):
\[
\boxed{\ M_5-B_5(v)\ \ge\ C(v)\bigl(M_3-B_3(v)\bigr)\ \ge\ 0\ },
\qquad
C(v)=\begin{cases}
2v^2-v+\tfrac34,&0<v\le\tfrac32,\\
3v^2-4v+3,&v\ge\tfrac32.
\end{cases}
\]
The displayed coefficient \(C(v)\) is the *largest possible* coefficient for each fixed \(v\) among all nonnegative laws with these first two moments. Equality in the first inequality holds exactly for the distribution assigning mass \(v/(1+v)\) to \(0\) and mass \(1/(1+v)\) to \(1+v\) for \(Y\). In particular, the sharp dependence has a transition at \(v=3/2\), where the optimal perturbation location reaches the support endpoint.

## Assumptions and scope
The support may be arbitrary in \([0,\infty)\), including atoms, continuous components, gaps, and unbounded right tails. No regularity or unimodality is assumed. The mean is positive, the variance is strictly positive, and \(\mathbb E X^5<\infty\). The result is invariant under positive rescaling of \(X\). Sharpness is a supremum over perturbations: except for the two-point endpoint law, no different distribution attains equality.

## Proof
**1. Normalization and exact identity.** We have \(\mathbb EY=1\) and \(\mathbb EY^2=1+v\). Write \(a=1+v\). Since \(\mathbb E[Y(Y-a)]=0\), direct expansion gives
\[
M_3-B_3(v)=\mathbb E[Y(Y-a)^2].\tag{1}
\]
Introduce the quadratic
\[
Q_v(y)=y^2+(2v-3)y+3v^2-4v+3.\tag{2}
\]
The polynomial \(H_v(y)=(y-1)^5-y(y-a)^2Q_v(y)\) has degree at most two; its coefficients in increasing powers of \(y\) are
\[
-1,\quad -3v^4-2v^3+2v^2-2v+2,\quad 4v^3-3v^2+2v-1.
\]
Therefore \(\mathbb EH_v(Y)=B_5(v)\) using exactly the first two moment constraints. It follows that
\[
M_5-B_5(v)=\mathbb E\bigl[Y(Y-a)^2Q_v(Y)\bigr].\tag{3}
\]
This identity is exact for every law in scope; it does not approximate higher moments.

**2. Pointwise minimization on the support.** Complete the square:
\[
Q_v(y)=\left(y-\left(\tfrac32-v\right)\right)^2
       +2v^2-v+\tfrac34.
\]
For \(0<v\le3/2\), the vertex \(y_v=3/2-v\) lies in \([0,\infty)\), so the first expression for \(C(v)\) is the exact minimum of \(Q_v\) on that half-line. For \(v\ge3/2\), the vertex is nonpositive and the minimum occurs at \(y=0\), giving \(Q_v(0)=3v^2-4v+3\). Both expressions are positive (the first is \(2(v-1/4)^2+5/8\)); they coincide at \(v=3/2\). Multiplying \(Q_v(Y)\ge C(v)\) by the nonnegative factor \(Y(Y-a)^2\), taking expectations, and using (1)–(3) proves the stated chain of inequalities.

**3. Best possible constant at every variance ratio.** Fix \(v>0\), put \(a=1+v\), and choose any fixed \(y>0\) with \(y\ne a\). For sufficiently small \(\varepsilon>0\), define
\[
 b_\varepsilon=\frac{a-\varepsilon y^2}{1-\varepsilon y},\qquad
 \beta_\varepsilon=\frac{1-\varepsilon y}{b_\varepsilon},\qquad
 \alpha_\varepsilon=1-\varepsilon-\beta_\varepsilon.
\]
These are positive near \(\varepsilon=0\), since \(\beta_0=1/a\), \(\alpha_0=v/a\), and \(b_0=a\). Let \(Y_\varepsilon\) put masses \(\alpha_\varepsilon,\varepsilon,\beta_\varepsilon\) at \(0,y,b_\varepsilon\), respectively. Direct substitution gives \(\mathbb EY_\varepsilon=1\) and \(\mathbb EY_\varepsilon^2=a\) exactly. Since \(b_\varepsilon=a+O(\varepsilon)\), equations (1) and (3) imply
\[
\begin{aligned}
M_3(Y_\varepsilon)-B_3(v)&=\varepsilon y(y-a)^2+O(\varepsilon^2),\\
M_5(Y_\varepsilon)-B_5(v)&=\varepsilon y(y-a)^2Q_v(y)+O(\varepsilon^2).
\end{aligned}
\]
Hence the ratio of these positive excesses tends to \(Q_v(y)\). Sending \(y\) toward the minimizer \(\max\{0,3/2-v\}\), while avoiding \(y=a\), proves that no coefficient larger than \(C(v)\) can work uniformly. This includes the exceptional case \(v=1/4\), where the minimizing location equals \(a\), because it can be approached by other positive \(y\); and includes \(v\ge3/2\) by taking \(y\downarrow0\).

**4. Equality.** If \(M_3-B_3(v)=0\), (1) forces \(Y\in\{0,a\}\) almost surely, and the first two moments determine the stated two-point law. Conversely this law makes both excesses zero. If the excess is positive, equality in the first inequality would require \(Y(Y-a)^2(Q_v(Y)-C(v))=0\) almost surely. The possible support would be \(\{0,a,y_v\}\) (with \(y_v>0\) only in the interior-vertex regime). But \(\mathbb E[Y(Y-a)]=0\) and \(y_v(y_v-a)\ne0\) whenever \(y_v\notin\{0,a\}\) force zero mass at that third location. Thus equality is impossible for any non-endpoint law.

## Verification
Run `python3 verify_moments.py` with Python 3 and no third-party packages. It uses exact polynomial coefficient arithmetic to verify the degree-five factorization, the quadratic expectation, and both vertex/boundary factorizations. It also checks exact first and second moments, positivity of the weights, both excesses, and the residual identity in 32 rational three-atom laws across eight variance ratios. The script's output gives check counts and sample exact rational slopes. The universal proof is the algebra and the explicit \(\varepsilon\to0\) construction above, **not** finite testing.

## Relationship to prior work
Meer and Weeks, *Bounded distributions place limits on skewness and larger moments* (first public version August 9, 2023), state the unrefined fifth-moment endpoint bound as a conjecture and explicitly ask about relations between different standardized moments. Their final February 2024 article still labels the fifth-moment bound conjectural. The weaker endpoint lower bound follows from the finding when the third-moment excess is dropped, but the *new assertion* is the globally optimal positive coefficient linking the third and fifth **excesses**, including its piecewise transition and sharpness proof.

Rowe's 1988 constant-sign-derivative transformation bounds concern extrema of one transformed expectation at fixed mean and variance; they do not state this sharp two-moment-excess relationship. In particular, the transformed function \((y-1)^5-C(v)(y-1)^3\) has third derivative \(60(y-1)^2-6C(v)\), which changes sign on the support, so the constant-sign-third-derivative condition in Rowe's method does not directly supply the claim. Castañeda-Leyva, Rodríguez-Narciso, Hernández-Quintero and Pérez (2023) analyze reciprocal and log-convex inequalities for *raw nonnegative moments*; their inspected results do not give the stated sharp comparison of **centered third and fifth moment deficits**. Classical moment cone positivity motivates the polynomial method and is not presented as novel in itself.

## Limitations
The result is not the full lower envelope of the fifth moment for every separately fixed value of the third moment; it gives the sharp universal **linear** improvement from the common endpoint minimum at fixed mean and variance. It neither classifies higher odd moments nor provides a fixed-coefficient estimate independent of \(v\) stronger than the stated profile. Bibliographic priority remains subject to checking equivalent formulations in older moment-problem literature; no independent expert validation has been performed.

## References
1. D. J. Meer and E. R. Weeks, *Bounded distributions place limits on skewness and larger moments*, arXiv:2308.05006, first submitted 2023-08-09, https://arxiv.org/abs/2308.05006 ; PLOS ONE 19 (2024), e0297862, https://doi.org/10.1371/journal.pone.0297862 .
2. N. C. Rowe, *Absolute bounds on the mean and standard deviation of transformed data for constant-sign-derivative transformations*, SIAM Journal on Scientific and Statistical Computing 9 (1988), 1098–1113, https://faculty.nps.edu/ncrowe/unary2.htm .
3. N. Castañeda-Leyva, S. Rodríguez-Narciso, A. Hernández-Quintero, and A. Pérez, *Moment inequalities for nonnegative random variables*, Probability and Mathematical Statistics 43 (2023), 41–61, https://doi.org/10.37190/0208-4147.00106 .
