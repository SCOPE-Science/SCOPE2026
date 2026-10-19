# Sharp first-delay fixation phase diagram and selection-strength reversal in a three-individual Moran game

## Finding

In a three-individual, well-mixed Moran birth–death evolutionary game, one historical update of fitness can either increase or decrease the fixation probability of a single initial mutant. The boundary admits a complete exact algebraic classification. Let \(x=f_1/g_1>0\) and \(y=f_2/g_2>0\) be mutant-to-resident relative fitnesses when one and two mutants, respectively, are present. If the initial history is uniformly one mutant, the no-delay and one-step-delay fixation probabilities are

\[
\Phi_0=\frac{xy}{xy+y+1},\qquad
\Phi_1=\frac{x^2(y+2)(2y+1)}{(xy+x+1)(2xy+3x+2y+2)}.
\]

Their difference factorizes as

\[
\boxed{\Phi_1-\Phi_0=-\frac{x(x-y)(xy-2y-2)}{(xy+x+1)(xy+y+1)(2xy+3x+2y+2)}.}
\]

Consequently delay helps exactly when \((x-y)(xy-2y-2)<0\), harms exactly when it is positive, and has no effect exactly on the union of \(x=y\) and \(x=2+2/y\). These are complete necessary and sufficient conditions for the stated process, not asymptotic approximations. The result also identifies three individuals as the smallest population size at which this fitness-delay effect can appear: a two-individual population has a single transient composition and hence its fixation probability is independent of the finite delay.

There exists a fixed strictly positive payoff game exhibiting a sharp **reversal with increasing selection strength**. With mutant/resident payoff matrix

\[
\begin{pmatrix}2&10\\3&1\end{pmatrix},
\]

linear fitness interpolation \(f=1-w+w\pi\) and \(0\leq w\leq1\), the one-step delay strictly increases fixation for \(0<w<w_*\), is neutral at \(w=0\) and at \(w=w_*\), and strictly decreases fixation for \(w_*<w\leq1\), where

\[
\boxed{w_*=(2+\sqrt{97})/31.}
\]

For all \(w>0\) in this example, mutant relative fitness is **higher** in the one-mutant composition than in the two-mutant composition; the reversal is not caused by a reversal of that relative ordering.

## Assumptions and scope

There are exactly three individuals and two heritable strategies \(A\) (mutant) and \(B\) (resident). No mutation occurs after initialization. At each discrete update, an individual is selected to reproduce with probability proportional to its **current numerical abundance** times its strategy's payoff-derived fitness, evaluated on the composition one update earlier. Its offspring replaces a uniformly selected different individual, as in the no-self-replacement Moran birth–death convention. A zero- or three-mutant population is absorbing. Fitness values \(f_1,g_1,f_2,g_2\) are all strictly positive. Initially the mutant count is one, including the one historical state used to evaluate the first birth. \(\Phi_\tau\) denotes eventual probability of reaching three mutants under lag \(\tau\). The comparison is between \(\tau=0\) and \(\tau=1\) only.

For game payoffs \(\bigl(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr)\), individuals interact equally with the other two individuals, without playing themselves. At full selection \(w=1\), \(f_1=b\), \(g_1=(c+d)/2\), \(f_2=(a+b)/2\), and \(g_2=c\). In the strength-dependent example, each fitness is a baseline-and-payoff interpolation \(1-w+w\pi\), where \(\pi\) is the strategy's average payoff. This normalization is specified because changing the self-play or replacement conventions changes the equations.

The positive payoff games realize exactly the region \(0<x<4y\) in ratio coordinates: positivity gives \(x/y=4bc/((a+b)(c+d))<4\). Conversely, for any such pair choose \(\alpha\in(x/(4y),1)\), \(c=2\alpha\), \(d=2(1-\alpha)\), \(b=x\), \(a=4\alpha y-x\); all entries are positive and produce the prescribed \(x,y\). Thus both sides of the nontrivial equality curve are genuine positive-payoff games when \(y>1\).

## Proof

Write \(A,B,C,E\) for fixation probabilities from the four transient delayed states \((i_{t-1},i_t)=(1,1),(1,2),(2,1),(2,2)\), respectively. If the current count is one and the historical mutant/resident fitness ratio is \(r\), the probabilities of an upward and downward step are respectively \(r/(r+2)\) and \(1/(r+2)\). If the current count is two, these probabilities are \(r/(2r+1)\) and \(1/(2r+1)\). The complementary probability is a holding step in both cases. First-step conditioning, multiplying through by the positive denominators, gives the four linear equations

\[
\begin{aligned}
(x+1)A&=xB,\\
(2x+1)B&=C+xE+x,\\
(y+2)C&=A+yB,\\
(y+1)E&=C+y.
\end{aligned}
\]

The inhomogeneous terms arise from a step to three mutants. Every transient state has a positive-probability path to absorption in a bounded number of steps. As the state set is finite and the ratios are positive, absorption occurs almost surely, so these linear equations uniquely determine fixation probabilities.

Define \(D=(xy+x+1)(2xy+3x+2y+2)\). Direct substitution, or elimination of the four equations, yields

\[
\begin{aligned}
A&=\frac{x^2(y+2)(2y+1)}D,\\
B&=\frac{x(x+1)(y+2)(2y+1)}D,\\
C&=\frac{x(2y+1)(xy+x+y)}D,\\
E&=\frac{2x^2y^2+5x^2y+x^2+2xy^2+6xy+2y}D.
\end{aligned}
\]

The original history is \((1,1)\), giving \(\Phi_1=A\). At zero lag, the ratio of down-step to up-step probabilities in state one is \(1/x\), and in state two it is \(1/y\). The two-state birth–death absorption recurrence gives \(\Phi_0=1/(1+1/x+1/(xy))=xy/(xy+y+1)\). Subtracting the two rational formulas and factoring the numerator gives the displayed boxed difference. Every denominator is positive for all \(x,y>0\), proving the complete sign and equality classification.

For the fixed positive payoff matrix in the finding, average payoffs at one mutant are \((10,2)\), and at two mutants they are \((6,3)\). Hence

\[
 x(w)=\frac{1+9w}{1+w},\qquad y(w)=\frac{1+5w}{1+2w},
\]

and straightforward polynomial identities give

\[
 x(w)-y(w)=\frac{w(5+13w)}{(1+w)(1+2w)},\qquad
 x(w)y(w)-2y(w)-2=\frac{31w^2-4w-3}{(1+w)(1+2w)}.
\]

The second numerator has exactly one positive zero, \((2+\sqrt{97})/31\), which lies strictly between zero and one. The first factor is positive throughout \(0<w\leq1\). Substitution into the exact sign law proves every assertion about the fixed game.

For two individuals, the only nonabsorbing mutant count is one. Before fixation or extinction, every historical count contributing to a finite fitness delay is necessarily one under the common all-one initial history. Thus delayed and instantaneous reproduction probabilities agree at every transient step. This proves the minimum-population claim.

## Verification

The standalone file `verify.py` uses only the Python 3 standard library. It checks as polynomial identities all four proposed delayed-state fixation equations and the factorization of the difference, plus the two polynomial identities used in the selection-strength witness. Separately, it constructs and solves the full four-state absorbing Markov chain over exact rational arithmetic for 144 positive rational pairs of ratios and compares the result to the closed formula. The positive and negative examples are checked with exact rational arithmetic as well. It can be run from a directory containing this file by invoking `python3 verify.py`. These finite tests supplement, rather than replace, the universally quantified algebraic proof.

In particular, at \((x,y)=(2,1)\) one obtains \(\Phi_1-\Phi_0=1/70>0\); for the game in the finding at full strength \((x,y)=(5,2)\), the difference is \(-15/2132<0\).

## Relationship to prior work

Mohamadichamgavi and Broom introduce the lagged-fitness Moran model, including the no-self-replacement transition rule and history-valued Markov states, and numerically explore the effects of lag, payoff class, population size, and selection intensity. Their arXiv preprint was first publicly posted on 14 March 2024, and the expanded journal article appeared later in 2024. Their general Markov-chain solution method makes small-system exact evaluation possible; that computational method is **prior work**, not claimed here. The specifically derived **complete factorized sign diagram**, **two exact equality loci**, **sharp three-person onset**, and **selection-strength threshold for one fixed positive game** are the assessed new statements. The motivating work discusses increases or decreases for selected game classes and reports numerical strength dependence, but does not state or prove these complete identities and fixed-game reversal criterion in the material inspected. This is a best-knowledge distinction, not a claim of exhaustive publication priority.

Other work on delayed evolutionary games studies delayed replicator dynamics and stationary stochastic stability rather than this first-lag finite-population fixation comparison. Classical Moran fixation formulas apply without a lag, and general fundamental-matrix formulas determine values algorithmically without providing this closed two-curve classification.

## Limitations

The classification is for population size three, exactly one lagged update, positive fitness, uniform all-one history, and birth–death updates without self-replacement. No assertion is made for additional lags, other population sizes, death–birth updating, allowing self-replacement, or spatial graphs. The fixed-game threshold is exact for the specified linear payoff-to-fitness interpolation; other fitness maps may have different thresholds. Full independent mathematical review and exhaustive priority checks have not been performed. A published general absorption-matrix theorem could in principle imply this finite case; the claim is that the explicit boundary and its interpretation were not located in inspected related sources.

## References

1. J. Mohamadichamgavi and M. Broom, *The Impact of Time Delay on Mutant Fixation in Evolutionary Games*, arXiv:2403.09864, version first public 14 March 2024, https://arxiv.org/abs/2403.09864.
2. J. Mohamadichamgavi and M. Broom, *The impact of time delays on mutant fixation in pairwise social dilemma games*, Proceedings of the Royal Society A **480** (2024), article 20240195, https://doi.org/10.1098/rspa.2024.0195. This journal publication is a subsequent version of the same underlying research.
3. J. Miȩkisz and S. Wesołowski, *Stochasticity and Time Delays in Evolutionary Games* (2011); a related stochastic-delay perspective with a different dynamical objective.
