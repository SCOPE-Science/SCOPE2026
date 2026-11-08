# A geometric-mean clearing law for indirect ecological occupancy markers

## Finding

Fix \\(\\alpha,\\beta,\\lambda>0\\). A site switches from empty to occupied at rate \\(\\alpha\\) and from occupied to empty at rate \\(\\beta\\). A binary indirect marker is deposited (turns on) at rate \\(\\lambda\\) when the site is occupied and the marker is off, and clears (turns off) at rate \\(\\delta>0\\), independently of current site occupancy. At stationarity, use the presence of the marker to diagnose current occupancy, with sensitivity \\(S_\\delta=\\Pr(M=1\\mid Z=1)\\), false-positive rate \\(F_\\delta=\\Pr(M=1\\mid Z=0)\\), and Youden discrimination \\(J_\\delta=S_\\delta-F_\\delta\\). Set

\\[
D_\\delta=\\delta^2+(\\alpha+\\beta+\\lambda)\\delta+\\alpha\\lambda.
\\]

Then, for every positive choice of the four rates,

\\[
S_\\delta=\\frac{\\lambda(\\alpha+\\delta)}{D_\\delta},\\quad
F_\\delta=\\frac{\\alpha\\lambda}{D_\\delta},\\quad
J_\\delta=\\frac{\\lambda\\delta}{D_\\delta}.
\\]

Consequently the **unique** clearing rate maximizing both stationary balanced diagnostic accuracy and the area under the ROC curve of the binary marker is

\\[
\\boxed{\\delta_*=\\sqrt{\\alpha\\lambda}},\\qquad
\\boxed{J_{\\delta_*}=\\frac{\\lambda}{\\alpha+\\beta+\\lambda+2\\sqrt{\\alpha\\lambda}}}.
\\]

In particular, the maximizing clearing rate does not depend on the site's extinction rate \\(\\beta\\). Moreover every \\(\\delta>0\\) obeys the exact reciprocal-equivalence law

\\[
J_\\delta=J_{\\alpha\\lambda/\\delta}.
\\]

## Assumptions and scope

The joint process \\((Z,M)\\in\\{0,1\\}^2\\) is a time-homogeneous continuous-time Markov chain. Its transitions are: \\(Z:0\\to1\\) at rate \\(\\alpha\\), \\(Z:1\\to0\\) at rate \\(\\beta\\) without directly changing \\(M\\); \\(M:0\\to1\\) at rate \\(\\lambda\\) only when \\(Z=1\\); and \\(M:1\\to0\\) at rate \\(\\delta\\) regardless of \\(Z\\). All four rates are strictly positive, ensuring a unique strictly positive stationary distribution. A marker already on is not multiplied by additional deposits; this is a *binary saturating and resetting marker*, not a count of individually decaying fecal pellets. Marker presence is observed without further measurement error. The optimization concerns balanced classification of *instantaneous* occupancy from a *single instantaneous marker*, not estimating the colonization rate, abundance, or prevalence using repeated surveys. Rates other than \\(\\delta\\) are fixed.

Balanced accuracy is \\(B_\\delta=(S_\\delta+1-F_\\delta)/2\\). For a binary diagnostic score, its ROC area, with half credit for tied scores, equals \\(B_\\delta\\). Thus maximizing either is equivalent to maximizing \\(J_\\delta\\). No claim is made about unbalanced, prevalence-weighted misclassification loss.

## Proof

Let \\(s=\\alpha+\\beta\\), \\(\\pi=\\Pr(Z=1)=\\alpha/s\\), \\(q=\\Pr(M=1)\\), and \\(r=\\Pr(Z=1,M=1)\\) in the stationary regime. Balancing creation and clearing of marks gives

\\[
0=\\lambda(\\pi-r)-\\delta q.
\\tag{1}
\\]

Balancing the joint event \\(Z=1,M=1\\) gives

\\[
0=\\alpha(q-r)+\\lambda(\\pi-r)-(\\beta+\\delta)r
 =\\alpha q+\\lambda\\pi-(s+\\lambda+\\delta)r.
\\tag{2}
\\]

The site process is autonomous, hence its stationary occupancy probability is \\(\\pi=\\alpha/s\\). Solving (1)–(2), with \\(D_\\delta\\) as above, yields

\\[
q=\\frac{\\lambda\\pi(s+\\delta)}{D_\\delta},\\qquad
r=\\frac{\\lambda\\pi(\\alpha+\\delta)}{D_\\delta}.
\\]

Therefore \\(S_\\delta=r/\\pi=\\lambda(\\alpha+\\delta)/D_\\delta\\). Also,

\\[
F_\\delta=\\frac{q-r}{1-\\pi}
=\\frac{\\lambda\\pi\\beta/D_\\delta}{\\beta/s}
=\\frac{\\alpha\\lambda}{D_\\delta}.
\\]

Subtracting proves the asserted formula for \\(J_\\delta\\). Direct differentiation then gives

\\[
\\frac{dJ_\\delta}{d\\delta}
=\\frac{\\lambda(\\alpha\\lambda-\\delta^2)}{D_\\delta^2}.
\\]

Because all rates are positive, this derivative is positive on \\(0<\\delta<\\sqrt{\\alpha\\lambda}\\) and negative on \\(\\delta>\\sqrt{\\alpha\\lambda}\\). Moreover \\(J_\\delta\\to0\\) at both endpoints \\(\\delta\\downarrow0\\) and \\(\\delta\\to\\infty\\). Thus \\(\\delta_*\\) is the unique global maximizer. Dividing the discrimination formula by \\(\\delta\\) gives

\\[
J_\\delta=\\frac{\\lambda}{\\delta+(\\alpha+\\beta+\\lambda)+\\alpha\\lambda/\\delta},
\\]

which simultaneously proves the reciprocal identity and the stated maximal value. In particular, \\(\\beta\\) affects the peak height but cancels from its location. Finally, the binary-score ROC area is \\(\\tfrac12(S_\\delta+1-F_\\delta)=(1+J_\\delta)/2\\), completing the claim.

## Verification

The standalone Python 3 script `verify.py` builds the four-state generator and independently solves its stationary balance equations using rational Gaussian elimination. It compares the resulting two conditional error probabilities to the closed forms, checks all four master equations and the reciprocal identity for \\(1296\\) rational parameter quadruples. Execution:

```bash
python3 verify.py
```

The script prints three PASS lines, each for \\(1296\\) parameter quadruples. These finite tests corroborate the equations; the unrestricted positive-rate theorem follows from the preceding algebra, not from numerical enumeration. As a check with \\(\\alpha=1,\\beta=4,\\lambda=9\\), the unique optimum is \\(\\delta_*=3\\), where sensitivity is \\(3/5\\), false-positive rate is \\(3/20\\), and discrimination is \\(9/20\\). The rates \\(\\delta=1\\) and \\(\\delta=9\\) give the same smaller discrimination \\(3/8\\), illustrating the reciprocal identity.

## Relationship to prior work

Guillera-Arroita, Ridout and Morgan (2010) analyze allocation and replicate precision in occupancy studies with imperfect detection, but explicitly hold occupancy and detection probabilities constant; they do not model decaying physical markers. Rhodes et al. (2011) motivate the specific conflict between old indirect signs persisting after local disappearance and missing short-lived signs at occupied sites. Their accessible Methods explicitly assume unchanged occupancy while calculating false negatives and say that actual false-positive rates require an occupancy-change model. The present four-state process supplies such a model, albeit for a binary resetting marker rather than individually decaying physical signs, and it optimizes the resulting balanced diagnostic criterion exactly. Miller et al. (2011) model false positives from misidentification using multiple detection classes rather than a dynamically accumulated/cleared marker. Fukaya and Royle (2013) study a broader hidden-Markov observation-error framework but not, in inspected material, this coupled marker mechanism and its geometric-mean clearing optimum. None of those frameworks alone implies the stated rate-independent optimizer without additional modeling and derivation. Historic priority of the exact formula in wider binary-sensor/telegraph-process literature is not excluded.

## Limitations

The binary marker clears as a single whole and switches on only when absent. This excludes independent survival of many deposited traces, environmentally correlated resetting and imperfect marker recognition. The optimality criterion weights specificity and sensitivity equally and assumes stationary dynamics; it need not optimize positive predictive value, total error under unequal class prevalence, Fisher information, or finite-horizon detection. The clearing rate may be an environmental characteristic rather than a controllable management variable, so the result is principally a comparison benchmark for marker types or recording media. Earlier equivalent treatments in engineering or ecology may exist. Independently checking full primary literature remains necessary before any public claim of publication-level novelty.

## References

1. Guillera-Arroita, G., Ridout, M. S., and Morgan, B. J. T. (2010). Design of occupancy studies with imperfect detection. *Methods in Ecology and Evolution* 1, 131–139. First public online date 2010-05-04. DOI: https://doi.org/10.1111/j.2041-210X.2010.00017.x
2. Rhodes, J. R., Lunney, D., Moon, C., Matthews, A., and McAlpine, C. A. (2011). The consequences of using indirect signs that decay to determine species' occupancy. *Ecography* 34, 141–150. DOI: https://doi.org/10.1111/j.1600-0587.2010.05908.x
3. Miller, D. A., Nichols, J. D., McClintock, B. T., Grant, E. H. C., Bailey, L. L., and Weir, L. A. (2011). Improving occupancy estimation when two types of observational error occur: non-detection and species misidentification. *Ecology* 92, 1422–1428. DOI: https://doi.org/10.1890/10-1396.1
4. Fukaya, K., and Royle, J. A. (2013). Markov models for community dynamics allowing for observation error. *Ecology* 94, 2670–2677. DOI: https://doi.org/10.1890/12-1540.1
