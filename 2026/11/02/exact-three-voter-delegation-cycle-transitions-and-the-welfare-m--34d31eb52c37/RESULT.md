# Exact three-voter delegation-cycle transitions and the welfare mismatch window

## Finding

In the default-delegation voting game of [1], take three voters at equally spaced locations \(0,h,2h\), with \(0<h\leq 1/2\), identical independent turnout probability \(p\in(0,1)\), and common tolerance \(\tau\geq0\). Write \(q=1-p\), \(t=\tau/h\), and
\[
\alpha=\frac{1+2q}{1+q},\qquad
\beta=1+\frac{1}{2q},\qquad
\gamma=1+\frac{1}{q}.
\]
Then \(1<\alpha<\beta<\gamma\). In a code such as `212`, the three digits respectively give the default delegate chosen by voters 1, 2 and 3; the digit equal to a voter's own index denotes self-delegation.

**Complete pure Nash-equilibrium classification:**

| Dimensionless tolerance | All pure Nash equilibria |
|---|---|
| \(0\leq t<1\) | `123` |
| \(t=1\) | `113`, `122`, `123`, `132`, `133`, `213`, `222`, `223` |
| \(1<t<\alpha\) | `132`, `213` |
| \(t=\alpha\) | `132`, `213`, `212`, `232` |
| \(\alpha<t<\gamma\) | `212`, `232` |
| \(t=\gamma\) | `212`, `232`, `231`, `312` |
| \(t>\gamma\) | `231`, `312` |

**Complete social-welfare-maximizer classification:**

| Dimensionless tolerance | All maximum-welfare profiles |
|---|---|
| \(0\leq t<1\) | `123` |
| \(t=1\) | `113`, `122`, `123`, `132`, `133`, `213`, `222`, `223` |
| \(1<t<\alpha\) | `132`, `213`, `222` |
| \(t=\alpha\) | `132`, `213`, `222`, `212`, `232` |
| \(\alpha<t<\beta\) | `212`, `232` |
| \(t=\beta\) | `212`, `232`, `231`, `312` |
| \(t>\beta\) | `231`, `312` |

Let \(\Delta=\max_{d} SW(d)-\min_{d\in\mathrm{PNE}}SW(d)\) be the additive welfare loss of the least efficient pure equilibrium. It is exactly
\[
\Delta=
\begin{cases}
 hpq\,[2q(t-1)-1],&\beta<t\leq\gamma,\\
 0,&\text{otherwise}.
\end{cases}
\]
Consequently, for every \(p\in(0,1)\), on the nonempty open interval \(\beta<t<\gamma\), **every pure equilibrium is welfare-suboptimal** even though the market is fully symmetric; at \(t=\gamma\) efficient and inefficient equilibria coexist. Beyond \(\gamma\), only three-voter delegation cycles survive and they are welfare-maximizing.

## Assumptions and scope

Agents are labeled \(1,2,3\), located at \(x_i=(i-1)h\). Every voter independently casts a ballot with probability \(p\) and, if not casting, passes voting weight to their chosen default delegate. A chain stops at the first casting voter; if the chain repeats a vertex without reaching one, representation is lost. Each voter chooses one default delegate, possibly themselves. If voter \(i\)'s eventual representative is \(j\), their realized utility is \(\tau-|x_i-x_j|\); if unrepresented, it is zero. Expected utilities define pure Nash equilibria. Social welfare is the sum of all three expected utilities, including negative utility from a distant representative when it occurs. The model does not forbid delegations beyond the tolerance radius. All claims quantify over every real \(p\in(0,1)\) and every real \(\tau\geq0\); there are no numerical approximation assumptions.

The equality case \(t=1\) contains utility ties and intentionally includes profiles outside the *general-position* convention sometimes used for the model. The payoffs remain unambiguous. At \(t=2\), the extreme voters are exactly a tolerance distance apart, also without ambiguity.

## Proof

**1. Exact path reduction.** For a profile \(d\), follow the longest nonrepeating delegation path from voter \(i\), written \((i,v_1,\ldots,v_\ell)\) with \(0\leq\ell\leq2\). By independence, its \(j\)th vertex casts first with probability \(p q^j\). Thus
\[
U_i(d)=p\tau+hpqF_i(d),\qquad
F_i(d)=\sum_{j=1}^{\ell}q^{j-1}(t-|i-v_j|).
\]
Define \(G(d)=F_1(d)+F_2(d)+F_3(d)\), so \(SW(d)=3p\tau+hpqG(d)\). Since \(hpq>0\), all equilibrium comparisons may be made using \(F_i\), and all welfare comparisons using \(G\). This identity follows from the random participation model, not from experimental enumeration.

**2. Exhaustive Nash comparison with symmetry.** Reflection of the voter line sends a delegate profile to \(\rho(d)_i=4-d_{4-i}\) and preserves the game. The \(27\) profiles reduce to exactly \(15\) reflection representatives:

`111`, `112`, `113`, `121`, `122`, `123`, `131`, `132`, `211`, `212`, `221`, `222`, `231`, `311`, `321`.

For \(t>1\), the following representatives have an explicit strictly profitable one-voter deviation. The *gain* in the table is the difference of normalized \(F_i\) values; multiply by \(hpq\) for the actual expected-utility gain.

| Representative(s) | A profitable deviation | Normalized gain |
|---|---|---|
| `111`, `112`, `113`, `121`, `122`, `123` | Voter 1 changes to delegate 2 | \(t-1\) |
| `221`, `222` | Voter 2 changes to delegate 1 | \(t-1\) |
| `131` | Voter 3 changes to delegate 2 | \(1\) |
| `311`, `321` | Voter 1 changes to delegate 2 | \(1\) |
| `211` | Voter 2 changes to delegate 3 | \(q(t-1)\) |

For the three surviving representatives, direct substitution into the same path formula gives all their no-profitable-deviation conditions:
\[
\begin{array}{c|c}
\text{Representative}&\text{Necessary and sufficient condition}\hline
\texttt{132}&(1+q)t\leq1+2q\quad(t\leq\alpha),\\
\texttt{212}&(1+q)t\geq1+2q\ \text{ and }\ qt\leq1+q\quad(\alpha\leq t\leq\gamma),\\
\texttt{231}&qt\geq1+q\quad(t\geq\gamma).
\end{array}
\]
In `132` the decisive possible improvement is voter 1 joining the pair at normalized gain \(t-1+q(t-2)\). In `212` the two possible binding improvements are voter 3 self-delegating (gain \(-[t-1+q(t-2)]\)) and voter 1 selecting voter 3 (gain \(q(t-1)-1\)). In `231` the binding improvement is voter 3 changing to delegate 2 (gain \(1+q-qt\)); every other deviation is nonprofitable whenever this is. For completeness, the following are *all* six normalized unilateral gains for each surviving representative. A notation such as \(1\to2\) means that voter 1 alone changes their default to voter 2; entries omitted from a given profile are not deviations.

| Profile | All alternative unilateral gains \(F_i(d')-F_i(d)\) |
|---|---|
| `132` | \(1\to2:(1+q)t-(1+2q)\); \(1\to3:(1+q)t-(2+q)\); \(2\to1:0\); \(2\to2:1-t\); \(3\to1:-1\); \(3\to3:1-t\) |
| `212` | \(1\to1:1-t\); \(1\to3:q(t-1)-1\); \(2\to2:1-t\); \(2\to3:0\); \(3\to1:q-1\); \(3\to3:(1+2q)-(1+q)t\) |
| `231` | \(1\to1:(1+2q)-(1+q)t\); \(1\to3:2q-1-qt\); \(2\to1:-q(t-1)\); \(2\to2:-(1+q)(t-1)\); \(3\to2:1+q-qt\); \(3\to3:2+q-(1+q)t\) |

For \(t>1\), \(0<q<1\), all the other gains have the required nonpositive signs whenever the displayed binding inequalities hold. In particular, \(\alpha<\gamma\) implies that the only change in the `212` stability condition after \(\alpha\) is at \(\gamma\). Reflection yields exactly the claimed equilibrium sets.

If \(t<1\), every positive-length delegation path exposes a voter to strictly negative extra utility relative to self-delegation, so `123` is uniquely stable. At \(t=1\), all extra path terms are nonpositive; a profile is stable precisely if no voter's path visits a nonself vertex two positions away, because self-delegation gives the maximal utility \(p\tau\). Checking the same \(15\) reflection classes then produces exactly the eight profiles displayed above.

**3. Exact welfare frontier.** The complete values of \(G\) on the \(15\) reflection representatives are:

| Profile | \(G(d)\) | Profile | \(G(d)\) | Profile | \(G(d)\) |
|---|---|---|---|---|---|
| `111` | \(2t-3\) | `112` | \(2t-2+q(t-2)\) | `113` | \(t-1\) |
| `121` | \(t-2\) | `122` | \(t-1\) | `123` | \(0\) |
| `131` | \(2t-3+q(t-1)\) | `132` | \(2(t-1)\) | `211` | \(3t-4+q(t-1)\) |
| `212` | \(3(t-1)+q(t-2)\) | `221` | \(2t-3+q(t-1)\) | `222` | \(2(t-1)\) |
| `231` | \((1+q)(3t-4)\) | `311` | \(3t-5+q(t-1)\) | `321` | \(2(t-2)\) |

For \(t>1\), every entry outside `132`, `212`, `222`, `231` is strictly smaller than at least one of these four. Explicitly, subtracting each nonfrontier entry from a dominating frontier entry gives, in the table's order, one of \(1\), \(t-1\), \(t\), \(2(t-1)\), \(t-q\), \(1-q\), or \(2-q\), or \(2\), each strictly positive under \(t>1\), \(0<q<1\). Thus only three distinct surplus curves can maximize welfare:
\[
G_A=2(t-1),\quad
G_B=3(t-1)+q(t-2),\quad
G_C=(1+q)(3t-4).
\]
The differences satisfy
\[
G_B-G_A=(1+q)t-(1+2q),\qquad
G_C-G_B=2q(t-1)-1.
\]
Hence \(G_A\) is maximal for \(1<t<\alpha\), \(G_B\) for \(\alpha<t<\beta\), and \(G_C\) for \(t>\beta\), with the stated tie sets at the boundaries. For \(t<1\), self-delegation uniquely maximizes welfare; at \(t=1\), precisely the eight profiles with no negative path terms maximize it.

**4. Welfare gap.** All equilibria have maximum welfare through \(t=\beta\). In \(\beta<t<\gamma\), both equilibria have type `212` and both maximum-welfare profiles have type `231`. Their welfare difference is \(hpq(G_C-G_B)=hpq[2q(t-1)-1]\). At \(t=\gamma\), types `212` and `231` coexist as equilibria, with the former still worse by \(hpq\). For \(t>\gamma\), only the welfare-maximizing `231` type remains. This proves the formula for \(\Delta\) with all endpoints covered.

## Verification

`CHECK.py` implements two mathematically independent evaluations of each expected utility: direct enumeration of all \(2^3\) casting subsets and the first-participant path expansion. It enumerates all \(3^3\) profiles, all unilateral deviations and every welfare value using exact rational arithmetic, checking threshold equalities and both sides of all three transitions for seven participation parameters. Running `python CHECK.py` returns `VERIFY_OK exact_parameter_cases= 83 event_level_payoffs= 6723 profile_deviation_checks= 13446`. These finite checks guard the algebra and boundary handling; the parameter-uniform proof is the symbolic comparison above, not the sampling.

For illustration, at \(p=q=1/2\), the three thresholds are \(\alpha=4/3\), \(\beta=2\), and \(\gamma=3\). At \(t=5/2\), the equilibria are `212` and `232`, the welfare maximizers are `231` and `312`, and the precise welfare shortfall is \(h/8\).

## Relationship to prior work

Brill et al. [1] introduce the stochastic default-delegation model and derive existence, structural cycle, and welfare-bound results (including their Theorems 1, 5, 11, 13 and Appendix B). Their work supplies the model and the qualitative importance of delegation cycles. The present result specializes to the minimal fully symmetric three-agent line and supplies a complete *sharp* Nash and welfare phase classification, the differing cycle-transition thresholds, and an exact positive inefficiency interval. These statements are not consequences of merely knowing equilibrium existence, the cycle-per-component property, or the general welfare bounds. The earlier liquid-democracy games of [2,3] have different payoff and delegation assumptions.

## Limitations

The theorem concerns exactly three equally spaced voters with common turnout probability and common tolerance; it makes no claim for heterogeneous parameters, more voters, arbitrary metric spaces, or mixed equilibria. The interval of inefficient equilibria is derived for this exact utility convention, including possible negative utility when a distant casting voter receives a ballot. The result is an exact mathematical classification, not an empirical prediction about actual delegations. Publication priority beyond the inspected sources cannot be certified by a finite search.

## References

[1] M. Brill, R. Colley, A.-M. George, G. Lisowski, G. Papasotiropoulos, and U. Schmidt-Kraepelin, *Cycles in Liquid Democracy: A Game-Theoretic Justification*, arXiv:2607.12610v1, first publicly posted July 14, 2026. https://arxiv.org/html/2607.12610

[2] B. Escoffier, H. Gilbert, and A. Pass-Lanneau, *The Convergence of Iterative Delegations in Liquid Democracy in a Social Network*, arXiv:1904.05775, first posted April 10, 2019. https://arxiv.org/abs/1904.05775

[3] D. Bloembergen, D. Grossi, and M. Lackner, *On Rational Delegations in Liquid Democracy*, AAAI 2019, DOI:10.1609/aaai.v33i01.33011796. https://doi.org/10.1609/aaai.v33i01.33011796
