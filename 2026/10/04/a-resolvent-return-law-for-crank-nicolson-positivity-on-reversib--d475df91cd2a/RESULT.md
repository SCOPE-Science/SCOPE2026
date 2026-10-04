# A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains
## Finding
Let \(Q\) be the generator of a finite continuous-time Markov chain in row convention:
\[
q_{ij}\ge0\quad(i\ne j),
\qquad
Q\mathbf 1=0.
\]
For a step \(h\ge0\), put \(s=h/2\) and define the Crank–Nicolson transition candidate
\[
C_h
=
(I-sQ)^{-1}(I+sQ).
\]
Also define the backward-Euler resolvent
\[
R_s=(I-sQ)^{-1}.
\]
Then
\[
C_h=2R_s-I.
\]
Because \(I-sQ\) is an \(M\)-matrix, \(R_s\) is entrywise nonnegative, and because \(Q\mathbf 1=0\),
\[
R_s\mathbf 1=\mathbf 1,
\qquad
C_h\mathbf 1=\mathbf 1.
\]
Consequently every off-diagonal entry of \(C_h\) is automatically nonnegative. The complete positivity test is therefore
\[
C_h\ge0
\quad\Longleftrightarrow\quad
(R_s)_{ii}\ge\frac12
\quad\text{for every state }i.
\]
Thus positivity of the whole Crank–Nicolson matrix is controlled exactly by the diagonal return entries of a backward-Euler resolvent.

Now assume the chain is irreducible and reversible with stationary distribution
\[
\pi=(\pi_1,\ldots,\pi_n),
\qquad
\pi_i>0.
\]
Let
\[
D=\operatorname{diag}(\pi),
\qquad
S=D^{1/2}QD^{-1/2}.
\]
Then \(S\) is symmetric. Write the eigenvalues of \(-S\) as
\[
0=\lambda_0<\lambda_1\le\cdots\le\lambda_{n-1}
\]
and choose an orthonormal eigenbasis \(u_0,\ldots,u_{n-1}\) with
\[
u_{0,i}=\sqrt{\pi_i}.
\]
For every state \(i\),
\[
(R_s)_{ii}
=
\pi_i+
\sum_{k=1}^{n-1}
\frac{u_{k,i}^2}{1+s\lambda_k}.
\]
This function is strictly decreasing in \(s\) whenever \(n>1\), from \(1\) to \(\pi_i\).

Hence, for each state with \(\pi_i<1/2\), there is a unique number \(s_i>0\) determined by
\[
\pi_i+
\sum_{k=1}^{n-1}
\frac{u_{k,i}^2}{1+s_i\lambda_k}
=
\frac12.
\]
States with \(\pi_i\ge1/2\) never create a finite positivity obstruction. Therefore the exact reversible-chain threshold is
\[
h_*=
2\min_{\{i:\,\pi_i<1/2\}}s_i,
\]
with the convention \(h_*=\infty\) when the set is empty, and
\[
C_h\ge0
\quad\Longleftrightarrow\quad
0\le h\le h_*.
\]

The individual crossing times satisfy the sharp spectral enclosure
\[
\frac{2}{\lambda_{n-1}(1-2\pi_i)}
\le
h_i:=2s_i
\le
\frac{2}{\lambda_1(1-2\pi_i)}
\qquad(\pi_i<1/2).
\]
Equality holds throughout when all nonzero eigenvalues are equal.

There is also a complete unconditional-positivity classification for irreducible finite chains. Since
\[
R_s\longrightarrow \mathbf 1\pi^{\mathsf T}
\qquad(s\to\infty),
\]
we have
\[
C_h\longrightarrow 2\mathbf 1\pi^{\mathsf T}-I.
\]
If \(n\ge3\), at least one stationary mass is below \(1/2\), so sufficiently large Crank–Nicolson steps necessarily have a negative diagonal entry. If \(n=2\), every irreducible generator has the form
\[
Q=
\begin{pmatrix}
-a&a\\
b&-b
\end{pmatrix},
\qquad
a,b>0,
\]
and
\[
h_*=
\begin{cases}
\infty,&a=b,\\[2mm]
\dfrac{2}{|a-b|},&a\ne b.
\end{cases}
\]
Thus, apart from the one-state case, the only irreducible finite Markov chain for which Crank–Nicolson is positive for every step size is the balanced two-state chain.

For the complete graph on \(n\ge3\) states with rate \(c>0\) on every directed edge,
\[
q_{ij}=c\quad(i\ne j),
\qquad
q_{ii}=-(n-1)c,
\]
the stationary law is uniform and all nonzero eigenvalues of \(-Q\) equal \(nc\). The threshold is therefore exactly
\[
h_*=\frac{2}{c(n-2)}.
\]

## Assumptions and scope
The matrix \(Q\) is a finite-state continuous-time Markov generator in row convention. The Crank–Nicolson update acts on row probability vectors by right multiplication with \(C_h\). Because \(Q\) commutes with every rational function of \(Q\), the equivalent left/right ordering of the two factors in \(C_h\) is immaterial.

The exact diagonal-resolvent criterion holds for every finite Markov generator, whether reversible or not. Reversibility is used only to prove that every diagonal resolvent entry decreases monotonically and hence that the positivity set is one interval with the displayed spectral formula and bounds.

The unconditional-positivity obstruction for irreducible chains uses only the finite-state resolvent limit and therefore does not require reversibility. Reducible chains are not classified here.

The result concerns entrywise nonnegativity of the end-step matrix. It does not assert stage positivity for a particular Runge–Kutta implementation, nor does it classify nonlinear positivity, strong-stability-preserving radii, or positivity after filtering or projection.

## Proof
Set \(s=h/2\). The Cayley identity gives
\[
C_h
=
(I-sQ)^{-1}(I+sQ)
=
2(I-sQ)^{-1}-I
=
2R_s-I.
\]
For \(s\ge0\), the matrix \(I-sQ\) has positive diagonal entries, nonpositive off-diagonal entries, and is a nonsingular \(M\)-matrix. Hence
\[
R_s\ge0.
\]
Moreover,
\[
(I-sQ)\mathbf 1=\mathbf 1,
\]
so
\[
R_s\mathbf 1=\mathbf 1.
\]
It follows that, for \(i\ne j\),
\[
(C_h)_{ij}=2(R_s)_{ij}\ge0,
\]
whereas
\[
(C_h)_{ii}=2(R_s)_{ii}-1.
\]
This proves the exact general criterion.

For the reversible part, detailed balance gives
\[
DQ=Q^{\mathsf T}D,
\]
so
\[
S=D^{1/2}QD^{-1/2}
\]
is real symmetric. Since
\[
Q=D^{-1/2}SD^{1/2},
\]
we have
\[
R_s
=
D^{-1/2}(I-sS)^{-1}D^{1/2}.
\]
Diagonal similarity leaves diagonal entries unchanged, and the spectral theorem gives
\[
(R_s)_{ii}
=
\sum_{k=0}^{n-1}
\frac{u_{k,i}^2}{1+s\lambda_k}.
\]
Irreducibility makes the zero eigenvalue simple and gives
\[
u_0=(\sqrt{\pi_1},\ldots,\sqrt{\pi_n})^{\mathsf T},
\]
which yields
\[
(R_s)_{ii}
=
\pi_i+
\sum_{k=1}^{n-1}
\frac{u_{k,i}^2}{1+s\lambda_k}.
\]
For \(n>1\),
\[
\sum_{k=1}^{n-1}u_{k,i}^2=1-\pi_i>0,
\]
so differentiation gives
\[
\frac{d}{ds}(R_s)_{ii}
=
-\sum_{k=1}^{n-1}
\frac{\lambda_k u_{k,i}^2}{(1+s\lambda_k)^2}
<0.
\]
The endpoint values are
\[
(R_0)_{ii}=1,
\qquad
\lim_{s\to\infty}(R_s)_{ii}=\pi_i.
\]
The unique-crossing statement and the formula for \(h_*\) follow immediately.

For the spectral enclosure, use
\[
\pi_i+
\frac{1-\pi_i}{1+s\lambda_{n-1}}
\le
(R_s)_{ii}
\le
\pi_i+
\frac{1-\pi_i}{1+s\lambda_1}.
\]
Solving either comparison expression at the level \(1/2\) gives
\[
s=
\frac{1}{\lambda(1-2\pi_i)},
\]
which proves the two-sided bound for \(h_i=2s_i\).

For a general irreducible finite generator, the standard finite-state resolvent limit is
\[
R_s\longrightarrow \mathbf 1\pi^{\mathsf T}.
\]
Therefore
\[
(C_h)_{ii}\longrightarrow 2\pi_i-1.
\]
If \(n\ge3\), not all stationary masses can be at least \(1/2\), so unconditional positivity is impossible. For \(n=2\), direct inversion gives
\[
(R_s)_{11}
=
\frac{1+sb}{1+s(a+b)},
\qquad
(R_s)_{22}
=
\frac{1+sa}{1+s(a+b)}.
\]
Both are at least \(1/2\) exactly when
\[
1-s|a-b|\ge0.
\]
Since \(h=2s\), this yields the two-state formula.

For the complete graph,
\[
-Q=nc(I-P),
\qquad
P=\frac1n\mathbf 1\mathbf 1^{\mathsf T}.
\]
Thus
\[
R_s
=
P+\frac{1}{1+snc}(I-P),
\]
so every diagonal entry equals
\[
\frac1n+\frac{n-1}{n(1+snc)}.
\]
Setting this equal to \(1/2\) gives
\[
s=\frac{1}{c(n-2)},
\]
and hence the displayed \(h_*\).

## Verification
The accompanying `verify.py` uses exact rational arithmetic. It reconstructs finite Markov generators, forms \(R_s=(I-sQ)^{-1}\) by exact Gaussian elimination, and verifies
\[
C_h=2R_s-I,
\qquad
R_s\mathbf 1=\mathbf 1,
\qquad
C_h\mathbf 1=\mathbf 1.
\]
For several rational reversible generators it checks that every off-diagonal Crank–Nicolson entry is nonnegative and that entrywise positivity is equivalent to the diagonal \(1/2\) test.

The checker verifies the two-state threshold algebra exactly for many rational rate pairs. It also verifies, for complete graphs of sizes \(3\) through \(20\), that the exact threshold is
\[
h_*=\frac{2}{c(n-2)}
\]
and that the threshold step has zero diagonal while smaller and larger rational test steps lie on the predicted sides.

The all-dimensional reversible spectral theorem, strict monotonicity, and finite-state limiting classification are proved analytically above rather than inferred from the finite replay.

## Relationship to prior work
Horváth gives a general positivity theory for Runge–Kutta methods and proves that the positivity radius equals the absolute-monotonicity radius. In particular, the paper explicitly records positivity radius \(2\) for the implicit trapezoidal rule. That is a problem-class worst-case statement and is prior work; the general Runge–Kutta positivity framework is not claimed here.

Fallat and Tsatsomeros study Cayley transforms of matrix positivity classes. Their Lemma 2.2 contains the matrix identity
\[
I+C(A)=2(I+A)^{-1},
\]
and their Section 4 studies Cayley transforms of \(M\)-matrices. Thus the Cayley/resolvent algebra used at the beginning of the proof is also prior work.

The present result specializes to Markov generators but asks a different sharp question: for one fixed generator, exactly when is its Crank–Nicolson end-step matrix stochastic and entrywise nonnegative? The answer reduces the full matrix question to resolvent return diagonals and, under reversibility, yields a complete one-interval threshold law, statewise spectral bounds, an unconditional-positivity classification, and closed thresholds for the two-state and complete-graph families.

The fixed-generator threshold can substantially exceed a problem-class positivity-radius bound and can even be infinite for the balanced two-state chain. The complete-graph family gives a simple chain-specific comparison:
\[
h_*=\frac{2}{c(n-2)},
\]
whereas the elementary sufficient condition obtained by forcing \(I+hQ/2\ge0\) is only
\[
h\le\frac{2}{c(n-1)}.
\]

## Limitations
The result does not classify positivity windows for nonreversible generators after the first loss of positivity; without reversibility, a resolvent diagonal need not be represented by a positive mixture of real scalar resolvents, so the single-crossing argument is unavailable.

The finite-state Markov-chain and matrix-Cayley literatures are broad. A specialized source may contain the same reversible return-resolvent threshold under stochastic-matrix, uniformization, or Cayley-transform terminology. Searches under those aliases did not locate an implication-equivalent statement, but this remains the principal originality risk.

The threshold concerns exact arithmetic. Near \(h_*\), floating-point roundoff can perturb entries that are mathematically zero.

## References
1. Zoltán Horváth, *Positivity of Runge–Kutta and Diagonally Split Runge–Kutta Methods*, Applied Numerical Mathematics 28 (1998), 309--326, DOI: 10.1016/S0168-9274(98)00050-6.
2. Shaun M. Fallat and Michael J. Tsatsomeros, *On the Cayley Transform of Positivity Classes of Matrices*, Electronic Journal of Linear Algebra 9 (2002), 190--196, DOI: 10.13001/1081-3810.1086.
