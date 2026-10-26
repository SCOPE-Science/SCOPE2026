# Sharp loss of unconditional positivity for stabilized Lawson–Euler on a weighted three-node path

## Finding

Consider the symmetric, conservative three-state generator
\[
Q_{a,b}=\begin{pmatrix}-a&a&0\\a&-a-b&b\\0&b&-b\end{pmatrix},\qquad a,b>0,
\]
and the stabilized Lawson–Euler map
\[
S_h=I+h\exp(\alpha hQ_{a,b})Q_{a,b},\qquad h>0,\quad\alpha>0.
\]
Its row and column sums are one for every step. The **complete all-step entrywise-positivity classification** is
\[
\boxed{S_h\geq0\text{ entrywise for every }h>0\quad\Longleftrightarrow\quad a=b\text{ and }\alpha\geq\frac{2}{3e}.}
\]
This threshold is sharp. In particular, every arbitrarily small edge-rate imbalance destroys all-step positivity for **every** fixed exponential stabilization coefficient, even where all nonstationary eigenmodes are strictly contractive.

If \(a>b\), the \((1,2)\) entry changes sign exactly once, at \(h_*=t_*(a,b)/\alpha\), and is strictly negative for all \(h>h_*\). If \(b>a\), the analogous statement holds for the \((2,3)\) entry. Put \(r=\max(a,b)\), \(s=\min(a,b)\), \(d=\sqrt{r^2-rs+s^2}\), and \(\ell_\pm=r+s\pm d\). Then the exact crossing time is
\[
\boxed{t_*(r,s)=\frac{1}{2d}\log\frac{\ell_+(2r-s+d)}{\ell_-(2r-s-d)}.}
\]
The logarithm's argument is greater than one for every \(r>s>0\). For fixed \(s>0\), near equal edge rates \(r=s+\delta\) the negative-entry onset has the sharp delay
\[
\boxed{t_*(s+\delta,s)=\frac{1}{2s}\log\frac{4s}{\delta}+o(1)\qquad(\delta\downarrow0).}
\]

## Assumptions and scope

The graph has precisely three vertices and two undirected edges, of conductances \(a,b>0\). The evolution \(u'=Q_{a,b}u\) is an irreducible symmetric continuous-time Markov/finite-volume diffusion system. We consider exact matrix exponentials and exact arithmetic. The parameter \(\alpha>0\) multiplies the reference generator in the stabilized Lawson–Euler scheme of Caliari, Cassini, Einkemmer and Ostermann; in their diffusion-splitting model it is usually restricted to \(0<\alpha\leq1\), within which the classification above still holds. The statement \(S_h\geq0\) means every component of \(S_h u\) remains nonnegative for **every** nonnegative \(u\), equivalent to entrywise matrix nonnegativity. The row/column-sum convention is immaterial here because \(Q_{a,b}\) is symmetric.

## Proof

**1. Reconstruct the update and conservation.** The source's stabilized Lawson–Euler formula is \(u^+=u+h\exp(hA)F(u)\). With \(F(u)=Q_{a,b}u\) and \(A=\alpha Q_{a,b}\) it gives exactly \(S_h\). Since \(Q_{a,b}{\bf1}=0\), also \(\exp(tQ_{a,b})Q_{a,b}{\bf1}=0\), and the same holds on the left by symmetry. Thus all row and column sums of \(S_h\) are one.

**2. Express entry signs as Markov-semigroup derivatives.** Let \(P(t)=\exp(tQ_{a,b})\). Matrix differentiation gives \(P'(t)=\exp(tQ_{a,b})Q_{a,b}\) and hence
\[
(S_h)_{ij}=\delta_{ij}+hP'_{ij}(\alpha h).
\]
For distinct vertices, \((S_h)_{ij}\) has precisely the sign of the corresponding transition-probability derivative.

**3. The exactly balanced path.** Suppose \(a=b=c>0\). The nonzero eigenvalues of \(-Q_{c,c}\) are \(c\) and \(3c\). Direct spectral projection yields the distinct off-diagonal derivatives
\[
P'_{12}(t)=P'_{23}(t)=c e^{-3ct},\qquad
P'_{13}(t)=\frac c2(e^{-ct}-e^{-3ct}),
\]
which are strictly positive for all \(t>0\). The diagonal derivatives are
\[
P'_{11}(t)=P'_{33}(t)=-\frac c2(e^{-ct}+e^{-3ct}),\qquad
P'_{22}(t)=-2c e^{-3ct}.
\]
Writing \(x=\alpha ch\), the middle diagonal of \(S_h\) is
\[
(S_h)_{22}=1-\frac{2x}{\alpha}e^{-3x}.
\]
The function \(2xe^{-3x}\) has a unique maximum \(2/(3e)\), attained at \(x=1/3\). Thus all-step positivity requires \(\alpha\geq2/(3e)\); if it fails, the middle diagonal becomes negative at \(h=1/(3\alpha c)\). For the endpoint diagonals,
\[
\frac{x}{2}(e^{-x}+e^{-3x})\leq\frac1{2e}+\frac1{6e}=\frac{2}{3e},
\]
using separately \(\sup_{x>0}xe^{-x}=1/e\) and \(\sup_{x>0}xe^{-3x}=1/(3e)\). At \(\alpha\geq2/(3e)\) every diagonal and off-diagonal is nonnegative. This proves both necessity and sufficiency in the balanced case, including equality.

**4. Any edge imbalance creates a unique negative off-diagonal ray.** The eigenvalues of \(-Q_{a,b}\) are \(0,\ell_-,\ell_+\), where
\[
d=\sqrt{a^2-ab+b^2}>0,\qquad\ell_\pm=a+b\pm d>0.
\]
The semigroup's adjacent entry on the \(a\)-edge has the exact spectral expansion
\[
P_{12}(t)=\frac13+\frac{2a-b-d}{6d}e^{-\ell_-t}
-\frac{2a-b+d}{6d}e^{-\ell_+t}.
\]
This follows uniquely from \(P_{12}(0)=0\), \(P'_{12}(0)=a\), and the two nonzero spectral rates. If \(a>b\), define
\[
C=\frac{2a-b-d}{6d}>0,\qquad B=\frac{2a-b+d}{6d}>0.
\]
The strict sign \(C>0\) follows from \((2a-b)^2-d^2=3a(a-b)>0\) and \(2a-b>0\). Differentiating gives
\[
P'_{12}(t)=\ell_+B e^{-\ell_+t}-\ell_-C e^{-\ell_-t}.
\]
The first term initially dominates because \(P'_{12}(0)=a>0\); the second decays more slowly. Therefore there is exactly one zero and it is \(t_*=(\ell_+-\ell_-)^{-1}\log(\ell_+B/(\ell_-C))\), which equals the displayed logarithmic formula since \(\ell_+-\ell_-=2d\). Its sign is positive before this zero and negative after. Consequently \((S_h)_{12}=hP'_{12}(\alpha h)<0\) for every \(h>t_*/\alpha\), for any \(\alpha>0\). When \(b>a\), exchange vertices \(1\leftrightarrow3\) and \(a\leftrightarrow b\) to obtain the corresponding result for \((S_h)_{23}\). This completes the global classification.

**5. Logarithmically delayed failure.** Fix \(s>0\), write \(r=s+\delta\), and expand as \(\delta\downarrow0\):
\[
d=s+\frac\delta2+O_s(\delta^2),\quad
\ell_-=s+O_s(\delta),\quad\ell_+=3s+O_s(\delta),
\]
\[
C=\frac\delta{4s}+O_s(\delta^2),\qquad
B=\frac13+O_s(\delta).
\]
Thus \(\ell_+B/(\ell_-C)=(4s/\delta)(1+O_s(\delta))\), and \((2d)^{-1}=(2s)^{-1}+O_s(\delta)\). Multiplication proves the stated \(o(1)\) asymptotic, including the exact constant inside the logarithm.

**6. Why modal stability does not rescue positivity.** For any symmetric negative-semidefinite generator with nonzero spectral decay rate \(\mu>0\), the corresponding mode of this map has factor
\[
R(-h\mu)=1-h\mu\exp(-\alpha h\mu).
\]
Since \(0<h\mu\exp(-\alpha h\mu)\leq1/(e\alpha)\), the method is power-bounded in the Euclidean norm at every \(h>0\) for \(\alpha\geq1/(2e)\) (strictly contractive on the orthogonal complement of constants when \(\alpha>1/(2e)\)). This scalar spectral bound is part of the originating literature, not claimed as new. The off-diagonal sign loss proved above persists for every \(\alpha\), including the strictly spectrally stable range.

## Verification

The accompanying standalone `checker.py` reconstructs the method and uses exact rational characteristic-polynomial identities, direct matrix-exponential evaluations, sign tests around the unique crossing, equal-edge threshold tests, and delayed-onset asymptotic checks. It passed 18,052 deterministic check units. The proofs of the all-step quantifiers and asymptotic limit are the analytical arguments above, not the finite tests. A user can run `python checker.py` with Python, NumPy, SciPy, and SymPy installed. No external files are required.

## Relationship to prior work

Caliari–Cassini–Einkemmer–Ostermann introduce stabilized Lawson–Euler and establish \(\alpha\geq1/(2e)\) for unconditional stability of real negative scalar modes. This result explicitly concerns **entrywise positivity of a matrix step**, not eigenvalue stability, and produces a discontinuous sharp criterion under edge heterogeneity. Hu–Shu establish positivity for a **different** exponential Runge–Kutta construction in kinetic models using positivity-preserving subflows and explicit coefficient constraints; it does not identify positivity of this stabilized Lawson–Euler map. Jones–Epstein–García-Mochón present the classical finite-state Markov transition-matrix spectral method, which supplies background, not the numerical-method positivity classification. These distinctions are implication-based; matching exponential/Markov terminology alone does not establish coverage.

## Limitations

This is an exact-arithmetic three-node *symmetric path* theorem, not a classification of all graphs, all generators, all Lawson methods, or every positivity-preserving discretization. For unbalanced paths the explicit time \(t_*\) is the unique sign crossing of the indicated off-diagonal entry; it is **not** asserted to be the first step at which any matrix entry becomes negative, since other entries may fail earlier. The conclusion does not bound the size of the negative entry under floating-point rounding or ensure that finite-step numerical searches detect delayed sign loss. The supporting literature search cannot exclude uncatalogued equivalent results; no independent scientific validation is claimed.

## References

1. M. Caliari, F. Cassini, L. Einkemmer, A. Ostermann, *Accelerating exponential integrators to efficiently solve semilinear advection-diffusion-reaction equations*, arXiv:2303.15861, first submitted 2023-03-28, especially Section 2, equation (4), Theorem 2.3, and the appendix. https://arxiv.org/abs/2303.15861
2. J. Hu and R. Shu, *A second-order asymptotic-preserving and positivity-preserving exponential Runge-Kutta method for a class of stiff kinetic equations*, arXiv:1807.03728, especially Section 2 and Proposition 2.2. https://arxiv.org/abs/1807.03728
3. E. Jones, D. Epstein and L. García-Mochón, *A Procedure for Deriving Formulas to Convert Transition Rates to Probabilities for Multistate Markov Models*, *Medical Decision Making* (2017), DOI:10.1177/0272989X17696997, especially the Kolmogorov and spectral-decomposition sections. https://doi.org/10.1177/0272989X17696997
