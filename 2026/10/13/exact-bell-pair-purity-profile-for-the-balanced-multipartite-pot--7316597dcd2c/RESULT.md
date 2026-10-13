# Exact Bell-pair purity profile for the balanced multipartite potential
## Finding
For every integer \(K\ge 2\), define the \(2K\)-qubit state
\[
|B_K\rangle=|\Phi^+\rangle^{\otimes K},
\qquad
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}.
\]
For \(1\le m\le K\), let
\[
\overline P_{{K,m}}=\binom{{2K}}{{m}}^{{-1}}\sum_{{|A|=m}}\operatorname{{tr}}(\rho_A^2)
\]
be the uniform mean purity over all \(m\)-qubit subsystems. Then
\[
\boxed{{\overline P_{{K,m}}=\frac{{[x^m](1+x+x^2)^K}}{{\binom{{2K}}{{m}}}}}}.
\]
In particular, for balanced bipartitions \(m=K\), Facchi et al.'s potential of multipartite entanglement is
\[
H(B_K)=\frac{{T_K}}{{\binom{{2K}}{{K}}}},
\qquad
T_K=[x^K](1+x+x^2)^K,
\]
where \(T_K\) is the central trinomial coefficient. Its sharp first-order asymptotic is
\[
H(B_K)\sim \frac{{\sqrt3}}2\left(\frac34\right)^K.
\]
The universal lower bound for a balanced \(K\)-qubit reduction is \(2^{{-K}}\), so
\[
\frac{{H(B_K)}}{{2^{{-K}}}}\sim
\frac{{\sqrt3}}2\left(\frac32\right)^K\longrightarrow\infty.
\]
Thus the average balanced purity tends to zero, but the Bell-pair product is exponentially far from the perfect balanced-purity lower bound in multiplicative units.

Equivalently, Scott's normalized purity measure satisfies
\[
Q_m(B_K)=\frac{{2^m}}{{2^m-1}}\left(1-\overline P_{{K,m}}\right).
\]
For every fixed \(m\), \(Q_m(B_K)\to1\) as \(K\to\infty\); more strikingly, the extremal balanced member also satisfies
\[
Q_K(B_K)=\frac{{2^K}}{{2^K-1}}\left(1-H(B_K)\right)\longrightarrow1.
\]
Nevertheless \(|B_K\rangle\) is a tensor product of two-qubit entangled blocks, so its entanglement depth is exactly \(2\), and for \(K\ge2\) it is separable across a nontrivial partition into Bell-pair blocks and therefore is not genuinely multipartite entangled.

## Assumptions and scope
The statement concerns pure qubit states and uniform averages over subsets. For the balanced potential, the number of qubits is even, \(n=2K\), so the balanced subsystem size is exactly \(K\). The result does not claim that the product of Bell pairs was previously unrecognized as nongenuine multipartite entanglement; that qualitative obstruction is explicit in earlier literature. The new claim is the exact all-subsystem-size purity profile, its central-trinomial balanced specialization, and the resulting sharp asymptotic separation between normalized saturation and entanglement depth.

## Proof
Fix a subset \(A\) of \(m\) qubits. For each Bell pair, there are three possibilities: \(A\) contains neither endpoint, exactly one endpoint, or both endpoints. If exactly one endpoint is retained, that pair contributes \(I/2\) to the reduced state and therefore contributes a factor \(1/2\) to the purity. If zero or two endpoints are retained, the corresponding reduced factor is pure (or absent) and contributes purity \(1\).

Suppose \(t\) Bell pairs have both endpoints in \(A\) and \(r\) Bell pairs have exactly one endpoint in \(A\). Then
\[
2t+r=m,
\qquad
\operatorname{{tr}}(\rho_A^2)=2^{{-r}}.
\]
For fixed \(t,r\), the number of such subsets is
\[
\binom Kt\binom{{K-t}}r 2^r.
\]
Multiplying by the purity cancels the factor \(2^r\). Therefore the sum of purities over all \(m\)-subsets is
\[
\sum_{{t=0}}^{{\lfloor m/2\rfloor}}
\binom Kt\binom{{K-t}}{{m-2t}}
=[x^m](1+x+x^2)^K.
\]
Dividing by \(\binom{{2K}}m\) proves the exact profile.

At \(m=K\), the numerator is the central trinomial coefficient \(T_K\). Using the constant-term representation
\[
T_K=\frac1{{2\pi}}\int_{{-\pi}}^\pi(1+2\cos\theta)^K\,d\theta
\]
and the expansion
\[
1+2\cos\theta=3-\theta^2+O(\theta^4)
=3\exp\left(-\frac{{\theta^2}}3+O(\theta^4)\right),
\]
Laplace's method gives
\[
T_K\sim\frac{{\sqrt3}}{{2\sqrt{{\pi K}}}}3^K.
\]
Stirling's formula gives
\[
\binom{{2K}}K\sim\frac{{4^K}}{{\sqrt{{\pi K}}}},
\]
so
\[
H(B_K)\sim\frac{{\sqrt3}}2\left(\frac34\right)^K.
\]
The lower bound \(2^{{-K}}\) follows because a density matrix on \(2^K\) dimensions has purity at least \(1/2^K\). The ratio formula follows immediately.

Finally, Scott's definition is the affine normalization of the same mean purity. Substitution yields the displayed expression for \(Q_m(B_K)\). For fixed \(m\), the coefficient ratio tends to \(2^{{-m}}\), while for \(m=K\) the preceding asymptotic shows \(H(B_K)\to0\); hence both limits of \(Q_m\) equal \(1\). The state itself is explicitly a product of \(K\) Bell-pair factors, proving entanglement depth exactly \(2\).

## Verification
The coefficient identity was replayed independently by direct enumeration of all subsets for \(1\le K\le8\) and all \(1\le m\le K\), using exact rational arithmetic. For the balanced cases, the first values of the numerator are
\[
T_1=1,\quad T_2=3,\quad T_3=7,\quad T_4=19,\quad T_5=51,
\]
and the exact averages begin
\[
H(B_2)=\frac12,\qquad H(B_3)=\frac7{{20}},\qquad H(B_4)=\frac{{19}}{{70}}.
\]
The bundled checker recomputes the subset enumeration, the polynomial coefficient, and these balanced values without external packages.

The asymptotic is analytic, not inferred from finite data. The finite replay checks the combinatorial identity only; Laplace's method and Stirling's formula establish the infinite-size statement.

## Relationship to prior work
Facchi, Florio, Marzolino, Parisi, and Pascazio define the balanced average purity \(H\) as their potential of multipartite entanglement and explicitly identify \(2^{{-K}}\) as the fixed-bipartition minimum. Their paper studies the optimization and statistical mechanics of this balanced average, but a search of the inspected full text found no Bell-pair, EPR, or central-trinomial specialization.

Scott defines the uniform-subset quantities \(Q_m\) as affine normalizations of average subsystem purity and notes that larger \(m\) probe larger blocks. The inspected paper gives formulas for GHZ and W families, but no Bell-pair-product formula was found.

De Oliveira, Rigolin, and de Oliveira explicitly use a tensor product of Bell pairs to show that the one-site Meyer-Wallach/global-entanglement quantity can be maximal on a state lacking genuine multipartite entanglement. Their later generalized quantity also evaluates a four-qubit EPR-pair product, but it uses a different averaging prescription: for that example their second-order value is \(7/9\), whereas the uniform two-subsystem Scott value from the present formula is \(2/3\). Those papers therefore cover the qualitative warning but do not imply the exact uniform-subset profile or the balanced central-trinomial asymptotic proved here.

Targeted searches for Bell-pair products, Scott quantities, balanced bipartition purity, central trinomial coefficients, and equivalent asymptotic formulations did not locate an implication-equivalent statement. This is evidence of noncoverage, not a proof of historical uniqueness.

## Limitations
The result is an exact benchmark for one structured family, not a classification of states at fixed average purity and not a new entanglement-depth witness. It shows that normalized average-purity saturation alone does not force large entanglement depth; it does not say that the unnormalized Facchi potential itself mistakes Bell-pair products for perfect MMES, because their multiplicative gap from the lower bound actually diverges.

The strongest residual originality risk is a poorly indexed calculation of the same Bell-pair purity profile in later work on generalized global entanglement. The closest inspected papers analyze Bell-pair products under different averaging conventions, and no source inspected here states the central-trinomial balanced formula or its asymptotic ratio to \(2^{{-K}}\).

## References
1. P. Facchi, G. Florio, U. Marzolino, G. Parisi, and S. Pascazio, “Statistical mechanics of multipartite entanglement,” arXiv:0803.4498; *Journal of Physics A: Mathematical and Theoretical* **42** (2009), 055304, DOI: 10.1088/1751-8113/42/5/055304.
2. A. J. Scott, “Multipartite entanglement, quantum-error-correcting codes, and entangling power of quantum evolutions,” arXiv:quant-ph/0310137; *Physical Review A* **69** (2004), 052330.
3. T. R. de Oliveira, G. Rigolin, and M. C. de Oliveira, “Genuine multipartite entanglement in quantum phase transitions,” arXiv:quant-ph/0507253.
4. G. Rigolin, T. R. de Oliveira, and M. C. de Oliveira, “Operational classification and quantification of multipartite entangled states,” arXiv:quant-ph/0603215.
