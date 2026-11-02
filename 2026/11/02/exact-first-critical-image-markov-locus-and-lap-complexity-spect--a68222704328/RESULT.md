# Exact first-critical-image Markov locus and lap-complexity spectrum of the M-map

## Finding
For the Lawnik–Berezowski M-map, the natural partition by all turning points has forward-invariant endpoints at **exactly five** parameters in the full allowed interval. At all five, every iterate has an explicit exact lap count and topological entropy. Three nontrivial interior parameters exhibit respectively the spectral growth factors \(2+\sqrt2\), \(3\), and \(1+\sqrt3\), giving exact topological entropies \(\log(2+\sqrt2)\), \(\log3\), and \(\log(1+\sqrt3)\). The endpoints give \(\log4\) and \(\log2\).

For \(p\in[1/4,1/2]\), define
\[
F_p(x)=\begin{cases}
\dfrac{x}{p}\left(2-\dfrac{x}{p}\right),&0\le x\le1/2,\\[4pt]
\dfrac{1-x}{p}\left(2-\dfrac{1-x}{p}\right),&1/2<x\le1.
\end{cases}
\]
Let \(\ell_n(p)\) be the number of maximal intervals of strict monotonicity of \(F_p^n\), \(n\ge1\). In the interior \(p\in(1/4,1/2)\), set \(B_p=\{0,p,1/2,1-p,1\}\). The condition \(F_p(B_p)\subseteq B_p\) holds if and only if \(p\) is one of the following three values:

* \(p_{-}\): unique root in \((1/4,1/2)\) of \(4p^3-4p+1=0\), approximately \(0.269594436405444558\).
* \(p_{0}=1-1/\sqrt2\), approximately \(0.292893218813452476\).
* \(p_{+}\): unique root in \((1/4,1/2)\) of \(4p^3-4p^2+4p-1=0\), approximately \(0.319448459735676311\).

Including the two endpoints, the exact lap counts and entropy are

| Parameter | Exact number \(\ell_n\), \(n\ge1\) | Topological entropy |
|---|---|---|
| \(p=1/4\) | \(4^n\) | \(\log4\) |
| \(p=p_-\) | \(\ell_1=4,\ \ell_2=14,\ \ell_n=4\ell_{n-1}-2\ell_{n-2}\) for \(n\ge3\) | \(\log(2+\sqrt2)\) |
| \(p=p_0\) | \(4\cdot3^{n-1}\) | \(\log3\) |
| \(p=p_+\) | \(\ell_1=4,\ \ell_2=10,\ \ell_n=2\ell_{n-1}+2\ell_{n-2}\) for \(n\ge3\) | \(\log(1+\sqrt3)\) |
| \(p=1/2\) | \(2^n\) | \(\log2\) |

The finite-lap generating functions \(\mathcal L_p(z)=\sum_{n\ge1}\ell_n(p)z^n\) at the three interior parameters are
\[
\mathcal L_{p_-}(z)=\frac{4z-2z^2}{1-4z+2z^2},\quad
\mathcal L_{p_0}(z)=\frac{4z}{1-3z},\quad
\mathcal L_{p_+}(z)=\frac{4z+2z^2}{1-2z-2z^2}.
\]

## Assumptions and scope
The map is a **continuous interval self-map** in the source's entire domain \(1/4\le p\le1/2\). At interior parameters it has exactly three turning points \(p\), \(1/2\), and \(1-p\). The classification is of parameters whose *immediate turning-point partition* is forward invariant. No claim is made that these are all postcritically finite parameters, all parameters with some other Markov partition, or a formula for entropy at arbitrary \(p\).

## Proof
**1. Critical images and exact locus.** Direct differentiation gives on the left half
\[
F_p'(x)=\frac{2}{p}\left(1-\frac{x}{p}\right),
\]
with the right half obtained by reflection. The four monotonic arms have endpoints \(0,p,1/2,1-p,1\). Their images satisfy
\[
F_p(0)=F_p(1)=0,\quad F_p(p)=F_p(1-p)=1,\quad
F_p(1/2)=v(p)=\frac{4p-1}{4p^2}.
\]
Thus \(F_p(B_p)\subseteq B_p\) is equivalent to \(v(p)\in B_p\). For \(1/4<p<1/2\), the critical value lies strictly between zero and one, and hence \(v(p)\) must equal \(p\), \(1/2\), or \(1-p\). Clearing denominators gives respectively
\[
4p^3-4p+1=0,\qquad 2p^2-4p+1=0,\qquad
4p^3-4p^2+4p-1=0.
\]
The first cubic is strictly decreasing on this interval, with opposite endpoint signs; the second polynomial has the unique admissible root \(1-1/\sqrt2\); the final cubic is strictly increasing, again with opposite signs. These three and only these three interior values close the partition. Numerically and exactly by the increasing critical-value relation, their order is \(p_-<p_0<p_+\). At \(p=1/4\), the central valley maps to zero; at \(p=1/2\), all turning points coalesce to the logistic-map apex.

**2. Markov transition matrices.** Order the four atoms as \(I_0=[0,p]\), \(I_1=[p,1/2]\), \(I_2=[1/2,1-p]\), and \(I_3=[1-p,1]\). At each interior Markov parameter their images are unions of whole atoms. With \(A_{ij}=1\) if \(F_p(I_i)\) covers \(I_j\), the three matrices are
\[
A_- =\begin{pmatrix}1&1&1&1\\0&1&1&1\\0&1&1&1\\1&1&1&1\end{pmatrix},\quad
A_0 =\begin{pmatrix}1&1&1&1\\0&0&1&1\\0&0&1&1\\1&1&1&1\end{pmatrix},\quad
A_+ =\begin{pmatrix}1&1&1&1\\0&0&0&1\\0&0&0&1\\1&1&1&1\end{pmatrix}.
\]
For example, the image of each outer atom is all of \([0,1]\), while the image of either inner atom is \([v(p),1]\). At the respective parameters, \(v(p)\) is \(p\), \(1/2\), or \(1-p\), yielding precisely these rows.

**3. Exact lap enumeration.** Every admissible length-\(n\) path through the four atoms determines a nondegenerate monotonic cylinder of \(F_p^n\), since the branch images cover the target atoms; inverse images on each arm are single intervals. At the base level the atom boundaries are all genuine turning points, and under backward iteration any newly introduced boundary is a preimage of a turning point before time \(n\). The turning points are strict extrema (the middle one is a strict valley), so adjacent cylinders do not join to form a larger monotonicity interval. Even when a turning point maps to another turning point at one of the listed parameters, its local extremum persists under further iterations. It follows that
\[
\ell_n(p)=\mathbf1^{\mathsf T}A_p^{n-1}\mathbf1,\qquad n\ge1,
\]
with \(\mathbf1=(1,1,1,1)^{\mathsf T}\).

The characteristic polynomials are
\[
\det(\lambda I-A_-)=\lambda^2(\lambda^2-4\lambda+2),\quad
\det(\lambda I-A_0)=\lambda^3(\lambda-3),\quad
\det(\lambda I-A_+)=\lambda^2(\lambda^2-2\lambda-2).
\]
Matrix summation yields the stated recurrences and rational generating functions. The matrices have a positive-power communicating component attaining their Perron roots, so these roots govern the exponential growth of the positive total path counts. For continuous piecewise-monotone interval maps, the Misiurewicz–Szlenk lap-growth formula is
\[
h_{\mathrm{top}}(F_p)=\lim_{n\to\infty}\frac{\log\ell_n(p)}{n}.
\]
The three positive growth factors are \(2+\sqrt2\), \(3\), and \(1+\sqrt3\), proving their entropy values.

**4. Endpoints.** At \(p=1/4\), the central valley equals zero and every one of the four monotone arms maps onto \([0,1]\). Therefore every iterate has \(4^n\) laps and entropy \(\log4\). At \(p=1/2\), the formula reduces to \(4x(1-x)\), a two-arm full map, giving \(2^n\) laps and entropy \(\log2\). This exhausts the stated five-point classification.

## Verification
The standalone script `proofcheck/mmap_markov_check.py` verifies the three algebraic critical-value equations, each transition matrix's characteristic polynomial and generating function, and 69 independently reconstructed Markov-image or iterated-preimage lap checks. For each interior parameter, it enumerates preimages of all turning points through seven iterates at 70-digit precision and compares their number plus one with the matrix-predicted lap count. Those finite checks detect implementation mistakes but do not replace the proof of the all-iterate formulas. Execute it with Python 3, SymPy, and mpmath installed: `python proofcheck/mmap_markov_check.py`.

## Relationship to prior work
Lawnik and Berezowski introduced exactly this M-map and analyzed fixed points, numerical bifurcations, Lyapunov exponents, and invariant-density behavior. They identify \(p=1-1/\sqrt2\) in their fixed-point classification, but the inspected article's analysis does not state the five-parameter forward-invariant turning partition classification or the exact finite-n lap and topological-entropy formulas. These results concern topological entropy, not the numerically estimated metric Lyapunov exponent or encryption entropy. The method uses the established lap-growth theorem of Misiurewicz and Szlenk together with a standard finite Markov matrix construction; the claim of a new result is the **exact specialized classification and explicit evaluated laws**, not those general principles.

## Limitations
The five values are **not** claimed to be the only Markov or postcritically finite parameters; longer critical orbits can close for additional parameters. No global entropy curve or invariant density is computed. The generating-function counts are for maximal monotonicity intervals, not for distinct periodic points or the number of topological conjugacy classes. The finite numerical tests are reproducibility checks, not an infinite proof. A fully exhaustive publication-priority survey or independent mathematical review has not been performed; an equivalent M-map kneading calculation outside the inspected literature remains a genuine risk.

## References
1. M. Lawnik and M. Berezowski, “New Chaotic System: M-Map and Its Application in Chaos-Based Cryptography,” *Symmetry* **14** (2022), article 895, published 27 April 2022. DOI: `10.3390/sym14050895`. Public full text: https://www.researchgate.net/publication/360245838_New_Chaotic_System_M-Map_and_Its_Application_in_Chaos-Based_Cryptography ; publisher: https://www.mdpi.com/2073-8994/14/5/895 .
2. M. Misiurewicz and W. Szlenk, “Entropy of piecewise monotone mappings,” *Studia Mathematica* **67** (1980), 45–63. DOI: `10.4064/sm-67-1-45-63`.
3. M. Misiurewicz and P. Raith, “Strict inequalities for the entropy of transitive piecewise monotone maps,” *Discrete and Continuous Dynamical Systems* **13** (2005), 451–468. DOI: `10.3934/dcds.2005.13.451`.
