# Sharp conditional-depth variance envelope in deterministic weighted recursive trees

## Finding
For a deterministic positive label-weighted recursive tree, the uncertainty of the next vertex's depth has a sharp extremal envelope over **all** weight profiles. Let the root be vertex \(1\), let \(D_j\) be the edge distance of vertex \(j\) to the root, and put
\[
v_j=\mathbb E\bigl[\operatorname{Var}(D_j\mid\mathcal F_{j-1})\bigr].
\]
For every integer \(n\ge3\), the precise maximum of \(v_n\) over positive weights equals \(B_n\), with
\[
B_2=0,\qquad B_{j+1}=B_j+\frac{1}{4(B_j+1)}\quad(j\ge2).
\]
The maximizing attachment fractions are uniquely determined for every \(2\le j<n\):
\[
\boxed{p_j=\frac{1}{2(B_j+1)}.}
\]
Every such fraction profile is achieved by positive weights. The sharp asymptotic envelope has a logarithmic second-order correction:
\[
\boxed{(B_n+1)^2=\frac n2+\frac18\log n+O(1),\qquad B_n\sim\sqrt{n/2}.}
\]
Thus the extremizing weights have fractions \(p_j\sim(2j)^{-1/2}\), rather than the reciprocal-label fractions characteristic of ordinary power-weight recursive trees.

There is also an exact stability identity: for arbitrary positive weights, with \(\Delta_j=B_j-v_j\),
\[
\boxed{\Delta_{j+1}=\left(1-\frac{1}{4(B_j+1)(v_j+1)}\right)\Delta_j+(v_j+1)\left(p_j-\frac{1}{2(v_j+1)}\right)^2.}
\]
Both contributions are nonnegative. In particular, equality at a fixed horizon holds only for the stated optimal fractions at every earlier stage.

## Assumptions and scope
For \(j\ge2\), vertex \(j\) independently chooses an earlier parent \(K_j\), with
\[
\Pr(K_j=i)=\frac{w_i}{W_{j-1}},\quad W_j=\sum_{i=1}^jw_i,\quad w_i>0,\quad 1\le i<j.
\]
Set \(p_j=w_j/W_j\in(0,1)\), and \(\mathcal F_{j-1}=\sigma(K_2,\ldots,K_{j-1})\). There are no regular-variation assumptions. The maximized quantity \(v_n\) is the **expected conditional** variance of a new vertex's depth, not the total (unconditional) depth variance and not the variance of total path length. The weights \(w_1,\ldots,w_{n-1}\) determine \(v_n\); the weight of the arriving vertex itself does not affect this variance.

## Proof
**1. Established variance recurrence.** Define the centered martingale innovation \(\xi_j=D_j-\mathbb E(D_j\mid\mathcal F_{j-1})\). Proposition 5.3 of Gałązka–Wdowicka gives, for all positive deterministic weights,
\[
v_2=0,\qquad v_{j+1}=(1-p_j^2)v_j+p_j(1-p_j).
\]
In particular \(v_j\ge0\). Rearrange by completing the square:
\[
v_{j+1}=v_j+\frac{1}{4(v_j+1)}-(v_j+1)\left(p_j-\frac1{2(v_j+1)}\right)^2.\tag{1}
\]
Every \(p_j\in(0,1)\) is allowed; the unique maximizing choice at fixed \(v_j\) is \(q(v_j)=1/[2(v_j+1)]\), which lies in \((0,1)\).

**2. Global optimality, existence, uniqueness.** Write \(G(x)=x+1/[4(x+1)]\) for \(x\ge0\). It is strictly increasing, since \(G'(x)=1-1/[4(x+1)^2]\ge3/4\). Equation (1) and induction imply \(v_j\le B_j\), where \(B_2=0\) and \(B_{j+1}=G(B_j)\). Equality at the next step requires equality both in the previous bound and the unique maximization of (1). Iterating establishes the unique fraction profile \(p_j=q(B_j)\) for \(2\le j<n\). Conversely, any sequence of fractions in \((0,1)\) is realized by choosing any \(w_1>0\) and recursively \(w_j=p_jW_{j-1}/(1-p_j)\). Hence the envelope is attained in the stated positive-weight class. Its fraction profile fixes \(w_1,\ldots,w_{n-1}\) up to the common initial scale.

**3. Exact deviation identity.** Subtract (1) from the recurrence for \(B_{j+1}\), using
\[
G(B_j)-G(v_j)=(B_j-v_j)\left(1-\frac1{4(B_j+1)(v_j+1)}\right).
\]
This proves the displayed nonnegative-deficit identity and the rigidity of equality at every horizon. The multiplier is at least \(3/4\), so a nonoptimal earlier fraction cannot be erased by later choices.

**4. Sharp asymptotic.** Let \(b_j=B_j+1\), so \(b_2=1\) and \(b_{j+1}=b_j+1/(4b_j)\). Squaring yields the exact telescoping identity
\[
b_{j+1}^2-b_j^2=\frac12+\frac1{16b_j^2}.
\]
It follows first that \(b_j^2\ge j/2\), and then that \(b_j^2=j/2+O(\log j)\), because \(\sum_{i<j}1/b_i^2\le2\sum_{i<j}1/i\). Thus
\[
\frac1{b_j^2}=\frac2j+O\left(\frac{\log j}{j^2}\right).
\]
The error is summable, and substituting into the telescoping formula gives
\[
b_n^2=\frac n2+\frac1{16}\sum_{j=2}^{n-1}\frac1{b_j^2}=\frac n2+\frac18\log n+O(1).
\]
Consequently \(B_n\sim\sqrt{n/2}\), while \(q(B_n)=1/(2b_n)\sim(2n)^{-1/2}\). Every asymptotic statement concerns the deterministic optimum and does not invoke finite enumeration as an infinite proof.

## Verification
A standalone exact-arithmetic checker `verify_envelope.py` independently enumerates all parent histories for three rational weight profiles on four vertices and checks their conditional-depth variances against the recurrence. It also checks the completed-square envelope and deficit identity using exact fractions, for a total of 1,612 passed assertions. A separate deterministic numerical calculation tests the stated asymptotic scale at several finite horizons; that calculation is not part of the asymptotic proof. Run `python3 verify_envelope.py` in the package directory; the expected output is in `verification_output.txt`.

## Relationship to prior work
Gałązka and Wdowicka (2026, Proposition 5.3) derived the universal innovation-variance recurrence, used to study total path length. Their paper does not optimize \(v_n\) over arbitrary positive weight profiles. The known depth-Bernoulli representation and the recursive-tree insertion-depth results of Desmarais (2024) concern different distributions or fixed weight regimes, not the global extremal envelope. Related work on recursive-tree root degree and path length concerns different observables. The present assertion is precisely the attained optimization, its unique evolving extremizer, sharp logarithmic correction, and exact stability identity. Its novelty is qualified by the possibility of an unlocated general optimization theorem; no independent priority audit has been performed.

## Limitations
The result applies to deterministic positive weights and the expected **conditional variance** of one arriving vertex's depth. It does not optimize the unconditional depth variance, height, total path length, degree distribution, or a random/adaptive weight policy. The source recurrence is prior work. The sharp envelope is an exact mathematical consequence of that recurrence, but the full-horizon optimization, all-horizon rigidity, and logarithmic correction are the contributions evaluated here. Independent validation and historical-priority review remain unperformed.

## References
1. M. Gałązka and H. Wdowicka, *Total Path Length in Power-Weight Recursive Trees: Martingale Limits and Global Fluctuations*, arXiv:2610.00614v1, first publicly posted 2026-09-30, especially Proposition 5.3.
2. C. Desmarais, *Depths in random recursive metric spaces*, Journal of Applied Probability 61 (2024), 1448–1462, DOI:10.1017/jpr.2024.32.
3. M. Sénizergues, *Geometry of weighted recursive trees*, 2021, as cited in the motivating article (weighted-tree depth and profile background).
