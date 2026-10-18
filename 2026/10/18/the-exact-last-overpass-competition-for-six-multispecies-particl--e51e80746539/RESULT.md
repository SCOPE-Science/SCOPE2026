# The exact last-overpass competition for six multispecies particles

## Finding
Consider the finite continuous-time three-species exchange process on the six-site interval, initially ordered as \(2,2,1,1,0,0\). Species have strictly increasing velocities \(v_0<v_1<v_2\). An adjacent inversion \((i,j)\), \(i>j\), swaps at rate \(v_i-v_j\); no other swaps occur. Let \(a=v_1-v_0>0\), \(b=v_2-v_1>0\), and \(x=b/a>0\). Define \(Q(x)\) as the probability that the **last** swap before full sorting \((0,0,1,1,2,2)\) is of type \((1,0)\), rather than \((2,1)\).

Let
\[
\begin{aligned}
A(x)={}&256x^9+3968x^8+27648x^7+114496x^6+299902x^5\\
&+498185x^4+513714x^3+313926x^2+103375x+14098.
\end{aligned}
\]
Then the exact, all-rate formula is
\[
\boxed{Q(x)=\frac{x^4 A(x)}{8(x+1)^3(x+2)^5(2x+1)^5}.}
\]
Moreover \(Q\) is strictly increasing over \((0,\infty)\), \(Q(1)=1/2\), and \(Q(x)+Q(1/x)=1\). Thus the smaller adjacent speed gap determines the more likely last overpass at this first nontrivial balanced population size: \(Q(x)>1/2\) exactly when \(b>a\). The limits are \(Q(x)\to0\) as \(x\downarrow0\) and \(Q(x)\to1\) as \(x\to\infty\). For example, \(Q(2)=1465319/1800000\).

## Assumptions and scope
The six labeled positions contain two indistinguishable particles of each species, independent exponential interchange clocks, and no boundary injections or removals. The theorem concerns the **identity of the last interchange**, not just the marginal distribution of the sorting time. The formula is for exactly two particles of each of three species and arbitrary positive adjacent speed gaps. Commonly scaling all rates changes time but not interchange order.

## Proof
Write \(s\) for one of the \(6!/(2!)^3=90\) distinct species arrangements and \(s^*=(0,0,1,1,2,2)\). For each adjacent inversion \((s_j,s_{j+1})\), let \(s^{(j)}\) be the state with that pair swapped, and let the dimensionless interchange rate \(r_j(s;x)\) be \(1\) for \((1,0)\), \(x\) for \((2,1)\), and \(1+x\) for \((2,0)\). Define \(F_s(x)\) to be the probability of a final \((1,0)\) interchange starting from \(s\), and for transitions ending in \(s^*\) assign the boundary payoff \(1\) for a final \((1,0)\) and \(0\) otherwise. Every allowed swap removes exactly one pair inversion. Thus the directed state graph is acyclic and all nonterminal states have positive total rate. The first-interchange decomposition yields, uniquely,
\[
F_s(x)=\frac{\sum_{j:s_j>s_{j+1}}r_j(s;x)\,V(s^{(j)},s_j,s_{j+1};x)}{\sum_{j:s_j>s_{j+1}}r_j(s;x)},
\]
where \(V(s^{(j)},i,j;x)=F_{s^{(j)}}(x)\) for nonterminal destinations and \(V(s^*,i,j;x)=\mathbf1_{(i,j)=(1,0)}\). This recurrence has precisely 89 nonterminal rational functions. Because every transition reduces inversion count, recursively applying it is an exhaustive proof, without truncating time or approximating the continuous-time process.

Exact rational-function reduction, executed over all states in `check.py`, gives \(F_{(2,2,1,1,0,0)}(x)=x^4A(x)/D(x)\) with \(D(x)=8(x+1)^3(x+2)^5(2x+1)^5\). The script supplies the complete independent, finite symbolic certificate for the displayed equality; each recurrence step is a finite first-step conditioning identity and is checked symbolically.

Differentiate the stated rational expression. Exact polynomial cancellation gives
\[
Q'(x)=\frac{x^3B(x)}{8(x+1)^4(x+2)^6(2x+1)^6},
\]
with
\[
\begin{aligned}
B(x)={}&112784x^8+991456x^7+3729476x^6+7807043x^5\\
&+9913144x^4+7807043x^3+3729476x^2+991456x+112784.
\end{aligned}
\]
Every coefficient of \(B\) is strictly positive, proving strict monotonicity on positive \(x\). Reverse the species labels and spatial order to interchange the two adjacent speed gaps; this maps the final \((1,0)\) event to the final \((2,1)\) event, so \(Q(x)+Q(1/x)=1\); the identity is also symbolically verified by `check.py`. Therefore \(Q(1)=1/2\), and monotonicity gives the claimed sharp threshold. The limits follow from polynomial degrees and positive leading constants. Finally, the last swap cannot have type \((2,0)\): swapping an adjacent \((2,0)\) into \((0,2)\) cannot directly produce the grouped sorted state, because the two species-1 particles separate the terminal species-0 and species-2 blocks.

## Verification
Run `python check.py` using `sympy>=1.11`, optionally after installing the package versions in `requirements.txt`. The program constructs all 90 distinct multisets, computes the first-step recursion in exact symbolic arithmetic, checks the published rational formula, differentiates it symbolically, checks all derivative coefficients positive, establishes the polynomial sign and reversal identities, and verifies \(Q(2)=1465319/1800000\). No Monte Carlo, interpolation, decimal tolerance or enumeration cutoff is involved. The finite dynamic program is exhaustive for the exact six-particle model, but does not prove a statement about any larger population.

## Relationship to prior work
Maga and Tóth (2026, arXiv:2610.08135v1), Theorem 1.1, identify each individual cut-completion time with an inhomogeneous last-passage time, and Theorem 1.2 describes its macroscopic growth. These established results motivate asking **which cut actually finishes last** in a finite balanced system, but the paper does not state the finite joint event probability evaluated here. The single-cut marginal laws do not determine the last-cut comparison in general.

Bisi, Cunden, Gibbons and Romik (2022) study last swap times of the usual oriented swap process with **unit interchange rates for permitted pairs**, not the three-velocity difference-dependent model here. Their paper develops joint-time questions but its inspected statements do not contain this six-particle two-gap rational comparison. Standard continuous-time Markov-chain first-step conditioning is used here as an established method, not claimed as new.

## Limitations
This is a natural first interacting finite balanced case, not a general population-size theorem or an asymptotic rate. The recurrence supplies a rigorous finite-state symbolic proof, subject to rerunning the embedded exact algebraic script. No independent audit or external priority certification has been performed. A general result not found in the inspected literature could subsume the displayed finite formula; numerical enumeration alone would not establish originality.

## References
1. B. Maga and B. Tóth, *Microscopic sorting in a multispecies exclusion process*, arXiv:2610.08135v1, first submitted 2026-10-06, especially Theorems 1.1–1.2.
2. E. Bisi, F. D. Cunden, S. Gibbons and D. Romik, *The oriented swap process and last passage percolation*, Random Structures & Algorithms 60 (2022), 690–715, DOI:10.1002/rsa.21055; originally arXiv:2005.02043.
