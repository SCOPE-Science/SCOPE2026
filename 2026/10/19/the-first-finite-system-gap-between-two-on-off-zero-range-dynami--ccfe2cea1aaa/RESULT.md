# The first finite-system gap between two on–off zero-range dynamics

## Finding

Initialize every clock ON. For the on–off zero-range process on a three-site ring with two conserved particles, let \(C(c)\) be the stationary probability in the accessible class that the particles occupy the same site. An ON site containing \(n\) particles emits at total rate \(n\); a hop chooses either other site with probability \(1/2\) and makes its destination OFF. In the original process, each OFF clock activates at rate \(c>0\). In the neighbor-gated process, each OFF clock attempts activation at rate \(c\) and succeeds only if a uniformly sampled neighbor is ON. Then
\[
C_{\rm original}(c)=\frac{(c+1)(c+2)}{3c^2+7c+3},\qquad
C_{\rm gated}(c)=\frac{c+2}{3c+4},
\]
and the excess clustering is
\[
C_{\rm original}(c)-C_{\rm gated}(c)
=\frac{c+2}{(3c+4)(3c^2+7c+3)}>0.
\]
This excess tends to \(1/6\) as \(c\downarrow0\) and is asymptotic to \(1/(9c^2)\) as \(c\to\infty\). With all clocks initially ON, this is the smallest system in which the two rules can differ: they agree for two sites with any positive conserved particle count and for one particle on any connected nearest-neighbor graph with at least two sites.

## Assumptions and scope

The sites are labeled and the particles indistinguishable. All dynamics are continuous-time and conserve the particle number. The active class used above is the class accessible from all clocks ON. Empty sites stay ON in that class, since a site can become empty only by an ON departure. If all clock assignments are allowed as initial states, the gated dynamics also has absorbing all-OFF configurations, which are not considered in the stationary probabilities or minimality assertion. Indeed no hop from an ON site can remove the last ON clock. With all clocks OFF, even two sites can distinguish the rules: the gated model is frozen whereas the original allows activation. This is a different initial-state comparison.

## Proof

**Communication.** For three sites and two particles each configuration with empty sites ON has a path to a configuration with all clocks ON via activations. In the gated case there is at least one empty ON site, and every other site is its neighbor. The all-ON configurations communicate by hopping one particle at a time and reactivating the receiver. A double occupation with its clock OFF can be obtained by hopping between two occupied ON sites. A split occupation with one clock OFF can be obtained by hopping from an ON double occupation to an empty site. From a split with one clock OFF, sending the ON particle to the empty site leaves both occupied clocks OFF. Relabeling gives every configuration of each type. The eighteen configurations with empty sites ON therefore form one closed irreducible class in both models.

**Balance.** Aggregate the configurations into five types \(A,B,C,D,E\): double occupation OFF, double occupation ON, split with both occupied sites OFF, split with one occupied site ON, and split with both occupied sites ON. By relabeling, transition rates between types depend only on the starting type. The off-diagonal rates of the resulting Markov chain are
\[
\begin{array}{c|l}
\text{source}&\text{destination and rate}\\\hline
A&B:c\\
B&D:2\\
C&D:\alpha c\\
D&A:1/2,\quad C:1/2,\quad E:c\\
E&A:1,\quad D:1 .
\end{array}
\]
Here \(\alpha=2\) for the original rule, while \(\alpha=1\) for the gated rule: in type \(C\) each OFF clock has just one of its two neighbors ON and activates at rate \(c/2\). In type \(D\) an ON hop either creates a double OFF occupation or goes to the empty site, leaving two occupied OFF sites; the lone OFF clock has both neighbors ON and activates at rate \(c\). In type \(E\) the two unit-rate emitters each send half their rate to the other particle and half to the empty site.

Write \(\pi_X\) for the stationary mass of type \(X\). Balancing the four types other than \(D\) gives
\[
\pi_E=\frac{c}{2}\pi_D,\qquad
\pi_C=\frac{\pi_D}{2\alpha c},\qquad
\pi_A=\frac{1+c}{2c}\pi_D,\qquad
\pi_B=\frac{c}{2}\pi_A.
\]
The fifth balance follows by summing the balance equations. Thus, by normalization and irreducibility,
\[
\pi_A+\pi_B=
\frac{(c+1)(c+2)}{(c+1)(c+2)+2/\alpha+4c+2c^2}.
\]
Substitution of the two values of \(\alpha\) proves the two laws. Their difference has the displayed factorization and its limiting behavior follows from the constant and leading coefficients.

**Minimality.** With only one particle, any OFF site in the accessible class contains that particle, so all its neighbors are ON. With two sites, a jump comes from an ON site and sets only its receiver OFF, and activations only remove OFF clocks. From all clocks ON there is therefore never more than one OFF site. In both cases every relevant OFF clock activates at rate \(c\) under either rule. Three sites and two particles are the first counts that permit type \(C\) with both occupied clocks OFF and a separate ON neighbor.

## Verification

The five-state balance above is an all-parameter algebraic proof for both generators. The accompanying `verify_minimal.py` also checks the original eighteen-state balance and the formula comparisons for positive rational rates; its samples are supplementary and not the proof of the all-rate claim.

## Relationship to prior work

Hirschberg, Mukamel and Schütz (2009) introduced the independent clock-resetting mechanism and studied condensation and the mean-field limit. Their 2012 work, §5, gives a different, solvable neighbor-gated rule and its factorized stationary law. Its symmetric ring with three sites has the hopping and activation rules used here. That product law already implies \(C_{\rm gated}\): substituting \(u(n)=n\) gives one-site weights \(f(0)=1\), \(f(1)=(c+1)/c\), \(f(2)=(c+1)(c+2)/(2c^2)\), so the canonical double versus split weights have ratio \(f(2):f(1)^2\). The direct balance independently recovers this value. Cavallaro, Mondragón and Harris (2015) treat open-boundary dynamics, including exact one-site laws. The finite original-model collision law and its signed gap from the gated law on the active class are the contributions here; the gated product law is not new.

## Limitations

The exact gap is for the three-site ring with uniform hopping, two particles, and total ON departure rate \(n\) at occupation \(n\). It does not assert a larger-system ordering, describe stationary mixtures involving all-OFF absorbing states, or address thermodynamic condensation or reservoirs. A previously published finite-size computation may cover the comparison.

## References

1. O. Hirschberg, D. Mukamel and G. M. Schütz, *Condensation in Temporally Correlated Zero-Range Dynamics* (2009), https://arxiv.org/abs/0906.0709.
2. O. Hirschberg, D. Mukamel and G. M. Schütz, *Motion of condensates in non-Markovian zero-range dynamics* (2012), §5, https://arxiv.org/abs/1207.1006.
3. M. Cavallaro, A. Mondragón and R. J. Harris, *Temporally correlated zero-range process with open boundaries: Steady state and fluctuations* (2015), https://arxiv.org/abs/1504.06309.
