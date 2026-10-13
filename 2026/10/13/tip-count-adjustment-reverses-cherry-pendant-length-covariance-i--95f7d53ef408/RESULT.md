# Tip-count adjustment reverses cherry–pendant-length covariance in the Yule process

## Finding

Consider a constant-rate Yule pure-birth process started from one lineage of age zero. Each extant lineage splits independently at rate \(\lambda>0\). At time \(t>0\), let \(N_t\) be the number of extant lineages, let \(C_t\) be the number of cherries (pairs of extant sibling leaves sharing a parent), and let \(P_t\) be the sum of the ages of all extant lineages, i.e. the total pendant-edge length under this one-lineage initialization.

Put \(r=e^{\lambda t}\). Then
\[
\operatorname{Cov}(C_t,P_t)
=
\frac{6r^5-19r^4+18r^3+12r^2-24r\log r-8r-9}
{36\lambda r^3}
>0.
\]

The positive raw covariance is driven by shared variation in the number of extant lineages. Define the canonical tip-count residuals
\[
U_t=C_t-\frac{N_t}3,
\qquad
V_t=P_t-\frac{N_t}{2\lambda}.
\]
Then the sign reverses:
\[
\operatorname{Cov}(U_t,V_t)
=
-\frac{r^4-6r^2+24r\log r-4r+9}
{36\lambda r^3}
<0.
\]
Their variances are
\[
\operatorname{Var}(U_t)
=
\frac{(r-1)(2r^4+2r^3+2r^2+7r+7)}{45r^4},
\]
and
\[
\operatorname{Var}(V_t)
=
\frac{5r^3-12r\log r-5}{12\lambda^2r^2}.
\]
Consequently
\[
\operatorname{Corr}(U_t,V_t)
\longrightarrow
-\frac{\sqrt6}{12}
\qquad
\text{as }\lambda t\to\infty.
\]

## Assumptions and scope

The process is the standard time-homogeneous Yule pure-birth process with one initial lineage and no extinction. The pendant-length convention includes the age of that initial lineage before its first split. A cherry is counted at time \(t\) exactly when both children of an internal branching event are still extant leaves at time \(t\). No conditioning on \(N_t\) is imposed.

The result concerns an exact mixed moment between a canonical tree-shape statistic and a canonical branch-length statistic. It does not assert a conditional covariance at fixed \(N_t\), nor does it extend here to birth-death processes with extinction.

## Proof

Rescale time by \(\tau=\lambda t\) and write \(L=\lambda P_t\). Let \(H\) be the sum of the dimensionless ages of the extant leaves that belong to cherries, and let \(J\) be the sum of squared dimensionless ages of all extant leaves. Between births, every extant age increases at unit speed.

When a leaf of age \(b\) splits, \(N\) increases by one and \(L\) decreases by \(b\). If the splitting leaf is not in a cherry then a new cherry is created; if it is already in a cherry, the old cherry is destroyed while the two daughters form a new cherry, so the net change in \(C\) is zero. Because each cherry contains two equal-age leaves, splitting a leaf from a cherry removes twice that leaf age from \(H\).

These jump rules close the following moment system, where a prime denotes differentiation with respect to \(\tau\):
\[
\begin{aligned}
(\mathbb EN)'&=\mathbb EN,\\
(\mathbb EN^2)'&=2\mathbb EN^2+\mathbb EN,\\
(\mathbb EC)'&=\mathbb EN-2\mathbb EC,\\
(\mathbb ENC)'&=\mathbb EN^2-\mathbb ENC+\mathbb EN-2\mathbb EC,\\
(\mathbb EC^2)'&=2\mathbb ENC+\mathbb EN-4\mathbb EC^2-2\mathbb EC,\\
(\mathbb EL)'&=\mathbb EN-\mathbb EL,\\
(\mathbb EH)'&=2\mathbb EC-2\mathbb EH,\\
(\mathbb ENL)'&=\mathbb EN^2-\mathbb EL,\\
(\mathbb EJ)'&=2\mathbb EL-\mathbb EJ,\\
(\mathbb EL^2)'&=2\mathbb ENL-2\mathbb EL^2+\mathbb EJ,\\
(\mathbb ECL)'&=\mathbb ENC+\mathbb ENL-3\mathbb ECL-\mathbb EL+\mathbb EH.
\end{aligned}
\]
At \(\tau=0\), \(N=1\) and \(C=L=H=J=0\). Solving gives, with \(r=e^\tau\),
\[
\mathbb EN=r,
\qquad
\mathbb EC=\frac{r-r^{-2}}3,
\qquad
\mathbb EL=\frac{r-r^{-1}}2,
\]
\[
\mathbb EN^2=2r^2-r,
\qquad
\mathbb ENC=\frac{2r^2-r-2r^{-2}+r^{-1}}3,
\]
\[
\mathbb ENL=r^2-\frac{3r}2+1-\frac1{2r},
\qquad
\mathbb EH=\frac{2(r^3-3\log r-1)}{9r^2},
\]
and
\[
\mathbb ECL
=
\frac{12r^5-19r^4+12r^3+6r^2-24r\log r-8r-3}
{36r^3}.
\]
Substituting these expressions into the covariance definitions yields the two displayed covariance formulas. The variance formulas follow similarly from
\[
\mathbb EC^2
=
\frac{(r-1)(10r^5+7r^4+7r^3+17r^2+2r+2)}{45r^4}
\]
and
\[
\mathbb EL^2
=
\frac{3r^4-5r^3+6r^2-6r\log r-3r-1}{6r^2}.
\]

For the residual covariance, define
\[
g(r)=r^4-6r^2+24r\log r-4r+9.
\]
One has \(g(1)=0\) and
\[
g'(r)=4\left(r^3-3r+6\log r+5\right).
\]
The bracket equals \(3\) at \(r=1\), and its derivative is
\[
3(r^2-1)+\frac6r>0
\qquad (r\ge1).
\]
Hence \(g(r)>0\) for \(r>1\), proving the strict negative sign.

For the raw covariance numerator
\[
F(r)=6r^5-19r^4+18r^3+12r^2-24r\log r-8r-9,
\]
one has \(F(1)=F'(1)=F''(1)=0\), \(F'''(1)=36\), and
\[
F''''(r)
=
\frac{24(30r^4-19r^3-2)}{r^3}>0
\qquad (r\ge1).
\]
Thus \(F(r)>0\) for \(r>1\). Finally, the leading terms
\[
\operatorname{Var}(U_t)\sim\frac{2r}{45},
\qquad
\operatorname{Var}(V_t)\sim\frac{5r}{12\lambda^2},
\qquad
\operatorname{Cov}(U_t,V_t)\sim-\frac{r}{36\lambda}
\]
give the limiting correlation.

## Verification

The accompanying `verify.py` independently substitutes all eleven closed-form moment expressions into the differential system, checks both covariance signs on a dense finite grid, and evaluates the limiting-correlation formula numerically at large \(\lambda t\). These computations are finite corroboration; the proof of the all-time statements is the analytic moment closure and sign argument above.

## Relationship to prior work

Classical Yule-tree work gives the fixed-tip-number distribution and moments of the cherry count, while separate branch-length work derives pendant-edge expectations and branch-length distributions. The cited cherry paper gives the familiar fixed-size mean near one third of the tip count and its variance; the cited branch-length papers analyze pendant and interior lengths but do not state the mixed cherry/total-pendant covariance above.

Later joint work on cherries and pitchforks tracks topological pendant-edge types rather than continuous pendant ages. The present mixed moment therefore links two previously separate Yule observables and shows that their raw positive dependence is reversed after removing their common tip-count component.

## Limitations

The originality comparison covered the most directly relevant Yule cherry, pendant-length, branch-length-distribution, and later cherry/pitchfork sources located by exact and semantic searches. Older or differently notated branching-process literature may still encode an equivalent mixed moment. The theorem is for the one-lineage pure-birth Yule process and the stated pendant-length convention only.

## References

McKenzie, A. and Steel, M. (2000). *Distributions of cherries for two models of trees*. Mathematical Biosciences 164(1), 81–92. DOI: 10.1016/S0025-5564(99)00060-7.

Steel, M. and Mooers, A. Ø. (2010). *The expected length of pendant and interior edges of a Yule tree*. Applied Mathematics Letters 23(11), 1315–1319. arXiv:0910.5240.

Stadler, T. and Steel, M. (2012). *Distribution of branch lengths and phylogenetic diversity under homogeneous speciation models*. Journal of Theoretical Biology 297, 33–40. arXiv:1107.5926; DOI: 10.1016/j.jtbi.2011.11.019.

Shpak, M. and Moschopoulos, P. G. (2010). *The distribution of family sizes under a time-homogeneous birth and death process*. Communications in Statistics—Theory and Methods. DOI: 10.1080/03610920902898498.

Choi, K. P., Kaur, G. and Wu, T. (2021). *On asymptotic joint distributions of cherries and pitchforks for random phylogenetic trees*. Journal of Mathematical Biology. DOI: 10.1007/s00285-021-01667-2.
