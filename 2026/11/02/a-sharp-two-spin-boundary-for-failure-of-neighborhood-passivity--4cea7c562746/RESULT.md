# A sharp two-spin boundary for failure of neighborhood passivity under Glauber annealing

## Finding

Consider a ferromagnetic two-spin Ising system with one-spin-flip Glauber dynamics and a strictly cooling inverse-temperature schedule. The neighborhood-passivity condition used as a sufficient route to an annealing activity bound can fail immediately after the first temperature change, even when that change is arbitrarily small. More precisely, the neighborhood-passivity functional at the high-energy aligned configuration has exactly one sign transition as the high aligned-state energy varies. The threshold is characterized by a strictly decreasing explicit scalar function, and a finite rational example proves strict negativity. A one-spin system cannot show this failure after its first heat-bath update; two spins are minimal for this effect.

The finding concerns the *neighborhood-passivity assumption* of Luo et al., Eq. (41), **not** a counterexample to their separate activity inequality in Eq. (39).

## Assumptions and scope

Let \(\sigma=(\sigma_1,\sigma_2)\in\{+1,-1\}^2\). Use the ferromagnetic Ising Hamiltonian

\[
\mathcal H(\sigma)=-J\sigma_1\sigma_2-h(\sigma_1+\sigma_2)+C,
\qquad J>0,\quad h>0,
\]

where the additive constant \(C\) normalizes \(\mathcal H(++)=0\). Set

\[
A=2J+2h,\qquad B=4h.
\]

Then the ordered state energies are \(\bigl(0,A,A,B\bigr)\) for \(\bigl(++,+-,-+,--\bigr)\). The equivalent ferromagnetic parameter domain is \(A>0\) and \(A<B<2A\), since \(J=(2A-B)/4\) and \(h=B/4\). We initially choose the Gibbs law at inverse temperature \(0\leq\beta_0<\beta_1\), update once using the Glauber kernel at \(\beta_1\), and evaluate the functional using any \(\beta_2>\beta_1\).

Each update proposes one of the two spin flips with probability \(1/2\), accepting a proposal from configuration \(i\) to neighboring configuration \(j\) with probability

\[
\frac{1}{1+\exp[\beta_1(E_j-E_i)]}.
\]

For a distribution \(p\), the next-temperature neighborhood-passivity functional is precisely

\[
\mathcal P_i(\beta_2;p)=\sum_{j\sim i}
\tanh\!\left[\frac{\beta_2(E_j-E_i)}2\right](p_i-p_j).
\]

Define the quantities

\[
\begin{gathered}
y=e^{-\beta_0 A},\quad z=e^{-\beta_0 B},\quad Z=1+2y+z,\\
f=(1+e^{\beta_1 A})^{-1},\quad
 g=(1+e^{\beta_1(B-A)})^{-1},\\
H(B)=(3g-1)(y+z)-f(1+y).
\end{gathered}
\]

For each \(A>0\) and \(0\leq\beta_0<\beta_1\), there is exactly one \(B_*\) in the open interval

\[
A<B_*<A+\frac{\log2}{\beta_1}
\]

with \(H(B_*)=0\). The complete sign classification for every \(B>A\) is

\[
\boxed{\mathcal P_{--}(\beta_2;p^{(1)})<0\ \Longleftrightarrow\ A<B<B_*}.
\]

At \(B=B_*\) the functional is zero; at \(B>B_*\) it is positive. In particular, the nonempty interval \(A<B<\min\{B_*,2A\}\) consists entirely of ferromagnetic examples with strict failure. The conclusion holds for **every** strictly positive cooling increment \(\beta_1-\beta_0\), without a uniform lower bound on its size.

## Proof

**One-step distribution.** Initially

\[
p^{(0)}_{++}=Z^{-1},\quad
p^{(0)}_{+-}=p^{(0)}_{-+}=y/Z,\quad
p^{(0)}_{--}=z/Z.
\]

The acceptance for \(++\to+-\) is \(f\), and that for \(+-\to--\) is \(g\). The reverse acceptances are respectively \(1-f\) and \(1-g\). Summing the two incoming paths and the stay-put probability yields

\[
\begin{aligned}
p^{(1)}_{--}&=\frac{g(y+z)}Z,\\
p^{(1)}_{+-}=p^{(1)}_{-+}
 &=\frac{y(1+f-g)+f+z(1-g)}{2Z}.
\end{aligned}
\]

Consequently

\[
 p^{(1)}_{--}-p^{(1)}_{+-}=\frac{(3g-1)(y+z)-f(1+y)}{2Z}
 =\frac{H(B)}{2Z}.
\]

The configuration \(--\) has exactly two neighbors, both of energy \(A\), whereas its own energy is \(B>A\). Therefore

\[
\boxed{
\mathcal P_{--}(\beta_2;p^{(1)})
=-\tanh\!\left[\frac{\beta_2(B-A)}2\right]\frac{H(B)}Z.
}
\]

The hyperbolic tangent and \(Z\) are strictly positive, so the sign of the functional is the opposite of the sign of \(H\).

**Unique sharp boundary.** At the left endpoint \(B=A\) (used only to locate the root), \(g=1/2\) and \(z=y\); hence

\[
H(A)=y-f(1+y)=
\frac{e^{(\beta_1-\beta_0)A}-1}{1+e^{\beta_1 A}}>0.
\]

At \(B=A+\log2/\beta_1\), \(g=1/3\) and

\[
H(B)=-f(1+y)<0.
\]

On the intervening open interval \(g>1/3\), and differentiation at fixed \(A,\beta_0,\beta_1\) gives

\[
\begin{aligned}
H'(B)&=3g'(B)(y+z)+(3g-1)z'(B),\\
g'(B)&=-\beta_1g(1-g)<0,\\
z'(B)&=-\beta_0 z\leq0.
\end{aligned}
\]

Thus \(H'<0\) on the entire interval and the intermediate-value theorem gives exactly one root. For larger \(B\), \(3g-1\leq0\), which forces \(H(B)<0\), so no further roots occur. Taking the intersection with \(B<2A\) proves the claimed ferromagnetic open interval, for any nonzero cooling increment.

**Exact rational certificate.** Choose

\[
A=4,\quad B=5,\quad
\beta_0=\log\frac{20}{19},\quad
\beta_1=\log\frac32,\quad
\beta_2=\log2.
\]

Then \(J=3/4>0\), \(h=5/4>0\), \(f=16/97\), \(g=2/5\), \(y=(19/20)^4\), and \(z=(19/20)^5\). Direct rational arithmetic gives

\[
\begin{aligned}
H(5)&=\frac{293719}{16000000}>0,\\
p^{(1)}_{--}-p^{(1)}_{+-}&=\frac{293719}{108889390}>0,\\
\mathcal P_{--}(\beta_2;p^{(1)})
&=-\frac{293719}{163334085}<0.
\end{aligned}
\]

The last equality uses \(\tanh[(\log2)/2]=1/3\). All temperatures are finite and strictly decreasing.

**Minimal spin count.** For a single spin with two energy levels and the same one-flip Glauber acceptance, its transition kernel has identical columns, each equal to the Gibbs distribution at the update temperature \(\beta_1\). Therefore its distribution after one update is exactly Gibbs at \(\beta_1\), regardless of the initial distribution. Every local passivity term at \(\beta_2>0\) is then nonnegative. The two-spin construction is minimal in spin count for failure after one update under this update rule.

## Verification

The accompanying standard-library script `verify.py` builds the four-by-four transition matrix directly from the specified energy differences and exactly checks the post-update populations, normalization, and strict negative passivity fraction. It also verifies the separate next-step jump activity is below \(1/2\) in the explicit witness, so that no activity-conjecture counterexample is being inferred. A deterministic parameter sweep of 1,000 positive-cooling triples checks the sharp-root bracket, the two signs, and the existence of ferromagnetic violating energies; these are diagnostics, not substitutes for the analytic monotonicity argument.

Reproduce with `python verify.py` using Python 3 and its standard library only.

## Relationship to prior work

Luo, Zhen, Liu, Ebler, and Dahlsten derive the single-spin-flip Glauber annealing kernel in Eqs. (30)–(32), conjecture the jump activity bound in Eq. (39), and introduce neighborhood passivity in Eq. (41) as a sufficient hypothesis for that bound. Their seven-spin numerical examples satisfy neighborhood passivity. The present result shows that the proposed preservation hypothesis does not hold universally, already in a two-spin ferromagnet, and determines the exact boundary for the two-spin test family. It leaves the activity conjecture itself undecided.

Fukushima-Kimura and collaborators describe conventional Glauber sampling and analyze a different, parallel-update stochastic cellular automaton. The standard kernel used here is consistent with their definition, while their mixing/convergence analysis does not furnish the local passivity threshold above. These statements concern implication between the identified results, not proof of global bibliographic uniqueness.

## Limitations

The result is for one update from a Gibbs start, uniform single-spin proposals, two spins with symmetric positive field, and an observable at the next colder temperature. It does not cover arbitrary graphs, repeated update sign patterns, or every type of proposal rule. Failure of a *sufficient local condition* does not imply failure of the global jump-activity conjecture; indeed the exact witness has next-step activity below \(1/2\). Publication priority remains subject to broader literature on order inversion and finite-state nonautonomous Markov chains.

## References

1. Y. Luo, Y.-Z. Zhen, X. Liu, D. Ebler, and O. Dahlsten, *Bound on annealing performance from stochastic thermodynamics, with application to simulated annealing*, arXiv:2311.10424v1 (2023), especially Eqs. (30)–(41), https://arxiv.org/html/2311.10424v1. First public version: 2023-11-17.
2. B. H. Fukushima-Kimura, S. Handa, K. Kamakura, Y. Kamijima, K. Kawamura, and A. Sakai, *Mixing time and simulated annealing for the stochastic cellular automata*, arXiv:2007.11287 (2020), especially Eq. (1.4), https://arxiv.org/abs/2007.11287.
