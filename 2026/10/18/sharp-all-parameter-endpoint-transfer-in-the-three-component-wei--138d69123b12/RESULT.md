# Sharp all-parameter endpoint transfer in the three-component weighted wave reduction

## Finding

**Theorem (sharp transfer envelope and arithmetic resonance for every positive three-site chain).** Given any three positive masses \(m_1,m_2,m_3\), two positive couplings \(k_1,k_2\), and the weighted three-vertex path Laplacian \(H=M^{-1/2}KM^{-1/2}\) defined below, the entire end-to-end wave response \(F(t)=|[\cos(t\sqrt H)]_{31}|^2\) admits an explicit three-mode expression and a sharp all-parameter supremum classification. For an irrational ratio of its two nonzero normal-mode frequencies, the sharp supremum equals an explicit asymmetry ceiling \(C^2\). For a rational frequency ratio \(p/q\) in lowest terms, the same ceiling is attained if and only if \(p\) is even and \(q\) odd; in every other rational case the strictly smaller exact maximum is the maximum of an explicit finite Chebyshev polynomial on \([-1,1]\). The ceiling equals one if and only if both endpoint masses and both couplings match. The infinite-time transfer optimum is therefore discontinuous at the rational frequencies with incompatible parity, despite continuous response at each fixed time.

The arithmetic conditions for exact *perfect* transmission of mirror-symmetric chains are established in earlier work (Vaia 2020) and are not claimed to be new. The assessed addition here is the quantitative optimal transfer law for **arbitrary asymmetric** masses and couplings, together with its exact resonant suppression and finite algebraic optimization.

## Assumptions and scope

Fix arbitrary real \(m_1,m_2,m_3,k_1,k_2>0\). Let \(M=\operatorname{diag}(m_1,m_2,m_3)\), and let the matrix \(K\) be the three-vertex weighted path Laplacian
\[
K=\begin{pmatrix} k_1&-k_1&0\\-k_1&k_1+k_2&-k_2\\0&-k_2&k_2\end{pmatrix},\qquad H=M^{-1/2}KM^{-1/2}.
\]
The response \(A(t)=[\cos(t\sqrt H)]_{31}\) and \(F(t)=A(t)^2\), \(t\ge0\), refer to **mass-normalized** endpoint coordinates. They are not the unnormalized displacement response for unequal endpoint masses. Set
\[
S=k_1(1/m_1+1/m_2)+k_2(1/m_2+1/m_3),\quad P=\frac{k_1k_2(m_1+m_2+m_3)}{m_1m_2m_3},\quad\Delta=\sqrt{S^2-4P}.
\]
The two positive eigenvalues are \(\lambda_-=(S-\Delta)/2\), \(\lambda_+=(S+\Delta)/2\), with \(0<\lambda_-<\lambda_+\). Define
\[
B=\frac{k_1k_2}{m_2\sqrt{m_1m_3}},\quad c_0=\frac{B}{\lambda_-\lambda_+}=\frac{\sqrt{m_1m_3}}{m_1+m_2+m_3},\quad c_-=-\frac{B}{\lambda_-\Delta},\quad c_+=\frac{B}{\lambda_+\Delta}.
\]
Then \(c_0>0,c_-<0,c_+>0\), \(c_0+c_-+c_+=0\). Let \(\omega_\pm=\sqrt{\lambda_\pm}\), \(R=\omega_+/\omega_->1\), and
\[
C=2|c_-|=\frac{2B}{\lambda_-\Delta}\in(0,1].
\]
**Exact classification.** For every \(t\ge0\),
\[
A(t)=c_0+c_-\cos(\omega_-t)+c_+\cos(\omega_+t),\qquad F(t)\le C^2.
\]
If \(R\notin\mathbb Q\), \(\sup_{t\ge0}F(t)=C^2\), but the supremum is not attained. If \(R=p/q\in\mathbb Q\) in lowest terms (\(p>q\ge1\)),
\[
\max_{t\ge0}F(t)=\max_{-1\le x\le1}\bigl(c_0+c_-T_q(x)+c_+T_p(x)\bigr)^2,
\]
where \(T_j(\cos\theta)=\cos(j\theta)\). The right-hand side can be evaluated exactly by taking \(x=\pm1\) and the real interior zeros of the derivative polynomial. It equals \(C^2\) if and only if \(p\) is even and \(q\) odd. Otherwise it is strictly less than \(C^2\). For compatible parity the first positive time reaching \(C\) is \(t=q\pi/\omega_-\).

Finally, \(C=1\) exactly when \(m_1=m_3\) and \(k_1=k_2\). In that symmetric case \(R=\sqrt{1+2m_1/m_2}\). Thus perfect transfer at some finite time occurs precisely at an even/odd reduced rational \(R\), and the supremum is one also for irrational \(R\); the latter gives arbitrarily accurate but never exact transfer. The statements about exact perfect transfer are included for orientation and overlap control, not as a separate original contribution.

## Proof

**1. Eigenvalues and projectors.** The matrix \(H\) is a real symmetric, positive semidefinite, irreducible tridiagonal Jacobi matrix with one zero eigenvalue, and therefore has three simple eigenvalues. Its characteristic polynomial is \(z(z^2-Sz+P)\). The product \(P\) follows either from the two-by-two principal minors or from the matrix-tree identity for a weighted path. Distinctness proves \(\Delta>0\).

Write \(E_0,E_-,E_+\) for the three orthogonal spectral projectors and \(c_j=(E_j)_{31}\). The normalized zero eigenvector is \(M^{1/2}(1,1,1)^T/\sqrt{m_1+m_2+m_3}\), hence \(c_0=\sqrt{m_1m_3}/(m_1+m_2+m_3)\). Since \(H_{31}=0\) and \((H^2)_{31}=B\), the spectral decomposition gives \(c_0+c_-+c_+=0\), \(\lambda_-c_-+\lambda_+c_+=0\), and \(\lambda_-^2c_-+\lambda_+^2c_+=B\). Solving gives the stated \(c_-,c_+\). Applying the continuous functional calculus gives the exact cosine response formula.

**2. Universal sharp envelope.** Because \(c_-=-(c_0+c_+)\), independent variation of the two cosine arguments over the square \([-1,1]^2\) would make \(A\) range from \(-2c_+\) to \(2(c_0+c_+)=2|c_-|=C\). The strict inequality \(2c_+<C\) follows from \(c_0>0\). Consequently \(|A(t)|\le C\), and equality can occur only if \(\cos(\omega_-t)=-1\) and \(\cos(\omega_+t)=1\). In particular, \(F(t)=C^2\) has precisely these phase requirements.

For a unit real eigenvector \(v_-\) of \(\lambda_-\), \(|c_-|=|v_{-,1}v_{-,3}|\le(v_{-,1}^2+v_{-,3}^2)/2\le1/2\). Hence \(C\le1\). Equality forces \(v_{-,2}=0\) and \(v_{-,1}=-v_{-,3}\), since the spectral sign is negative. The first and third row equations then require \(k_1/m_1=k_2/m_3\), while the middle row requires \(k_1/\sqrt{m_1}=k_2/\sqrt{m_3}\). Their conjunction is equivalent to \(m_1=m_3\), \(k_1=k_2\). Conversely those equalities give normalized antisymmetric eigenvector \((1,0,-1)^T/\sqrt2\), so \(C=1\).

**3. Irrational versus rational frequency ratios.** If \(R\) is irrational, Kronecker's density theorem for the one-parameter flow on the two-dimensional phase torus supplies positive times at which \(\omega_-t\) approaches an odd multiple of \(\pi\) and \(\omega_+t\) approaches an even multiple of \(\pi\) simultaneously. The envelope \(C\) is therefore the supremum. Exact equality would require \(\omega_-t=(2a+1)\pi\) and \(\omega_+t=2b\pi\) for integers \(a,b\); their quotient would be rational, contradiction.

If \(R=p/q\) is reduced rational, write \(\theta=\omega_-t/q\). Then \(A(t)=c_0+c_-\cos(q\theta)+c_+\cos(p\theta)\), a continuous \(2\pi\)-periodic function. With \(x=\cos\theta\), the Chebyshev identity proves the exact polynomial maximization, including the finite endpoint-and-critical-root recipe. To reach the envelope, we need \(q\theta\equiv\pi\pmod{2\pi}\) and \(p\theta\equiv0\pmod{2\pi}\). Equivalently \(\omega_-t/\pi\) must be odd and \((p/q)(\omega_-t/\pi)\) must be even. Coprimality forces \(q\) odd and \(p\) even. For these parities \(t=q\pi/\omega_-\) realizes both phase requirements, and it is the first positive such time. For incompatible parities no equality is possible; continuity and compactness of the phase orbit make the maximum strictly less than \(C^2\).

**4. Symmetric family and concrete arithmetic defect.** With \(m_1=m_3=m\) and \(k_1=k_2=k\), \(\lambda_-=k/m\) and \(\lambda_+=k/m+2k/m_2\); thus \(R=\sqrt{1+2m/m_2}\). For \((m_1,m_2,m_3)=(12,8,12)\), \(k_1=k_2=1\), one has \(R=2\), so \(t=\pi\sqrt{12}\) yields \(F=1\). For \((24,6,24)\), \(R=3\), \(c_0=4/9\), \(c_-=-1/2\), \(c_+=1/18\). With \(x=\cos(t/\sqrt{24})\),
\[
A(t)=\frac49-\frac12x+\frac1{18}(4x^3-3x)=\frac49-\frac23x+\frac29x^3.
\]
Its derivative \((2/3)(x^2-1)\) is nonpositive on \([-1,1]\). The amplitude ranges from zero to \(8/9\), hence its exact squared maximum is \(64/81\), although \(C^2=1\). The choice \((12,12,12)\) has irrational \(R=\sqrt3\), demonstrating supremum one without a finite maximizing time. All three mass triples are even integers and may be realized as internal arc-counts of connected finite graph components; the two bridges each have multiplicity one.

## Verification

The included standalone `check_p3.py` builds the matrix independently of the spectral-projector formula, computes its eigenpairs, and compares the closed expression with directly diagonalized matrix cosines. It checks 2,100 independently randomized endpoint-response comparisons; for nine reduced rational frequency ratios in all parity regimes, it evaluates the exact Chebyshev critical-point maximum; it checks the \(64/81\) and unity examples and constructs explicit high-fidelity irrational approximants. Run `python check_p3.py` with Python 3 and NumPy installed. Numerical checks support the symbolic proof but do not replace the universal argument or the use of Kronecker's theorem.

## Relationship to prior work

Hosaka and Segawa's 2026 *Pulsation of quantum walk on finite graph* (arXiv:2610.07768v1) proves a weak-bridge reduction of discrete Grover walks to a continuous mass-weighted wave equation and analyzes representative reduced graphs. Its reduction is **prior** and is the reason this all-parameter three-component endpoint optimization is natural. Vaia's 2020 *Dispersionless pulse transport in mass-spring chains: All possible perfect Newton's cradles* (arXiv:2008.01685) already establishes mirror symmetry and alternating spectral parity for exact perfect mass-spring transmission. Schérer, Vinet and Zhedanov (arXiv:2110.01042) likewise construct classes of perfect and fractionally reviving chains. None of these observations is presented here as new. The result assessed here is the quantitative *best possible* squared wave response for **every unequal-mass, unequal-coupling** three-site chain, including its generically sharp ceiling and exact parity-obstructed polynomial maximum. Ordinary Hamiltonian transfer governed by \(e^{-itH}\) is a different propagator from \(\cos(t\sqrt H)\); formulas for the former cannot be used as if they were directly the latter.

## Limitations

This is an exact statement about a finite-dimensional continuous-time wave propagator. In the weak-bridge quantum-walk application, the cited asymptotics concern each fixed rescaled time as bridge weight tends to zero. The passage to an unbounded sequence of rescaled times, used to define the irrational supremum here, is **not** uniform in that small coupling parameter. Therefore the theorem by itself establishes neither pretty-good nor perfect transfer in any **fixed finite-weight Grover walk**. The model uses mass-normalized endpoint amplitudes; unequal endpoint physical displacement/momentum efficiencies require their own normalization. Rational extrema are characterized by a polynomial algorithm rather than a single radical formula for every possible numerator \(p\). The result says nothing about damping, disorder, noisy parameter identification, or longer reduced graphs.

## References

1. T. Hosaka and E. Segawa, *Pulsation of quantum walk on finite graph*, arXiv:2610.07768v1, first posted 2026-10-06. https://arxiv.org/abs/2610.07768
2. R. Vaia, *Dispersionless pulse transport in mass-spring chains: All possible perfect Newton's cradles*, arXiv:2008.01685, *Physical Review E* 102 (2020), 023005. https://arxiv.org/abs/2008.01685
3. H. Schérer, L. Vinet and A. Zhedanov, *A classical model for perfect transfer and fractional revival based on q-Racah polynomials*, arXiv:2110.01042. https://arxiv.org/abs/2110.01042
4. T. Hosaka and E. Segawa, *Pulsation of quantum walk between two arbitrary graphs with weakly connected bridge*, arXiv:2511.12872. https://arxiv.org/abs/2511.12872
