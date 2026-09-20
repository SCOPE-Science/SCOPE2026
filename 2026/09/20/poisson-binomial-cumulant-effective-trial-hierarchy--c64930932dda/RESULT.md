# Cumulant effective-trial hierarchy for Poisson-binomial laws

## Statement

Let
\[
W=\sum_{i=1}^n B_i,
\qquad B_i\sim \operatorname{Bernoulli}(p_i)
\]
with independent summands. Write
\[
v_i=p_i(1-p_i),\qquad V=\kappa_2(W)=\sum_i v_i>0,
\]
and let \(r=\#\{i:0<p_i<1\}\) be the number of nondegenerate Bernoulli summands. The third and fourth cumulants are
\[
\kappa_3=\sum_i v_i(1-2p_i),
\qquad
\kappa_4=\sum_i v_i(1-6v_i).
\]
Define two real-valued effective trial counts
\[
N_3:=\frac{4V^3}{V^2-\kappa_3^2},
\qquad
N_4:=\frac{6V^2}{V-\kappa_4}.
\]
Then
\[
\boxed{4V\le N_3\le N_4\le r\le n.}
\]
The denominator in \(N_3\) is strictly positive whenever \(V>0\).

The equality cases are explicit:

- \(N_3=4V\) iff \(\kappa_3=0\).
- \(N_3=N_4\) iff all nondegenerate \(p_i\) are equal.
- \(N_4=r\) iff all nondegenerate Bernoulli variances \(p_i(1-p_i)\) are equal, equivalently there is \(p\in(0,1/2]\) such that every active \(p_i\in\{p,1-p\}\).
- Hence \(N_3=N_4=r\) iff all nondegenerate \(p_i\) are equal.

## Proof

Put \(w_i=v_i/V\) on the active indices, so that \(w_i>0\) and \(\sum w_i=1\), and define
\[
p_*:=\sum_i w_i p_i.
\]
Since
\[
\frac{\kappa_3}{V}=\sum_iw_i(1-2p_i)=1-2p_*,
\]
we obtain
\[
N_3=\frac{V}{p_*(1-p_*)}.
\]
Therefore \(N_3\ge4V\), with equality iff \(p_*=1/2\), equivalently \(\kappa_3=0\).

Next, with \(A:=\sum_i v_i^2\),
\[
V-\kappa_4=6A,
\qquad
N_4=\frac{V^2}{A}.
\]
Moreover
\[
p_*(1-p_*)-\sum_iw_i p_i(1-p_i)
=\sum_iw_i p_i^2-p_*^2
=\operatorname{Var}_w(p_i)\ge0.
\]
Since \(\sum_iw_i p_i(1-p_i)=A/V\), this gives
\[
\frac{V}{p_*(1-p_*)}\le\frac{V^2}{A},
\]
that is, \(N_3\le N_4\). Equality holds exactly when the active \(p_i\)'s are all equal.

Finally Cauchy--Schwarz on the \(r\) positive numbers \(v_i\) gives
\[
V^2\le rA,
\]
so \(N_4\le r\), with equality exactly when all active \(v_i\)'s are equal. This proves the hierarchy and its equality conditions.

## Sharp low-moment consequences

The hierarchy is equivalent to several exact constraints on the first four cumulants.

First,
\[
\boxed{3\kappa_3^2\le V^2+2V\kappa_4,}
\]
with equality iff all nondegenerate success probabilities are equal. In standardized skewness \(\gamma_1=\kappa_3/V^{3/2}\) and excess kurtosis \(\gamma_2=\kappa_4/V^2\),
\[
\boxed{3\gamma_1^2\le \frac1V+2\gamma_2.}
\]

Second, if the total number of Bernoulli trials is \(n\), then for every \(0<V\le n/4\),
\[
\boxed{|\kappa_3|\le V\sqrt{1-\frac{4V}{n}},}
\]
and this is sharp for every admissible \(V\): equality is attained by taking all \(p_i\)'s equal, with \(p(1-p)=V/n\).

For the fourth cumulant there is an exact fixed-\((n,V)\) interval. Set
\[
k=\lfloor4V\rfloor,\qquad \delta=V-\frac{k}{4}\in[0,1/4).
\]
Then
\[
\boxed{
V-6\left(\frac{k}{16}+\delta^2\right)
\le \kappa_4
\le V-\frac{6V^2}{n}.
}
\]
The upper endpoint is attained exactly when all \(n\) Bernoulli variances are equal; complementary probabilities \(p\) and \(1-p\) may be mixed. The lower endpoint is attained by packing the variance into \(k\) fair Bernoulli variables, one additional Bernoulli variable of variance \(\delta\) when \(\delta>0\), and deterministic variables for the remainder.

For the lower endpoint, maximize \(A=\sum v_i^2\) subject to \(0\le v_i\le1/4\) and \(\sum v_i=V\). If two coordinates lie strictly between \(0\) and \(1/4\), transferring mass from the smaller to the larger while preserving their sum cannot decrease the sum of squares. Iteration leaves at most one interior coordinate, giving \(A_{\max}=k/16+\delta^2\). The upper endpoint follows from \(A\ge V^2/n\).

## Exact consequence for the Berry--Esseen numerator

For a centered Bernoulli summand,
\[
\mathbb E|B_i-p_i|^3=v_i(1-2v_i).
\]
Thus the Lyapunov numerator
\[
L_3:=\sum_i\mathbb E|B_i-p_i|^3
\]
is determined by the fourth cumulant:
\[
\boxed{L_3=V-2\sum_i v_i^2=\frac{2V+\kappa_4}{3}.}
\]
Consequently the exact fixed-\((n,V)\) range is
\[
\boxed{
V-2\left(\frac{k}{16}+\delta^2\right)
\le L_3
\le V-\frac{2V^2}{n}.
}
\]
In particular,
\[
\frac{L_3}{V^{3/2}}
\le \frac1{\sqrt V}-\frac{2\sqrt V}{n},
\]
with equality when all Bernoulli variances are equal. This is a sharp finite-\(n\) refinement of the elementary bound \(L_3\le V\).

## Relation to three-parameter shifted-binomial matching

Peköz, Röllin, Čekanavičius and Shwartz (2009) write \(\lambda_j=\sum_i p_i^j\) and derive the real-valued moment-matching parameters
\[
p^*=\frac{\lambda_2-\lambda_3}{\lambda_1-\lambda_2},
\qquad
n^*=\frac{\lambda_1-\lambda_2}{p^*(1-p^*)}.
\]
Here \(\lambda_1-\lambda_2=V\) and \(\lambda_2-\lambda_3=\sum_i p_i v_i\), so their \(p^*\) equals the variance-weighted \(p_*\) above and
\[
\boxed{n^*=N_3.}
\]
The hierarchy therefore shows that the third-moment-matched real trial count is bounded above by the fourth-cumulant participation count
\[
N_4=\frac{(\sum_i v_i)^2}{\sum_i v_i^2},
\]
which in turn is bounded by the actual number of nondegenerate trials. Thus the first four cumulants alone imply, for every Poisson-binomial representation,
\[
r\ge \lceil N_4\rceil.
\]

## Context and originality

Hoeffding's 1956 extremal theory for sums of independent Bernoulli trials includes the classical fact that, at fixed mean and fixed trial count, equal success probabilities maximize variance. The 2023 survey of Tang and Tang reviews this mean-fixed homogenization principle, stochastic orderings, and Poisson/normal/binomial approximation for Poisson-binomial laws.

The closest direct antecedent found is the 2009 three-parameter shifted-binomial approximation of Peköz, Röllin, Čekanavičius and Shwartz, whose main-results section gives the real moment-matching \(p^*,n^*\) above. The present contribution does not claim that formula, the elementary cumulant formulas, or general moment formulas for Bernoulli sums as new. The claimed new content is the exact hierarchy \(4V\le N_3\le N_4\le r\), its equality characterization, the joint third/fourth-cumulant constraint, and the resulting sharp fixed-variance skewness, kurtosis, and third-absolute-moment envelopes.

To the best of our knowledge, these statements were not located in the inspected Poisson-binomial survey and approximation literature. A residual originality risk remains because Bernoulli-sum moment identities are classical and the 2022 paper of Shuldiner and Oldford develops general central-moment formulas for Bernoulli sums; its abstract and bibliographic record were inspected, but its full text was not checked here for an equivalent inequality stated in different language.

## Verification

`artifacts/verify_cumulant_hierarchy.py` uses exact rational arithmetic to test the hierarchy, the joint cumulant inequality, both fixed-variance projection bounds, the Lyapunov identity and bounds, and representative equality cases. It exhaustively checks 66,429 parameter vectors with lengths one through five over a fixed nine-point rational grid. The recorded output is in `artifacts/verification_output.txt`. These computations are corroborative; the theorem itself is proved above.

## Limitations

The results require independence of the Bernoulli summands. The active-count bound concerns the number of nondegenerate Bernoulli components in a Poisson-binomial representation and does not extend as stated to dependent Bernoulli sums. The moment constraints are necessary for Poisson-binomial laws but are not claimed to characterize the full feasible region of \((V,\kappa_3,\kappa_4)\). No optimal Berry--Esseen constant is claimed; only the exact numerator range is derived.

## References

1. W. Hoeffding, “On the Distribution of the Number of Successes in Independent Trials,” *Annals of Mathematical Statistics* 27 (1956), 713–721. https://doi.org/10.1214/AOMS/1177728178
2. E. A. Peköz, A. Röllin, V. Čekanavičius, and M. Shwartz, “A Three-Parameter Binomial Approximation,” *Journal of Applied Probability* 46 (2009), 1073–1085. https://doi.org/10.1239/jap/1261670689 ; arXiv:0906.2855.
3. W. Tang and F. Tang, “The Poisson Binomial Distribution—Old & New,” *Statistical Science* 38 (2023), 108–119. https://doi.org/10.1214/22-STS852
4. P. Shuldiner and R. W. Oldford, “Bernoulli Sums: The only random variables that count,” arXiv:2110.02363v2 (2022). https://doi.org/10.48550/arXiv.2110.02363
