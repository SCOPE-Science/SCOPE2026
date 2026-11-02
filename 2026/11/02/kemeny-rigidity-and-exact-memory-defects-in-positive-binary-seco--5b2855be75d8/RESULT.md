# Kemeny rigidity and exact memory defects in positive binary second-order chains

## Finding
Let \((X_t)_{t\ge0}\) be a time-homogeneous binary second-order Markov chain, with
\[
q_{ab}=\Pr(X_{t+1}=1\mid X_t=a,X_{t-1}=b),\qquad a,b\in\{0,1\},
\]
and assume that each of its four transition probabilities lies strictly between zero and one. Write
\[
u=q_{00},\quad v=q_{01},\quad w=q_{10},\quad z=q_{11},\qquad
A=1+\frac{1-v}{u},\quad B=1+\frac{w}{1-z}.
\]
Let \(\pi\) be the stationary one-time law, independently sample a target \(Y\) from \(\pi\), and define, for every initial history \((a,b)\),
\[
\theta_{ab}=\mathbb E\!\left[\min\{j\ge1:X_{t+j}=Y\}\mid (X_t,X_{t-1})=(a,b)\right].
\]
This definition includes positive return times when the target equals the current state, as in the expected marginal mixing time of Han (2026).

**Theorem.** The stationary masses and the two *exact signed memory defects* are
\[
\pi(1)=\frac{B}{A+B},\qquad \pi(0)=\frac{A}{A+B},
\]
\[
\boxed{\theta_{00}-\theta_{01}=\pi(1)\frac{(u-v)^2}{u},\qquad
\theta_{11}-\theta_{10}=\pi(0)\frac{(w-z)^2}{1-z}.}
\]
Consequently, the four expected marginal mixing times are all equal **if and only if**
\[
u=v\quad\text{and}\quad w=z.
\]
These equalities mean exactly that the process is a first-order binary Markov chain: the previous-but-one bit contributes no predictive information once the current bit is known. In that case the common expected first-positive-hitting time is
\[
\boxed{\theta_{ab}=1+\frac{1}{u+1-w}\quad\text{for every }(a,b)\in\{0,1\}^2.}
\]
For arbitrary positive parameters, its range obeys the explicit memory-sensitive lower bound
\[
\max_{a,b}\theta_{ab}-\min_{a,b}\theta_{ab}\ \ge\
\max\left\{\pi(1)\frac{(u-v)^2}{u},\ \pi(0)\frac{(w-z)^2}{1-z}\right\}.
\]
The assertion is a complete necessity-and-sufficiency classification, within the positive binary second-order family, of the constant expected marginal mixing time property posed in Han (2026, Remark 5.1). The general characterization for larger alphabets or greater memory depth is not claimed.

## Assumptions and scope
The state space is \(\{0,1\}\), the chain is homogeneous with two-step conditional probabilities \(q_{ab}\in(0,1)\), and the target is sampled independently according to the unique stationary one-time marginal. The lifted four-state chain on \((X_t,X_{t-1})\) is irreducible and aperiodic because every two-step binary output word has positive probability from every initial pair. Every first-positive-passage expectation is finite. All identities hold for every allowed parameter quadruple, without asymptotics or a symmetry assumption.

## Proof
**Stationary one-time weights.** Write \(s\) for the common stationary masses of pair states \((0,1)\) and \((1,0)\), which are equal by invariance of adjacent one-time marginals. Balance at \((0,0)\) and \((1,1)\) gives
\[
\Pr_\pi(0,0)\,u=s(1-v),\qquad
\Pr_\pi(1,1)\,(1-z)=sw.
\]
After normalization, \(s=1/(A+B)\); the stationary marginal probabilities are therefore \(\pi(0)=sA\) and \(\pi(1)=sB\). These are strictly positive.

**First positive passage means.** Define \(h_y(a,b)=\mathbb E[\min\{j\ge1:X_{t+j}=y\}\mid(X_t,X_{t-1})=(a,b)]\), for \(y\in\{0,1\}\). The first-step equations, including the recurrence case, are
\[
 h_1(a,b)=1+(1-q_{ab})h_1(0,a),\qquad
 h_0(a,b)=1+q_{ab}h_0(1,a).
\]
Solving these elementary equations gives the complete tables
\[
\begin{array}{c|rrrr}
 (a,b)&(0,0)&(0,1)&(1,0)&(1,1)\\ \hline
 h_1(a,b)&1/u&A&1+(1-w)A&1+(1-z)A\\
 h_0(a,b)&1+uB&1+vB&B&1/(1-z)
\end{array}
\]
For example, \(h_1(0,0)=1+(1-u)h_1(0,0)=1/u\), while \(h_0(1,1)=1+zh_0(1,1)=1/(1-z)\). Each other entry follows by one substitution. Since \(Y\) is sampled independently from \(\pi\),
\[
\theta_{ab}=\pi(1)h_1(a,b)+\pi(0)h_0(a,b).
\]

**The quadratic defects.** By the tables,
\[
\begin{aligned}
\theta_{00}-\theta_{01}
&=\frac{B}{A+B}\left(\frac{1}{u}-A\right)
 +\frac{A}{A+B}(u-v)B\\
&=\frac{B}{A+B}(u-v)\left(A-\frac1u\right)
=\pi(1)\frac{(u-v)^2}{u},
\end{aligned}
\]
where \(A-1/u=(u-v)/u\). Similarly,
\[
\begin{aligned}
\theta_{11}-\theta_{10}
&=\frac{B}{A+B}(w-z)A
 +\frac{A}{A+B}\left(\frac1{1-z}-B\right)\\
&=\frac{A}{A+B}(w-z)\left(B-\frac1{1-z}\right)
=\pi(0)\frac{(w-z)^2}{1-z},
\end{aligned}
\]
where \(B-1/(1-z)=(w-z)/(1-z)\). Both coefficients are strictly positive. Hence four-way constancy forces \(u=v\) and \(w=z\). Conversely those equalities make the visible chain first-order, so the standard first-positive-return Kemeny identity applies; alternatively direct substitution into the displayed tables yields the common value \(1+1/(u+1-w)\). The range lower bound is immediate from the two nonnegative pair differences. This proves every asserted statement.

**Exact example.** With \((u,v,w,z)=(1/2,1/4,1/2,3/4)\), the stationary one-time weights are \(\pi(1)=6/11\), \(\pi(0)=5/11\), and the expected times are
\[
(\theta_{00},\theta_{01},\theta_{10},\theta_{11})=(49/22,95/44,57/22,119/44).
\]
The two defects are precisely \(3/44\) and \(5/44\), respectively.

## Verification
Run `python verify.py` (Python standard library only). The checker independently builds the lifted four-state transition matrix, solves the stationary linear system, solves two separate hitting-time linear systems by exact Gauss–Jordan elimination, and compares their outputs with the theorem's closed expressions. It checks all \(5^4=625\) parameter quadruples from a fixed rational grid and 400 additional seeded rational quadruples, including all equality and nonequality cases represented by that sample. The saved output is `verify_output.txt`. All 1,025 parameter tuples passed. The finite checker corroborates algebra and conventions but is not a proof for the continuum of parameters; the proof above establishes the universal identities.

## Relationship to prior work
Han, *Marginal Stationary Distributions and Convergence Rates of Higher Order Markov Chains* (arXiv:2607.12303v1, 2026), defines the expected marginal mixing time and explicitly asks when it is independent of initial history (Remark 5.1). That article gives a sufficient condition that the older history coordinate does not matter, but does not give the binary two-step necessity or the exact quadratic defects. Fredes and Marckert (arXiv:2510.26207) establish general Kemeny identities for fully observed finite first-order chains; those identities explain the sufficient direction once the visible process is Markov, but do not supply the converse for a non-Markov visible process. The classical Kemeny–Snell lumpability test, also reviewed by Wolfer and Watanabe (arXiv:2203.04575), says when a projected chain remains first-order. Here the additional statement is that *constancy of a single stationary-target expected hitting-time functional forces precisely that lumpability* for the positive binary second-order de Bruijn lift, with exact quantitative defects. No historical uniqueness claim follows merely from a database search.

## Limitations
Strict positivity is essential to the stated finite formulas and to the proof's positive denominators; degenerate boundary tensors, larger alphabets, and longer memories are not classified here. The result concerns a stationary-random target and first *positive* hitting time, not total-variation mixing time or first nonnegative hitting time. It does not assert an independent audit or that all historical literature has been exhaustively examined. The novelty comparison relies on accessible indexed and primary sources and remains subject to unindexed earlier work on lumped hitting-time identities.

## References
1. L. Han, *Marginal Stationary Distributions and Convergence Rates of Higher Order Markov Chains*, arXiv:2607.12303v1 (first posted 2026-07-14), §§3 and 5, especially Definition 5.2, Theorem 5.2 and Remark 5.1. https://arxiv.org/abs/2607.12303
2. L. Fredes and J.-F. Marckert, *A combinatorial perspective on the Kemeny constant and more*, arXiv:2510.26207 (2025), §1. https://arxiv.org/abs/2510.26207
3. G. Wolfer and S. Watanabe, *Geometric Aspects of Data-Processing of Markov Chains*, arXiv:2203.04575 (2022), on lumpability and information-preserving projections. https://arxiv.org/abs/2203.04575
4. J. J. Hunter, *The Role of Kemeny's Constant in Properties of Markov Chains*, arXiv:1208.4716 (2012), background on stationary-target mean passage times. https://arxiv.org/abs/1208.4716
