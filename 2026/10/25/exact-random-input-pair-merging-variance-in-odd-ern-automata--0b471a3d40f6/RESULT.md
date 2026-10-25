# Exact random-input pair-merging variance in odd Černý automata

## Finding
Let \(n=2m+1\ge3\). In the \(n\)-state Černý automaton defined below, feed independent uniformly random letters and let \(T_n\) be the number of letters needed to merge states \(0\) and \(m\). Then
\[
\mathbb E T_n=2m^2(4m+3),\qquad
\operatorname{Var}(T_n)=\frac{2m(2m+1)}3(32m^4+32m^3+6m^2+5m-4).
\]
Equivalently,
\[
\operatorname{Var}(T_n)=\frac{n(n-1)}6(4n^4-8n^3+3n^2+7n-14).
\]
Consequently \(\operatorname{Var}(T_n)\sim\frac23n^6\) and \(\sqrt{\operatorname{Var}(T_n)}/\mathbb E T_n\to\sqrt{2/3}\) along odd \(n\). Thus random-input pair-merging time retains order-one relative fluctuations, despite the deterministic cubic upper bound for its expectation. The mean formula was already established by Gusev (2014); the variance and its consequence are the asserted result.

## Assumptions and scope
For odd \(n=2m+1\ge3\), take states \(Q=\{0,1,\ldots,n-1\}\). The input alphabet is \(\{a,b\}\), with \(a:i\mapsto i+1\pmod n\), while \(b\) fixes every state except \(b(n-1)=0\). At each step \(a\) and \(b\) are sampled independently with probability \(1/2\). The stopping time \(T_n\) is the first nonnegative time at which states \(0,m\) have identical images under the sampled input prefix. This paper treats odd \(n\) and this specified pair; neither even \(n\) nor all-state merging is claimed. All moments are finite because each pair admits a finite synchronizing input word.

For the proof, conjugate the states by \(i\mapsto i+1\) and exchange the letter names: write \(c\) for the rotation, \(d\) for the map \(0\mapsto1\), fixing other states. The initial pair becomes \(\{1,m+1\}\). For \(1\le \ell\le m\), let \((i,\ell)\) represent the unordered pair \(\{i,i+\ell\pmod n\}\). These \(nm\) labels are precisely all unordered distinct pairs. Write \(e_{i,\ell}\) and \(s_{i,\ell}\) for the conditional first and second hitting-time moments from this pair, and set \(A_\ell=e_{1,\ell}\), \(B_\ell=e_{0,\ell}\), \(X_\ell=s_{1,\ell}\), \(Y_\ell=s_{0,\ell}\), with \(A_0=X_0=0\).

## Proof
**1. Pair transition graph.** The rotation sends \((i,\ell)\mapsto(i+1\pmod n,\ell)\). The other letter acts as the identity except at \((0,1)\), which merges; at \((0,\ell)\) for \(2\le\ell\le m\), which moves to \((1,\ell-1)\); at \((n-\ell,\ell)\) for \(1\le\ell<m\), which moves to \((n-\ell,\ell+1)\); and at \((m+1,m)\), which moves to \((1,m)\). This is verified by applying the two maps to the pair elements. The first-step equations are
\[
e_{i,\ell}=1+\tfrac12(e_{c(i,\ell)}+e_{d(i,\ell)}),\qquad
s_{i,\ell}=2e_{i,\ell}-1+\tfrac12(s_{c(i,\ell)}+s_{d(i,\ell)}),
\]
with zero moments at the absorbing merged state.

**2. First moments.** Direct substitution into the above pair equations (or the equivalent calculation in Gusev, 2014, Section 3) gives
\[
A_\ell=(4n^2-4n)\ell-(4n-2)\ell^2,\quad
B_\ell=1+\frac{A_{\ell-1}+A_\ell}{2}.
\]
On the two intervals of ordinary self-loops these extend to
\[
e_{i,\ell}=A_\ell-2(i-1)\quad(1\le i\le n-\ell),\quad
e_{i,\ell}=B_\ell+2(n-i)\quad(n-\ell+1\le i<n).
\]
Together with the special-transition equations and \(A_0=0\), these expressions verify the first-step system at every pair. Every pair can reach the absorbing state, so the transient linear system has a unique solution. In particular \(A_m=2m^2(4m+3)\).

**3. Second-moment segment equations.** Set \(p_\ell=n-\ell-1\), \(E_\ell=A_\ell-2p_\ell\), \(Z_\ell=2B_\ell-1\), and
\[
\begin{aligned}
L_\ell&=p_\ell(4A_\ell-2)-4p_\ell(p_\ell-1),\\
R_\ell&=(\ell-1)(4B_\ell-2)+4\ell(\ell-1),\\
R^+_\ell&=\ell(4B_{\ell+1}-2)+4\ell(\ell+1).
\end{aligned}
\]
For any pair at which \(d\) is an identity, the second-moment equation reduces to \(s_{i,\ell}-s_{i+1,\ell}=4e_{i,\ell}-2\). Summation along the ordinary intervals gives
\[
s_{n-\ell,\ell}=X_\ell-L_\ell,\quad
s_{n-\ell+1,\ell}=Y_\ell+R_\ell,\quad
s_{n-\ell,\ell+1}=Y_{\ell+1}+R^+_\ell.
\]
At \((0,\ell)\), the special transition gives \(Y_\ell=\tfrac12(X_{\ell-1}+X_\ell)+Z_\ell\), including \(\ell=1\) with absorbing \(X_0=0\).

For \(1\le\ell<m\), the special transition at \((n-\ell,\ell)\), after substituting these segment identities, gives
\[
2X_\ell-X_{\ell-1}-X_{\ell+1}=D_\ell,
\]
where
\[
\begin{aligned}
D_\ell&=4\left(L_\ell+2E_\ell-1+\frac{R_\ell+R^+_\ell}{2}\right)+2(Z_\ell+Z_{\ell+1})\\
&=-4(64\ell^2m^2+32\ell^2m+4\ell^2-128\ell m^3-96\ell m^2+4\ell-4m+1).
\end{aligned}
\]
At the upper boundary \((m+1,m)\), the reflection transition instead gives
\[
X_m-X_{m-1}=H_m:=4L_m+8E_m-4+2Z_m+2R_m
=2(96m^4+88m^3-16m^2+2m-1).
\]
Thus, with \(X_0=0\), summing the successive first differences backward from \(m\) gives
\[
X_m=mH_m+\sum_{\ell=1}^{m-1}\ell D_\ell
=\frac{2m}{3}(160m^5+240m^4+98m^3+16m^2-3m-4).
\]
The last polynomial equality follows by expanding \(D_\ell\) and applying the sums of \(\ell\), \(\ell^2\), and \(\ell^3\) (with \(\ell=1,\ldots,m-1\)); it is also amenable to the exact degree-six polynomial-identity check in the standalone checker. Subtracting \(A_m^2\) yields the stated variance. Positivity is clear for \(m\ge1\). The two displayed asymptotics follow from the leading terms \(\mathbb E T_n\sim n^3\) and \(\operatorname{Var}(T_n)\sim 2n^6/3\).

## Verification
Execute `python3 checker.py` with Python 3; no nonstandard dependencies are needed. The checker constructs the unordered-pair absorbing Markov chain independently of the proof's reduced recurrences, solves its first- and second-moment linear systems with exact rational Gaussian elimination for \(n=3,5,7,9,11\), and compares both moments with the closed formulas. It also checks the final polynomial identity at seven different positive \(m\)-values. Since the reduced expression is a polynomial of degree at most six, these seven exact points certify that particular polynomial identity once the displayed recurrence reduction is established. The direct chain checks are finite corroboration, not a proof of all \(n\). The general result rests on the pair-state recurrence, uniqueness, and symbolic summation above.

## Relationship to prior work
V. V. Gusev, *Synchronizing automata with random inputs* (arXiv:1404.6731, first public 2014-04-27), gives the exact expectation for the worst-position pair of Černý automata and the pair-state reduction used here. The present result retains that known expectation and analyzes the second hitting-time moment, which is not determined by an expectation or an upper bound. Classical studies of deterministic shortest reset words and studies sampling random *automata* instead of random *inputs* answer distinct questions. A mathematical-record search found no equivalent variance expression; that negative search is not a uniqueness proof.

## Limitations
Only odd numbers of states, the specified pair, and independent fair letters are covered. The result does not give the complete hitting-time distribution, the all-state synchronization time, or a variance formula for biased letters. Earlier equivalent second-moment formulas might exist under a different stochastic-automata formulation. The polynomial sum is supported by an independent exact certificate, but the proof is not an independent audit.

## References
1. V. V. Gusev, *Synchronizing automata with random inputs*, arXiv:1404.6731, first submitted 27 April 2014. https://arxiv.org/abs/1404.6731
2. A. Kisielewicz, J. Kowalski, M. Szykuła, *Computing the shortest reset words of synchronizing automata*, Journal of Combinatorial Optimization 29 (2015), 88–124. https://doi.org/10.1007/s10878-013-9682-0
3. F. Gonze, R. M. Jungers, *On the synchronizing probability function and the triple rendezvous time for synchronizing automata*, SIAM Journal on Discrete Mathematics 30 (2016), 995–1014.
