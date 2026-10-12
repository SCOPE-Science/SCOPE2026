# Sharp finite-time mixing envelope for the three-card quantum stochastic shuffle

## Finding

Consider the random-transposition quantum stochastic walk on the six-dimensional group algebra of \(S_3\), starting at the identity permutation. Let \(\gamma>0\) be the classical jump rate, \(\alpha\geq0\) the coherent Hamiltonian coupling, and \(t>0\) the observation time. Write \(x=e^{-\gamma t}\), \(c=\cos(\alpha t)\), and let \(D(t,\alpha)\) denote the total-variation distance of the computational-basis distribution from uniformity.

For every \(x\in(0,1)\) and \(c\in[-1,1]\), put
\[
\xi=\frac{x^2(1+2c^2)}3,\qquad \eta=\frac{x(1+2c)}3.
\]
The exact distance is
\[
D_x(c)=\frac{|\xi+4\eta|+3\xi+2|\xi-2\eta|}{12}.
\]
**The sharp finite-time mixing theorem** states that its unique minimizing cosine is
\[
c_*(x)=\frac{2-\sqrt{4+4x-2x^2}}{2x}\ \in(-\tfrac12,0),
\]
and that the minimum over every \(\alpha\geq0\) is
\[
\boxed{\min_{\alpha\geq0}D(t,\alpha)=\frac{x^2}{6}\bigl(1+2c_*(x)^2\bigr)=\frac{2+x-\sqrt{4+4x-2x^2}}3.}
\]
Thus optimal angles satisfy \(\cos(\alpha t)=c_*(x)\); there are infinitely many equivalent angles, **not** a unique value of \(\alpha\). At these angles the two three-cycles have exactly uniform probabilities, while the identity and three transpositions carry all remaining deviation. The limit
\[
\boxed{\lim_{t\to\infty}e^{2\gamma t}\min_{\alpha\geq0}D(t,\alpha)=\tfrac14}
\]
is sharp. At \(\alpha=0\), the classical walk instead has \(D(t,0)=(x^2+4x)/6\); hence the optimized distance divided by the classical one is \((3/8)x+O(x^2)\). No finite \(t>0\) and finite \(\alpha\) yields exactly uniform probabilities.

## Assumptions and scope

The computational basis is \(\{|g\rangle:g\in S_3\}\). If \(T\) is the set of the three transpositions and \(L_\tau|g\rangle=|\tau g\rangle\), define
\[
H=\frac13\sum_{\tau\in T}L_\tau,\qquad
\Phi(\rho)=\frac13\sum_{\tau\in T}L_\tau\rho L_\tau^\dagger.
\]
The density matrix obeys the trace-preserving Lindblad equation
\[
\frac{d\rho}{dt}=-i\alpha[H,\rho]+\gamma\bigl(\Phi(\rho)-\rho\bigr),
\qquad\rho(0)=|e\rangle\langle e|.
\]
Set \(p_t(g)=\langle g|\rho(t)|g\rangle\) and \(D(t,\alpha)=\frac12\sum_{g\in S_3}|p_t(g)-1/6|\). The result optimizes over **unbounded, observation-time-dependent** \(\alpha\geq0\) at each fixed \(t>0\), with fixed \(\gamma>0\). It does not assert a uniform advantage of one fixed nonzero coupling for every observation time.

## Proof

**1. Central spectral structure.** As the sum of all transpositions is central in \(\mathbb C[S_3]\), \(H\) commutes with every \(L_\tau\) and therefore with \(\Phi\). Consequently the dissipative and unitary superoperators commute. The permutation transition probabilities equal the convolution of the classical random-transposition kernel at time \(t\) and the squared amplitudes of \(U=e^{-i\alpha tH}\) started at the identity.

The irreducible character table for the classes \(e\), transpositions, and three-cycles, respectively, is
\[
\chi_{\mathrm{triv}}=(1,1,1),\quad
\chi_{\mathrm{sign}}=(1,-1,1),\quad
\chi_{\mathrm{std}}=(2,0,-1).
\]
The central Hamiltonian has eigenvalues \(1,-1,0\) in those respective irreducibles. The matrix element of \(U\) from the identity to an element in each class is therefore
\[
u_e=\frac{2+c}{3},\qquad
u_{\mathrm{trans}}=-\frac{i\sin(\alpha t)}3,\qquad
u_{\mathrm{cycle}}=\frac{c-1}{3}.
\]
The three corresponding per-element quantum probabilities are \((2+c)^2/9\), \((1-c^2)/9\), and \((1-c)^2/9\). Their sign and standard **normalized** character transforms equal \((1+2c^2)/3\) and \((1+2c)/3\). In the classical walk, the sign and standard character modes decay as \(e^{-2\gamma t}=x^2\) and \(e^{-\gamma t}=x\). Multiplication of central Fourier transforms therefore yields modes \(\xi\) and \(\eta\) as in the finding.

Character inversion gives the individual probabilities
\[
p_t(e)=\frac{1+\xi+4\eta}{6},\quad
p_t(\tau)=\frac{1-\xi}{6}\quad(\tau\in T),\quad
p_t(r)=\frac{1+\xi-2\eta}{6}\quad(r\text{ a three-cycle}).
\]
Their six terms sum to one. Taking absolute deviations proves the exact formula for \(D_x(c)\).

**2. Sharp global minimization.** For fixed \(0<x<1\), there are exactly two sign-change points of the absolute-value expression: \(c_-(x)\in(-1,-1/2)\) determined by \(\eta=-\xi/4\), and \(c_*(x)\in(-1/2,0)\) determined by \(\eta=\xi/2\). The existence and uniqueness of the former follow from monotonicity of \(4+8c+x(1+2c^2)\) on \([-1,-1/2]\); the latter follows from monotonicity of \(2+4c-x(1+2c^2)\) on \([-1/2,0]\). The second equation gives
\[
2+4c_*=x(1+2c_*^2),
\]
whose sole solution in that interval is the stated square-root expression. The distance reduces to the following three pieces:
\[
D_x(c)=\begin{cases}
\xi/3-2\eta/3,&-1\le c<c_-,\\
\xi/2,&c_-\le c\le c_*,\\
\xi/6+2\eta/3,&c_*<c\le1.
\end{cases}
\]
The respective derivatives are \(4x(xc-1)/9<0\), \(2x^2c/3<0\), and \(2x(xc+2)/9>0\). Hence the unique global minimizing **cosine** is \(c_*\), and its distance is \(\xi(c_*)/2=x^2(1+2c_*^2)/6=(2+x-\sqrt{4+4x-2x^2})/3\); the last identity follows by substituting the displayed root and simplifying. Since \(\eta=\xi/2\) there, both three-cycles have probability exactly \(1/6\), while \(p_t(e)=(1+3\xi)/6\) and \(p_t(\tau)=(1-\xi)/6\). At \(\alpha=0\), inserting \(c=1\) yields \(D(t,0)=(x^2+4x)/6\).

**3. Sharp asymptotics and impossibility of exact mixing.** Expanding the defining equation near \(x=0\) gives \(c_*(x)=-1/2+3x/8+O(x^2)\). Inserting it gives \(D_{\min}=x^2/4+O(x^3)\) and, by division by the exact classical expression, the ratio \(3x/8+O(x^2)\). The matching upper and lower asymptotics prove the asserted sharp constant, not merely a finite-grid estimate. Finally \(\xi=x^2(1+2c^2)/3>0\) at every finite \(t>0\), whence each transposition retains \(p_t(\tau)<1/6\) and exact uniformity is impossible.

## Verification

Run `python3 verify.py` from the same directory as this document. This self-contained, standard-library-only program constructs all six permutations, the left-regular transposition Hamiltonian, and its three spectral projectors; independently propagates the classical distribution and the unitary; compares the resulting probabilities and total-variation distance against the formulas; checks 18,205 finite identities, inequalities, and grid comparisons, including exact rational tests. It prints `VERIFY_OK 18205 six_state_checks, sharp_envelope and asymptotic_ratio`. The continuum uniqueness and asymptotic statements are proved above; the finite checks are independent corroboration, not an infinite certificate.

## Relationship to prior work

He, Hutsalyuk, Mussardo, and Stampiggi (2026), arXiv:2609.13387, introduce the general coherent-plus-dissipative permutation-group quantum stochastic walk, prove the qualitative computational-basis speedup bound, and give an exact group-Fourier convolution formula. Inspection of the complete primary arXiv manuscript, particularly Section 5 Eqs. (68), (73)–(75), (85), and (99), confirms that its explicit small-group case is \(S_2\) and that its larger-size analysis does not give the present six-state exact extremum. The related openly available Stampiggi thesis reproduces those results in Chapter 3, especially Eqs. (3.94), (3.96), and (3.107)–(3.109), and analyzes the two-card case, the slow mode, and larger-size numerics. The model, group characters, Fourier machinery, and generic speedup are not new here. The **specific additional statement** is the sharp, time-dependent global minimization of the six-state total-variation functional over all coherent couplings, including the optimizer, exact parity-mode saturation, and sharp residual prefactor. This is a derivable refinement of the original Fourier solution; priority for implicit derivations has not been excluded.

Ahmadi, Belk, Tamon, and Wendler (2003) analyze instantaneous uniform mixing in purely unitary walks, including balanced complete multipartite graphs. Their theorem addresses a different, non-dissipative optimization and does not imply the fixed-time dissipative optimum above. Classical character-based analyses of random transpositions supply the \(S_3\) representation structure, and are likewise not claimed as new.

## Limitations

This is a sharp **six-state** result, not an extension to arbitrary symmetric groups. The coupling is allowed to depend on the observation horizon and has no upper bound; in fact the smallest optimal positive coupling behaves as \((2\pi/3)/t\) for large \(t\). The theorem gives a computational-basis total-variation optimum, not a trace-distance improvement (the latter is invariant under the commuting unitary). It does not optimize under control-amplitude costs or address experimental errors, different Lindblad jump operators, or general noncentral Hamiltonians. It does not establish that this optimal-control consequence was unknown to all prior authors.

## References

1. Feng He, Arthur Hutsalyuk, Giuseppe Mussardo, and Andrea Stampiggi, *Quantum Stochastic Walks on the Permutation Group*, arXiv:2609.13387 (first public 2026-09-11), https://arxiv.org/abs/2609.13387.
2. Andrea Stampiggi, *Statistical Spectroscopy of Quantum Many-Body Systems*, thesis (2026), Chapter 3, particularly Section 3.6 and Eqs. (3.94), (3.96), (3.107)–(3.109), https://iris.sissa.it/retrieve/a757920f-ee74-4fa1-8338-98fce66b67ed/phd_thesis_v3.pdf.
3. Amir Ahmadi, Ryan Belk, Christino Tamon, and Carolyn Wendler, *On Mixing in Continuous-Time Quantum Walks on Some Circulant Graphs*, Quantum Information and Computation 3 (2003), 611–618, https://www.rintonpress.com/xqic3/qic-3-6/611-618.pdf.
