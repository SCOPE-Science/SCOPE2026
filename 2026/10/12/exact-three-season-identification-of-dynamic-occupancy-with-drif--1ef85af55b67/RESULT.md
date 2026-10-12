# Exact three-season identification of dynamic occupancy with drifting detection

## Finding

A single detection or nondetection at each of three consecutive ecological survey seasons identifies **all six parameters** of a time-homogeneous, two-state colonization–persistence model even when each season has a different, completely unknown detection probability, provided colonization and persistence are unequal. The result is exact, global, and sharp: two seasons do not suffice, and the degenerate equal-transition case is unidentifiable with any number of such observations.

Write \(m_t=\Pr(Y_t=1)\), \(d_{ij}=\Pr(Y_i=1,Y_j=1)\), and, from the eight exact binary-history probabilities, form

\[
 r_2=\frac{d_{12}}{m_1},\quad r_3=\frac{d_{23}}{m_2},\quad
 h_2=\frac{m_2}{r_2},\quad h_3=\frac{m_3}{r_3},\quad
 T=\frac{d_{13}}{m_1r_3}.
\]

Then set

\[
 \delta=\frac{T-h_3}{1-h_2},\qquad b=T-\delta,\qquad
 s=\frac{\delta}{1-b},\qquad c=bs,\qquad
 \pi=\frac{sh_2-c}{\delta},\qquad
 (p_1,p_2,p_3)=\left(\frac{m_1}{\pi},\frac{r_2}{s},\frac{r_3}{s}\right).
\]

These expressions recover every parameter uniquely on the entire strictly interior region \(c\ne s\); none of their denominators vanishes there. In particular, seasonal detection probabilities need **not** be equal and initial occupancy need **not** be stationary.

## Assumptions and scope

Let \(Z_t\in\{0,1\}\) denote actual occupancy in season \(t\in\{1,2,3\}\). Set \(\Pr(Z_1=1)=\pi\), and assume the homogeneous hidden-state transitions

\[
 \Pr(Z_{t+1}=1\mid Z_t=0)=c,\qquad
 \Pr(Z_{t+1}=1\mid Z_t=1)=s,\qquad t=1,2.
\]

All six numbers \(\pi,c,s,p_1,p_2,p_3\) are strictly between zero and one. Observed detections \(Y_t\in\{0,1\}\) have no false positives: \(\Pr(Y_t=1\mid Z_t=0)=0\) and \(\Pr(Y_t=1\mid Z_t=1)=p_t\). Conditional on the complete hidden path, the three observations are independent. The full joint probability distribution of \((Y_1,Y_2,Y_3)\) is assumed known exactly, e.g. as a population-level limiting law across independently surveyed homogeneous sites. Nothing requires the hidden chain to start in its stationary distribution.

The result is a *structural* identifiability statement for this precise model, not a finite-sample estimator or a test for hidden Markov model assumptions. A seasonal detection means at least one successful survey at that season; here only **one** unreplicated detection is used per season.

## Proof

**1. Reduction to observable moments.** Write \(z_t=\Pr(Z_t=1)\), and \(\delta=s-c\). Marginal occupancy obeys

\[
 z_1=\pi,\qquad z_{t+1}=c+\delta z_t,\qquad m_t=z_tp_t.
\]

No false positives imply that observing \(Y_1=1\) certifies \(Z_1=1\). Hence

\[
 d_{12}=m_1sp_2,\qquad d_{23}=m_2sp_3.
\]

Therefore \(r_2=sp_2\), \(r_3=sp_3\), \(h_2=z_2/s\), and \(h_3=z_3/s\). All displayed quantities are positive under the strict interior assumptions. In addition, two-step hidden transition probability from occupied to occupied equals \(s^2+(1-s)c=c+s(s-c)\), so

\[
 d_{13}=m_1p_3[c+s(s-c)],\qquad
 T=\frac{d_{13}}{m_1r_3}=\frac cs+\delta.
\]

Put \(b=c/s\). The occupancy recursion gives a second affine identity

\[
 h_3=b+\delta h_2,\qquad T=b+\delta.
\]

Subtracting yields \(T-h_3=\delta(1-h_2)\), proving the formula for \(\delta\), then \(b\). The identity \(b=c/s\) gives \(s=\delta/(1-b)\), \(c=bs\); \(z_2=c+\delta\pi=sh_2\) gives \(\pi=(sh_2-c)/\delta\); finally \(m_1=\pi p_1\) and \(r_i=sp_i\) give all three detection probabilities.

**2. No hidden divisions by zero.** Throughout the claimed region, \(s>0\), \(\pi<1\), and \(\delta\ne0\). Since \(z_2=c+\delta\pi\) and \(s=c+\delta\),

\[
 1-h_2=\frac{s-z_2}{s}=\frac{\delta(1-\pi)}s\ne0,
 \qquad 1-b=\frac{\delta}{s}\ne0.
\]

Every remaining denominator is one of the strictly positive \(m_1,r_2,r_3,s,\pi\) or the nonzero \(\delta\). Thus the formulas are defined everywhere in the claimed region. They are left inverses to the parameter-to-history-law map, proving **global uniqueness**, not just generic or local identifiability.

**3. Two seasons are insufficient at every interior point.** For two observations, the joint distribution is completely specified by the three statistics \(m_1,m_2,d_{12}\), with \(d_{12}=m_1sp_2\). Fix \(s,p_2\), and perturb the initial occupancy \(\pi\) to a nearby different \(\pi'\). Define

\[
 p_1'=\frac{m_1}{\pi'},\qquad
 c'=\frac{m_2/p_2-s\pi'}{1-\pi'}.
\]

The altered model has the same \(m_1,m_2,d_{12}\), hence exactly the same complete two-season law. At the original \(\pi\), the new parameters equal the originals. By strict interior openness, all sufficiently small nonzero perturbations remain admissible, and when initially \(c\ne s\) the difference remains nonzero for a sufficiently small perturbation. This proves local nonidentifiability for two seasons throughout the interior, not merely by dimension counting.

**4. Equal transitions are a genuine structural boundary.** If \(c=s=a\), then \(Z_2,Z_3,\ldots\) are independent Bernoulli variables with parameter \(a\), independent of \(Z_1\). The binary observations across all seasons are mutually independent, with success probabilities \(\pi p_1, ap_2,ap_3,\ldots\). Their joint law identifies only these products. Continuously changing \(\pi\) and \(p_1\), or \(a\) and the later \(p_t\), while keeping the products fixed and parameters interior, leaves every observable law unchanged. Therefore no finite or infinite single-visit sequence resolves the equal-transition case without extra restrictions. This completes the exact sharp statement.

## Verification

The accompanying `verify_model.py` is a standalone exact-rational checker using Python's standard library. It constructs all \(2^3=8\) detection-history probabilities by an explicit sum over all \(2^3=8\) hidden paths, tests the inverse identities, checks 554 strictly interior nonsingular parameter tuples (including 54 examples with season-dependent detection and 30 stationary-start cases), and checks explicit two-season and singular three-season observational aliases. Execute from the extracted package with `python3 verify_model.py`; the observed success output is recorded in `VERIFICATION.md`. Exact enumeration validates those finite cases only: the general theorem is established by the symbolic identities in the proof.

## Relationship to prior work

MacKenzie et al. (2003) introduced dynamic site-occupancy models with imperfect detection, motivating designs with repeated within-season surveys. The present theorem determines the exact information obtained from **one** unreplicated visit at each of **three** seasons when the hidden transitions are homogeneous and seasonal detection rates may vary. This different design replaces temporal replication within seasons with the uniform transition structure between seasons.

An, Hu and Shum (2013) prove identification for homogeneous hidden Markov models and explicitly assume time-independent emission distributions, whereas \(p_1,p_2,p_3\) here are independently varying unknowns. Liu and Culpepper (2025) study heterogeneous-emission hidden Markov models, but their inspected three-occasion conditions include strictly positive emission matrices, a stationary initial hidden distribution and an adjacent pair of equal emission matrices. This theorem instead has a structural zero for false positives, an unrestricted initial occupancy, and no equality restriction on the three emission probabilities. Neither identified theorem, with its stated hypotheses, directly implies this result.

Doser and Stoudt (2023/2024) discuss single-visit multi-season ecological occupancy estimation and fractional replication, reinforcing practical interest in the exact boundary. The formal overlap review remains limited by incomplete access to some historical source texts; absence from the sources examined is not a proof of worldwide novelty.

## Limitations

The two hidden-state transition probabilities must be constant across the two seasonal intervals and unequal, no false positives are permitted, observations are conditionally independent given hidden states, and the parameter tuple lies strictly in the interior. Survey sites are assumed to share a common law, and all joint detection-history probabilities are treated as known exactly; sampling variation, estimator conditioning near \(c=s\), site heterogeneity, observer effects, and arbitrary time-varying colonization/persistence are not addressed. The singular equal-transition case is unidentifiable. The formulas do not imply practical accuracy from a small number of sites, nor identify a general heterogeneous hidden Markov model.

## References

1. MacKenzie, D. I., Nichols, J. D., Hines, J. E., Knutson, M. G., Franklin, A. B. (2003). *Estimating site occupancy, colonization, and local extinction when a species is detected imperfectly*. Ecology 84, 2200–2207. DOI: 10.1890/02-3090. First public date used: 2003-08-01.
2. An, Y., Hu, Y., Shum, M. (2013). *Identifiability and Inference of Hidden Markov Models*. PDF at https://www.econ2.jhu.edu/people/hu/HMM.pdf, §2.1 and identification theorem.
3. Liu, J. and Culpepper, S. A. (2025). *Designing Learning Intervention Studies: Identifiability of Heterogeneous Hidden Markov Models*. Psychometrika. DOI: 10.1017/psy.2025.10024. See Theorems 1–2.
4. Doser, J. W., Stoudt, S. (first online 2023-12-26). *Fractional replication in single-visit multi-season occupancy models*. Methods in Ecology and Evolution. DOI: 10.1111/2041-210X.14275.
5. Hines et al. (2014). *Multiseason occupancy models for correlated replicate surveys*. Methods in Ecology and Evolution. DOI: 10.1111/2041-210X.12186.
