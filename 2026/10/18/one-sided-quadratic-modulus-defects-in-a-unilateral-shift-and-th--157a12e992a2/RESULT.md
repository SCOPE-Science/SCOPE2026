# One-sided quadratic modulus defects in a unilateral shift and their finite sections

## Finding
Let \(H\) be a complex Hilbert space and let \(A=A^*\ge aI\), where \(a>0\), and \(B=B^*\) be bounded. Define the two one-sided modulus-order defects, for real \(t\ge0\), by
\[
d_\pm(t)=\bigl\|\bigl(|A\pm itB|-A\bigr)_+\bigr\|.
\]
There is a bounded self-adjoint operator \(L\), determined uniquely by
\[
AL+LA=i[A,B],
\]
such that
\[
d_\pm(t)=t\bigl\|(\pm L)_+\bigr\|+O_{A,B}(t^2)\quad(t\downarrow0).
\]
In finite dimension, if \([A,B]\ne0\), then both linear coefficients are strictly positive. The infinite-dimensional conclusion is sharply different: on \(\ell_2(\mathbb N_0)\) there are explicit bounded self-adjoint \(A\ge I\) and \(B\) with \([A,B]\ne0\), satisfying
\[
3\bigl(\sqrt{1+4t^2}-1\bigr)\le d_+(t)\le C t^2,
\qquad
 d_-(t)=\tfrac12t+O(t^2)
\]
for every sufficiently small \(t\ge0\), with \(C\) independent of \(t\). Consequently the positive direction has exactly quadratic order while the opposite direction has linear order.

Moreover, truncating the unilateral shift in this explicit construction to every \(n\ge2\) gives \(n\)-dimensional pairs \((A_n,B_n)\) for which **both** directions have leading coefficient \(1/2\):
\[
d_{n,+}(t)=\tfrac12t+O_n(t^2),\qquad d_{n,-}(t)=\tfrac12t+O_n(t^2).
\]
Thus the one-sided first-order modulus defect is not preserved by the natural sequence of finite shift sections.

## Assumptions and scope
The modulus of a bounded operator is \(|T|=(T^*T)^{1/2}\). For self-adjoint \(D\), \(D_+\) denotes its positive part; \(\|D_+\|=\max\{0,\sup\sigma(D)\}\). All statements concern complex Hilbert spaces, bounded operators, and the operator norm. The symbol \(O_{A,B}(t^2)\) means a norm bound with a constant depending on the fixed operators; no dimension-free uniform estimate for the finite sections is claimed.

For the explicit example, let \(S\) be the unilateral forward shift \(Se_j=e_{j+1}\) on \(\ell_2(\mathbb N_0)\), let \(P_0\) be the orthogonal projection onto \(\mathbb C e_0\), and put
\[
A=2I+\frac{S+S^*}{2},\qquad
Y=\frac{S-S^*}{2i},\qquad
X=I-Y,\qquad
B=AX+XA.
\]
Here \(A=A^*\ge I\), \(X=X^*\), \(B=B^*\), and \(\|A\|=3\). For a finite section of length \(n\), replace \(S\) by the nilpotent forward shift \(S_n\) on \(\mathbb C^n\) throughout.

## Proof
**First variation.** The positive operator \(A^2\) has spectrum in \([a^2,\|A\|^2]\). In operator norm, the holomorphic functional calculus for the principal square root in a neighborhood of this spectrum gives
\[
|A+itB|=\bigl(A^2+it[A,B]+t^2B^2\bigr)^{1/2}
=A+tL+O_{A,B}(t^2).
\]
Differentiating the square-root identity and equating terms of order \(t\) gives \(AL+LA=i[A,B]\). Since \(A\ge aI\), the map \(D\mapsto AD+DA\) is invertible on bounded operators, with inverse
\[
D\longmapsto\int_0^\infty e^{-sA}D e^{-sA}\,ds.
\]
In particular, if
\[
X_0=\int_0^\infty e^{-sA}B e^{-sA}\,ds,
\]
then \(AX_0+X_0A=B\) and \(L=i[A,X_0]\). This is self-adjoint. The elementary spectral identity for the positive-part norm and the inequality \(|\sup\sigma(D)-\sup\sigma(E)|\le\|D-E\|\) for self-adjoint \(D,E\) yield
\[
\big|\|(D)_+\|-\|(E)_+\|\big|\le\|D-E\|.
\]
Taking \(D=|A\pm itB|-A\) and \(E=\pm tL\) proves the stated one-sided expansions.

**Finite-dimensional obstruction.** In a finite-dimensional Hilbert space, \(\operatorname{tr}L=i\operatorname{tr}[A,X_0]=0\). The Sylvester equation implies \(L=0\) exactly when \([A,B]=0\). Thus if \([A,B]\ne0\), the nonzero traceless self-adjoint \(L\) has both a strictly positive and a strictly negative eigenvalue; hence \(\|L_+\|>0\) and \(\|(-L)_+\|>0\).

**One-sided infinite-dimensional witness.** For the specified unilateral shift, \([S,S^*]=-P_0\), so direct commutator calculation gives
\[
i[A,Y]=\frac12P_0,\qquad
L=i[A,X]=-\frac12P_0.
\]
Because \(B=AX+XA\), uniqueness in the Sylvester equation shows that this \(X\) equals \(X_0\) in the first-variation formula. Therefore
\[
d_+(t)=O(t^2),\qquad d_-(t)=\tfrac12t+O(t^2).
\]
The pair is noncommuting: \(i[A,B]=AL+LA=-(AP_0+P_0A)/2\ne0\).

To establish a matching *positive* quadratic lower bound, choose unit vectors
\[
v_N=N^{-1/2}\sum_{j=0}^{N-1}e_j.
\]
The shift and its adjoint satisfy \(\|(S-I)v_N\|\to0\) and \(\|(S^*-I)v_N\|\to0\). Hence \(\|(A-3I)v_N\|\to0\), \(\|(X-I)v_N\|\to0\), and \(\|(B-6I)v_N\|\to0\). It follows for each fixed \(t\ge0\) that
\[
\|A+itB\|\ge\lim_{N\to\infty}\|(A+itB)v_N\|
=3\sqrt{1+4t^2}.
\]
By definition of \(d_+(t)\), the operator-order inequality \(|A+itB|\le A+d_+(t)I\) holds, so
\[
\|A+itB\|=\||A+itB|\|\le\|A\|+d_+(t)=3+d_+(t).
\]
The two inequalities give \(d_+(t)\ge3(\sqrt{1+4t^2}-1)=6t^2+O(t^4)\). Combined with the first variation, this proves \(d_+(t)=\Theta(t^2)\). In particular \(\liminf_{t\downarrow0}d_+(t)/t^2\ge6\); no exact quadratic coefficient is asserted.

**Every finite shift section.** For \(n\ge2\), \([S_n,S_n^*]=-P_0+P_{n-1}\), where \(P_{n-1}\) is the projection onto the last coordinate. The same commutator identity gives
\[
L_n=i[A_n,X_n]=\tfrac12(P_{n-1}-P_0).
\]
This has eigenvalues \(1/2\) and \(-1/2\), and possibly zero eigenvalues. The finite-dimensional first-variation formula therefore gives both asserted expansions for every fixed \(n\ge2\). No interchange of \(n\to\infty\) with \(t\downarrow0\) is used.

## Verification
The critical infinite-dimensional identities are verified directly using \(SS^*=I-P_0\) and \(S^*S=I\), and the lower bound uses explicit approximate joint eigenvectors rather than finite-size extrapolation. The holomorphic square-root expansion applies because \(A\ge I\), so its spectrum stays away from zero. All finite-dimensional statements follow from the exact rank-two endpoint commutator.

The standalone `verify.py` executes exact dyadic complex-arithmetic checks for the commutator, self-adjointness, and Sylvester equation on 79 finite sections of sizes 2 through 80. Its output is diagnostic only: finite computation is not a proof of an infinite-dimensional claim or of convergence rates.

## Relationship to prior work
Ma's *A General Proof of the Fong–Tsui Conjecture* (September 9, 2026, arXiv:2609.10797v1), particularly its quantitative stability discussion, studies the defect \(|T|\le|\operatorname{Re}T|+\varepsilon I\) and general \(\varepsilon^{1/8}\)-scale estimates. Aouichaoui, Kittaneh, and Ma's September 14, 2026 proof (arXiv:2609.16236v1) settles the exact zero-defect implication. The present contribution concerns first-order **one-sided** asymmetry for a nonnormal perturbation and a finite-versus-infinite distinction; it does not improve their general uniform stability bound or challenge the exact zero-defect theorem.

The earlier published sharp normal-operator stability result (October 4, 2026) treats commuting Cartesian parts, unlike the present noncommuting pair. The published flat-modulus-real-part result (October 11, 2026) treats real parts \(A\) with \(|A|=\|A\|P\), whereas the concrete \(A=2I+(S+S^*)/2\) has nontrivial spectral interval \([1,3]\). Neither theorem implies one-sided quadratic order or the finite-section discontinuity. The Sylvester derivative formula is a standard operator-calculus ingredient, not independently claimed as new.

## Limitations
This is a single explicit nonnormal family, not a classification of all positive real parts or a sharp general perturbation theorem. The proof gives the exact order of the positive-direction defect but only a lower bound for its normalized quadratic coefficient. The finite-section remainder constants may depend on dimension. The possibility that equivalent unilateral-shift and modulus-derivative examples exist under other terminology in earlier operator-perturbation literature remains a publication-priority risk. No independent mathematical audit has been performed.

## References
1. Y. Ma, *A General Proof of the Fong–Tsui Conjecture*, arXiv:2609.10797v1 (first posted September 9, 2026), especially Sections 4–5. https://arxiv.org/abs/2609.10797
2. M. A. Aouichaoui, F. Kittaneh, Y. Ma, *A proof of the Fong–Tsui conjecture*, arXiv:2609.16236v1 (first posted September 14, 2026), MSC2020 47B15. https://arxiv.org/abs/2609.16236
3. *Sharp normal-operator stability for the approximate Fong–Tsui inequality*, published mathematical result (October 4, 2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-normal-operator-stability-for-the-approximate-fong-tsui-in--969c2f6b34c4
4. *Sharp square-root Fong–Tsui stability for flat-modulus real parts*, published mathematical result (October 11, 2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-square-root-fong-tsui-stability-for-flat-modulus-real-part--a4e9e3cc0326
