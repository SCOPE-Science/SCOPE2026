# Exact cyclic-gap law for saturation-excess runoff from two periodic storms

## Finding

Consider a finite hydrological store with exponential between-step depletion, two equal rainfall pulses in each repeated period, and saturation-excess runoff. The *total runoff in the unique periodic state* is completely determined by the shorter cyclic separation of the two pulses. It decreases monotonically as that separation increases, with a strict decrease whenever the more equally spaced arrangement still generates runoff. Thus adjacent pulses maximize saturation-excess runoff, whereas pulses spaced as evenly as the integer period permits minimize it.

More precisely, let \(N\geq 3\) be an integer, \(C>0\) the storage capacity, \(P>0\) the rainfall amount per pulse, and \(0<r<1\) the fraction of storage retained over one time step. Exactly two of the \(N\) periodically repeated steps receive precipitation \(P\), and all other steps receive zero. Let \(g\) be the smaller of their cyclic forward separations, so \(1\leq g\leq \lfloor N/2\rfloor\). Set \(p=P/C\). The total saturation-excess runoff over one period, \(W_g\), is exactly

\[
\frac{W_g}{C}=\max\{0,\;p(1+r^g)+r^N-1,\;2(p-1)+r^g+r^{N-g}\}.
\]

Define the two thresholds

\[
p_0(g)=\frac{1-r^N}{1+r^g},\qquad p_1(g)=1-r^{N-g}.
\]

Then \(p_0(g)\leq p_1(g)\), with equality precisely for equally spaced pulses (\(N=2g\)). For \(p\leq p_0(g)\), neither rainfall pulse causes positive runoff; for \(p_0(g)<p\leq p_1(g)\), exactly one pulse causes positive runoff; and for \(p>p_1(g)\), both do. The intermediate regime is absent in the exactly balanced case.

For \(1\leq g<\lfloor N/2\rfloor\),

\[
W_g\geq W_{g+1},\qquad W_{g+1}>0\ \Longrightarrow\ W_g>W_{g+1}.
\]

For \(N\geq4\), every pulse arrangement has zero runoff if \(p\leq p_0(1)\), while every arrangement has positive runoff if \(p>p_0(\lfloor N/2\rfloor)\). In the intervening range, clustering can cause runoff while the most even spacing prevents it entirely.

For example, at \(N=6\), \(r=1/2\), and \(P/C=3/4\), two pulses separated by one step give \(W_1/C=9/64\), whereas separation by two or three steps gives \(W_2=W_3=0\). Total period rainfall is identical in all three configurations.

## Assumptions and scope

At the end of discrete time step \(t\), let \(S_t\in[0,C]\) be retained storage. If \(P_t\) is rain received in that step, the model is

\[
S_t=\min\{C,rS_{t-1}+P_t\},\qquad O_t=\max\{0,rS_{t-1}+P_t-C\}.
\]

In each cyclic period of length \(N\), exactly two step inputs equal \(P\), and all other inputs equal zero. The period-total excess runoff is \(W_g=\sum_{t=1}^{N}O_t\) on the attracting periodic orbit. The model treats every step identically: instantaneous pulse input, fractional drainage before input, no infiltration-excess component, and no between-pulse positive runoff. Parameters are constant from period to period. The statement concerns modeled saturation-excess volume, not observed flood peak discharge or flow-routing effects.

## Proof

**Existence and uniqueness of the periodic state.** Every one-step storage update is Lipschitz with constant at most \(r\). Hence its \(N\)-step Poincaré map is a contraction with constant at most \(r^N<1\) on \([0,C]\). It has a unique attracting fixed point, so the positive and zero runoff outcomes below are independent of initial storage after transients vanish.

**Reduction to two storage variables.** Normalize post-rainfall storage by \(C\), and let \(a\) and \(b\) be its values immediately after the first and second rain pulses. Label the pulses so that the smaller gap \(g\) precedes \(a\), while \(h=N-g\geq g\) precedes \(b\). During a dry stretch the normalized storage is multiplied by a power of \(r\). Therefore

\[
a=\min\{1,p+r^g b\},\qquad b=\min\{1,p+r^h a\}.
\]

Since \(g\leq h\), any hypothesized \(a<b\) would imply \(p+r^g b>p+r^h a\), hence \(a\geq b\) by monotonicity of the clipping map, a contradiction. Thus \(a\geq b\). The only possible partial-saturation pattern has \(a=1\) before \(b=1\).

**The three regimes.** When neither pulse saturates the storage, solve the linear system to obtain

\[
a=\frac{p(1+r^g)}{1-r^N},\qquad b=\frac{p(1+r^h)}{1-r^N}.
\]

The first value reaches \(1\) at \(p_0=(1-r^N)/(1+r^g)\). One has \(p_0\leq p_1=1-r^h\) because \(r^g\geq r^h\), with equality precisely if \(g=h\).

For \(p_0<p\leq p_1\), the unique fixed point is \(a=1\), \(b=p+r^h\leq1\). Consequently only the event preceding \(a\) gives positive runoff, and its normalized amount is

\[
p+r^g(p+r^h)-1=p(1+r^g)+r^N-1.
\]

At \(p=p_1\), the second pulse only just fills the store, with zero excess. For \(p>p_1\), both post-pulse states equal \(1\), and the sum of both positive excesses is

\[
(p+r^g-1)+(p+r^h-1)=2(p-1)+r^g+r^h.
\]

Below \(p_0\), the excess vanishes. The formulas agree at the regime boundaries. Throughout the intermediate regime, the two-overflow expression does not exceed the one-overflow expression, since their difference is \((p+r^h-1)(1-r^g)\leq0\). Below \(p_0\), both nonzero candidate expressions are nonpositive. Above \(p_1\), the two-overflow expression dominates. This proves the stated maximum-of-three formula and exact runoff counts.

**Strict spacing comparison.** For any adjacent permissible gap indices, \(r^{g+1}<r^g\), so \(p(1+r^{g+1})+r^N-1\) is strictly smaller than its value at \(g\). The other nonconstant candidate also strictly decreases: its difference across consecutive gaps is

\[
(r^g+r^{N-g})-(r^{g+1}+r^{N-g-1})=(1-r)(r^g-r^{N-g-1})>0
\]

for \(g+1\leq\lfloor N/2\rfloor\). The maximum of zero and two strictly decreasing functions is nonincreasing and must decrease strictly whenever its value at the larger gap is positive. This proves optimality, uniqueness where positive, and the precise possible zero-runoff ties. Finally, \(p_0(g)\) increases strictly with \(g\); comparing \(p\) to its endpoint values proves the last assertions.

## Verification

The included standalone, standard-library Python file `verify_bucket.py` checks the piecewise fixed point against the original two-variable recurrence using exact rational arithmetic, verifies both threshold inequalities and the unified maximum formula, and checks all consecutive cyclic-gap comparisons. It passes 42,600 parameter-and-gap instances across six positive rational drainage fractions, period lengths from 3 through 17, and 100 positive rational rain amounts per parameter pair, plus independent boundary and exact-example tests. Run `python3 verify_bucket.py` in the directory containing this result and the script. These finite computations corroborate boundary arithmetic but do not replace the contraction and exact algebraic proof above.

## Relationship to prior work

Finite-capacity water-balance models with threshold overflow are established in hydrology. Milly (1993) analytically studied stochastic storage and runoff under Poisson storm arrivals and random storm depths. McGrath, Hinz and Sivapalan (2007) studied the effects of rainfall timing on threshold-flow event statistics using that stochastic setting. Their detailed rainfall-model and runoff-statistics sections concern random arrivals rather than the exact periodic placement of two fixed pulses. Kusumastuti and coauthors (2007) coupled deterministic, threshold-based rainfall-runoff buckets to stochastic rainfall sequences for flood-frequency analysis. Rogger and coauthors (2013) studied how storage thresholds affect stochastic flood frequency and temporal variability; their Methods describe Poisson yearly storm counts and a threshold runoff coefficient. The present result concerns the deterministic *within-period cyclic-gap optimization* of the complete, clipped recurrence and gives both event-specific onset thresholds and a sharp all-gap ordering. It does not assert that environmental timing effects, saturation-excess runoff, or general smoothing intuitions are new.

## Limitations

The theorem assumes a single spatially homogeneous store, two equal pulses, fixed retention, and a completely periodic forcing pattern. It does not establish an optimal spacing law for three or more unequal pulses, variable drainage rates, spatially distributed storage, arbitrary stochastic storm times, or hydrological peak-flow routing. The sharp statement is about asymptotic model runoff volume. Classical results on deterministic finite-buffer fluid queues or majorization may imply the gap ordering in another formulation; full historical priority has not been independently established. Milly (1993) was accessible through an abstract-level public record rather than its original complete paper. For McGrath et al. (2007), Kusumastuti et al. (2007), and Rogger et al. (2013), the relevant primary methods and conclusions were inspected in full-text formats.

## References

1. Milly, P. C. D. (1993), *An analytic solution of the stochastic storage problem applicable to soil water*, Water Resources Research 29, 3755–3758. DOI: 10.1029/93WR01934. U.S. Geological Survey dated record: https://www.usgs.gov/publications/analytic-solution-stochastic-storage-problem-applicable-soil-water (1 November 1993).
2. McGrath, G. S., Hinz, C., and Sivapalan, M. (2007), *Temporal dynamics of hydrological threshold events*, Hydrology and Earth System Sciences 11, 923–938. DOI: 10.5194/hess-11-923-2007. Open full text: https://hess.copernicus.org/articles/11/923/2007/hess-11-923-2007.pdf. Public discussion commenced 1 September 2006.
3. Kusumastuti, D. I., Struthers, I., Sivapalan, M., and Reynolds, D. A. (2007), *Threshold effects in catchment storm response and the occurrence and magnitude of flood events: implications for flood frequency*, Hydrology and Earth System Sciences 11, 1515–1528. DOI: 10.5194/hess-11-1515-2007. Open full text: https://hess.copernicus.org/articles/11/1515/2007/hess-11-1515-2007.pdf. Public discussion commenced 23 October 2006.
4. Rogger, M., Viglione, A., Derx, J., and Blöschl, G. (2013), *Quantifying effects of catchments storage thresholds on step changes in the flood frequency curve*, Water Resources Research. DOI: 10.1002/wrcr.20553.
