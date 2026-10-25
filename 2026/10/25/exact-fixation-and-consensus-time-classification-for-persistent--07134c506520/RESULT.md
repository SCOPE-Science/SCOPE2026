# Exact fixation and consensus-time classification for persistent voting on a triangle

## Finding

In the transient-zealot persistent voter process below, the complete graph on three individuals admits an exact closed classification of eventual opinion fixation and time to consensus, for **every** initial opinion/confidence configuration and every confidence increment \(\Delta\eta\geq1\). This gives the first nontrivial complete-graph size at which the initial all-normal configuration departs from the classical voter martingale.

For a mixed opinion state, let \(A\) be the unique current minority opinion, let \(z\in\{0,1\}\) be the zealot flag of its unique holder, and let \(m\in\{0,1,2\}\) be the number of zealots among the two holders of the opposite opinion. The probability that opinion \(A\) eventually fixes, and the expected number of individual ordered-pair updates to opinion consensus, are respectively

\[
\boxed{\Pr(A\text{ fixes})=\frac{105+36z-(25+4z)m+\binom m2}{339}}
\]

and

\[
\boxed{\mathbb E[\tau]=\frac{621+366z+(105+3z)m-87\binom m2}{131}.}
\]

Thus with every agent initially nonzealous, a one-holder minority wins with probability \(35/113\), strictly less than its classical-voter probability \(1/3\), and the mean number of updates to consensus is \(621/131>3\). A uniquely initially zealous minority facing two nonzealous majority voters instead wins with probability \(47/113>1/3\). Indeed, \(\Pr(A\text{ fixes})>1/3\) occurs **if and only if** \(z=1\) and \(m=0\); every other mixed initial confidence configuration yields probability less than \(1/3\). All six confidence configurations have mean consensus time exceeding the classical value \(3\).

For two initially nonzealous individuals of opposing opinions on the complete graph of order two, consensus occurs in one update and each opinion wins with probability \(1/2\). Hence the three-person system is the smallest complete graph exhibiting a strict failure of initial opinion-fraction fixation from an all-nonzealous state.

## Assumptions and scope

There are exactly three vertices, forming the undirected simple triangle; each holds an opinion \(s_i\in\{0,1\}\) and a nonnegative confidence \(\eta_i\), with zealot flag \(c_i=\mathbf1_{\{\eta_i\geq1\}}\). Fix any constant \(\Delta\eta\geq1\). At each discrete attempt an ordered pair \((i,j)\), with \(i\ne j\), is drawn uniformly from the six choices; \(i\) is the focal voter and \(j\) the speaker. All pre-update comparisons use the opinions before the draw:

* If \(s_i=s_j\), both confidences gain \(\Delta\eta\), with no opinion change.
* If \(s_i\ne s_j\), voter \(j\)'s confidence gains \(\Delta\eta\), voter \(i\)'s confidence is reset to zero, and \(i\) adopts \(s_j\) precisely if \(c_i=0\) before the draw. If \(c_i=1\), \(i\) retains its opinion.

This is the complete-graph, full-confidence-reset specialization of the published persistent-voter update. Since \(\Delta\eta\geq1\), the future depends only on the binary flags \(c_i\): on an agreement both participants become zealots, and on disagreement the focal becomes nonzealous and the speaker zealous. Consequently the result applies to arbitrary nonnegative starting confidences, not just zero/one values.

Consensus time \(\tau\) is the first time all **opinions** agree, regardless of confidence flags; a unanimous state has \(\tau=0\). All expectations count single update attempts, not full Monte Carlo sweeps. The theorem neither describes finite-\(\gamma\) partial resets nor increments \(\Delta\eta<1\).

## Proof

**Binary-state reduction.** Write a state as three ordered pairs \((s_i,c_i)\). With old pairs \((a,u)\) and \((b,v)\) at the focal and speaker, respectively, the update is

\[
(s_i',c_i')=\bigl(b\mathbf1_{\{u=0\}}+a\mathbf1_{\{u=1\}},\ \mathbf1_{\{a=b\}}\bigr),
\qquad(s_j',c_j')=(b,1).
\]

The formula is valid whether or not a zealot was already present, and uses the old opinions. It also immediately shows that unanimous opinion states are closed.

**Finite absorption and uniqueness.** Every nonunanimous three-person state has a unique minority holder. If that voter is nonzealous, selecting it as focal and any opposite speaker achieves consensus in one attempt, with probability \(1/3\). If it is zealous, the same selection resets its zealotry; repeating the selection one attempt later changes its opinion. The latter two-step event has probability \(1/9\). Thus from any mixed state the conditional probability of hitting consensus within two attempts is at least \(1/9\), uniformly over all flags. Iterating in two-attempt blocks proves almost-sure absorption with finite expected time. In particular, the bounded harmonic hitting-probability equation and the finite expected-hitting-time equation have unique solutions subject to their unanimity boundary conditions.

**Verification of the exact solutions.** There are four individual types (two opinions by two flags), hence twenty unlabeled count configurations; eight are unanimous and twelve have mixed opinions. Color interchange pairs the mixed states into exactly six classes, indexed by \((z,m)\). Denote the two boxed candidate functions by \(f(z,m)\) and \(g(z,m)\). For a mixed state with opinion 1 in the minority, the candidate probability of all-1 consensus is \(f(z,m)\); when opinion 0 is the minority it is \(1-f(z,m)\). On unanimous states the all-1 probability is its obvious zero/one boundary value. Similarly the candidate expected time is \(g(z,m)\) for either minority label and zero on unanimity.

Enumerating the six equally likely ordered-pair updates gives the following complete transition-multiplicity table. Here \(A_{zm}\) is a state with the currently tracked opinion \(A\) in the minority, \(B_{zm}\) denotes the same configuration with the opposite opinion \(B\) in the minority, and \(B_*\) is unanimous \(B\). An entry's coefficient is the number of the six ordered-pair choices leading to it.

| \((z,m)\) | Six one-step outcomes from \(A_{zm}\) |
|---|---|
| \((0,0)\) | \(2B_*+2B_{01}+2A_{02}\) |
| \((0,1)\) | \(2B_*+A_{10}+2A_{02}+B_{11}\) |
| \((0,2)\) | \(2B_*+2A_{11}+2A_{02}\) |
| \((1,0)\) | \(2A_{01}+2B_{01}+2A_{12}\) |
| \((1,1)\) | \(A_{01}+A_{02}+A_{10}+2A_{12}+B_{11}\) |
| \((1,2)\) | \(2A_{02}+2A_{11}+2A_{12}\) |

For example the first row gives \(6f(0,0)=2(1-f(0,1))+2f(0,2)\) and \(6g(0,0)=6+2g(0,1)+2g(0,2)\). Substitution of the two boxed formulas verifies, row by row, the corresponding six probability and six time equations, using \(\Pr(A\text{ fixes}\mid B_{zm})=1-f(z,m)\) and \(g=0\) on unanimous outcomes. Color symmetry supplies the six remaining mixed cases. Finite absorption and uniqueness therefore prove both formulas without extrapolation or unproved numerical inversion.

**Thresholds and smallest size.** Substituting \(z=0,1\) and \(m=0,1,2\) into \(f\) gives, in denominator \(339\), the six numerators \(105,80,56\) and \(141,112,84\), respectively. The neutral fraction \(1/3\) has numerator \(113\), so precisely the case \((z,m)=(1,0)\) lies above it. For \(g\), the six numerators in denominator \(131\) are \(621,726,744\) and \(987,1095,1116\); each exceeds \(3\cdot131\). The size-two assertion is immediate from a pair of nonzealous opposing voters copying one another at the first selection. For classical three-person voter copying, one minority wins with probability \(1/3\) by the opinion-count martingale and the mean consensus time solves \(t=1+(2/3)t\), giving \(t=3\).

## Verification

The accompanying standalone Python 3 verifier uses exact rational arithmetic. It constructs all 64 labeled opinion/flag states, checks the proposed hitting-probability and expected-time harmonic equations at all 48 mixed states, and independently forms and solves the twelve-state unlabeled transient linear systems for probability and time. All checks passed. The analytical proof above is finite and complete; the code independently checks its finite algebra and is not a simulation.

## Relationship to prior work

Latoski, Dantas and Arenzon introduced self-induced zealotry in 2022 and subsequently studied opinion inertia and coarsening in 2024. The underlying update mechanism, transient zealotry, and qualitative consequences for spatial coarsening are prior work; the present scope is only the exact finite triangle fixation/time classification for their full-reset specialization. Volovik and Redner's earlier confident-voter model has two confidence types but distinct partner-reinforcement and flipping rules, so its mean-field analysis does not imply these rational constants. The 2025 and 2026 persistent-voter papers study a simplified update or long-range spatial correlations, not these exact full-reset triangle quantities. Finite absorbing-chain recurrences are standard mathematics; the claimed new content is the concrete closed formula, threshold and complete microscopic classification for this particular process, not the general recurrence method.

## Limitations

Only a three-person complete network, a single fixed update law, increments \(\Delta\eta\geq1\), full reset on disagreement and exactly two opinions are covered. Neither an arbitrary-network majority amplification law nor a claim that inertia slows consensus in large systems follows. The exact coefficients are proved for discrete ordered-pair attempts and cannot be transferred without rescaling to continuous-time dynamics or Monte Carlo sweeps. Scientific priority relative to all literature is not independently certified.

## References

1. L. C. F. Latoski, W. G. Dantas and J. J. Arenzon, *Curvature-driven growth and interfacial noise in the voter model with self-induced zealots* (first public preprint 2022-04-07), arXiv:2204.03402, https://arxiv.org/abs/2204.03402.
2. L. C. F. Latoski, W. G. Dantas and J. J. Arenzon, *Opinion inertia and coarsening in the Persistent Voter model* (first public preprint 2024-03-04), arXiv:2403.02483, https://arxiv.org/abs/2403.02483.
3. D. Volovik and S. Redner, *Dynamics of confident voting*, J. Stat. Mech. (2012) P04003, arXiv:1111.3883, https://arxiv.org/abs/1111.3883.
4. R. G. de Almeida et al., *Coarsening in the Persistent Voter Model: analytical results* (2025), arXiv:2503.17295, https://arxiv.org/abs/2503.17295.
5. J. J. Arenzon et al., *Coarsening in the long-range Persistent Voter Model* (2026), arXiv:2603.14165, https://arxiv.org/abs/2603.14165.
