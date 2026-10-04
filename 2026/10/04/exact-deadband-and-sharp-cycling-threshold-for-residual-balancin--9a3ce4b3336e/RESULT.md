# Exact deadband and sharp cycling threshold for residual-balancing ADMM
## Finding
Consider standard unrelaxed ADMM for
\[
\min_{x,z\in\mathbb R}\frac a2x^2+\frac b2z^2
\quad\text{subject to}\quad x-z=0,
\qquad a,b>0,
\]
with a positive penalty \(\rho_k\). Use the unscaled multiplier \(y^k\), primal residual \(r^{k+1}=x^{k+1}-z^{k+1}\), and dual residual \(s^{k+1}=-\rho_k(z^{k+1}-z^k)\). After each iteration, update the penalty by the symmetric residual-balancing rule with \(\mu>1\) and \(\tau>1\): multiply by \(\tau\) when \(|r|>\mu|s|\), divide by \(\tau\) when \(|s|>\mu|r|\), and otherwise leave it unchanged.

After the first completed ADMM update one has the exact invariant
\[
y^k=bz^k.
\]
On every subsequent nonstationary update,
\[
\frac{|r^{k+1}|}{|s^{k+1}|}=\frac{b}{\rho_k^2}.
\]
Consequently the adaptive penalty is governed exactly by the state-independent map
\[
\Phi(\rho)=
\begin{cases}
\tau\rho,&0<\rho<\sqrt{b/\mu},\\
\rho,&\sqrt{b/\mu}\le \rho\le\sqrt{\mu b},\\
\rho/\tau,&\rho>\sqrt{\mu b}.
\end{cases}
\]
This gives a sharp dichotomy. Every positive starting penalty enters the deadband and then freezes after finitely many adaptive updates if and only if
\[
1<\tau\le\mu.
\]
If \(\tau>\mu\), every \(\rho\) in the nonempty interval
\[
\left(\frac{\sqrt{\mu b}}{\tau},\sqrt{\frac b\mu}\right)
\]
generates an exact penalty two-cycle \(\rho\leftrightarrow\tau\rho\). The primal-dual state nevertheless continues to converge geometrically: after the invariant is established,
\[
z^{k+1}=q(\rho_k)z^k,
\qquad
q(\rho)=\frac{\rho^2+ab}{(a+\rho)(b+\rho)}\in(0,1).
\]
Thus the cycling is a genuine parameter oscillation, not divergence of this scalar ADMM state.

For fixed \(\rho\), the contraction \(q(\rho)\) is uniquely minimized at the already-known rate-optimal penalty
\[
\rho_*=\sqrt{ab},
\qquad
q_* = \frac{2\sqrt{ab}}{(\sqrt a+\sqrt b)^2}.
\]
The residual-balancing deadband contains \(\rho_*\) exactly when \(1/\mu\le a\le\mu\) in these numerical coordinates. In particular, with \(b=1\) and fixed \(\mu\), if \(a>\mu\), every frozen residual-balanced penalty lies below \(\rho_*\), and even the best contraction allowed by the deadband satisfies
\[
q(\sqrt\mu)\longrightarrow \frac{1}{1+\sqrt\mu}
\quad\text{as }a\to\infty,
\]
whereas \(q_*\sim2/\sqrt a\to0\). Hence residual balance can stabilize finitely yet remain arbitrarily far, in relative rate, from the optimal fixed penalty.

## Assumptions and scope
The result uses the classical two-block ADMM ordering and the standard primal and dual residuals for \(A=1\), \(B=-1\), \(c=0\). The penalty update is applied after the residuals of the current iteration are computed. A symmetric multiplier \(\tau\) is used for increases and decreases; asymmetric update factors require a different interval-map analysis.

The exact penalty map applies after the invariant \(y=bz\) has been established. This happens after one completed ADMM update for every initialization, even when the penalty changes between later iterations. If the invariant state is already stationary, both residuals vanish and the usual rule leaves the penalty unchanged; the residual ratio is then not defined and is not needed.

When a scaled dual variable is used in an implementation, it must be rescaled when \(\rho\) changes so that the unscaled multiplier \(y=\rho u\) is preserved. The analysis is carried out in the unscaled multiplier to avoid that bookkeeping ambiguity.

## Proof
The ADMM updates at penalty \(\rho_k\) are
\[
x^{k+1}=\frac{\rho_k z^k-y^k}{a+\rho_k},
\qquad
z^{k+1}=\frac{y^k+\rho_k x^{k+1}}{b+\rho_k},
\]
\[
y^{k+1}=y^k+\rho_k(x^{k+1}-z^{k+1}).
\]
The \(z\)-optimality relation is
\[
y^k+\rho_k(x^{k+1}-z^{k+1})=bz^{k+1},
\]
so the multiplier update gives \(y^{k+1}=bz^{k+1}\). This proves the invariant after one completed update, without assuming that \(\rho_k\) is constant in time.

For every later iteration,
\[
\rho_k r^{k+1}=y^{k+1}-y^k=b(z^{k+1}-z^k).
\]
The standard dual residual has magnitude
\[
|s^{k+1}|=\rho_k|z^{k+1}-z^k|.
\]
Whenever the update is nonstationary, division yields
\[
\frac{|r^{k+1}|}{|s^{k+1}|}=\frac b{\rho_k^2}.
\]
The three branches of \(\Phi\) now follow directly from the two residual-balancing inequalities.

Put \(L=\sqrt{b/\mu}\) and \(U=\sqrt{\mu b}\), so \(U/L=\mu\). Suppose first that \(\tau\le\mu\). Starting below \(L\), repeated multiplication by \(\tau\) has a first iterate at least \(L\); because the preceding value was below \(L\), this first crossing is below \(\tau L\le U\). It therefore lands in the deadband. The same argument from above uses division: the first iterate at most \(U\) is larger than \(U/\tau\ge L\). Hence every positive penalty enters \([L,U]\) in finitely many adaptive updates and then remains fixed.

Conversely, if \(\tau>\mu\), then \(U/\tau<L\). For any \(\rho\in(U/\tau,L)\), the low branch gives \(\Phi(\rho)=\tau\rho>U\), and the high branch gives \(\Phi(\tau\rho)=\rho\). Thus an exact two-cycle exists. This proves sharpness of the threshold \(\tau=\mu\).

On the invariant manifold, substituting \(y^k=bz^k\) into the \(x\)- and \(z\)-updates gives
\[
z^{k+1}
=\frac{\rho_k^2+ab}{(a+\rho_k)(b+\rho_k)}z^k
=q(\rho_k)z^k.
\]
Since the denominator exceeds the numerator by \(\rho_k(a+b)>0\), one has \(0<q(\rho_k)<1\). A two-cycling penalty therefore multiplies \(z\) by \(q(\rho)q(\tau\rho)\in(0,1)\) every two steps.

Finally,
\[
q'(\rho)=
\frac{(a+b)(\rho^2-ab)}{(a+\rho)^2(b+\rho)^2},
\]
so the unique fixed-penalty minimizer is \(\rho_*=\sqrt{ab}\), agreeing with the scalar specialization of the published quadratic-ADMM parameter theorem. Substitution gives the stated \(q_*\). The condition \(L\le\rho_*\le U\) reduces to \(1/\mu\le a\le\mu\). With \(b=1\) and \(a>\mu\), the whole deadband lies below \(\rho_*\), where \(q\) is decreasing; its best member is therefore \(U=\sqrt\mu\). Direct substitution gives the stated positive limit, while \(q_*\sim2/\sqrt a\).

## Verification
The accompanying `verify.py` uses exact rational arithmetic to replay the unscaled scalar ADMM iteration for many rational choices of \(a\), \(b\), \(\rho\), and initial state. It verifies \(y^{k+1}=bz^{k+1}\), the exact residual identity \(\rho r=b\Delta z\), the ratio \(|r|/|s|=b/\rho^2\), and the recurrence factor \(q(\rho)\). It separately checks the deadband map on rational examples, including finite stabilization when \(\tau\le\mu\) and exact two-cycles when \(\tau>\mu\).

The derivative, interval-crossing argument, and all-parameter sharpness statement are analytic; finite replay is only a consistency check of the formulas and implementation.

## Relationship to prior work
The residual-balancing rule itself is classical. Boyd, Parikh, Chu, Peleato, and Eckstein define the standard primal and dual residuals, give the multiplicative penalty update, and note typical choices \(\mu=10\) and increase/decrease factors equal to \(2\). Their presentation also notes that the scaled dual variable must be adjusted when the penalty changes.

Ghadimi, Teixeira, Shames, and Johansson analyze the same \(\ell_2\)-regularized quadratic ADMM family with a fixed penalty. Their Theorem 1 gives the rate-optimal constant penalty. In the scalar specialization used here it is exactly \(\rho_*=\sqrt{ab}\). That optimizer and the fixed-penalty contraction analysis are therefore prior work; the present claim is the exact dynamics induced by applying residual balancing to this family, the sharp \(\tau\le\mu\) universal stabilization threshold, the period-two obstruction above it, and the quantitative relation between the residual deadband and the known fixed-penalty optimum.

Wohlberg later identified a general scaling flaw in residual balancing and emphasized that the appropriate target ratio of primal to dual residual need not be one. The present scalar theorem is consistent with that critique and makes the mechanism exact: after one update the ratio is \(b/\rho^2\), so the heuristic sees only \(b\) while the rate-optimal penalty depends on both curvatures through \(\sqrt{ab}\). The general scaling critique itself is not claimed as new.

A later robust-penalty paper by McCann and Wohlberg develops an affine fixed-point framework for quadratic ADMM and compares adaptive penalty methods. Its accessible abstract establishes that quadratic penalty selection is a central object of analysis, but the full text was not inspected in this review; an equivalent scalar deadband/cycling theorem there remains a residual originality risk.

## Limitations
The theorem concerns a scalar strongly convex quadratic with the classical residual definitions and symmetric multiplicative update factor. It does not imply that residual balancing cycles on typical large problems, nor that a cycling penalty prevents state convergence. The deadband-to-rate comparison is coordinate-scale dependent, exactly as expected from the known scaling sensitivity of the heuristic.

The claim does not supersede published fixed-penalty optimality results, and it does not establish an optimal adaptive rule. Later adaptive-ADMM literature is extensive. In particular, the full text of the 2024 McCann--Wohlberg paper was not inspected here, so an equivalent special-case calculation in that source cannot be excluded.

## References
1. S. Boyd, N. Parikh, E. Chu, B. Peleato, J. Eckstein, *Distributed Optimization and Statistical Learning via the Alternating Direction Method of Multipliers*, Foundations and Trends in Machine Learning 3(1), 2011, DOI: 10.1561/2200000016.
2. E. Ghadimi, A. Teixeira, I. Shames, M. Johansson, *Optimal Parameter Selection for the Alternating Direction Method of Multipliers (ADMM): Quadratic Problems*, Optimization Online, first public record June 10, 2013; IEEE Transactions on Automatic Control 60(3), 2015, DOI: 10.1109/TAC.2014.2354892.
3. B. Wohlberg, *ADMM Penalty Parameter Selection by Residual Balancing*, arXiv:1704.06209v1, April 20, 2017.
4. M. T. McCann, B. Wohlberg, *Robust and Simple ADMM Penalty Parameter Selection*, IEEE Open Journal of Signal Processing 5 (2024), 402--420, DOI: 10.1109/OJSP.2023.3349115.
