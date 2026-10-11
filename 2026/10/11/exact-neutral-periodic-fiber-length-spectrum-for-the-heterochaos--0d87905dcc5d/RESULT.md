# Exact neutral-periodic fiber length spectrum for the heterochaos baker maps

## Finding

Let \(M\ge 2\) be an integer, \(0<a,b<1/M\), and let \(f=f_{a,b}\) be the generalized three-dimensional heterochaos baker map defined below. Let \(\Lambda\) be its two-sided smooth symbolic core, and define \(N_n=\{p\in\Lambda:f^n(p)=p,\ \partial_c(f^n)(p)=1\}\). The latter condition means that the central multiplier, not merely some other multiplier, is one.

For every odd positive \(n\), \(N_n=\varnothing\). For every integer \(m\ge1\), \(N_{2m}\) is a disjoint union of finitely many straight, open, center-parallel intervals. The exact number of interval components of Euclidean length \(M^{-j}\), for \(0\le j\le m\), is

\[
K_{M,m}(j)=M^m\left[\binom{2m}{m+j}-\binom{2m}{m+j+1}\right],
\qquad 0\le j\le m,
\]

with the convention \(\binom{2m}{2m+1}=0\). Consequently their total one-dimensional Hausdorff measure is

\[
\mathcal H^1(N_{2m})=M^m\sum_{j=0}^{m} M^{-j}\left[\binom{2m}{m+j}-\binom{2m}{m+j+1}\right].
\]

For each fixed \(M\ge2\), put \(C_M=M(M+1)/(M-1)^2\). The sharp large-period law is

\[
\boxed{\mathcal H^1(N_{2m})\sim \frac{C_M}{\sqrt\pi}\frac{(4M)^m}{m^{3/2}}}\qquad(m\to\infty).
\]

The component count \(M^m\binom{2m}{m}\) was already available at the level of neutral Dyck-shift sequences; the additional conclusions here are the geometric length spectrum and its weighted asymptotics.

There is a corresponding geometric selection phenomenon. Choose an interval component of \(N_{2m}\) uniformly and write its length as \(M^{-J_m}\). For every \(x\ge0\),

\[
\lim_{m\to\infty}\Pr\{J_m/\sqrt m\le x\}=1-e^{-x^2}.
\]

If instead components are sampled with probability proportional to their Euclidean lengths, the induced depth variable \(J_m^{(1)}\) obeys, for each fixed \(j\ge0\),

\[
\lim_{m\to\infty}\Pr\{J_m^{(1)}=j\}
=\frac{(2j+1)M^{-j}}{C_M}.
\]

Thus a uniformly chosen component has depth of order \(\sqrt m\), whereas a length-weighted component has a tight, explicitly known limiting depth distribution. All statements are independent of the allowed parameters \(a,b\).

## Assumptions and scope

Write coordinates as \((u,c,s)\in[0,1]^3\). The expanding base map is

\[
\tau_a(u)=\begin{cases}
(u-(k-1)a)/a,&u\in[(k-1)a,ka),\quad k=1,\ldots,M,\\
(u-Ma)/(1-Ma),&u\in[Ma,1].
\end{cases}
\]

On the branch denoted \(\alpha_k\), where \(u\in[(k-1)a,ka)\), define

\[
f(u,c,s)=\left(\tau_a(u),\frac{c+k-1}{M},(1-Mb)s\right).
\]

On the branch \(\beta_k\), where \(u\in[Ma,1]\) and \(c\in[(k-1)/M,k/M)\), define

\[
f(u,c,s)=\left(\tau_a(u),Mc-k+1,bs+1+b(k-M-1)\right).
\]

As usual, the last \(\beta_M\) branch includes the upper endpoint. The symbol \(\Lambda\) denotes the maximal invariant set with a complete two-sided orbit remaining in interiors of these branch domains. The claim concerns \(f^n\)-fixed points in \(\Lambda\), not points of exact least period \(n\), and excludes ambiguous discontinuity boundaries. The planar map obtained by discarding the stable coordinate shares the same central itinerary mechanism, but the measure formula is claimed here only for the stated three-dimensional map. Euclidean lengths and \(\mathcal H^1\) use the standard unscaled coordinate metric.

## Proof

**1. Return multiplier and affine decoupling.** The derivative of the center coordinate on an \(\alpha_k\) branch is \(M^{-1}\), and on a \(\beta_k\) branch it is \(M\). Thus a smooth \(n\)-periodic point has neutral central multiplier exactly when its itinerary contains equal numbers of \(\alpha\) and \(\beta\) symbols. This requires \(n=2m\). The base coordinate expands strictly on every branch, so each prescribed binary/labeled forward itinerary has at most one periodic \(u\)-coordinate. The stable coordinate is a strict contraction on every branch, so each full itinerary has at most one periodic \(s\)-coordinate. Both unique coordinates exist in the appropriate branch interiors for balanced, compatible labeled itineraries: inverse base branches are contractions onto distinct interior strips, and the stable forward branches have disjoint output strips; because a balanced itinerary uses both types, the periodic coordinates avoid outer and internal boundaries. Distinct compatible labeled words therefore yield disjoint center fibers.

**2. Bracket-cancellation criterion.** On the center interval, introduce maps \(g_k(c)=(c+k-1)/M\). An \(\alpha_k\) step is \(g_k\); a \(\beta_k\) step is \(g_k^{-1}\), defined on \(g_k((0,1))\). For any binary itinerary containing \(m\) steps of each type, set \(h_0=0\) and \(h_i=\#\{\alpha\text{ in steps }1,\ldots,i\}-\#\{\beta\text{ in steps }1,\ldots,i\}\). Then \(h_{2m}=0\). Cyclically start the word at a global minimum of \(h_i\); the rotated type word is a Dyck path (all its partial heights are nonnegative). For its center return to fix a nonempty open interval, each closing symbol \(\beta_k\) must be paired with the innermost unmatched \(\alpha_k\) of the same label. If labels disagree, inverse-branch domain intervals are disjoint in their interiors, and no open center fiber survives. Conversely, every assignment of one of \(M\) labels to each of the \(m\) matched pairs produces identity center return on the entire open interval \((0,1)\) at the selected minimum-phase section. Hence every balanced binary word yields exactly \(M^m\) valid labeled center-neutral periodic words.

**3. Physical fiber length at the fixed time cut.** Set \(j=-\min_{0\le i\le2m}h_i\). At the original time cut, the stack height is exactly \(j\) above that of the chosen cyclic minimum. Passing from minimum-phase center coordinate to the original cut cancels all closed brackets and leaves exactly \(j\) unmatched prefix contractions \(g_k\), each with derivative \(1/M\). Therefore the original-cut center fiber is a translated base-\(M\) cylinder of Euclidean length \(M^{-j}\), with endpoints excluded. There are no isolated smooth center-neutral periodic points: on any fixed itinerary the center return is affine with slope one, so it is either identity (yielding that interval) or a nonzero translation (yielding no fixed point). The finite component decomposition follows.

**4. Exact reflection count.** Among \(\binom{2m}{m}\) binary bridges with \(m\) up-steps and \(m\) down-steps, the reflection principle gives the number whose minimum is at least \(-j\) as \(\binom{2m}{m}-\binom{2m}{m+j+1}\). Subtracting the case with minimum at least \(-(j-1)\), the number with minimum exactly \(-j\) is \(B_m(j)=\binom{2m}{m+j}-\binom{2m}{m+j+1}\). Multiplication by the \(M^m\) independent valid bracket labels proves \(K_{M,m}(j)\). The disjoint union of finitely many straight open intervals has \(\mathcal H^1\) equal to their summed lengths, proving the finite formula. In particular, \(\sum_{j=0}^m B_m(j)=\binom{2m}{m}\), recovering the previously known unweighted symbolic count, but not using it as a novel assertion.

**5. Sharp length asymptotic.** Elementary binomial algebra gives

\[
B_m(j)=\binom{2m}{m+j}\frac{2j+1}{m+j+1}.
\]

For every fixed \(j\), \(m B_m(j)/\binom{2m}{m}\to 2j+1\). For all \(0\le j\le m\), the same quantity is at most \(2j+1\). Because \(M\ge2\), dominated convergence applies to the geometrically weighted sum, giving

\[
\frac{m}{\binom{2m}{m}}\sum_{j=0}^{m}M^{-j}B_m(j)
\longrightarrow \sum_{j=0}^{\infty}(2j+1)M^{-j}
=\frac{M(M+1)}{(M-1)^2}=C_M.
\]

Finally \(\binom{2m}{m}\sim4^m/\sqrt{\pi m}\) by Stirling's formula, yielding the stated precise \(\mathcal H^1\) asymptotic.

**6. Two depth distributions.** Uniformly sampling components cancels the factor \(M^m\). For every integer \(j\in[0,m]\), the reflection formula telescopes to

\[
\Pr(J_m\le j)=1-\frac{\binom{2m}{m+j+1}}{\binom{2m}{m}}.
\]

For \(j=\lfloor x\sqrt m\rfloor\), the ratio of successive binomials or Stirling's formula gives a limit \(e^{-x^2}\), proving the distributional law. Under length weighting, \(\Pr(J_m^{(1)}=j)=M^{-j}B_m(j)/\sum_{k=0}^m M^{-k}B_m(k)\). The dominated-convergence limit in step 5 yields the displayed discrete probability distribution. Its probabilities sum to one by the definition of \(C_M\), so no mass escapes to infinity.

## Verification

A standalone, standard-library-only checker `verify.py` enumerates every word over the \(2M\) branch symbols for \(M=2,3\) and \(m=1,2,3\). It uses exact rational arithmetic to intersect the admissible central intervals, checks that the full center return is the identity, and reconstructs the unique unstable and stable periodic coordinates for admissibility in branch interiors at \(a=1/(M+2)\) and \(b=1/(M+3)\). It independently compares the exact length histograms with the reflection-principle formulas. Executing `python3 verify.py` prints `CHECK_OK` on success. These are finite cross-checks, not an argument for the all-period result; the proof is in the preceding section.

For example, at \(M=2\) and \(m=2\), the predicted interval histogram is \(8\) intervals of length \(1\), \(12\) of length \(1/2\), and \(4\) of length \(1/4\), for \(\mathcal H^1(N_4)=15\). The exact enumerator agrees.

## Relationship to prior work

Saiki, Takahasi and Yorke introduced heterochaos baker maps and exhibited neutral period-two segments; their 2018 preprint focused on heterogeneity of *hyperbolic* periodic points. Takahasi and Yamamoto proved the Dyck-system symbolic coding in their 2022 preprint, and Saiki, Takahasi, Yamamoto and Yorke discussed non-singleton center fibers in their 2024 review. Takahasi's 2024 paper specifically excluded nonhyperbolic periodic continua from its equidistribution theorem and stated the exact count \(M^m\binom{2m}{m}\) of neutral *symbolic* period-\(2m\) points (Equation (2.6)). These prior existence, coding and count results are not claimed as new. The present contribution assigns exact **Euclidean lengths** to the corresponding geometric periodic fibers, computes their total \(\mathcal H^1\), and identifies a length-weighted selection law distinct from uniform component statistics. Takahasi and Tsujii proved an algebraic correlation-decay law at a mostly-neutral parameter boundary using random-walk excursions; that is a transfer-operator/mixing statement, not a count or Hausdorff-length formula for neutral periodic fibers throughout the present parameter region. Saiki, Takahasi and Yorke studied Hausdorff dimensions of Cantor *heteroclinic intersections* in smooth heterochaos horseshoe diffeomorphisms, a different object from the fixed-fiber length spectrum of the piecewise-affine baker map. Published general reflection-principle counting is used, not reasserted as original.

## Limitations

The statement uses the smooth two-sided core, not boundary periodic points of a discontinuous extension. It counts points fixed by the \(2m\)-th iterate, not primitive period \(2m\); removing proper divisors changes the statistic. The asymptotic keeps \(M\) fixed. It does not claim robustness under nonlinear perturbations, Hausdorff dimension of a limit set across all periods, or a law for every neutral invariant measure. Prior-art searches cannot certify absolute publication priority; an equivalent statement in unindexed geometric symbolic-dynamics literature remains a residual risk.

## References

1. Y. Saiki, H. Takahasi and J. A. Yorke, *Piecewise linear maps with heterogeneous chaos*, arXiv:1811.01009v4 (first public 2018-11-02); see Section 1.4 for a neutral period-two segment.
2. H. Takahasi and K. Yamamoto, *Heterochaos baker maps and the Dyck system: maximal entropy measures and a mechanism for the breakdown of entropy approachability*, arXiv:2209.04905v1 (2022-09-11); see Theorem A and Section 1.3.
3. Y. Saiki, H. Takahasi, K. Yamamoto and J. A. Yorke, *The dynamics of the heterochaos baker maps*, arXiv:2401.00836v2 (first public 2024-01-01); see Sections 2.1 and 3.5.
4. H. Takahasi, *Distributions of periodic points for the Dyck shift and the heterochaos baker maps*, arXiv:2409.01261v1 (first public 2024-09-02); see Sections 1.1, 2.5 (Equation (2.6)) and 3.2.
5. T. Hamachi and K. Inoue, *Embedding of shifts of finite type into the Dyck shift*, Monatshefte für Mathematik **145** (2005), 107–129; cited for earlier Dyck periodic-point enumeration, not used as a statement on geometric fiber lengths.
6. H. Takahasi and M. Tsujii, *Polynomial rate of mixing for the heterochaos baker maps with mostly neutral center*, arXiv:2408.16618v1 (2024-08-29); see Sections 1.1–1.3 and the central random-walk estimate.
7. Y. Saiki, H. Takahasi and J. A. Yorke, *Hausdorff dimension of Cantor intersections and robust heterodimensional cycles for heterochaos horseshoe maps*, arXiv:2011.12264v4 (first public 2020-11-24); see Sections 1.1–1.2.
