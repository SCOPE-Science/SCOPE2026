# Sharp phase law for independent culling of two exchanging pest patches

## Finding

Two habitats exchange individuals continuously while each habitat receives one fixed-fraction culling intervention per period. In the irreducibly coupled, two-dimensional linear pest-growth model defined below, **simultaneous culling uniquely minimizes the asymptotic pest multiplication factor**, while **half-period-staggered culling uniquely maximizes it**, even with unequal intrinsic growth, asymmetric exchange and unequal culling efficacies. The phase effect is given by an exact positive hyperbolic-product identity. In a concrete exact-parameter example, simply changing phase, without changing either cull or the period, switches the pest-free state from exponentially attracting to exponentially repelling.

Let \(T>0\), \(b,c>0\), \(a,d\in\mathbb R\), and \(0<s_1,s_2<1\). Define
\[
G=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
D_1=\operatorname{diag}(s_1,1),\qquad D_2=\operatorname{diag}(1,s_2).
\]
Patch 1 is culled at time zero in each period and patch 2 at phase \(\delta\in[0,T]\), with free growth \(\dot x=Gx\) between jumps. One monodromy is
\[
M_\delta=e^{G(T-\delta)}D_2e^{G\delta}D_1.
\]
Put \(\tau=(a+d)/2\), \(h=(a-d)/2\), \(\kappa=\sqrt{h^2+bc}>0\), and
\[
\begin{aligned}
H_0&=e^{\tau T}\left[(s_1+s_2)\cosh(\kappa T)
 +(s_1-s_2)\frac h\kappa\sinh(\kappa T)\right],\\
B&=\frac{(1-s_1)(1-s_2)bc\,e^{\tau T}}{\kappa^2}>0,\\
\Delta&=s_1s_2e^{2\tau T}>0.
\end{aligned}
\]
Then, for every \(\delta\in[0,T]\),
\[
\boxed{\operatorname{tr}M_\delta=H_0+B\sinh(\kappa\delta)\sinh(\kappa(T-\delta)),\qquad \det M_\delta=\Delta.}
\]
Consequently the Perron multiplier is
\[
\boxed{\rho(M_\delta)=\frac{H_\delta+\sqrt{H_\delta^2-4\Delta}}2,\qquad H_\delta=\operatorname{tr}M_\delta.}
\]
It is strictly increasing on \([0,T/2]\), strictly decreasing on \([T/2,T]\), and symmetric about \(T/2\). Thus \(\delta=0\) modulo \(T\) is the sole minimizing phase and \(\delta=T/2\) the sole maximizing phase.

When \(\Delta<1\), the positive zero state is linearly asymptotically stable precisely at the phases with \(H_\delta<1+\Delta\), unstable at those with \(H_\delta>1+\Delta\), and marginal at equality. If \(H_0<1+\Delta<H_{T/2}\), there is exactly one critical phase \(\delta_c\in(0,T/2)\), and stability holds precisely for phases within distance \(\delta_c\) of synchrony, modulo \(T\). Explicitly,
\[
\boxed{\delta_c=\frac T2-\frac1{2\kappa}\operatorname{arcosh}\left(\cosh(\kappa T)-\frac{2(1+\Delta-H_0)}B\right).}
\]
If \(\Delta\ge1\), no phase has a multiplier below one.

## Assumptions and scope

The state \(x=(x_1,x_2)^\mathsf T\) consists of small, nonnegative pest abundances in two coupled habitat patches. The underlying linearization may arise from \(\dot x_1=(g_1-m_{12})x_1+m_{21}x_2\) and \(\dot x_2=m_{12}x_1+(g_2-m_{21})x_2\), with strictly positive dispersal rates \(m_{12},m_{21}\). Negative effective diagonal coefficients are allowed. Each instantaneous cull multiplies the target abundance by the fixed survival fraction \(s_i\), leaving the other patch unchanged. The pulses are administered exactly once to each patch per common period \(T\). At \(\delta=0\) or \(T\) their order is immaterial because the two diagonal culling matrices commute. The theorem concerns the local exponential invasion/extinction multiplier of this linear model; it does not assert global extinction of a nonlinear ecosystem.

## Proof

**1. Propagation and cross-terms.** Set \(K=G-\tau I\). The relation \(K^2=(h^2+bc)I=\kappa^2I\) proves by the exponential power series that
\[
E(t):=e^{Gt}=e^{\tau t}\left(\cosh(\kappa t)I+\frac{\sinh(\kappa t)}\kappa K\right).
\]
In particular, for \(t\ge0\),
\[
E(t)_{12}=\frac{b}{\kappa}e^{\tau t}\sinh(\kappa t),\qquad
E(t)_{21}=\frac{c}{\kappa}e^{\tau t}\sinh(\kappa t).
\]
For positive \(t\) both are positive. Moreover, \(E(t)\) has strictly positive diagonal entries by positivity of the Metzler semigroup (or directly \(\cosh z>|h|\sinh z/\kappa\)).

**2. Trace defect.** Let \(P_1=\operatorname{diag}(1,0)\), \(P_2=\operatorname{diag}(0,1)\), \(u=1-s_1>0\), and \(v=1-s_2>0\). Expand \(D_i=I-(1-s_i)P_i\), apply \(E(T-\delta)E(\delta)=E(T)\), and cycle the trace:
\[
\begin{aligned}
\operatorname{tr}M_\delta
 &=\operatorname{tr}E(T)-u\operatorname{tr}(E(T)P_1)
 -v\operatorname{tr}(E(T)P_2)\\
 &\quad+uv\operatorname{tr}(E(T-\delta)P_2E(\delta)P_1)\\
 &=\operatorname{tr}(E(T)D_1D_2)
 +uv E(T-\delta)_{12}E(\delta)_{21}.
\end{aligned}
\]
The mixed term at simultaneous phase vanishes, since \(P_1P_2=0\). Inserting the propagation entries establishes the displayed positive \(B\) formula and \(H_0\) expression for every phase, endpoints included.

**3. Determinant, Perron root and sharp phase order.** Multiplicativity of determinants and \(\det e^{Gt}=e^{\operatorname{tr}G\,t}\) give \(\det M_\delta=s_1s_2e^{(a+d)T}=\Delta\). All entries of \(M_\delta\) are strictly positive, including at the endpoints, because \(T>0\), \(b,c>0\) and both survival factors are positive. Hence the two eigenvalues are distinct, real and positive: their discriminant is \((M_{11}-M_{22})^2+4M_{12}M_{21}>0\), their sum is positive and their product is \(\Delta>0\). Consequently the larger eigenvalue \(\rho=(H+\sqrt{H^2-4\Delta})/2\) increases strictly with \(H\) for fixed \(\Delta\); indeed \(d\rho/dH=(1+H/\sqrt{H^2-4\Delta})/2>0\).

The elementary identity
\[
\sinh(\kappa\delta)\sinh(\kappa(T-\delta))
 =\tfrac12\left(\cosh(\kappa T)-\cosh(\kappa(T-2\delta))\right)
\]
shows strict increase from zero to its unique peak at \(T/2\) and strict decrease back to zero, because \(\kappa>0\). Since \(B>0\), the phase order is strict with only the stated equality phases.

**4. Threshold classification and exact reversal witness.** For two distinct positive eigenvalues whose product is \(\Delta<1\), the larger one is below, equal to, or above one exactly when their sum \(H\) is below, equal to, or above \(1+\Delta\). At \(\Delta\ge1\), the larger positive eigenvalue is strictly above one. Solving the preceding hyperbolic-product identity at \(H=1+\Delta\) yields the stated unique \(\delta_c\) provided \(H_0<1+\Delta<H_{T/2}\).

For an exact example let \(q=97/100\), \(T=1\), \(s_1=s_2=1/2\), and
\[
G=\begin{pmatrix}\log q&\log2\\\log2&\log q\end{pmatrix},\qquad
E(1)=\frac q4\begin{pmatrix}5&3\\3&5\end{pmatrix},\qquad
E(1/2)=\sqrt{\frac q8}\begin{pmatrix}3&1\\1&3\end{pmatrix}.
\]
This is a positive-migration, positive-unculled-growth example, as \(g_1=g_2=\log(2q)>0\). Direct exact multiplication gives
\[
\begin{array}{c|c|c|c}
\text{phase}&H&\Delta&H-(1+\Delta)\\\hline
0&97/80&9409/40000&-909/40000\\
1/2&3977/3200&9409/40000&607/80000
\end{array}
\]
and
\[
\rho(M_0)=97/100<1,\qquad
\rho(M_{1/2})=\frac{3977+291\sqrt{73}}{6400}>1.
\]
Thus keeping both treatment strengths, frequency, and local growth fixed but staggering them by half a period changes extinction into growth. The unique critical phase is approximately \(0.2461198104\) of a period (and its reflection), for these parameters.

## Verification

Run the included standalone program `python3 check.py` with Python 3; it depends only on the standard library. It independently obtains the matrix exponential using a scaling-and-squaring power series rather than the hyperbolic closed form. For 1,500 seeded admissible parameter choices it checks the trace, determinant, reflection symmetry, maximal and minimal phase bounds, and positive discriminant; it also uses exact rational arithmetic to verify the two example traces, shared determinant and opposite spectral-threshold signs. The packaged program passed 9,005 assertions. These finite tests complement, but do not replace, the universal analytic proof above.

## Relationship to prior work

Terry (2010), published online January 20, studies independent impulsive adult culling in two patches **with juvenile-adult structure and delay**, proving eradication conditions and exhibiting simulations. Georgescu, Dimitriu and Sinclair (2010) analyze a two-patch SI integrated-pest-management system with dispersal and a **simultaneous spraying matrix** by Floquet methods. Ives and Settle (1997) and Byers and Castle (2005) motivate synchrony versus asynchronous control; in particular, Byers and Castle already report a qualitative synchronization advantage in an areawide, threshold-triggered simulation model. These antecedents establish the ecological problem and the qualitative phenomenon, not a claim of previously unknown benefits from synchronized control. Browne, Smith and Bourouiba (2014), in a two-region SIR vaccination model, prove a **local** synchrony optimum under identical-patch and no-infected-migration assumptions (Theorem 5), and show numerical phase-induced eradication-versus-persistence changes for broader epidemiological settings. Their pulses reduce the susceptible class and the effective reproduction number is computed via time-varying infection coefficients; they do not derive the present direct-cull constant two-state Floquet trace law. The assessed mathematical contribution is the **all-parameter sharp continuous phase-ordering formula** in the specified constant two-state system, and its exact phase-dependent Floquet stability reversal at fixed treatment strengths. The inspected full Terry and Georgescu texts do not contain this universal two-local-pulse theorem. A broader historical novelty claim is not proven.

## Limitations

Only a two-dimensional, constant-coefficient positive linear model is covered. Culls have fixed multiplicative survival factors and exactly one event per patch each period. The full-text historical-priority comparison remains limited for Ives and Settle and Byers and Castle, which were inspected at the abstract level rather than in full, and related wider literature may contain equivalent matrix inequalities. No global nonlinear pest-eradication, pesticide-safety, ecological-outcome, cost-optimality, or empirical-field conclusion follows. Near the threshold, measurement and timing uncertainties can change the practical verdict. Numerical tests do not certify all real parameter values independently of the proof.

## References

1. A. J. Terry, “Impulsive culling of a structured population on two patches,” *Journal of Mathematical Biology* 61 (2010), 843–875; first publicly online 2010-01-20. DOI: [10.1007/s00285-009-0325-0](https://doi.org/10.1007/s00285-009-0325-0). Full author-uploaded text: https://www.researchgate.net/publication/41089669_Impulsive_culling_of_a_structured_population_on_two_patches
2. P. Georgescu, G. Dimitriu, R. Sinclair, “Impulsive control of an integrated pest management model with dispersal between patches,” *Journal of Biological Systems* 18 (2010), 535–569. DOI: [10.1142/S0218339010003561](https://doi.org/10.1142/S0218339010003561). Author-hosted full text: https://math.etti.tuiasi.ro/pg/papers/JBS10.pdf
3. A. R. Ives, W. H. Settle, “Metapopulation dynamics and pest control in agricultural systems,” *The American Naturalist* 149 (1997), 220–246. DOI: [10.1086/285988](https://doi.org/10.1086/285988).
4. J. A. Byers, S. J. Castle, “Areawide models comparing synchronous versus asynchronous treatments for control of dispersing insect pests,” *Journal of Economic Entomology* 98 (2005), 1763–1773. DOI: [10.1603/0022-0493-98.6.1763](https://doi.org/10.1603/0022-0493-98.6.1763).
5. C. J. Browne, R. J. Smith, L. Bourouiba, “From regional pulse vaccination to global disease eradication: insights from a mathematical model of poliomyelitis,” *Journal of Mathematical Biology* 71 (2015), 215–253; preprint arXiv:1309.0265 (2013). DOI: [10.1007/s00285-014-0810-y](https://doi.org/10.1007/s00285-014-0810-y). Full author-uploaded preprint: https://www.researchgate.net/publication/264392661_From_regional_pulse_vaccination_to_global_disease_eradication_insights_from_a_mathematical_model_of_poliomyelitis
