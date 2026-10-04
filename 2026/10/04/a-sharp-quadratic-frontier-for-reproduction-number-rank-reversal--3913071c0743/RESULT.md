# A sharp quadratic frontier for reproduction-number rank reversals in household epidemics
## Finding
For the proportionate-global-mixing household SIR model of Ball and Critcher, write \(r=R_*\) and let \(a>0\) be the mean number of global contacts made by a typical primary case. Their reduction gives \(R_I\) as the unique positive root of
\[
x^2-a x-(r-a)=0,
\]
with \(0<a\le r\). It follows that
\[
\begin{cases}
\sqrt r<R_I\le r, & r>1,\\
r\le R_I<\sqrt r, & 0<r<1,\\
R_I=1, & r=1.
\end{cases}
\]
Equality \(R_I=r\) holds exactly when \(r-a=0\), equivalently when the individual-based offspring matrix has no effective local-secondary contribution.

For two growing epidemics with prescribed \(r_A=R_{*,A}>r_B=R_{*,B}>1\), these bounds yield a sharp rank-reversal frontier. A reversal \(R_{I,A}<R_{I,B}\) is impossible whenever \(r_A\ge r_B^2\). Conversely, for every
\[
r_B<r_A<r_B^2,
\]
there are admissible single-type household models with those exact \(R_*\) values and \(R_{I,A}<R_{I,B}\). Hence the quadratic boundary is optimal over the model class.

An exact finite witness is \(R_{*,A}=3>2=R_{*,B}\) while \(R_{I,A}<2=R_{I,B}\). Model B has households of size one, mean-one infectious periods, and global contact rate \(2\). Model A has households of size four, mean-one exponential infectious periods, local pairwise infection rate \(2\), and global contact rate \(675/779\). The expected final number infected in a model-A household outbreak initiated by one infective is exactly \(779/225\), so its household reproduction number is exactly \(3\), but its individual reproduction number is below \(2\).

## Assumptions and scope
The setting is the Ball--Critcher stochastic SIR model with one or more individual types, households of finite size within each model, local within-household transmission, and proportionate global mixing. The source defines \(R_*\) as the household-based reproduction number and \(R_I\) as the individual-based reproduction number. Under proportionate mixing its individual-based offspring matrix reduces to
\[
M_I=\begin{pmatrix}a&u^\top\\v&0\end{pmatrix},
\]
where \(a>0\), \(u^\top v\ge0\), and the source proves
\[
u^\top v=R_*-a.
\]
Thus \(0<a\le R_*\). The rank-reversal statement compares two separate admissible models and concerns only the ordering induced by \(R_*\) versus \(R_I\). It does not claim an ordering of outbreak probabilities, final sizes, \(R_0\), vaccination thresholds, or exponential growth rates.

## Proof
Set \(r=R_*\). The source gives
\[
R_I=\frac{a+\sqrt{a^2+4u^\top v}}2
\]
and \(u^\top v=r-a\). Therefore \(R_I\) is the unique positive zero of
\[
p_r(x)=x^2-a x-(r-a).
\]
Since \(p_r(0)=-(r-a)\le0\) and the other root is nonpositive, the sign of \(p_r\) changes from nonpositive to positive at \(R_I\). Evaluate it at the two natural comparison points:
\[
p_r(r)=(r-1)(r-a),
\qquad
p_r(\sqrt r)=a(1-\sqrt r).
\]
If \(r>1\), then \(p_r(\sqrt r)<0\) and \(p_r(r)\ge0\), giving \(\sqrt r<R_I\le r\). If \(0<r<1\), then \(p_r(r)\le0\) and \(p_r(\sqrt r)>0\), giving \(r\le R_I<\sqrt r\). At \(r=1\), direct substitution gives \(p_1(1)=0\), hence \(R_I=1\). For \(r\ne1\), equality at the \(r\)-endpoint occurs exactly when \(r-a=0\).

Now let \(r_A>r_B>1\). If \(r_A\ge r_B^2\), then
\[
R_{I,A}>\sqrt{r_A}\ge r_B\ge R_{I,B},
\]
so reversal is impossible.

For sharpness, suppose \(r_B<r_A<r_B^2\), so \(\sqrt{r_A}<r_B\). Take model B to have one-person households, mean-one infectious periods, and global rate \(r_B\). Then no local secondary case is possible and
\[
R_{*,B}=R_{I,B}=r_B.
\]
For model A, take a single type, all households of size \(n\), mean-one exponential infectious periods, and local pairwise infection rate \(\lambda>0\). Let \(m_n(\lambda)\) be the expected final number infected in a household outbreak started by one infective. Choose the global contact rate
\[
\beta_A=\frac{r_A}{m_n(\lambda)}.
\]
Then exactly \(R_{*,A}=r_A\), while \(a_A=\beta_A\). Starting with \(n-1\) susceptibles and one infective, the probability that the next \(n-1\) events are infections is
\[
\prod_{s=1}^{n-1}\frac{\lambda s}{\lambda s+1},
\]
which tends to one as \(\lambda\to\infty\). Hence \(m_n(\lambda)\to n\) for each fixed \(n\). By first taking \(n\) large and then \(\lambda\) large, \(a_A=r_A/m_n(\lambda)\) can be made arbitrarily small. The positive root of
\[
x^2-a_Ax-(r_A-a_A)=0
\]
therefore approaches \(\sqrt{r_A}<r_B\). For finite sufficiently large \(n\) and \(\lambda\), this gives \(R_{I,A}<r_B=R_{I,B}\). Thus every point below the quadratic boundary admits a reversal.

For the explicit witness, model A has \(n=4\) and \(\lambda=2\). If \(F(s,i)\) is the expected number of future infections from a household state with \(s\) susceptibles and \(i\) infectives, then
\[
F(s,i)=\frac{2s}{2s+1}\bigl(1+F(s-1,i+1)\bigr)+\frac1{2s+1}F(s,i-1),
\]
with \(F(s,0)=F(0,i)=0\). Exact rational recursion gives
\[
m_4(2)=1+F(3,1)=\frac{779}{225}.
\]
Taking \(\beta_A=675/779\) gives \(R_{*,A}=\beta_A m_4(2)=3\). Its polynomial at \(x=2\) is
\[
p_3(2)=1-\frac{675}{779}=\frac{104}{779}>0.
\]
Since \(p_3(0)<0\), its unique positive root satisfies \(R_{I,A}<2\). Model B with one-person households and global rate \(2\) has \(R_{*,B}=R_{I,B}=2\), proving the finite reversal.

## Verification
The identities \(u^\top v=R_*-a\) and the closed formula for \(R_I\) were independently reconstructed from the displayed offspring matrix in the primary source. The endpoint signs above are exact algebra. The finite witness is replayed by `verify.py` using exact rational arithmetic for the household continuous-time Markov chain recursion; it verifies \(m_4(2)=779/225\), \(R_{*,A}=3\), and \(p_3(2)=104/779>0\).

The sharpness argument is analytic rather than experimental: the displayed finite product proves \(m_n(\lambda)\to n\), and continuity of the quadratic root as \(a\downarrow0\) proves existence of finite parameters throughout \(r_B<r_A<r_B^2\).

## Relationship to prior work
Ball and Critcher explicitly note that \(R_*\), although easy to calculate, can be misleading when comparing epidemics with different household structures. Their Theorem 4.1 gives the standard one-model ordering \(R_*\ge R_I>1\) for growing epidemics and the reverse ordering below threshold. Their equations (4.2), (4.5), and (4.6) supply the two scalar identities used here, but they do not state the square-root envelope or the sharp cross-model quadratic rank-reversal frontier.

Ball, Pellis, and Trapman (2016) provide a broad comparison theory for household reproduction numbers and likewise prove the standard \(R_*\) versus \(R_I\) ordering. Full-text inspection of their open preprint found no square-root or quadratic cross-model frontier. The present result is narrower in objects but sharper for the specific comparison problem highlighted by Ball and Critcher.

## Limitations
The result compares \(R_*\) and \(R_I\) only. It does not say that one of two epidemics has larger outbreak probability, larger final size, faster early growth, or a larger vaccination threshold. The square-root endpoint is generally an unattained limit when global contact rates are required to be positive; sharpness means it is approached by finite admissible models, and the reversal boundary itself is exact. Search and source inspection reduce but cannot eliminate the possibility that an equivalent algebraic frontier appeared in older or poorly indexed household-epidemic literature.

## References
1. F. Ball and L. Critcher, “Multitype SIR epidemics among a population partitioned into households with proportionate global mixing,” *Journal of Mathematical Biology* 92, 77 (2026). DOI: 10.1007/s00285-026-02359-5.
2. F. Ball, L. Pellis, and P. Trapman, “Reproduction numbers for epidemic models with households and other social structures II: comparisons and implications for vaccination,” *Mathematical Biosciences* 274 (2016), 108–139. DOI: 10.1016/j.mbs.2016.01.006; arXiv:1410.4469.
