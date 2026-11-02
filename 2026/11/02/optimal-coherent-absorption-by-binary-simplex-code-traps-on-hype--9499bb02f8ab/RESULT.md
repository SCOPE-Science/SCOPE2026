# Optimal coherent absorption by binary simplex-code traps on hypercubes

## Finding

Let \(m\ge3\), \(N=2^m-1\), and let \(Q_N\) denote the graph on \(\mathbb F_2^N\) in which two words are adjacent when their Hamming distance equals one. We consider continuous-time one-particle dynamics with uniform hopping and absorbing sites:
\[
H_{\mathrm{eff}}=J A_{Q_N}-i\Gamma,\qquad
\Gamma=\sum_{x\in T}\gamma_x|x\rangle\langle x|,
\qquad J>0,\quad\gamma_x>0.
\]
The absorber set \(T\) is an arbitrary affine binary subspace of dimension \(m\), hence it contains exactly \(2^m=N+1\) sites. Let \(\mathcal E_w\) be the adjacency eigenspace of energy \(J(N-2w)\), and let \(r_w(T)\) be the rank of the restriction map from \(\mathcal E_w\) to functions on \(T\). Define the bright dimension \(B(T)=\sum_{w=0}^N r_w(T)\). The orthogonal complement of the bright subspace is the space of modes that never lose norm.

**Sharp universal optimum.** Every such affine absorber set satisfies
\[
 B(T)\le N^2-3.
\]
Equality is attained by the binary simplex-code set
\[
T_* = \left\{\big(t\cdot a\big)_{a\in\mathbb F_2^m\setminus\{0\}}:
 t\in\mathbb F_2^m\right\},
\]
where all products are over \(\mathbb F_2\). Its complete energy-resolved bright profile is
\[
 r_w(T_*)=
 \begin{cases}
  1,&w\in\{0,N\},\\
  N,&w\in\{1,2,N-2,N-1\},\\
  N+1,&3\le w\le N-3.
 \end{cases}
\]
Consequently its dark dimension is \(2^N-N^2+3\). For a maximally mixed initial one-particle state, its eventual absorbed fraction is \((N^2-3)/2^N\). The statements are invariant under translating \(T_*\) and under arbitrary choices of the strictly positive individual loss rates. In particular, at \(m=3\) there are \(46\) bright and \(82\) dark dimensions on the 128-site hypercube; at \(m=4\) the respective dimensions are \(222\) and \(32546\).

## Assumptions and scope

All arithmetic defining \(Q_N\), the affine code, coordinate characters, and subset sums takes place over \(\mathbb F_2\). Spectral matrix ranks are ordinary ranks over \(\mathbb C\). The statement concerns finite-dimensional continuous-time single-particle dynamics for the non-Hermitian generator \(H_{\mathrm{eff}}\). All absorber rates are strictly positive and no other disorder or dephasing is present. The total capture probability is defined as initial trace minus surviving trace in the limit of infinite time; it equals the bright-space weight, not a claim about finite-time speed.

## Proof

**1. Fourier reduction.** The Walsh characters \(\chi_u(x)=(-1)^{u\cdot x}\) for \(u\in\mathbb F_2^N\) diagonalize the hypercube adjacency operator: \(A_{Q_N}\chi_u=(N-2|u|)\chi_u\). Thus \(\mathcal E_w\) is spanned by exactly the characters of Hamming weight \(w\). Parametrize an arbitrary affine \(m\)-subspace as \(x=x_0+(t\cdot a_i)_{i=1}^N\), with \(t\in\mathbb F_2^m\), where the generator columns \(a_1,\ldots,a_N\) span \(\mathbb F_2^m\). Restricting \(\chi_u\) to this subspace yields the nonzero scalar factor \((-1)^{u\cdot x_0}\) times the parameter character \((-1)^{t\cdot\sum_{i:u_i=1}a_i}\). Distinct parameter characters are linearly independent. Therefore
\[
 r_w(T)=\left|\left\{\sum_{i\in I}a_i:\ I\subseteq\{1,\ldots,N\},\ |I|=w\right\}\right|.
\]
Complements of subsets translate all these syndromes by the fixed sum \(\sum_i a_i\), so \(r_{N-w}(T)=r_w(T)\). Also \(r_0=r_N=1\), \(r_1\le N\), and all \(r_w\le N+1\).

**2. A universal upper bound.** If \(r_1\le N-1\), then by complement symmetry
\[
 B(T)\le2+2(N-1)+(N-3)(N+1)=N^2-3.
\]
If instead \(r_1=N\), all the \(N\) columns \(a_i\) are distinct. In characteristic two, the XOR of two distinct columns cannot be zero, so \(r_2\le N\); the same holds at weight \(N-2\). Hence
\[
 B(T)\le2+4N+(N-5)(N+1)=N^2-3.
\]
Both estimates hold for every \(N=2^m-1\ge7\), independently of any minimum-distance assumption on the absorber code.

**3. Sharpness in the endpoint shells.** For \(T_*\), the columns are exactly the \(N\) distinct nonzero vectors of \(\mathbb F_2^m\). Thus \(r_1=N\). Every nonzero vector is an XOR of two distinct nonzero vectors (choose any nonzero vector different from it), and a pair of distinct vectors never XORs to zero. Therefore \(r_2=N\). Complement symmetry gives \(r_{N-1}=r_{N-2}=N\), while \(r_0=r_N=1\).

**4. Full rank in every interior shell.** Write \(L=2^{m-1}\), so \(N=2L-1\) and \(|T_*|=2L\). Two distinct simplex codewords differ in exactly \(L\) positions: each nonzero linear functional on \(\mathbb F_2^m\) equals one at precisely half the input vectors. For \(0\le w\le N\), let \(M_w\) be the matrix whose rows are the \(2L\) trap words and whose columns are the \(\binom Nw\) weight-\(w\) Walsh characters evaluated on those words. The diagonal entries of \(M_wM_w^{\mathsf T}\) are \(c=\binom Nw\), and all off-diagonal entries equal
\[
 b_w=[z^w](1-z)^L(1+z)^{L-1}
     =[z^w](1-z)(1-z^2)^{L-1}.
\]
Consequently \(|b_w|=\binom{L-1}{\lfloor w/2\rfloor}\), and the Gram matrix has precisely two eigenvalues,
\[
 \lambda_{\mathrm{constant}}=c+Nb_w\quad(\text{multiplicity }1),
 \qquad \lambda_{\mathrm{orthogonal}}=c-b_w\quad(\text{multiplicity }N).
\]
We show both are positive for \(3\le w\le N-3\). For odd \(w=2j+1\), the ratio
\[
 R_{\mathrm{odd}}(j)=\frac{\binom{N}{2j+1}}{\binom{L-1}{j}}
\]
has successive ratio \(R_{\mathrm{odd}}(j+1)/R_{\mathrm{odd}}(j)=(2(L-j)-3)/(2j+3)\). For even \(w=2j\), the analogous ratio satisfies
\[
 \frac{R_{\mathrm{even}}(j+1)}{R_{\mathrm{even}}(j)}=
 \frac{2(L-j)-1}{2j+1}.
\]
Both successive ratios decrease strictly with \(j\), so each finite sequence first increases and then decreases, and its minimum lies at an endpoint. The endpoint values on the relevant ranges \(3\le w\le N-3\) are all \(N(N-2)/3\): for example, at weight three the ratio is \(\binom N3/(L-1)=N(N-2)/3\), and at weight four it is \(\binom N4/\binom{L-1}2=N(N-2)/3\); opposite endpoints follow by complement symmetry. Since \(N\ge7\), this common lower bound exceeds \(N\). We obtain \(c>N|b_w|\) throughout the interior, so the two Gram eigenvalues are strictly positive and \(r_w(T_*)=\operatorname{rank}(M_w)=N+1\). Combining all weights gives
\[
 B(T_*)=2+4N+(N-5)(N+1)=N^2-3.
\]

**5. Relating bright rank to absorption.** Let \(\mathcal D=\bigoplus_w\{\psi\in\mathcal E_w:\psi|_T=0\}\). Every \(\psi\in\mathcal D\) is an adjacency eigenmode annihilated by \(\Gamma\); therefore \(\mathcal D\) is invariant under \(H_{\mathrm{eff}}\) and its adjoint. Its orthogonal complement is invariant as well. The loss identity
\[
\frac{d}{dt}\|\psi(t)\|^2=-2\langle\psi(t),\Gamma\psi(t)\rangle\le0
\]
shows that a nondecaying eigenmode must lie in \(\ker\Gamma\), hence in an adjacency eigenspace of \(A_{Q_N}\) that vanishes on \(T\); on the orthogonal complement of \(\mathcal D\), all eigenvalues have strictly negative dissipative imaginary part. Finite dimensionality makes that complementary semigroup decay to zero. Thus \(\dim\mathcal D=\sum_w(\dim\mathcal E_w-r_w)=2^N-B(T)\). Starting from \(I/2^N\), the surviving trace tends to \(\dim\mathcal D/2^N\), giving the capture formula. The proof uses only \(\gamma_x>0\), explaining the claimed rate independence.

## Verification

The self-contained file `verification/verify_simplex_absorption.py` implements exact subset-XOR shell-rank enumeration, independent modular Fourier-matrix ranks, Gram eigenvalue checks, a complete 2696-instance full-rank generator-multiset census at \(m=3\), 400 deterministic random full-rank generator checks at \(m=4\), and an independent 128-site Krylov calculation. Running `python3 verification/verify_simplex_absorption.py` prints `VERIFY_OK` together with the check counts. The modular calculations use the prime \(2^{61}-1\); the Hadamard bound for the Fourier minors (at most sixteen rows) is strictly smaller than this prime, so their modular ranks equal rational ranks. For the Krylov test the independently proved upper bound and a modular lower bound coincide. These finite tests support, but do not replace, the general proof above.

## Relationship to prior work

Moore and Russell analyze hypercube quantum-walk dynamics without structured many-site absorption. Krovi and Brun and Varbanov, Krovi, and Brun establish dark-mode and hitting-time frameworks. Krapivsky, Luck, and Mallick study survival under non-Hermitian traps, including periodic and disordered systems, but their inspected setting does not provide this affine-code maximal-capture result. The Fourier-shell structure and linear-code encoding are classical tools; the mathematical claim here is the sharp optimum over all affine \(m\)-dimensional trap subspaces together with the complete simplex-trap energy-shell rank profile and resulting physical absorption law. Specialized older coding-theoretic observability or trap literature may contain a prior equivalent statement; no absolute novelty is asserted.

## Limitations

The bound is optimized only over affine binary subspaces of dimension \(m\), not over all unconstrained sets of \(2^m\) trap vertices. It concerns one-particle, uniform-hopping, zero-dephasing dynamics with all traps strictly active, not absorption rates, first-passage time, disordered transport, general nonlinear loss, or many-particle dynamics. Maximizing eventual capture does not imply maximizing its speed. We do not classify all equality cases.

## References

1. C. Moore and A. Russell, *Quantum Walks on the Hypercube* (2001), [arXiv:quant-ph/0104137](https://arxiv.org/abs/quant-ph/0104137), original public version 2001-04-29.
2. H. Krovi and T. A. Brun, *Quantum walks with infinite hitting times* (2006), [arXiv:quant-ph/0606094](https://arxiv.org/abs/quant-ph/0606094).
3. M. Varbanov, H. Krovi and T. A. Brun, *Hitting time for the continuous quantum walk* (2008), [arXiv:0803.3446](https://arxiv.org/abs/0803.3446).
4. P. L. Krapivsky, J. M. Luck and K. Mallick, *Survival of classical and quantum particles in the presence of traps* (2013), [arXiv:1311.6298](https://arxiv.org/abs/1311.6298).
5. A. Makmal and collaborators, *Quantum walks on embedded hypercubes* (2015), [arXiv:1510.08388](https://arxiv.org/abs/1510.08388).
