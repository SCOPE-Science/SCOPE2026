# Four-level three-cycle sampling spectrum for the symmetric-group standard Fourier block

## Finding

Let \(n\ge4\), let \(G=S_n\), and equip \(\ell^2(G)\) with normalized counting measure. Write \(V=\{z\in\mathbb C^n:\sum_i z_i=0\}\) for the standard representation, and let \(H\subset\ell^2(G)\) be its complete matrix-coefficient Fourier block (dimension \((n-1)^2\)). Let \(P\) denote the orthogonal projection onto \(H\), and let \(T_n\) be the conjugacy class of all three-cycles. The concentration operator \(C_n=PM_{\mathbf1_{T_n}}P\vert_H\) has the following exact eigenvalue/multiplicity pairs:

\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
\frac{n-1}{n!}\frac{n(n-2)(n-4)^2}{3}&1\\
\frac{n-1}{n!}n(n-3)&n-1\\
\frac{n-1}{n!}(n-4)&\frac{n(n-3)}2\\
\frac{n-1}{n!}n&\frac{(n-1)(n-2)}2
\end{array}
\]

Zero eigenvalues and coincident levels are retained and multiplicities are combined. For \(n=4\), the concentration operator has rank \(6\) and spectrum \(\{(1/2)^{[6]},0^{[3]}\}\); for every \(n\ge5\), it is positive definite on \(H\). Thus every function in \(H\) is uniquely determined by its values on *all* three-cycles if and only if \(n\ge5\). For \(n\ge6\), the sampling analysis operator (with its natural normalized group norm) has sharp condition number
\[
\kappa_n=\sqrt{\frac{n(n-2)(n-4)}3}.
\]
This condition number is the ratio of largest to smallest nonzero singular values of restriction to the three-cycle class; at \(n\ge5\) all singular values on \(H\) are nonzero.

## Assumptions and scope

All statements concern ordinary complex-valued functions and the *complete* standard-representation Fourier block; this is not the space of class functions and is not the space of the standard representation itself. The normalized inner product is \(\langle f,g\rangle_G=(n!)^{-1}\sum_{h\in S_n}f(h)\overline{g(h)}\). The indicator multiplier is \(M_{\mathbf1_{T_n}}f=\mathbf1_{T_n}f\), so \(0\le C_n\le I_H\). The symmetric-group action in the proof is by conjugation on endomorphisms; brackets \([\lambda]\) denote the complex Specht module of partition \(\lambda\). No character normalization other than the standard normalized group measure is implicit.

## Proof

**1. Fourier coefficient model.** Let \(\rho\) be the real orthogonal standard representation of degree \(d=n-1\). The matrix-coefficient map from the Hilbert--Schmidt space \(\operatorname{End}(V)\) to \(H\), \(X\mapsto f_X\) defined by \(f_X(g)=\sqrt d\,\operatorname{tr}(X^{\mathsf T}\rho(g))\), is unitary by Schur orthogonality, after complex-linear extension from real matrices. The restriction operator has Gram/frame operator on \(\operatorname{End}(V)\)
\[
\mathcal F=\frac{d}{n!}\sum_{g\in T_n}|\rho(g)\rangle\langle\rho(g)|,
\]
where \(|R\rangle\langle R|\) means \(X\mapsto\langle X,R\rangle_{\rm HS}R\). Thus it suffices to determine its eigenvalues.

**2. Multiplicity-free conjugation action.** Under \(X\mapsto\rho(h)X\rho(h)^{-1}\), the endomorphism space decomposes orthogonally as
\[
\operatorname{End}(V)=[n]\oplus[n-1,1]\oplus[n-2,2]\oplus[n-2,1,1],
\]
with dimensions respectively \(1\), \(n-1\), \(n(n-3)/2\), and \((n-1)(n-2)/2\). The first three summands comprise \(\operatorname{Sym}^2(V)\), whereas the fourth equals \(\bigwedge^2(V)\). The decomposition is valid also for \(n=4\), where the four partitions remain distinct. By conjugation invariance and Schur's lemma, \(\mathcal F\) is scalar on each summand.

**3. Geometry of one three-cycle.** Fix a cycle supported on a vertex triple \(U\). Let \(J\) be the all-ones matrix and \(Q=I-J/n\), the projector of \(\mathbb R^n\) onto \(V\). Let \(L_U\) be the Laplacian of the triangle on \(U\), extended by zero outside \(U\). Define \(S=(\rho(g)+\rho(g)^{-1})/2\) and \(A=(\rho(g)-\rho(g)^{-1})/2\). As operators on \(V\), \(S=Q-\tfrac12L_U\), and \(A\) is skew-symmetric. The Laplacian has two nonzero eigenvalues, each equal to \(3\), whence
\[
\operatorname{tr}S=n-4,\qquad\|S\|_{\rm HS}^2=n-\tfrac52,\qquad\|A\|_{\rm HS}^2=\tfrac32.
\]
The orthogonal projection of \(S\) onto the scalar endomorphisms is \((n-4)I_V/(n-1)\), with squared norm \((n-4)^2/(n-1)\).

**4. Standard and second-row projections.** Set \(q_i=Qe_i\) and \(F_i=q_iq_i^{\mathsf T}\). The span of \(\{F_i\}\) consists exactly of the scalar and standard summands of \(\operatorname{Sym}^2(V)\): the Gram matrix \(\langle F_i,F_j\rangle\) is \((n-2)I/n+J/n^2\), so its eigenvalue on zero-sum coefficient vectors is \((n-2)/n\). Moreover, \(\langle S,F_i\rangle=-1/n\) for \(i\in U\) and \((n-1)/n\) otherwise. Centering yields a vector with entries \(3/n-\mathbf1_U(i)\) and squared norm \(3(n-3)/n\). Therefore the standard-sector squared projection is
\[
\|\operatorname{proj}_{[n-1,1]}S\|_{\rm HS}^2=\frac{3(n-3)}{n-2}.
\]
Subtracting this and the scalar-sector norm from \(\|S\|_{\rm HS}^2\) gives
\[
\|\operatorname{proj}_{[n-2,2]}S\|_{\rm HS}^2=\frac{3(n-4)(n-3)}{2(n-2)(n-1)}.
\]
The antisymmetric vector \(A\) is entirely in \([n-2,1,1]\), with squared norm \(3/2\).

**5. Conjugacy averaging.** The class \(T_n\) contains \(m=n(n-1)(n-2)/3\) elements, with each oriented three-cycle paired with its inverse. Since \(\rho(g)=S+A\) and \(\rho(g^{-1})=S-A\), the sum of their outer products is twice the sum of the separate symmetric and skew outer products. For a multiplicity-one irreducible conjugation summand \(W\) of dimension \(d_W\), Schur averaging gives \(m\|\operatorname{proj}_W S\|^2/d_W\), or \(m\|\operatorname{proj}_W A\|^2/d_W\) on the skew summand, as its eigenvalue in the *unscaled* Gram operator. The values for the four summands are, in order,
\[
\frac{n(n-2)(n-4)^2}{3},\quad n(n-3),\quad n-4,\quad n.
\]
Multiplication by the Schur-orthogonality factor \((n-1)/n!\) proves the announced spectrum.

**6. Boundaries and conditioning.** At \(n=4\) exactly the first and third sectors vanish, of total multiplicity \(1+2=3\), while the other two each have eigenvalue \(1/2\). At \(n\ge5\) every listed raw value is positive. For \(n\ge6\), the largest raw value is \(n(n-2)(n-4)^2/3\), the smallest is \(n-4\), and their ratio gives the square of the optimal sampling condition number. Coincident levels at \(n=5\) cause no rank loss.

## Verification

The accompanying standalone Python checker `verify.py` uses only the standard library. Run `python3 verify.py` after extraction. It forms the exact integer Gram matrix of all oriented three-cycle matrices in the standard representation, with entries \(\#\operatorname{Fix}(g^{-1}h)-1\); checks its first four power traces against the proposed eigenvalue/multiplicity formula; and verifies that the matrix is annihilated by the product of all predicted distinct linear spectral factors. All checks succeeded for \(4\le n\le8\), encompassing the singular boundary and the coincident-level case. This finite computation is corroboration, not an exhaustive proof beyond this range; steps 1--6 are the all-parameter proof.

## Relationship to prior work

Scarabotti and Tolli (2007, arXiv:math/0701533) develop harmonic analysis on finite homogeneous spaces and explicitly decompose permutation modules of ordered pairs into relevant Specht components. Their construction supplies useful representation-theoretic context but does not give this complete-matrix-coefficient, three-cycle-restriction concentration spectrum. Thill and Hassibi (2015, arXiv:1509.05739) analyze group Fourier frames, group-theoretic coherence, and sampling from conjugacy-dependent selections. Their frame results do not state the four exact symmetric-group eigenvalues or the sharp all-three-cycle recovery threshold. The universal Schur-orthogonality and conjugacy-averaging ingredients are classical; the asserted result is their explicit combination for the specific conjugacy-class sampling problem, including the sharp rank boundary and conditioning law.

## Limitations

This theorem is specific to the full standard Fourier block of \(S_n\), to the complete three-cycle conjugacy class, and to normalized \(\ell^2\) concentration. It does not determine optimal sampling by proper subsets of the class, restricted isotypic sums, or conditioning with noisy or weighted nonuniform samples. An equivalent formula could occur in older conjugation association-scheme or matrix-frame literature; absence from the inspected sources alone cannot establish worldwide priority. No independent mathematical audit has been performed.

## References

- F. Scarabotti and F. Tolli, *Harmonic analysis on a finite homogeneous space*, arXiv:math/0701533, first publicly submitted 19 January 2007.
- M. Thill and B. Hassibi, *Low-Coherence Frames from Group Fourier Matrices*, arXiv:1509.05739, first publicly submitted 18 September 2015.
