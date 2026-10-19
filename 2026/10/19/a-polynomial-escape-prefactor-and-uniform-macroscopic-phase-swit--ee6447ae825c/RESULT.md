# A polynomial escape prefactor and uniform macroscopic phase-switching law for the golden-mean double-pole hole

## Finding

Let \(T:[0,1)\to[0,1)\) be \(T(x)=2x\bmod1\), let the absorbing hole be \(H=[3/4,5/6]\), and initialize \(X\) uniformly on \([0,1)\). Write \(\mathcal S_n=\{x:T^j(x)\notin H\text{ for }0\le j<n\}\) and \(p_n=\operatorname{Leb}(\mathcal S_n)\), for integers \(n\ge1\). Set \(r_+=(1+\sqrt5)/4\) and \(r_-=(1-\sqrt5)/4\). Then, **exactly for all \(n\ge1\)**,

\[
p_n=\left(\frac{2+\sqrt5}{30}n+\frac12+\frac{11\sqrt5}{50}\right)r_+^n+
\left(\frac{2-\sqrt5}{30}n+\frac12-\frac{11\sqrt5}{50}\right)r_-^n.
\]

In particular, \(p_n\sim((2+\sqrt5)/30)\,n r_+^n\), with escape rate \(-\log r_+\) but a **nonzero linear prefactor**. The exact generating function is

\[
\sum_{n\ge1}p_n z^n=\frac{z(44-4z-15z^2-3z^3)}{3(4-2z-z^2)^2}.
\]

There is also a conditional macroscopic law not determined by the escape rate. Classify the alive states \(A=(0,1/3)\), \(C=(1/2,2/3)\) as the *upstream phase*, and \(B=(1/3,1/2)\), \(D=(2/3,3/4)\), \(E=(5/6,1)\) as the *downstream phase*. Let \(J_n\) be the first time \(0\le j<n\) with \(T^j(X)\) in the downstream phase, with \(J_n=n\) when no such time occurs. Under Lebesgue measure conditioned on \(\mathcal S_n\),

\[
\frac{J_n}{n}\ \Longrightarrow\ \operatorname{Uniform}[0,1].
\]

In the same conditioning, the initial partition location converges to the distribution supported on \(A,C\) with probabilities \(\gamma/(\gamma+1)\) and \(1/(\gamma+1)\), respectively, where \(\gamma=(1+\sqrt5)/2\).

## Assumptions and scope

Only Lebesgue initial probability, the full doubling map, the single fixed absorbing hole \([3/4,5/6]\), and the first \(n\) observations \(j=0,\ldots,n-1\) are considered. Interval endpoints and their preimages have Lebesgue measure zero and may be assigned arbitrarily. The survival probability counts *all* initial states avoiding the hole; the phase label records which of the five Markov partition intervals contains an alive iterate. The phase-switch statistic is defined only in the conditional law given survival through time \(n-1\).

## Proof

**1. Exact Markov partition.** The complement of the hole splits, up to endpoints, into the five intervals \(A,B,C,D,E\) in the order displayed above, of respective lengths \((1/3,1/6,1/6,1/12,1/6)\). The restrictions of \(T\) to these intervals are one-to-one with slope \(2\). Directly applying \(T\) gives the complete surviving transition graph

\[
A\to A,B,C;\quad B\to D,E;\quad C\to A;\quad D\to B;\quad E\to D,E.
\]

In the order \((A,B,C,D,E)\) its adjacency matrix is

\[
M=\begin{pmatrix}
1&1&1&0&0\\
0&0&0&1&1\\
1&0&0&0&0\\
0&1&0&0&0\\
0&0&0&1&1
\end{pmatrix}.
\]

Because every full target interval has an inverse branch of length exactly one half inside each allowed source interval, the survivor mass with \(n\) observations and an initial state in interval \(i\) is the \(i\)-th entry of \(2^{1-n}M^{n-1}\ell\), where \(\ell=(1/3,1/6,1/6,1/12,1/6)^{\mathsf T}\). Hence

\[
p_n=2^{1-n}\mathbf1^{\mathsf T}M^{n-1}\ell.
\]

**2. Exact generating function and coefficients.** Summing the geometric matrix series gives

\[
F(z)=\sum_{n\ge1}p_n z^n=z\mathbf1^{\mathsf T}(I-zM/2)^{-1}\ell.
\]

A rational inverse (or Gaussian elimination) evaluates it as the displayed rational function. In particular, \(\det(tI-M)=t(t^2-t-1)^2\). The denominator \((4-2z-z^2)^2\) has double zeros at \(z=1/r_+\) and \(z=1/r_-\). Its partial fractions, followed by coefficient extraction, give the claimed exact formula for every \(n\ge1\). The leading \(n r_+^n\) term has coefficient \((2+\sqrt5)/30>0\); the other exponential satisfies \(|r_-|<r_+\). This proves the sharp survival asymptotic.

**3. One-way transition and conditional phase time.** Permute the states into \((A,C\mid B,D,E)\). In this ordering the adjacency matrix becomes block upper triangular, with blocks

\[
U=\begin{pmatrix}1&1\\1&0\end{pmatrix},\qquad
C_*=\begin{pmatrix}1&0&0\\0&0&0\end{pmatrix},\qquad
V=\begin{pmatrix}0&1&1\\1&0&0\\0&1&1\end{pmatrix}.
\]

Both \(U\) and \(V\) are primitive nonnegative matrices. Their simple common Perron eigenvalue is \(\gamma=(1+\sqrt5)/2\). Every other eigenvalue in their spectra has modulus strictly smaller than \(\gamma\). The graph admits only a one-way move from \(A,C\) to \(B,D,E\), and that move uses \(A\to B\).

With \(u=(1,1)^{\mathsf T}\), \(\ell_V=(1/6,1/12,1/6)^{\mathsf T}\), the unnormalized probability of \(J_n=j\) and \(\mathcal S_n\), for \(1\le j<n\), is exactly

\[
2^{1-n}u^{\mathsf T}U^{j-1}C_*V^{n-j-1}\ell_V.
\]

Perron projections \(\Pi_U\) and \(\Pi_V\) therefore give, uniformly whenever both \(j\) and \(n-j\) tend to infinity,

\[
\Pr(J_n=j,\mathcal S_n)=2^{1-n}\gamma^{n-2}\bigl(c+o(1)\bigr),
\quad c=u^{\mathsf T}\Pi_U C_*\Pi_V\ell_V
=\frac{11}{120}+\frac{\sqrt5}{24}>0.
\]

Indeed choose Perron right vectors \((\gamma,1)^{\mathsf T}\), \((\gamma,1,\gamma)^{\mathsf T}\) and left vectors \((\gamma,1)^{\mathsf T}\), \((1,\gamma,\gamma)^{\mathsf T}\); normalization by their scalar products yields the displayed \(c\). The contributions from starting downstream (\(J_n=0\)) or never switching (\(J_n=n\)) are only \(O((\gamma/2)^n)\). For any fixed \(K\), at most \(2K\) switch indices are within \(K\) of an endpoint, and all their individual masses are uniformly \(O((\gamma/2)^n)\); thus they carry vanishing conditional probability after \(n\to\infty\). In the remaining bulk, Perron projection errors are bounded by a constant times a geometric power of the distance from the nearer end. Riemann sums over indices \(j/n\), divided by \(p_n\sim((2+\sqrt5)/30)nr_+^n\), therefore converge to Lebesgue integration on \([0,1]\). The constants agree because \(2c/\gamma^2=(2+\sqrt5)/30\). This proves the uniform law.

**4. Initial-location law.** In the upstream block, the vector \(M^{n-1}\ell\) has its dominant order-\(n\gamma^{n-1}\) contribution parallel to the Perron right eigenvector \((\gamma,1)^{\mathsf T}\), while its downstream coordinates are only \(O(\gamma^{n-1})\). After normalization by their sum, the initial weights tend to \(\gamma/(\gamma+1)\) on \(A\) and \(1/(\gamma+1)\) on \(C\).

## Verification

The accompanying standalone `verify.py` executes exact rational checks of the \(5\)-state matrix against the rational generating-function recurrence for \(n=1,\dots,30\), independently computes the intervals surviving up to \(12\) observations by iterated rational affine inverse images, and checks eight finite phase-switch decompositions against the exact survivor mass. Run `python verify.py`. All checked identities are finite; the general \(n\) statements and weak limit follow from the proof above, not from finite testing.

## Relationship to prior work

Bandtlow and Rugh, *Entropy-continuity for interval maps with holes*, arXiv:1510.06043 (first public 2015-10-20), Section 6.2, introduced precisely the moving-hole example \([3/4,5/6]\) and identified its double leading eigenvalue \(\gamma\), defective Jordan structure and entropy \(\log\gamma\). That spectral observation and the transition graph are prior mathematics and are not claimed new. The present results concern the **Lebesgue survival probability with an evaluated all-time prefactor**, and the **conditional macroscopic location of the unique transition between equal-entropy communicating classes**. Those statistical statements do not follow from the value of entropy alone, and were not stated in the inspected sections of the motivating paper. Standard Perron–Frobenius and finite-state matrix methods are used as established tools.

## Limitations

The calculation depends on the exact Markov geometry of this rational hole; it does not prove similar formulas for arbitrary sliding holes. The uniform switch law is a distributional asymptotic under conditional Lebesgue initialization, not an assertion of samplewise convergence along a single orbit. The double leading eigenvalue itself and the general possibility of polynomial factors for reducible matrices are prior facts. Earlier treatments of this exact hole's survival statistics or generalized conditioned path decompositions could establish related statements; historical priority is not independently certified.

## References

1. O. F. Bandtlow and H. H. Rugh, *Entropy-continuity for interval maps with holes*, arXiv:1510.06043v1 (2015), especially Section 6.2, https://arxiv.org/abs/1510.06043.
2. A. Ferguson and M. Pollicott, *Escape rates for Gibbs measures*, Ergodic Theory and Dynamical Systems 32 (2012), 961–988, https://doi.org/10.1017/S0143385711000058 (general escape-rate context; not used as a theorem).
