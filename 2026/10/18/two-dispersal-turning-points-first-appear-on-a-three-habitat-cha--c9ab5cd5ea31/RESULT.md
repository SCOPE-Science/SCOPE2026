# Two dispersal turning points first appear on a three-habitat chain

## Finding

For a stable linear stochastic population model with independent, additive, patch-specific environmental forcing and symmetric nearest-neighbor dispersal at rate \(d\geq0\), **one or two habitat patches cannot produce two distinct strict interior extrema of stationary total-abundance variance** as dispersal varies. On a three-habitat chain, however, this phenomenon occurs with strictly positive, integer-valued local return and noise-intensity parameters. In the explicit example below, regional variance has **exactly one strict local minimum followed by exactly one strict local maximum** for \(d>0\). The behavior persists throughout an open neighborhood of the parameters.

Take the three-node path with local return rates \((2,1,3)\) and independent environmental forcing intensities \((8,1,1)\). Its stationary aggregate variance is exactly

\[
V(d)=\frac{180d^5+1824d^4+6021d^3+8209d^2+4764d+960}{(6d^2+17d+6)(12d^3+80d^2+129d+60)}.
\]

The unique positive critical points are approximately \(d_-=0.062102233838928\) and \(d_+=1.309448514493987\). Variance decreases on \((0,d_-)\), increases on \((d_-,d_+)\), then decreases on \((d_+,\infty)\). In particular the intervention first stabilizes, subsequently destabilizes, and finally stabilizes regional abundance fluctuations again.

## Assumptions and scope

For a connected simple undirected habitat graph \(G\) with \(n\) vertices and graph Laplacian \(L_G\), let \(a_1,\ldots,a_n>0\) be local linear return rates and \(q_1,\ldots,q_n>0\) independent forcing intensities. Consider the centered Ornstein--Uhlenbeck model

\[
\mathrm dX(t)=-K_dX(t)\,\mathrm dt+\operatorname{diag}(\sqrt{q_1},\ldots,\sqrt{q_n})\,\mathrm dW(t),\qquad K_d=\operatorname{diag}(a_1,\ldots,a_n)+dL_G,
\]

where the components of \(W\) are independent standard Brownian motions and \(d\geq0\). The positive definiteness of \(K_d\) gives a unique stationary mean-zero Gaussian law. Let \(C_d\) be its covariance, uniquely specified by \(K_dC_d+C_dK_d=\operatorname{diag}(q_1,\ldots,q_n)\), and define regional variance

\[
V_G(d)=\operatorname{Var}\!\left(\sum_{i=1}^nX_i\right)=\mathbf1^{\mathsf T}C_d\mathbf1.
\]

A *strict turning point* means a positive dispersal rate at which the sign of the derivative changes. For \(n=1\), no coupling parameter is present. For \(n=2\), the only connected graph is a single edge. The theorem concerns this continuous-time linear fluctuation model, not positive-valued nonlinear population trajectories or extinction risk.

## Proof

**Two-habitat exclusion.** Write \(0<a<b\) for the two local return rates and \(A,B>0\) for their independent noise intensities. Direct solution of the \(2\times2\) stationary Lyapunov equation gives

\[
\begin{aligned}
V_2(d)={}&\frac{A(ab+ad+b^2+5bd+4d^2)+B(a^2+ab+5ad+bd+4d^2)}{2(a+b+2d)[ab+(a+b)d]}.
\end{aligned}
\]

Differentiating yields

\[
V'_2(d)=\frac{(b-a)(c_0+c_1d+c_2d^2)}{2(a+b+2d)^2[ab+(a+b)d]^2},
\]

where

\[
\begin{aligned}
c_0&=(a+b)(Ba^2-Ab^2),\\
c_1&=4(a+b)(Ba-Ab),\\
c_2&=2[B(3a+b)-A(a+3b)].
\end{aligned}
\]

The three coefficient signs, in ascending polynomial degree, change at the noise ratios \(A/B=a^2/b^2\), \(A/B=a/b\), and \(A/B=(3a+b)/(a+3b)\), respectively. These thresholds are strictly increasing because \(a<b\). Consequently, in descending-degree order the nonzero coefficients of \(c_2d^2+c_1d+c_0\) have at most one sign change. Descartes' rule of signs therefore gives at most one positive stationary point. If \(a=b\), the sum process has drift \(-a\) irrespective of dispersal, so its variance is the constant \((A+B)/(2a)\). This proves that no one- or two-habitat model in the stated class has two strict interior turning points.

**Three-habitat witness.** For the three-node path \(1-2-3\), choose

\[
K_d=\begin{pmatrix}2+d&-d&0\\-d&1+2d&-d\\0&-d&3+d\end{pmatrix},\qquad Q=\operatorname{diag}(8,1,1).
\]

Solving the six independent entries of \(K_dC_d+C_dK_d=Q\) over the rationals yields the displayed \(V(d)\). Exact differentiation gives

\[
V'(d)=-\frac{P(d)}{(6d^2+17d+6)^2(12d^3+80d^2+129d+60)^2},
\]

where

\[
\begin{aligned}
P(d)={}&8208d^8+72864d^7+229944d^6+245880d^5\\
&-172079d^4-584580d^3-427134d^2-87120d+7200.
\end{aligned}
\]

The denominator is strictly positive for every \(d\geq0\). The descending nonzero coefficient signs of \(P\) are \((+,+,+,+,-,-,-,-,+)\), giving **at most two** positive roots by Descartes' rule. Exact substitution gives \(P(0)=7200>0\), \(P(1/10)<0\), and \(P(3)>0\). The intermediate value theorem therefore supplies at least one positive root in each of \((0,1/10)\) and \((1/10,3)\). The two bounds match: there are precisely two distinct positive roots, necessarily of odd multiplicity, and no other positive stationary points. Their derivative signs give one strict local minimum and one strict local maximum in this order. Algebraic root isolation or numerical evaluation gives the decimal approximations stated above.

**Robustness.** The Lyapunov solution and its dispersal derivative vary continuously with all strictly positive local return and forcing parameters. The three strict derivative inequalities at \(d=0,1/10,3\) persist for every sufficiently small perturbation of the six parameters. Thus an open, full-dimensional parameter neighborhood still has at least two interior turning points. The sharp minimum of three patches follows from the two-habitat exclusion.

## Verification

Run `python verify.py` with SymPy installed. The script symbolically solves the six covariance equations, reconstructs the rational variance, checks the full eighth-degree derivative numerator, checks the three exact derivative-sign witnesses and the Descartes sign pattern, and independently reconstructs the universal two-habitat derivative and threshold-order algebra. These symbolic calculations reproduce the identities used in the proof; the logical deductions from positivity, Descartes' rule, continuity, and the intermediate value theorem are stated above.

Numerically, \(V(0)=8/3\), \(V(d_-)\approx2.665131944\), \(V(d_+)\approx2.696082705\), and \(\lim_{d\to\infty}V(d)=5/2\). The numerical values are illustrations, not the proof of root counts or parameter robustness.

## Relationship to prior work

The ecological question of how spatial coupling alters fluctuation variability is motivated by Wang, Haegeman and Loreau (2015), whose published results discuss local stabilizing effects, spatial synchronization, and heterogeneous **two-patch** metapopulations. The present theorem provides an exact, explicit **three-patch-path** two-turning-point construction and a sharp one-/two-patch exclusion under a specified additive-noise linear model. The prior qualitative statement that dispersal can be stabilizing or destabilizing does not, on its own, imply two opposite changes of derivative sign in the same fixed system.

Kendall and collaborators (2000) analyze dispersal and environmental correlations in spatial population synchrony. Duan and collaborators (2009) discuss network \(H_2\)-norm accumulation under homogeneous coupling; Huang and collaborators (2014) introduce related network-volatility measures. Stationary aggregate variance here is an \(H_2\)-type observable, so these are substantively related frameworks. The claimed contribution is the sharp small-network two-turning-point phenomenon, **not** the general Lyapunov or OU covariance formalism. The available material from these sources does not establish the exact certificate above, but equivalent results under other terminology cannot be ruled out.

## Limitations

The analysis assumes an undirected path, symmetric nearest-neighbor coupling, strictly positive fixed local return rates, independent temporally white additive shocks, and variance of the *sum* rather than variance of a normalized nonlinear biomass process. Additive Gaussian noise is a local linearization and permits negative fluctuations, so the result does not model extinction probabilities or guarantee positivity of total population size. The theorem does not claim a global optimal finite dispersal rate: \(V(d_-)\) is a **local** minimum and the strong-dispersal limit is lower. Bibliographic originality remains subject to independent expert review, especially for other names for network \(H_2\) performance and details not accessible in full texts.

## References

- Wang, S., Haegeman, B., and Loreau, M. (2015). *Dispersal and metapopulation stability*. PeerJ 3:e1295. DOI: 10.7717/peerj.1295. Published October 1, 2015.
- Kendall, B. E., Bjørnstad, O. N., Bascompte, J., Keitt, T. H., and Fagan, W. F. (2000). *Dispersal, environmental correlation, and spatial synchrony in population dynamics*. American Naturalist 155:628–636. DOI: 10.1086/303350.
- Duan, Z., Wang, J., Chen, G., and Huang, L. (2009). *H2 norm accumulation and its impact on synchronisation of complex dynamical networks*. International Journal of Control 82:2356–2364. DOI: 10.1080/00207170903062182.
- Huang, Q., Yuan, Y., Gonçalves, J., and Dahleh, M. (2014). *H2 Norm Based Network Volatility Measures*. American Control Conference proceedings.
