# Three count-only visits identify Markov availability and detection except at zero temporal memory

## Finding

For a stationary, irreducible two-state Markov availability process observed on three equally spaced occasions through a common imperfect detector, the **unlabelled total number of detections** uniquely determines both latent transition probabilities and the conditional detection probability, provided the latent one-step memory is nonzero. Exactly two visits never identify the three parameters. At zero temporal memory, even arbitrarily long ordered observation histories cannot separate availability from detection. All statements are structural, population-law assertions.

Write \(K=Y_1+Y_2+Y_3\), \(g_k=\Pr(K=k)\), and define quantities computable from the four count probabilities by
\[
m=\frac{g_1+2g_2+3g_3}{3},\qquad S=g_2+3g_3,\qquad T=g_3,\qquad z=\sqrt{T/m}-m.
\]
For every admissible parameter triple with nonzero memory, the unique inverse is
\[
r=\frac{S-3m^2}{mz}-2,\qquad d=m+\frac zr,\qquad \pi=\frac md,\qquad u=\pi(1-r),\qquad v=(1-\pi)(1-r).
\]
Here \(\pi\) denotes stationary availability, \(d\) conditional detectability, \(r\) one-step Markov memory, and \(u,v\) the unavailable-to-available and available-to-unavailable transition probabilities. The inversion is global on the entire admissible nonzero-memory region, including alternating availability \(r<0\) and perfect detection \(d=1\). At \(r=0\), \(K\) is binomial with parameters \(3,m\), where \(m=\pi d\), and neither \(\pi\) nor \(d\) is separately identifiable.

## Assumptions and scope

Consider independently replicated sites at which the species is known to be present throughout the three-visit interval. At every site, the unobserved available/unavailable process \((Z_1,Z_2,Z_3)\in\{0,1\}^3\) starts at stationarity and has the same homogeneous transition matrix
\[
P=\begin{pmatrix}1-u&u\\v&1-v\end{pmatrix},\qquad 0<u<1,\quad 0<v<1.
\]
At visit \(t\), an available species is detected with probability \(d\in(0,1]\), independently between occasions conditional on the latent process; an unavailable species is never detected and false positives are absent. The observed outcome is \(Y_t=Z_tB_t\), with independent conditional detector trials \(B_t\sim\operatorname{Bernoulli}(d)\). Only \(K\), not the ordered vector \((Y_1,Y_2,Y_3)\), is retained for each site. Replicate sites supply the population distribution of \(K\); finite-sample estimation error is outside the theorem. Set
\[
\pi=\frac{u}{u+v}\in(0,1),\qquad r=1-u-v\in(-1,1),\qquad m=\pi d.
\]
The feasible \(r\) is further restricted by \(0<\pi(1-r)<1\) and \(0<(1-\pi)(1-r)<1\). No unmodelled permanent absence, location effect, abundance variation, false alarm, time-varying sensitivity, or between-site parameter mixture is allowed.

## Proof

**Joint detection moments.** Stationarity and the Markov transition yield \(\Pr(Z_{t+1}=1\mid Z_t=1)=1-v=\pi+(1-\pi)r\). Consequently,
\[
\mathbb E Y_t=m,\qquad \mathbb E(Y_1Y_2)=\mathbb E(Y_2Y_3)=m^2+m(d-m)r,
\]
\[
\mathbb E(Y_1Y_3)=m^2+m(d-m)r^2,
\qquad \mathbb E(Y_1Y_2Y_3)=d^3\pi\,[\pi+(1-\pi)r]^2.
\]
The nonadjacent pair formula follows from the two-step Markov transition \(\Pr(Z_3=1\mid Z_1=1)=\pi+(1-\pi)r^2\), while the triple moment follows by multiplying two one-step transitions. Since \(m=\pi d\), the triple moment can be rewritten as
\[
\frac{T}{m}=\big[d\pi+d(1-\pi)r\big]^2
  =\big[m+(d-m)r\big]^2.
\]
The positive square root is the right branch because its unsigned argument equals \(d(1-v)>0\). Thus \(z=(d-m)r\). The factorial second count moment obeys
\[
S=\mathbb E\binom K2=3m^2+mz(2+r).
\]
For \(r\ne0\), both \(d-m=d(1-\pi)>0\) and \(z\ne0\), so these identities solve successively for \(r,d,\pi,u,v\) as stated. Hence different admissible nonzero-memory triples cannot induce the same count law. Conversely, the recovered parameters equal the starting triple, proving exact identification throughout this domain.

**Exceptional region.** At \(r=0\), the latent Markov transition rows agree, so the latent availabilities are independent Bernoulli trials of parameter \(\pi\). All \(Y_t\) are then iid Bernoulli of parameter \(m=\pi d\). Keeping \(m\) fixed and varying \(\pi\in(m,1)\) with \(d=m/\pi\) yields infinitely many admissible parameter sets with the same law of every finite ordered detection history. The three-visit count distribution is exactly \(\operatorname{Binomial}(3,m)\). Moreover, \(z=0\) implies \(r=0\), since \(d-m>0\); the exception is exact, not merely a failure of a chosen formula.

**Two visits cannot suffice.** A two-visit unlabelled count distribution determines only \(m\) and \(C=\Pr(Y_1=Y_2=1)=m^2+m(d-m)r\). For any interior nonzero \(r\), vary \(r\) slightly and choose \(d'=m+(d-m)r/r'\) and \(\pi'=m/d'\): both observables remain unchanged, and admissibility persists for sufficiently small changes (one-sided if \(d=1\)). When \(r=0\), any alternative admissible factorization of \(m=\pi d\) with \(r=0\) produces the same data. Thus no two-visit count law identifies the full parameter triple, whereas three visits do whenever \(r\ne0\). The same two-visit counterargument applies to ordered histories by stationarity, since both mixed one-detection histories have equal probability.

**Sensitivity at the boundary.** Differentiating \((m,S,T)\) with respect to \((\pi,d,r)\) yields
\[
\det\frac{\partial(m,S,T)}{\partial(\pi,d,r)}
=-2d^5\pi^2(1-\pi)[\pi+(1-\pi)r]r^2.
\]
All factors other than \(r^2\) are strictly positive on the stated domain. Hence local invertibility has exactly the same nonzero-memory domain, and its Jacobian degenerates quadratically as \(r\to0\). This mathematical statement concerns identifiability, not a universal finite-sample variance bound.

## Verification

The accompanying `check.py` is self-contained Python using only the standard library. It enumerates all eight latent paths and eight possible observation histories with exact rational arithmetic, sums histories into four unlabelled count probabilities, and reconstructs the original parameters on 687 independently sampled admissible rational triples with positive and negative memory. It checks the zero-memory binomial collapse on three additional exact instances and supplies the following exact example:
\[
\pi=\frac25,\quad d=\frac34,\quad r=\frac12,\quad(u,v)=\bigg(\frac15,\frac3{10}\bigg),
\]
\[
(g_0,g_1,g_2,g_3)=\frac1{16000}(7297,4329,3051,1323),\quad
m=\frac3{10},\quad S=\frac{351}{800},\quad z=\frac9{40}.
\]
The reconstruction returns exactly the stated parameters. The computer tests corroborate the symbolic argument and do not substitute for its global proof. Run `python3 check.py` from the extracted package directory.

## Relationship to prior work

Hines and colleagues (2010) study two-stage cluster detection and occupancy using observation histories; their likelihood framework is highly relevant, but the present result addresses global inversion from a single **unlabelled total count** on known-occupied sites and precisely characterizes the zero-memory obstruction. Hines and colleagues (2014) model correlated replicate surveys using temporal detection histories; the available model-development and discussion sections do not state this count-only minimal-visit inversion. Dekking and Kong (2011) study the Markov-binomial distribution of an **observed** Markov chain, without a separate unknown imperfect detector. Allman, Matias and Rhodes (2009) establish generic hidden Markov identification from the full ordered joint law; a theorem about an ordered law does not by itself demonstrate that the count-aggregation map retains identification. These sources are mathematical context rather than a proof that the present formulation has never appeared. Broader inverse-results for thinned Markov-binomial laws may still imply it.

## Limitations

The result assumes stationary homogeneous latent availability, common conditional detection probability, equal observation spacings, no false positives, known persistent site occupancy, and no site-level heterogeneity. Three visits identify a population law, not arbitrary finite data or parameters estimated without uncertainty. Near \(r=0\), inverse sensitivity is poor, as indicated by the vanishing Jacobian; at exactly \(r=0\) no number of repeated visits resolves the availability/detectability product. This theorem does not establish practical sample-size requirements, robust estimation procedures, identifiability for varying observation intervals, or ecological persistence conclusions. The priority comparison remains provisional pending independent examination of any more general count-thinned Markov-process inverse theorem.

## References

- Hines, J. E., Nichols, J. D., Royle, J. A., MacKenzie, D. I., Gopalaswamy, A. M., Kumar, N. S., and Karanth, K. U. (2010). *Tigers on trails: occupancy modeling for cluster sampling.* Ecological Applications 20(5), 1456–1466. DOI: 10.1890/09-0321.1.
- Hines, J. E., Nichols, J. D., and Collazo, J. A. (2014). *Multiseason occupancy models for correlated replicate surveys.* Methods in Ecology and Evolution. DOI: 10.1111/2041-210X.12186.
- Dekking, F. M., and Kong, D. (2011). *Multimodality of the Markov binomial distribution.* arXiv:1102.3613.
- Allman, E. S., Matias, C., and Rhodes, J. A. (2009). *Identifiability of parameters in latent structure models with many observed variables.* Annals of Statistics 37(6A), 3099–3132. arXiv:0809.5032.
