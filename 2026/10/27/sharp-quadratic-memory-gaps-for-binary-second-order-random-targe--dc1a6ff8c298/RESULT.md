# Sharp quadratic memory gaps for binary second-order random-target hitting times

## Finding

For a homogeneous binary second-order Markov chain with all eight transition probabilities strictly positive, define
\[
\begin{aligned}
a&=\Pr(X_{t+1}=1\mid X_t=0,X_{t-1}=0),\\
b&=\Pr(X_{t+1}=1\mid X_t=0,X_{t-1}=1),\\
c&=\Pr(X_{t+1}=1\mid X_t=1,X_{t-1}=0),\\
d&=\Pr(X_{t+1}=1\mid X_t=1,X_{t-1}=1).
\end{aligned}
\]
Let \(\pi=(\pi_0,\pi_1)\) be the unique stationary one-time marginal and define the *strictly positive* target-hitting time \(T_y=\inf\{k\ge1:X_{t+k}=y\}\). The expected stationary-random-target hitting time conditional on a full two-symbol history is
\[
K_{ij}=\sum_{y\in\{0,1\}}\pi_y\,\mathbb E[T_y\mid X_t=i,X_{t-1}=j].
\]
For every \(a,b,c,d\in(0,1)\), set
\[
\Delta=(1-b)(1-d)+ac+2a(1-d)>0.
\]
Then the two within-current-symbol memory gaps are *exactly*
\[
\boxed{K_{00}-K_{01}=\frac{(a-b)^2(1+c-d)}{\Delta}},
\qquad
\boxed{K_{11}-K_{10}=\frac{(c-d)^2(1+a-b)}{\Delta}}.
\]
In particular, both are nonnegative and vanish exactly when the corresponding transition probabilities cease to depend on the previous symbol. Thus
\[
\boxed{K_{00}=K_{01}=K_{10}=K_{11}\ \Longleftrightarrow\ a=b\text{ and }c=d.}
\]
Equivalently, *full-history constancy of expected marginal mixing time holds precisely when the positive binary second-order kernel is in fact first-order*. This gives a complete two-state, order-two classification of the constancy question posed by Han (2026, Remark 5.1).

## Assumptions and scope

The time index ranges over the integers, and the state space is \(\{0,1\}\). The process is homogeneous and depends on its two latest symbols, with all four probabilities of next symbol \(1\) in the open unit interval. The complementary next-symbol probabilities are positive automatically. Every two-symbol history has positive stationary mass; the lifted four-state chain is irreducible and aperiodic, so there is a unique stationary two-symbol distribution, a unique marginal \(\pi\), and finite means for each strictly positive hitting time. We use the convention \(\inf\{k\ge1\}\), not a zero-time hit when the target is already occupied. The target is chosen independently from \(\pi\). The conditional expectations themselves are well-defined from each history without requiring a stationary initial law, but \(\pi\) is always the stationary marginal of the specified kernel.

## Proof

**1. Unique stationary marginal.** Write \(\mu_{ij}=\Pr(X_t=i,X_{t-1}=j)\) in stationarity, and put
\[
u=\frac{1-b}{a},\qquad v=\frac{c}{1-d},\qquad W=u+v+2.
\]
Stationary flux between differing symbols gives \(\mu_{01}=\mu_{10}\). Invariance of the lifted chain at the diagonal histories gives \(a\mu_{00}=(1-b)\mu_{01}\) and \((1-d)\mu_{11}=c\mu_{10}\). Normalization therefore yields, in the order \((00,01,10,11)\),
\[
(\mu_{00},\mu_{01},\mu_{10},\mu_{11})=\frac{(u,1,1,v)}{W},
\quad \pi_0=\frac{1+u}{W},\quad \pi_1=\frac{1+v}{W}.
\]
These equations also prove directly that both marginal probabilities are strictly positive. Uniqueness follows independently from the positive two-step lifted transition matrix.

**2. All eight positive first-hitting means.** Put \(h^{(y)}_{ij}=\mathbb E[T_y\mid X_t=i,X_{t-1}=j]\). First-step conditioning, with absorption upon the next occurrence of target \(y\), gives
\[
h^{(y)}_{ij}=1+\sum_{k\in\{0,1\}\setminus\{y\}}
\Pr(X_{t+1}=k\mid X_t=i,X_{t-1}=j)\,h^{(y)}_{ki}.
\]
Solving these recurrences directly gives the following complete lists, with no zero-time hitting convention:
\[
\begin{aligned}
h^{(1)}_{00}&=1/a,&h^{(1)}_{01}&=1+u,\\
h^{(1)}_{10}&=1+(1-c)(1+u),&h^{(1)}_{11}&=1+(1-d)(1+u),\\
h^{(0)}_{00}&=1+a(1+v),&h^{(0)}_{01}&=1+b(1+v),\\
h^{(0)}_{10}&=1+v,&h^{(0)}_{11}&=1/(1-d).
\end{aligned}
\]
For instance, \(h^{(1)}_{00}=1+(1-a)h^{(1)}_{00}\); from \((0,1)\), failing to hit \(1\) produces history \((0,0)\), giving \(h^{(1)}_{01}=1+(1-b)h^{(1)}_{00}\). The other equations follow in the same manner. The strict positivity of the kernel guarantees these are the unique finite solutions.

**3. Exact factorizations.** Using \(K_{ij}=\pi_0h^{(0)}_{ij}+\pi_1h^{(1)}_{ij}\), the two differences simplify to
\[
\begin{aligned}
K_{00}-K_{01}
&=\pi_0(a-b)(1+v)+\pi_1\frac{b-a}{a}
=\frac{(a-b)^2(1+v)}{aW},\\
K_{11}-K_{10}
&=\pi_0\frac{d-c}{1-d}+\pi_1(c-d)(1+u)
=\frac{(c-d)^2(1+u)}{(1-d)W}.
\end{aligned}
\]
Since \(a(1-d)W=(1-b)(1-d)+ac+2a(1-d)=\Delta\), these become the boxed formulas above. Both coefficients \(1+c-d\) and \(1+a-b\) are strictly positive under the assumptions, proving strictness whenever the associated second-order memory parameter is nonzero.

**4. Constancy is equivalent to memorylessness.** If all four \(K_{ij}\) are equal, the first square forces \(a=b\) and the second forces \(c=d\). These equalities say exactly that the next-symbol conditional law depends only on \(X_t\). Conversely, if \(a=b\) and \(c=d\), the kernel is a positive first-order two-state chain, so the classical random-target lemma applies. Direct substitution also gives the same common value at every history,
\[
K_{ij}=1+\frac1{a+1-c},\qquad i,j\in\{0,1\},
\]
with the strictly positive hitting-time convention used here. This proves both directions.

**Exact witness.** For \((a,b,c,d)=(1/4,3/4,2/3,1/3)\), the stationary one-time marginal is \((1/2,1/2)\), but
\[
(K_{00},K_{01},K_{10},K_{11})
=(11/4,9/4,11/6,23/12).
\]
The two memory gaps are exactly \(1/2\) and \(1/12\). Thus even a balanced stationary marginal does not hide the historical sensitivity of this hitting-time observable.

## Verification

The accompanying `check_binary_second_order.py` uses independent exact-rational linear algebra: it forms the four-state lifted transition matrix, solves the stationary equations, solves separate four-state positive first-hitting systems for targets \(0\) and \(1\), then checks both closed formulas and the equivalence of constancy with first-order memorylessness. The verifier handles 268 parameter quadruples with rational coefficients, including full-memory, one-sided-memory, memoryless, and displayed-witness cases. The saved `check_output.txt` is the output of that program. All checks passed. Their role is diagnostic: the theorem for the entire open parameter cube follows from the finite algebraic proof above, not from enumeration.

To reproduce: with Python 3 and both supplied files in one directory, run `python check_binary_second_order.py`. Only the standard library is required. Output values are written as reduced exact fractions.

## Relationship to prior work

Han (2026, Section 5, Theorem 5.2 and Remark 5.1) defines expected marginal mixing time as a stationary-marginal-weighted first positive hitting time for a higher-order Markov chain. Han explicitly asks for conditions ensuring constancy over full initial histories and notes that the first-order condition is sufficient. The present theorem establishes necessity as well, specifically for the strictly positive binary second-order case; it supplies two exact nonnegative quadratic deficits, rather than assuming a reduced first-order transition matrix gives the marginal-target result.

Fasino, Tonetto, and Tudisco (2021, Section 5, especially Corollary 5.7) prove a second-order random-target lemma under an equilibrium/pullback construction and additional regularity of return times. Their constancy concerns a different averaging of histories and does not assert constancy conditional on each individual two-symbol initial history. Xu (2026, Section 6) surveys higher-order mean first-passage tensor equations and contrasts them with first-order hitting times of the lifted chain; it does not characterize the constancy of marginal-stationary-weighted hitting times across all binary initial histories. The classical Kemeny–Snell random-target lemma supplies the already-known first-order implication only.

## Limitations

Only the strictly positive \(2\)-state, second-order case is classified. Boundary transition probabilities in \(\{0,1\}\), reducible or periodic lifts, larger alphabets, orders three and higher, and nonstationary target weights are not covered. The proof is elementary exact finite algebra but is not an independent historical-priority certificate; a previously unlocated algebraic or Markov-renewal characterization might imply an equivalent result. No external independent mathematical audit has been performed. The theorem says nothing about constancy of target hitting times for the four *lifted history states*, which is a different classical random-target observable.

## References

1. L. Han, *Marginal Stationary Distributions and Convergence Rates of Higher Order Markov Chains*, arXiv:2607.12303v1 (first publicly posted 2026-07-14), Section 5, Theorem 5.2 and Remark 5.1. https://arxiv.org/abs/2607.12303
2. D. Fasino, A. Tonetto, and F. Tudisco, *Hitting times for second-order random walks*, arXiv:2105.14438 (first publicly posted 2021-05-30), Sections 4–5. https://arxiv.org/abs/2105.14438
3. J. Xu, *Can a higher-order Markov chain be treated as a first-order Markov chain?*, *Probability in the Engineering and Informational Sciences* 40 (2026), 400–415, Section 6. DOI: 10.1017/S0269964826100230.
4. J. G. Kemeny and J. L. Snell, *Finite Markov Chains* (1960), classical random-target lemma.
