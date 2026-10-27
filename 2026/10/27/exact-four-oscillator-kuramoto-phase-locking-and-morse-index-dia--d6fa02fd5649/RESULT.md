# Exact four-oscillator Kuramoto phase-locking and Morse-index diagram

## Finding
For the attractive all-to-all Kuramoto flow on four oscillators with natural frequencies \((-3,-1,1,3)\), write
\[
\dot\theta_j=\omega_j+\frac K4\sum_{k=1}^4\sin(\theta_k-\theta_j),\qquad K>0.
\]
Equilibria are identified only modulo common rotation, not modulo permutation of oscillators. Define
\[
x_*=\frac{20+2\sqrt{73}}3,\quad
K_*=\frac{2x_*}{\sqrt{x_*-9}+\sqrt{x_*-1}},\quad
K_0=\frac9{\sqrt2},\quad K_1=12.
\]
Then \(0<K_*<K_0<K_1\), with \(K_*\approx4.750657407544264\). The following table is the COMPLETE count of phase-locked states, with nondegenerate states grouped by the number of positive real eigenvalues of the linearized flow after removal of the rotational zero mode (the unstable index).

| Coupling | Total states | Unstable indices of nondegenerate states | Degenerate states |
| --- | ---: | --- | --- |
| \(0<K<K_*\) | 0 | none | 0 |
| \(K=K_*\) | 1 | none | 1 |
| \(K_*<K<K_0\) | 2 | \(0:1,\ 1:1\) | 0 |
| \(K=K_0\) | 2 | \(0:1\) | 1 |
| \(K_0<K<K_1\) | 4 | \(0:1,\ 1:2,\ 2:1\) | 0 |
| \(K=K_1\) | 6 | \(0:1,\ 1:2,\ 2:1\) | 2 |
| \(K>K_1\) | 8 | \(0:1,\ 1:4,\ 2:3\) | 0 |

At each exceptional coupling the degenerate state has exactly one additional zero eigenvalue in the three-dimensional reduced system. At \(K_*\) this is a fold of the stable and index-one branches; at \(K_0\) an unstable four-branch junction (one incoming and three outgoing branches) occurs; at \(12\) two simultaneous folds produce the four additional higher-index states. In particular exactly one asymptotically stable phase-locked state exists for every \(K>K_*\) except at the singular coupling values, where that stable state remains nondegenerate at \(K_0\) and \(12\); at \(K_*\) there is no hyperbolically stable state.

## Assumptions and scope
The phases are elements of \(\mathbb R/2\pi\mathbb Z\), coupling is exactly \(K/4\) per ordered edge, and all frequencies and phase indices are labeled. A phase-locked state has a common angular velocity equal to the frequency mean, here zero. Equivalence means adding a common constant to all four phases. "Degenerate" refers to an additional zero eigenvalue beyond the ubiquitous rotational eigenvalue; the table does not assign a hyperbolic Morse index at exceptional parameter values. Stable means asymptotically stable on the rotational quotient.

## Proof
**1. Exhaustive parameterization.** Let \(re^{i\psi}=\frac14\sum_j e^{i\theta_j}\). At equilibrium \(r>0\), because \(r=0\) would force \(\dot\theta_j=\omega_j\ne0\). Use rotation to make \(\psi=0\). Put \(q=Kr\); then \(q\ge3\), \(\sin\theta_j=\omega_j/q\), and \(\cos\theta_j=\varepsilon_j\sqrt{1-\omega_j^2/q^2}\), where \(\varepsilon_j\in\{-1,1\}\) when \(q>3\). The sine components cancel in the order parameter. With \(x=q^2\), \(h=\sqrt{x-9}\), \(l=\sqrt{x-1}\), and \(a=\varepsilon_1+\varepsilon_4\), \(b=\varepsilon_2+\varepsilon_3\), self-consistency is equivalent to
\[
K=\frac{4x}{ah+bl},\qquad ah+bl>0.
\]
Since \(l>h>0\) and \(a,b\in\{-2,0,2\}\), the only possibilities are \((a,b)=(2,2),(2,0),(0,2),(-2,2)\). They give, respectively,
\[
A:\ K_A(x)=\frac{2x}{h+l}\quad(1\text{ labeled branch}),\qquad
B:\ K_B(x)=\frac{2x}{h}\quad(2),
\]
\[
C:\ K_C(x)=\frac{2x}{l}\quad(2),\qquad
D:\ K_D(x)=\frac{2x}{l-h}=\frac{x(h+l)}4\quad(1).
\]
The last equality uses \(l^2-h^2=8\). Conversely each root \(x>9\) and each compatible sign pattern constructs a valid equilibrium by \(\theta_j=\operatorname{atan2}(\omega_j/\sqrt x,\varepsilon_j\sqrt{1-\omega_j^2/x})\). No phase-locked states have been omitted.

**2. Branch extrema and enumeration.** The derivative of \(K_A\) has the sign of \(2hl-x\), whose only solution above nine is \(x=x_*\), since its squared equation is \(3x^2-40x+36=0\). Thus \(A\) has one strict minimum \(K_*\), decreases from \(K_0\) at \(x\downarrow9\), and increases to infinity. Similarly \(B\) has a single minimum \(12\) at \(x=18\) and diverges at both endpoints; \(C\) and \(D\) increase strictly from \(K_0\) to infinity. The branch counts away from boundary parameters are therefore, respectively, \(0,2,4,8\) in the four open coupling intervals. At \(x=9\), the two outer cosine signs collapse to zero, and the positive order parameter requires both inner cosines positive. This is exactly ONE state at \(K=K_0\), merging the lower \(A\), both \(C\), and \(D\) branches. At the \(B\) minimum, its two independently labeled sign assignments yield two distinct states at \(K=12\), not four; adding the other four branches gives six states.

**3. Complete instability count.** For a fixed equilibrium let \(c_j=\cos\theta_j\), \(s_j=\sin\theta_j\). Its negative Jacobian is the symmetric weighted Laplacian
\[
H=Kr\operatorname{diag}(c)-\frac K4(cc^{\mathsf T}+ss^{\mathsf T}).
\]
Since \(\sum c_j=4r>0\) and \(\sum s_j=0\), every class modulo rotation has a unique representative in \(c\cdot v=0\). There the quadratic form equals
\[
q\sum_jc_jv_j^2-\frac K4(s\cdot v)^2.
\]
For \(x>9\), the first term restricted to this hyperplane is nondegenerate with exactly \(n\) negative directions, where \(n\) is the number of negative \(c_j\). Its rank-one negative perturbation adds one negative direction when \(T>1\), adds no direction when \(T<1\), and creates exactly one additional zero at \(T=1\), where
\[
T=\frac K{4q}\sum_j\frac{s_j^2}{c_j}.
\]
This identity follows from a one-dimensional Schur complement; no positivity assumption on the original diagonal form is needed. The correction from projection onto \(c\cdot v=0\) vanishes because \(\sum_js_j=0\). Substitution gives
\[
T_A=\frac{x}{hl}-1,\qquad T_B=\frac9{x-9},\qquad
T_C=\frac1{x-1},\qquad T_D<0.
\]
Hence \(A\) has index one for \(9<x<x_*\), and index zero above; \(B\) has index two for \(9<x<18\) and index one above; \(C\) has index one; \(D\) has index two. Equalities occur only at the two fold thresholds. At \(q=3\), direct substitution of \(\cos\theta=(0,2\sqrt2/3,2\sqrt2/3,0)\) into \(H\) gives exactly one reduced zero mode, one reduced positive mode and one reduced negative mode. Thus the boundary state is degenerate with a one-dimensional reduced kernel. Combining the branch counts with these indices gives every row of the table and proves uniqueness of the index-zero state whenever it exists.

## Verification
`verify.py` is a standalone executable script (Python 3, NumPy, SciPy and SymPy). It verifies the exact polynomial for \(x_*\), four formula-based sign families, self-consistency and original vector-field residuals, and the three reduced Hessian eigenvalue signs at six parameter samples. Output produced from the attached script includes `VERIFY_OK` and totals 0, 2, 4, 4, 8, 8 at couplings 4, 5, 6.5, 8, 12.1, and 14. These numerical samples supplement, but do not replace, the exhaustive analytical branch and inertia proofs above. The exact algebraic thresholds and exceptional merging arguments are proven in the text.

## Relationship to prior work
Ottino-Löffler and Strogatz (2015 preprint) address finite-size corrections for uniform-frequency locking thresholds as the oscillator count tends to infinity; they do not tabulate the exact four-node Morse phase diagram. Verwoerd and Mason discuss fixed-point existence for finite networks. Xin, Kikkawa and Liu (2016) reduce general three/four-oscillator equilibrium equations to high-degree polynomials and bound total counts, without giving the three threshold values and the instability-index diagram here. Coss et al. (2017) provide general equilibrium-solving methods and illustrative four-node examples, but not this closed all-coupling, labeled-state Morse diagram. Yagasaki's 2025 uniform-frequency bifurcation theory concentrates its multi-branch statements on odd node counts; it does not supply this even four-node classification. General numerical/algebraic approaches and existence criteria are acknowledged rather than claimed as new.

## Limitations
The result is for the exactly labeled four-node complete graph with frequency scale fixed as shown. Common rescaling of all frequencies and coupling gives equivalent cases and is not a distinct result. At the degenerate thresholds only the reduced linear spectrum is classified, not all nonlinear normal-form coefficients or basins of attraction. An unindexed earlier special-case calculation is a residual priority risk. One strongly relevant 2016 conference paper could be assessed only through its publicly accessible abstract and sections; this incomplete comparison should be revisited in an independent literature audit.

## References
- B. Ottino-Löffler and S. H. Strogatz, *Kuramoto Model with Uniformly Spaced Frequencies: Finite-N Asymptotics of the Locking Threshold*, arXiv:1512.02321v1 (public 2015-12-08), https://arxiv.org/abs/1512.02321.
- G. A. Verwoerd and O. Mason, *Conditions for Existence of Fixed Points in a Finite System of Kuramoto Oscillators* (2007), 2007 proceedings publication.
- X. Xin, T. Kikkawa and Y. Liu, *Analytical Solutions of Equilibrium Points of the Standard Kuramoto Model: 3 and 4 Oscillators* (2016), DOI:10.1109/ACC.2016.7525284.
- Coss et al., *Computing all equilibria for the Kuramoto model*, arXiv:1705.06568 (2017), https://arxiv.org/abs/1705.06568.
- K. Yagasaki, *Bifurcations and Stability of Synchronized Solutions in the Kuramoto Model with Uniformly Spaced Natural Frequencies*, arXiv:2501.02889 (2025), https://arxiv.org/abs/2501.02889.
