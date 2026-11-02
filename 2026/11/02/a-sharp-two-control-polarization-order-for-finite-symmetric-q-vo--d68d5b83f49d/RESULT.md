# A sharp two-control polarization order for finite symmetric q-voters

## Finding

In the finite symmetric nonlinear \(q\)-voter model with the same number of committed agents for both opinions, **increasing conformity and increasing balanced commitment have competing effects on the distribution of opinion polarization**. This theorem gives exact, distinct thresholds for the likelihood-ratio ordering of the entire stationary polarization law, including a nonempty intermediate regime in which neither likelihood-ratio ordering holds.

Fix an integer \(S\ge4\) of susceptible voters, two positive integer zealot counts \(1\le Z_1<Z_2\) *per opinion*, and two integer consultation sizes \(2\le q_1<q_2\). For each pair \((Z_i,q_i)\), let \(K_i\) denote the equilibrium number of susceptible voters supporting the first opinion, with stationary probabilities \(\pi_i(k)\), and put \(R_i=|2K_i-S|\). Write
\[
m=\frac{S-1}{2},\qquad a_i=m+Z_i,\qquad
F(d)=\frac{\log((a_1+d)/(a_1-d))}{\log((a_2+d)/(a_2-d))},\quad 0<d\le m.
\]
Define \(d_-=1/2\) when \(S\) is even and \(d_-=1\) when \(S\) is odd, and the two **sharp** thresholds
\[
\kappa_-=F(d_-),\qquad \kappa_+=F(m).
\]
Then \(1<\kappa_-<\kappa_+\), and exactly one of the following holds for \(\kappa=q_2/q_1\):

1. If \(\kappa\le\kappa_-\), \(R_2\) is strictly **smaller** than \(R_1\) in likelihood-ratio order (except that a boundary edge may tie). Every proper positive-polarization tail is smaller, and \(K_2\) is strictly smaller than \(K_1\) in convex order.
2. If \(\kappa_-<\kappa<\kappa_+\), the ratio \(\Pr(R_2=r)/\Pr(R_1=r)\) has an interior maximum as a function of the allowable polarization radii, possibly at two adjacent tied radii. Neither radial likelihood-ratio order holds. This statement does **not** assert incomparability in ordinary stochastic or convex order.
3. If \(\kappa\ge\kappa_+\), \(R_2\) is strictly **larger** than \(R_1\) in likelihood-ratio order (with the analogous possible boundary tie). Every proper positive-polarization tail is larger, and \(K_2\) is strictly larger than \(K_1\) in convex order.

The term "strict" means that the distributions differ, all nontrivial radial tail inequalities are strict in the ordered regimes, and every *strictly convex* test function separates the two distributions in the asserted direction. The likelihood-ratio order itself permits equality at a single adjacent radius on a threshold.

**Exact three-regime example.** Keep \(S=20\), raise equal per-opinion zealot counts from \(Z_1=2\) to \(Z_2=5\), and start from \(q_1=5\). Here
\[
\kappa_- =\frac{\log(12/11)}{\log(15/14)}\approx1.2611647423,
\qquad
\kappa_+=\frac{\log(21/2)}{\log(24/5)}\approx1.4990127477.
\]
Consequently consultation sizes \(q_2=6\), \(7\), and \(8\) respectively give less polarization, a genuinely interior likelihood-ratio peak, and more polarization. The checker verifies all adjacent likelihood ratios and every strict radial tail in the ordered cases using exact integer arithmetic.

## Assumptions and scope

The network is complete (well-mixed); everyone holds one of two opinions. Exactly \(S\) agents are susceptible, exactly \(Z\) permanent zealots support each opinion, and the total population is \(N=S+2Z\). At each update, a uniformly selected susceptible may adopt the unanimously held opinion of \(q\) independently sampled other agents; sampling **with replacement** is allowed, and there is no spontaneous flipping. The model has no zealot asymmetry, susceptibility heterogeneity, spatial structure, or observation noise. Under these assumptions the number \(K\) of susceptibles supporting the first opinion is an irreducible birth–death chain on \(\{0,\ldots,S\}\), with rates proportional to
\[
T_k^+=\frac{S-k}{N}\left(\frac{k+Z}{N-1}\right)^q,
\qquad
T_k^-=\frac{k}{N}\left(\frac{S+Z-k}{N-1}\right)^q.
\]
All comparisons keep the susceptible population \(S\) fixed. Changing the zealot count therefore changes \(N\), which is why the theorem compares the **number of polarized susceptibles**, not total-population-normalized magnetization.

Likelihood-ratio ordering of \(R\) means that the ratio of the second to the first radial probability mass is monotone in radius. Convex order of \(K\) means that every convex function of \(K\) has an expectation ordered accordingly; both laws have mean \(S/2\).

## Proof

**Step 1 (stationary weights).** Since both zealot classes are nonempty, the finite chain is irreducible and its stationary distribution is unique. Detailed balance gives the already-known exact formula
\[
\pi_{Z,q}(k)=\frac{\displaystyle\binom Sk\big[(Z)_k(Z)_{S-k}\big]^q}{\displaystyle\sum_{j=0}^S\binom Sj\big[(Z)_j(Z)_{S-j}\big]^q},
\quad (Z)_j=\prod_{t=0}^{j-1}(Z+t).
\]
Indeed, for \(0\le k<S\),
\[
\frac{\pi_{Z,q}(k+1)}{\pi_{Z,q}(k)}
=\frac{S-k}{k+1}\left(\frac{Z+k}{Z+S-k-1}\right)^q
=\frac{T_k^+}{T_{k+1}^-}.
\]
Symmetry yields \(\pi_{Z,q}(k)=\pi_{Z,q}(S-k)\). This formula itself is not claimed as new; it is Eq. (10) of Mobilia (2015).

**Step 2 (a normalized comparison with one sign change).** Let \(h(k)=\pi_2(k)/\pi_1(k)\). For a left-half adjacent step \(0\le k<\lfloor S/2\rfloor\), put \(d=m-k>0\). After cancelling the binomial factors,
\[
\log\frac{h(k+1)}{h(k)}
=q_1\log\frac{a_1+d}{a_1-d}
-q_2\log\frac{a_2+d}{a_2-d}
=q_1\log\frac{a_2+d}{a_2-d}\left(F(d)-\frac{q_2}{q_1}\right).
\]
The allowed positive values of \(d\) are \(m,m-1,\ldots,d_-\). In the odd-\(S\) case the additional central step has ratio exactly one by reflection and cannot alter ordering.

**Step 3 (strict growth of the threshold function).** Set \(a_2>a_1>m\) and
\[
g_a(t)=\frac{2a}{a^2-t^2},\qquad
\log\frac{a+d}{a-d}=\int_0^d g_a(t)\,dt.
\]
The integrand ratio
\[
\frac{g_{a_1}(t)}{g_{a_2}(t)}
=\frac{a_1}{a_2}\frac{a_2^2-t^2}{a_1^2-t^2}
\]
is strictly increasing for \(0<t\le m\), since \(a_2>a_1\). Its \(g_{a_2}\)-weighted average on \([0,d]\), namely \(F(d)\), is therefore strictly increasing in \(d\). Also \(F(d)>1\), since \(a\mapsto\log((a+d)/(a-d))\) strictly decreases for \(a>d\). Because \(S\ge4\), at least two positive radius steps exist and hence \(1<F(d_-)<F(m)\).

**Step 4 (classification).** Moving from the left boundary toward the center, \(d\) strictly decreases, so the sign of \(\log(h(k+1)/h(k))\) can pass from positive to negative at most once. For \(q_2/q_1\le F(d_-)\) it is nonnegative at all such steps, and strictly positive at some; hence \(h\) increases toward the center, and its ratio on radial masses decreases with polarization. For \(q_2/q_1\ge F(m)\), all signs reverse, giving the opposite radial likelihood-ratio order. Strict tail ordering follows by summing the positive masses under a nonconstant monotone likelihood ratio. Between these two sharp cutoffs the extreme signs are opposite, forcing an interior relative-likelihood maximum (possibly an adjacent tie), with neither likelihood-ratio ordering possible. Reflection covers the right half of the chain.

**Step 5 (convex-order consequence).** For any convex \(\varphi\), the symmetric average
\[
H_\varphi(r)=\tfrac12\left[\varphi\left(\frac{S+r}{2}\right)+\varphi\left(\frac{S-r}{2}\right)\right]
\]
is nondecreasing in \(r\), and strictly increasing at distinct radii for strictly convex \(\varphi\). Because the stationary laws are reflection-symmetric, \(\mathbb E[\varphi(K_i)]=\mathbb E[H_\varphi(R_i)]\). Strict stochastic ordering of \(R\) consequently gives the claimed strict convex ordering of \(K\). No convex-order assertion is made in the middle band.

## Verification

The standalone `check.py` uses Python 3 standard-library integer and rational arithmetic. It independently checks the birth–death detailed-balance ratio for 38,556 cases; the discrete single-turn and parameter-regime sign pattern for 87,808 pairs of controls; and exact radial likelihood-ratio and tail inequalities for all three stated integer examples. It also compares 1,568 sampled threshold-function grids in floating point, solely as a numerical corroboration of the analytic monotonic-integral proof. All checks passed. Execute `python3 check.py` from the extracted file's directory. Finite checks do not replace the general proof, and the sampled logarithm comparisons are not offered as exact certificates.

## Relationship to prior work

Mobilia's 2015 full paper establishes this exact birth–death model, detailed-balance stationary formula, and qualitative low-/high-zealotry changes in modality. The present result does **not** claim the stationary formula or the existence of those phases as new. It instead compares two *different* stationary models simultaneously varying both control parameters and proves exact, sharp likelihood-ratio-order cutoffs for the full finite polarization distribution. Those two-control thresholds and interior relative-likelihood shape are not stated in the inspected original work. Mellor, Mobilia, and Zia (2016) study two susceptibility types with differing consultation sizes *within one population*, producing a generally nonreversible two-dimensional chain; their analysis does not imply the present one-dimensional comparative order. Classical linear voter work likewise uses the different \(q=1\) mechanism.

## Limitations

The conclusion is restricted to the fixed-susceptible, balanced-zealot, complete-graph, with-replacement model. The middle region means *only* failure of likelihood-ratio ordering, not necessarily failure of tail or convex ordering. The result is a structural comparison derived from a known exact stationary law; independently assessed historical priority and possible generic likelihood-ratio comparison theorems remain open. No empirical behavior, time-to-consensus, finite-time transient, asymmetric zealot effect, or real-world intervention effect is inferred.

## References

1. M. Mobilia, "Nonlinear \(q\)-voter model with inflexible zealots," first public preprint 16 June 2015, arXiv:1506.04911, especially Sections II and IV and Eq. (10). https://arxiv.org/abs/1506.04911
2. A. Mellor, M. Mobilia, and R. K. P. Zia, "Characterization of the Nonequilibrium Steady State of a Heterogeneous Nonlinear \(q\)-Voter Model with Zealotry," first public preprint 14 January 2016, arXiv:1601.03766. https://arxiv.org/abs/1601.03766
3. M. Mobilia, A. Petersen, and S. Redner, "On the Role of Zealotry in the Voter Model," first public preprint 2007, arXiv:0706.2892. https://arxiv.org/abs/0706.2892
