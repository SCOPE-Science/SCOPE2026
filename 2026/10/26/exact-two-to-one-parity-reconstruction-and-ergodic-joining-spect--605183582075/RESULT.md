# Exact two-to-one parity reconstruction and ergodic joining spectrum for a resonant Sturmian product

## Finding
Fix any irrational \(0<\alpha<1\). Let \(X_\alpha\subset\{0,1\}^{\mathbb Z}\) be the two-sided Sturmian subshift of slope \(\alpha\). Consider the one-block parity map
\[
\Phi:X_\alpha\times X_\alpha\longrightarrow\{0,1\}^{\mathbb Z},\qquad
\Phi(u,v)_n=u_n\oplus v_n,
\]
with the diagonal shift, and write \(Y_\alpha=\Phi(X_\alpha\times X_\alpha)\). Then the following constitute one exact description of this parity factor.

**Complete ordered fibres.** For every nonzero \(w\in Y_\alpha\), there is a unique unordered pair \(\{u,v\}\subset X_\alpha\) with \(u\ne v\) and \(u\oplus v=w\); its ordered fibre is precisely \(\{(u,v),(v,u)\}\). The fibre of the all-zero word is the entire diagonal \(\{(u,u):u\in X_\alpha\}\), which is uncountable. Consequently the induced shift is topologically conjugate to the symmetric square \(\operatorname{Sym}^2(X_\alpha)\) with its diagonal collapsed to a single fixed point.

**Complete ergodic-measure spectrum.** Every shift-ergodic Borel probability on \(Y_\alpha\) is \(\nu_\delta\) for exactly one \(\delta\in[0,1/2]\), where \(\nu_\delta\) is the law of the parity of the two Sturmian codings at phases \(t\) and \(t+\delta\), with \(t\) uniform on \(\mathbb R/\mathbb Z\). Here \(\nu_0\) is the Dirac mass at the all-zero word; \(\nu_\delta=\nu_{1-\delta}\), and there are no other coincidences. All of \(Y_\alpha\) has zero topological entropy, despite having a continuum of distinct ergodic probability measures.

An exact recovery procedure for nonzero outputs first reconstructs the symmetric difference of two circle intervals from its complete Fourier--Bohr coefficients, then recovers the unordered pair of phases via finite-support jump parity, and finally resolves the Sturmian singular choices from their two-site discrepancies. Finite-support outputs with exactly two adjacent ones arise from the opposite singular choices at one phase and are included in the two-point ordered-fibre statement.

## Assumptions and scope
Write \(\mathbb T=\mathbb R/\mathbb Z\), \(I=[1-\alpha,1)\subset\mathbb T\), and \(R_\alpha(t)=t+\alpha\pmod1\). Define the lower mechanical coding
\[
c_t(n)=\lfloor t+(n+1)\alpha\rfloor-\lfloor t+n\alpha\rfloor\quad(n\in\mathbb Z),
\]
for a representative \(t\in[0,1)\). Its upper version uses ceilings instead of floors. The closure of all these codings is \(X_\alpha\). The standard phase map \(\pi:X_\alpha\to\mathbb T\) sends each coding to its intercept; it intertwines the shift with \(R_\alpha\). Away from \(B=\{-k\alpha\pmod1:k\in\mathbb Z\}\), the phase fibre contains one coding; over each \(t\in B\) it contains exactly the lower and upper codings. Their difference is the indicator of two adjacent sites. Each \(\alpha\) considered here is irrational; no uniform claim for rational slopes, noisy observations, or finite output windows is made.

For each \(\delta\in\mathbb T\), \(\nu_\delta\) is the pushforward of normalized Haar measure in \(t\) under \(t\mapsto c_t\oplus c_{t+\delta}\). Choices at the countable set of singular intercepts do not affect this law. The representatives \(\delta\in[0,1/2]\) identify \(\delta\) with \(-\delta\) in \(\mathbb T\).

## Proof
**1. Full sequences determine symmetric differences of arcs.** For phases \(t,s\in\mathbb T\), put
\[
g_{t,s}(x)=\mathbf1_I(x+t)\oplus\mathbf1_I(x+s)\quad(x\in\mathbb T).
\]
Each actual Sturmian code agrees with \(\mathbf1_I(t+n\alpha)\) at all but at most two coordinates. Therefore \(u\oplus v\) for intercepts \((t,s)\) differs at only finitely many coordinates from \(g_{t,s}(n\alpha)\). If two parity outputs coincide, the associated piecewise-constant functions \(g_{t,s}\) agree almost everywhere: otherwise they differ on a nonempty open arc, visited infinitely often by the dense irrational rotation. Equivalently, for every \(k\in\mathbb Z\), the coefficient
\[
\lim_{N\to\infty}\frac{1}{2N+1}\sum_{n=-N}^{N}(u_n\oplus v_n)e^{-2\pi i k n\alpha}
=\int_{\mathbb T}g_{t,s}(x)e^{-2\pi i kx}\,dx
\]
exists. This follows from equidistribution and the finite exceptional set. The coefficients uniquely determine \(g_{t,s}\) in \(L^2(\mathbb T)\).

**2. Finite jump parity determines the unordered phases.** Work in the vector space of finitely supported functions \(\mathbb T\to\mathbb F_2\). Let \(\tau\) translate support by \(\alpha\). The jump locations of \(g_{t,s}\), counted modulo two, are \((1+\tau)\eta_{t,s}\), where \(\eta_{t,s}\) records one selected endpoint of each of the intervals \(I-t\) and \(I-s\). Their selected endpoints are the translates of \(-t\) and \(-s\) by the same fixed constant. The operator \(1+\tau\) is injective on finite support: if \((1+\tau)\eta=0\), then \(\eta\) is constant along every \(\alpha\)-orbit; irrationality makes every such orbit infinite, so finite support forces \(\eta=0\). It follows that equality of the symmetric-difference functions implies equality of the two-element phase multisets modulo two. For \(t\ne s\), this gives \(\{t,s\}=\{t',s'\}\). When \(t=s\), the jump function is zero and every diagonal phase produces the same zero-valued circle function.

**3. Symbolic boundary choices cause no additional collisions.** For \(t\notin B\), the coding is unique. For a singular intercept \(t=-k\alpha\), its lower and upper codes differ at exactly \(k-1\) and \(k\). Denote the resulting finitely supported parity pulse by \(e_{k-1}+e_k\) over \(\mathbb F_2\). Pulses corresponding to distinct singular phases are distinct nonzero vectors. Thus, with two distinct phases fixed, changing any one or both of their upper/lower branch choices changes the output: a single pulse is nonzero, and two different pulses do not cancel. Consequently a nonzero output associated with distinct phases has one unordered coding pair. If both intercepts coincide, equal branches yield zero, while opposite branches yield one adjacent two-site pulse; different singular phases give distinct pulses. No distinct-phase pair can yield a finite-support output, because its circle symmetric difference is a nonempty open set and hence has positive orbit frequency. Therefore every nonzero output has exactly one unordered pair and two ordered predecessors, whereas zero has precisely the diagonal.

**4. The quotient topology.** The continuous parity map is invariant under transposition of its two coordinates. It collapses the diagonal of the compact symmetric square to the zero word and is otherwise injective by Step 3. The induced map from the diagonal-collapsed compact quotient to the Hausdorff compact subshift \(Y_\alpha\) is thus a continuous bijection and hence a shift-equivariant homeomorphism. Since Sturmian shifts have zero topological entropy, so does their product and its factor.

**5. All invariant ergodic laws.** The phase-pair map sends the diagonal shift to \((t,s)\mapsto(t+\alpha,s+\alpha)\) on \(\mathbb T^2\). Every ergodic invariant measure on this torus is Haar measure on one circle \(s-t=\delta\), because \(s-t\) is invariant and each remaining irrational rotation is uniquely ergodic. Any invariant ergodic measure upstairs projects to such a Haar law. The exceptional Sturmian phase fibres lie over countably many points, which have Haar measure zero, so the lift is unique. Conversely each phase-circle Haar law has an ergodic lift. Pushing these laws through parity gives exactly \(\nu_\delta\). Swapping the two inputs identifies \(\delta\) with \(-\delta\), and Step 3 reconstructs their unordered phases from every nonzero output; hence no other two nonzero separations yield the same ergodic law. At separation zero, almost every input pair has identical codings and the law is \(\delta_{0^{\mathbb Z}}\). Every invariant measure on the factor lifts to an invariant measure upstairs; choosing ergodic components shows this list exhausts the factor's ergodic measures.

## Verification
A dependency-free Python verifier accompanies this statement. Invoke `python3 verify.py`. It checks that for rational coprime approximants \(89/233\) and \(144/377\), all unordered off-diagonal phase pairs in the respective discrete rotation grids have distinct length-one-period parity words (\(27028\) and \(70876\) pairs), and all diagonal pairs yield zero. Separately, with 90-digit decimal arithmetic at the golden-mean slope, it checks the lower/upper singular difference at two adjacent indices over 701 sites and four shifted singular intercepts. These finite checks test the coding and branch formulas only. The irrational no-collision statement follows from the injectivity of \(1+\tau\) on finite supports, and the ergodic classification follows from the torus phase factor; neither assertion is inferred from finite enumeration.

## Relationship to prior work
Berstel and Vuillon, *Coding rotations on intervals* (2001 preprint, 2002 journal), develop recoding of rotation partitions by Sturmian words, not the inverse problem for the coordinatewise parity of two full Sturmian subshifts. Frid and Jamet, *The number of binary rotation words* (2013 preprint), count binary rotation languages and, through their Lemma 2, identify first differences with differences of same-slope Sturmian codings (whose reductions modulo two give XOR); their finite-word collision lemmas do not supply this symmetric-square quotient or the complete invariant-measure classification. Barbieri, Labbé and Starosta, *A characterization of Sturmian sequences by indistinguishable asymptotic pairs* (2020 preprint), prove the classical two-site singular branch structure used here, but do not study XOR fibres or the measures of this parity factor. A distinct parity reconstruction theorem for **rationally independent** slopes does not imply the present equal-slope statement: here the phase-difference coordinate is invariant and the entire diagonal collapses. Relevant records and primary-source searches yielded no equivalent result; this is an evidence-limited originality assessment, not a claim of certified historical priority.

## Limitations
The classification assumes exactly two two-sided Sturmian inputs with the same known irrational slope and exact, infinite binary outputs. For a nonzero output, recovering the circle step function from Fourier--Bohr data uses all frequencies and does not give a stable finite-data reconstruction algorithm. The zero output has an uncountable ordered fibre, so there is no global inverse. Numerical tests of rational approximants are consistency checks, not proofs for all irrational slopes. Earlier specialized parity-factor results not exposed by the searches remain a priority risk.

## References
- J. Berstel and L. Vuillon, *Coding rotations on intervals*, arXiv:math/0106217v1, first public 2001-06-26, https://arxiv.org/abs/math/0106217.
- A. Frid and D. Jamet, *The number of binary rotation words*, arXiv:1302.3722v1, first public 2013-02-15, https://arxiv.org/abs/1302.3722.
- S. Barbieri, S. Labbé and Š. Starosta, *A characterization of Sturmian sequences by indistinguishable asymptotic pairs*, arXiv:2011.08112v1 (2020), https://arxiv.org/abs/2011.08112.
