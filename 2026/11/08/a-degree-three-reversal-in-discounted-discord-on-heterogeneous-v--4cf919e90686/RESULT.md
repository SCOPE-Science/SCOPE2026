# A degree-three reversal in discounted discord on heterogeneous voter stars

## Finding

Consider a continuous-time node-update voter model on the \(k\)-leaf star, with \(k\ge2\). Let \(H\) be the hub and \(L_1,\ldots,L_k\) its leaves. Each leaf independently updates at rate \(\alpha>0\), copying the hub. The hub updates at rate \(\beta>0\), uniformly chooses one leaf, and copies that leaf. Updates are independent exponential clocks. Initially each binary opinion is independent Bernoulli\((\rho)\), where \(0<\rho<1\).

Write \(D_t=\sum_{i=1}^{k}{\bf1}\{\eta_H(t)\ne\eta_{L_i}(t)\}\) for the number of disagreeing edges. For any discount \(\delta\ge0\), including no discount, define the expected cumulative discord
\[
J_\delta(\beta)=\mathbb E\int_0^\infty e^{-\delta t}D_t\,dt.
\]
Then
\[
\boxed{J_\delta(\beta)=2\rho(1-\rho)k\frac{\delta+2\alpha+(k-1)\beta/k}{\delta^2+(3\alpha+\beta)\delta+2\alpha(\alpha+\beta/k)}}.
\]
For fixed \(k,\alpha,\rho,\delta\), its sensitivity to hub update rate has the exact factorization
\[
\boxed{\frac{\partial J_\delta}{\partial\beta}=\frac{2\rho(1-\rho)(\delta+2\alpha)[\alpha(k-3)-\delta]}{[\delta^2+(3\alpha+\beta)\delta+2\alpha(\alpha+\beta/k)]^2}}.
\]
Consequently, for \(k=2\), increasing hub activity strictly *decreases* cumulative discord for every \(\delta\ge0\). For \(k=3\), it strictly decreases discord at every \(\delta>0\), whereas at \(\delta=0\) the cumulative discord is independent of the hub rate. For every \(k\ge4\) the exact, hub-rate-independent threshold is \(\delta_*=\alpha(k-3)\): increasing hub activity strictly *increases* discounted discord if \(0\le\delta<\delta_*\), strictly *decreases* it if \(\delta>\delta_*\), and leaves it invariant if \(\delta=\delta_*\). At equality its common value is \(2\rho(1-\rho)k/[\alpha(k-2)]\).

This reversal is not visible in the initial trend: for every \(k\ge2\), \(D'_0:=\left.\frac{d}{dt}\mathbb ED_t\right|_{t=0}=-2\rho(1-\rho)(k\alpha+\beta)\), which is strictly more negative at higher hub rates. In a four-leaf star with \(\alpha=1\), \(\rho=1/2\), hub rates \(\beta=1\) and \(\beta=4\), cumulative discord is respectively \(11/5\) and \(5/2\) without discount, both exactly \(1\) when \(\delta=1\), and respectively \(19/29\) and \(7/11\) when \(\delta=2\).

## Assumptions and scope

There are precisely \(k+1\) vertices, \(k\ge2\), and the *node-update* voter convention is used: the leaf update rate \(\alpha\) and the total hub update rate \(\beta\) are rates per vertex, not per edge. Rates are time-homogeneous, strictly positive and independent of current opinions. Initial opinions are independent, identically distributed binary variables with success probability \(\rho\in(0,1)\). All statements compare \(\beta\) while **holding \(\alpha\), \(k\), \(\rho\), and \(\delta\) fixed**; the total network-wide update rate need not be fixed. The target is expected integrated *edge disagreement*, not mean consensus time or the probability of any specified terminal opinion.

## Proof

Let \(u(t)=\Pr(\eta_H(t)\ne\eta_{L_1}(t))\) and \(v(t)=\Pr(\eta_{L_1}(t)\ne\eta_{L_2}(t))\). Exchangeability of leaves persists at all times. One leaf copying the hub eliminates hub–leaf discord at rate \(\alpha\); when the hub copies the tested leaf (rate \(\beta/k\)) the same discord vanishes, whereas copying another leaf (aggregate rate \(\beta(k-1)/k\)) replaces hub–leaf discord by leaf–leaf discord. For two distinct leaves, either leaf copying the hub (each at rate \(\alpha\)) replaces their mutual discord by hub–leaf discord. Thus the full Markov chain closes exactly at two pair probabilities:
\[
\begin{aligned}
u'(t)&=-(\alpha+\beta)u(t)+\frac{k-1}{k}\beta v(t),\\
v'(t)&=2\alpha[u(t)-v(t)],\\
u(0)&=v(0)=c:=2\rho(1-\rho).
\end{aligned}
\]

The coefficient matrix has negative trace \(-(3\alpha+\beta)\) and strictly positive determinant \(2\alpha(\alpha+\beta/k)\). Therefore both eigenvalues have strictly negative real parts. Accordingly \(u(t),v(t)\) decay exponentially, and even \(J_0\) converges absolutely.

Let \(U(\delta)=\int_0^\infty e^{-\delta t}u(t)dt\) and \(V(\delta)=\int_0^\infty e^{-\delta t}v(t)dt\), for \(\delta\ge0\). Laplace transforming the equations gives
\[
\begin{pmatrix}\delta+\alpha+\beta&-(k-1)\beta/k\\-2\alpha&\delta+2\alpha\end{pmatrix}
\begin{pmatrix}U\\V\end{pmatrix}=
\begin{pmatrix}c\\c\end{pmatrix}.
\]
The determinant is
\[
\Delta=(\delta+\alpha+\beta)(\delta+2\alpha)-2\alpha\beta(k-1)/k
=\delta^2+(3\alpha+\beta)\delta+2\alpha(\alpha+\beta/k)>0.
\]
Cramer's rule yields \(U=c[\delta+2\alpha+(k-1)\beta/k]/\Delta\). By symmetry, \(\mathbb ED_t=ku(t)\), giving the displayed exact formula for \(J_\delta=kU\).

For differentiation at fixed \(\alpha,\delta,k,\rho\), write \(N=\delta+2\alpha+(k-1)\beta/k\) and \(\Delta\) as above. Since \(\partial_\beta N=(k-1)/k\) and \(\partial_\beta\Delta=\delta+2\alpha/k\), direct expansion gives the exact identity
\[
k\left(\frac{k-1}{k}\Delta-N\left(\delta+\frac{2\alpha}{k}\right)\right)
=(\delta+2\alpha)[\alpha(k-3)-\delta].
\]
Substituting into the quotient derivative proves the claimed factorization. All factors outside the final bracket are strictly positive, proving the three-degree phase diagram, with no numerical or asymptotic inference. Setting \(\delta=\alpha(k-3)\) for \(k\ge4\) in the exact formula simplifies it to the claimed hub-rate-independent constant; for \(k=3,\delta=0\), the same direct simplification holds. Finally, \(\left.\frac{d}{dt}\mathbb ED_t\right|_{t=0}=k u'(0)=-kc(\alpha+\beta/k)=-c(k\alpha+\beta)\), proving the initial-time opposition.

## Verification

The self-contained standard-library Python program `checker.py` independently constructs the complete \(2^{k+1}\)-state generator and solves its rational resolvent, rather than reusing the two-moment reduction. It checks \(54\) exact full-state cases across \(k=2,3,4\), three rate pairs, three discounts and two initial densities, as well as extensive exact rational threshold comparisons, equality cases and initial-slope identities. Run `python3 checker.py`; the verified output is `PASS 1196 exact assertions; full-state cases 54`. These finite calculations are consistency checks; the all-parameter proof is the two-moment analytic derivation above.

## Relationship to prior work

The heterogeneous-update voter-model setting is motivated by Masuda, Gibert and Redner's *Heterogeneous Voter Models* (arXiv:1003.0768; initially public March 3, 2010), which develops consensus outcomes and time scales under heterogeneous rates but does not state the displayed star discord resolvent or degree-three discount reversal. Iwamasa and Masuda's *Networks maximizing the consensus time of voter models* (arXiv:1404.6360; first public April 25, 2014) studies network shapes, including double-star networks and coalescing random-walk duality, for mean consensus time; a result on global consensus time does not imply the hub-activity response of the discounted integral of the number of disagreeing edges. Cooper, Elsässer, Ono and Radzik's *Coalescing Random Walks and Voting on Connected Graphs* (arXiv:1204.4106; first public April 17, 2012) gives general bounds for coalescing walks and voting, but does not specialize to this continuous hub-rate sensitivity or identify its sharp discount threshold. The three primary full texts and their relevant sections were inspected. The model's pair equations may also be derived from standard voter duality, so the novelty proposed here is the exact global phase classification and the counterintuitive first-moment reversal, not a new voter-model definition or duality theorem.

## Limitations

This is a binary, symmetric-under-leaf-permutations, finite star model with constant positive vertex update rates and iid initial opinions. The reward is cumulative edge disagreements, not elapsed consensus time, mean opinion, entropy or a fixed-budget design. It does not establish the same threshold for arbitrary graphs, unequal leaf rates, correlated initial states, nonlinear update rules or epidemiological processes. Priority remains provisional: a historically earlier equivalent discounted pair-correlation or coalescing-walk calculation may exist under different terminology. Self-review is not independent certification.

## References

1. N. Masuda, N. Gibert, and S. Redner, *Heterogeneous Voter Models*, arXiv:1003.0768, initially posted 2010-03-03, https://arxiv.org/abs/1003.0768.
2. Y. Iwamasa and N. Masuda, *Networks maximizing the consensus time of voter models*, arXiv:1404.6360, initially posted 2014-04-25, https://arxiv.org/abs/1404.6360.
3. C. Cooper, R. Elsässer, H. Ono, and T. Radzik, *Coalescing Random Walks and Voting on Connected Graphs*, arXiv:1204.4106, initially posted 2012-04-17, https://arxiv.org/abs/1204.4106.
