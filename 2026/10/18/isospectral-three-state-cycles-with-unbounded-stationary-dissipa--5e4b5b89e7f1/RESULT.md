# Isospectral three-state cycles with unbounded stationary dissipation at fixed activity

## Finding

For every prescribed value \(s\in[0,\infty)\), there exists an irreducible three-state, bidirectionally connected continuous-time Markov generator whose stationary entropy-production rate is exactly \(s\), while the **entire** generator spectrum, invariant distribution, and stationary jump activity have the same values for every \(s\):
\[
\operatorname{spec}(Q)=\{0,-3-1/\sqrt2,-3+1/\sqrt2\},\qquad
\pi=(1/3,1/3,1/3),\qquad \mathcal A=2.
\]
All transition rates are strictly positive and all exit rates are less than \(5/2\). The claim remains true when requiring the three nonzero-state modes to have simple real eigenvalues (there are two distinct nonzero eigenvalues). The number three of states is minimal: an irreducible two-state continuous-time chain always has zero stationary entropy production. This establishes an exact obstruction to estimating thermodynamic dissipation from the complete relaxation spectrum, stationary populations, and stationary activity, even jointly.

## Assumptions and scope

There are three states \(0,1,2\), connected as the oriented cycle \(0\to1\to2\to0\). The Markov generator \(Q\) acts on probability row vectors and has nonnegative off-diagonal jump rates \(Q_{ij}\) and zero row sums. All six directed edge rates are strictly positive. The stationary distribution \(\pi\) is defined by \(\pi Q=0\). Its stationary average activity is \(\mathcal A=\sum_i\pi_i(-Q_{ii})\). The standard stationary entropy-production rate in natural logarithm units is
\[
\sigma(Q)=\sum_{\{i,j\}}(\pi_iQ_{ij}-\pi_jQ_{ji})
\log\!\frac{\pi_iQ_{ij}}{\pi_jQ_{ji}},
\]
where the sum is over all three unordered edges and the logarithm uses the current direction in the numerator. This expression is independent of edge orientation. It agrees with the familiar steady Markov-jump entropy production under local detailed balance.

For \(0\le t<1/2\), put \(h(t)=\sqrt{t^2+2/3}\) and define
\[
 a(t)=1+\frac t2+\frac{h(t)}2,\qquad
 b(t)=1+\frac t2-\frac{h(t)}2,\qquad
 c(t)=1-t.
\]
Define the family of generators
\[
 Q(t)=\begin{pmatrix}
 -(a+c)&a+t&c-t\\
 a-t&-(a+b)&b+t\\
 c+t&b-t&-(b+c)
 \end{pmatrix}.
\]
The forward oriented rates on the edges are \(a+t,b+t,c+t\); the reverse rates are \(a-t,b-t,c-t\). Only the finite-state jump process and its stationary thermodynamics are asserted; trajectory-resolved transition measurements, or knowledge of the generator entries themselves, can of course distinguish family members.

## Proof

**1. Strict positivity and fixed stationary law.** For the last edge, \(c+t=1\) and \(c-t=1-2t>0\). Also \(a-t=1-t/2+h/2>0\) and \(a+t>0\). For the remaining edge, \(b-t=(2-t-h)/2\). Both \(2-t\) and \(h\) are positive, and
\[
 (2-t)^2-h(t)^2=\frac{10}{3}-4t>\frac43>0,
\]
so \(b-t>0\), hence \(b+t>0\). Every directed transition is therefore positive. The row sums and column sums of \(Q(t)\) are zero by direct inspection, making \(\pi=(1/3,1/3,1/3)\) stationary. Because all transitions are positive, the invariant distribution is unique.

**2. Exactly fixed simple spectrum.** For arbitrary reals \(a,b,c,t\), expanding the characteristic polynomial of the displayed cycle matrix gives the identity
\[
 \det(zI-Q)=z\Bigl[z^2+2(a+b+c)z
 +3(ab+bc+ca+t^2)\Bigr].
\]
Our parametrization satisfies
\[
 a+b+c=3,\qquad ab=\frac56+t,\qquad
 bc+ca=(1-t)(2+t)=2-t-t^2,
\]
so \(ab+bc+ca+t^2=17/6\) exactly. Therefore
\[
 \det(zI-Q(t))=z\left(z^2+6z+\frac{17}{2}\right),
\]
whose distinct roots are \(0\) and \(-3\pm1/\sqrt2\), independent of \(t\). In particular every generator is diagonalizable over the reals and has the same nonoscillatory relaxation exponents.

**3. Fixed activity and bounded microscopic timescales.** The stationary mean number of jumps per unit time is
\[
 \mathcal A=\frac{(a+c)+(a+b)+(b+c)}3
 =\frac23(a+b+c)=2.
\]
The exit rates are \(a+b=2+t<5/2\), \(b+c=2-t/2-h/2<2\), and \(a+c=2-t/2+h/2\). Since \(h'(t)=t/h(t)<1\), the last quantity decreases with \(t\) and is at most \(2+1/\sqrt6<5/2\). Thus no unbounded escape rate or activity is hidden in the construction.

**4. A positive cycle current with arbitrarily large entropy production.** At uniform stationarity, each forward-minus-backward edge current is \(J(t)=((a+t)-(a-t))/3=2t/3\), with the analogous identity on the other two edges. Hence
\[
 \sigma(t)=\frac{2t}{3}
 \left[\log\frac{a+t}{a-t}+
 \log\frac{b+t}{b-t}+
 \log\frac{c+t}{c-t}\right].
\]
This is a continuous, finite, nonnegative function on \([0,1/2)\), with \(\sigma(0)=0\) and strict positivity for every \(t>0\). In the final ratio \((c+t)/(c-t)=1/(1-2t)\); the first two ratios approach strictly positive finite limits as \(t\uparrow1/2\). Consequently
\[
 \sigma(t)=\frac13\log\frac1{1-2t}+O(1)
 \quad\text{as}\quad t\uparrow\frac12,
\]
which diverges to \(+\infty\). The intermediate-value theorem now supplies, for **every** prescribed finite \(s\ge0\), some \(t\in[0,1/2)\) with \(\sigma(t)=s\). Importantly, the backwards rate \(1-2t\) is *positive for every finite target* \(s\); no zero rate or singular generator is needed.

**5. Minimality.** In an irreducible two-state Markov chain, stationarity forces \(\pi_0Q_{01}=\pi_1Q_{10}\). Its only edge has zero stationary current and therefore zero steady entropy production. An irreducible one-state chain likewise has zero production. Three states are consequently the smallest possible dimension for this phenomenon.

## Verification

Run `python verify.py` with Python 3 and SymPy available. The checker proves the general three-cycle characteristic-polynomial identity symbolically, independently verifies the parametrized identity, and tests positivity, double stochasticity of the generator in the zero-sum sense, activity, exit-rate bounds, stationary currents, characteristic coefficients, and entropy nonnegativity at 101 sample parameters. The exact proof above, rather than these samples, establishes all universal quantifiers and the divergent limit. No numerical continuation or external data are required.

## Relationship to prior work

Kolchinsky, Ohga and Ito's 2026 cycle-affinity/winding theorem constrains **nonreal** eigenvalues in nonequilibrium Markov generators; their Theorem 1 is expressly restricted to nonreal eigenpairs. This result gives a three-state obstruction in the complementary regime: the *entire* (simple, real) spectrum and stationary jump traffic remain fixed while cycle affinity and stationary dissipation are unbounded. The theorem in that paper does not furnish an upper entropy-production bound here.

Shiraishi's September 2026 counterexample shows that a **single complex slow eigenvalue** fails to furnish a proposed *lower* dissipation bound in a large layered Markov network with small stationary weight on the oscillating component. That work does not imply the present fixed, complete real spectrum, uniform invariant measure, fixed activity, three-state construction or an *unbounded upper* dissipation range.

Kolchinsky, Ohga and Ito's earlier 2024 spectral-perturbation bound provides entropy-production *lower bounds* for spectral differences from a reference equilibrium generator. Equality of the complete spectra of two different generators cannot supply an upper bound on production from that theorem. Standard cycle-current and affinity expressions are used as known thermodynamic identities, not claimed as new results. General rate-matrix inverse-spectral constructions may provide alternate proofs or stronger families; none is asserted to be ruled out by the literature comparison.

## Limitations

The phenomenon concerns spectra, invariant measures and scalar activity, not full transition kernels or eigenvectors: time-resolved, state-labelled transition statistics distinguish the generators. Unbounded dissipation arises as a reverse rate tends to zero, though each individual generator has strictly positive rates. The conclusion is not a statement about chains constrained by a fixed lower bound on every directed rate, and does not establish claims for arbitrary larger graphs. The normalization sets a common time scale; all rates are measured in its reciprocal units.

## References

1. A. Kolchinsky, N. Ohga and S. Ito, *Cycle affinity and winding localize eigenvalues of Markov generators*, arXiv:2605.15884v1 (first publicly available 15 May 2026), https://arxiv.org/abs/2605.15884 . Relevant main-text theorem statements and selected supplementary passages in v3 (8 October 2026) were compared for scope.
2. N. Shiraishi, *Second largest eigenvalue does not bound stationary entropy production*, arXiv:2609.34352v1 (2026), https://arxiv.org/abs/2609.34352 . Related but directionally different nonidentifiability obstruction.
3. A. Kolchinsky, N. Ohga and S. Ito, *Thermodynamic bounds on spectral perturbations, with applications to oscillations and relaxation dynamics*, arXiv:2304.01714 (2023); *Physical Review Research* 6, 013082 (2024), https://arxiv.org/abs/2304.01714 . Established spectral perturbation lower bounds.
4. A. Dechant, *Minimum entropy production, detailed balance and Wasserstein distance for continuous-time Markov processes*, arXiv:2110.01141 (2021), https://arxiv.org/abs/2110.01141 . General entropy-production and activity context.
