# Orientation-selected entropy and exact stripe-wave counts in a three-color cyclic automaton

## Finding

Consider the deterministic three-color cyclic cellular automaton on the square lattice with its eight-site Moore neighborhood and integer excitation threshold \(1\leq\theta\leq8\). A site advances by one modulo three exactly when at least \(\theta\) neighbors have its successor color. Write \(Y_\theta^{\mathrm{ax}}\) for all horizontal-stripe configurations \(c(i,j)=a_i\) that advance by one stripe index per update, and \(Y_\theta^{\mathrm{diag}}\) for all diagonal-stripe configurations \(c(i,j)=a_{i+j}\) satisfying the analogous one-index shift. These are the **complete** unit-index-speed traveling families within their respective stripe classes, not selected collections of sample waves.

The topological entropies of one time-step, restricted to the respective traveling families, are exactly
\[
 h_{\mathrm{ax}}(\theta)=\begin{cases}\log2,&1\le\theta\le3,\\0,&4\le\theta\le8,\end{cases}
\]
\[
 h_{\mathrm{diag}}(\theta)=\begin{cases}
 0,&\theta=1,\\
 \log\rho,&\theta=2,\\
 \log\bigl((1+\sqrt5)/2\bigr),&\theta=3,\\
 0,&4\le\theta\le8,
 \end{cases}
 \qquad \rho=1.866760399173862\ldots,
\]
where \(\rho\) is the Perron root of \(\lambda^4-2\lambda^3+\lambda-1\). In particular, the orientation affects whether exponentially many distinct unit-speed waves exist at threshold one, and distinguishes two strictly positive entropies at thresholds two and three.

For \(1\le\theta\le3\), the axial traveling family is a mixing three-symbol edge shift with adjacency matrix \(I+P\), where \(P\) is the cyclic three-color permutation. Its number of period-dividing-\(n\) points, for every \(n\ge1\), and Artin–Mazur zeta function are
\[
 \#\operatorname{Fix}(F_\theta^n\mid Y_\theta^{\mathrm{ax}})
 =2^n+2\cos(n\pi/3),\qquad
 \zeta(z)=\frac1{(1-2z)(1-z+z^2)}.
\]
For \(n\ge3\), the same formula counts horizontal-strip unit-speed configurations on an \(n\)-periodic horizontal cylinder (with vertical circumference at least three). Every primitive temporal period \(n\ge3\) occurs; primitive period two does not.

## Assumptions and scope

Sites are indexed by \((i,j)\in\mathbb Z^2\), the color alphabet is \(\mathbb Z/3\mathbb Z\), and neighbors are exactly the eight **distinct offsets** \((u,v)\in\{-1,0,1\}^2\setminus\{(0,0)\}\). On a finite horizontal-periodic cylinder, use circumference \(n\ge3\) and vertical circumference at least three, so no neighbor offsets are identified. The update \(F_\theta\) is simultaneous. In the formulas above, a 'traveling' stripe means \((F_\theta c)(i,j)=c(i+1,j)\); for diagonal stripes this corresponds to increasing \(i+j\) by one, not to a Euclidean unit translation along the diagonal normal. No claim is made that every configuration of the full two-dimensional automaton is a stripe or a traveling wave.

Topological entropy is the usual topological entropy of the compact, shift-invariant **one-dimensional stripe family** under the induced time evolution. The set of all unit-index-speed stripe waves is closed by a finite-block condition, and the induced update is exactly the left shift. Entropy in this theorem is not the entropy of the entire two-dimensional configuration system.

## Proof

**Step 1: necessity of binary increments.** If the stripe word \(a_i\) shifts by one index under a single update, then each symbol \(a_{i+1}\) must equal either \(a_i\) or \(a_i+1\pmod3\): the local rule can only keep or advance a color. Define the unique binary increments \(b_i\in\{0,1\}\) by \(a_{i+1}=a_i+b_i\pmod3\). Conversely, every bi-infinite binary sequence determines exactly three color sequences, by selecting \(a_0\); this finite-to-one coding preserves exponential word-growth rates and hence entropy.

**Step 2: axial stripes.** At a site of axial index \(i\), the only possible successor-colored neighboring column is \(i+1\), which contributes exactly three Moore offsets when \(b_i=1\). The column at \(i-1\) is either equal or predecessor-colored, so cannot excite the site. Hence the successor-neighbor count is \(3b_i\). The requirement that the next color equal \(a_{i+1}\) is therefore satisfied for **every** binary sequence when \(1\le\theta\le3\), and only for the all-zero increment sequence when \(4\le\theta\le8\). Thus the positive-entropy axial family is the edge shift of the three-color graph with allowed steps \(0\) and \(+1\), adjacency \(A=I+P\). It is primitive because the graph is strongly connected and has loops. Its eigenvalues are \(2,e^{i\pi/3},e^{-i\pi/3}\), giving entropy \(\log2\), the exact trace formula, and the zeta formula by \(\det(I-zA)^{-1}\). If \(\theta\ge4\), only three spatially constant words remain and the entropy is zero. For \(n\ge3\), the binary increment word consisting of three successive ones followed by \(n-3\) zeros yields a primitive \(n\)-cycle; a primitive two-cycle is absent because \(\#\operatorname{Fix}(F_\theta^2)=\#\operatorname{Fix}(F_\theta)=3\).

**Step 3: diagonal stripes.** With stripe index \(i+j\), the eight Moore offsets have index changes \(-2,-1,0,+1,+2\) with multiplicities \(1,2,2,2,1\). For a binary increment sequence, the exact number of successor-colored neighbors at index \(i\) is
\[
 N_i=2b_i+(b_i\oplus b_{i+1})+b_{i-2}b_{i-1}.
\]
Here \(\oplus\) denotes exclusive OR. Indeed, the \(+1\) offsets contribute \(2b_i\); the \(+2\) offset contributes precisely when exactly one of two forward increments equals one; the \(-1\) offsets never contribute; and the \(-2\) offset contributes when both backward increments equal one. Thus the **necessary and sufficient** traveling condition is
\[
 b_i=1\Longrightarrow N_i\ge\theta,
 \qquad b_i=0\Longrightarrow N_i<\theta,
 \quad\text{for every }i\in\mathbb Z.
\]
This is a four-bit finite-type constraint. Index an eight-state directed graph by triples \((a,b,c)\in\{0,1\}^3\); insert an edge from \((a,b,c)\) to \((b,c,d)\) precisely when \(2c+(c\oplus d)+ab\ge\theta\) for \(c=1\), or \(2c+(c\oplus d)+ab<\theta\) for \(c=0\). Let \(M_\theta\) be its integer adjacency matrix. Direct finite determinant expansion gives
\[
\begin{array}{c|l}
\theta&\det(\lambda I-M_\theta)\\\hline
1&\lambda^6(\lambda-1)^2\\
2&\lambda^4(\lambda^4-2\lambda^3+\lambda-1)\\
3&\lambda^5(\lambda-1)(\lambda^2-\lambda-1)\\
4,5,6,7,8&\lambda^7(\lambda-1).
\end{array}
\]
The graph for \(\theta=2\) is strongly connected, with a self-loop, so its Perron root is the unique maximal-modulus eigenvalue \(\rho>1\). At \(\theta=3\), the entropy-carrying strongly connected component consists of the golden-mean binary sequences (no two adjacent ones), while an all-one cycle is entropy zero. At \(\theta=1\) only the all-zero and all-one binary bi-infinite sequences are permitted; at \(\theta\ge4\) only the all-zero sequence remains. The topological entropy of each finite-type shift is the logarithm of its adjacency spectral radius. The three-to-one color lift does not alter this entropy. This yields all asserted orientation-dependent values.

**Step 4: finite-cylinder interpretation.** For an axial period \(n\), a binary increment word closes modulo three exactly when its number \(k\) of ones is divisible by three. There are three choices of initial color. Therefore
\[
 3\sum_{k\equiv0\ (\mathrm{mod}\ 3)}\binom nk
 =\operatorname{tr}(A^n)=2^n+2\cos(n\pi/3).
\]
A fixed, finite vertical circumference at least three does not change any of the predecessor counts in Step 2.

## Verification

The accompanying standalone `verify_cca_waves.py` uses only the Python standard library. It enumerates the eight-state diagonal adjacency matrices, reconstructs their characteristic polynomials using Newton identities and exact integer arithmetic, and checks the **full two-dimensional Moore update** against the symbolic traveling constraints for all horizontally periodic widths three through eight, each threshold one through eight, and both orientations. It also checks the finite axial count identity and diagonal binary transfer traces. Its observed output ends with `ALL CHECKS PASSED`. The finite computations are **not** a proof for all stripe lengths or the infinite lattice; Steps 1–4 provide that proof.

## Relationship to prior work

Sharipov, Koterle, Grozdanov, and Prosen (arXiv:2503.16593, first submitted March 20, 2025) investigate ergodic classes of reversible three-state brickwork cellular automata. Their paper explicitly singles out topological entropy as a further analytic diagnostic. Their rules are one-dimensional and reversible, unlike this two-dimensional irreversible cyclic rule, so none of their classifications imply this theorem.

Fisch, Gravner, and Griffeath (1991) study threshold-range scaling in Greenberg–Hastings and cyclic cellular automata, and **already identify** the horizontal/vertical band-propagation threshold \(\theta\le3\) for a Moore radius-one neighborhood. This threshold, by itself, is not claimed new. Urías, Salazar-Anaya, Ugalde, and Enciso (1996) develop general finite-automaton methods for traveling configurations and their topological entropies, an important methodological predecessor. The present contribution is the concrete complete **two-orientation, three-color** stripe classification, including the distinct diagonal transfer matrices and sharp entropy values, the positive-entropy interval specific to each orientation, and the axial exact periodic-orbit census. Muñoz and Nuño (arXiv:2610.37990, submitted October 27, 2026) analyze the **same three-color Moore rule** through symmetry-resolved periods and observed attracting three-band waves. Their inspected model, traveling-wave discussion, and parameter sweeps do not give the all-stripe unit-speed SFT, either diagonal transfer polynomial, or a topological entropy classification. Their finding that observed waves from sampled initial conditions have three bands is not a classification of all wave configurations; many of the waves here may have negligible basins. The broad 1996 algorithmic precedent and specialized literature create residual historical-priority risks.

## Limitations

Only stripe configurations and their unit-index-speed traveling subsets are classified; the theorem does not claim to classify spirals, other velocities, diagonal translations by other lattice vectors, general two-dimensional transients, or topological entropy of the complete automaton. Diagonal \(\theta=3\) may include heteroclinic binary sequences not contained in its entropy-maximizing component. The spectral method is finite-state and algorithmic; further searches of the specialized traveling-automata literature might locate an earlier application to this precise rule. The verification script tests finite sizes and does not replace the infinite symbolic argument.

## References

1. R. Sharipov, M. Koterle, S. Grozdanov, T. Prosen, *Ergodic behaviors in reversible 3-state cellular automata*, arXiv:2503.16593, version first publicly submitted March 20, 2025. https://arxiv.org/abs/2503.16593
2. R. Fisch, J. Gravner, D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing **1** (1991), 23–39. DOI: 10.1007/BF01890834. Open full text: https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf
3. J. Urías, G. Salazar-Anaya, E. Ugalde, A. Enciso, *Traveling patterns in cellular automata*, Chaos **6** (1996), 493–503. https://doi.org/10.1063/1.166190
4. F. J. Muñoz, J. C. Nuño, *Symmetry-resolved periods in a cyclic-dominance automaton: separating intrinsic from lattice-induced periodicity*, arXiv:2610.37990, first public October 27, 2026. https://arxiv.org/abs/2610.37990 (later self-review)
5. Mathematics Subject Classification 2020, entry 37B40 (topological entropy), https://mathscinet.ams.org/msc/msc2020.html
