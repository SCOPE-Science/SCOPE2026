# A critical Yaglom law for the open Pelikan random map

## Finding
For every fixed opening parameter \(0<\varepsilon<1\), choose the random-map probability \(p=4/[4+(2-\varepsilon)^2]\) and its complement \(q=1-p\). Let \(\tau\) be the first killing time, for an initial point uniformly distributed on the top dyadic cell and independent random choices. Put \(\lambda=4(2-\varepsilon)/[4+(2-\varepsilon)^2]\). Then the exact critical survival law is
\[
\mathbb P(\tau>n)\sim
\frac{4\sqrt{2/\pi}(1-\varepsilon)}{\varepsilon(2-\varepsilon)}
\frac{\lambda^n}{\sqrt n}.
\]
Moreover, the conditional laws of the occupied dyadic cell, given \(\tau>n\), converge **in total variation** to the probability vector
\[
 u_k=\frac{\varepsilon}{4}\sum_{j=0}^{k}2^{-j}
 \left(\frac{2-\varepsilon}{2}\right)^{k-j},\quad k\ge0.
\]
The complete conditional interval distribution likewise converges in total variation to the density equal to \(u_k/|I_k|\) on \(I_k\). This critical parameter line has an algebraic return-generating-function singularity: its exponentially damped survival has a nontrivial inverse-square-root prefactor.

## Assumptions and scope
Work on \([0,1)\) with independent random maps. With probability \(q\), apply \(C(x)=x/2\). With probability \(p\), apply the open piecewise-expanding map
\[
 E_{\varepsilon}(x)=\begin{cases}
 2x,&0\le x<1/2,\\
 \dagger,&1/2\le x<(1+\varepsilon)/2,\\
 (2x-1-\varepsilon)/(1-\varepsilon),&(1+\varepsilon)/2\le x<1.
 \end{cases}
\]
Here \(\dagger\) is an absorbing cemetery state. Define \(I_k=[2^{-k-1},2^{-k})\) for integers \(k\ge0\), and take the initial law to be normalized Lebesgue measure on \(I_0=[1/2,1)\). The sampling of map choices is independent at each step. The stated limits hold for each fixed \(\varepsilon\) strictly between zero and one; they are not claimed uniformly at either endpoint.

Write \(a=2-\varepsilon\), so \(1<a<2\), and define \(\lambda=ap\). The strict inequality \(\lambda<1\) follows from \(1-\lambda=\varepsilon^2/(4+a^2)>0\). Conditional uniformity within every occupied \(I_k\) is preserved by both branches. Thus the interval process has exactly the substochastic cell transition matrix \(M\), with source index \(i\) and target index \(j\),
\[
 M_{ji}=p\mathbf1_{\{i\ge1,j=i-1\}}+q\mathbf1_{\{j=i+1\}}+
 p(1-\varepsilon)2^{-j-1}\mathbf1_{\{i=0\}}.
\]
The only loss of probability mass in one step is \(p\varepsilon\) from cell zero. The geometric-reset part above is a genuine transition probability and not a separate normalized kernel.

## Proof
**1. First-return renewal law.** Let \(\mu_{n,k}=\Pr\{\tau>n, X_n\in I_k\}\), and \(G(z)=\sum_{n\ge0}\mu_{n,0}z^n\). Starting at level \(k\ge1\), the ordinary biased nearest-neighbor walk, stopped on first hitting zero, has hitting-time generating function \(h(z)^k\), where the solution analytic at the origin of \(h=z(p+qh^2)\) is
\[
 h(z)=\frac{1-\sqrt{1-4pqz^2}}{2qz}
      =\frac{2pz}{1+\sqrt{1-4pqz^2}}.
\]
A first return to cell zero occurs either by the initial contraction into cell one or by an expanding-branch reset followed by a first hit of zero. Its defective return generating function is
\[
 f(z)=z\left(qh(z)+\frac{p(1-\varepsilon)}{2-h(z)}\right),
 \qquad G(z)=\frac1{1-f(z)}.
\]
These are identities of power series around zero; the geometric series in the reset term is valid since \(|h(z)|<2\) near zero. The second identity is the ordinary renewal decomposition at cell zero.

**2. Critical singularity.** Set \(R=1/\lambda\) and \(\Delta(z)=\sqrt{1-\lambda^2z^2}\). Because \(4pq=\lambda^2\), at the positive branchpoint we have \(h(R)=2/a<2\) and
\[
 f(R)=1,\qquad
 1-f(z)=\frac{a}{2(a-1)}\Delta(z)+O(\Delta(z)^2)
 \quad(z\to R).
\]
Since \(\Delta(z)\sim\sqrt{2}\sqrt{1-z/R}\),
\[
 G(z)=\frac{\sqrt2(a-1)}a(1-z/R)^{-1/2}+O(1).
\]
No other singularity on the convergence circle has this dominant inverse-square-root order. Indeed, the defective first-return power series has strictly positive coefficients at times one and two, so on \(|z|=R\), \(|f(z)|< f(R)=1\) unless \(z=R\). Its only other square-root branchpoint, \(-R\), has \(f(-R)\ne1\), hence contributes at most the lower-order \(O(R^{-n}n^{-3/2})\) coefficient term. The explicit algebraic formulas provide slit-domain analytic continuations permitting coefficient transfer. Consequently
\[
 \mu_{n,0}\sim\frac{\sqrt2(a-1)}{a\sqrt\pi}
 \frac{R^{-n}}{\sqrt n}.
\]

**3. Sharp survival prefactor.** Let \(S_n=\sum_{k\ge0}\mu_{n,k}\). The one-step mass defect is exactly \(S_{n+1}=S_n-p\varepsilon\mu_{n,0}\), with \(S_0=1\). Therefore
\[
 \mathcal S(z):=\sum_{n\ge0}S_nz^n
 =\frac{1-zp\varepsilon G(z)}{1-z}.
\]
Because \(1-R<0\) and the identity \(1-\lambda=p\varepsilon^2/4\) holds,
\[
 \mathcal S(z)=\frac4\varepsilon\,
 \frac{\sqrt2(a-1)}a(1-z/R)^{-1/2}+O(1).
\]
The same singularity analysis yields
\[
 S_n\sim \frac{4\sqrt{2/\pi}(a-1)}{\varepsilon a}
 \frac{\lambda^n}{\sqrt n},
\]
which is the claimed explicit constant.

**4. Conditional law and total variation.** Define the bivariate cell generating function
\[
 \mathcal F(z,w)=\sum_{n,k\ge0}\mu_{n,k}z^nw^k.
\]
The transition law gives the exact meromorphic representation, with removable factors interpreted by analytic continuation,
\[
 \mathcal F(z,w)=
 \frac{1-\dfrac{zpG(z)(2-aw)}{w(2-w)}}
 {1-z(p/w+qw)}.
\]
For each fixed nonnegative integer \(k\), extract the coefficient of \(w^k\) first. The leading singular coefficient at \(z=R\) is \(B_kG(z)\), where
\[
 B(w)=\sum_{k\ge0}B_kw^k
  =\frac{4}{(2-w)(2-aw)}.
\]
To see the factor, substitute \(Rp=1/a\) and \(Rq=a/4\) into the denominator at \(z=R\), cancel its repeated factor \((2-aw)\), and retain the coefficient multiplying the divergent \(G(z)\). The remaining terms are regular or have a strictly weaker branchpoint singularity for every fixed coefficient \(w^k\). Therefore \(\mu_{n,k}/\mu_{n,0}\to B_k\). Since \(B(1)=4/\varepsilon\), normalization gives
\[
 U(w)=\sum_{k\ge0}u_kw^k
 =\frac{B(w)}{B(1)}
 =\frac{\varepsilon}{(2-w)(2-aw)},
\]
which has the coefficient formula in the finding and satisfies \(U(1)=1\). Pointwise convergence of probability masses to a probability vector implies total-variation convergence: for each finite set of cells use coordinatewise limits; the complement has arbitrarily small limiting mass by summability. Because the within-cell conditionals remain uniform, the same conclusion holds for the interval distributions. Direct substitution in the transition matrix verifies \(Mu=\lambda u\); hence \(u\) is a quasi-stationary cell distribution.

## Verification
The included standalone script `check.py` recomputes the transition evolution using exact rational arithmetic, independently builds the first-return and bivariate generating coefficients, and verifies their agreement over several opening parameters and time indices. It also tests the critical prefactor and limiting cell weights numerically at much larger times. A run of the script produced `EXACT_RENEWAL_AND_TRANSFER_COEFFICIENTS_PASS 39` and ended in `CHECKS_PASS`. These finite tests support, but are not substituted for, the generating-function proof. The text establishes asymptotics for all integers \(n\to\infty\), not an exhaustive finite-enumeration claim.

## Relationship to prior work
Brevitt and Klages (2026) define and study this open Pelikan random map and its associated countable substochastic Markov chain, calculate families of quasi-stationary distributions and quasi-ergodic measures, and identify the algebraic critical line with coincident branchpoint and return pole. Their text explicitly does not analyze that boundary in depth. The result here is the critical **sharp inverse-square-root survival amplitude together with a total-variation conditioned-time limit from the dyadic initial cell**, not the previously known existence of critical quasi-stationary laws. General denumerable Markov-chain quasi-stationarity theory provides background but does not supply this computed amplitude or this specific conditional limit without application to the model's return kernel. The original-model relation is exact, not a heuristic continuum approximation.

## Limitations
The result assumes one fixed opening parameter in the strict range, independent branch choices, and an initially uniform top dyadic cell; it does not imply analogous critical laws from arbitrary singular initial distributions or uniformly as opening tends to zero. The cell-preserving property is essential. The derived total-variation Yaglom limit must not be conflated with quasi-ergodic time-average convergence. A potentially overlapping 2026 doctoral thesis by one of the model's authors could not be completely inspected; mathematical priority remains subject to that source and broader literature.

## References
- S. Brevitt and R. Klages, *Quasi-stationary and quasi-ergodic distributions in the Pelikan random map*, arXiv:2607.19084v1 (first public version July 21, 2026), https://arxiv.org/html/2607.19084v1 .
- C. Monthus, *Explicit dynamical properties of the Pelikan random map in the chaotic region and at the intermittent critical point towards the non-chaotic region*, arXiv:2409.19999 (2024), https://arxiv.org/abs/2409.19999 .
- E. Seneta and D. Vere-Jones, *On quasi-stationary distributions in discrete-time Markov chains with a denumerable infinity of states*, Journal of Applied Probability **3** (1966), background theory as cited by Brevitt and Klages.
