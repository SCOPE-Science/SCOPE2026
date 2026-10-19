# Fourfold stationary-mode coexistence in a distinct-panel voter process

## Finding

Consider a well-mixed two-opinion, two-neighbor conformity process with two equally sized groups of permanently committed agents. When the two influencers are required to be *distinct* and are sampled uniformly without replacement, the exact finite-population stationary distribution has at most four global modes, and four modes occur for infinitely many population sizes. The exceptional populations are linked to the negative Pell equation. This differs from the with-replacement implementation at the same population parameters.

Write \(2m\) for the number of susceptible agents and \(z\ge2\) for each of the two opposing zealot counts, with \(m\ge1\). Let \(p_j\) be the stationary probability that exactly \(j\) of the susceptible agents support the positive opinion, for \(0\le j\le2m\). Set
\[
\Delta=m(m+1)-(z-1)(z-2).
\]
The exact classification of **global** maximizers of \(p_j\) is:

1. If \(\Delta<0\), only \(j=m\) maximizes \(p_j\).
2. If \(\Delta=0\) (equivalently \(z=m+2\)), exactly \(j=m-1,m,m+1\) maximize \(p_j\).
3. If \(\Delta>0\) equals \(k(k+1)\) for an integer \(1\le k\le m-1\), exactly four values maximize \(p_j\): \(m-k-1,m-k,m+k,m+k+1\).
4. In every remaining case with \(\Delta>0\), let \(k\) be the smallest member of \(\{1,\ldots,m\}\) satisfying \(k(k+1)>\Delta\), if one exists, and let \(k=m\) otherwise. Then the two and only two maximizers are \(m-k,m+k\).

In particular, all possible mode multiplicities are \(1,2,3,4\), and **the upper bound four is sharp infinitely often**. For each integer \(r\ge1\), define the positive odd integers \(x_r,y_r\) by
\[
x_r+y_r\sqrt2=(1+\sqrt2)^{2r+1},\qquad
m_r=(x_r-1)/2,\quad a_r=(y_r-1)/2,\quad z_r=a_r+2.
\]
These populations have four exactly equally high global stationary peaks, at \(m_r-a_r-1,m_r-a_r,m_r+a_r,m_r+a_r+1\). For \((m,z)=(3,4)\), the modes are \(0,1,5,6\). For \((m,z)=(20,16)\), they are \(5,6,34,35\).

At those same Pell-family parameters, sampling the two influencers *with* replacement produces only two modes, at \(m_r-a_r,m_r+a_r\). Thus the seemingly minor requirement that the two influencers be different changes the exact discrete coexistence structure, even on a complete graph.

## Assumptions and scope

There are \(N=2m+2z\) labelled agents on a complete graph. Exactly \(z\) always support opinion \(+\) and exactly \(z\) always support opinion \(-\), and neither group ever changes. The other \(2m\) agents are susceptible. At each elementary step, one uniformly chosen agent is offered an update. If that agent is susceptible, two **different** agents are drawn uniformly from the remaining \(N-1\) agents. Only if their two opinions coincide does the susceptible adopt that opinion. Otherwise nothing happens. Zealots never update. Sampling is repeated afresh at subsequent steps; the pair is not permanently assigned. The stationary measure refers to this finite irreducible Markov chain, not to a deterministic mean-field fixed point or an infinite-population limit.

The statement covers every pair of integers \(m\ge1,z\ge2\). It does not cover asymmetric zealot populations, groups of three or more influencers, stochastic independence, or a general network topology. The mode count is for the probability distribution of the **number** of positive susceptibles, not the probability of an individual labelled microconfiguration.

## Proof

**1. Exact birth and death probabilities.** Denote the current number of positive susceptibles by \(j\). A negative susceptible is chosen with probability \((2m-j)/N\), and among the other \(N-1\) agents there are \(j+z\) supporters of opinion \(+\). Consequently,
\[
T_j^+=\frac{2m-j}{N}\frac{(j+z)(j+z-1)}{(N-1)(N-2)}.
\]
Similarly,
\[
T_j^-=\frac{j}{N}\frac{(2m-j+z)(2m-j+z-1)}{(N-1)(N-2)}.
\]
Every interior birth and death probability is strictly positive since \(z\ge2\); hence the chain on \(\{0,\ldots,2m\}\) has a unique stationary distribution. Its detailed-balance ratios are
\[
\frac{p_{j+1}}{p_j}
=\frac{2m-j}{j+1}\frac{(j+z)(j+z-1)}{(2m-j+z-1)(2m-j+z-2)}.
\tag{1}
\]
Equivalently, a completely explicit positive stationary weight is
\[
p_j=\frac{w_j}{\sum_{\ell=0}^{2m}w_\ell},\qquad
w_j=\binom{2m}{j}(j+z-1)!(j+z-2)!
(2m-j+z-1)!(2m-j+z-2)!.
\tag{2}
\]
The factorial formula can be verified by taking consecutive ratios. In particular \(p_{2m-j}=p_j\).

**2. A factored mode test.** Since all denominators in (1) are positive, the sign of \(p_{j+1}-p_j\) is that of
\[
\begin{aligned}
G_j={}&(2m-j)(j+z)(j+z-1)\\
&-(j+1)(2m-j+z-1)(2m-j+z-2)\\
={}&(2m-2j-1)\bigl[j^2+(1-2m)j-2m+(z-1)(z-2)\bigr].
\end{aligned}
\tag{3}
\]
For the left half, put \(j=m-1-k\), where \(0\le k\le m-1\). Then
\[
G_{m-1-k}=(2k+1)\bigl[k(k+1)-\Delta\bigr].
\tag{4}
\]
As \(j\) increases toward the center, \(k\) strictly decreases, so the sign in (4) can switch only once, from positive to negative. Therefore the stationary probabilities first increase and then decrease on the left half, possibly with one equal-height pair; reflection symmetry supplies the right half. When \(\Delta<0\), all left ratios strictly exceed one, giving a unique central peak. When \(\Delta=0\), the last left ratio equals one and all previous ones exceed one: \(p_{m-1}=p_m=p_{m+1}\) are the three maxima. When \(\Delta>0\), a root \(k\in\{1,\ldots,m-1\}\) gives exactly one equal-height adjacent peak pair on the left and its reflected counterpart on the right. Otherwise the sign change occurs between two consecutive ratios and gives exactly one peak on each side, with the location specified in the finding; the endpoint case \(z=2\) is included. This proves the complete classification and the bound of four.

**3. Infinitely many fourfold cases.** Let \(x_r+y_r\sqrt2=(1+\sqrt2)^{2r+1}\), with \(r\ge1\). Because the norm is \(-1\),
\[
x_r^2-2y_r^2=-1
\quad\Longleftrightarrow\quad
m_r(m_r+1)=2a_r(a_r+1).
\tag{5}
\]
The integers \(m_r>a_r\ge2\) increase without bound. With \(z_r=a_r+2\), equation (5) implies
\[
\Delta=m_r(m_r+1)-(a_r+1)a_r=a_r(a_r+1).
\]
The third case of the classification therefore applies with \(k=a_r\), proving four stationary maxima at every indicated size.

**4. Exact contrast with replacement.** If an influencer can be selected twice, the two factors in the numerator of (1) become \((j+z)^2\), and the denominator factors become \((2m-j+z-1)^2\). In the left half the analogue of (4) is \((2k+1)[k(k+1)-\Delta_R]\), where \(\Delta_R=m(m+1)-(z-1)^2\). On the Pell family \(\Delta_R=a_r^2-1\), which lies strictly between \((a_r-1)a_r\) and \(a_r(a_r+1)\) for \(a_r\ge2\). Thus no ratio equals one at the global peaks, and the two unique modes are \(m_r-a_r,m_r+a_r\). This comparison uses the same \(N,m,z\) and differs only in the two-agent panel sampling rule.

## Verification

Run `python verify.py` with SymPy 1.14.0 (`requirements.txt`) from the directory containing this document. The independent checker tests the polynomial factorization symbolically, constructs rational stationary weights from update rates for all \(1\le m\le15\) and \(2\le z\le m+11\), compares all exact global mode sets against the classification, verifies detailed balance using independently computed combinatorial draw counts, and checks the Pell family and the with-replacement comparison. All checks completed successfully. Exact finite arithmetic is used, with no simulation tolerance.

The computer checks cover finitely many values. The universal mode classification and the infinite Pell family are proved algebraically in the preceding section.

## Relationship to prior work

Mobilia (2015) establishes a two-opinion nonlinear voter model with inflexible zealots, its exact birth-death stationary distribution, and the symmetric bimodal-to-unimodal transition, but explicitly samples the \(q\) influencers **with possible repetition**; see its Sec. II and Eqs. (2), (10). The present finite-size formula and Pell plateau family concern a different transition kernel. Jędrzejewski, Sznajd-Weron and Szwabiński (2015, 2016 journal version) discuss the physical importance of choosing distinct influencers and compare methods of panel composition, but study a modified model with independent updates on networks, not this symmetric finite-size zealot stationary-mode census. Weron, Nyczka and Szwabiński (2024) systematically compare replacement policies in a \(q\)-voter model **with independence**, not the opposing-zealot stationary law here. The possibility that another publication treats precisely this variant, or obtains the result through an equivalent birth-death formulation, remains an originality risk.

The new mathematical claim is the complete finite-population mode classification and the infinite arithmetic coexistence family, **not** the standard detailed-balance formula in isolation, nor the previously known macroscopic zealotry transition.

## Limitations

The stationary modes are modes of a lumped population-count distribution; they need not be modes of the full labelled-state law. The result does not concern switching times, mixing times, quasistationary distributions, or the width and relative mass of metastable peaks. Four equal *point probabilities* need not imply four well-separated macroscopic phases. The Pell family demonstrates infinitely many exact finite-size ties, without claiming a thermodynamic phase transition attributable to those ties. Only the symmetric two-neighbor, no-replacement process defined above is classified.

## References

1. M. Mobilia, *Nonlinear q-voter model with inflexible zealots* (first arXiv version 2015-06-16), arXiv:1506.04911, Phys. Rev. E 92, 012803 (2015). https://arxiv.org/abs/1506.04911
2. A. Jędrzejewski, K. Sznajd-Weron and J. Szwabiński, *Mapping the q-voter model: From a single chain to complex networks* (first arXiv version 2015-01-21), arXiv:1501.05091, Physica A 446, 110–119 (2016). https://arxiv.org/abs/1501.05091
3. T. Weron, P. Nyczka and J. Szwabiński, *Composition of the Influence Group in the q-Voter Model and Its Impact on the Dynamics of Opinions*, Entropy 26, 132 (2024). https://doi.org/10.3390/e26020132
