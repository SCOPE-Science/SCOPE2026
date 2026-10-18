# A sharp interior rate optimum for reciprocal random-action consensus

## Finding

Consider two agents on a reciprocal directed link, updating their probabilities of choosing action 1 from independently sampled Bernoulli actions. Although they reach the same random binary opinion almost surely for each fixed relaxation coefficient \(0<\alpha<1\), the exact **expected squared distance to this terminal consensus** has asymptotic rate

\[
\lambda_+(\alpha)=1-2\alpha+\frac32\alpha^2+\frac{\alpha}{2}\sqrt{17\alpha^2-32\alpha+16}.
\]

For every initial state except the two already-unanimous binary states, this rate is attained, not merely bounded above:

\[
\mathbb E\!\left[(X_1(t)-Z)^2+(X_2(t)-Z)^2\right]
\sim C(X(0),\alpha)\lambda_+(\alpha)^t,
\qquad C(X(0),\alpha)>0.
\]

Here \(Z\in\{0,1\}\) is the common almost-sure limit. The rate has a unique minimizer over \(0<\alpha<1\):

\[
\boxed{\alpha_*=\frac{47+\sqrt{33}}{68}},\qquad
\boxed{\lambda_+(\alpha_*)=\frac{369+99\sqrt{33}}{1156}}.
\]

Numerically these are approximately \(0.7756553330\) and \(0.8111692924\), respectively. In particular, using stronger action influence is not always faster. The expected quadratic rate deteriorates toward 1 at **both** the zero-influence and unit-influence endpoints.

## Assumptions and scope

Fix deterministic initial \(X(0)=(p,q)\in[0,1]^2\). At each integer time \(t\ge0\), conditional on the current opinions, the two actions \(A_1(t)\) and \(A_2(t)\) are independent with

\[
\mathbb P(A_i(t)=1\mid X(t))=X_i(t).
\]

The simultaneous update is

\[
X_1(t+1)=(1-\alpha)X_1(t)+\alpha A_2(t),\qquad
X_2(t+1)=(1-\alpha)X_2(t)+\alpha A_1(t),
\]

with one common fixed \(0<\alpha<1\). This is the random-actions rule of Leshem and Scaglione for the two-vertex reciprocal trust matrix \(W=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\). Actions are sampled afresh conditionally independently at each update. We do not assume deterministic agents, a stubborn agent, asynchronous updates, or additional self-loop trust.

For every time define two nonnegative expected second moments

\[
U_t=\frac12\,\mathbb E\!\left[X_1(t)(1-X_1(t))+X_2(t)(1-X_2(t))\right],\qquad
V_t=\frac14\,\mathbb E[(X_1(t)-X_2(t))^2].
\]

## Proof

**1. Closed exact moment system.** Write \(m=(X_1+X_2)/2\), \(d=(X_1-X_2)/2\), and let \(u\) and \(v\) denote the corresponding instantaneous (unaveraged) quantities in the definitions of \(U_t\) and \(V_t\). Then \(u=m(1-m)-d^2\), \(v=d^2\). Conditional expectations satisfy

\[
\mathbb E[m'\mid X]=m,\quad
\mathbb E[d'\mid X]=(1-2\alpha)d,\quad
\operatorname{Var}(m'\mid X)=\operatorname{Var}(d'\mid X)=\frac{\alpha^2}{2}u.
\]

Because \(m'=(1-\alpha)m+\alpha(A_1+A_2)/2\) and \(d'=(1-\alpha)d-\alpha(A_1-A_2)/2\), these follow directly from conditional Bernoulli independence. In particular,

\[
\begin{split}
\mathbb E[v'\mid X]&=(1-2\alpha)^2v+\frac{\alpha^2}{2}u,\\
\mathbb E[u'\mid X]&=(1-\alpha^2)u+4\alpha(1-\alpha)v.
\end{split}
\]

Averaging gives the **exact** recursion for every \(t\ge0\):

\[
\begin{pmatrix}U_{t+1}\\V_{t+1}\end{pmatrix}
=M_\alpha\begin{pmatrix}U_t\\V_t\end{pmatrix},\qquad
M_\alpha=
\begin{pmatrix}
1-\alpha^2&4\alpha(1-\alpha)\\
\alpha^2/2&(1-2\alpha)^2
\end{pmatrix}.
\]

The eigenvalues of \(M_\alpha\) are

\[
\lambda_\pm=1-2\alpha+\frac32\alpha^2\pm\frac\alpha2\sqrt{17\alpha^2-32\alpha+16}.
\]

**2. Strict contraction and an attained asymptotic rate.** For \(0<\alpha<1\), \(M_\alpha\) has strictly positive off-diagonal entries and nonnegative diagonal entries. Furthermore, both diagonal entries are less than 1 and

\[
\det(I-M_\alpha)=2\alpha^3(1-\alpha)>0.
\]

These facts imply its Perron eigenvalue satisfies \(0<\lambda_+(\alpha)<1\). Perron–Frobenius also gives \(\lvert\lambda_-\rvert<\lambda_+\) and strictly positive left and right Perron eigenvectors. For any deterministic initial opinions other than \((0,0)\) and \((1,1)\), the vector \((U_0,V_0)\) is nonzero and nonnegative. Hence for every strictly positive row vector \(w\),

\[
wM_\alpha^t(U_0,V_0)^\mathsf T\sim c_w\lambda_+(\alpha)^t,\qquad c_w>0.
\]

**3. Binary consensus and terminal quadratic error.** The average \(m_t=(X_1(t)+X_2(t))/2\) is a bounded martingale and therefore converges almost surely to some \(Z\in[0,1]\). Since \(\mathbb E[d_t^2]=V_t\to0\) at a summable geometric rate, Markov's inequality and Borel–Cantelli imply \(d_t\to0\) almost surely. Also \(\mathbb E[m_t(1-m_t)]=U_t+V_t\to0\); bounded convergence then forces \(Z(1-Z)=0\) almost surely. Thus both opinions converge almost surely to the same \(Z\in\{0,1\}\). Uniform integrability of the bounded martingale gives \(\mathbb E[Z\mid\mathcal F_t]=m_t\).

Conditioning on the current opinions and expanding the squares yields

\[
\begin{split}
\mathbb E[(X_1(t)-Z)^2+(X_2(t)-Z)^2\mid\mathcal F_t]
&=2m_t(1-m_t)+2d_t^2.
\end{split}
\]

Taking expectations and using \(\mathbb E[m_t(1-m_t)]=U_t+V_t\) produces the **exact finite-time identity**

\[
\mathbb E[(X_1(t)-Z)^2+(X_2(t)-Z)^2]=2U_t+4V_t.
\]

By step 2, its positive asymptotic rate is \(\lambda_+\). The limit's distribution is \(\mathbb P(Z=1)=(p+q)/2\), independently of \(\alpha\).

**4. Unique optimal coefficient.** Put \(h(\alpha)=\sqrt{17\alpha^2-32\alpha+16}\). Direct differentiation of the explicit eigenvalue yields

\[
\lambda_+'(\alpha)=\frac{(3\alpha-2)h(\alpha)+17\alpha^2-24\alpha+8}{h(\alpha)}.
\]

A zero of this derivative in \((0,1)\) must satisfy, after squaring,

\[
-4\alpha(\alpha-1)(34\alpha^2-47\alpha+16)=0.
\]

The two interior candidates are \(\alpha_\pm=(47\pm\sqrt{33})/68\). The smaller lies strictly between \(3/5\) and \(2/3\), where both terms in the numerator of \(\lambda_+'\) are negative; it is a spurious root introduced by squaring. The larger lies between \(3/4\) and \(4/5\), where the two terms have opposite signs and the squared equality gives a genuine zero. Since \(\lambda_+'<0\) close to zero and \(\lambda_+'(1)=2>0\), this is the unique global minimizer. Substitution into the characteristic equation and selection of the larger eigenvalue gives the stated exact minimum. The endpoint limits are \(\lambda_+(0)=\lambda_+(1)=1\).

As an additional distinction, the Perron root obeys \(\lambda_+>1-\alpha^2>1-\alpha\): the ensemble quadratic rate is strictly slower than the idealized single-run late descent factor \(1-\alpha\).

## Verification

The accompanying self-contained Python/SymPy program `code/verify_random_actions.py` symbolically checks both conditional-moment identities, the characteristic polynomial, the derivative formula, the stationary-point polynomial and the exact optimal eigenvalue. It additionally uses direct enumeration of Bernoulli branches to check the moment recurrence through three updates on 64 exact initial-parameter choices (256 time-index comparisons). Its exact symbolic and rational checks passed. These calculations corroborate the algebraic steps; almost-sure convergence and the strict universal minimizer are consequences of the analytical proof above, not of finite enumeration.

## Relationship to prior work

Leshem and Scaglione's *The Impact of Random Actions on Opinion Dynamics* (first public preprint April 5, 2017; IEEE journal 2018), Section I and the discussion of numerical rates in Section III, establish the random-actions mechanism and qualitative herding. Their rate discussion concerns the final rapid descent along trajectories when common actions recur, with factor \(1-\alpha\); it does not provide the global expected quadratic terminal-error rate or optimize it across the full admissible coefficient interval. Abrahamsson, Danev and Larsson's *Strong Convergence of a Random Actions Model in Opinion Dynamics* (preprint January 29, 2024), Sections II–IV and its appendix, establishes rigorous almost-sure and moment convergence for general networks, again without this exact two-agent second-moment spectrum or the sharp interior optimizer. The exact 2-by-2 calculation addresses a different quantitative question and is not implied by either qualitative convergence theorem.

Searches for reciprocal/two-agent Bernoulli random actions, optimal gain, second-moment spectral rates and equivalent voter-model formulations identified no source containing this complete statement. This is evidence from a bounded search, not a guarantee of global novelty; analogous two-state stochastic-consensus formulas elsewhere may exist. A related 2024 thesis by Abrahamsson was identified, but its full text could not be retrieved in this assessment; its available chapter excerpt reproduces the general random-action model and does not establish coverage.

## Limitations

The theorem concerns the **two-agent reciprocal link**, independent Bernoulli action sampling, simultaneous updates, fixed common \(0<\alpha<1\), and mean squared error **to the random terminal binary consensus**. It does not assert that the exact optimizer applies to a general network, asynchronous actions, or a chosen deterministic target. At \(\alpha=1\) the theorem no longer claims almost-sure consensus: for example, the initial state \((1,0)\) swaps deterministically forever. Exact consensus is generally approached asymptotically and is not attained at finite time when both opinions lie strictly between zero and one. No claim of independent verification or literature exhaustiveness is made.

## References

- A. Leshem and A. Scaglione, *The Impact of Random Actions on Opinion Dynamics*, arXiv:1704.01660, first posted April 5, 2017; *IEEE Transactions on Signal and Information Processing over Networks* 4 (2018), 576–584. Open author manuscript: https://www.eng.biu.ac.il/leshema/files/2018/01/TSIPN1_final-with-bios.pdf ; DOI: https://doi.org/10.1109/TSIPN.2018.2797800 .
- O. Abrahamsson, D. Danev, and E. G. Larsson, *Strong Convergence of a Random Actions Model in Opinion Dynamics*, arXiv:2401.16574, first posted January 29, 2024; *IEEE Transactions on Signal and Information Processing over Networks* 10 (2024), 147–161. Repository postprint: https://www.diva-portal.org/smash/get/diva2:1846986/FULLTEXT01.pdf ; DOI: https://doi.org/10.1109/TSIPN.2024.3361373 .
- O. Abrahamsson, *On Aggregation and Dynamics of Opinions in Complex Networks* (2024), DOI: https://doi.org/10.3384/9789180755993 ; identified as relevant related literature, full document not retrieved for this comparison.
