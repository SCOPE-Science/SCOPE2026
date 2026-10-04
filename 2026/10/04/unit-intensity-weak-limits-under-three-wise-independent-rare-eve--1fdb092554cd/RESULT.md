# Unit-intensity weak limits under three-wise independent rare events
## Finding
Let, for each row, \(X_{n,1},\ldots,X_{n,m_n}\) be Bernoulli variables that are three-wise independent within the row. Put \(p_{n,i}=\Pr(X_{n,i}=1)\) and \(S_n=\sum_i X_{n,i}\). Assume
\[
\max_i p_{n,i}\longrightarrow0,
\qquad
\sum_i p_{n,i}\longrightarrow1.
\]
Write \((x)_r=x(x-1)\cdots(x-r+1)\). Then the weak subsequential limits of \(S_n\) are exactly the laws on \(\mathbb Z_{\ge0}\) satisfying
\[
\mathbb EY=1,
\qquad
\mathbb E(Y)_2=1,
\qquad
\mathbb E(Y)_3\le1.
\]
Equivalently, the first two conditions say \(\mathbb EY=1\) and \(\operatorname{Var}(Y)=1\). Conversely, every such law is realizable by exchangeable three-wise independent rows of exactly \(n\) Bernoulli variables, each with marginal \(\operatorname{Bernoulli}(1/n)\), for all sufficiently large \(n\) along one triangular array converging to \(Y\).

Thus moving from pairwise to three-wise independence makes the limiting variance rigid but still permits loss of the third factorial moment. The first moment that can escape to vanishing-probability large-count events moves from order two to order three.

## Assumptions and scope
Three-wise independence means that every subfamily of at most three coordinates is mutually independent. No identical-marginal assumption is imposed in the necessity direction. The equal marginal \(1/n\) is used only in the realization direction.

The intensity is fixed at the canonical value \(1\). This is the value singled out by the pairwise predecessor as the simplest regime in which the independent Poisson limit can fail maximally. No classification for arbitrary intensity or for four-wise and higher independence is claimed.

## Proof
For \(r\in\{1,2,3\}\), three-wise independence gives
\[
\mathbb E(S_n)_r
=
\sum_{i_1,\ldots,i_r\ \mathrm{distinct}}
 p_{n,i_1}\cdots p_{n,i_r}.
\]
For \(r=1\) the limit is \(1\). For \(r=2\),
\[
\mathbb E(S_n)_2
=
\left(\sum_i p_{n,i}\right)^2-
\sum_i p_{n,i}^2
\longrightarrow1,
\]
because \(\sum_i p_{n,i}^2\le(\max_i p_{n,i})\sum_i p_{n,i}\to0\). For \(r=3\),
\[
\mathbb E(S_n)_3
=
\left(\sum_i p_{n,i}\right)^3
-3\left(\sum_i p_{n,i}\right)\left(\sum_i p_{n,i}^2\right)
+2\sum_i p_{n,i}^3
\longrightarrow1.
\]
Since
\[
S_n^3=(S_n)_3+3(S_n)_2+S_n,
\]
the third moments are uniformly bounded. Hence \(S_n\) and \(S_n^2\) are uniformly integrable. If \(S_n\Rightarrow Y\) along a subsequence, then \(Y\) is nonnegative and integer-valued, and uniform integrability yields
\[
\mathbb EY=1,
\qquad
\mathbb EY^2=2,
\]
so \(\mathbb E(Y)_2=1\). For the third factorial moment, use the nonnegative continuous function
\[
g(x)=\max\{0,x(x-1)(x-2)\}.
\]
It equals \((x)_3\) at every nonnegative integer. Portmanteau therefore gives
\[
\mathbb E(Y)_3
\le
\liminf_n \mathbb E(S_n)_3
=1.
\]
This proves necessity.

For sufficiency, first consider a finitely supported target law \(Q\) on \(\mathbb Z_{\ge0}\) such that
\[
\mathbb EQ=1,
\qquad
\mathbb E(Q)_2=1,
\qquad
c:=\mathbb E(Q)_3<1,
\]
and such that \(Q\) gives positive mass to \(0,1,2\). Take \(n\) larger than the support of \(Q\), and set
\[
a_{3,n}=\frac{(n-1)(n-2)}{n^2},
\qquad
\varepsilon_n=
\frac{a_{3,n}-c}{n(n-1)(n-2)}.
\]
For all sufficiently large \(n\), \(\varepsilon_n>0\). Add mass \(\varepsilon_n\) at \(n\), and change the masses at \(0,1,2\) by
\[
\delta_{2,n}
=-\frac1{2n}-\frac{n(n-1)}2\varepsilon_n,
\]
\[
\delta_{1,n}
=\frac1n+n(n-2)\varepsilon_n,
\]
\[
\delta_{0,n}
=-\frac1{2n}-\frac{(n-1)(n-2)}2\varepsilon_n.
\]
These corrections satisfy
\[
\delta_{0,n}+\delta_{1,n}+\delta_{2,n}+\varepsilon_n=0,
\]
\[
\delta_{1,n}+2\delta_{2,n}+n\varepsilon_n=0,
\]
\[
2\delta_{2,n}+n(n-1)\varepsilon_n=-\frac1n.
\]
Therefore the resulting count law \(K_n\) obeys exactly
\[
\mathbb EK_n=1,
\qquad
\mathbb E(K_n)_2=1-\frac1n,
\qquad
\mathbb E(K_n)_3=\frac{(n-1)(n-2)}{n^2}.
\]
Because \(\varepsilon_n=O(n^{-3})\), all three \(\delta\)-corrections are \(O(n^{-1})\). The positive masses of \(Q\) at \(0,1,2\) therefore make \(K_n\) a genuine probability law for all sufficiently large \(n\), and \(K_n\to Q\) in total variation.

Conditional on \(K_n=k\), choose a uniformly random \(k\)-subset of \([n]\), and let its membership indicators be \(X_{n,1},\ldots,X_{n,n}\). Then for every \(r\in\{1,2,3\}\) and every \(r\) distinct coordinates,
\[
\Pr(X_{n,i_1}=\cdots=X_{n,i_r}=1)
=
\frac{\mathbb E(K_n)_r}{(n)_r}
=
\frac1{n^r}.
\]
Inclusion-exclusion then gives the full product law on every subfamily of at most three coordinates. Thus the row is exchangeable, three-wise independent, and has marginal \(1/n\), while its sum is exactly \(K_n\).

It remains to remove the finite-support and strict-inequality assumptions. Introduce the reference law \(R\) on \(\{0,1,2,3\}\) with masses
\[
\Pr(R=0)=\frac5{12},\quad
\Pr(R=1)=\frac14,\quad
\Pr(R=2)=\frac14,\quad
\Pr(R=3)=\frac1{12}.
\]
It satisfies
\[
\mathbb ER=1,
\qquad
\mathbb E(R)_2=1,
\qquad
\mathbb E(R)_3=\frac12.
\]
Given any admissible \(Y\), mix it with \(R\): \(Y^{(\eta)}=(1-\eta)Y+\eta R\). The first two factorial moments remain one, the third becomes strictly less than one, and the masses at \(0,1,2\) are all positive. Since \(\mathbb E(Y)_3\le1\) and the first two factorial moments are finite, \(Y\) has finite third moment. Truncate \(Y^{(\eta)}\) above a large \(M\). If the deleted tail has mass \(t_0\), first moment \(t_1\), and second factorial moment \(t_2\), restore those three quantities by adding at \(0,1,2\), respectively,
\[
t_0-t_1+\frac{t_2}{2},
\qquad
t_1-t_2,
\qquad\frac{t_2}{2}.
\]
For fixed \(\eta>0\), these corrections tend to zero as \(M\to\infty\), so positivity is eventually preserved. The resulting finite law has the same first two factorial moments, and its third factorial moment is the mixed law's third factorial moment minus the deleted tail contribution, hence is still strictly below one.

Choose \(\eta\downarrow0\), then \(M\uparrow\infty\), and finally let the finite-law index grow slowly with \(n\). The preceding exact construction then gives one triangular array with \(S_n\Rightarrow Y\). This proves sufficiency.

## Verification
The necessity calculation uses exact factorial-moment identities and the rare-event bound \(\sum_i p_{n,i}^2\le(\max_i p_{n,i})\sum_i p_{n,i}\). The passage of first and second moments is justified by the uniformly bounded third moment, not by weak convergence alone. The third-factorial inequality uses lower semicontinuity and is intentionally one-sided.

For the realization direction, the three displayed correction identities independently verify preservation of total mass and mean and the exact decrement \(1/n\) in the second factorial moment. The added atom at \(n\) supplies exactly \(a_{3,n}-c\) in the third factorial moment. The uniform-subset construction converts those three count moments into the required joint all-one probabilities for every set of at most three coordinates; Bernoulli inclusion-exclusion then gives three-wise independence.

No finite computation is used as evidence for the infinite theorem.

## Relationship to prior work
The published record *Weak-limit classification for rare pairwise-independent Bernoulli sums* proves that, under pairwise independence and rare-event scaling with limiting intensity \(\lambda\), the weak limits are exactly the nonnegative-integer laws with mean \(\lambda\) and variance at most \(\lambda\). Its limitations explicitly leave higher-wise independence as a different moment problem. The present theorem resolves the first higher-wise case at the canonical unit intensity and shows a qualitative shift: the variance can no longer leak, while the third factorial moment can.

Ramachandra and Natarajan prove an exact finite-\(n\) reduction for identically distributed \(t\)-wise independent Bernoulli variables: their Corollary 4.2 identifies feasible count laws through the first \(t\) binomial moments and uses this to optimize tail probabilities. That finite moment formulation supplies relevant background but does not state the weak-limit classification above or the asymptotic realization of every law satisfying the three limiting constraints. Berend, Ernst, Kontorovich, and Kumar study exact extremal all-one probabilities under \(k\)-wise independence, again a different finite-dimensional objective.

## Limitations
The theorem treats only limiting intensity \(1\) and only three-wise independence. It classifies scalar count limits, not point-process limits or the locations of rare events. It does not optimize support size or sampling complexity of the realizing rows. Older finite-exchangeability, discrete moment, orthogonal-array, or limited-independence literature could contain an equivalent asymptotic formulation under different terminology; this remains the main originality risk.

## References
1. *Weak-limit classification for rare pairwise-independent Bernoulli sums*, public record SCOPE-20260920-81d03613e25b, first public 2026-09-20.
2. A. K. Ramachandra and K. Natarajan, *Tight Probability Bounds with Pairwise Independence*, SIAM Journal on Discrete Mathematics 37 (2023), arXiv:2006.00516, DOI 10.1137/21M1408294.
3. D. Berend, P. A. Ernst, A. Kontorovich, and R. Kumar, *Exact expressions for the maximal probability that all \(k\)-wise independent bits are 1*, arXiv:2407.18688.
4. J. P. Schmidt, A. Siegel, and A. Srinivasan, *Chernoff--Hoeffding Bounds for Applications with Limited Independence*, SIAM Journal on Discrete Mathematics 8 (1995), 223--250, DOI 10.1137/S089548019223872X.
5. L. Le Cam, *An approximation theorem for the Poisson binomial distribution*, Pacific Journal of Mathematics 10 (1960), 1181--1197.
